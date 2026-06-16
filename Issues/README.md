# Задачи

[← Точка входа](../README.md) | [Реестр задач](issue_registry.jsonl) | [События задач](issue_events.jsonl) | [Протокол жизненного цикла](../Protocols/issue_lifecycle.md)

`Issues/` хранит рабочие артефакты жизненного цикла задач: причину, происхождение, утверждение, зависимости, очистку, проверку и якорь возврата. История восстанавливается только из имеющихся фактов репозитория; недостающие детали помечаются как `reconstructed`, а не придумываются задним числом.

## Обязательная модель задачи

| Поле | Назначение | Где проверяется |
|---|---|---|
| `issue_id` | стабильный идентификатор | `Issues/issue_registry.jsonl` |
| `type` | тип: сервисный, исполнительный, исправление или проверка | реестр и заголовок артефакта |
| `status` | рабочий статус без финального ярлыка | реестр, журнал событий, проверка |
| `priority` | приоритет: `blocker`, `major`, `normal` | реестр |
| `reason` | почему задача существует | реестр и артефакт |
| `provenance` | источник: пользователь, состояние репозитория, восстановленная база или утверждённое аудиторское исправление | реестр и артефакт |
| `approval` | утверждение: `approved`, `reconstructed`, `not_required`, `blocked` | реестр |
| `dependencies` | родительские, дочерние и связанные задачи, а также состояния ожидания | реестр, связанные файлы |
| `cleanup` | очистка: `retained`, `migrated`, `removed_with_reason`, `pending` | реестр, события, проверка |
| `current_refs` | рабочие файлы с актуальными доказательствами | реестр и артефакт |
| `return_anchor` | куда возвращаться после действия | реестр, отчёт синхронизации |

## Активные маршруты

| Задача | Роль | Артефакт | Доказательства |
|---|---|---|---|
| `CB-P2` | исправление Phase 2 по утверждённому реестру `D-001`…`D-063` | [`CB-P2/README.md`](CB-P2/README.md) | `Validation/final_check.md`, `Validation/sync_report.md` |
| `CB-002` | общие базовые протоколы | [`CB-002/README.md`](CB-002/README.md) | `Protocols/state_architecture.md`, `Protocols/context_loading.md` |
| `CB-003` | рабочий цикл задач | [`CB-003/README.md`](CB-003/README.md) | `Protocols/issue_lifecycle.md`, `Issues/issue_events.jsonl` |
| `CB-004` | протоколы записи, конфликта и проверки | [`CB-004/README.md`](CB-004/README.md) | `Protocols/github_write_protocol.md`, `Protocols/validation_protocol.md` |
| `CB-005` | начальная загрузка исполнения и шаблон концепции | [`CB-005/README.md`](CB-005/README.md) | `Protocols/execution_bootstrap.md`, `Templates/concept/README.md` |
| `CB-006` | библиотека шаблонов | [`CB-006/README.md`](CB-006/README.md) | `Templates/README.md`, `Protocols/template_validation.md` |
| `CB-007` | усиление потока задач | [`CB-007/README.md`](CB-007/README.md) | `Protocols/task_flow_hardening.md`, `Templates/task/README.md` |
| `CB-008` | проверка пробным прогоном | [`CB-008/README.md`](CB-008/README.md) | `Validation/cb008_dry_run.md`, `Validation/cb008_closure_plan.md` |
| `CB-009` | проверочный пример и экспорт | [`CB-009/README.md`](CB-009/README.md) | `Concepts/smoke/README.md`, `Concepts/smoke/export.md` |

## Решения по очистке

- `Issues/cb89.md` не является активным рабочим артефактом задачи: сведения разделены между `CB-008`, `CB-009`, реестром, событиями и проверкой.
- `Plans/cb008.md` не восстанавливается: валидная часть перенесена в `Validation/cb008_closure_plan.md`.
- Закрытие задачи допускается только при связанном отчёте и доказательствах, а не по одиночному статусному слову.

## Правило P2-005

P2-005 нормализует индекс задач, строку реестра, журнал событий и артефакты отдельных задач как одну связанную модель. Если один элемент не совпадает с остальными, статус остаётся `partial` или `blocked`, а не финальным.