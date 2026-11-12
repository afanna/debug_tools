"""从 A2UI 组件中提取数据绑定路径，用于期望值是否被真实引用。"""

from __future__ import annotations

import json
import re
from typing import Any

_PATH_IN_EXPRESSION = re.compile(r"\$\{([^}]+)\}")
_PATH_IN_TEMPLATE = re.compile(r"\{\{\s*([A-Za-z0-9_$\[\]./-]+)\s*\}\}")
_PATH_LIKE = re.compile(r"/(?:data|page|app|user|global)[A-Za-z0-9_$./\[\]-]*")
_STRING_PROPS = ("content", "src", "value", "text", "label")


def parse_genui(source: str) -> dict[str, Any]:
    """解析 JSONL 行，返回组件、数据模型和 surface 信息。"""
    components: dict[str, dict[str, Any]] = {}
    data: dict[str, Any] = {}
    surface_id = "surface_card"
    surface: dict[str, Any] = {}
    rows = 0
    for line in source.splitlines():
        if not line.strip():
            continue
        try:
            row = json.loads(line)
        except ValueError:
            continue
        if not isinstance(row, dict):
            continue
        rows += 1
        create = row.get("createSurface")
        if isinstance(create, dict):
            if isinstance(create.get("surfaceId"), str):
                surface_id = create["surfaceId"]
            surface = dict(create)
        update_data = row.get("updateDataModel")
        if isinstance(update_data, dict):
            path = update_data.get("path")
            value = update_data.get("value")
            if path in (None, "/") and isinstance(value, dict):
                data.update(value)
            elif isinstance(path, str) and isinstance(value, dict):
                _set_path(data, path, value)
        update = row.get("updateComponents")
        if not isinstance(update, dict):
            continue
        items = update.get("components")
        if not isinstance(items, list):
            continue
        for item in items:
            if isinstance(item, dict) and isinstance(item.get("id"), str):
                components[item["id"]] = item
    return {
        "components": components,
        "data": data,
        "surfaceId": surface_id,
        "surface": surface,
        "rows": rows,
    }


def _set_path(data: dict[str, Any], path: str, value: dict[str, Any]) -> None:
    parts = [part for part in path.split("/") if part]
    node: dict[str, Any] = data
    for part in parts[:-1]:
        child = node.get(part)
        if not isinstance(child, dict):
            child = {}
            node[part] = child
        node = child
    if parts:
        node[parts[-1]] = value


def extract_paths(text: str) -> list[str]:
    """从模板表达式里提取数据路径，保留首次出现顺序。"""
    if not isinstance(text, str) or not text:
        return []
    found: list[str] = []
    for match in _PATH_IN_EXPRESSION.finditer(text):
        expression = match.group(1)
        for path in _PATH_LIKE.findall(expression):
            found.append(_normalize_path(path))
    for match in _PATH_IN_TEMPLATE.finditer(text):
        found.append(_normalize_path(match.group(1)))
    if not found:
        for path in _PATH_LIKE.findall(text):
            found.append(_normalize_path(path))
    unique: list[str] = []
    seen: set[str] = set()
    for path in found:
        if path and path not in seen:
            seen.add(path)
            unique.append(path)
    return unique


def _normalize_path(path: str) -> str:
    value = str(path).strip().rstrip(".")
    if value.startswith("$"):
        value = value[1:]
    if value.startswith("."):
        value = value.replace(".", "/", 1)
    value = value.replace(".", "/") if "/" not in value else value
    if not value.startswith("/"):
        value = f"/{value}"
    return re.sub(r"/{2,}", "/", value)


def component_paths(component: dict[str, Any]) -> list[str]:
    paths: list[str] = []
    for key in _STRING_PROPS:
        value = component.get(key)
        paths.extend(extract_paths(value) if isinstance(value, str) else [])
    styles = component.get("styles")
    if isinstance(styles, dict):
        for value in styles.values():
            if isinstance(value, str):
                paths.extend(extract_paths(value))
    return paths


def binding_index(components: dict[str, Any]) -> dict[str, list[str]]:
    """路径 → 引用它的组件 ID 列表。"""
    index: dict[str, list[str]] = {}
    for component_id, component in components.items():
        if not isinstance(component, dict):
            continue
        for path in component_paths(component):
            index.setdefault(path, []).append(component_id)
    return index


def field_path(write_result_to: str | None, field_name: str) -> str | None:
    if not write_result_to:
        return None
    prefix = write_result_to.rstrip("/")
    return f"{prefix}/{field_name.lstrip('/')}"


def leaf_component_ids(
    components: dict[str, Any],
    roots: list[str],
) -> list[str]:
    """返回 roots 及其后代中真正承载文本的组件 ID。"""
    children: dict[str, list[str]] = {}
    for component_id, component in components.items():
        if not isinstance(component, dict):
            continue
        raw = component.get("children")
        if isinstance(raw, list):
            children[component_id] = [item for item in raw if isinstance(item, str)]
    result: list[str] = []
    seen: set[str] = set()
    queue = list(roots)
    while queue:
        current = queue.pop(0)
        if current in seen:
            continue
        seen.add(current)
        if not children.get(current):
            result.append(current)
        queue.extend(children.get(current, []))
    return result
