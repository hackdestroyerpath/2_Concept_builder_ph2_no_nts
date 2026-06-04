# Протокол разбора команд

[← К реестру протоколов](protocol_index.md)

## Цель

Разбирать короткие и числовые команды через текущий `dialogue_state` и последнее меню.

## Входы

- `dialogue_state`;
- `active_menu_id`;
- последнее меню;
- текст команды;
- `active_issue` и стадия.

## Правила

1. Один символ имеет одно значение в одном state.
2. `1` и `2` действуют только для последнего меню в state.
3. При неясном меню агент сначала восстанавливает state.
4. При смене режима применяется `mode_boundary_protocol.md`.

## Таблица

| `dialogue_state` | Команда | Действие |
|---|---|---|
| `awaiting_primary_navigation` | `1` | создать новый `issue` |
| `awaiting_primary_navigation` | `2` | выбрать существующий `issue` |
| `awaiting_issue_registry_decision` | `утвердить всё` | перевести кандидаты в `approved` |
| `awaiting_issue_registry_decision` | `обсудить ISSUE-ID` | открыть обсуждение одного `issue` |
| `awaiting_requirements_decision` | `утверждаю` | принять requirements |
| `awaiting_solution_decision` | `утверждаю` | принять solution и contract |

## Выход

Однозначное действие, запрос уточнения или остановка перехода до восстановления state.
