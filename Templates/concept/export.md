# Export

[← Концепция](README.md) | [Output](output.md) | [Concept export protocol](../../Protocols/concept_export.md)

## Manifest

```text
export_id:
concept_id: {{concept_id}}
active_issue: {{issue_id}}
owner_mode: Execution Mode
export_scope:
source_paths:
excluded_paths:
audience:
format:
version:
readiness_status: draft | evidence_pending_final_readback | export_ready | blocked
validation_anchor:
```

## Export result

{{export_result}}

## Acceptance gates

| Gate | Evidence |
|---|---|
| source paths listed |  |
| output page exists | output.md |
| local registry exists | page_registry.jsonl |
| target audience defined |  |
| excluded paths documented |  |
| validation readback recorded |  |

## Правило

Export получает статус `export_ready` только после проверки через `Protocols/validation_protocol.md`. A single word such as `ready` is not evidence.
