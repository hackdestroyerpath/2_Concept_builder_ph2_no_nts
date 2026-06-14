# CB-009 — Smoke fixture and export

[← Issues](../README.md) | [Smoke fixture](../../Concepts/smoke/README.md) | [Execution state](../../State/execution_state.md)

## Provenance

Status is `fixed_with_evidence`. `Concepts/smoke` is retained as a validation fixture, not as a user-facing concept. The issue documents why it remains and how export readiness is checked.

## Scope

- remove orphan/stub `Concepts/smoke/o2.md`;
- make `README.md`, `purpose`, `requirements`, `operating_model`, `process`, `output`, `export`, state and local registry coherent;
- align `State/execution_state.md` with fixture readiness;
- record export dry-run evidence.

## Evidence

- `Concepts/smoke/README.md`
- `Concepts/smoke/page_registry.jsonl`
- `Concepts/smoke/output.md`
- `Concepts/smoke/export.md`
- `State/execution_state.md`

## Cleanup

`Concepts/smoke/o2.md` is removed. No alternate `output.txt` or `e.txt` is used as the production output/export page.
