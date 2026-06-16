# Execution state

[← Точка входа](../README.md) | [Концепции](../Concepts/README.md) | [Smoke fixture](../Concepts/smoke/README.md) | [Export protocol](../Protocols/concept_export.md)

```text
state_id: execution-state-2026-06-16-smoke-final
owner: Execution Mode
active_mode: Execution Mode
active_object: Concepts/smoke
active_issue: CB-009
status: validation_fixture_export_readback_verified
mode_owner: Execution Mode
mode_boundary_status: execution_scope_bound_to_selected_concept
dialogue_state: waiting_for_explicit_execution_request
current_focus: smoke validation fixture and export readiness evidence
current_stage: p2_009_smoke_export_evidence_complete
required_protocols: execution_bootstrap; context_loading; mode_routing; concept_export; validation_protocol; response_marker
loaded_context_scope: README.md; State/execution_state.md; Concepts/README.md; Concepts/smoke/README.md; Concepts/smoke/page_registry.jsonl; Concepts/smoke/output.md; Concepts/smoke/export.md; Protocols/protocol_index.md; Protocols/execution_bootstrap.md; Protocols/concept_export.md
loaded_protocols: execution_bootstrap; context_loading; mode_routing; concept_export; validation_protocol
allowed_read_scope: Concepts/; Templates/concept/; Issues/CB-009/; State/execution_state.md; Registry/; Validation/
allowed_write_scope: selected concept folder and its linked execution issue only after explicit Execution Mode action
export_readiness_status: ready_with_readback_evidence
persistence_status: synced_with_final_readback_evidence
updated_at: 2026-06-16
next_step: for a real user concept, run execution bootstrap and create a new concept folder from Templates/concept/
return_anchor: Concepts/smoke/README.md
```

## Решение по `smoke`

`Concepts/smoke` сохранён как production validation fixture, а не как пользовательская концепция. Его назначение: проверять шаблон концепции, local registry, backlinks, output/export model и границы `Execution Mode`. Strict pages `output.md` и `export.md` остаются единственными output/export страницами.

## P2-009 execution/export dry-run

| Проверка | Evidence | Состояние |
|---|---|---|
| Execution entrypoint найден | `README.md` → `Concepts/README.md` → `Concepts/smoke/README.md` | passed_with_evidence |
| State uses canonical fields | этот файл содержит `state_id`, `owner`, `active_mode`, `active_object`, `active_issue`, `status`, `dialogue_state`, `current_stage`, scopes и marker fields | passed_with_evidence |
| Scope does not mix service/protocol writes | `allowed_write_scope` ограничен выбранной концепцией и linked execution issue | passed_with_evidence |
| Export readiness has manifest | `Concepts/smoke/export.md` | passed_with_evidence |
| Orphan debris absent | expected 404 in sync report | passed_with_evidence |
