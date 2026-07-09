# R223M-P4 R97B Static Page Signal Integration Review

```text
stage_id=1013R_R223M_P4_R97B_STATIC_PAGE_SIGNAL_INTEGRATION
status=static_presentation_rule_hardening_only
ZIP_SHA256=0CDF775F3B617444947293AF6001F545498E53E7279F265AC05F2A02106ACD17
formal_ui=blocked
R97B / UI / runtime / prompt / model / db = untouched
```

## Open First

- `R223M_P4_teacher_readable_process_v5.html`
- `R223M_P4_teacher_readable_process_v5.md`
- `R223M_P4_r97b_static_page_signal_audit.md`

## What Changed

P4 integrates R97B static page signals as rules, not UI:

- lesson text first
- quiet header/meta
- preview-only before teacher confirmation
- short Xiaojiao judgement summary
- impact summary for screen/sheet/assessment
- low-weight local intent bar
- notebook/margin-note reading order
- action gate

## Boundary

This is a narrow review archive. It does not modify R97B or any formal app code.
