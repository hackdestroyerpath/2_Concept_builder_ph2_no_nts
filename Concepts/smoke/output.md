# Output

[← Smoke](README.md) | [Requirements](requirements.md) | [Export](export.md)

## Output summary

`Smoke validation fixture` подтверждает, что concept template можно представить как связанную production-сеть с локальным state, registry, process, output и export manifest.

## Requirement mapping

| Requirement | Output evidence | Result |
|---|---|---|
| `SMK-R-001` | `structure.md` и `page_registry.jsonl` описывают одинаковый набор strict pages. | passed_with_evidence |
| `SMK-R-002` | local registry содержит metadata, а не только path. | passed_with_evidence |
| `SMK-R-003` | эта страница содержит result summary and mapping. | passed_with_evidence |
| `SMK-R-004` | `export.md` содержит manifest fields. | passed_with_evidence |
| `SMK-R-005` | orphan/stub files перечислены как absent targets в final validation. | passed_with_evidence |

## Output status

```text
status: passed_with_evidence
linked_issue: CB-009
export_manifest: export.md
validation_anchor: ../../Validation/final_check.md
readback_anchor: ../../Validation/sync_report.md
```
