# Решение

[← Задача](README.md) | [Requirements](requirements.md) | [Contract](contract.md) | [Исполнение issue](../../Protocols/issue_execution.md)

## Предложение

```text
summary:
approach:
changed_paths:
state_changes:
registry_changes:
event_changes:
validation_changes:
risks:
alternatives_rejected:
```

## Проверки безопасности

- target paths находятся внутри scope активного режима;
- development files исключены;
- rollback plan существует для каждой записи;
- linked issue/dependency status известен;
- language и navigation checks запланированы;
- acceptance criteria сопоставлены с evidence paths или readback refs.

## Gate

Solution не является исполнением. Execution начинается только после того, как `contract.md` или равнозначное issue event определяет точные target paths, operation и validation plan.
