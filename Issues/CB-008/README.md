# CB-008 — Dry-run validation

[← Issues](../README.md) | [Dry run](../../Validation/cb008_dry_run.md) | [Closure plan](../../Validation/cb008_closure_plan.md)

## Provenance

Status is `fixed_with_evidence`. The old `Plans/cb008.md` and mixed `Issues/cb89.md` are not retained as production lifecycle artifacts. Their valid intent is migrated here and into `Validation/`.

## Scope

- instantiate task-template route without writing development files;
- check issue registry fields and event coupling;
- confirm QA skip reason and requirements gate;
- verify cleanup/closure plan.

## Evidence

- `Validation/cb008_dry_run.md`
- `Validation/cb008_closure_plan.md`
- `Issues/issue_events.jsonl`
- `Templates/task/README.md`

## Cleanup

`Plans/cb008.md` is removed after migration. `Issues/cb89.md` is removed after split into `CB-008` and `CB-009`.
