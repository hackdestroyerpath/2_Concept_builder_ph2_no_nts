# Concepts

[← К точке входа](../README.md) | [Execution state](../State/execution_state.md) | [Execution bootstrap](../Protocols/execution_bootstrap.md)

`Concepts/` хранит конкретные концепции как связанные сети MD-файлов.

## Статус

Конкретные концепции ещё не выбраны. Создание концепции выполняется через утверждённый `issue`, `Execution Mode` и протокол [`execution_bootstrap`](../Protocols/execution_bootstrap.md).

## Создание новой концепции

Новая концепция создаётся в папке:

```text
Concepts/<concept_id>/
```

Базовая структура копируется из [`Templates/concept/`](../Templates/concept/README.md), затем заполняются `README.md`, `concept_state.md`, `structure.md`, `page_registry.jsonl` и стартовые страницы концепции.

## Обязательная проверка

После создания или выбора концепции обновляется `State/execution_state.md` и запускается `Protocols/validation_protocol.md`.
