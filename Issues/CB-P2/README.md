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
| Operation scope | update `Registry/page_registry_schema.md`, `Registry/structure.md`, `Templates/task/README.md`, `Issues/issue_registry.jsonl`, `Issues/issue_events.jsonl`, `State/service_state.md`, `Issues/CB-P2/README.md`, `Validation/final_check.md`, `Validation/sync_report.md`; read/verify `Registry/page_registry.jsonl`, `Concepts/smoke/page_registry.jsonl`, `Templates/concept/page_registry.jsonl`, `Templates/task/page_registry.jsonl`; absent/no-write `Issues/cb89.md`, `Concepts/smoke/o2.md` |
| Acceptance evidence | schema contains required navigation fields; global registry contains owner/source/backlink metadata; local registries are not path-only; task template has clickable artifact routes; debris paths are not active registry entries |
| Open risk | Full protocol routing/state dry-run continues in `P2-003` and `P2-004`; final acceptance remains blocked until `P2-010`. |
| Next safe step | `P2-003` |

## P2-003 report

| Поле | Значение |
|---|---|
| Task | `P2-003 — Canonicalize modes, state architecture, context loading and response marker` |
| Defects | `D-018`, `D-019`, `D-020`, `D-021`, `D-022`, `D-024`, `D-025`, `D-026`, `D-027`, `D-028` |
| Branch | `agent/phase2-patch-20260614T000000Z` |
| Operation scope | update `README.md`, `Protocols/state_architecture.md`, `Protocols/context_loading.md`, `Protocols/mode_routing.md`, `Protocols/response_marker.md`, `State/service_state.md`, `State/execution_state.md`, `Instructions/concept_builder_service_instructions.md`, `Instructions/concept_builder_execution_instructions.md`, `Issues/issue_registry.jsonl`, `Issues/issue_events.jsonl`, `Issues/CB-P2/README.md`, `Validation/final_check.md`, `Validation/sync_report.md` |
| Acceptance evidence | canonical state schema; lossless state-to-marker mapping; Service/Execution context dry-run; instruction char counts under 8000; mode boundary matrix |
| Open risk | Protocol routing card depth continues in `P2-004`; concept state/output/export final repair continues in `P2-009`; final acceptance remains blocked until `P2-010`. |
| Next safe step | `P2-004` |

## Status

`executing_with_evidence`: P2-003 state/context/marker contract is recorded with readback requirements. Финальный статус меняется только после GitHub readback, PR diff gate и merge verification. Закрытие не объявляется.
