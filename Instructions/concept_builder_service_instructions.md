# Инструкция проекта `Concept Builder Service Mode`

[← К главной точке входа](../README.md)

## Назначение

Эта инструкция запускает агента, который обслуживает саму систему `Concept Builder`: протоколы, инструкции, state, registry, service `issue` и правила записи.

## Bootstrap

1. Загрузить [`../README.md`](../README.md).
2. Загрузить [`../State/service_state.md`](../State/service_state.md).
3. Загрузить [`../Protocols/protocol_index.md`](../Protocols/protocol_index.md).
4. Определить текущий `dialogue_state`, активное меню и допустимый write scope.
5. Подгрузить только протокол, нужный для текущего действия.

## Границы режима

`Service Mode` может менять только сервисные production-файлы: `README.md`, `Instructions/`, `Protocols/`, `State/`, `Issues/`, `Inbox/`, `Registry/` и утверждённые `Scripts/`, если они появятся через отдельный `issue`.

`Service Mode` не развивает содержимое конкретной концепции вместо `Execution Mode`. Если пользователь просит менять концепцию, агент создаёт transfer-issue или указывает вход в [`../Concepts/README.md`](../Concepts/README.md).

## Обязательная запись

Перед ответом, который меняет state или артефакт, агент обязан сохранить изменение в `GitHub`, перечитать изменённые файлы и сообщить sync-status. Если запись невозможна, агент фиксирует `persistence_status: failed` или `conflict` и не делает вид, что состояние сохранено.

## Контекст

Загружать весь репозиторий запрещено без отдельной причины. Минимальный контекст: state режима, активный `issue`, protocol index и профильный протокол текущего действия.

## Ответ

Каждый содержательный ответ содержит marker:

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
