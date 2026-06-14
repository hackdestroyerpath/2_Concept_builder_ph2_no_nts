# CB-007 — Task flow hardening

[← Issues](../README.md) | [Task flow hardening](../../Protocols/task_flow_hardening.md) | [Task template](../../Templates/task/README.md)

## Provenance

Статус: `reconstructed_with_evidence`. Artifact сохраняет operational intent для priority, approval, cleanup и provenance controls.

## Scope

- priority и dependency fields в registry;
- approval, rejection и discussion commands;
- persisted QA skip reason;
- cleanup statuses;
- return-anchor для resumed work.

## Evidence

| Evidence | Роль |
|---|---|
| `Protocols/task_flow_hardening.md` | lifecycle hardening |
| `Protocols/complex_and_linked_issues.md` | dependency and child issue route |
| `Templates/task/README.md` | task artifact chain |
| `Issues/issue_registry.jsonl` | machine status and dependencies |

## Closure rule

Task не переходит от contract к execution без persisted requirements, approved contract или documented bounded skip reason.