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

Запись в рабочий контур разрешена только тогда, когда этот контракт или равнозначное событие задачи (`issue event`) определяет целевые пути (`target_paths`), операцию (`operation`), исходное состояние (`pre-sha/source`), план валидации (`validation_plan`) и план отката (`rollback_plan`).

## Нарушение контракта

Если фактически изменённые пути отличаются от `target_paths`, статус получает значение `conflict`, затем запускается `github_conflict_recovery.md`.
