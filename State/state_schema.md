# Схема state

[← К главной точке входа](../README.md)

## Минимальные поля

```text
active_mode
active_object
active_issue
current_stage
dialogue_state
active_menu_id
loaded_context
loaded_protocols
allowed_read_scope
allowed_write_scope
next_step
return_anchor
persistence_status
```

## Правила

1. State отражает фактическое состояние после последней проверенной записи.
2. `allowed_write_scope` уже, чем `allowed_read_scope`.
3. `active_issue: none` используется, если issue не выбран.
4. `persistence_status` меняется только после проверки сохранения или ошибки.
5. Новое поле добавляется только если у него есть владелец, назначение и потребитель в протоколе.

## Файлы state

- [`service_state.md`](service_state.md) — состояние `Service Mode`.
- [`execution_state.md`](execution_state.md) — состояние `Execution Mode`.
