# Export

[← Smoke](README.md) | [Output](output.md) | [Concept export protocol](../../Protocols/concept_export.md)

## Manifest

```text
export_id: smoke-export-2026-06-14
concept_id: smoke
active_issue: CB-009
owner_mode: Execution Mode
export_scope: validation_fixture
source_paths: README.md; purpose.md; requirements.md; operating_model.md; process.md; output.md; concept_state.md; page_registry.jsonl
excluded_paths: o2.md; output.txt; e.txt; development handoff; audit notes
format: markdown_bundle
intended_audience: Service Mode validation and Execution Mode bootstrap test
readiness_status: evidence_pending_final_readback
validation_anchor: ../../Validation/final_check.md
```

## Acceptance gates

| Gate | Evidence |
|---|---|
| scope is explicit | `export_scope` and `source_paths` are listed |
| output exists | [`output.md`](output.md) |
| local registry exists | [`page_registry.jsonl`](page_registry.jsonl) |
| source pages are linked | [`README.md`](README.md) |
| orphan files absent | final validation checks expected 404/absence |

## Notes

This export is a validation fixture export, not a deliverable for an external customer.
