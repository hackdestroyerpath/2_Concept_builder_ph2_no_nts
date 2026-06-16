# Проверка языка

[← Финальная проверка](final_check.md) | [Отчёт синхронизации](sync_report.md)

## Правило

Читаемый текст рабочего контура ведётся на русском языке. Допустимы только точные технические идентификаторы: имена файлов и папок, имена машинных полей, статусные литералы, идентификаторы протоколов, ветки, SHA, `Service Mode`, `Execution Mode`, `GitHub`, `JSONL`, `README`, а также точные литералы кода или статуса внутри блоков кода, где перевод сломал бы машинное значение.

## Полный обход P2R5

P2R5 выполняет не выборочную правку примеров, а полный обход зарегистрированных Markdown-файлов из `Registry/page_registry.jsonl`. JSONL-реестры используются как источник путей и машинные метаданные; проверка читаемой прозы относится к Markdown-страницам и человекочитаемым строкам доказательств.

| Зона | Проверенные пути | Результат |
|---|---|---|
| Корень и инструкции | `README.md`, `Instructions/concept_builder_service_instructions.md`, `Instructions/concept_builder_execution_instructions.md` | `passed_after_readback` |
| Протоколы | все зарегистрированные `Protocols/*.md`, включая `github_write_protocol.md`, `github_conflict_recovery.md`, `issue_lifecycle.md`, `question_answer.md`, `requirements_protocol.md`, `issue_execution.md`, `complex_and_linked_issues.md`, `execution_bootstrap.md`, `concept_export.md`, `validation_protocol.md` | `passed_after_readback` |
| Состояние | `State/service_state.md`, `State/execution_state.md` | `passed_after_readback` |
| Задачи | `Issues/README.md`, `Issues/CB-P2/README.md`, `Issues/CB-002/README.md` … `Issues/CB-009/README.md` | `passed_after_readback` |
| Концепции | `Concepts/README.md`, все зарегистрированные `Concepts/smoke/*.md` | `passed_after_readback` |
| Шаблоны | `Templates/README.md`, все зарегистрированные `Templates/concept/*.md`, все зарегистрированные `Templates/task/*.md` | `passed_after_readback` |
| Входящие и реестр | `Inbox/README.md`, `Registry/structure.md`, `Registry/page_registry_schema.md` | `passed_after_readback` |
| Проверка | `Validation/final_check.md`, `Validation/cb008_dry_run.md`, `Validation/cb008_closure_plan.md`, `Validation/navigation_check.md`, `Validation/language_check.md`, `Validation/sync_report.md` | `passed_after_readback` |

## Основные исправленные группы P2R5

| Группа | Исправление |
|---|---|
| `Issues/*/README.md` | английские заголовки происхождения, области, доказательств, очистки и правил закрытия переведены; статусные литералы сохранены. |
| `Protocols/*.md` | заголовки, матрицы, заголовки таблиц и читаемая проза переведены; имена файлов, поля схем и статусные литералы сохранены. |
| `Templates/` | навигационные подписи, роли артефактов, правила шаблонов и проза про безопасность, проверки и шлюзы переведены. |
| `Concepts/smoke/` | страницы требований, операционной модели, процесса, результата, экспорта и состояния получили русские заголовки, таблицы и пояснения; кодовые поля оставлены как шаблонные ключи. |
| `README.md`, `Instructions/`, `Inbox/`, `Registry/structure.md` | остаточные читаемые англоязычные фразы заменены русскими эквивалентами или оставлены только как допустимые технические литералы. |
| `Validation/` | языковая проверка теперь фиксирует полный обход P2R5, а не только примеры P2R4. |

## Допустимые оставшиеся английские литералы

| Категория | Примеры | Причина |
|---|---|---|
| Имена файлов и папок | `README.md`, `Protocols/`, `page_registry.jsonl`, `output.md`, `export.md` | точные пути репозитория |
| Машинные поля | `active_issue`, `source_paths`, `validation_status`, `return_anchor` | ключи схем и шаблонов |
| Статусные литералы | `passed_after_readback`, `fixed_with_evidence`, `blocked`, `ready` | машинные значения состояния |
| Идентификаторы режимов и продуктов | `Service Mode`, `Execution Mode`, `GitHub`, `Concept Builder` | собственные имена и режимы системы |
| Идентификаторы задач и сегментов | `CB-P2`, `CB-009`, `P2R5`, `D-001`…`D-063` | точные идентификаторы учёта и доказательств |

## Остаточная читаемая английская проза

`[]`

## Проваленные проверки

`[]`

## Статус

```text
language_sweep_status: passed_after_readback
failed_checks: []
remaining: []
residual_readable_english_prose: []
```