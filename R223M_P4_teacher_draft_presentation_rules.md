# R223M-P4 教师稿呈现规则

```text
lesson_text_first=true
reasoning_chain_default=appendix_or_backend
component_default=embedded_classroom_action
preview_only=true
teacher_confirmed=false
formal_apply_allowed=false
```

## 规则

| 规则 | 说明 |
| --- | --- |
| 正文第一 | 教师先读连续教学过程；推理链、组件、证据不得先于正文抢主位。 |
| 标题降噪 | 标题下只保留短元信息；状态、边界、确认门作为轻 meta。 |
| 推理链附录化 | 大观念、阶段责任、组件触发、证据链可追溯，但默认进入附录或后端 JSON。 |
| 组件动作化 | 组件必须嵌入课堂动作，不能显示为工具货架。 |
| 派生物摘要化 | 大屏、学习单、评价只给当前环节影响摘要，不展开完整材料表。 |
| 小教判断短摘要 | 每环节最多 1 个判断、1 个风险、1 个建议、1 个确认点。 |
| 局部意图输入 | 底部输入只用于补材料、改本段、改话术、预览课堂联动，不做聊天主入口。 |
| 预览确认门 | teacher_confirmed=false 前不得写入正式备课本，所有操作保持 preview_only。 |

## 对 P3 标准的修订

P3 的课堂事件字段继续保留，但教师主稿只显露两种轻旁注：

- `【小教判断】`：压成一个很短的判断摘要，帮助教师知道该守住什么。
- `【派生物影响】`：只说明大屏、学习单、评价证据和确认点会受什么影响。

完整的 `screen_trigger`、`component_trigger`、`learning_sheet_trigger`、`evidence_trigger` 仍在 JSON 和附录中，不直接铺给老师。
