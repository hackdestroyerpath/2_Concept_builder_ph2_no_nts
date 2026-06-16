# Требования

[← Задача](README.md) | [Вопросы и ответы](question_answer.md) | [Контракт](contract.md) | [Протокол](../../Protocols/requirements_protocol.md)

## Дерево требований

| ID | Требование | Источник | Причина | Связанные вопросы, входы или задачи | Критерии приёмки | Статус |
|---|---|---|---|---|---|---|
| `REQ-001` |  | пользователь/система/репозиторий/событие/протокол |  |  |  | `proposed` |

## Область

```text
goal:
in_scope:
out_of_scope:
inputs:
outputs:
assumptions:
constraints:
risks:
```

## Утверждение

```text
approval_status: proposed | approved_with_scope | rejected | skipped_with_reason | blocked
approved_by:
approved_at:
approval_source:
blocking_questions:
scope_exclusions:
validation_plan:
```

## Шлюз

Исполнение не может начаться, пока требования не имеют статус `approved_with_scope` или пока задача не имеет явную причину ограниченного пропуска с источником и критериями проверки.