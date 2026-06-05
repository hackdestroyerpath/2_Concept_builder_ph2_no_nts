# State `Service Mode`

[← К схеме state](state_schema.md) | [← К главной точке входа](../README.md)

```yaml
active_mode: Service Mode
active_object: Concept Builder
active_issue: none
current_stage: validation_report_created
dialogue_state: awaiting_primary_navigation
active_menu_id: service_primary_navigation_v1
loaded_context:
  - README.md
  - State/service_state.md
  - Protocols/protocol_index.md
  - Registry/structure.md
  - Registry/validation_report.md
loaded_protocols:
  - bootstrap_context
  - context_loading
  - github_write
  - navigation_validation
  - response_marker
allowed_read_scope:
  - README.md
  - Instructions/
  - Protocols/
  - State/
  - Issues/
  - Inbox/
  - Concepts/
  - Registry/
allowed_write_scope:
  - README.md
  - Instructions/
  - Protocols/
  - State/
  - Issues/
  - Inbox/
  - Registry/
next_step: create_or_select_issue
return_anchor: README.md
persistence_status: synced
last_verified_paths:
  - Protocols/protocol_index.md
  - Protocols/protocol_registry.jsonl
  - State/state_schema.md
  - Issues/README.md
  - Concepts/README.md
  - Registry/structure.md
  - Registry/validation_report.md
```

## Активное меню

1. Создать новый `issue`.
2. Взять существующий `issue`.

Команды действуют только пока `dialogue_state: awaiting_primary_navigation`.
