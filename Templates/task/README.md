# Шаблон задачи

[← Templates](../README.md) | [State](item_state.md) | [Registry](page_registry.jsonl) | [Исполнение issue](../../Protocols/issue_execution.md)

`Templates/task/` хранит артефактную цепочку управляемой задачи. Шаблон не означает, что все шаги обязательны для каждой задачи; он означает, что пропуск шага должен иметь persisted reason в issue artifact, event log или report.

## Цепочка артефактов

| Порядок | Файл | Роль | Gate |
|---|---|---|---|
| 1 | [`item_state.md`](item_state.md) | state активной задачи | issue exists in registry |
| 2 | [`question_answer.md`](question_answer.md) | вопросы, ответы или skip reason | неизвестности классифицированы |
| 3 | [`requirements.md`](requirements.md) | дерево требований, источники и acceptance | requirements scoped or skip reason recorded |
| 4 | [`solution.md`](solution.md) | предложенный подход, риски и changed paths | risks and target paths defined |
| 5 | [`contract.md`](contract.md) | execution contract | target paths, operation, validation plan and rollback plan recorded |
| 6 | [`linked_files.md`](linked_files.md) | dependencies, attachments and child issues | no unresolved cycle or blocking child issue |
| 7 | [`report.md`](report.md) | result and validation evidence | readback and sync-report evidence present |
| 8 | [`page_registry.jsonl`](page_registry.jsonl) | local navigation contract | all task artifacts registered |

## Обязательный маршрут

```text
issue_lifecycle -> question_answer -> requirements_protocol -> issue_execution -> github_write_protocol -> validation_protocol
```

## Контракт навигации

| Объект | Проверка |
|---|---|
| README template | содержит clickable routes ко всем child artifacts |
| `page_registry.jsonl` | содержит owner/source/backlinks для всей artifact chain |
| child artifact | имеет backlink через parent `README.md` и protocol cross-link, если применимо |
| skipped artifact | требует persisted reason, иначе статус задачи остаётся `partial` или `blocked` |
| report | указывает readback ref, registry/state/event result и next step |

## Правило scoped skip

Если задача достаточно мала и отдельный QA, solution или contract документ не нужен, причина пропуска записывается в task artifact или issue event. Молчание не является процессом, хотя комитеты старались доказать обратное.
