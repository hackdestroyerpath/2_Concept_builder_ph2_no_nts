# Протокол приёма входа и создания `issue`

[← К реестру протоколов](protocol_index.md) | [Issues](../Issues/README.md) | [Inbox](../Inbox/README.md)

## Цель

Превратить входной текст, файлы или команду пользователя в проверяемые кандидаты `issue` с reason и сохранённым provenance.

## Входы

- текст пользователя;
- точка входа или attachment;
- текущий режим;
- `Issues/issue_registry.jsonl`;
- `Issues/issue_events.jsonl`;
- `Inbox/README.md`.

## Процесс

1. Создать `input_id` и сохранить входной материал в `Inbox/{input_id}/`.
2. Разобрать вход на один или несколько кандидатов `issue`.
3. Для каждого кандидата сформировать `issue_id`, тип, режим, краткий title, reason и предполагаемый owner.
4. Записать кандидатов в registry со статусом `proposed`.
5. Создать для каждого кандидата минимальные `state.md` и `reason.md`.
6. Записать событие intake в `issue_events.jsonl`.
7. Перечитать registry, события и созданные файлы.
8. Показать пользователю таблицу кандидатов и допустимые решения.

## Правило reason

`issue` без reason не создаётся. Reason должен объяснять, какой вход породил задачу, почему она принадлежит текущему режиму и какой результат ожидается.

## Выход

Сохранённый набор кандидатов `issue`, reason-файлы, event и marker с `dialogue_state: awaiting_issue_registry_decision`.
