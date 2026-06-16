# Concept Builder

`Concept Builder` — рабочая система для ведения концепций через два режима: `Service Mode` обслуживает сам репозиторий, `Execution Mode` ведёт конкретные концепции в `Concepts/`. Источник истины — рабочие файлы этого репозитория, а не ярлыки закрытия, аудиторские заметки, prompt-ы или контрольные архивы.

## Текущее рабочее состояние

| Поле | Значение |
|---|---|
| Контур | рабочий репозиторий `Concept Builder` |
| Активный режим обслуживания | `Service Mode` |
| Активная задача исправления | `CB-P2` |
| Активный сегмент доработки | `P2R5` — финальная языковая зачистка зарегистрированных Markdown-файлов и повторная проверка |
| Основание | утверждённый реестр дефектов Phase 1 `D-001`…`D-063` и пятая проверка языкового шлюза |
| Проверка готовности | [`Validation/final_check.md`](Validation/final_check.md), [`Validation/sync_report.md`](Validation/sync_report.md), [`Validation/navigation_check.md`](Validation/navigation_check.md), [`Validation/language_check.md`](Validation/language_check.md) |
| Статус финального принятия | `passed`: `D-001`…`D-063` имеют доказательства закрытия, блокеры `0`, `remaining: []` |
| Следующий безопасный шаг | вернуть локальный финальный архив-кандидат; архив и материалы передачи не добавляются в репозиторий |

## Режимы

| Режим | Назначение | Состояние | Основные маршруты |
|---|---|---|---|
| `Service Mode` | обслуживание протоколов, реестров, состояния, шаблонов, проверки и сервисных задач | [`State/service_state.md`](State/service_state.md) | [`Protocols/protocol_index.md`](Protocols/protocol_index.md), [`Issues/README.md`](Issues/README.md), [`Registry/page_registry.jsonl`](Registry/page_registry.jsonl), [`Validation/final_check.md`](Validation/final_check.md) |
| `Execution Mode` | работа с выбранной концепцией внутри `Concepts/` | [`State/execution_state.md`](State/execution_state.md) | [`Protocols/execution_bootstrap.md`](Protocols/execution_bootstrap.md), [`Concepts/README.md`](Concepts/README.md), [`Protocols/concept_export.md`](Protocols/concept_export.md) |

## Маршруты верхнего уровня

| Путь | Назначение | Владелец | Источник истины | Маршрут из `README.md` |
|---|---|---|---|---|
| [`Instructions/`](Instructions/concept_builder_service_instructions.md) | короткие начальные инструкции для проектов `ChatGPT` | `Service Mode` / `Execution Mode` | сами файлы инструкций + состояние | [`service`](Instructions/concept_builder_service_instructions.md), [`execution`](Instructions/concept_builder_execution_instructions.md) |
| [`Protocols/`](Protocols/protocol_index.md) | исполнимые протоколы, матрица маршрутов и маршруты отказов | `Service Mode` | [`Protocols/protocol_index.md`](Protocols/protocol_index.md) | [`Protocols/protocol_index.md`](Protocols/protocol_index.md) |
| [`State/`](State/service_state.md) | сервисное и исполнительное состояние | соответствующий режим | файлы состояния и маркер ответа | [`State/service_state.md`](State/service_state.md), [`State/execution_state.md`](State/execution_state.md) |
| [`Issues/`](Issues/README.md) | реестр, события и артефакты задач | `Service Mode` | [`Issues/issue_registry.jsonl`](Issues/issue_registry.jsonl), [`Issues/issue_events.jsonl`](Issues/issue_events.jsonl) | [`Issues/README.md`](Issues/README.md), [`Issues/CB-P2/README.md`](Issues/CB-P2/README.md) |
| [`Concepts/`](Concepts/README.md) | концепции как связанные Markdown-сети; `smoke` сохранён только как проверочный пример | `Execution Mode` | `README.md`, состояние и реестр каждой концепции | [`Concepts/README.md`](Concepts/README.md), [`Concepts/smoke/README.md`](Concepts/smoke/README.md) |
| [`Templates/`](Templates/README.md) | рабочие шаблоны задач и концепций | `Service Mode` | локальные реестры в `Templates/` | [`Templates/README.md`](Templates/README.md), [`Templates/concept/README.md`](Templates/concept/README.md), [`Templates/task/README.md`](Templates/task/README.md) |
| [`Inbox/`](Inbox/README.md) | входящие материалы до классификации в задачу | `Service Mode` | политика `Issues/README.md` + журнал событий | [`Inbox/README.md`](Inbox/README.md) |
| [`Registry/`](Registry/structure.md) | глобальная карта страниц, владельцев, связей и статуса навигации | `Service Mode` | [`Registry/page_registry_schema.md`](Registry/page_registry_schema.md), [`Registry/page_registry.jsonl`](Registry/page_registry.jsonl) | [`Registry/structure.md`](Registry/structure.md) |
| [`Validation/`](Validation/final_check.md) | проверки доказательств, пробный прогон, языковая/навигационная проверка и отчёт синхронизации | `Service Mode` | [`Validation/final_check.md`](Validation/final_check.md), [`Validation/sync_report.md`](Validation/sync_report.md) | [`Validation/final_check.md`](Validation/final_check.md), [`Validation/sync_report.md`](Validation/sync_report.md) |

`Plans/` и `Closure/` не являются активными рабочими зонами. Сведения из прежних файлов процесса и лишних материалов мигрированы в `Issues/` и `Validation/`; отсутствующие `Plans/cb008.md` и `Closure/status.md` не восстанавливаются.

## Основные протоколы

| Действие | Стартовый протокол | Выход |
|---|---|---|
| Загрузить контекст | [`context_loading`](Protocols/context_loading.md) | ограниченный набор файлов по режиму и области |
| Выбрать режим | [`mode_routing`](Protocols/mode_routing.md) | `Service Mode`, `Execution Mode` или передача/блокировка |
| Сверить состояние и маркер | [`state_architecture`](Protocols/state_architecture.md), [`response_marker`](Protocols/response_marker.md) | канонические поля и маркер ответа |
| Создать или продолжить задачу | [`issue_lifecycle`](Protocols/issue_lifecycle.md) | строка реестра, события, обновление состояния |
| Уточнить требования | [`question_answer`](Protocols/question_answer.md) и [`requirements_protocol`](Protocols/requirements_protocol.md) | утверждённые требования или сохранённая причина пропуска |
| Исполнить задачу | [`issue_execution`](Protocols/issue_execution.md) | решение, контракт, результат, отчёт |
| Записать в `GitHub` | [`github_write_protocol`](Protocols/github_write_protocol.md) | перечитывание, отчёт синхронизации, статус |
| Восстановиться после конфликта | [`github_conflict_recovery`](Protocols/github_conflict_recovery.md), [`rollback_protocol`](Protocols/rollback_protocol.md) | решение конфликта, откат или новая задача |
| Экспортировать концепцию | [`concept_export`](Protocols/concept_export.md) | рабочий манифест экспорта |
| Проверить готовность | [`validation_protocol`](Protocols/validation_protocol.md) | матрица доказательств без закрытия только по утверждению |

## Правила записи

1. Перед записью классифицировать файл как рабочий или разработческий.
2. Не загружать материалы передачи исправления, аудит Phase 1, prompt-ы, контрольные архивы, временные отчёты и исходный архив передачи.
3. Писать только в разрешённую область активного режима.
4. После записи перечитать изменённые файлы из `GitHub`, проверить реестр, состояние, события, ссылки и язык, затем обновить доказательства отчёта синхронизации.
5. Статусы `closed`, `passed`, `synced`, `Ready`, `OK` не являются доказательством без записей в `Validation/`.

## Финальный результат Phase 2

`CB-P2` завершён как `fixed_with_evidence` после полной зачистки P2R5 и финального перечитывания. Цепочка доказательств: `README.md`, `State/service_state.md`, `Issues/CB-P2/README.md`, `Issues/issue_registry.jsonl`, `Issues/issue_events.jsonl`, `Protocols/`, `Templates/`, `Concepts/smoke/`, `Registry/`, `Validation/final_check.md`, `Validation/sync_report.md`, `Validation/navigation_check.md`, `Validation/language_check.md`.

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