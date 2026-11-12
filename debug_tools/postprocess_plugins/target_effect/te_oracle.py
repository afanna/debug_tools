"""倒计时目标语义 Oracle：只从请求参数、设备参考时间和显式期望推导。

批跑产物里的数据模型只是占位值（例如 ``days: 3``），不参与任何期望比对。
Oracle 只使用 ``candidateDataBindings[].arguments`` 与 ``deviceInfo.time``，
或数据集作者显式声明的 ``expectations.json``。
"""

from __future__ import annotations

import calendar
import json
from dataclasses import dataclass, field
from datetime import date, timedelta
from pathlib import Path
from typing import Any

CAPABILITY_ID = "GetDateCounter"
RELATION_LEFT = "还剩"
RELATION_TODAY = "就是今天"
RELATION_PAST = "已过"
PROVENANCE_EXPLICIT = "explicit"
PROVENANCE_DERIVED = "derived"
PROVENANCE_INFERRED = "inferred"
PROVENANCE_AMBIGUOUS = "ambiguous"
GATE_PROVENANCE = {PROVENANCE_EXPLICIT, PROVENANCE_DERIVED}
DEFAULT_TIMEZONE = "Asia/Shanghai"
DATE_FORMAT = "%Y/%m/%d"


@dataclass
class Oracle:
    """一个样本的期望目标语义。gate=False 时只展示，不参与自动失败。"""

    sample_id: str
    scenario: str = "unknown"
    timezone: str = DEFAULT_TIMEZONE
    reference_date: str | None = None
    target_date: str | None = None
    days: int | None = None
    relation_text: str | None = None
    target_date_text: str | None = None
    write_result_to: str | None = None
    fields: list[str] = field(default_factory=list)
    arguments: dict[str, Any] = field(default_factory=dict)
    gate: bool = False
    provenance: dict[str, str] = field(default_factory=dict)
    notes: list[str] = field(default_factory=list)

    def values(self) -> dict[str, Any]:
        payload: dict[str, Any] = {}
        if self.days is not None:
            payload["days"] = self.days
        if self.relation_text is not None:
            payload["relationText"] = self.relation_text
        if self.target_date_text is not None:
            payload["targetDateText"] = self.target_date_text
        if self.target_date is not None:
            payload["targetDate"] = self.target_date
        return payload

    def card_values(self) -> dict[str, Any]:
        """卡面可绑定的输出字段；targetDate 只是工具入参，默认不参与比对。"""
        values = self.values()
        declared = {
            str(item).strip("/").split("/")[0]
            for item in self.fields
            if isinstance(item, str) and item.strip("/")
        }
        names = declared or {"days", "relationText", "targetDateText"}
        return {key: value for key, value in values.items() if key in names}

    def as_dict(self) -> dict[str, Any]:
        return {
            "sampleId": self.sample_id,
            "scenario": self.scenario,
            "timezone": self.timezone,
            "referenceDate": self.reference_date,
            "targetDate": self.target_date,
            "expectedDays": self.days,
            "expectedRelationText": self.relation_text,
            "expectedTargetDateText": self.target_date_text,
            "writeResultTo": self.write_result_to,
            "fields": list(self.fields),
            "arguments": dict(self.arguments),
            "gate": self.gate,
            "provenance": dict(self.provenance),
            "notes": list(self.notes),
        }


def read_json_object(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"JSON 根节点必须为对象：{path.name}")
    return value


def load_request(attempt_dir: Path) -> dict[str, Any]:
    """读取最终尝试的原始请求；缺失时返回空对象，由调用方判定 L0 失败。"""
    for candidate in (attempt_dir / "request.json", attempt_dir / "blocks" / "request.json"):
        if candidate.is_file():
            return read_json_object(candidate)
    return {}


def request_section(request: dict[str, Any]) -> dict[str, Any]:
    """请求正文既可能在顶层，也可能包在 ``content`` 中。"""
    content = request.get("content")
    if isinstance(content, dict):
        merged = dict(request)
        merged.update(content)
        return merged
    return request


def parse_reference_date(device_info: dict[str, Any] | None) -> date | None:
    """``deviceInfo.time`` 为 17 位本地时间串，前 8 位是 YYYYMMDD。"""
    if not isinstance(device_info, dict):
        return None
    raw = device_info.get("time")
    if not isinstance(raw, str) or len(raw) < 8 or not raw[:8].isdigit():
        return None
    try:
        return date(int(raw[0:4]), int(raw[4:6]), int(raw[6:8]))
    except ValueError:
        return None


def parse_iso_date(value: Any) -> date | None:
    if not isinstance(value, str) or len(value) < 10:
        return None
    try:
        return date.fromisoformat(value[:10])
    except ValueError:
        return None


def load_expectations(path: Path) -> dict[str, dict[str, Any]]:
    """读取数据集作者声明的期望值；没有文件时返回空表。"""
    if not path.is_file():
        return {}
    value = read_json_object(path)
    samples = value.get("samples")
    if not isinstance(samples, dict):
        raise ValueError("expectations.json 缺少 samples 对象")
    result: dict[str, dict[str, Any]] = {}
    for sample_id, item in samples.items():
        if isinstance(item, dict):
            result[str(sample_id)] = item
    return result


def _date_text(value: date) -> str:
    return value.strftime(DATE_FORMAT)


def _relation(delta: int) -> str:
    if delta > 0:
        return RELATION_LEFT
    if delta == 0:
        return RELATION_TODAY
    return RELATION_PAST


def _next_weekly(anchor: date, reference: date) -> tuple[date, list[str]]:
    steps = (anchor.weekday() - reference.weekday()) % 7
    return reference + timedelta(days=steps), []


def _next_monthly(anchor: date, reference: date) -> tuple[date | None, list[str]]:
    year, month = reference.year, reference.month
    for _ in range(0, 14):
        last_day = calendar.monthrange(year, month)[1]
        if anchor.day <= last_day:
            candidate = date(year, month, anchor.day)
            if candidate >= reference:
                return candidate, []
        month += 1
        if month > 12:
            month = 1
            year += 1
    return None, ["按月重复在 14 个月内没有有效日期"]


def _next_yearly(anchor: date, reference: date) -> tuple[date | None, list[str]]:
    for year in (reference.year, reference.year + 1, reference.year + 2):
        if anchor.month == 2 and anchor.day == 29 and not calendar.isleap(year):
            continue
        try:
            candidate = date(year, anchor.month, anchor.day)
        except ValueError:
            continue
        if candidate >= reference:
            return candidate, []
    return None, ["按年重复在 3 年内没有有效日期"]


def _next_interval(
    anchor: date,
    reference: date,
    interval: int,
) -> tuple[date | None, list[str]]:
    if interval <= 0:
        return None, ["重复间隔必须为正数"]
    if anchor >= reference:
        return anchor, []
    span = (reference - anchor).days
    steps = (span + interval - 1) // interval
    return anchor + timedelta(days=steps * interval), []


def _repeat_interval(repeat: dict[str, Any]) -> int:
    interval = repeat.get("interval")
    if isinstance(interval, bool):
        return 1
    if isinstance(interval, int) and interval > 0:
        return interval
    return 1


def _scenario_for(arguments: dict[str, Any]) -> str:
    calendar_name = arguments.get("calendar")
    repeat = arguments.get("repeat")
    if isinstance(calendar_name, str) and calendar_name.lower() == "lunar":
        unit = repeat.get("unit") if isinstance(repeat, dict) else None
        return f"lunar_{unit}" if isinstance(unit, str) else "lunar_once"
    if isinstance(repeat, dict):
        unit = repeat.get("unit")
        if isinstance(unit, str) and unit:
            return f"repeat_{unit}"
        return "repeat_unknown"
    return "once"


def build_oracle(
    sample_id: str,
    request: dict[str, Any],
    *,
    override: dict[str, Any] | None = None,
    repeat_gates: bool = False,
    today_counts_as_next: bool = False,
    timezone: str = DEFAULT_TIMEZONE,
) -> Oracle:
    """推导单个样本的目标语义；无法确定时降级为仅展示（gate=False）。"""
    body = request_section(request)
    bindings = body.get("candidateDataBindings")
    binding = _first_binding(bindings)
    oracle = Oracle(sample_id=sample_id, timezone=timezone)
    if binding is None:
        oracle.notes.append("请求中没有 GetDateCounter 数据绑定")
        oracle.provenance = {"targetDate": PROVENANCE_AMBIGUOUS}
        return _apply_override(oracle, override)

    arguments = binding.get("arguments")
    if not isinstance(arguments, dict):
        arguments = {}
    oracle.arguments = dict(arguments)
    write_to = binding.get("writeResultTo")
    if isinstance(write_to, str) and write_to.strip():
        oracle.write_result_to = write_to.strip()
    fields = binding.get("candidateOutputFields")
    if isinstance(fields, list):
        oracle.fields = [str(item) for item in fields if isinstance(item, str)]

    reference = parse_reference_date(request.get("deviceInfo"))
    if reference is None:
        oracle.notes.append("缺少可解析的 deviceInfo.time 参考时间")
    else:
        oracle.reference_date = reference.isoformat()

    target = parse_iso_date(arguments.get("targetDate"))
    if target is None:
        oracle.notes.append("缺少可解析的 targetDate")
    oracle.scenario = _scenario_for(arguments)
    if reference is None or target is None:
        oracle.provenance = {"targetDate": PROVENANCE_AMBIGUOUS}
        return _apply_override(oracle, override)

    gate, resolved, notes = _resolve_target(
        oracle.scenario,
        target,
        reference,
        arguments,
        repeat_gates=repeat_gates,
        today_counts_as_next=today_counts_as_next,
    )
    oracle.notes.extend(notes)
    if resolved is not None:
        delta = (resolved - reference).days
        oracle.target_date = resolved.isoformat()
        oracle.days = abs(delta)
        oracle.relation_text = _relation(delta)
        oracle.target_date_text = _date_text(resolved)
        provenance = PROVENANCE_DERIVED if gate else PROVENANCE_AMBIGUOUS
        oracle.provenance = {
            "targetDate": PROVENANCE_EXPLICIT,
            "days": provenance,
            "relationText": provenance,
            "targetDateText": provenance,
        }
    oracle.gate = gate and resolved is not None
    return _apply_override(oracle, override)


def _first_binding(bindings: Any) -> dict[str, Any] | None:
    if not isinstance(bindings, list):
        return None
    for item in bindings:
        if isinstance(item, dict) and item.get("capabilityId") == CAPABILITY_ID:
            return item
    return None


def _resolve_target(
    scenario: str,
    anchor: date,
    reference: date,
    arguments: dict[str, Any],
    *,
    repeat_gates: bool,
    today_counts_as_next: bool,
) -> tuple[bool, date | None, list[str]]:
    notes: list[str] = []
    if scenario == "once":
        return True, anchor, notes
    if scenario.startswith("lunar"):
        notes.append("农历日期需日历库或人工确认，本次不自动判定目标日")
        return False, None, notes
    repeat = arguments.get("repeat")
    if not isinstance(repeat, dict):
        return False, anchor, ["重复参数缺失，无法推导下一次触发"]
    unit = repeat.get("unit")
    if unit == "week":
        candidate, extra = _next_weekly(anchor, reference)
    elif unit == "month":
        candidate, extra = _next_monthly(anchor, reference)
    elif unit == "year":
        candidate, extra = _next_yearly(anchor, reference)
    elif unit == "day":
        candidate, extra = _next_interval(anchor, reference, _repeat_interval(repeat))
    else:
        notes.append(f"未注册的重复单位：{unit}")
        return False, None, notes
    notes.extend(extra)
    if candidate is None:
        return False, None, notes
    if candidate == reference and not today_counts_as_next:
        notes.append("下一次触发日与参考日相同，需确认“今天是否算下一次”")
        return False, candidate, notes
    if not repeat_gates:
        notes.append("重复场景默认只展示期望值，开启 repeatGates 后才参与自动失败")
        return False, candidate, notes
    return True, candidate, notes


def _apply_override(oracle: Oracle, override: dict[str, Any] | None) -> Oracle:
    """显式期望覆盖推导值；仅 explicit/derived 允许参与门禁。"""
    if not isinstance(override, dict):
        return oracle
    provenance = override.get("provenance")
    if not isinstance(provenance, dict):
        provenance = {}
    days = _int_or_none(override.get("expectedDays"))
    target_text = override.get("expectedTargetDateText")
    relation = override.get("expectedRelationText")
    target_date = override.get("expectedTargetDate")
    if days is not None:
        oracle.days = days
    if isinstance(target_text, str) and target_text.strip():
        oracle.target_date_text = target_text.strip()
    if isinstance(relation, str) and relation.strip():
        oracle.relation_text = relation.strip()
    if isinstance(target_date, str) and target_date.strip():
        oracle.target_date = target_date.strip()
    scenario = override.get("scenario")
    if isinstance(scenario, str) and scenario.strip():
        oracle.scenario = scenario.strip()
    timezone_value = override.get("timezone")
    if isinstance(timezone_value, str) and timezone_value.strip():
        oracle.timezone = timezone_value.strip()
    reference = override.get("referenceDate")
    if isinstance(reference, str) and reference.strip():
        oracle.reference_date = reference.strip()
    if provenance:
        oracle.provenance = {str(key): str(value) for key, value in provenance.items()}
    levels = set(oracle.provenance.values())
    oracle.gate = bool(levels) and levels <= GATE_PROVENANCE and all(
        _has_value(oracle, key) for key in oracle.provenance
    )
    return oracle


def _has_value(oracle: Oracle, key: str) -> bool:
    mapping = {
        "days": oracle.days,
        "relationText": oracle.relation_text,
        "targetDateText": oracle.target_date_text,
        "targetDate": oracle.target_date,
        "expectedDays": oracle.days,
        "expectedRelationText": oracle.relation_text,
    }
    if key in mapping:
        return mapping[key] is not None
    return True


def _int_or_none(value: Any) -> int | None:
    if isinstance(value, bool):
        return None
    if isinstance(value, int):
        return value
    if isinstance(value, float) and value.is_integer():
        return int(value)
    return None


def injected_jsonl(source: str, oracle: Oracle) -> tuple[str, list[dict[str, Any]]]:
    """在原始 genui 末尾追加诊断用 updateDataModel，返回文本与注入记录。

    只改内存/派生产物，不回写批跑目录；注入行单独记录，报告可区分
    “这是诊断注入，不是原始运行数据”。
    """
    rows: list[dict[str, Any]] = []
    version = "v0.9"
    surface_id = "surface_card"
    for line in source.splitlines():
        if not line.strip():
            continue
        try:
            row = json.loads(line)
        except ValueError:
            continue
        if not isinstance(row, dict):
            continue
        rows.append(row)
        if isinstance(row.get("version"), str):
            version = row["version"]
        surface = row.get("createSurface")
        if isinstance(surface, dict) and isinstance(surface.get("surfaceId"), str):
            surface_id = surface["surfaceId"]
    if oracle.write_result_to is None or not oracle.card_values():
        return source, []
    injected: list[dict[str, Any]] = []
    for key, value in oracle.card_values().items():
        path = f"{oracle.write_result_to.rstrip('/')}/{key}"
        row = {
            "version": version,
            "updateDataModel": {"surfaceId": surface_id, "path": path, "value": value},
        }
        rows.append(row)
        injected.append({"path": path, "value": value})
    text = "\n".join(json.dumps(row, ensure_ascii=False) for row in rows) + "\n"
    return text, injected
