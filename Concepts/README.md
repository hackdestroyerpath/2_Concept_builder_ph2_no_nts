# Concepts

[← Точка входа](../README.md) | [Execution state](../State/execution_state.md) | [Execution bootstrap](../Protocols/execution_bootstrap.md) | [Smoke fixture](smoke/README.md)

`Concepts/` хранит конкретные концепции как связанные сети MD-файлов с локальным registry, state, output и export manifest.

## Current production entries

| Concept | Role | Status | Issue |
|---|---|---|---|
| [`smoke`](smoke/README.md) | validation fixture | retained for Execution/export dry-run | [`CB-009`](../Issues/CB-009/README.md) |

## Создание новой концепции

Новая пользовательская концепция создаётся только после explicit `Execution Mode` bootstrap:

```text
Concepts/<concept_id>/
```

Базовая структура копируется из [`Templates/concept/`](../Templates/concept/README.md), затем заполняются `README.md`, `concept_state.md`, `structure.md`, `page_registry.jsonl`, `purpose.md`, `requirements.md`, `operating_model.md`, `process.md`, `output.md` и `export.md`.

## Smoke fixture policy

`smoke` не является пользовательской концепцией. Он остаётся как validation fixture для проверки шаблона и export route. Orphan/stub файлы внутри fixture удаляются, а strict output/export pages сохраняются как `output.md` и `export.md`.

## Обязательная проверка

После создания или выбора концепции обновляется `State/execution_state.md`, local registry и issue link, затем запускается [`Protocols/validation_protocol.md`](../Protocols/validation_protocol.md).
