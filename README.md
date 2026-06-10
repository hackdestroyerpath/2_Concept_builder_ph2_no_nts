# Concept Builder

`Concept Builder` — production-система для ведения концепций через два режима: обслуживание самой системы и исполнение конкретных концепций. Источник истины — этот репозиторий `GitHub`.

## Статус

| Поле | Значение |
|---|---|
| Контур | `production repository` |
| Активный режим | `Service Mode` |
| Активный этап | task flow hardening синхронизирован |
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
| [`Templates/README.md`](Templates/README.md) | Production-шаблоны для концепций и задач. |
| [`Registry/structure.md`](Registry/structure.md) | Человекочитаемая карта файлов. |
| [`Registry/page_registry.jsonl`](Registry/page_registry.jsonl) | Машинный реестр страниц и связей. |

## Основные протоколы

| Протокол | Назначение |
|---|---|
| [`github_write_protocol`](Protocols/github_write_protocol.md) | Запись и проверка файлов в `GitHub`. |
| [`github_conflict_recovery`](Protocols/github_conflict_recovery.md) | Conflict / recovery для `GitHub`-записей. |
| [`issue_lifecycle`](Protocols/issue_lifecycle.md) | Статусы, переходы и закрытие `issue`. |
| [`task_flow_hardening`](Protocols/task_flow_hardening.md) | Approval, rejection, cleanup, priority и provenance. |
| [`template_validation`](Protocols/template_validation.md) | Проверка production-шаблонов перед использованием. |
| [`execution_bootstrap`](Protocols/execution_bootstrap.md) | Выбор или создание концепции в `Execution Mode`. |
| [`concept_export`](Protocols/concept_export.md) | Подготовка export-результата концепции. |
| [`validation_protocol`](Protocols/validation_protocol.md) | Финальная проверка production-состояния. |

## Правила работы

1. В репозиторий попадают только production-файлы `Concept Builder`.
2. Рабочие checkpoint-архивы, техническое задание, промежуточные отчёты и временные материалы реализации не загружаются в этот репозиторий.
3. Перед записью агент определяет режим, разрешённую область записи, причину изменения, затрагиваемые реестры и план проверки.
4. После записи агент перечитывает изменённые файлы, проверяет связи и возвращает sync-report.
5. Все читаемые тексты ведутся на русском языке, кроме имён файлов, папок, сервисов, программ, проектов и технических идентификаторов.

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
