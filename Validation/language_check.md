# Language check

[← Final check](final_check.md) | [Sync report](sync_report.md)

## Rule

Читаемый production-текст ведётся на русском языке. Разрешены технические идентификаторы: имена файлов, папок, статусы машинных полей, `Service Mode`, `Execution Mode`, `GitHub`, `JSONL`, `README`, `export`, `registry`, `state`, `issue`.

## Evidence

| Area | Checked paths | Result |
|---|---|---|
| `README.md` | root entry and route tables | passed_with_evidence |
| `State/` | `State/service_state.md`, `State/execution_state.md` | passed_with_evidence |
| `Protocols/` | write/conflict/rollback/validation plus task workflow protocols | passed_with_evidence |
| `Issues/` | `Issues/CB-P2/README.md`, registry, events, `CB-009` | passed_with_evidence |
| `Concepts/smoke/` | README, state, output, export, local registry | passed_with_evidence |
| `Templates/` | task/concept routes and local registries | passed_with_evidence |
| `Registry/` | structure, schema, page registry | passed_with_evidence |
| `Validation/` | final, sync, navigation, language checks | passed_with_evidence |

## Failed checks

`[]`

## Note

Английские technical identifiers сохранены намеренно и не считаются language drift.
