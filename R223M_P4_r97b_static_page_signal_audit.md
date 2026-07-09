# R223M-P4 R97B 静态页信号抽取

```text
stage_id=1013R_R223M_P4_R97B_STATIC_PAGE_SIGNAL_INTEGRATION
status=static_page_signal_audit
source=V2C selected C notebook paper + R97B clean shell preview
formal_ui=blocked
R97B / UI / runtime / prompt / model / db = untouched
```

## 结论

R97B 静态页有价值，但价值不在于直接复制三栏或纸张视觉，而在于已经打磨出的产品秩序：正文第一、影响摘要、小教低权重、候选预览、教师确认前不生效。P4 将这些作为教师稿呈现规则并入 P3 标准。

| signal_id | R97B / V2C 信号 | 并入 R223M-P4 的方式 |
| --- | --- | --- |
| lesson_text_first | 中心 lesson text 保持第一视觉目标；AI、证据和派生物在场但安静。 | 进入教师稿呈现规则：正文第一，推理链和派生物退到轻旁注/附录。 |
| quiet_header_meta | LessonHeader 降噪，状态和影响作为 meta，而不是长 chip row。 | 教师稿头部只保留 stage/status/boundary 的短元信息。 |
| preview_only_before_teacher_confirm | 候选预览、教师确认前不生效、不写入正式备课本。 | P4 明确 preview_only=true / teacher_confirmed=false / formal_apply_allowed=false。 |
| xiaojiao_judgement_summary | 小教只提示当前环节确认点，不展示完整教案摘要。 | 每环节最多 1 个核心判断、1 个高风险、1 个建议动作、1 个确认点。 |
| impact_summary_for_screen_sheet_assessment | 右栏改为下游影响摘要：课堂大屏、学习单、评价点。 | 每环节只给大屏/学习单/评价/素材确认的短摘要。 |
| low_weight_bottom_intent_bar | 底部小教是系统级 intent bar，不是浮动聊天插件。 | 局部输入只服务补材料、改本段、预览课堂联动。 |
| notebook_paper_margin_note | C 方向保留纸面阅读和页边注感觉。 | 最终稿像教案正文，依据和组件像页边轻注，不做卡片墙。 |
| action_gate | 动作限制为预览、确认、修改、替换、删除；确认前不生效。 | 所有派生物先入确认门，删除不能破坏唯一必要证据。 |

## 来源文档摘要

### V2C README

- Top tools are intentionally expanded for this review. They should not be
  treated as a failure of the earlier "fold more actions" direction.
- The notebook paper backplate is restored with a visible border and a paper
  background color of `rgb(241, 239, 225)`.
- The inner notebook bottom rim is now measured in the smoke manifest:
  `binder_to_panel=18`, `binder_to_workspace=18`, `binder_to_bottom_xiaojiao=28`
  at 2560px width.
- Bottom Xiaojiao is a 60px system-level input bar for the selected C review
  state, not a floating chat plugin.
- The center lesson text remains the first visual target; the right rail stays
  a quiet downstream-impact summary.

### V2C 方向比较

- Top toolbar is no longer an icon pile. A/B keep `进入编辑` and `小教推进` visible with `更多` folded; C is expanded by human request for this review round.
- LessonHeader is quieter: title first, status and impact as meta, and links for evidence/status instead of a long chip row.
- Header chips are reduced from 4 visible chips to 0 visible legacy chips. The information is preserved as quieter meta text.
- Right rail becomes an impact summary:
  - 课堂大屏：生成 2 页观察引导
  - 学习单：生成 1 个找渐变任务
  - 评价点：记录“能否说出颜色变化方向”
- Right rail actions are limited to `预览课堂材料` and `查看全部`.
- Bottom Xiaojiao is a system-level intent bar rather than a floating chat card.

### R97B 右栏策略

# R97B Right Rail Priority Policy

右侧栏在教师默认视图中的优先级：

1. P6 课堂联动。
2. 当前 episode 对应的大屏页 S01-S10。
3. 当前 episode 对应的学习单任务、教师观察维度、学生自评项。
4. 小教当前 episode 提示。
5. 历史 8 屏草稿与旧 draft 只能折叠为开发者/历史核对内容。

## Episode 到右栏

- 1. 看见渐变：S01 / S02
- 2. 分清亮暗与鲜灰：S03 / S04
- 3. 三格试色：S05 / S06
- 4. 放进作品：S07 / S08
- 5. 自查与微修订：S09 / S10

本策略只用于静态 preview，不导出正式课件。

## HTML / 壳层证据摘录

- `outputs\1013V_VISUAL_SYSTEM_POLISH_LINE\V2C_R97B_VISUAL_HIERARCHY_AND_AESTHETIC_DIRECTION\v2c_direction_C_notebook_paper.html:11909` 预览层候选预览 / 教师确认前不生效
- `outputs\1013V_VISUAL_SYSTEM_POLISH_LINE\V2C_R97B_VISUAL_HIERARCHY_AND_AESTHETIC_DIRECTION\v2c_direction_C_notebook_paper.html:11985` classProgressSchedule: "班级排课使用真实课题和正式课位作为落点依据，但顺延和调课仍等待教师确认。",
- `outputs\1013V_VISUAL_SYSTEM_POLISH_LINE\V2C_R97B_VISUAL_HIERARCHY_AND_AESTHETIC_DIRECTION\v2c_direction_C_notebook_paper.html:12102` pending: "等待教师确认、修改或采纳到预览，暂不正式写入。",
- `outputs\1013V_VISUAL_SYSTEM_POLISH_LINE\V2C_R97B_VISUAL_HIERARCHY_AND_AESTHETIC_DIRECTION\v2c_direction_C_notebook_paper.html:12945` ["当前风险", "课时标题和材料清单待教师确认"]
- `outputs\1013V_VISUAL_SYSTEM_POLISH_LINE\V2C_R97B_VISUAL_HIERARCHY_AND_AESTHETIC_DIRECTION\v2c_direction_C_notebook_paper.html:12966` text: "小教已生成1个课前处理建议，等待教师确认。",
- `outputs\1013V_VISUAL_SYSTEM_POLISH_LINE\V2C_R97B_VISUAL_HIERARCHY_AND_AESTHETIC_DIRECTION\v2c_direction_C_notebook_paper.html:13474` const R6K_BIG_UNIT_PLACEMENT = {"stage": "1013I_R6J_BIG_UNIT_PREP_HTML_FIXTURE_ORIGINAL_PAGE_INTEGRATION_REVIEW_GATE", "placement_decision": "inside_prep_room", "top_level_nav_not_modified": true, "big_unit_not_new_globa
- `outputs\1013V_VISUAL_SYSTEM_POLISH_LINE\V2C_R97B_VISUAL_HIERARCHY_AND_AESTHETIC_DIRECTION\v2c_direction_C_notebook_paper.html:13967` const aiSummary = (section.body || [])[1] || "小教根据教师后记、课堂观察和作品证据整理总结候选，等待教师确认后再进入档案沉淀。";
- `outputs\1013V_VISUAL_SYSTEM_POLISH_LINE\V2C_R97B_VISUAL_HIERARCHY_AND_AESTHETIC_DIRECTION\v2c_direction_C_notebook_paper.html:14358` ${html(episode.key_teacher_talk || "关键话术待教师确认。")}
- `outputs\1013V_VISUAL_SYSTEM_POLISH_LINE\V2C_R97B_VISUAL_HIERARCHY_AND_AESTHETIC_DIRECTION\v2c_direction_C_notebook_paper.html:14659` activeIndex === 3 ? "等待教师确认" :
- `outputs\1013V_VISUAL_SYSTEM_POLISH_LINE\V2C_R97B_VISUAL_HIERARCHY_AND_AESTHETIC_DIRECTION\v2c_direction_C_notebook_paper.html:14714` var coursewareScreens1013JR1 = [{"id": "screen_01_cover", "index": "01", "title": "课题导入", "screen_title": "色彩的感觉", "classroom_text": "颜色为什么会让人产生不同感觉？", "lesson_link": "导入问题", "placeholder": "课题背景图", "status": "已有文字", "to
- `outputs\1013V_VISUAL_SYSTEM_POLISH_LINE\V2C_R97B_VISUAL_HIERARCHY_AND_AESTHETIC_DIRECTION\v2c_direction_C_notebook_paper.html:14851` var coursewareScreens1013JR1 = [{"id": "screen_01_cover", "index": "01", "title": "课题导入", "screen_title": "色彩的感觉", "classroom_text": "颜色为什么会让人产生不同感觉？", "lesson_link": "导入问题", "placeholder": "课题背景图", "status": "已有文字", "to
- `outputs\1013V_VISUAL_SYSTEM_POLISH_LINE\V2C_R97B_VISUAL_HIERARCHY_AND_AESTHETIC_DIRECTION\v2c_direction_C_notebook_paper.html:14998` var coursewareScreens1013JR1 = [{"id": "screen_01_cover", "index": "01", "title": "课题导入", "screen_title": "色彩的感觉", "classroom_text": "颜色为什么会让人产生不同感觉？", "lesson_link": "导入问题", "placeholder": "课题背景图", "status": "已有文字", "to
- `outputs\1013V_VISUAL_SYSTEM_POLISH_LINE\V2C_R97B_VISUAL_HIERARCHY_AND_AESTHETIC_DIRECTION\v2c_direction_C_notebook_paper.html:15155` ["继续上次备课", "回到最近一次候选预览，继续查看、修改或补资料。", "继续"]
- `outputs\1013V_VISUAL_SYSTEM_POLISH_LINE\V2C_R97B_VISUAL_HIERARCHY_AND_AESTHETIC_DIRECTION\v2c_direction_C_notebook_paper.html:15480` ${iconButtonLabel("打开课前包", "arrow")}
- `outputs\1013V_VISUAL_SYSTEM_POLISH_LINE\V2C_R97B_VISUAL_HIERARCHY_AND_AESTHETIC_DIRECTION\v2c_direction_C_notebook_paper.html:15481` ${iconButtonLabel("生成缺失材料", "wand")}
- `outputs\1013V_VISUAL_SYSTEM_POLISH_LINE\V2C_R97B_VISUAL_HIERARCHY_AND_AESTHETIC_DIRECTION\v2c_direction_C_notebook_paper.html:15617` ${iconButtonLabel("查看调整方案", "arrow")}
- `outputs\PREP_ROOM_RENDER_CANVAS_DEEPEN_V1\1013R_R97B_TEACHER_SHELL_EXPERIENCE_POLISH_AND_STALE_CONTENT_CLEANUP\r97b_clean_shell_context_preview.html:10903` done: "已形成备课正文、教学过程、课件屏、学习单和评价证据的只读预览。"
- `outputs\PREP_ROOM_RENDER_CANVAS_DEEPEN_V1\1013R_R97B_TEACHER_SHELL_EXPERIENCE_POLISH_AND_STALE_CONTENT_CLEANUP\r97b_clean_shell_context_preview.html:12347` ${iconButtonLabel("确认到预览", "check")}
- `outputs\PREP_ROOM_RENDER_CANVAS_DEEPEN_V1\1013R_R97B_TEACHER_SHELL_EXPERIENCE_POLISH_AND_STALE_CONTENT_CLEANUP\r97b_clean_shell_context_preview.html:12358` 教师确认前不生效
- `outputs\PREP_ROOM_RENDER_CANVAS_DEEPEN_V1\1013R_R97B_TEACHER_SHELL_EXPERIENCE_POLISH_AND_STALE_CONTENT_CLEANUP\r97b_clean_shell_context_preview.html:12385` 大单元 ● 预览
- `outputs\PREP_ROOM_RENDER_CANVAS_DEEPEN_V1\1013R_R97B_TEACHER_SHELL_EXPERIENCE_POLISH_AND_STALE_CONTENT_CLEANUP\r97b_clean_shell_context_preview.html:13079` preview_only: true,
- `outputs\PREP_ROOM_RENDER_CANVAS_DEEPEN_V1\1013R_R97B_TEACHER_SHELL_EXPERIENCE_POLISH_AND_STALE_CONTENT_CLEANUP\r97b_clean_shell_context_preview.html:13107` preview_only: true,
- `outputs\PREP_ROOM_RENDER_CANVAS_DEEPEN_V1\1013R_R97B_TEACHER_SHELL_EXPERIENCE_POLISH_AND_STALE_CONTENT_CLEANUP\r97b_clean_shell_context_preview.html:13377` 只读候选 · 不写入正式备课本
- `outputs\PREP_ROOM_RENDER_CANVAS_DEEPEN_V1\1013R_R97B_TEACHER_SHELL_EXPERIENCE_POLISH_AND_STALE_CONTENT_CLEANUP\r97b_clean_shell_context_preview.html:16130` brief: "本课按真实教材目录重锚定为第二单元《多彩的世界》第1课《色彩的渐变》。当前页依据教材第6-7页可见信息与本地旧 AI 资料中的渐变技法参考生成，教师确认前不写入正式备课本。",
- `outputs\PREP_ROOM_RENDER_CANVAS_DEEPEN_V1\1013R_R97B_TEACHER_SHELL_EXPERIENCE_POLISH_AND_STALE_CONTENT_CLEANUP\r97b_clean_shell_context_preview.html:17090` model.negotiation.notes.prepNotebook = "备课页已同步到真实教材：三年级第二单元《多彩的世界》第1课《色彩的渐变》。当前只读预演，教师确认前不写入正式备课本。";
- `outputs\PREP_ROOM_RENDER_CANVAS_DEEPEN_V1\1013R_R97B_TEACHER_SHELL_EXPERIENCE_POLISH_AND_STALE_CONTENT_CLEANUP\r97b_clean_shell_context_preview.html:17123` {"stage":"1013K_R22_BIG_UNIT_PAGE_STATIC_READONLY_BINDING_MERGE","merged_into":"1013J_R1M_courseware_classroom_display_preview_static","binding_mode":"merged_static_fixture","chunk_count":10,"chunks":["render_chunk_curri
- `outputs\PREP_ROOM_RENDER_CANVAS_DEEPEN_V1\1013R_R97B_TEACHER_SHELL_EXPERIENCE_POLISH_AND_STALE_CONTENT_CLEANUP\r97b_clean_shell_context_preview.html:17124` {"stage":"1013K_R27_COURSEWARE_VIEWMODEL_TO_EXISTING_PAGE_HIDDEN_DATA_INJECTION","source_stage":"1013K_R26_COURSEWARE_SCREEN_SEED_TO_VIEWMODEL_FIXTURE","target_existing_page":"1013J_R1M_courseware_classroom_display_previ
- `outputs\PREP_ROOM_RENDER_CANVAS_DEEPEN_V1\1013R_R97B_TEACHER_SHELL_EXPERIENCE_POLISH_AND_STALE_CONTENT_CLEANUP\r97b_clean_shell_context_preview.html:17125` {"stage":"1013K_R29A_COURSEWARE_VIEWMODEL_NORMALIZATION_BEFORE_VISIBLE_RENDER","source_stage":"1013K_R25_CURRICULUM_CHUNK_TO_COURSEWARE_SCREEN_SEED_CONTRACT","target_existing_page":"1013J_R1M_courseware_classroom_display
