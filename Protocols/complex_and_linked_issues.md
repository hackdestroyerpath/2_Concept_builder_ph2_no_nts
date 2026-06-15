# Complex and linked issues

[← Реестр протоколов](protocol_index.md) | [Issue lifecycle](issue_lifecycle.md) | [Issue execution](issue_execution.md)

## Назначение

Протокол управляет parent/child/dependency связями, transfer между режимами, cleanup decisions и roll-up evidence. Цель — не дать одной “маленькой” задаче тайно переписать полрепозитория, этот жанр уже занят человечеством.

## Link types

| Type | Meaning | Blocks parent validation |
|---|---|---|
| `parent` | объединяет child issues | yes, until required children resolved |
| `child` | выполняет часть parent scope | parent depends on child state |
| `depends_on` | требует output другого issue/path | yes |
| `blocks` | текущий issue мешает другому | yes for blocked target |
| `relates_to` | контекстная связь без блокировки | no |
| `transfer` | работа переходит между `Service Mode` и `Execution Mode` | yes until receiver exists |
| `cleanup` | path retained/migrated/removed with reason | yes if unsafe or unverified |

## Dependency state machine

```text
proposed -> required -> waiting_on_parent | waiting_on_child | waiting_on_external
required -> resolved_with_evidence
required -> removed_with_reason
waiting_* -> blocked
blocked -> resolved_with_evidence only after event + validation evidence
cycle_detected -> blocked_until_scope_split
transfer_required -> receiver_issue_created -> resolved_with_evidence
```

## Registry extension

```json
{"parent_issue":"CB-000","child_issues":["CB-001"],"depends_on":["CB-002"],"blocks":[],"related_issues":[],"transfer_to":null,"dependency_state":"required","rollup_status":"waiting|blocked|resolved_with_evidence|removed_with_reason","return_anchor":"Validation/sync_report.md"}
```

## Rules

1. Child issue has its own reason, scope, owner mode and acceptance criteria.
2. Parent issue cannot reach `fixed_with_evidence` while required child or dependency is unresolved.
3. Cycles are `blocked` until scope split, dependency removal with reason, or explicit human decision.
4. Transfer creates a receiving issue before write in the other mode.
5. Roll-up event names child statuses, evidence refs and unresolved risks.
6. Cleanup decision names migrated target or absence evidence.
7. Return anchor must survive every parent/child handoff.

## Roll-up event format

```text
event_type: dependency_rollup | child_issue_rollup | transfer_rollup | cleanup_rollup
parent_issue:
child_issues:
dependency_state:
evidence:
blocked_items:
return_anchor:
```

## Validation gate

Parent validation requires all required children resolved with evidence, dependencies resolved or removed with reason, registry/events updated, and final validation evidence recorded.
