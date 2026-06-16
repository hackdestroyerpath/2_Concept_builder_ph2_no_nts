# Concepts

[← Точка входа](../README.md) | [Execution state](../State/execution_state.md) | [Execution bootstrap](../Protocols/execution_bootstrap.md) | [Smoke fixture](smoke/README.md)

`Concepts/` хранит конкретные концепции как связанные сети MD-файлов с локальным registry, state, output и export manifest.

## Управление

| Поле | Значение |
|---|---|
| Владелец | `Execution Mode` |
| Источник истины | README, `concept_state.md` и `page_registry.jsonl` каждой концепции |
| Глобальный маршрут | `README.md` → `Concepts/README.md` |
| Протокол запуска | [`Protocols/execution_bootstrap.md`](../Protocols/execution_bootstrap.md) |
| Протокол экспорта | [`Protocols/concept_export.md`](../Protocols/concept_export.md) |

## Текущие production-записи

| Концепция | Роль | Статус | Issue |
|---|---|---|---|
| [`smoke`](smoke/README.md) | validation fixture | сохранён для Execution/export dry-run; readback evidence recorded | [`CB-009`](../Issues/CB-009/README.md) |

## Создание новой концепции

Новая пользовательская концепция создаётся только после явного `Execution Mode` bootstrap:

```text
Concepts/<concept_id>/
```

Базовая структура копируется из [`Templates/concept/`](../Templates/concept/README.md), затем заполняются `README.md`, `concept_state.md`, `structure.md`, `page_registry.jsonl`, `purpose.md`, `requirements.md`, `operating_model.md`, `process.md`, `output.md` и `export.md`.

## Политика smoke fixture

`smoke` не является пользовательской концепцией. Он остаётся как validation fixture для проверки шаблона и export route. Orphan/stub файлы внутри fixture удаляются, а strict output/export pages сохраняются как `output.md` и `export.md`.

## Обязательная проверка

После создания или выбора концепции обновляется `State/execution_state.md`, local registry и issue link, затем запускается [`Protocols/validation_protocol.md`](../Protocols/validation_protocol.md). Для `smoke` финальное Phase 2 evidence находится в [`Validation/final_check.md`](../Validation/final_check.md) и [`Validation/sync_report.md`](../Validation/sync_report.md).
