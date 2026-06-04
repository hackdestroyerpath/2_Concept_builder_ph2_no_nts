# Протокол переходов state

[← К реестру протоколов](protocol_index.md) | [Схема state](../State/state_schema.md)

## Цель

Менять state предсказуемо: один переход, один reason, один набор файлов и проверяемый результат.

## Входы

- текущий state;
- команда или событие;
- active mode;
- active object;
- active issue;
- целевой lifecycle status;
- affected paths.

## Правило перехода

```text
read current state
classify event
check mode and scope
write target artifacts
write event
update state
read back changed files
report marker
```

## Поля transition

| Поле | Смысл |
|---|---|
| `transition_id` | локальный ID перехода |
| `from_stage` | стадия до перехода |
| `to_stage` | стадия после перехода |
| `reason` | почему переход допустим |
| `paths` | production-файлы перехода |
| `verification` | что перечитано и проверено |

## Выход

Обновлённый state, event и marker с фактическим `persistence_status`.
