# Task flow hardening

[← Реестр протоколов](protocol_index.md) | [Issue lifecycle](issue_lifecycle.md) | [Complex issues](complex_and_linked_issues.md) | [Task template](../Templates/task/README.md)

## Назначение

Протокол усиливает task flow так, чтобы задача не теряла priority, approval, provenance, dependencies, cleanup и evidence. Ничто не принимается по настроению, даже если настроение у Markdown сегодня солнечное.

## Registry fields

```text
priority: normal | major | blocker
approval: requested | approved | rejected | reconstructed | not_required
provenance: user_request | repo_state | validation_finding | transfer | audit_approved_patch | reconstructed_repo_baseline
cleanup: retain | pending | removed_with_reason | migrated_then_removed
dependencies: []
current_task:
current_rework_segment:
next_task:
return_anchor:
```

## Decision events

| Event | Required fields |
|---|---|
| `approval_requested` | approver, reason, target scope |
| `approved` | approver, requirements, contract/evidence |
| `rejected` | reason, affected paths |
| `qa_skipped_with_reason` | reason, source, why safe |
| `requirements_scoped` | requirement IDs, source refs, acceptance criteria |
| `contract_approved` | target paths, operation, validation plan, rollback plan |
| `cleanup_required` | path, reason, migration target |
| `cleanup_removed` | path, absence evidence, validation anchor |
| `validation_verified` | checked paths, ref, evidence matrix |
| `rollback` | trigger, affected paths, rollback sha |

## Priority policy

| Priority | Meaning |
|---|---|
| `blocker` | blocks final validation or core operation |
| `major` | required for reliable production use |
| `normal` | useful hardening, does not block final validation by itself |

## Transition matrix

| From | Required evidence | To |
|---|---|---|
| `proposed` | reason, provenance, priority | `requirements` |
| `requirements` | QA answer or skip reason + requirement IDs | `contract` |
| `contract` | target paths + validation/rollback plan | `in_progress` |
| `in_progress` | write/readback or documented no-write result | `review_required` |
| `review_required` | registry/state/event/validation agree | `fixed_with_evidence` |
| any | unresolved dependency, conflict, missing evidence | `blocked` |

## Closure gate

A task reaches `fixed_with_evidence` only if registry, events, state, readback and validation agree. If a child issue or dependency is unresolved, parent stays `blocked` or `review_required`.
