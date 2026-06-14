# Complex and linked issues

[← Реестр протоколов](protocol_index.md) | [Issue lifecycle](issue_lifecycle.md) | [Issue execution](issue_execution.md)

## Назначение

Протокол управляет parent/child/dependency связями, transfer между режимами и блокировками. Цель — не дать одной “маленькой” задаче тайно переписать полрепозитория, этот жанр уже занят человечеством.

## Link types

| Type | Meaning | Blocks closure |
|---|---|---|
| `parent` | объединяет child issues | yes, until required children done |
| `child` | выполняет часть parent scope | parent depends on status |
| `depends_on` | требует output другого issue | yes |
| `blocks` | текущий issue мешает другому | yes for blocked issue |
| `relates_to` | контекстная связь без блокировки | no |
| `transfer` | работа переходит между Service/Execution mode | yes until receiving issue exists |

## Registry extension

```json
{"parent_issue":"CB-000","child_issues":["CB-001"],"depends_on":["CB-002"],"blocks":[],"related_issues":[],"transfer_to":null,"rollup_status":"waiting|ready|blocked|fixed_with_evidence"}
```

## Rules

1. Child issue has its own reason, scope, owner mode and acceptance criteria.
2. Parent issue cannot reach `fixed_with_evidence` while required child is not validated.
3. Cycles are `blocked` until a human decision or scope split.
4. Transfer creates a receiving issue before write in the other mode.
5. Roll-up event names child statuses and evidence refs.

## Closure gate

Parent closure requires all required children fixed with evidence, dependencies resolved or explicitly removed with reason, registry/events updated and final validation passed.
