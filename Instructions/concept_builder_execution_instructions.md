# Инструкция проекта `Concept Builder`

[← К главной точке входа](../README.md) | [Вход `Execution Mode`](../Concepts/README.md)

## Назначение

Эта инструкция запускает агента `Execution Mode`, который работает с конкретными концепциями внутри `Concepts/` и не обслуживает архитектуру системы без передачи в `Service Mode`.

## Bootstrap

1. Загрузить [`../Concepts/README.md`](../Concepts/README.md).
2. Загрузить [`../State/execution_state.md`](../State/execution_state.md).
3. Загрузить [`../Protocols/protocol_index.md`](../Protocols/protocol_index.md).
4. Определить активную концепцию, активный `issue`, return-anchor и allowed write scope.
5. Подгрузить только локальные файлы выбранной концепции и протокол текущего действия.

## Границы режима

`Execution Mode` пишет только в выбранную концепцию, её рабочие `issue`, связанный state и output. Он не меняет сервисные протоколы, инструкции и глобальные registry без transfer-issue в `Service Mode`.

Если активная концепция не выбрана, агент показывает безопасный вход: создать новую концепцию через `issue` или выбрать существующую папку в `Concepts/`.

## Работа с концепцией

Каждая концепция должна быть связанной MD-сетью с входным `README.md`, утверждёнными требованиями, `operating_model`, процессом, `structure.md` и `page_registry.jsonl`. Файл без маршрута из входного README считается сиротой и не используется.

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
