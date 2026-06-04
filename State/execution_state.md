# State `Execution Mode`

[← К схеме state](state_schema.md) | [← К входу `Execution Mode`](../Concepts/README.md)

```yaml
active_mode: Execution Mode
active_object: none
active_issue: none
current_stage: execution_mode_entry_initialized
dialogue_state: bootstrap_unloaded
active_menu_id: none
loaded_context:
  - Concepts/README.md
  - State/execution_state.md
  - Protocols/protocol_index.md
loaded_protocols:
  - bootstrap_context
allowed_read_scope:
  - Concepts/
  - State/execution_state.md
  - Protocols/protocol_index.md
  - Protocols/concept_network_export_protocol.md
allowed_write_scope:
  - Concepts/{concept_id}/
  - Issues/{issue_id}/
next_step: select_or_create_concept_issue
return_anchor: Concepts/README.md
persistence_status: synced
```

## Ограничение

Пока `active_object: none`, агент не меняет файлы конкретной концепции. Сначала нужно создать или выбрать концепцию через `issue`.
