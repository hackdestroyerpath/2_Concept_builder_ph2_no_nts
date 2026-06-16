# Проверка языка

[← Финальная проверка](final_check.md) | [Sync report](sync_report.md)

## Правило

Читаемый production-текст ведётся на русском языке. Разрешены только технические идентификаторы: имена файлов и папок, имена machine fields, status literals, protocol IDs, `Service Mode`, `Execution Mode`, `GitHub`, `JSONL`, `README`, `export`, `registry`, `state`, `issue`, а также точные code/status literals внутри code blocks, где перевод сломал бы machine meaning.

## Sweep и readback

| Зона | Проверенные paths | Результат |
|---|---|---|
| `Concepts/smoke/` | `README.md`, `output.md`, `export.md`, связанные fixture pages | passed_after_readback |
| `Templates/task/` | `README.md`, `item_state.md`, `question_answer.md`, `requirements.md`, `solution.md`, `contract.md`, `linked_files.md`, `report.md` | passed_after_readback |
| `Templates/concept/` | `README.md`, `export.md`, route/table prose | passed_after_readback |
| `Validation/` | `cb008_closure_plan.md`, `language_check.md`, `final_check.md`, `sync_report.md`, `navigation_check.md` | passed_after_readback |
| `Issues/` и `State/` | `Issues/CB-P2/README.md`, `Issues/issue_events.jsonl`, `Issues/issue_registry.jsonl`, `State/service_state.md` | passed_after_readback |

## Переведённые readable fragments

| Path | Исправление |
|---|---|
| `Concepts/smoke/export.md` | English note sentence переведена на русский. |
| `Templates/task/contract.md` | English gate/breach prose переведена на русский. |
| `Templates/concept/export.md` | English rule sentence переведена на русский. |
| `Validation/cb008_closure_plan.md` | English headings, table labels и closure steps переведены на русский. |
| `Concepts/smoke/README.md` | mixed readable English в status/notes/navigation переведён или оставлен только как technical identifier. |
| `Concepts/smoke/output.md` | English headings/prose переведены; status literals сохранены. |
| `Templates/task/` и `Templates/concept/` | найденные readable English template fragments переведены; schema literals сохранены. |

## Failed checks

`[]`

## Примечание

Предыдущая проверка языка была неполной: она заявляла `failed_checks: []`, хотя production Markdown ещё содержал readable English prose. В этом pass такие fragments переведены, а оставшийся English классифицирован только как technical identifier или machine literal.
