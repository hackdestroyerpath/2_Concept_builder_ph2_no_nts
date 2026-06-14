# GitHub conflict recovery

[← Реестр протоколов](protocol_index.md) | [Write protocol](github_write_protocol.md) | [Rollback](rollback_protocol.md)

## Назначение

Протокол задаёт state machine для conflict/recovery. Recovery не равен бесконечному retry: каждое действие должно иметь фактическую проверку branch/ref, diff, registry/state/events и next decision.

## Conflict statuses

| Status | Meaning | Next action |
|---|---|---|
| `sha_conflict` | update/delete использовал устаревший blob sha | fresh fetch + one bounded retry |
| `target_confusion` | запись была в branch, проверка шла по другому ref | restore ledger + verify correct ref |
| `scope_conflict` | diff затрагивает неожиданные paths | stop + user decision or rollback |
| `merge_conflict` | PR не может быть merged safely | rebuild branch from base or split patch |
| `validation_conflict` | readback есть, но links/state/events failed | patch coupled files or rollback |
| `external_blocked` | нужен внешний доступ или user decision | record blocked event |

## Decision flow

1. Зафиксировать active branch, base branch, active issue, target paths.
2. Перечитать фактические файлы на active branch.
3. Сравнить expected vs actual.
4. Если ошибка только в fresh sha, повторить один write со свежим sha.
5. Если diff затрагивает чужой scope, остановиться и записать event.
6. Если запись уже persisted, выбрать: patch-forward, rollback, split into new issue, user decision.
7. После решения обновить `Validation/sync_report.md`.

## Stop rules

- Нельзя создавать вторую ветку, пока не восстановлена первая.
- Нельзя объявлять read-only, если уже есть branch, commit, PR или readback evidence.
- Нельзя merge-ить PR без changed files/patch gate.
- Нельзя использовать `closed`, `passed`, `synced`, `Ready`, `OK` как замену evidence.

## Recovery event

```json
{"event_type":"conflict_recovery","active_issue":"CB-P2","status":"validation_conflict","target_paths":[],"decision":"patch_forward|rollback|blocked|user_decision","evidence":[]}
```
