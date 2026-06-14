# Service state

[← Точка входа](../README.md) | [Реестр протоколов](../Protocols/protocol_index.md) | [Issue registry](../Issues/issue_registry.jsonl) | [Sync report](../Validation/sync_report.md)

```text
state_id: service-state-2026-06-14-p2
owner: Service Mode
active_mode: Service Mode
active_object: Concept Builder production repository
active_issue: CB-P2
status: patch_execution
mode_owner: Service Mode
mode_boundary_status: service_scope_only
dialogue_state: executing_phase2_patch
current_focus: approved_defect_register_D-001_D-063
current_stage: P2-004_protocol_routing_patch
working_branch: agent/phase2-patch-20260614T000000Z
base_branch: main
branch_base_sha: 05607f14d3baa10fdb9427f5810bda4d47e2cb4e
required_protocols: context_loading; mode_routing; protocol_index; execution_bootstrap; github_write_protocol; validation_protocol
loaded_context_scope: README.md; State/service_state.md; Protocols/protocol_index.md; Protocols/context_loading.md; Protocols/mode_routing.md; Protocols/execution_bootstrap.md; Issues/issue_registry.jsonl; Issues/issue_events.jsonl; Issues/CB-P2/README.md; Validation/final_check.md; Validation/sync_report.md
loaded_protocols: context_loading; mode_routing; protocol_index; execution_bootstrap; github_write_protocol; validation_protocol
allowed_read_scope: README.md; Instructions/; Protocols/; State/; Issues/; Concepts/; Templates/; Inbox/; Registry/; Validation/
allowed_write_scope: Service production files for Phase 2 patch only
write_package_required: mode; active_object; active_issue; reason; operation; target_paths; pre_sha; post_sha; registry_state_event_coupling; validation_plan
persistence_status: p2_004_written_readback_required
updated_at: 2026-06-14
next_step: P2-005 rebuild issue registry, event log and per-issue artifact model after P2-004 readback evidence
return_anchor: Validation/sync_report.md
```

## Инструкции проекта

| Файл | Назначение | Символов | Ограничение | Состояние |
|---|---|---:|---:|---|
| `Instructions/concept_builder_service_instructions.md` | bootstrap для `Service Mode` | 2179 | 8000 | проверено P2-003 |
| `Instructions/concept_builder_execution_instructions.md` | bootstrap для `Execution Mode` | 2180 | 8000 | проверено P2-003 |

## P2-004 write/readback scope

| Path | Operation | Classifier | Evidence state |
|---|---|---|---|
| `Protocols/protocol_index.md` | update | production protocol index | route matrix and protocol cards written |
| `Protocols/mode_routing.md` | update | production mode routing protocol | decision matrix and existing issue resume flow written |
| `Protocols/context_loading.md` | update | production context protocol | context route matrix and resume context written |
| `Protocols/execution_bootstrap.md` | update | production execution bootstrap protocol | execution route card and blocking conditions written |
| `Issues/issue_registry.jsonl` | update | production issue registry | current_task advanced to `P2-004` |
| `Issues/issue_events.jsonl` | update | production event log | `service-event-000017` appended |
| `State/service_state.md` | update | production service state | this state records P2-004 scope |
| `Issues/CB-P2/README.md` | update | production active issue artifact | P2-004 report records scope |
| `Validation/final_check.md` | update | production validation gate | P2-004 matrix and acceptance criteria recorded |
| `Validation/sync_report.md` | update | production sync-report | final P2-004 readback anchor |

## Правило сохранения

Любой статус завершения считается действительным только вместе с readback evidence, registry entry, state/event update и ссылкой на проверку в `Validation/`. Если хотя бы один элемент отсутствует, используется статус `partial`, `failed`, `conflict` или `blocked`, а не закрывающее утверждение.