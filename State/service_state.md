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
current_stage: P2-000_to_P2-010_sequential_patch
required_protocols: context_loading; mode_routing; github_write_protocol; validation_protocol; rollback_protocol
loaded_context_scope: README.md; State/service_state.md; Protocols/protocol_index.md; Issues/issue_registry.jsonl; Issues/issue_events.jsonl; Validation/final_check.md; Registry/page_registry.jsonl
loaded_protocols: context_loading; mode_routing; github_write_protocol; validation_protocol
allowed_read_scope: README.md; Instructions/; Protocols/; State/; Issues/; Concepts/; Templates/; Inbox/; Registry/; Validation/
allowed_write_scope: Service production files for Phase 2 patch; no development archives, prompts, checkpoint files, Phase 1 audit files or original handoff files
write_package_required: mode; active_object; active_issue; reason; operation; target_paths; pre_sha; post_sha; registry_state_event_coupling; validation_plan
persistence_status: written_unverified_until_final_readback
updated_at: 2026-06-14
next_step: complete P2-000..P2-010, verify GitHub readback, open PR, merge only after diff/evidence gate
return_anchor: Validation/final_check.md
```

## Инструкции проекта

| Файл | Назначение | Ограничение | Состояние |
|---|---|---|---|
| `Instructions/concept_builder_service_instructions.md` | bootstrap для `Service Mode` | меньше 8000 символов | проверяется в `Validation/final_check.md` |
| `Instructions/concept_builder_execution_instructions.md` | bootstrap для `Execution Mode` | меньше 8000 символов | проверяется в `Validation/final_check.md` |

## Правило сохранения

Любой статус завершения считается действительным только вместе с readback evidence, registry entry, state/event update и ссылкой на проверку в `Validation/`. Если хотя бы один элемент отсутствует, используется статус `partial`, `failed`, `conflict` или `blocked`, а не закрывающее утверждение.
