# Инструкция проекта: Concept Builder Execution Mode

[← К точке входа](../README.md)

## Роль

Ты работаешь в `Execution Mode`: ведёшь конкретную концепцию внутри `Concepts/`, создаёшь и обновляешь её связанную сеть MD-файлов, требования, process, operating model, output и export.

## Источник истины

Источник истины — репозиторий `GitHub`: `hackdestroyerpath/2_Concept_builder_ph2_no_nts`.

Работай только с выбранной концепцией и её разрешёнными `issue`. Не смешивай задачи конкретной концепции с обслуживанием самой системы.

## Старт

1. Прочитай [`../README.md`](../README.md).
2. Прочитай [`../State/execution_state.md`](../State/execution_state.md).
3. Прочитай [`../Concepts/README.md`](../Concepts/README.md).
4. Прочитай [`../Protocols/protocol_index.md`](../Protocols/protocol_index.md).
5. Определи выбранную концепцию, `active_issue`, текущий этап и разрешённую область записи.
6. Загружай только локальный контекст концепции, нужный для текущего действия.

## Границы записи

Разрешённая запись в этом режиме: файлы активной концепции внутри `Concepts/`, связанные с ней `issue`, её state, output и production-export, если это разрешено текущим протоколом.

Запрещено менять сервисные протоколы, глобальные инструкции и service-state как часть работы над концепцией. Для такой задачи создай transfer-issue в `Service Mode` или останови переход.

## Запись в GitHub

Перед записью подготовь пакет изменений: активная концепция, причина, файлы, реестры, state и проверка. После записи перечитай изменённые файлы из `GitHub`, проверь ожидаемое содержимое и зафиксируй `persistence_status`.

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
