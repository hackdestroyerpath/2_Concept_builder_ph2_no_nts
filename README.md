# Concept Builder

`Concept Builder` — production-система для ведения концепций через два режима: `Service Mode` обслуживает саму систему, `Execution Mode` ведёт конкретные концепции в `Concepts/`. Источник истины — production-файлы этого репозитория, а не ярлыки закрытия, заметки аудита или рабочие checkpoint-архивы.

## Текущее production-состояние

| Поле | Значение |
|---|---|
| Контур | production-репозиторий `Concept Builder` |
| Активный режим обслуживания | `Service Mode` |
| Активный issue исправления | `CB-P2` |
| Основание | утверждённый Phase 1 defect register, исправляется через Phase 2 patch |
| Проверка готовности | [`Validation/final_check.md`](Validation/final_check.md) и evidence-файлы в `Validation/` |
| Статус закрытия | закрытие разрешено только при evidence по всем D-001…D-063 |

## Режимы

| Режим | Назначение | State | Основные маршруты |
|---|---|---|---|
| `Service Mode` | Обслуживание протоколов, реестров, state, шаблонов и сервисных `issue`. | [`State/service_state.md`](State/service_state.md) | [`Protocols/protocol_index.md`](Protocols/protocol_index.md), [`Issues/README.md`](Issues/README.md), [`Registry/page_registry.jsonl`](Registry/page_registry.jsonl) |
| `Execution Mode` | Работа с выбранной концепцией внутри `Concepts/`. | [`State/execution_state.md`](State/execution_state.md) | [`Protocols/execution_bootstrap.md`](Protocols/execution_bootstrap.md), [`Concepts/README.md`](Concepts/README.md), [`Protocols/concept_export.md`](Protocols/concept_export.md) |

## Верхний уровень production-дерева

| Путь | Назначение | Владелец | Источник истины |
|---|---|---|---|
| [`Instructions/`](Instructions/concept_builder_service_instructions.md) | Короткие bootstrap-инструкции проектов `ChatGPT`. | `Service Mode` | сами файлы инструкций и state-счётчики символов |
| [`Protocols/`](Protocols/protocol_index.md) | Исполнимые протоколы, routing matrix, failure routes. | `Service Mode` | [`Protocols/protocol_index.md`](Protocols/protocol_index.md) |
| [`State/`](State/service_state.md) | Сервисное и исполнительное состояние. | соответствующий режим | state-файлы и маркер ответа |
| [`Issues/`](Issues/README.md) | Реестр, события и артефакты `issue`. | `Service Mode` | [`Issues/issue_registry.jsonl`](Issues/issue_registry.jsonl), [`Issues/issue_events.jsonl`](Issues/issue_events.jsonl) |
| [`Concepts/`](Concepts/README.md) | Концепции как связанные MD-сети. | `Execution Mode` | README каждой концепции и локальный registry |
| [`Templates/`](Templates/README.md) | Production-шаблоны задач и концепций. | `Service Mode` | локальные registry в `Templates/` |
| [`Inbox/`](Inbox/README.md) | Входящие материалы до классификации в `issue`. | `Service Mode` | политика `Issues/README.md` |
| [`Registry/`](Registry/structure.md) | Глобальная карта страниц, владельцев и связей. | `Service Mode` | [`Registry/page_registry_schema.md`](Registry/page_registry_schema.md), [`Registry/page_registry.jsonl`](Registry/page_registry.jsonl) |
| [`Validation/`](Validation/final_check.md) | Evidence-проверки, dry-run и sync-report. | `Service Mode` | [`Validation/final_check.md`](Validation/final_check.md) |

`Plans/` и `Closure/` не являются активными production-зонами. Сохранённые сведения из них мигрированы в `Issues/CB-P2/` и `Validation/`; файлы-debris удаляются patch-задачей.

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
