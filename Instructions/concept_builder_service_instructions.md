# Инструкция проекта: Concept Builder Service Mode

[← К точке входа](../README.md)

## Роль

Ты работаешь в `Service Mode`: обслуживаешь саму систему `Concept Builder`, её production-файлы, протоколы, state, реестры, validation, шаблоны и сервисные `issue`.

## Источник истины

Источник истины — production-файлы репозитория `GitHub` `hackdestroyerpath/2_Concept_builder_ph2_no_nts`.

Не считай локальные черновики, вложенные архивы, prompt-ы, audit-материалы или checkpoint-и production-состоянием, пока соответствующие production-файлы не записаны и не перечитаны из `GitHub`.

## Старт

1. Прочитай [`../README.md`](../README.md).
2. Прочитай [`../State/service_state.md`](../State/service_state.md).
3. Прочитай [`../Protocols/protocol_index.md`](../Protocols/protocol_index.md).
4. Примени [`../Protocols/context_loading.md`](../Protocols/context_loading.md) и [`../Protocols/mode_routing.md`](../Protocols/mode_routing.md).
5. Определи `active_issue`, `current_stage`, разрешённые области чтения и записи.
6. Загружай только контекст, нужный для текущего bounded step.

## Границы записи

Разрешённая запись в этом режиме: `README.md`, `Instructions/`, `Protocols/`, `State/service_state.md`, service-часть `State/execution_state.md` только для repair/transfer patch, сервисные файлы `Issues/`, `Inbox/`, `Registry/`, `Validation/` и production-шаблоны, если они входят в активный `issue`.

Запрещено менять содержимое конкретной пользовательской концепции как service-action. Для такой работы нужен `Execution Mode`, selected concept и linked execution issue.

## Запись в GitHub

Перед записью подготовь пакет изменений: режим, active issue, reason, operation, target paths, pre-sha, validation plan и registry/state/event coupling. После записи перечитай изменённые файлы из `GitHub`, проверь expected content и обнови `Validation/sync_report.md`.

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

`stage` берётся из `current_stage`, `loaded_context` — из реально прочитанных файлов, `persistence_status` не может быть финальным без readback evidence.
