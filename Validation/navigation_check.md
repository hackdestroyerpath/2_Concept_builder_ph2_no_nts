# Navigation check

[← Final check](final_check.md) | [Registry](../Registry/page_registry.jsonl) | [Structure](../Registry/structure.md)

## Scope

```text
readback_ref: main after PR #6 merge 276b893043cd6f21f1ecf0cd18afc9faa6c5d52d plus final evidence writes
checked_area: README; Protocols; State; Issues; Concepts/smoke; Templates; Registry; Validation
status: passed_with_evidence
failed_checks: []
```

## Checks

| Check | Evidence | Status |
|---|---|---|
| Root entry routes to production zones | `README.md` links all top-level zones | passed_with_evidence |
| Global registry has owner/backlinks/source_of_truth | `Registry/page_registry.jsonl` uses extended schema rows | passed_with_evidence |
| Schema describes required fields | `Registry/page_registry_schema.md` | passed_with_evidence |
| Structure map matches target tree | `Registry/structure.md` | passed_with_evidence |
| Issues have active entry and per-issue artifacts | `Issues/README.md`, `Issues/CB-P2`, `CB-002`…`CB-009` | passed_with_evidence |
| Write/conflict/rollback routes are reachable | `README.md` → `Protocols/github_write_protocol.md` → conflict/rollback | passed_with_evidence |
| Smoke fixture is reachable | `Concepts/README.md` → `Concepts/smoke/README.md` | passed_with_evidence |
| Smoke local registry is not path-only | `Concepts/smoke/page_registry.jsonl` | passed_with_evidence |
| Task local registry is not path-only | `Templates/task/page_registry.jsonl` | passed_with_evidence |
| Concept local registry template is not path-only | `Templates/concept/page_registry.jsonl` | passed_with_evidence |
| Deprecated active zones are not in registry | `Plans/`, `Closure/`, `Issues/cb89.md`, `Concepts/smoke/o2.md` removed from active registry | passed_with_evidence |

## Expected absent paths

| Path | Expected result | Reason | Evidence |
|---|---|---|---|
| `Issues/cb89.md` | 404 after cleanup | mixed debris | `Validation/sync_report.md` absent-path checks |
| `Plans/cb008.md` | 404 after cleanup | migrated to validation/issue artifacts | `Validation/sync_report.md` absent-path checks |
| `Closure/status.md` | 404 after cleanup | assertion-only closure replaced | `Validation/sync_report.md` absent-path checks |
| `Concepts/smoke/o2.md` | 404 after cleanup | orphan/stub | `Validation/sync_report.md` absent-path checks |
