# Экспорт

[← Проверочный пример](README.md) | [Результат](output.md) | [Протокол экспорта концепции](../../Protocols/concept_export.md)

## Манифест

```text
export_id: smoke-export-2026-06-16-final
concept_id: smoke
active_issue: CB-009
owner_mode: Execution Mode
export_scope: validation_fixture
source_paths: README.md; purpose.md; requirements.md; operating_model.md; process.md; output.md; concept_state.md; page_registry.jsonl
excluded_paths: черновые файлы output/export; передаточные материалы разработки; аудиторские заметки
format: markdown_bundle
intended_audience: проверка Service Mode и bootstrap-тест Execution Mode
readiness_status: passed_with_evidence
validation_anchor: ../../Validation/final_check.md
```

## Приёмочные проверки

| Проверка | Доказательство | Результат |
|---|---|---|
| область экспорта явно указана | перечислены `export_scope` и `source_paths` | `passed_with_evidence` |
| выходной файл существует | [`output.md`](output.md) | `passed_with_evidence` |
| локальный реестр существует | [`page_registry.jsonl`](page_registry.jsonl) | `passed_with_evidence` |
| исходные страницы связаны ссылками | [`README.md`](README.md) | `passed_with_evidence` |
| осиротевшие файлы отсутствуют | финальная проверка фиксирует ожидаемое отсутствие | `passed_with_evidence` |

## Примечания

Этот экспорт является фикстурой валидации, а не поставляемым пользовательским результатом.