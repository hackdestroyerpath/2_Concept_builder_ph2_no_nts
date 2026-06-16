# Проверка языка

[← Финальная проверка](final_check.md) | [Отчёт синхронизации](sync_report.md)

## Правило

Читаемый production-текст ведётся на русском языке. Разрешены только технические идентификаторы: имена файлов и папок, имена machine fields, status literals, protocol IDs, `Service Mode`, `Execution Mode`, `GitHub`, `JSONL`, `README`, `export`, `registry`, `state`, `issue`, а также точные code/status literals внутри code blocks, где перевод сломал бы machine meaning.

## Обход и readback

| Зона | Проверенные paths | Результат |
|---|---|---|
| `Concepts/smoke/` | `README.md`, `output.md`, `export.md`, связанные fixture pages | passed_after_readback |
| `Templates/task/` | `README.md`, `item_state.md`, `question_answer.md`, `requirements.md`, `solution.md`, `contract.md`, `linked_files.md`, `report.md` | passed_after_readback |
| `Templates/concept/` | `README.md`, `export.md`, route/table prose | passed_after_readback |
| `Validation/` | `cb008_closure_plan.md`, `cb008_dry_run.md`, `language_check.md`, `final_check.md`, `sync_report.md`, `navigation_check.md` | passed_after_readback |
| `Issues/` и `State/` | `Issues/CB-P2/README.md`, `Issues/issue_events.jsonl`, `Issues/issue_registry.jsonl`, `State/service_state.md` | passed_after_readback |

## Исправленные фрагменты

| Path | Исправление |
|---|---|
| `Concepts/smoke/export.md` | примечание переведено на русский. |
| `Templates/task/contract.md` | текст gate/breach переведён на русский. |
| `Templates/concept/export.md` | правило готовности export переведено на русский. |
| `Validation/cb008_closure_plan.md` | заголовки, table labels и closure steps переведены на русский. |
| `Validation/cb008_dry_run.md` | заголовки, scenario labels и notes переведены на русский. |
| `Concepts/smoke/README.md` | mixed prose в status/notes/navigation переведён или оставлен только как technical identifier. |
| `Concepts/smoke/output.md` | headings/prose переведены; status literals сохранены. |
| `Templates/task/` и `Templates/concept/` | найденные template fragments переведены; schema literals сохранены. |

## Проваленные проверки

`[]`

## Примечание

Предыдущая проверка языка была неполной: она заявляла `failed_checks: []`, хотя production Markdown ещё содержал readable prose не на русском. В этом pass такие fragments переведены, а оставшийся English классифицирован только как technical identifier или machine literal.