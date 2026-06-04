# Протокол границ режимов

[← К реестру протоколов](protocol_index.md)

## Цель

Разделять обслуживание системы и работу с конкретными концепциями.

## Матрица

| Режим | Чтение | Запись |
|---|---|---|
| `Service Mode` | сервисные файлы, service `issue`, registry, state | `README.md`, `Instructions/`, `Protocols/`, `State/`, `Issues/`, `Inbox/`, `Registry/` |
| `Execution Mode` | выбранная концепция, её state, её `issue`, нужные общие протоколы | `Concepts/{concept_id}/`, связанные `issue`, output выбранной концепции |

## Проверка перед действием

1. Сопоставить команду пользователя с текущим `active_mode`.
2. Проверить `active_object` и `allowed_write_scope`.
3. Если команда относится к другому режиму, остановить запись за пределами scope.
4. Создать transfer-issue или дать точный route к нужному режиму.
5. В marker указать причину остановки или передачи.

## Выход

`allowed`, `blocked` или `transfer_needed` с указанием следующего протокола.
