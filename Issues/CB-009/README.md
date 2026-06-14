# CB-009 — Smoke fixture and export

[← Issues](../README.md) | [Smoke fixture](../../Concepts/smoke/README.md) | [Execution state](../../State/execution_state.md)

## Provenance

Статус: `fixed_with_evidence`. `Concepts/smoke` сохранён как validation fixture, а не как пользовательская концепция. Issue объясняет, почему fixture остаётся в production tree и как проверяется export readiness.

## Scope

- удалить orphan/stub `Concepts/smoke/o2.md`;
- согласовать `README.md`, purpose, requirements, operating model, process, output, export, state и local registry;
- связать `State/execution_state.md` с fixture readiness;
- записать export dry-run evidence.

## Evidence

| Evidence | Роль |
|---|---|
| `Concepts/smoke/README.md` | fixture entrypoint |
| `Concepts/smoke/page_registry.jsonl` | local registry |
| `Concepts/smoke/output.md` | output evidence |
| `Concepts/smoke/export.md` | export manifest |
| `State/execution_state.md` | execution state and scope |

## Cleanup

`Concepts/smoke/o2.md` удалён. Alternative `output.txt` или `e.txt` не используются как production output/export page.