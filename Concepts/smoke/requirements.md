# Requirements

[← Smoke](README.md) | [Purpose](purpose.md) | [Output](output.md) | [Export](export.md)

## Requirement tree

| ID | Requirement | Acceptance evidence |
|---|---|---|
| `SMK-R-001` | Fixture содержит все страницы concept template. | `structure.md` и `page_registry.jsonl` перечисляют одинаковые pages. |
| `SMK-R-002` | Local registry не path-only. | Каждая строка содержит owner, parent, children, links, source_of_truth. |
| `SMK-R-003` | Output page описывает результат и связь с требованиями. | `output.md` содержит mapping `SMK-R-*`. |
| `SMK-R-004` | Export page является manifest, а не одиночной декларацией. | `export.md` содержит source paths, audience, format, validation gates. |
| `SMK-R-005` | Orphan/stub pages отсутствуют. | `o2.md`, `output.txt`, `e.txt` удалены или отсутствуют. |

## Inputs and outputs

```text
inputs: Templates/concept; Protocols/execution_bootstrap.md; Protocols/concept_export.md
outputs: Concepts/smoke/output.md; Concepts/smoke/export.md; Concepts/smoke/page_registry.jsonl
criteria_status: pending_final_readback
```
