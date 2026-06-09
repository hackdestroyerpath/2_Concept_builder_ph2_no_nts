# Структура production-репозитория

[← К точке входа](../README.md) | [Машинный реестр](page_registry.jsonl) | [Схема реестра](page_registry_schema.md)

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
  - issue_lifecycle.md
  - question_answer.md
  - requirements_protocol.md
  - issue_execution.md
  - complex_and_linked_issues.md
  - concept_export.md
  - validation_protocol.md
  - execution_bootstrap.md
- State/
  - service_state.md
  - execution_state.md
- Issues/
  - issue_registry.jsonl
  - issue_events.jsonl
- Concepts/
  - README.md
- Templates/
  - README.md
  - concept/
    - README.md
    - concept_state.md
    - structure.md
    - page_registry.jsonl
    - purpose.md
    - requirements.md
    - operating_model.md
    - process.md
    - output.md
    - export.md
- Inbox/
  - README.md
- Registry/
  - structure.md
  - page_registry.jsonl
  - page_registry_schema.md
```

`Scripts/` не создана: production-скрипты требуют отдельного утверждённого `issue`, контракта входов и выходов, проверки безопасности и связи с протоколом.
