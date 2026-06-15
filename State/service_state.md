# Service state

[← Точка входа](../README.md) | [Реестр протоколов](../Protocols/protocol_index.md) | [Issue registry](../Issues/issue_registry.jsonl) | [Sync report](../Validation/sync_report.md)

```text
state_id: service-state-2026-06-15-p2r000
owner: Service Mode
active_mode: Service Mode
active_object: Concept Builder production repository
active_issue: CB-P2
status: patch_rework_execution
mode_owner: Service Mode
mode_boundary_status: service_scope_only
dialogue_state: executing_phase2_rework
current_focus: approved_defect_register_D-001_D-063
current_stage: P2R-000_post_merge_truth_source_normalization
last_checkpoint_scope: P2-000...P2-005
last_checkpoint_pr: #5
last_checkpoint_merge_sha: 79fabaefb8c03876078606bb02e4dbda6017f5bd
working_branch: agent/phase2-rework-20260614T223441Z
base_branch: main
branch_base_sha: 79fabaefb8c03876078606bb02e4dbda6017f5bd
required_protocols: context_loading; mode_routing; issue_lifecycle; task_flow_hardening; github_write_protocol; validation_protocol
loaded_context_scope: README.md; State/service_state.md; Issues/README.md; Issues/issue_registry.jsonl; Issues/issue_events.jsonl; Issues/CB-P2/README.md; Issues/CB-002/README.md; Issues/CB-003/README.md; Issues/CB-004/README.md; Issues/CB-005/README.md; Issues/CB-006/README.md; Issues/CB-007/README.md; Issues/CB-008/README.md; Issues/CB-009/README.md; Validation/final_check.md; Validation/sync_report.md
loaded_protocols: context_loading; mode_routing; issue_lifecycle; task_flow_hardening; github_write_protocol; validation_protocol
allowed_read_scope: README.md; Instructions/; Protocols/; State/; Issues/; Concepts/; Templates/; Inbox/; Registry/; Validation/
allowed_write_scope: Service production files for Phase 2 rework only
write_package_required: mode; active_object; active_issue; reason; operation; target_paths; pre_sha; post_sha; registry_state_event_coupling; validation_plan
persistence_status: p2r000_truth_source_normalization_written_requires_readback
updated_at: 2026-06-15
next_step: read back P2R-000 changed files, then continue P2-006 task template / requirements / contract hardening
return_anchor: Validation/sync_report.md
```

## Инструкции проекта

| Файл | Назначение | Символов | Ограничение | Evidence state |
|---|---|---:|---:|---|
| `Instructions/concept_builder_service_instructions.md` | bootstrap для `Service Mode` | 2179 | 8000 | checked in checkpoint through P2-003 |
| `Instructions/concept_builder_execution_instructions.md` | bootstrap для `Execution Mode` | 2180 | 8000 | checked in checkpoint through P2-003 |

## P2-005 readback scope recorded before P2R-000

| Path | Operation | Classifier | Evidence state |
|---|---|---|---|
| `Issues/README.md` | update | production issue index | readback observed on rework branch |
| `Issues/CB-002/README.md` | update | production issue artifact | readback observed on rework branch |
| `Issues/CB-003/README.md` | update | production issue artifact | readback observed on rework branch |
| `Issues/CB-004/README.md` | update | production issue artifact | readback observed on rework branch |
| `Issues/CB-005/README.md` | update | production issue artifact | readback observed on rework branch |
| `Issues/CB-006/README.md` | update | production issue artifact | readback observed on rework branch |
| `Issues/CB-007/README.md` | update | production issue artifact | readback observed on rework branch |
| `Issues/CB-008/README.md` | update | production issue artifact | readback observed on rework branch |
| `Issues/CB-009/README.md` | update | production issue artifact | readback observed on rework branch |
| `Issues/issue_registry.jsonl` | update | production issue registry | `CB-P2` moved to P2R-000 normalization in this batch |
| `Issues/issue_events.jsonl` | update | production event log | `service-event-000019` records post-merge normalization |
| `State/service_state.md` | update | production service state | this state records P2R-000 |
| `Issues/CB-P2/README.md` | update | production active issue artifact | P2R-000 report records checkpoint merge evidence |
| `Validation/final_check.md` | update | production validation gate | P2R-000 matrix records merge/readback evidence without final claim |
| `Validation/sync_report.md` | update | production sync-report | merge state no longer `not_started`; P2R-000 readback remains next verification |

## Правило сохранения

Любой статус завершения считается действительным только вместе с readback evidence, registry entry, state/event update и ссылкой на проверку в `Validation/`. Если хотя бы один элемент отсутствует, используется статус `partial`, `failed`, `conflict` или `blocked`, а не закрывающее утверждение.
