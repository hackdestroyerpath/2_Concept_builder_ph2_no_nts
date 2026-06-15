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
| `P2R-000` | Post-merge truth-source normalization | truth-source contradiction after rejected checkpoint | `README.md`, `State/service_state.md`, this issue, registry, events, `Validation/final_check.md`, `Validation/sync_report.md`; event `service-event-000019` | `P2R-001` |
| `P2R-001` / `P2-006` | Task workflow gates | `D-038`…`D-045` | QA, requirements, execution, linked issue and task-template gates; event `service-event-000020` | readback this batch, then `P2-007` |

## P2R-001 / P2-006 report

| Поле | Значение |
|---|---|
| Task | `P2R-001 — Complete P2-006 task workflow gates` |
| Branch | `agent/phase2-rework-20260614T223441Z` |
| Base | `main` at merge commit `79fabaefb8c03876078606bb02e4dbda6017f5bd` |
| Operation scope | update QA, requirements, issue execution, complex/linked issues, task flow hardening, `Templates/task/`, registry, event log, state, validation and sync report |
| Acceptance evidence | protocols define blocking decisions, persisted skip reasons, requirement IDs, approved contract gates, dependency state machine, task artifacts and local registry metadata |
| Open risk | P2R-001 changed-path readback is required before `P2-007`; P2-007…P2-010 are not executed yet |

## Status

`executing_with_evidence`: P2R-001 records P2-006 task workflow gates and keeps final acceptance blocked until P2-010, full D-001…D-063 matrix, PR diff gate and merge verification.
