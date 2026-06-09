# Структура production-репозитория

[← К точке входа](../README.md) | [Машинный реестр](page_registry.jsonl)

```text
2_Concept_builder_ph2_no_nts/
- README.md
- Instructions/
  - concept_builder_service_instructions.md
  - concept_builder_execution_instructions.md
- Protocols/
  - protocol_index.md
  - state_architecture.md
  - context_loading.md
  - mode_routing.md
  - response_marker.md
  - github_write_protocol.md
- State/
  - service_state.md
  - execution_state.md
- Issues/
  - issue_registry.jsonl
  - issue_events.jsonl
- Concepts/
  - README.md
- Inbox/
  - README.md
- Registry/
  - structure.md
  - page_registry.jsonl
```

`Scripts/` не создана: production-скрипты требуют отдельного утверждённого `issue`, контракта входов и выходов, проверки безопасности и связи с протоколом.
