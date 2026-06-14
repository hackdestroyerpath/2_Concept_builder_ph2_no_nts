# Contract

[← Task](README.md) | [Solution](solution.md) | [Report](report.md) | [Write protocol](../../Protocols/github_write_protocol.md)

## Execution contract

```text
contract_id:
active_issue:
approved_requirements:
inputs:
outputs:
target_paths:
allowed_operations: create | update | delete | move
state_change:
registry_change:
event_change:
validation_plan:
rollback_plan:
approval_status: proposed | approved | rejected
approved_by:
approved_at:
```

## Gate

A production write is allowed only when this contract or equivalent issue event defines target paths, operation and validation plan.

## Contract breach

If actual changed paths differ from `target_paths`, status becomes `conflict` and `github_conflict_recovery.md` starts.
