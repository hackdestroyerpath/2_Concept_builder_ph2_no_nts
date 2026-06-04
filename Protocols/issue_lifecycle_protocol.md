# Протокол жизненного цикла `issue`

[← К реестру протоколов](protocol_index.md) | [Описание `Issues`](../Issues/README.md)

## Статусы

Основной путь:

```text
creating → proposed → approved → questioning → requirements_review → solution_review → ready_for_execution → executing → completed → closed
```

Дополнительные статусы:

```text
rejected
blocked
waiting_dependency
needs_discussion
cleanup_pending
```

## Создание нового `issue`

1. Принять input: текст, файлы, точку входа и attachments.
2. Сохранить точку входа и attachments в [`../Inbox/`](../Inbox/README.md).
3. Проанализировать input и предложить registry кандидатов.
4. До ответа сохранить `Issues/issue_registry.jsonl`, `Issues/issue_events.jsonl`, state и reason каждого `issue`.
5. В чат вывести таблицу `issue` и reason-блоки, совпадающие с сохранёнными файлами.

## Решения по registry

Допустимые команды: утвердить всё, утвердить ID, отклонить ID, обсудить ID, добавить `issue` с обязательным reason. `Issue` без reason не создаётся.

## QA и requirements

`Question Answer` используется только если уточнения реально повышают качество. Даже если вопросы пропущены, requirements всегда создаются и утверждаются перед выполнением.

## Выполнение

`simple issue` проходит через `solution`, `contract`, утверждение, выполнение, `output`, `report` и проверку закрытия.

`complex issue` создаёт дочерние `issue`; родитель закрывается только после их закрытия и roll-up.

Linked issues фиксируют зависимости и блокировки.

## Cleanup

Отклонённые и закрытые `issue` обрабатываются по cleanup-политике после проверки зависимостей и сохранения provenance.
