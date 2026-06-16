# Проверочный пример `smoke`

[← Концепции](../README.md) | [Состояние](concept_state.md) | [Реестр](page_registry.jsonl) | [Задача CB-009](../../Issues/CB-009/README.md)

```text
concept_id: smoke
concept_title: Фикстура smoke-валидации
owner_mode: Execution Mode
active_issue: CB-009
status: validation_fixture
purpose: проверить структуру концепции, локальный реестр, страницы output/export и границы Execution Mode
persistence_status: synced_with_final_readback_evidence
```

Кодовый блок сохраняет технические поля, статусы и пути как machine-литералы.

## Назначение

`Concepts/smoke` — проверочный пример рабочего контура. Это не пользовательская концепция и не пример бизнес-содержания. Папка сохранена, чтобы проверять создание концепции из шаблона, локальные ссылки, реестр, модель результата (`output`) и манифест экспорта (`export`).

## Навигация

| Файл | Роль | Состояние доказательств |
|---|---|---|
| [`concept_state.md`](concept_state.md) | состояние примера и готовность к экспорту | перечитано после P2R5 |
| [`structure.md`](structure.md) | локальное дерево | перечитано после P2R5 |
| [`page_registry.jsonl`](page_registry.jsonl) | локальный реестр с владельцами и обратными ссылками | перечитано после P2R5 |
| [`purpose.md`](purpose.md) | цель и область примера | перечитано после P2R5 |
| [`requirements.md`](requirements.md) | требования и критерии приёмки | перечитано после P2R5 |
| [`operating_model.md`](operating_model.md) | объекты, роли, инварианты и режимы отказа | перечитано после P2R5 |
| [`process.md`](process.md) | исполнимый сценарий проверки | перечитано после P2R5 |
| [`output.md`](output.md) | карта результата (`output`) | перечитано после P2R5 |
| [`export.md`](export.md) | манифест экспорта | перечитано после P2R5 |

## Очистка

Черновые альтернативы для результата и экспорта не являются рабочими страницами примера. Строгий набор рабочих страниц: `output.md` и `export.md`. Отсутствие несвязанных или заглушечных файлов проверено в `Validation/sync_report.md`.