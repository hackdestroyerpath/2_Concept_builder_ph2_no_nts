# Execution Mode bootstrap

[← Реестр протоколов](protocol_index.md) | [Execution state](../State/execution_state.md) | [Concepts](../Concepts/README.md)

## Назначение

Протокол описывает безопасный вход в `Execution Mode`: выбор существующей концепции или создание новой концепции из production-шаблона.

## Когда применяется

`execution_bootstrap` применяется, когда пользователь просит создать, выбрать или продолжить конкретную концепцию внутри `Concepts/`.

## Входные данные

```text
command:
concept_id:
concept_title:
mode:
active_issue:
source_materials:
acceptance_criteria:
```

`concept_id` должен быть коротким техническим идентификатором без пробелов. Название концепции хранится отдельно как `concept_title`.

## Создание концепции

1. Проверить, что задача относится к `Execution Mode`.
2. Создать или подтвердить `issue` на создание концепции.
3. Проверить `concept_id`, чтобы не перезаписать существующую папку.
4. Скопировать структуру из `Templates/concept/` в `Concepts/<concept_id>/`.
5. Заполнить `README.md`, `structure.md`, `page_registry.jsonl` и стартовые страницы концепции.
6. Обновить `State/execution_state.md`, глобальный `Registry/page_registry.jsonl` и журналы `Issues/`.
7. Запустить `Protocols/validation_protocol.md`.

## Выбор существующей концепции

1. Найти папку `Concepts/<concept_id>/`.
2. Прочитать `Concepts/<concept_id>/README.md` и локальный `page_registry.jsonl`.
3. Обновить `State/execution_state.md`.
4. Вернуть маркер ответа с выбранным `active_object`.

## Блокировки

Концепция не создаётся, если отсутствует `concept_id`, неясен режим, конфликтует путь, нет `issue` или нарушена область записи.
