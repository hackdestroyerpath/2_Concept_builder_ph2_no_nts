# Issues

[← Точка входа](../README.md) | [Issue registry](issue_registry.jsonl) | [Issue events](issue_events.jsonl) | [Lifecycle protocol](../Protocols/issue_lifecycle.md)

`Issues/` хранит production-артефакты жизненного цикла задач: reason, provenance, approval, dependencies, cleanup, validation и return-anchor. История восстанавливается только из имеющихся repo-фактов; недостающие детали помечаются как reconstructed, а не выдумываются постфактум, потому что магическое мышление уже достаточно натворило в `status: done`.

## Обязательная модель issue

| Поле | Назначение |
|---|---|
| `issue_id` | стабильный идентификатор |
| `type` | service, execution, patch, validation |
| `status` | proposed, approved, executing, validation, fixed_with_evidence, blocked, cleanup_removed |
| `priority` | blocker, major, normal |
| `reason` | почему issue существует |
| `provenance` | источник: пользователь, repo state, reconstructed baseline, audit-approved patch |
| `approval` | approved, reconstructed, not_required, blocked |
| `dependencies` | parent/child/linked issues и waiting states |
| `cleanup` | retained, migrated, removed_with_reason, pending |
| `current_refs` | production-файлы, где лежит актуальное evidence |
| `return_anchor` | куда возвращаться после действия |

## Активные маршруты

| Issue | Роль | Артефакт |
|---|---|---|
| `CB-P2` | Phase 2 patch по утверждённому реестру D-001…D-063 | [`CB-P2/README.md`](CB-P2/README.md) |
| `CB-002`…`CB-007` | реконструированные service issues исходной реализации | `CB-00X/README.md` |
| `CB-008` | dry-run проверки task/template lifecycle | [`CB-008/README.md`](CB-008/README.md), [`../Validation/cb008_dry_run.md`](../Validation/cb008_dry_run.md) |
| `CB-009` | smoke fixture и export dry-run | [`CB-009/README.md`](CB-009/README.md), [`../Concepts/smoke/README.md`](../Concepts/smoke/README.md) |

## Cleanup decisions

- `Issues/cb89.md` удаляется как debris: он смешивал `CB-008` и `CB-009` и не был lifecycle artifact.
- Валидные сведения из него перенесены в `CB-008`, `CB-009`, `issue_events.jsonl` и `Validation/`.
- Закрытие issue допускается только при связанном report/evidence, а не по одному слову `done`.
