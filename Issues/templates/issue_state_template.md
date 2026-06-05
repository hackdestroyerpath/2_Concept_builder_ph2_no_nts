# Шаблон `issue/state.md`

[← К Issues](../README.md)

```yaml
issue_id:
title:
mode:
owner:
type: simple | complex | linked | service | concept
status: creating | proposed | approved | questioning | requirements_review | solution_review | ready_for_execution | executing | completed | closed | rejected | blocked | waiting_dependency | needs_discussion | cleanup_pending
priority:
parent_issue:
child_issues: []
linked_issues: []
input_refs: []
reason_ref:
qa_ref:
requirements_ref:
solution_ref:
contract_ref:
output_ref:
report_ref:
attachments: []
dependency_status:
created_at:
updated_at:
return_anchor:
next_step:
persistence_status:
```

## Правило

State конкретного `issue` хранит текущее состояние этого `issue`, а не заменяет registry или event log.
