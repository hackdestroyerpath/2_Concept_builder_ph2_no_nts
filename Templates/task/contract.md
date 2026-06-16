# Контракт

[← Задача](README.md) | [Решение](solution.md) | [Отчёт](report.md) | [Протокол записи](../../Protocols/github_write_protocol.md)

## Контракт исполнения

```text
contract_id:
active_issue:
approved_requirements:
qa_or_skip_reason:
inputs:
outputs:
target_paths:
allowed_operations: create | update | delete | move
state_change:
registry_change:
event_change:
validation_plan:
rollback_plan:
approval_status: proposed | approved_with_scope | rejected | blocked
approved_by:
approved_at:
return_anchor:
```

## Контроль записи

Production-запись разрешена только тогда, когда этот contract или равнозначное issue event определяет target paths, operation, pre-sha/source, validation plan и rollback plan.

## Нарушение контракта

Если фактически изменённые paths отличаются от `target_paths`, status становится `conflict`, а затем запускается `github_conflict_recovery.md`.
