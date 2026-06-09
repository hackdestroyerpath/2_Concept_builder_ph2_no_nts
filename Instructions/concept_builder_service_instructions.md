# Инструкция проекта: Concept Builder Service Mode

[← К точке входа](../README.md)

## Роль

Ты работаешь в `Service Mode`: обслуживаешь саму систему `Concept Builder`, её production-файлы, протоколы, state, реестры и сервисные `issue`.

## Источник истины

Источник истины — репозиторий `GitHub`: `hackdestroyerpath/2_Concept_builder_ph2_no_nts`.

Не считай локальные черновики, переписку или вложенные архивы production-состоянием, пока соответствующие production-файлы не записаны и не перечитаны из `GitHub`.

## Старт

1. Прочитай [`../README.md`](../README.md).
2. Прочитай [`../State/service_state.md`](../State/service_state.md).
3. Прочитай [`../Protocols/protocol_index.md`](../Protocols/protocol_index.md).
4. Определи текущий `active_issue`, `current_stage`, разрешённые области чтения и записи.
5. Загружай только контекст, нужный для текущего действия.

## Границы записи

Разрешённая запись в этом режиме: `README.md`, `Instructions/`, `Protocols/`, `State/service_state.md`, сервисные файлы `Issues/`, `Inbox/`, `Registry/` и другие production-файлы системы, если они разрешены текущим протоколом.

Запрещено писать в файлы конкретной концепции внутри `Concepts/`, если задача относится к `Execution Mode`. Для такой задачи создай transfer-issue или останови переход с объяснением.

## Запись в GitHub

Перед записью подготовь пакет изменений: режим, причина, файлы, реестры, state и проверка. После записи перечитай изменённые файлы из `GitHub`, проверь ожидаемое содержимое и зафиксируй `persistence_status`.

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
