# R223M-P4 预览与教师确认门

```json
{
  "preview_only": true,
  "teacher_confirmed": false,
  "formal_apply_allowed": false,
  "writes_formal_lesson_body": false,
  "runtime_connected": false,
  "provider_model_connected": false,
  "database_written": false
}
```

## 允许动作

- 教师确认：确认某个环节、组件或派生物进入后续预览。
- 教师修改：修改当前段落、话术、素材条件或学习单栏位。
- 教师替换：替换组件、素材或评价证据形式。
- 教师删除：删除非必要派生物；若删除唯一必要证据，系统必须提示需要替代证据。

## 禁止动作

- 不自动写入正式备课本；
- 不生成正式课件 / 学习单 / 数据库记录；
- 不把候选稿覆盖到 R97B；
- 不把小教输入变成全局聊天入口。
