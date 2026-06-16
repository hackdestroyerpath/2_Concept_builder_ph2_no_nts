# Экспорт

[← Концепция](README.md) | [Результат](output.md) | [Протокол экспорта концепции](../../Protocols/concept_export.md)

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
| исходные пути перечислены |  |
| страница результата `output.md` существует | output.md |
| локальный реестр существует | page_registry.jsonl |
| целевая аудитория определена |  |
| исключённые пути задокументированы |  |
| перечитывание после валидации записано |  |

## Правило

Статус `export_ready` присваивается только после проверки через `Protocols/validation_protocol.md`. Одного слова `ready` недостаточно как доказательства.
