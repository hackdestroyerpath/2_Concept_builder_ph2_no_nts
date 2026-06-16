# CB-009 — Smoke fixture and export

[← Issues](../README.md) | [Smoke fixture](../../Concepts/smoke/README.md) | [Execution state](../../State/execution_state.md)

## Provenance

Статус: `fixed_with_evidence`. `Concepts/smoke` сохранён как validation fixture, а не как пользовательская концепция. Issue объясняет, почему fixture остаётся в production tree и как проверяется export readiness.

## Scope

- удалить orphan/stub fixture debris;
- согласовать `README.md`, purpose, requirements, operating model, process, output, export, state и local registry;
- связать `State/execution_state.md` с fixture readiness;
- записать export dry-run evidence.

## Evidence

| Evidence | Роль | Result |
|---|---|---|
| `Concepts/smoke/README.md` | fixture entrypoint | passed_with_evidence |
| `Concepts/smoke/page_registry.jsonl` | local registry | passed_with_evidence |
| `Concepts/smoke/output.md` | output evidence | passed_with_evidence |
| `Concepts/smoke/export.md` | export manifest | passed_with_evidence |
| `State/execution_state.md` | execution state and scope | passed_with_evidence |
| `Validation/sync_report.md` | readback and absence evidence | passed_with_evidence |

## Cleanup

Alternate output/export scratch files не используются как production output/export page. Absence is verified in the final sync report.
