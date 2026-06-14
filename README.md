# Concept Builder

`Concept Builder` — production-система для ведения концепций через два режима: `Service Mode` обслуживает сам репозиторий, `Execution Mode` ведёт конкретные концепции в `Concepts/`. Источник истины — production-файлы этого репозитория, а не ярлыки закрытия, audit-заметки, prompt-ы или checkpoint-архивы. Да, приходится проговаривать очевидное, потому что иначе ярлык `OK` снова притворится доказательством.

## Текущее production-состояние

| Поле | Значение |
|---|---|
| Контур | production-репозиторий `Concept Builder` |
| Активный режим обслуживания | `Service Mode` |
| Активный issue исправления | `CB-P2` |
| Активная patch-задача | `P2-001` — root README и top-level governance |
| Рабочая ветка patch | `agent/phase2-patch-20260614T000000Z` |
| Основание | утверждённый Phase 1 defect register D-001…D-063 |
| Проверка готовности | [`Validation/final_check.md`](Validation/final_check.md) и evidence-файлы в `Validation/` |
| Статус финального закрытия | финальная приёмка не выполнена; закрытие разрешено только после evidence matrix D-001…D-063 |

## Режимы

| Режим | Назначение | State | Основные маршруты |
|---|---|---|---|
| `Service Mode` | Обслуживание протоколов, реестров, state, шаблонов, validation и сервисных `issue`. | [`State/service_state.md`](State/service_state.md) | [`Protocols/protocol_index.md`](Protocols/protocol_index.md), [`Issues/README.md`](Issues/README.md), [`Registry/page_registry.jsonl`](Registry/page_registry.jsonl), [`Validation/final_check.md`](Validation/final_check.md) |
| `Execution Mode` | Работа с выбранной концепцией внутри `Concepts/`. | [`State/execution_state.md`](State/execution_state.md) | [`Protocols/execution_bootstrap.md`](Protocols/execution_bootstrap.md), [`Concepts/README.md`](Concepts/README.md), [`Protocols/concept_export.md`](Protocols/concept_export.md) |

## Маршруты верхнего уровня

| Путь | Назначение | Владелец | Источник истины | Маршрут из README |
|---|---|---|---|---|
| [`Instructions/`](Instructions/concept_builder_service_instructions.md) | Короткие bootstrap-инструкции для проектов `ChatGPT`. | `Service Mode` / `Execution Mode` | сами файлы инструкций + state | [`service`](Instructions/concept_builder_service_instructions.md), [`execution`](Instructions/concept_builder_execution_instructions.md) |
| [`Protocols/`](Protocols/protocol_index.md) | Исполнимые протоколы, routing matrix, failure routes. | `Service Mode` | [`Protocols/protocol_index.md`](Protocols/protocol_index.md) | [`Protocols/protocol_index.md`](Protocols/protocol_index.md) |
| [`State/`](State/service_state.md) | Сервисное и исполнительное состояние. | соответствующий режим | state-файлы и response marker | [`State/service_state.md`](State/service_state.md), [`State/execution_state.md`](State/execution_state.md) |
| [`Issues/`](Issues/README.md) | Реестр, события и артефакты `issue`. | `Service Mode` | [`Issues/issue_registry.jsonl`](Issues/issue_registry.jsonl), [`Issues/issue_events.jsonl`](Issues/issue_events.jsonl) | [`Issues/README.md`](Issues/README.md), [`Issues/CB-P2/README.md`](Issues/CB-P2/README.md) |
| [`Concepts/`](Concepts/README.md) | Концепции как связанные MD-сети; `smoke` сохранён только как validation fixture. | `Execution Mode` | README/state/registry каждой концепции | [`Concepts/README.md`](Concepts/README.md), [`Concepts/smoke/README.md`](Concepts/smoke/README.md) |
| [`Templates/`](Templates/README.md) | Production-шаблоны задач и концепций. | `Service Mode` | локальные registry в `Templates/` | [`Templates/README.md`](Templates/README.md), [`Templates/concept/README.md`](Templates/concept/README.md), [`Templates/task/README.md`](Templates/task/README.md) |
| [`Inbox/`](Inbox/README.md) | Входящие материалы до классификации в `issue`. | `Service Mode` | политика `Issues/README.md` + event log | [`Inbox/README.md`](Inbox/README.md) |
| [`Registry/`](Registry/structure.md) | Глобальная карта страниц, владельцев, связей и navigation status. | `Service Mode` | [`Registry/page_registry_schema.md`](Registry/page_registry_schema.md), [`Registry/page_registry.jsonl`](Registry/page_registry.jsonl) | [`Registry/structure.md`](Registry/structure.md) |
| [`Validation/`](Validation/final_check.md) | Evidence-проверки, dry-run, language/navigation check и sync-report. | `Service Mode` | [`Validation/final_check.md`](Validation/final_check.md), [`Validation/sync_report.md`](Validation/sync_report.md) | [`Validation/final_check.md`](Validation/final_check.md), [`Validation/sync_report.md`](Validation/sync_report.md) |

`Plans/` и `Closure/` не являются активными production-зонами. Сведения из прежних process/debris-файлов мигрируются в `Issues/` и `Validation/`; отсутствующие `Plans/cb008.md` и `Closure/status.md` не восстанавливаются.

## Основные протоколы

| Действие | Стартовый протокол | Выход |
|---|---|---|
| Загрузить контекст | [`context_loading`](Protocols/context_loading.md) | ограниченный набор файлов по mode/scope |
| Выбрать режим | [`mode_routing`](Protocols/mode_routing.md) | `Service Mode`, `Execution Mode` или transfer/blocked |
| Создать или продолжить `issue` | [`issue_lifecycle`](Protocols/issue_lifecycle.md) | registry row, events, state update |
| Уточнить требования | [`question_answer`](Protocols/question_answer.md) и [`requirements_protocol`](Protocols/requirements_protocol.md) | утверждённые требования или persisted skip reason |
| Исполнить задачу | [`issue_execution`](Protocols/issue_execution.md) | solution, contract, output, report |
| Записать в `GitHub` | [`github_write_protocol`](Protocols/github_write_protocol.md) | readback, sync-report, status |
| Восстановиться после конфликта | [`github_conflict_recovery`](Protocols/github_conflict_recovery.md), [`rollback_protocol`](Protocols/rollback_protocol.md) | conflict decision, rollback или новый issue |
| Экспортировать концепцию | [`concept_export`](Protocols/concept_export.md) | production-export manifest |
| Проверить готовность | [`validation_protocol`](Protocols/validation_protocol.md) | evidence matrix без assertion-only closure |

## Правила записи

1. Перед записью классифицировать файл как production или development.
2. Не загружать patch-handoff, Phase 1 audit, prompt-ы, checkpoint-и, временные отчёты и исходный handoff-архив.
3. Писать только в разрешённый scope активного режима.
4. После записи перечитать изменённые файлы из `GitHub`, проверить registry/state/events/links/language и обновить sync-report.
5. Статусы `closed`, `passed`, `synced`, `Ready`, `OK` не являются доказательством без evidence в `Validation/`.

## Следующий безопасный шаг

После readback этого P2-001-сегмента следующий patch-step — `P2-002`: rebuild global/local registries и navigation metadata. Финальное закрытие до `P2-010` запрещено.

## Маркер ответа агента

```text
mode:
active_object:
active_issue:
stage:
loaded_context:
persistence_status:
next_step:
return_anchor:
```
