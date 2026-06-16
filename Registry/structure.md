# Структура рабочего репозитория

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

| Путь | Решение | Доказательство |
|---|---|---|
| `Plans/cb008.md` | сведения мигрированы в `Issues/CB-008/README.md` и `Validation/cb008_closure_plan.md`; файл не восстанавливается | `Validation/final_check.md`, `Validation/sync_report.md` |
| `Closure/status.md` | закрытие только по утверждению заменено финальной проверкой на доказательствах; файл не восстанавливается | `Validation/final_check.md` |
| `Issues/cb89.md` | заменён корректными папками задач `CB-008` и `CB-009`; лишний файл не восстанавливается | `Issues/issue_events.jsonl` |
| `Concepts/smoke/o2.md` | удалён как несвязанный или пустой файл; строгая страница результата — `Concepts/smoke/output.md` | `Concepts/smoke/page_registry.jsonl` |

## Управление верхнего уровня

| Узел | Рабочая роль | Владелец | Источник истины | Маршрут |
|---|---|---|---|---|
| `Instructions/` | начальные инструкции проекта `ChatGPT` | `Service Mode` / `Execution Mode` | состояние + проверка | `README.md` → `Instructions/*.md` |
| `Protocols/` | исполнимые правила режима, задачи, записи, экспорта и проверки | `Service Mode` | `Protocols/protocol_index.md` | `README.md` → `Protocols/protocol_index.md` |
| `State/` | текущая модель состояния | режим-владелец | файлы состояния | `README.md` → `State/service_state.md` / `State/execution_state.md` |
| `Issues/` | жизненный цикл, происхождение, решения и события | `Service Mode` | реестр и события | `README.md` → `Issues/README.md` |
| `Concepts/` | исполнительные объекты и проверочный пример | `Execution Mode` | локальный реестр концепции | `README.md` → `Concepts/README.md` |
| `Templates/` | рабочая библиотека шаблонов | `Service Mode` | локальные реестры шаблонов | `README.md` → `Templates/README.md` |
| `Inbox/` | политика входящих материалов | `Service Mode` | `Issues/README.md` + события | `README.md` → `Inbox/README.md` |
| `Registry/` | навигационный контракт | `Service Mode` | схема + JSONL | `README.md` → `Registry/structure.md` |
| `Validation/` | отчёты доказательств и финальные шлюзы приёмки | `Service Mode` | финальная проверка + отчёт синхронизации | `README.md` → `Validation/final_check.md` |

## Проверочные заметки P2-001

- Корневой `README.md` содержит граф маршрутов ко всем узлам верхнего уровня.
- `Plans/` и `Closure/` не входят в утверждённое рабочее дерево.
- `Concepts/smoke` сохранён только как проверочный пример; `o2.md` не является частью дерева.

## Заметки навигационного контракта P2-002

- `Registry/page_registry_schema.md` задаёт обязательные поля `title`, `type`, `owner`, `parent`, `children`, `cross_links`, `backlinks`, `description`, `source_of_truth`, `navigation_status`.
- `Registry/page_registry.jsonl` является глобальным навигационным контрактом для активного рабочего дерева.
- `Concepts/smoke/page_registry.jsonl`, `Templates/concept/page_registry.jsonl` и `Templates/task/page_registry.jsonl` являются локальными реестрами и используют локальные `README.md` как родительские или корневые страницы.
- `Templates/task/README.md` содержит кликабельную цепочку артефактов задачи, а не перечисление только путей.
- `Issues/cb89.md` и `Concepts/smoke/o2.md` не регистрируются как активные рабочие страницы; их удаление или невосстановление фиксируется через `Validation/final_check.md`, `Validation/sync_report.md` и `Issues/issue_events.jsonl`.
- Полная финальная приёмка остаётся за P2R5/P2-010; P2-002 фиксирует только доказательства реестра и навигации, потому что навигационная карта — это не магический талисман, как бы ни хотелось.