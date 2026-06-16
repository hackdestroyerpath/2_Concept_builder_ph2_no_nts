# Проверка навигации

[← Финальная проверка](final_check.md) | [Registry](../Registry/page_registry.jsonl) | [Structure](../Registry/structure.md)

## Область

```text
readback_ref: main_after_pr7_merge
checked_area: README; Protocols; State; Issues; Concepts/smoke; Templates; Registry; Validation
status: passed_after_readback
failed_checks: []
```

## Проверки

| Проверка | Доказательство | Статус |
|---|---|---|
| Root entry ведёт в production zones | `README.md` содержит ссылки на все top-level zones | passed_with_evidence |
| Global registry содержит owner/backlinks/source_of_truth | `Registry/page_registry.jsonl` использует extended schema rows | passed_with_evidence |
| Schema описывает required fields | `Registry/page_registry_schema.md` | passed_with_evidence |
| Structure map совпадает с target tree | `Registry/structure.md` | passed_with_evidence |
| Issues имеют active entry и per-issue artifacts | `Issues/README.md`, `Issues/CB-P2`, `CB-002`…`CB-009` | passed_with_evidence |
| Маршруты записи и восстановления достижимы | `README.md` → протоколы записи и восстановления | passed_with_evidence |
| Smoke fixture достижим | `Concepts/README.md` → `Concepts/smoke/README.md` | passed_with_evidence |
| Smoke local registry не является path-only | `Concepts/smoke/page_registry.jsonl` | passed_with_evidence |
| Task local registry не является path-only | `Templates/task/page_registry.jsonl` | passed_with_evidence |
| Concept local registry template не является path-only | `Templates/concept/page_registry.jsonl` | passed_with_evidence |
| Deprecated active zones отсутствуют в registry | `Plans/`, `Closure/`, `Issues/cb89.md`, `Concepts/smoke/o2.md` исключены из active registry | passed_with_evidence |

## Ожидаемо отсутствующие paths

| Path | Ожидаемый результат | Причина | Доказательство |
|---|---|---|---|
| `Issues/cb89.md` | 404 / absent | смешанный debris | absent-path checks в `Validation/sync_report.md` |
| `Plans/cb008.md` | 404 / absent | перенесён в validation/issue artifacts | absent-path checks в `Validation/sync_report.md` |
| `Closure/status.md` | 404 / absent | assertion-only closure заменён evidence | absent-path checks в `Validation/sync_report.md` |
| `Concepts/smoke/o2.md` | 404 / absent | orphan/stub | absent-path checks в `Validation/sync_report.md` |
