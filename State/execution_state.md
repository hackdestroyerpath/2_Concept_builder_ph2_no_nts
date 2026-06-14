# Execution state

[← Точка входа](../README.md) | [Концепции](../Concepts/README.md) | [Smoke fixture](../Concepts/smoke/README.md) | [Export protocol](../Protocols/concept_export.md)

```text
state_id: execution-state-2026-06-14-smoke
owner: Execution Mode
active_mode: Execution Mode
active_object: Concepts/smoke
active_issue: CB-009
status: validation_fixture_retained
mode_owner: Execution Mode
mode_boundary_status: execution_scope_bound_to_selected_concept
dialogue_state: waiting_for_explicit_execution_request
current_focus: smoke validation fixture and export readiness evidence
current_stage: baseline_ready_after_phase2_patch
required_protocols: execution_bootstrap; concept_export; validation_protocol; response_marker
loaded_context_scope: README.md; State/execution_state.md; Concepts/README.md; Concepts/smoke/README.md; Concepts/smoke/page_registry.jsonl; Protocols/concept_export.md
loaded_protocols: execution_bootstrap; concept_export
allowed_read_scope: Concepts/; Templates/concept/; Issues/CB-009/; State/execution_state.md; Registry/
allowed_write_scope: selected concept folder and its linked execution issue only after explicit Execution Mode action
export_readiness_status: ready_with_structural_evidence
persistence_status: written_unverified_until_final_readback
updated_at: 2026-06-14
next_step: for a real user concept, run execution bootstrap and create a new concept folder from Templates/concept/
return_anchor: Concepts/smoke/README.md
```

## Решение по `smoke`

`Concepts/smoke` сохранён как production validation fixture, а не как пользовательская концепция. Его назначение: проверять шаблон концепции, локальный registry, backlinks, output/export model и границы `Execution Mode`. Файл `Concepts/smoke/o2.md` удаляется как orphan/stub; strict pages `output.md` и `export.md` являются единственными output/export страницами fixture.
