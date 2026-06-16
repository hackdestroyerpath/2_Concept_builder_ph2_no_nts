# Экспорт

[← Концепция](README.md) | [Output](output.md) | [Протокол экспорта концепции](../../Protocols/concept_export.md)

## Манифест

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

## Результат экспорта

{{export_result}}

## Приёмочные проверки

| Проверка | Доказательство |
|---|---|
| source paths перечислены |  |
| страница output существует | output.md |
| локальный registry существует | page_registry.jsonl |
| целевая аудитория определена |  |
| excluded paths задокументированы |  |
| validation readback записан |  |

## Правило

Export получает статус `export_ready` только после проверки через `Protocols/validation_protocol.md`. Одно слово вроде `ready` не является доказательством.
