# Проверка языка

[← Финальная проверка](final_check.md) | [Отчёт синхронизации](sync_report.md)

## Правило

Читаемый текст рабочего контура ведётся на русском языке. Разрешены только технические идентификаторы: имена файлов и папок, имена машинных полей, статусные литералы, идентификаторы протоколов, `Service Mode`, `Execution Mode`, `GitHub`, `JSONL`, `README`, `export`, `registry`, `state`, `issue`, а также точные литералы кода или статуса внутри блоков кода, где перевод сломал бы машинное значение.

## Обход и перечитывание

| Зона | Проверенные пути | Результат |
|---|---|---|
| `Concepts/smoke/` | `README.md`, `output.md`, `export.md`, связанные страницы фикстуры | passed_after_readback |
| `Templates/task/` | `contract.md` и ранее проверенные страницы шаблона | passed_after_readback |
| `Templates/concept/` | `export.md` и ранее проверенные страницы шаблона | passed_after_readback |
| `Validation/` | `cb008_closure_plan.md`, `cb008_dry_run.md`, `navigation_check.md`, `language_check.md`, `final_check.md`, `sync_report.md` | passed_after_readback |
| `Issues/` и `State/` | `Issues/CB-P2/README.md`, `Issues/issue_events.jsonl`, `Issues/issue_registry.jsonl`, `State/service_state.md` | passed_after_readback |

## Исправленные фрагменты P2R4

| Путь | Исправление |
|---|---|
| `Concepts/smoke/README.md` | заголовок `Cleanup`, читаемые `readback`, `failure modes`, `mapping`, `production pages`, `fixture`, `orphan/stub debris` переведены или оставлены только как точные литералы. |
| `Concepts/smoke/output.md` | заголовок `Output`, подписи результата, карта связей, поля манифеста, отсутствующие цели и валидационная фраза переведены. |
| `Concepts/smoke/export.md` | читаемые значения манифеста, строки приёмочных проверок и примечание переведены; машинные поля сохранены. |
| `Templates/concept/export.md` | строки `source paths`, `excluded paths`, `validation readback` переведены как читаемые подписи; поля схемы сохранены. |
| `Templates/task/contract.md` | фразы про запись в рабочий контур, контракт, событие задачи, целевые пути и статус конфликта получили русские эквиваленты. |
| `Validation/navigation_check.md` | читаемые строки навигационной проверки и причины отсутствующих путей переведены. |
| `Validation/cb008_closure_plan.md` | остаточные читаемые фразы про пробный прогон, реестр, доказательства и блокеры переведены. |
| `Validation/cb008_dry_run.md` | сценарии пробного прогона, доказательства и примечание переведены. |

## Проваленные проверки

`[]`

## Статус

```text
language_sweep_status: passed_after_readback
failed_checks: []
remaining: []
```
