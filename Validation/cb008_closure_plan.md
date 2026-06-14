# CB-008 closure plan

[← Dry run](cb008_dry_run.md) | [Final check](final_check.md) | [Issue CB-008](../Issues/CB-008/README.md)

## Scope

| Area | Closure evidence |
|---|---|
| Service Mode route | issue lifecycle, task flow and registry events updated |
| Task template | local task registry and artifact gates updated |
| GitHub recovery | write, conflict and rollback protocols updated |
| Event records | `service-event-000008`…`service-event-000012` record Phase 2 patch evidence |
| Page registry | global registry rebuilt with owner/backlinks/source_of_truth |

## Closure sequence

1. Replace assertion-only dry-run result with evidence-backed scenarios.
2. Migrate valid information from `Plans/cb008.md` into `Issues/CB-008/README.md` and this file.
3. Remove `Plans/cb008.md` after migration.
4. Verify branch readback and update `Validation/sync_report.md`.
5. Close via `Validation/final_check.md` only after D-001…D-063 matrix has no blocker.

## Status

`closure_ready_after_readback`: this plan is valid only together with final readback and PR/base verification.
