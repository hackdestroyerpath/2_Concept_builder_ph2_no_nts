# Инструкция проекта: Concept Builder Execution Mode

[← К точке входа](../README.md)

## Роль

Ты работаешь в `Execution Mode`: ведёшь выбранную концепцию внутри `Concepts/`, поддерживаешь её связанную сеть MD-файлов, requirements, operating model, process, output, export и local registry.

## Источник истины

Источник истины — production-файлы репозитория `GitHub` `hackdestroyerpath/2_Concept_builder_ph2_no_nts`, state выбранной концепции и её local registry.

Работай только с выбранной концепцией и её разрешёнными `issue`. Не смешивай работу над концепцией с обслуживанием системных протоколов.

## Старт

1. Прочитай [`../README.md`](../README.md).
2. Прочитай [`../State/execution_state.md`](../State/execution_state.md).
3. Прочитай [`../Concepts/README.md`](../Concepts/README.md).
4. Прочитай [`../Protocols/protocol_index.md`](../Protocols/protocol_index.md).
5. Примени [`../Protocols/execution_bootstrap.md`](../Protocols/execution_bootstrap.md) и [`../Protocols/context_loading.md`](../Protocols/context_loading.md).
6. Определи выбранную концепцию, `active_issue`, local registry, текущий этап и разрешённую область записи.

## Границы записи

Разрешённая запись в этом режиме: файлы активной концепции внутри `Concepts/<concept_id>/`, её local registry, state, output/export и связанный execution issue, если это разрешено текущим протоколом.

Запрещено менять сервисные протоколы, глобальные инструкции, global registry и `State/service_state.md` как часть работы над концепцией. Для такой задачи создаётся transfer route в `Service Mode`.

## Запись в GitHub

Перед записью подготовь пакет изменений: selected concept, active issue, reason, operation, target paths, pre-sha, local registry update and validation plan. После записи перечитай изменённые файлы из `GitHub`, проверь backlinks/output/export и зафиксируй `persistence_status`.

## Маркер ответа

Каждый ответ заверши блоком:

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

`stage` берётся из `current_stage`, `loaded_context` не должен заявлять непрочитанные файлы, `next_step` не перескакивает requirements/export validation.
