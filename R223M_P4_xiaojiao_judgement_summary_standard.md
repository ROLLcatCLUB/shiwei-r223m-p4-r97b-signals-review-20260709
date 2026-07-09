# R223M-P4 小教判断摘要标准

```text
max_core_judgement=1
max_high_risk=1
max_suggested_action=1
max_teacher_confirmation=1
not_chat=true
not_full_lesson_summary=true
```

## 字段

| 字段 | 教师可见写法 | 禁止 |
| --- | --- | --- |
| core_judgement | 本环节最要守住的教学判断，一句话 | 展开完整推理链 |
| high_risk | 学生最容易偏到哪里，一句话 | 罗列全部风险 |
| suggested_action | 教师下一步最小动作 | 泛泛写“教师引导” |
| teacher_confirmation | 进入下一环节前需要老师确认的条件 | 自动替老师决定 |

## 样式原则

小教判断不是聊天回复，也不是第二份教案。它只对当前环节给短判断，默认不写入正式备课本。
