# CB-008 — Dry-run validation

[← Issues](../README.md) | [Dry run](../../Validation/cb008_dry_run.md) | [Closure plan](../../Validation/cb008_closure_plan.md)

## Provenance

Статус: `fixed_with_evidence`. Старые `Plans/cb008.md` и смешанный `Issues/cb89.md` не сохраняются как production lifecycle artifacts. Их валидный intent перенесён сюда и в `Validation/`.

## Scope

- проверить task-template route без записи development files;
- проверить поля issue registry и event coupling;
- подтвердить QA skip reason и requirements gate;
- проверить cleanup/closure plan.

## Evidence

| Evidence | Роль |
|---|---|
| `Validation/cb008_dry_run.md` | observable dry-run |
| `Validation/cb008_closure_plan.md` | closure plan без assertion-only status |
| `Issues/issue_events.jsonl` | migration and cleanup event trace |
| `Templates/task/README.md` | task artifact route |

## Cleanup

`Plans/cb008.md` удалён после migration. `Issues/cb89.md` удалён после разделения на `CB-008` и `CB-009`.