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

## P2-001 report

| Поле | Значение |
|---|---|
| Task | `P2-001 — Restore root README and top-level production governance` |
| Defects | `D-001`, `D-003`, `D-004`, `D-005`, `D-009`, `D-010`, `D-011`, `D-016`, `D-028` |
| Branch | `agent/phase2-patch-20260614T000000Z` |
| Operation scope | update `README.md`, `Registry/structure.md`, `Concepts/README.md`, `Templates/README.md`, `Inbox/README.md`, `Validation/final_check.md`, `Issues/issue_registry.jsonl`, `Issues/issue_events.jsonl`, `State/service_state.md`, `Issues/CB-P2/README.md`, `Validation/sync_report.md`; absent/no-write `Plans/cb008.md`, `Closure/status.md` |
| Acceptance evidence | README route graph; structure governance table; Concepts smoke decision; Templates/Inbox owner/source policy; registry/state/events/sync coupling |
| Open risk | Full global/local registry metadata is intentionally deferred to `P2-002`; final acceptance remains blocked until `P2-010`. |
| Next safe step | `P2-002` |

## P2-002 report

| Поле | Значение |
|---|---|
| Task | `P2-002 — Rebuild global and local page registries as navigation contract` |
| Defects | `D-002`, `D-011`, `D-012`, `D-014`, `D-015`, `D-016`, `D-023`, `D-041`, `D-061` |
| Branch | `agent/phase2-patch-20260614T000000Z` |
| Successful writes in this segment | `Registry/page_registry_schema.md`, `Templates/task/README.md`, `State/service_state.md`, `Issues/CB-P2/README.md`, `Validation/sync_report.md` |
| Pending writes | `Registry/page_registry.jsonl`, `Registry/structure.md`, `Concepts/smoke/page_registry.jsonl`, `Templates/concept/page_registry.jsonl`, `Templates/task/page_registry.jsonl`, `Issues/issue_registry.jsonl`, `Issues/issue_events.jsonl`, `Validation/final_check.md` |
| Partial evidence | schema expanded; task template route table is Russian-readable and clickable; service state and sync-report explicitly mark P2-002 as partial |
| Open risk | Registry/local-registry writes and registry/event/final-check coupling are not complete yet; P2-003 is blocked until P2-002 readback is coherent. |
| Next safe step | complete pending P2-002 writes |

## Status

`executing_with_evidence`: P2-002 is partial. Финальный статус меняется только после GitHub readback, PR diff gate и merge verification. Закрытие не объявляется.
