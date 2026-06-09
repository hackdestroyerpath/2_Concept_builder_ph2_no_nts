# Маркер ответа

[← Реестр протоколов](protocol_index.md) | [Архитектура состояния](state_architecture.md)

## Назначение

Маркер ответа фиксирует рабочее состояние в конце каждого ответа агента.

## Формат

```text
mode:
active_object:
active_issue:
stage:
loaded_context:
persistence_status:
next_step:
return_anchor:
```

## Поля

| Поле | Смысл |
|---|---|
| `mode` | Активный режим: `Service Mode` или `Execution Mode`. |
| `active_object` | Система, концепция или иной объект работы. |
| `active_issue` | Текущая задача или `none`. |
| `stage` | Короткий идентификатор текущей стадии. |
| `loaded_context` | Файлы, реально прочитанные для ответа. |
| `persistence_status` | Статус записи и проверки в `GitHub`. |
| `next_step` | Следующий ограниченный шаг. |
| `return_anchor` | Файл, с которого удобно продолжить. |

## Правила

1. Маркер не заменяет отчёт, а дополняет его.
2. `loaded_context` не должен заявлять файлы, которые не были прочитаны.
3. `persistence_status` показывает `not_written`, `written_unverified`, `synced` или причину блокировки.
4. Если менялся state, маркер должен совпадать с новым state.
