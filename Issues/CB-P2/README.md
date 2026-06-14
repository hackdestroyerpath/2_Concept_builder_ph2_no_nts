# CB-P2 — Phase 2 patch

[← Issues](../README.md) | [Registry](../issue_registry.jsonl) | [Events](../issue_events.jsonl) | [Final check](../../Validation/final_check.md)

## Назначение

`CB-P2` — активный service issue для исправления утверждённого реестра D-001…D-063. Issue не является внешним audit-файлом; он хранит production-след patch-работы, route, cleanup decisions и validation anchors.

## Scope

- восстановить root README как service map;
- расширить registry schema и entries;
- канонизировать state/mode/context marker;
- усилить issue lifecycle, QA, requirements, solution, contract, write, conflict, rollback, validation;
- сохранить `Concepts/smoke` как validation fixture и удалить orphan/stub debris;
- заменить assertion-only closure evidence matrix.

## Cleanup decisions

| Путь | Решение |
|---|---|
| `Issues/cb89.md` | удалить после переноса сведений в `CB-008`, `CB-009`, registry/events |
| `Plans/cb008.md` | удалить после переноса в `Validation/cb008_closure_plan.md` |
| `Closure/status.md` | удалить; финальное состояние живёт в `Validation/final_check.md` |
| `Concepts/smoke/o2.md` | удалить как orphan/stub |

## Evidence anchors

- [`Validation/final_check.md`](../../Validation/final_check.md)
- [`Validation/navigation_check.md`](../../Validation/navigation_check.md)
- [`Validation/language_check.md`](../../Validation/language_check.md)
- [`Validation/sync_report.md`](../../Validation/sync_report.md)

## Status

`executing_with_evidence`: финальный статус меняется только после GitHub readback, PR diff gate и merge verification.
