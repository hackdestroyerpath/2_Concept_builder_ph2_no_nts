# Issue execution

[← Реестр протоколов](protocol_index.md) | [Жизненный цикл issue](issue_lifecycle.md) | [Requirements protocol](requirements_protocol.md)

## Назначение

Протокол описывает выполнение `issue` после статуса `ready`.

## Вход

```text
issue_id:
mode:
active_object:
requirements:
allowed_scope:
acceptance_criteria:
validation_plan:
```

## Этапы выполнения

1. Перевести `issue` в `in_progress`.
2. Сформировать пакет изменений: цель, файлы, state, реестры, проверка.
3. Выполнить запись только в разрешённой области.
4. Перечитать изменённые файлы из `GitHub`.
5. Проверить acceptance criteria.
6. Обновить реестры, журнал событий и state.
7. Перевести `issue` в `review` или `done`.

## Report

Отчёт по выполнению должен включать:

```text
issue_id:
changed_paths:
validation_result:
persistence_status:
open_risks:
next_step:
```

## Блокировки

Если запись, проверка или критерии готовности не выполнены, `issue` получает статус `blocked` или `review`, но не `done`.
