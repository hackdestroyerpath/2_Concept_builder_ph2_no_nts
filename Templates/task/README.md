# Шаблон задачи

[← Templates](../README.md) | [State](item_state.md) | [Registry](page_registry.jsonl) | [Issue execution](../../Protocols/issue_execution.md)

`Templates/task/` хранит артефактную цепочку управляемой задачи. Шаблон не означает, что все шаги обязательны для каждой задачи; он означает, что пропуск шага должен иметь persisted reason в issue artifact, event log или report.

## Цепочка артефактов

| Порядок | Файл | Роль | Gate |
|---|---|---|---|
| 1 | [`item_state.md`](item_state.md) | state активной задачи | issue существует в registry |
| 2 | [`question_answer.md`](question_answer.md) | вопросы, ответы или skip reason | неизвестности классифицированы |
| 3 | [`requirements.md`](requirements.md) | дерево требований и acceptance | требования утверждены или scoped |
| 4 | [`solution.md`](solution.md) | proposed approach | риски и changed paths определены |
| 5 | [`contract.md`](contract.md) | execution contract | target paths и validation plan утверждены |
| 6 | [`linked_files.md`](linked_files.md) | зависимости и attachments | нет циклов или unresolved child issues |
| 7 | [`report.md`](report.md) | результат и validation evidence | readback и sync-report присутствуют |
| 8 | [`page_registry.jsonl`](page_registry.jsonl) | local navigation contract | все task artifacts зарегистрированы |

## Обязательный маршрут

```text
issue_lifecycle -> question_answer -> requirements_protocol -> issue_execution -> github_write_protocol -> validation_protocol
```

## Navigation contract

| Объект | Проверка |
|---|---|
| README template | имеет clickable routes ко всем child artifacts |
| `page_registry.jsonl` | содержит owner/source/backlinks для всей artifact chain |
| child artifact | имеет backlink через parent `README.md` и protocol cross-link, если применимо |
| skipped artifact | требует persisted reason, иначе статус задачи остаётся `partial` или `blocked` |

Если задача достаточно мала и отдельный QA, solution или contract документ не нужен, причина пропуска записывается в task artifact или issue event. Молчание не является процессом, даже если комитеты старались доказать обратное.
