# Task state

[← Task](README.md) | [Issue lifecycle](../../Protocols/issue_lifecycle.md)

```text
task_id: {{issue_id}}
mode: {{mode}}
active_object: {{active_object}}
status: proposed | approved | executing | validation | closed_with_evidence | blocked
stage: {{stage}}
priority: normal | major | blocker
owner: {{active_object}}
dependencies:
approval_status:
current_artifact:
validation_status: not_run | running | passed_with_evidence | failed | blocked
persistence_status: not_written | written_unverified | synced | partial | failed | conflict | blocked
return_anchor:
updated_at:
```

## Правило

State задачи обновляется после каждого значимого перехода lifecycle и должен соответствовать `Issues/issue_registry.jsonl`.
