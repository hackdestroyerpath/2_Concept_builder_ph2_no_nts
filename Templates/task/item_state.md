# Состояние задачи

[← Задача](README.md) | [Жизненный цикл задачи](../../Protocols/issue_lifecycle.md) | [Поток задач](../../Protocols/task_flow_hardening.md)

```text
task_id: {{issue_id}}
mode: {{mode}}
active_object: {{active_object}}
owner_mode: Service Mode | Execution Mode
status: proposed | requirements_scoped | contract_approved | executing | review_required | fixed_with_evidence | blocked
stage: {{stage}}
priority: normal | major | blocker
provenance:
approval_status: requested | approved | rejected | reconstructed | not_required
dependencies:
current_artifact:
validation_status: not_run | running | verified_with_evidence | failed | blocked
persistence_status: not_written | written_unverified | repo_evidence_confirmed | partial | failed | conflict | blocked
return_anchor:
updated_at:
```

## Правило

Состояние задачи обновляется после каждого значимого перехода жизненного цикла и должно соответствовать `Issues/issue_registry.jsonl`, `Issues/issue_events.jsonl` и последнему отчёту.