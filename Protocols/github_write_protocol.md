# Протокол записи в GitHub

[← Реестр протоколов](protocol_index.md) | [Загрузка контекста](context_loading.md) | [Conflict recovery](github_conflict_recovery.md) | [Rollback](rollback_protocol.md)

## Назначение

Протокол описывает безопасную запись production-файлов в `GitHub`. Любая запись должна иметь classifier, preflight, fresh read, write package, readback, registry/state/events coupling и sync-report. Запись без readback — это не подвиг, а просто способ оставить следующему человеку мину в Markdown.

## Production/development classifier

| Класс | Примеры | Решение |
|---|---|---|
| production | `README.md`, `Protocols/`, `State/`, `Issues/`, `Concepts/`, `Templates/`, `Registry/`, `Validation/`, `Inbox/` | можно писать в пределах active mode scope |
| development | patch-handoff, Phase 1 audit, prompt, original handoff, checkpoint, временный отчёт | не загружать в production repo |
| conditional | scripts, generated archive, attachment | нужен отдельный issue/contract |
| debris | legacy scratch/debris paths and assertion-only closure files | удалить или мигрировать с evidence |

## Write package

Перед записью агент фиксирует:

```text
mode:
active_object:
active_issue:
reason:
operation: create | update | delete | move
classification:
target_paths:
pre_sha:
expected_post_state:
related_registry_paths:
related_state_paths:
related_event_paths:
validation_plan:
rollback_plan:
```

## Preflight

1. Проверить, что `target_paths` входят в `allowed_write_scope` active mode.
2. Для update/delete перечитать файл и взять свежий `sha`.
3. Для create проверить отсутствие production-дубликата.
4. Для delete убедиться, что причина зафиксирована в registry/events/validation.
5. Подготовить связанное обновление registry, state, events и validation.

## Persistence statuses

| Статус | Значение |
|---|---|
| `not_written` | запись не выполнялась |
| `written_unverified` | запись выполнена, readback ещё не пройден |
| `synced` | запись выполнена и перечитана из `GitHub` |
| `partial` | часть write package записана, часть требует продолжения |
| `failed` | запись не выполнена или readback не совпал |
| `conflict` | GitHub/version/diff conflict требует recovery |
| `blocked` | остановлено внешним решением или scope-ограничением |

## После записи

1. Перечитать каждый changed path из `GitHub` на active branch.
2. Проверить ключевые строки, links, registry entries, state fields, issue events.
3. Обновить `Validation/sync_report.md`.
4. Перед merge создать PR, проверить changed files и representative patch. Если работа идёт direct-to-main по явному rework-контракту, sync-report должен назвать это вместо PR.
5. После merge или direct write проверить changed paths на base branch.

## P2-007 protocol-level dry-run scenarios

| Scenario | Trigger | Required evidence | Expected status |
|---|---|---|---|
| success write/readback | fresh SHA, bounded production path, target content matches after fetch | pre-sha, response commit/ref, readback sha, sync-report row | `synced` |
| partial write / coupling missing | file write succeeds but registry/state/event/final/sync coupling is incomplete | changed path list plus failed coupling field | `partial` until coupling patch or rollback decision |
| SHA conflict | update/delete uses stale blob SHA | stale sha, current readback sha, conflict event, no same-request blind retry | `conflict` then recovery re-plan |
| blocked rollback | rollback would require force update or remove validated user output | rollback trigger, protected path, blocked reason, event row | `blocked` with user decision required |

## P2-007 acceptance gate

`P2-007` считается выполненным только если `github_write_protocol.md`, `github_conflict_recovery.md`, `rollback_protocol.md`, `validation_protocol.md`, `Issues/issue_events.jsonl`, `State/service_state.md`, `Validation/final_check.md` и `Validation/sync_report.md` согласованы. Dry-run scenarios являются protocol-level evidence; они не симулируют запись в чужой production path.

## Ошибки

| Ситуация | Действие |
|---|---|
| duplicate create | перейти на update flow со свежим `sha` |
| stale sha | перечитать файл и повторить только новый bounded request с новым request id/ledger entry |
| safety/payload block | убрать optional fields, сократить message/content или разбить patch |
| unexpected diff | остановиться, записать event, вызвать `github_conflict_recovery` |
| wrong target branch | восстановить ledger, проверить branch и diff |

## Запреты

- Не объявлять write unavailable при наличии branch/commit/readback фактов.
- Не проверять branch write по `main` до merge.
- Не загружать development материалы.
- Не использовать closure labels как evidence.
- Не считать `synced` без `fetch_file` readback и sync-report row.
