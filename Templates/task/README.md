# Task template

[← Templates](../README.md) | [State](item_state.md) | [Registry](page_registry.jsonl) | [Issue execution](../../Protocols/issue_execution.md)

`Templates/task/` хранит артефактную цепочку управляемой задачи. Шаблон не означает, что все шаги обязательны для каждой задачи; он означает, что пропуск шага должен иметь persisted reason.

## Artifact chain

| Order | File | Role | Gate |
|---|---|---|---|
| 1 | [`item_state.md`](item_state.md) | active issue state | issue exists in registry |
| 2 | [`question_answer.md`](question_answer.md) | unresolved questions or skip reason | unknowns classified |
| 3 | [`requirements.md`](requirements.md) | requirement tree and acceptance | requirements approved or scoped |
| 4 | [`solution.md`](solution.md) | proposed approach | risks and changed paths identified |
| 5 | [`contract.md`](contract.md) | execution contract | target paths and validation plan approved |
| 6 | [`linked_files.md`](linked_files.md) | dependencies and attachments | no cycles or unresolved child |
| 7 | [`report.md`](report.md) | result and validation evidence | readback and sync-report present |
| 8 | [`page_registry.jsonl`](page_registry.jsonl) | local navigation contract | all artifacts registered |

## Required route

```text
issue_lifecycle -> question_answer -> requirements_protocol -> issue_execution -> github_write_protocol -> validation_protocol
```

If the task is small enough to skip a separate QA or solution document, the skip reason must be written in the task artifact or issue event. Silence is not a process, despite heroic attempts by committees to prove otherwise.
