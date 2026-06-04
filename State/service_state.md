# State `Service Mode`

[← К схеме state](state_schema.md) | [← К главной точке входа](../README.md)

```yaml
active_mode: Service Mode
active_object: Concept Builder
active_issue: none
current_stage: repository_skeleton_initialized
dialogue_state: awaiting_primary_navigation
active_menu_id: service_primary_navigation_v1
loaded_context:
  - README.md
  - State/service_state.md
  - Protocols/protocol_index.md
loaded_protocols:
  - bootstrap_context
  - github_write
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
next_step: stage_2_common_core
return_anchor: README.md
persistence_status: synced
```

## Активное меню

1. Создать новый `issue`.
2. Взять существующий `issue`.

Команды действуют только пока `dialogue_state: awaiting_primary_navigation`.
