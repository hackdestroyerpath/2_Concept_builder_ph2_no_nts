# Rollback protocol

[← Реестр протоколов](protocol_index.md) | [GitHub write](github_write_protocol.md) | [Conflict recovery](github_conflict_recovery.md) | [Sync report](../Validation/sync_report.md)

## Назначение

Rollback нужен, когда production write уже выполнен, но последующая проверка показала неверный scope, broken links, language regression, registry/state/event drift, merge conflict или user-decision stop. Rollback не заменяет validation; он сам проходит validation.

## Trigger

Rollback запускается при одном из событий:

1. write затронул path вне `allowed_write_scope`;
2. readback не совпадает с expected content;
3. diff содержит неожиданные deletes/additions;
4. registry/state/events расходятся после записи;
5. PR diff gate нашёл небезопасный scratch-tree или unrelated files;
6. пользователь отклонил patch или потребовал восстановление.

## Scope

| Scope | Действие |
|---|---|
| один файл | восстановить предыдущий blob content или удалить новый файл |
| несколько связанных файлов | создать rollback commit с registry/state/events coupling |
| PR ещё не merged | закрыть PR или обновить branch rollback commit |
| PR merged | создать новый service issue и rollback PR; direct force запрещён без явного user approval |

## Защищённые файлы

`Registry/page_registry.jsonl`, `State/service_state.md`, `Issues/issue_events.jsonl`, `Validation/sync_report.md` обновляются вместе с rollback или получают `blocked` event, если rollback остановлен внешним решением.

## Event schema

```json
{"event_type":"rollback","active_issue":"CB-P2","trigger":"scope_mismatch","affected_paths":[],"pre_sha":"","rollback_sha":"","validation_ref":"Validation/sync_report.md","status":"validated|blocked"}
```

## Stop conditions

Rollback останавливается и создаёт `blocked` event, если восстановление удалит validated user output, затронет чужой режим, потребует force update default branch, либо конфликт требует человеческого выбора.

## Validation

После rollback агент проверяет:

- changed paths ровно соответствуют rollback scope;
- registry/state/events снова согласованы;
- readback проходит для затронутых файлов;
- `Validation/sync_report.md` содержит branch, commit, rollback reason, remaining risk.
