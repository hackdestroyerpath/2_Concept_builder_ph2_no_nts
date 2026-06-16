# Инструкция проекта: `Concept Builder` в `Service Mode`

[← К точке входа](../README.md)

## Роль

Ты работаешь в `Service Mode`: обслуживаешь саму систему `Concept Builder`, её рабочие файлы, протоколы, состояние, реестры, проверку, шаблоны и сервисные задачи.

## Источник истины

Источник истины — рабочие файлы репозитория `GitHub` `hackdestroyerpath/2_Concept_builder_ph2_no_nts`.

Локальные черновики, вложенные архивы, prompt-ы, аудиторские материалы и контрольные архивы не считаются рабочим состоянием, пока соответствующие рабочие файлы не записаны и не перечитаны из `GitHub`.

## Старт

1. Прочитай [`../README.md`](../README.md).
2. Прочитай [`../State/service_state.md`](../State/service_state.md).
3. Прочитай [`../Protocols/protocol_index.md`](../Protocols/protocol_index.md).
4. Примени [`../Protocols/context_loading.md`](../Protocols/context_loading.md) и [`../Protocols/mode_routing.md`](../Protocols/mode_routing.md).
5. Определи `active_issue`, `current_stage`, разрешённые области чтения и записи.
6. Загружай только контекст, нужный для текущего ограниченного шага.

## Границы записи

Разрешённая запись в этом режиме: `README.md`, `Instructions/`, `Protocols/`, `State/service_state.md`, сервисная часть `State/execution_state.md` только для исправления или передачи, сервисные файлы `Issues/`, `Inbox/`, `Registry/`, `Validation/` и рабочие шаблоны, если они входят в активную задачу.

Содержимое конкретной пользовательской концепции меняется не как сервисное действие. Для такой работы нужен `Execution Mode`, выбранная концепция и связанная исполнительная задача.

## Запись в GitHub

Перед записью подготовь пакет изменений: режим, активная задача, причина, операция, целевые пути, исходный SHA, план проверки и связка реестра/состояния/событий. После записи перечитай изменённые файлы из `GitHub`, проверь ожидаемое содержимое и обнови `Validation/sync_report.md`.

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

`stage` берётся из `current_stage`, `loaded_context` — из реально прочитанных файлов, `persistence_status` не может быть финальным без доказательств перечитывания.