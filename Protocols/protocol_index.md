# Реестр протоколов

[← К точке входа](../README.md)

`Protocols/protocol_index.md` — начальная карта маршрутизации. Детальные протоколы создаются последующими ограниченными этапами и не дублируются в инструкциях проекта.

## Обязательные направления

| Направление | Текущий статус | Планируемый источник истины |
|---|---|---|
| Загрузка контекста | запланировано | `Protocols/context_loading.md` |
| Маршрутизация режимов | запланировано | `Protocols/mode_routing.md` |
| Запись в `GitHub` | запланировано | `Protocols/github_write_protocol.md` |
| Жизненный цикл `issue` | запланировано | `Protocols/issue_lifecycle.md` |
| `Question Answer` | запланировано | `Protocols/question_answer.md` |
| `requirements` | запланировано | `Protocols/requirements_protocol.md` |
| `solution`, `contract`, выполнение и report | запланировано | `Protocols/issue_execution.md` |
| `complex issue` и linked issues | запланировано | `Protocols/complex_and_linked_issues.md` |
| Концепции и export | запланировано | `Protocols/concept_export.md` |
| Финальная проверка | запланировано | `Protocols/validation_protocol.md` |

## Правило маршрутизации

1. Агент сначала читает state активного режима.
2. Затем выбирает только те протоколы, которые нужны для текущего `current_stage` или команды пользователя.
3. Если протокол ещё не создан, агент фиксирует блокировку или создаёт сервисное `issue` на реализацию протокола.
4. Подробные процедуры не переносятся в инструкции проекта `ChatGPT`; инструкции остаются стартовыми файлами.

## Минимальный маркер ответа

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
