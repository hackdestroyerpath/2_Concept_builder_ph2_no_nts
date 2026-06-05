# Схема state

[← К главной точке входа](../README.md)

## Минимальные поля режима

```yaml
active_mode:
active_object:
active_issue:
current_stage:
dialogue_state:
active_menu_id:
loaded_context: []
loaded_context_scope:
loaded_protocols: []
allowed_read_scope: []
allowed_write_scope: []
parent_chain: []
linked_dependencies: []
return_anchor:
next_step:
persistence_status:
last_verified_paths: []
```

## Поля `issue/state.md`

```yaml
issue_id:
title:
mode:
owner:
type:
status:
priority:
parent_issue:
child_issues: []
linked_issues: []
input_refs: []
reason_ref:
qa_ref:
requirements_ref:
solution_ref:
contract_ref:
output_ref:
report_ref:
dependency_status:
return_anchor:
next_step:
persistence_status:
```

## Статусы lifecycle

```text
creating → proposed → approved → questioning → requirements_review → solution_review → ready_for_execution → executing → completed → closed
```

Дополнительные статусы: `rejected`, `blocked`, `waiting_dependency`, `needs_discussion`, `cleanup_pending`.

## Статусы сохранения

| Статус | Значение |
|---|---|
| `synced` | запись выполнена и перечитана |
| `partial` | записана часть пакета, нужен следующий sync-step |
| `failed` | запись или проверка не прошла |
| `conflict` | найдено расхождение с текущим GitHub state |
| `not_required` | запись не требовалась |
| `blocked` | переход остановлен до решения причины |

## Правила

1. State отражает фактическое состояние после последней проверенной записи.
2. `allowed_write_scope` уже, чем `allowed_read_scope`.
3. `active_issue: none` используется, если issue не выбран.
4. `persistence_status` меняется только после проверки сохранения или ошибки.
5. Новое поле добавляется только если у него есть владелец, назначение и потребитель в протоколе.
6. После закрытия глубокого шага state возвращается к `return_anchor`, а детали сворачиваются в summary.

## Файлы state

- [`service_state.md`](service_state.md) — состояние `Service Mode`.
- [`execution_state.md`](execution_state.md) — состояние `Execution Mode`.
