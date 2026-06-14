# Структура production-репозитория

[← Точка входа](../README.md) | [Машинный реестр](page_registry.jsonl) | [Схема реестра](page_registry_schema.md) | [Навигационная проверка](../Validation/navigation_check.md)

## Утверждённое дерево Phase 2

```text
2_Concept_builder_ph2_no_nts/
├── README.md
├── Instructions/
│   ├── concept_builder_service_instructions.md
│   └── concept_builder_execution_instructions.md
├── Protocols/
│   ├── protocol_index.md
│   ├── state_architecture.md
│   ├── context_loading.md
│   ├── mode_routing.md
│   ├── response_marker.md
│   ├── github_write_protocol.md
│   ├── github_conflict_recovery.md
│   ├── rollback_protocol.md
│   ├── issue_lifecycle.md
│   ├── question_answer.md
│   ├── requirements_protocol.md
│   ├── issue_execution.md
│   ├── complex_and_linked_issues.md
│   ├── task_flow_hardening.md
│   ├── template_validation.md
│   ├── execution_bootstrap.md
│   ├── concept_export.md
│   └── validation_protocol.md
├── State/
│   ├── service_state.md
│   └── execution_state.md
├── Issues/
│   ├── README.md
│   ├── issue_registry.jsonl
│   ├── issue_events.jsonl
│   ├── CB-P2/README.md
│   ├── CB-002/README.md
│   ├── CB-003/README.md
│   ├── CB-004/README.md
│   ├── CB-005/README.md
│   ├── CB-006/README.md
│   ├── CB-007/README.md
│   ├── CB-008/README.md
│   └── CB-009/README.md
├── Concepts/
│   ├── README.md
│   └── smoke/
│       ├── README.md
│       ├── concept_state.md
│       ├── structure.md
│       ├── page_registry.jsonl
│       ├── purpose.md
│       ├── requirements.md
│       ├── operating_model.md
│       ├── process.md
│       ├── output.md
│       └── export.md
├── Templates/
│   ├── README.md
│   ├── concept/
│   │   ├── README.md
│   │   ├── concept_state.md
│   │   ├── structure.md
│   │   ├── page_registry.jsonl
│   │   ├── purpose.md
│   │   ├── requirements.md
│   │   ├── operating_model.md
│   │   ├── process.md
│   │   ├── output.md
│   │   └── export.md
│   └── task/
│       ├── README.md
│       ├── item_state.md
│       ├── question_answer.md
│       ├── requirements.md
│       ├── solution.md
│       ├── contract.md
│       ├── report.md
│       ├── linked_files.md
│       └── page_registry.jsonl
├── Inbox/
│   └── README.md
├── Registry/
│   ├── structure.md
│   ├── page_registry_schema.md
│   └── page_registry.jsonl
└── Validation/
    ├── final_check.md
    ├── cb008_dry_run.md
    ├── cb008_closure_plan.md
    ├── navigation_check.md
    ├── language_check.md
    └── sync_report.md
```

## Удалённые или мигрированные зоны

| Путь | Решение | Evidence |
|---|---|---|
| `Plans/cb008.md` | мигрировать валидные сведения в `Issues/CB-008/README.md` и `Validation/cb008_closure_plan.md`, затем удалить | `Validation/final_check.md` |
| `Closure/status.md` | заменить evidence-backed финальной проверкой в `Validation/final_check.md`, затем удалить | `Validation/final_check.md` |
| `Issues/cb89.md` | заменить proper issue folders `CB-008` и `CB-009`, затем удалить | `Issues/issue_events.jsonl` |
| `Concepts/smoke/o2.md` | удалить как orphan/stub; strict output page — `Concepts/smoke/output.md` | `Concepts/smoke/page_registry.jsonl` |

## Top-level governance

| Узел | Production-роль | Владелец | Source of truth |
|---|---|---|---|
| `Instructions/` | bootstrap-инструкции проекта `ChatGPT` | `Service Mode` | state + validation |
| `Protocols/` | исполнимые правила mode/issue/write/export/validation | `Service Mode` | `protocol_index.md` |
| `State/` | текущая state model | режим-владелец | state-файлы |
| `Issues/` | lifecycle, provenance, decisions, events | `Service Mode` | registry + events |
| `Concepts/` | execution objects | `Execution Mode` | local concept registry |
| `Templates/` | production template library | `Service Mode` | local template registries |
| `Inbox/` | input staging policy | `Service Mode` | `Issues/README.md` |
| `Registry/` | navigation contract | `Service Mode` | schema + JSONL |
| `Validation/` | evidence reports | `Service Mode` | final check + sync report |
