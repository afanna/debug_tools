# 倒计时目标效果评测

- profile：`countdown-card-spec-v1`
- 样本数：6，通过 0，待复核 0，失败 6
- 规则通过率：65.0%
- 平均总分：75.1 / 100
- 评分口径：目标语义 40、可见性 25、规范符合 25、素材渲染 10；待复核按半通过，不适用维度剔除；目标语义未通过时总分封顶 59.9。

## 规则汇总

| 规则 | 说明 | 通过 | 失败 | 待复核 | 不适用 | 通过率 |
|---|---|---|---|---|---|---|
| `TARGET.BINDING_MISSING` | 期望字段被组件引用 | 5 | 0 | 0 | 0 | 100.0% |
| `TARGET.BINDING_VALUE_MISMATCH` | 绑定值随注入变化 | 5 | 0 | 0 | 0 | 100.0% |
| `TARGET.DAYS_MISMATCH` | 天数与参考日一致 | 5 | 0 | 0 | 0 | 100.0% |
| `TARGET.RELATION_TEXT_MISMATCH` | 关系文案与日期差一致 | 5 | 0 | 0 | 0 | 100.0% |
| `TARGET.VISIBLE_EXPECTATION_MISSING` | 期望文本可见 | 5 | 0 | 0 | 0 | 100.0% |
| `TARGET.PLACEHOLDER_VISIBLE` | 无占位文案 | 6 | 0 | 0 | 0 | 100.0% |
| `TARGET.SCENARIO_RULE_VIOLATION` | 场景规则 | 1 | 0 | 0 | 0 | 100.0% |
| `VIS.TEXT_CLIPPED` | 文字未被裁切 | 0 | 6 | 0 | 0 | 0.0% |
| `VIS.TEXT_OVERFLOW` | 文字未越出画布 | 6 | 0 | 0 | 0 | 100.0% |
| `VIS.TEXT_OVERLAP` | 文字未互相遮挡 | 6 | 0 | 0 | 0 | 100.0% |
| `VIS.IMAGE_OVERFLOW` | 图片未越出画布 | 6 | 0 | 0 | 0 | 100.0% |
| `VIS.IMAGE_LOAD_FAILED` | 素材真实加载 | 6 | 0 | 0 | 0 | 100.0% |
| `VIS.FONT_TOO_SMALL` | 正文字号下限 | 6 | 0 | 0 | 0 | 100.0% |
| `VIS.CONTRAST_LOW` | 文字对比度 | 0 | 6 | 0 | 0 | 0.0% |
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
| `SPEC.SAFE_AREA` | 安全区内 | 6 | 0 | 0 | 0 | 100.0% |

## 样本结论

| 样本 | 总分 | 目标语义 | 可见性 | 规范符合 | 素材渲染 | 状态 | 结论 | 失败项 | 待复核项 |
|---|---|---|---|---|---|---|---|---|---|
| `Q001` | 77.3 | 40.0 | 17.9 | 11.7 | — | failed | 可见性失败 | SPEC.MASK, SPEC.TITLE_FONT, SPEC.TITLE_ELLIPSIS, SPEC.TITLE_COLOR, SPEC.PRIMARY_FONT, SPEC.UNIT_FONT, SPEC.SUPPORT_FONT, SPEC.SUPPORT_COLOR | — |
| `Q031` | 77.3 | 40.0 | 17.9 | 11.7 | — | failed | 可见性失败 | SPEC.MASK, SPEC.TITLE_FONT, SPEC.TITLE_ELLIPSIS, SPEC.TITLE_COLOR, SPEC.PRIMARY_FONT, SPEC.UNIT_FONT, SPEC.SUPPORT_FONT, SPEC.SUPPORT_COLOR | — |
| `Q061` | 60.8 | — | 17.9 | 12.5 | — | failed | 可见性失败 | SPEC.MASK, SPEC.TITLE_FONT, SPEC.TITLE_ELLIPSIS, SPEC.PRIMARY_FONT, SPEC.UNIT_FONT, SPEC.SUPPORT_FONT, SPEC.SUPPORT_COLOR, VIS.TEXT_CLIPPED | — |
| `Q076` | 77.3 | 40.0 | 17.9 | 11.7 | — | failed | 可见性失败 | SPEC.MASK, SPEC.TITLE_FONT, SPEC.TITLE_ELLIPSIS, SPEC.TITLE_COLOR, SPEC.PRIMARY_FONT, SPEC.UNIT_FONT, SPEC.SUPPORT_FONT, SPEC.SUPPORT_COLOR | — |
| `Q086` | 79.1 | 40.0 | 17.9 | 13.3 | — | failed | 可见性失败 | SPEC.MASK, SPEC.TITLE_FONT, SPEC.TITLE_ELLIPSIS, SPEC.PRIMARY_FONT, SPEC.UNIT_FONT, SPEC.SUPPORT_FONT, SPEC.SUPPORT_COLOR, VIS.TEXT_CLIPPED | — |
| `Q091` | 79.1 | 40.0 | 17.9 | 13.3 | — | failed | 可见性失败 | SPEC.MASK, SPEC.TITLE_FONT, SPEC.TITLE_ELLIPSIS, SPEC.TITLE_COLOR, SPEC.UNIT_FONT, SPEC.SUPPORT_FONT, SPEC.SUPPORT_COLOR, VIS.TEXT_CLIPPED | — |
