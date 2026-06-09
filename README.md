# Concept Builder

`Concept Builder` — production-система для ведения концепций через два режима: обслуживание самой системы и исполнение конкретных концепций. Источник истины — этот репозиторий `GitHub`.

## Статус

| Поле | Значение |
|---|---|
| Контур | `production repository` |
| Активный режим | `Service Mode` |
| Активный этап | сервисное ядро протоколов синхронизировано |
| Источник правил | production-файлы этого репозитория |
| Рабочие материалы реализации | не хранятся в репозитории |

## Режимы

| Режим | Назначение | Стартовый state |
|---|---|---|
| `Service Mode` | Обслуживание системы `Concept Builder`, протоколов, state, реестров и сервисных `issue`. | [`State/service_state.md`](State/service_state.md) |
| `Execution Mode` | Работа с конкретными концепциями внутри `Concepts/`. | [`State/execution_state.md`](State/execution_state.md) |

## Навигация верхнего уровня

| Путь | Назначение |
|---|---|
| [`Instructions/`](Instructions/concept_builder_service_instructions.md) | Короткие инструкции проектов `ChatGPT`: сервисный режим и режим исполнения. |
| [`Protocols/protocol_index.md`](Protocols/protocol_index.md) | Реестр протоколов и маршрутизация по состоянию или действию. |
| [`State/service_state.md`](State/service_state.md) | Текущее состояние `Service Mode`. |
| [`State/execution_state.md`](State/execution_state.md) | Текущее состояние `Execution Mode`. |
| [`Issues/issue_registry.jsonl`](Issues/issue_registry.jsonl) | Машинный реестр `issue`. |
| [`Issues/issue_events.jsonl`](Issues/issue_events.jsonl) | Журнал событий `issue` и сервисных переходов. |
| [`Concepts/README.md`](Concepts/README.md) | Входная страница пространства концепций. |
| [`Inbox/README.md`](Inbox/README.md) | Временное хранилище входных материалов до их обработки. |
| [`Registry/structure.md`](Registry/structure.md) | Человекочитаемая карта файлов. |
| [`Registry/page_registry.jsonl`](Registry/page_registry.jsonl) | Машинный реестр страниц и связей. |

## Ядро протоколов

| Протокол | Назначение |
|---|---|
| [`state_architecture`](Protocols/state_architecture.md) | Модель state и правила его обновления. |
| [`context_loading`](Protocols/context_loading.md) | Порядок загрузки минимального контекста. |
| [`mode_routing`](Protocols/mode_routing.md) | Выбор между `Service Mode` и `Execution Mode`. |
| [`response_marker`](Protocols/response_marker.md) | Стандартный маркер ответа агента. |
| [`github_write_protocol`](Protocols/github_write_protocol.md) | Правила записи и проверки файлов в `GitHub`. |

## Правила работы

1. В репозиторий попадают только production-файлы `Concept Builder`.
2. Рабочие checkpoint-архивы, техническое задание, промежуточные отчёты и временные материалы реализации не загружаются в этот репозиторий.
3. Перед записью агент определяет режим, разрешённую область записи, причину изменения, затрагиваемые реестры и план проверки.
4. После записи агент перечитывает изменённые файлы, проверяет связи и возвращает sync-report.
5. Все читаемые тексты ведутся на русском языке, кроме имён файлов, папок, сервисов, программ, проектов и технических идентификаторов.

## Маркер ответа агента

Каждый рабочий ответ агента показывает:

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
