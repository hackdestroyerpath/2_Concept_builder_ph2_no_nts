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
| `P2-005` | Issue registry, events and per-issue artifacts | `D-029`…`D-037` | `Issues/README.md`, `CB-002`…`CB-009`, registry row, event `service-event-000018` | finish readback, then `P2-006` |

## P2-005 report

| Поле | Значение |
|---|---|
| Task | `P2-005 — Rebuild issue registry, event log and per-issue artifact model` |
| Branch | `agent/phase2-patch-20260614T000000Z` |
| Operation scope | update `Issues/README.md`, `Issues/CB-002/README.md`, `Issues/CB-003/README.md`, `Issues/CB-004/README.md`, `Issues/CB-005/README.md`, `Issues/CB-006/README.md`, `Issues/CB-007/README.md`, `Issues/CB-008/README.md`, `Issues/CB-009/README.md`, `Issues/issue_registry.jsonl`, `Issues/issue_events.jsonl`, `State/service_state.md`, `Issues/CB-P2/README.md`, `Validation/final_check.md`, `Validation/sync_report.md` |
| Acceptance evidence | issue index contains required model fields; per-issue artifacts use Russian-readable evidence model; registry current refs match artifacts; event log records P2-005 |
| Open risk | task/requirements/contract depth continues in `P2-006`; final acceptance remains blocked until `P2-010` |
| Next safe step | finish P2-005 readback, then `P2-006` |

## Status

`executing_with_evidence`: P2-005 issue artifact model is recorded with readback requirements. Финальный статус меняется только после GitHub readback, PR diff gate и merge verification. Закрытие не объявляется.