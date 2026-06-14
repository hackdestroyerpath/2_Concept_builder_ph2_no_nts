# Process

[← Smoke](README.md) | [Operating model](operating_model.md) | [Output](output.md)

## Dry-run scenario

1. Загрузить `State/execution_state.md` и выбрать `Concepts/smoke` как active object.
2. Проверить `README.md`, `concept_state.md`, `structure.md`, `page_registry.jsonl`.
3. Проверить pages `purpose`, `requirements`, `operating_model`, `process`, `output`, `export`.
4. Проверить, что local registry содержит owner/backlinks/source_of_truth.
5. Проверить отсутствие orphan/debris pages.
6. Сформировать output mapping и export manifest.
7. Перед закрытием перечитать файлы из `GitHub` и записать результат в `Validation/final_check.md`.

## Validation hooks

```text
readback_paths: Concepts/smoke/README.md; Concepts/smoke/page_registry.jsonl; Concepts/smoke/output.md; Concepts/smoke/export.md
expected_absent_paths: Concepts/smoke/o2.md; Concepts/smoke/output.txt; Concepts/smoke/e.txt
linked_issue: CB-009
```
