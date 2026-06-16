# Output

[← Smoke](README.md) | [Requirements](requirements.md) | [Export](export.md)

## Сводка output

Фикстура `smoke` подтверждает, что concept template можно представить как связанную production-сеть с локальным state, registry, process, output и export manifest.

## Связь с требованиями

| Требование | Доказательство output | Результат |
|---|---|---|
| `SMK-R-001` | `structure.md` и `page_registry.jsonl` описывают одинаковый набор strict pages. | passed_with_evidence |
| `SMK-R-002` | local registry содержит metadata, а не только path. | passed_with_evidence |
| `SMK-R-003` | эта страница содержит сводку результата и mapping. | passed_with_evidence |
| `SMK-R-004` | `export.md` содержит manifest fields. | passed_with_evidence |
| `SMK-R-005` | orphan/stub files перечислены как absent targets в финальной validation. | passed_with_evidence |

## Статус output

```text
status: passed_with_evidence
linked_issue: CB-009
export_manifest: export.md
validation_anchor: ../../Validation/final_check.md
readback_anchor: ../../Validation/sync_report.md
```