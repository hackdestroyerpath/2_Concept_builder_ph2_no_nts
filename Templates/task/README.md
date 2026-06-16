# Шаблон задачи

[← Templates](../README.md) | [State](item_state.md) | [Registry](page_registry.jsonl) | [Исполнение issue](../../Protocols/issue_execution.md)

`Templates/task/` хранит артефактную цепочку управляемой задачи. Шаблон не означает, что все шаги обязательны для каждой задачи; он означает, что пропуск шага должен иметь persisted reason в issue artifact, event log или report.

## Цепочка артефактов

| Порядок | Файл | Роль | Контроль |
|---|---|---|---|
| 1 | [`item_state.md`](item_state.md) | state активной задачи | issue существует в registry |
| 2 | [`question_answer.md`](question_answer.md) | вопросы, ответы или skip reason | неизвестности классифицированы |
| 3 | [`requirements.md`](requirements.md) | дерево требований, источники и критерии приёмки | область requirements определена или причина пропуска записана |
| 4 | [`solution.md`](solution.md) | предложенный подход, риски и changed paths | risks и target paths определены |
| 5 | [`contract.md`](contract.md) | contract исполнения | target paths, validation plan и rollback plan записаны |
| 6 | [`linked_files.md`](linked_files.md) | dependencies, attachments и дочерние issue | нет нерешённого цикла или блокирующего дочернего issue |
| 7 | [`report.md`](report.md) | результат и validation evidence | readback и sync-report evidence присутствуют |
| 8 | [`page_registry.jsonl`](page_registry.jsonl) | local navigation contract | все task artifacts зарегистрированы |

## Обязательный маршрут

```text
issue_lifecycle -> question_answer -> requirements_protocol -> issue_execution -> validation_protocol
```

## Контракт навигации

| Объект | Проверка |
|---|---|
| README template | содержит маршруты ко всем дочерним artifacts |
| `page_registry.jsonl` | содержит owner/source/backlinks для всей artifact chain |
| child artifact | имеет backlink через parent `README.md` и protocol cross-link, если применимо |
| skipped artifact | требует persisted reason, иначе статус задачи остаётся `partial` или `blocked` |
| report | указывает readback ref, registry/state/event result и next step |

## Правило ограниченного пропуска

Если задача достаточно мала и отдельный QA, solution или contract документ не нужен, причина пропуска записывается в task artifact или issue event. Молчание не является процессом.