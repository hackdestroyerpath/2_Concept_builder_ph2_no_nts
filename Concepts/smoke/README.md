# Фикстура smoke-валидации

[← Концепции](../README.md) | [Состояние](concept_state.md) | [Реестр](page_registry.jsonl) | [Issue CB-009](../../Issues/CB-009/README.md)

```text
concept_id: smoke
concept_title: Фикстура smoke-валидации
owner_mode: Execution Mode
active_issue: CB-009
status: validation_fixture
purpose: проверить структуру концепции, локальный реестр, страницы output/export и границы Execution Mode
persistence_status: synced_with_final_readback_evidence
```

## Назначение

`Concepts/smoke` — фикстура валидации рабочего контура. Это не пользовательская концепция и не пример бизнес-содержания. Папка сохранена, чтобы проверять создание концепции из шаблона, локальные ссылки, реестр, модель результата (`output`) и манифест экспорта (`export`).

## Навигация

| Файл | Роль | Состояние доказательств |
|---|---|---|
| [`concept_state.md`](concept_state.md) | состояние фикстуры и готовность к экспорту | перечитано после P2R4 |
| [`structure.md`](structure.md) | локальное дерево | перечитано после P2R4 |
| [`page_registry.jsonl`](page_registry.jsonl) | локальный реестр с владельцами и обратными ссылками | перечитано после P2R4 |
| [`purpose.md`](purpose.md) | цель и область фикстуры | перечитано после P2R4 |
| [`requirements.md`](requirements.md) | требования и критерии приёмки | перечитано после P2R4 |
| [`operating_model.md`](operating_model.md) | объекты, роли, инварианты и режимы отказа | перечитано после P2R4 |
| [`process.md`](process.md) | исполнимый сценарий проверки | перечитано после P2R4 |
| [`output.md`](output.md) | карта результата (`output`) | перечитано после P2R4 |
| [`export.md`](export.md) | манифест экспорта | перечитано после P2R4 |

## Очистка

Черновые альтернативы для результата и экспорта не являются рабочими страницами фикстуры. Строгий набор рабочих страниц: `output.md` и `export.md`. Отсутствие осиротевшего или заглушечного мусора проверено в `Validation/sync_report.md`.
