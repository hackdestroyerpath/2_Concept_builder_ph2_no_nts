# Issues

[← Точка входа](../README.md) | [Issue registry](issue_registry.jsonl) | [Issue events](issue_events.jsonl) | [Lifecycle protocol](../Protocols/issue_lifecycle.md)

`Issues/` хранит production-артефакты жизненного цикла задач: reason, provenance, approval, dependencies, cleanup, validation и return-anchor. История восстанавливается только из имеющихся repo-фактов; недостающие детали помечаются как `reconstructed`, а не придумываются задним числом.

## Обязательная модель issue

| Поле | Назначение | Где проверяется |
|---|---|---|
| `issue_id` | стабильный идентификатор | `Issues/issue_registry.jsonl` |
| `type` | service, execution, patch, validation | registry и artifact heading |
| `status` | рабочий статус без финального ярлыка | registry, event log, validation |
| `priority` | blocker, major, normal | registry |
| `reason` | почему issue существует | registry и artifact |
| `provenance` | источник: user, repo state, reconstructed baseline, audit-approved patch | registry и artifact |
| `approval` | approved, reconstructed, not_required, blocked | registry |
| `dependencies` | parent/child/linked issues и waiting states | registry, linked files |
| `cleanup` | retained, migrated, removed_with_reason, pending | registry, events, validation |
| `current_refs` | production-файлы, где лежит актуальное evidence | registry и artifact |
| `return_anchor` | куда возвращаться после действия | registry, sync-report |

## Активные маршруты

| Issue | Роль | Артефакт | Evidence |
|---|---|---|---|
| `CB-P2` | Phase 2 patch по утверждённому реестру D-001…D-063 | [`CB-P2/README.md`](CB-P2/README.md) | `Validation/final_check.md`, `Validation/sync_report.md` |
| `CB-002` | common core protocols | [`CB-002/README.md`](CB-002/README.md) | `Protocols/state_architecture.md`, `Protocols/context_loading.md` |
| `CB-003` | issue workflow | [`CB-003/README.md`](CB-003/README.md) | `Protocols/issue_lifecycle.md`, `Issues/issue_events.jsonl` |
| `CB-004` | write/conflict/validation protocols | [`CB-004/README.md`](CB-004/README.md) | `Protocols/github_write_protocol.md`, `Protocols/validation_protocol.md` |
| `CB-005` | execution bootstrap and concept template | [`CB-005/README.md`](CB-005/README.md) | `Protocols/execution_bootstrap.md`, `Templates/concept/README.md` |
| `CB-006` | template library | [`CB-006/README.md`](CB-006/README.md) | `Templates/README.md`, `Protocols/template_validation.md` |
| `CB-007` | task flow hardening | [`CB-007/README.md`](CB-007/README.md) | `Protocols/task_flow_hardening.md`, `Templates/task/README.md` |
| `CB-008` | dry-run validation | [`CB-008/README.md`](CB-008/README.md) | `Validation/cb008_dry_run.md`, `Validation/cb008_closure_plan.md` |
| `CB-009` | smoke fixture and export | [`CB-009/README.md`](CB-009/README.md) | `Concepts/smoke/README.md`, `Concepts/smoke/export.md` |

## Cleanup decisions

- `Issues/cb89.md` не является активным production issue artifact: сведения разделены между `CB-008`, `CB-009`, registry/events и validation.
- `Plans/cb008.md` не восстанавливается: валидная часть перенесена в `Validation/cb008_closure_plan.md`.
- Закрытие issue допускается только при связанном report/evidence, а не по одиночному статусному слову.

## P2-005 правило

P2-005 нормализует issue index, registry row, event log и per-issue artifacts как одну связанную модель. Если один элемент не совпадает с остальными, статус остаётся `partial` или `blocked`, а не финальным.