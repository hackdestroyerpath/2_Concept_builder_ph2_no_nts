# CB-P2 — Phase 2 patch

[← Issues](../README.md) | [Registry](../issue_registry.jsonl) | [Events](../issue_events.jsonl) | [Final check](../../Validation/final_check.md) | [Sync report](../../Validation/sync_report.md)

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
- [`Issues/issue_events.jsonl`](../issue_events.jsonl)

## P2-000 report

| Поле | Значение |
|---|---|
| Task | `P2-000 — Intake, freeze snapshot, reopen closure as audit-approved patch` |
| Defects | `D-006`, `D-017`, `D-049`, `D-052` |
| Branch | `agent/phase2-patch-20260614T000000Z` |
| Base SHA | `05607f14d3baa10fdb9427f5810bda4d47e2cb4e` |
| Operation scope | update `Validation/final_check.md`, `Issues/issue_registry.jsonl`, `Issues/issue_events.jsonl`, `State/service_state.md`, `Issues/CB-P2/README.md`, `Validation/sync_report.md`; read/no-change `README.md`; absent/no-write `Closure/status.md` |
| Acceptance evidence | active issue exists; final check is reopened as evidence gate; sync-report uses current branch; state/event registry are coupled |
| Open risk | Full D-001…D-063 matrix is not final until P2-010. |
| Next safe step | `P2-001` |

## Status

`executing_with_evidence`: финальный статус меняется только после GitHub readback, PR diff gate и merge verification. На P2-000 issue остаётся активным; закрытие не объявляется.
