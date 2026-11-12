"""把倒计时评测的规则结论折算成 100 分制总分与维度分。

评分只消费 ``RuleResult`` 的确定性结论，不引入模型或人工判断：

- 目标语义（25）：仅当期望日期来自作者显式声明时才计分；由 mock 设备时间
  推导的期望只做参考，整维不适用，避免把 mock 数值当成标准答案；
- 可见性（37.5）：``VIS.*`` 规则通过率；
- 规范符合（37.5）：``countdown-card-spec-v1`` 的 ``SPEC.*`` 规则通过率；
- 素材渲染、图标、点阵间距：``ASSET.*`` 等只做诊断，不参与计分。

三个维度的权重固定为 25 + 37.5 + 37.5 = 100，不适用维度记 0 分并保留原因，
分母不随适用性收缩，因此维度分相加就是总分。待复核按半通过计分。L0 失败时
总分记 0。显式期望的目标语义未通过时总分封顶 59.9，避免“样式好看但数字错误”
的卡片得高分。
非 Pixso 主题（融合/渐变/纯色/黑字）不做规范门禁，规范维度整维不适用。
"""

from __future__ import annotations

from typing import Any

DIMENSION_ORDER = (
    ("target", "目标语义", 25.0),
    ("visibility", "可见性", 37.5),
    ("spec", "规范符合", 37.5),
)
TARGET_RULE_BY_FIELD = {
    "days": "TARGET.DAYS_MISMATCH",
    "relationText": "TARGET.RELATION_TEXT_MISMATCH",
    "targetDateText": "TARGET.VISIBLE_EXPECTATION_MISSING",
}
TARGET_FIELD_KEYS = ("days", "relationText", "targetDateText")
FIELD_LABELS = {
    "days": "天数",
    "relationText": "关系文案",
    "targetDateText": "期望文本可见",
}
STATUS_VALUE = {
    "pass": 1.0,
    "fail": 0.0,
    "pending": 0.5,
}
DIAGNOSTIC_RULES = {
    "ASSET.FILE_MISSING",
    "ASSET.RENDERED",
    "SPEC.THEME_ELIGIBLE",
    "SPEC.USER_PREFERENCE",
    "SPEC.ICON",
    "SPEC.BG_FIT",
    "SPEC.PATTERN_PITCH",
    "SPEC.UNIT_BASELINE",
}
FULL_WEIGHT = 100.0
TARGET_CAP = 59.9
BANDS = (
    (90.0, "优秀"),
    (75.0, "良好"),
    (60.0, "及格"),
    (0.0, "不合格"),
)


def score_sample(results: list[dict[str, Any]], oracle: dict[str, Any]) -> dict[str, Any]:
    """返回 ``total``、``band`` 与各维度的得分明细。

    每个维度同时给出 ``items``：该维度下逐条规则的得分权重与扣分，
    让使用方能看到分数具体扣在哪条规则上。
    """
    rows = [item for item in results if isinstance(item, dict)]
    by_rule: dict[str, list[float]] = {}
    for item in rows:
        rule = str(item.get("rule") or "")
        value = STATUS_VALUE.get(str(item.get("status") or ""))
        if not rule or value is None:
            continue
        by_rule.setdefault(rule, []).append(value)
    fatal = any(
        rule.startswith("L0.") and any(value == 0.0 for value in values)
        for rule, values in by_rule.items()
    )
    if fatal:
        dimensions = [
            _empty_dimension(key, label, weight, "L0 失败")
            for key, label, weight in DIMENSION_ORDER
        ]
        return _pack(
            0.0,
            dimensions,
            True,
            "",
            {"targetGated": False, "availableWeight": FULL_WEIGHT},
        )

    info = _rule_info(rows)
    target_checks = (
        _target_checks(by_rule, oracle, info) if target_applicable(oracle) else []
    )
    checks = {
        "target": target_checks,
        "visibility": _prefix_checks(by_rule, "VIS.", info),
        "spec": _prefix_checks(by_rule, "SPEC.", info),
    }
    dimensions: list[dict[str, Any]] = []
    for key, label, weight in DIMENSION_ORDER:
        values = checks[key]
        if not values:
            dimensions.append(
                _empty_dimension(key, label, weight, _empty_reason(key, oracle))
            )
            continue
        dimensions.append(_dimension(key, label, weight, values))
    available = sum(float(item["max"]) for item in dimensions)
    earned = sum(float(item["score"] or 0.0) for item in dimensions)
    total = round(earned, 1) if available else 0.0
    target = next((item for item in dimensions if item["key"] == "target"), None)
    gated = bool(oracle.get("gate"))
    capped = bool(
        gated
        and target is not None
        and target.get("applicable")
        and float(target.get("ratio") or 0) < 100.0
    )
    if capped:
        total = min(total, TARGET_CAP)
    note = "目标语义未通过，总分封顶 59.9" if capped else ""
    return _pack(
        total,
        dimensions,
        False,
        note,
        {
            "targetGated": gated,
            "availableWeight": available,
            "capped": capped,
        },
    )


def _dimension(
    key: str,
    label: str,
    weight: float,
    checks: list[dict[str, Any]],
) -> dict[str, Any]:
    """按规则等权折算一个维度，并给出每条规则的扣分。"""
    values = [float(item["value"]) for item in checks]
    ratio = sum(values) / len(values)
    passed = sum(1 for value in values if value == 1.0)
    pending = sum(1 for value in values if value == 0.5)
    unit = weight / len(values)
    items: list[dict[str, Any]] = []
    for check in checks:
        value = float(check["value"])
        items.append(
            {
                "rule": str(check.get("rule") or ""),
                "status": str(check.get("status") or ""),
                "value": round(value, 2),
                "weight": round(unit, 1),
                "deduction": round(unit * (1.0 - value), 1),
                "expected": str(check.get("expected") or ""),
                "actual": str(check.get("actual") or ""),
            }
        )
    return {
        "key": key,
        "label": label,
        "max": weight,
        "score": round(weight * ratio, 1),
        "ratio": round(ratio * 100, 1),
        "checks": len(values),
        "passed": passed,
        "pending": pending,
        "applicable": True,
        "items": items,
    }


def _rule_info(rows: list[dict[str, Any]]) -> dict[str, dict[str, str]]:
    """收集每条规则的期望值与前两个非空实测值，便于说明扣分原因。"""
    expected: dict[str, str] = {}
    actuals: dict[str, list[str]] = {}
    for item in rows:
        rule = str(item.get("rule") or "")
        if not rule:
            continue
        if not expected.get(rule):
            expected[rule] = str(item.get("expected") or "")
        bucket = actuals.setdefault(rule, [])
        actual = str(item.get("actual") or "")
        if actual and actual not in bucket and len(bucket) < 2:
            bucket.append(actual)
    info: dict[str, dict[str, str]] = {}
    for rule in actuals:
        info[rule] = {
            "expected": expected.get(rule) or "",
            "actual": "；".join(actuals.get(rule) or []),
        }
    return info


def target_applicable(oracle: dict[str, Any]) -> bool:
    """只有作者显式声明的期望才参与目标语义计分。

    ``deviceInfo.time`` 是批跑时的 mock 参考时间，按它推导出的天数不能当作
    标准答案；这类样本的目标语义规则降级为参考项，不扣分也不影响结论。
    """
    provenance = oracle.get("provenance")
    if not isinstance(provenance, dict):
        return False
    names = [name for name in TARGET_FIELD_KEYS if name in provenance]
    if not names:
        return False
    return all(str(provenance.get(name) or "") == "explicit" for name in names)


def _target_checks(
    by_rule: dict[str, list[float]],
    oracle: dict[str, Any],
    info: dict[str, dict[str, str]],
) -> list[dict[str, Any]]:
    """只按期望字段计分；占位数据与工具入参不参与。"""
    fields = oracle.get("fields")
    if not isinstance(fields, list):
        return []
    checks: list[dict[str, Any]] = []
    missing = _missing_fields(by_rule)
    for raw in fields:
        field_name = str(raw).strip("/").split("/")[0]
        rule = TARGET_RULE_BY_FIELD.get(field_name)
        if rule is None:
            continue
        if rule in by_rule:
            values = by_rule[rule]
            value = sum(values) / len(values)
            meta = info.get(rule) or {}
            checks.append(
                {
                    "rule": rule,
                    "status": _status_of(value),
                    "value": value,
                    "expected": str(meta.get("expected") or ""),
                    "actual": str(meta.get("actual") or ""),
                }
            )
            continue
        if field_name in missing:
            checks.append(
                {
                    "rule": rule,
                    "status": "fail",
                    "value": 0.0,
                    "expected": FIELD_LABELS.get(field_name, field_name),
                    "actual": "绑定缺失",
                }
            )
    return checks


def _missing_fields(by_rule: dict[str, list[float]]) -> set[str]:
    if not any(value < 1.0 for value in by_rule.get("TARGET.BINDING_MISSING", [])):
        return set()
    return set(TARGET_RULE_BY_FIELD)


def _prefix_checks(
    by_rule: dict[str, list[float]],
    prefix: str,
    info: dict[str, dict[str, str]],
) -> list[dict[str, Any]]:
    checks: list[dict[str, Any]] = []
    for rule, items in by_rule.items():
        if not rule.startswith(prefix):
            continue
        if rule in DIAGNOSTIC_RULES:
            continue
        value = sum(items) / len(items)
        meta = info.get(rule) or {}
        checks.append(
            {
                "rule": rule,
                "status": _status_of(value),
                "value": value,
                "expected": str(meta.get("expected") or ""),
                "actual": str(meta.get("actual") or ""),
            }
        )
    return checks


def _status_of(value: float) -> str:
    if value >= 1.0:
        return "pass"
    if value >= 0.5:
        return "pending"
    return "fail"


def _empty_reason(key: str, oracle: dict[str, Any]) -> str:
    if key == "target":
        if oracle.get("provenance"):
            return "期望日期由 mock 设备时间推导，仅作参考；目标语义记 0 分"
        return "未提供显式期望；目标语义记 0 分"
    if key == "spec":
        return str(oracle.get("specExcludedReason") or "无适用检查；规范符合记 0 分")
    return "无适用检查"


def _empty_dimension(key: str, label: str, weight: float, reason: str) -> dict[str, Any]:
    return {
        "key": key,
        "label": label,
        "max": weight,
        "score": 0.0,
        "ratio": 0.0,
        "checks": 0,
        "passed": 0,
        "pending": 0,
        "applicable": False,
        "reason": reason,
        "items": [],
    }


def _pack(
    total: float,
    dimensions: list[dict[str, Any]],
    fatal: bool,
    note: str,
    extra: dict[str, Any],
) -> dict[str, Any]:
    value = {
        "total": total,
        "band": _band(total),
        "dimensions": dimensions,
        "fatal": fatal,
        "note": note,
    }
    value.update(extra)
    return value


def _band(total: float) -> str:
    for threshold, label in BANDS:
        if total >= threshold:
            return label
    return BANDS[-1][1]


def dimension_score(score: dict[str, Any], key: str) -> float | None:
    """供表格展开使用；不适用维度返回 None。"""
    for item in score.get("dimensions") or []:
        if item.get("key") == key:
            value = item.get("score")
            return float(value) if value is not None else None
    return None
