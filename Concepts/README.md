# Концепции

[← Точка входа](../README.md) | [Состояние исполнения](../State/execution_state.md) | [Начальная загрузка исполнения](../Protocols/execution_bootstrap.md) | [Проверочный пример](smoke/README.md)

`Concepts/` хранит конкретные концепции как связанные сети Markdown-файлов с локальным реестром, состоянием, результатом и манифестом экспорта.

## Управление

| Поле | Значение |
|---|---|
| Владелец | `Execution Mode` |
| Источник истины | `README.md`, `concept_state.md` и `page_registry.jsonl` каждой концепции |
| Глобальный маршрут | `README.md` → `Concepts/README.md` |
| Протокол запуска | [`Protocols/execution_bootstrap.md`](../Protocols/execution_bootstrap.md) |
| Протокол экспорта | [`Protocols/concept_export.md`](../Protocols/concept_export.md) |

## Текущие рабочие записи

| Концепция | Роль | Статус | Задача |
|---|---|---|---|
| [`smoke`](smoke/README.md) | проверочный пример | сохранён для пробного прогона исполнения и экспорта; доказательство перечитывания записано | [`CB-009`](../Issues/CB-009/README.md) |

## Создание новой концепции

Новая пользовательская концепция создаётся только после явной начальной загрузки `Execution Mode`:

```text
Concepts/<concept_id>/
```

Базовая структура копируется из [`Templates/concept/`](../Templates/concept/README.md), затем заполняются `README.md`, `concept_state.md`, `structure.md`, `page_registry.jsonl`, `purpose.md`, `requirements.md`, `operating_model.md`, `process.md`, `output.md` и `export.md`.

## Политика проверочного примера `smoke`

`smoke` не является пользовательской концепцией. Он остаётся как проверочный пример для проверки шаблона и маршрута экспорта. Несвязанные или пустые файлы внутри примера удаляются, а строгие страницы результата и экспорта сохраняются как `output.md` и `export.md`.

## Обязательная проверка

После создания или выбора концепции обновляются `State/execution_state.md`, локальный реестр и связь задачи, затем запускается [`Protocols/validation_protocol.md`](../Protocols/validation_protocol.md). Для `smoke` финальные доказательства Phase 2 находятся в [`Validation/final_check.md`](../Validation/final_check.md) и [`Validation/sync_report.md`](../Validation/sync_report.md).