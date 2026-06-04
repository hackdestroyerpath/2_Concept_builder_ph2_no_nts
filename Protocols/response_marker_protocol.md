# Протокол маркера ответа

[← К реестру протоколов](protocol_index.md)

## Назначение

Файл задаёт обязательный короткий блок состояния в ответах агента.

## Поля

`mode`, `active_object`, `active_issue`, `stage`, `loaded_context`, `persistence_status`, `next_step`, `return_anchor`.

## Правила

`mode` и `active_issue` берутся из текущего state. `loaded_context` перечисляет только реально загруженные ключевые файлы. `persistence_status` отражает фактический результат сохранения. `next_step` содержит одно безопасное следующее действие. `return_anchor` указывает файл или раздел возврата.
