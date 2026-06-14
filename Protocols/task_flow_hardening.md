# Task flow hardening

[← Реестр протоколов](protocol_index.md) | [Issue lifecycle](issue_lifecycle.md) | [Complex issues](complex_and_linked_issues.md)

## Назначение

Протокол усиливает task flow так, чтобы задача не теряла priority, approval, provenance, dependencies, cleanup и evidence. Ничто не закрывается по настроению, даже если настроение у Markdown сегодня солнечное.

## Registry fields

```text
priority: normal | major | blocker
approval: requested | approved | rejected | reconstructed | not_required
provenance: user_request | repo_state | validation_finding | transfer | audit_approved_patch | reconstructed_repo_baseline
cleanup: retain | pending | removed_with_reason | migrated_then_removed
dependencies: []
return_anchor:
```

## Decision events

| Event | Required fields |
|---|---|
| approval_requested | approver, reason, target scope |
| approved | approver, requirements, contract/evidence |
| rejected | reason, affected paths |
| cleanup_required | path, reason, migration target |
| cleanup_removed | path, delete sha/commit, validation anchor |
| validation_passed | checked paths, ref, evidence matrix |
| rollback | trigger, affected paths, rollback sha |

## Priority policy

| Priority | Meaning |
|---|---|
| `blocker` | blocks closure or core operation |
| `major` | required for reliable production use |
| `normal` | useful hardening, does not block closure |

## Closure gate

A task reaches `fixed_with_evidence` only if registry, events, state, readback and validation agree. If a child issue is unresolved, parent stays `blocked` or `validation`, not closed.
