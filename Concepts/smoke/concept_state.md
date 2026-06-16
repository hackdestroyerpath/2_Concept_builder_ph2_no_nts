# Smoke concept state

[← Smoke](README.md) | [Structure](structure.md) | [Export](export.md)

```text
concept_id: smoke
concept_title: Smoke validation fixture
owner_mode: Execution Mode
active_issue: CB-009
current_stage: validation_fixture_export_check_complete
loaded_context: README.md; concept_state.md; structure.md; page_registry.jsonl; purpose.md; requirements.md; operating_model.md; process.md; output.md; export.md
allowed_read_scope: Concepts/smoke/; Templates/concept/; Protocols/concept_export.md
allowed_write_scope: Concepts/smoke/ only when active_object is Concepts/smoke
validation_status: passed_with_evidence
export_status: manifest_present_and_readback_verified
orphan_cleanup_status: absent_with_evidence
persistence_status: synced_with_final_readback_evidence
return_anchor: Concepts/smoke/README.md
```

## Правило

Файл обновляется только в `Execution Mode` после явного выбора `Concepts/smoke` как validation fixture или в `Service Mode` при validation patch с issue `CB-009`/`CB-P2`.
