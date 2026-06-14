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
| `Plans/cb008.md` | сведения мигрированы в `Issues/CB-008/README.md` и `Validation/cb008_closure_plan.md`; файл не восстанавливается | `Validation/final_check.md`, `Validation/sync_report.md` |
| `Closure/status.md` | assertion-only closure заменён evidence-backed финальной проверкой; файл не восстанавливается | `Validation/final_check.md` |
| `Issues/cb89.md` | заменён proper issue folders `CB-008` и `CB-009`; файл-debris не восстанавливается | `Issues/issue_events.jsonl` |
| `Concepts/smoke/o2.md` | удалён как orphan/stub; strict output page — `Concepts/smoke/output.md` | `Concepts/smoke/page_registry.jsonl` |

## Governance верхнего уровня

| Узел | Production-роль | Владелец | Источник истины | Маршрут |
|---|---|---|---|---|
| `Instructions/` | bootstrap-инструкции проекта `ChatGPT` | `Service Mode` / `Execution Mode` | state + validation | `README.md` → `Instructions/*.md` |
| `Protocols/` | исполнимые правила mode/issue/write/export/validation | `Service Mode` | `Protocols/protocol_index.md` | `README.md` → `Protocols/protocol_index.md` |
| `State/` | текущая state model | режим-владелец | state-файлы | `README.md` → `State/service_state.md` / `State/execution_state.md` |
| `Issues/` | lifecycle, provenance, decisions, events | `Service Mode` | registry + events | `README.md` → `Issues/README.md` |
| `Concepts/` | execution objects и validation fixture | `Execution Mode` | local concept registry | `README.md` → `Concepts/README.md` |
| `Templates/` | production template library | `Service Mode` | local template registries | `README.md` → `Templates/README.md` |
| `Inbox/` | input staging policy | `Service Mode` | `Issues/README.md` + events | `README.md` → `Inbox/README.md` |
| `Registry/` | navigation contract | `Service Mode` | schema + JSONL | `README.md` → `Registry/structure.md` |
| `Validation/` | evidence reports and final acceptance gates | `Service Mode` | final check + sync report | `README.md` → `Validation/final_check.md` |

## P2-001 validation notes

- Root README содержит route graph ко всем top-level узлам.
- `Plans/` и `Closure/` не входят в утверждённое production-дерево.
- `Concepts/smoke` сохранён только как validation fixture; orphan/stub `o2.md` не является частью дерева.

## P2-002 navigation contract notes

- `Registry/page_registry_schema.md` задаёт обязательные поля `title`, `type`, `owner`, `parent`, `children`, `cross_links`, `backlinks`, `description`, `source_of_truth`, `navigation_status`.
- `Registry/page_registry.jsonl` является глобальным navigation contract для active production tree.
- `Concepts/smoke/page_registry.jsonl`, `Templates/concept/page_registry.jsonl` и `Templates/task/page_registry.jsonl` являются local registry и используют локальные `README.md` как parent/root.
- `Templates/task/README.md` содержит кликабельную цепочку task artifacts, а не path-only перечисление.
- `Issues/cb89.md` и `Concepts/smoke/o2.md` не регистрируются как active production pages; их удаление/невосстановление фиксируется через `Validation/final_check.md`, `Validation/sync_report.md` и `Issues/issue_events.jsonl`.
- Полная финальная приёмка остаётся заблокированной до P2-010; P2-002 фиксирует только registry/navigation evidence, потому что навигационная карта — это не магический талисман, как бы ни хотелось.