# Concept Builder

`Concept Builder` — production-система для ведения концепций через два режима: `Service Mode` обслуживает сам репозиторий, `Execution Mode` ведёт конкретные концепции в `Concepts/`. Источник истины — production-файлы этого репозитория, а не ярлыки закрытия, audit-заметки, prompt-ы или checkpoint-архивы.

## Текущее production-состояние

| Поле | Значение |
|---|---|
| Контур | production-репозиторий `Concept Builder` |
| Активный режим обслуживания | `Service Mode` |
| Активный issue исправления | `CB-P2` |
| Активный rework-сегмент | `P2R-006` — final acceptance candidate archive prepared from production evidence |
| Последний checkpoint merge | PR `#6`, merge commit `276b893043cd6f21f1ecf0cd18afc9faa6c5d52d`, scope through `P2R-001` / `P2-006` |
| Финальные direct-to-main evidence writes | post-PR6 writes on `main`, latest observed head before final control `6ecb13e2c2726899ff3162b18deadf52fffad1af` |
| Основание | утверждённый Phase 1 defect register `D-001`…`D-063` и second rejection handoff |
| Проверка готовности | [`Validation/final_check.md`](Validation/final_check.md), [`Validation/sync_report.md`](Validation/sync_report.md), [`Validation/navigation_check.md`](Validation/navigation_check.md), [`Validation/language_check.md`](Validation/language_check.md) |
| Статус финального принятия | `passed_with_evidence`: `D-001`…`D-063` имеют closure evidence, blockers `0` |
| Следующий безопасный шаг | отправить локальный final acceptance candidate archive; новых Phase 2 patch-step нет |

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

`Plans/` и `Closure/` не являются активными production-зонами. Сведения из прежних process/debris-файлов мигрированы в `Issues/` и `Validation/`; отсутствующие `Plans/cb008.md` и `Closure/status.md` не восстанавливаются.

## Основные протоколы

| Действие | Стартовый протокол | Выход |
|---|---|---|
| Загрузить контекст | [`context_loading`](Protocols/context_loading.md) | ограниченный набор файлов по mode/scope |
| Выбрать режим | [`mode_routing`](Protocols/mode_routing.md) | `Service Mode`, `Execution Mode` или transfer/blocked |
| Сверить state/marker | [`state_architecture`](Protocols/state_architecture.md), [`response_marker`](Protocols/response_marker.md) | canonical fields и маркер ответа |
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
4. После записи перечитать изменённые файлы из `GitHub`, проверить registry/state/events/links/language и обновить sync-report evidence.
5. Статусы `closed`, `passed`, `synced`, `Ready`, `OK` не являются доказательством без evidence в `Validation/`.

## Финальный Phase 2 результат

`CB-P2` завершён как `fixed_with_evidence`. Evidence chain: `README.md`, `State/service_state.md`, `Issues/CB-P2/README.md`, `Issues/issue_registry.jsonl`, `Issues/issue_events.jsonl`, `Protocols/`, `Templates/`, `Concepts/smoke/`, `Registry/`, `Validation/final_check.md`, `Validation/sync_report.md`, `Validation/navigation_check.md`, `Validation/language_check.md`.

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
