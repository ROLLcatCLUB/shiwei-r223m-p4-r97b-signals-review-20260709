from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent
STAGE_ID = "1013R_R223M_P4_R97B_STATIC_PAGE_SIGNAL_INTEGRATION"


def read(name: str) -> str:
    return (ROOT / name).read_text(encoding="utf-8")


def main() -> int:
    required = [
        "R223M_P4_r97b_static_page_signal_audit.md",
        "R223M_P4_teacher_draft_presentation_rules.md",
        "R223M_P4_xiaojiao_judgement_summary_standard.md",
        "R223M_P4_derived_material_impact_summary_standard.md",
        "R223M_P4_preview_and_teacher_confirmation_gate.md",
        "R223M_P4_teacher_readable_process_v5.md",
        "R223M_P4_teacher_readable_process_v5.html",
        "R223M_P4_before_after_compare_with_P3.md",
        "R223M_P4_report.md",
        "README_FOR_GPT_REVIEW.md",
        "PACKAGE_MANIFEST.json",
    ]
    failures: list[str] = []
    checks = 0

    for name in required:
        checks += 1
        if not (ROOT / name).exists():
            failures.append(f"missing:{name}")

    if failures:
        result = {
            "passed": False,
            "check_count": checks,
            "failed": len(failures),
            "failures": failures,
            "stage_id": STAGE_ID,
        }
        print(json.dumps(result, ensure_ascii=False))
        return 1

    audit = read("R223M_P4_r97b_static_page_signal_audit.md")
    rules = read("R223M_P4_teacher_draft_presentation_rules.md")
    gate = read("R223M_P4_preview_and_teacher_confirmation_gate.md")
    md = read("R223M_P4_teacher_readable_process_v5.md")
    html = read("R223M_P4_teacher_readable_process_v5.html")
    manifest = json.loads(read("PACKAGE_MANIFEST.json"))

    signal_ids = [
        "lesson_text_first",
        "quiet_header_meta",
        "preview_only_before_teacher_confirm",
        "xiaojiao_judgement_summary",
        "impact_summary_for_screen_sheet_assessment",
        "low_weight_bottom_intent_bar",
        "notebook_paper_margin_note",
        "action_gate",
    ]
    for sig in signal_ids:
        checks += 1
        if sig not in audit:
            failures.append(f"missing_signal:{sig}")

    for phrase in [
        "正文第一",
        "推理链附录化",
        "组件动作化",
        "派生物摘要化",
        "小教判断短摘要",
        "预览确认门",
    ]:
        checks += 1
        if phrase not in rules:
            failures.append(f"missing_presentation_rule:{phrase}")

    for token in [
        '"preview_only": true',
        '"teacher_confirmed": false',
        '"formal_apply_allowed": false',
        '"writes_formal_lesson_body": false',
    ]:
        checks += 1
        if token not in gate:
            failures.append(f"missing_gate_token:{token}")

    for phrase in ["【本环节在做什么】", "【小教判断】", "【师维控制点】", "【派生物影响】", "过渡语："]:
        checks += 1
        count = md.count(phrase)
        if count != 7:
            failures.append(f"bad_count:{phrase}:{count}")

    for phrase in ["小教判断", "师维控制点", "派生物影响", "本环节在做什么"]:
        checks += 1
        count = html.count(phrase)
        if count < 7:
            failures.append(f"html_missing_visible_phrase:{phrase}:{count}")

    for token in ["data-preview-only=\"true\"", "data-teacher-confirmed=\"false\"", STAGE_ID]:
        checks += 1
        if token not in html:
            failures.append(f"missing_html_state:{token}")

    for forbidden in [
        "R223_FORMAL_UI = ALLOWED",
        "formal_apply_allowed=true",
        "teacher_confirmed=true",
        "正式 UI 放行",
        "作为聊天主入口",
        "组件货架已启用",
    ]:
        checks += 1
        if forbidden in (audit + rules + gate + md + html):
            failures.append(f"forbidden_text:{forbidden}")

    for mojibake in ["???", "锟", "\ufffd"]:
        checks += 1
        if mojibake in html:
            failures.append(f"mojibake:{mojibake}")

    checks += 1
    if manifest.get("stage_id") != STAGE_ID:
        failures.append("manifest_stage_mismatch")
    checks += 1
    if manifest.get("boundary", {}).get("r97b_modified") is not False:
        failures.append("manifest_r97b_modified_not_false")
    checks += 1
    if manifest.get("boundary", {}).get("formal_ui") is not False:
        failures.append("manifest_formal_ui_not_false")

    result = {
        "passed": not failures,
        "check_count": checks,
        "failed": len(failures),
        "failures": failures,
        "stage_id": STAGE_ID,
        "html_xiaojiao_count": html.count("小教判断"),
        "html_impact_count": html.count("派生物影响"),
        "formal_ui": "blocked",
    }
    (ROOT / "validate_1013R_R223M_P4_r97b_static_page_signal_integration_result.json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(result, ensure_ascii=False))
    return 0 if result["passed"] else 1


if __name__ == "__main__":
    sys.exit(main())
