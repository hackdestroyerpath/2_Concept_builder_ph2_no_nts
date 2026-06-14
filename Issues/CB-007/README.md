# CB-007 — Task flow hardening

[← Issues](../README.md) | [Task flow hardening](../../Protocols/task_flow_hardening.md) | [Task template](../../Templates/task/README.md)

## Provenance

Status is `reconstructed_with_evidence`. This artifact preserves the operational intent of priority, approval, cleanup and provenance controls.

## Reconstructed scope

- priority and dependency fields in registry;
- approval/rejection/discussion commands;
- QA skip reason;
- cleanup statuses;
- return-anchor for resumed work.

## Evidence

- `Protocols/task_flow_hardening.md`
- `Protocols/complex_and_linked_issues.md`
- `Templates/task/README.md`
- `Issues/issue_registry.jsonl`

## Closure rule

A task cannot move from contract to execution without persisted requirements and an approved contract.
