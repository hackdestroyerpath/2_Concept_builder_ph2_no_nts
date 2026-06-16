# CB-P2 — Phase 2 patch

[← Issues](../README.md) | [Registry](../issue_registry.jsonl) | [Events](../issue_events.jsonl) | [Final check](../../Validation/final_check.md) | [Sync report](../../Validation/sync_report.md)

## Назначение

`CB-P2` — service issue для исправления утверждённого реестра `D-001`…`D-063`. Issue хранит production-след patch-работы, route, cleanup decisions, readback evidence и validation anchors.

## Scope

- восстановить root README как service map;
- расширить registry schema и entries;
- канонизировать state/mode/context marker;
- усилить issue lifecycle, QA, requirements, solution, contract, write, conflict, rollback, validation;
- сохранить `Concepts/smoke` как validation fixture и удалить orphan/stub debris;
- заменить assertion-only closure evidence matrix;
- выполнить final control pass и подготовить final acceptance candidate archive вне production repo.

## Cleanup decisions

| Путь | Решение | Evidence |
|---|---|---|
| `Issues/cb89.md` | удалён после переноса сведений в `CB-008`, `CB-009`, registry/events | absent-path check in `Validation/sync_report.md` |
| `Plans/cb008.md` | удалён после переноса в `Validation/cb008_closure_plan.md` | absent-path check in `Validation/sync_report.md` |
| `Closure/status.md` | удалён; финальное состояние живёт в `Validation/final_check.md` | absent-path check in `Validation/sync_report.md` |
| `Concepts/smoke/o2.md` | удалён как orphan/stub | absent-path check in `Validation/sync_report.md` |

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
| `P2R-000` | Post-merge truth-source normalization | truth-source contradiction after rejected checkpoint | README/state/issue/registry/events/final/sync; event `service-event-000019` | `P2R-001` |
| `P2R-001` / `P2-006` | Task workflow gates | `D-038`…`D-045` | QA, requirements, execution, linked issue and task-template gates; changed-path readback complete | `P2R-002` |
| `P2R-002` / `P2-007` | Write/conflict/rollback evidence | `D-046`…`D-052` | write package statuses, conflict recovery, rollback dry-runs and validation coupling | `P2R-003` |
| `P2R-003` / `P2-008` | Validation evidence replacement | `D-053`…`D-058` | final/navigation/language/sync checks name checked paths, failed checks and readback evidence | `P2R-004` |
| `P2R-004` / `P2-009` | Smoke/export final evidence | `D-059`…`D-062` | smoke fixture, export manifest, execution state, local/global registry and debris absence evidence | `P2R-005` |
| `P2R-005` / `P2-010` | Final control pass | `D-001`…`D-063` | closure total 63, fixed_or_resolved 63, blocked 0; final validation passed | `P2R-006` |
| `P2R-006` | Final acceptance archive | archive contract | local archive only, not uploaded to production repo | complete |

## Final control report

| Поле | Значение |
|---|---|
| Final task | `P2R-005 / P2-010 — final control pass` |
| Final archive task | `P2R-006 — final acceptance candidate archive` |
| Base checkpoint | PR `#6`, merge commit `276b893043cd6f21f1ecf0cd18afc9faa6c5d52d` |
| Final production path | direct-to-main evidence writes after PR #6 |
| Defect closure | total `63`, fixed_or_resolved `63`, blocked `0` |
| Validation status | `passed_with_evidence` |
| Open blocking risks | `none` |

## Status

`fixed_with_evidence`: Phase 2 production evidence covers `P2-000`…`P2-010`, `P2R-000`…`P2R-006`, and `D-001`…`D-063`. The final acceptance candidate archive is generated outside the production repository.
