# Архитектура состояния

[← Реестр протоколов](protocol_index.md) | [Service state](../State/service_state.md) | [Execution state](../State/execution_state.md)

## Назначение

Этот протокол задаёт минимальную модель состояния `Concept Builder`. State обеспечивает непрерывность работы агента между действиями, проверками и записями в `GitHub`.

## Источники состояния

| Файл | Режим | Назначение |
|---|---|---|
| `State/service_state.md` | `Service Mode` | Состояние обслуживания системы, протоколов, реестров и сервисных `issue`. |
| `State/execution_state.md` | `Execution Mode` | Состояние работы с выбранной концепцией внутри `Concepts/`. |

## Обязательные поля

```text
active_mode:
active_object:
active_issue:
current_stage:
loaded_context:
loaded_protocols:
allowed_read_scope:
allowed_write_scope:
persistence_status:
next_step:
return_anchor:
```

## Правила обновления

1. Перед чтением дополнительных файлов агент читает state активного режима.
2. Перед записью агент сверяет `allowed_write_scope` с целевыми путями.
3. После успешной записи агент перечитывает изменённые файлы из `GitHub`.
4. `persistence_status` нельзя ставить как `synced`, пока проверочное чтение не прошло.
5. `active_issue` указывает на текущую задачу или `none`, если задача не заведена.
6. State другого режима не меняется без явной передачи задачи между режимами.

## Стадии

Стадия должна быть коротким техническим идентификатором. Примеры:

```text
initial_repository_skeleton
common_core_protocols_synced
issue_lifecycle_design
waiting_for_concept_selection
concept_requirements_collection
```

## Ошибки состояния

Если state противоречит команде пользователя, агент не пишет в репозиторий. Он фиксирует причину, предлагает transfer-issue или создаёт сервисное `issue`, если это разрешено активным режимом.
