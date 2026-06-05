# Протокол фокусировки на `issue`

[← К реестру протоколов](protocol_index.md) | [Issues](../Issues/README.md)

## Цель

Перейти от общего registry к одному активному `issue` без загрузки лишней истории.

## Входы

- `Issues/issue_registry.jsonl`;
- `Issues/{issue_id}/state.md`;
- `Issues/{issue_id}/reason.md`;
- parent-chain и dependencies из registry;
- текущий `dialogue_state`.

## Процесс

1. Проверить, что `issue_id` существует в registry.
2. Загрузить только state, reason, текущую stage-страницу и прямые зависимости.
3. Установить `active_issue` в state режима.
4. Определить следующий протокол по статусу `issue`.
5. Сохранить return-anchor: registry, parent issue или concept README.
6. Перечитать state и показать marker.

## Status route

| Статус | Следующий протокол |
|---|---|
| `approved` | `qa_protocol` или `requirements_protocol` |
| `questioning` | `qa_protocol` |
| `requirements_review` | `requirements_protocol` |
| `solution_review` | `execution_protocol` |
| `waiting_dependency` | `linked_issue_protocol` |
| `completed` | `closure_cleanup_protocol` |

## Выход

Активный локальный контекст одного `issue` и безопасный следующий шаг.
