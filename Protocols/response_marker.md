# Маркер ответа

[← Реестр протоколов](protocol_index.md) | [Архитектура состояния](state_architecture.md) | [Загрузка контекста](context_loading.md)

## Назначение

Маркер ответа — короткая человекочитаемая проекция state в конце ответа агента. Он не заменяет registry, event log, sync-report или validation evidence, а показывает, откуда продолжать.

## Канонический формат

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

## Mapping к state

| Marker field | State field | Правило |
|---|---|---|
| `mode` | `active_mode` | `Service Mode` или `Execution Mode`. |
| `active_object` | `active_object` | Production repo или выбранная концепция. |
| `active_issue` | `active_issue` | Текущий issue ID или `none`. |
| `stage` | `current_stage` | В state хранится canonical `current_stage`; в маркере — короткий alias `stage`. |
| `loaded_context` | `loaded_context_scope` | Только реально прочитанные файлы. |
| `persistence_status` | `persistence_status` | Read/write status без assertion-only финала. |
| `next_step` | `next_step` | Один следующий bounded step. |
| `return_anchor` | `return_anchor` | Существующий production-файл. |

## Разрешённые persistence-status значения

| Значение | Когда использовать |
|---|---|
| `not_written` | Действие только читало контекст. |
| `written_unverified` | Запись выполнена, но GitHub readback ещё не прошёл. |
| `readback_required` | Есть записанные файлы, которые нужно перечитать. |
| `partial` | Часть acceptance criteria не закрыта evidence. |
| `blocked` | Нельзя продолжать без условия, решения или контекста. |
| `conflict` | Readback/SHA/API показали конфликт. |
| `failed` | Действие завершилось ошибкой с evidence. |

Слова `closed`, `passed`, `synced`, `Ready`, `OK` не используются как доказательство. Если их нужно упомянуть как внешние tokens, рядом указывается русское значение и evidence.

## Правила

1. Маркер всегда согласован с active state.
2. `stage` не должен расходиться с `current_stage`.
3. `loaded_context` не должен включать файлы, которые не читались.
4. `next_step` не должен перескакивать dependency.
5. После записи в `GitHub` маркер должен ссылаться на `Validation/sync_report.md` или другой readback anchor.
6. Если state менялся, response marker проверяется как часть P2-003/P2-010 validation.

## P2-003 check

P2-003 закрепляет lossless mapping `state → marker → next turn`: state хранит подробный ledger, marker показывает компактный route, sync-report содержит readback evidence.
