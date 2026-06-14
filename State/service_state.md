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
current_stage: P2-002_registry_navigation_patch
working_branch: agent/phase2-patch-20260614T000000Z
base_branch: main
branch_base_sha: 05607f14d3baa10fdb9427f5810bda4d47e2cb4e
required_protocols: context_loading; mode_routing; github_write_protocol; validation_protocol; rollback_protocol
loaded_context_scope: Registry/page_registry_schema.md; Registry/page_registry.jsonl; Registry/structure.md; Concepts/smoke/page_registry.jsonl; Templates/concept/page_registry.jsonl; Templates/task/page_registry.jsonl; Templates/task/README.md; State/service_state.md; Issues/issue_registry.jsonl; Issues/issue_events.jsonl; Issues/CB-P2/README.md; Validation/final_check.md; Validation/sync_report.md
loaded_protocols: context_loading; mode_routing; github_write_protocol; validation_protocol
allowed_read_scope: README.md; Instructions/; Protocols/; State/; Issues/; Concepts/; Templates/; Inbox/; Registry/; Validation/
allowed_write_scope: Service production files for Phase 2 patch; no development archives, prompts, checkpoint files, Phase 1 audit files or original handoff files
write_package_required: mode; active_object; active_issue; reason; operation; target_paths; pre_sha; post_sha; registry_state_event_coupling; validation_plan
persistence_status: p2_002_written_readback_required
updated_at: 2026-06-14
next_step: P2-003 canonicalize modes, state architecture, context loading and response marker after P2-002 readback evidence
return_anchor: Validation/sync_report.md
```

## Инструкции проекта

| Файл | Назначение | Ограничение | Состояние |
|---|---|---|---|
| `Instructions/concept_builder_service_instructions.md` | bootstrap для `Service Mode` | меньше 8000 символов | проверяется в `Validation/final_check.md` |
| `Instructions/concept_builder_execution_instructions.md` | bootstrap для `Execution Mode` | меньше 8000 символов | проверяется в `Validation/final_check.md` |

## Current write scope — P2-002

| Path | Operation | Classifier |
|---|---|---|
| `Registry/page_registry_schema.md` | update | production navigation schema |
| `Registry/page_registry.jsonl` | update | production global page registry |
| `Registry/structure.md` | update | production registry map |
| `Concepts/smoke/page_registry.jsonl` | update | production local concept registry |
| `Templates/concept/page_registry.jsonl` | update | production local concept template registry |
| `Templates/task/page_registry.jsonl` | update | production local task template registry |
| `Templates/task/README.md` | update | production task template entry |
| `Issues/issue_registry.jsonl` | update | production issue registry |
| `Issues/issue_events.jsonl` | update | production event log |
| `Issues/CB-P2/README.md` | update | production active issue artifact |
| `Validation/final_check.md` | update | production validation gate |
| `Validation/sync_report.md` | update | production sync-report |
| `Issues/cb89.md` | absent/no-write | issue debris not restored |
| `Concepts/smoke/o2.md` | absent/no-write | orphan/stub not restored |

## Правило сохранения

Любой статус завершения считается действительным только вместе с readback evidence, registry entry, state/event update и ссылкой на проверку в `Validation/`. Если хотя бы один элемент отсутствует, используется статус `partial`, `failed`, `conflict` или `blocked`, а не закрывающее утверждение.
