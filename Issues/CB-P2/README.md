# CB-P2 — Phase 2 patch

[← Issues](../README.md) | [Registry](../issue_registry.jsonl) | [Events](../issue_events.jsonl) | [Final check](../../Validation/final_check.md) | [Sync report](../../Validation/sync_report.md)

## Назначение

`CB-P2` — активный service issue для исправления утверждённого реестра D-001…D-063. Issue хранит production-след patch-работы, route, cleanup decisions и validation anchors.

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

## Segment reports

| Step | Task | Defects | Evidence | Next |
|---|---|---|---|---|
| `P2-000` | Intake, freeze snapshot, reopen closure | `D-006`, `D-017`, `D-049`, `D-052` | active issue, reopened validation gate, registry/state/events/sync coupling | `P2-001` |
| `P2-001` | Root README and top-level governance | `D-001`, `D-003`, `D-004`, `D-005`, `D-009`, `D-010`, `D-011`, `D-016`, `D-028` | README route graph, structure governance, smoke decision | `P2-002` |
| `P2-002` | Global/local registries | `D-002`, `D-011`, `D-012`, `D-014`, `D-015`, `D-016`, `D-023`, `D-041`, `D-061` | registry schema, global/local registry metadata, debris exclusion | `P2-003` |
| `P2-003` | State/context/mode/marker | `D-018`…`D-028` | canonical state schema, context dry-run, marker mapping, instruction counts | `P2-004` |
| `P2-004` | Protocol index and routing cards | `D-012`, `D-023`, `D-024`, `D-042` | route matrix, protocol cards, existing issue resume flow | `P2-005` |
| `P2-005` | Issue registry, events and per-issue artifacts | `D-029`…`D-037` | `Issues/README.md`, `CB-002`…`CB-009`, registry row, event `service-event-000018`; checkpoint PR #5 merged at `79fabaefb8c03876078606bb02e4dbda6017f5bd` | `P2R-000` |
| `P2R-000` | Post-merge truth-source normalization | truth-source contradiction after rejected checkpoint | `README.md`, `State/service_state.md`, `Issues/CB-P2/README.md`, registry, events, `Validation/final_check.md`, `Validation/sync_report.md`; event `service-event-000019` | readback this batch, then `P2-006` |

## P2R-000 report

| Поле | Значение |
|---|---|
| Task | `P2R-000 — Resume from merged checkpoint and normalize truth sources` |
| Branch | `agent/phase2-rework-20260614T223441Z` |
| Base | `main` at merge commit `79fabaefb8c03876078606bb02e4dbda6017f5bd` |
| PR evidence | PR `#5` is merged; checkpoint body states scope through `P2-005` and explicitly not final |
| Operation scope | update `README.md`, `State/service_state.md`, `Issues/CB-P2/README.md`, `Issues/issue_registry.jsonl`, `Issues/issue_events.jsonl`, `Validation/final_check.md`, `Validation/sync_report.md` |
| Acceptance evidence | truth-source files agree on `P2R-000`; `merge_state` no longer says `not_started`; next safe patch-step is `P2-006` after readback |
| Open risk | P2-006…P2-010 are not executed yet; final acceptance remains blocked |

## Status

`executing_with_evidence`: P2R-000 records checkpoint merge/readback evidence and removes the P2-003/P2-005 truth-source contradiction. Финальный статус меняется только после P2-010, full D-001…D-063 matrix, PR diff gate and merge verification.
