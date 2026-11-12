# 倒计时目标效果评测

- profile：`countdown-card-spec-v1`
- 样本数：6，通过 0，待复核 0，失败 6
- 规则通过率：42.7%
- 采集异常：RuntimeError: asyncio.run() cannot be called from a running event loop

## 规则汇总

| 规则 | 说明 | 通过 | 失败 | 待复核 | 不适用 | 通过率 |
|---|---|---|---|---|---|---|
| `VIS.EVIDENCE_MISSING` | 可见性证据完整 | 0 | 0 | 6 | 0 | 0.0% |
| `SPEC.RADIUS` | 圆角 20 | 6 | 0 | 0 | 0 | 100.0% |
| `SPEC.PADDING` | 内边距 12 | 6 | 0 | 0 | 0 | 100.0% |
| `SPEC.BG_FULL_BLEED` | 背景铺满 | 6 | 0 | 0 | 0 | 100.0% |
| `SPEC.MASK` | 黑色蒙层 60% | 0 | 6 | 0 | 0 | 0.0% |
| `SPEC.TITLE_REQUIRED` | 标题必选 | 6 | 0 | 0 | 0 | 100.0% |
| `SPEC.TITLE_FONT` | 标题 16/20fp | 0 | 6 | 0 | 0 | 0.0% |
| `SPEC.TITLE_ELLIPSIS` | 标题单行省略 | 0 | 6 | 0 | 0 | 0.0% |
| `SPEC.TITLE_COLOR` | 标题白色 | 2 | 4 | 0 | 0 | 33.3% |
| `SPEC.PRIMARY_FONT` | 主值 56/38fp | 1 | 5 | 0 | 0 | 16.7% |
| `SPEC.UNIT_FONT` | 单位 16fp 独立 | 0 | 6 | 0 | 0 | 0.0% |
| `SPEC.SUPPORT_FONT` | 副文本 16fp | 0 | 6 | 0 | 0 | 0.0% |
| `SPEC.SUPPORT_COLOR` | 副文本 60% 白 | 0 | 6 | 0 | 0 | 0.0% |
| `SPEC.CONTENT_TYPE` | 内容属于 C1–C5 | 6 | 0 | 0 | 0 | 100.0% |
| `SPEC.PATTERN_GEOMETRY` | 图案几何 | 0 | 0 | 0 | 6 | — |
| `SPEC.DIGIT_LIMIT` | 数字最多 6 位 | 5 | 0 | 0 | 1 | 100.0% |

## 样本结论

| 样本 | 状态 | 结论 | 失败项 | 待复核项 |
|---|---|---|---|---|
| `Q001` | failed | 采集失败 | SPEC.MASK, SPEC.TITLE_FONT, SPEC.TITLE_ELLIPSIS, SPEC.TITLE_COLOR, SPEC.PRIMARY_FONT, SPEC.UNIT_FONT, SPEC.SUPPORT_FONT, SPEC.SUPPORT_COLOR | VIS.EVIDENCE_MISSING |
| `Q031` | failed | 采集失败 | SPEC.MASK, SPEC.TITLE_FONT, SPEC.TITLE_ELLIPSIS, SPEC.TITLE_COLOR, SPEC.PRIMARY_FONT, SPEC.UNIT_FONT, SPEC.SUPPORT_FONT, SPEC.SUPPORT_COLOR | VIS.EVIDENCE_MISSING |
| `Q061` | failed | 采集失败 | SPEC.MASK, SPEC.TITLE_FONT, SPEC.TITLE_ELLIPSIS, SPEC.PRIMARY_FONT, SPEC.UNIT_FONT, SPEC.SUPPORT_FONT, SPEC.SUPPORT_COLOR, L0.CAPTURE_FAILED | VIS.EVIDENCE_MISSING |
| `Q076` | failed | 采集失败 | SPEC.MASK, SPEC.TITLE_FONT, SPEC.TITLE_ELLIPSIS, SPEC.TITLE_COLOR, SPEC.PRIMARY_FONT, SPEC.UNIT_FONT, SPEC.SUPPORT_FONT, SPEC.SUPPORT_COLOR | VIS.EVIDENCE_MISSING |
| `Q086` | failed | 采集失败 | SPEC.MASK, SPEC.TITLE_FONT, SPEC.TITLE_ELLIPSIS, SPEC.PRIMARY_FONT, SPEC.UNIT_FONT, SPEC.SUPPORT_FONT, SPEC.SUPPORT_COLOR, L0.CAPTURE_FAILED | VIS.EVIDENCE_MISSING |
| `Q091` | failed | 采集失败 | SPEC.MASK, SPEC.TITLE_FONT, SPEC.TITLE_ELLIPSIS, SPEC.TITLE_COLOR, SPEC.UNIT_FONT, SPEC.SUPPORT_FONT, SPEC.SUPPORT_COLOR, L0.CAPTURE_FAILED | VIS.EVIDENCE_MISSING |
