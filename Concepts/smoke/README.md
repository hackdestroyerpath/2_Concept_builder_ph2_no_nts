# Smoke validation fixture

[← Concepts](../README.md) | [State](concept_state.md) | [Registry](page_registry.jsonl) | [Issue CB-009](../../Issues/CB-009/README.md)

```text
concept_id: smoke
concept_title: Smoke validation fixture
owner_mode: Execution Mode
active_issue: CB-009
status: validation_fixture
purpose: проверить структуру концепции, local registry, output/export и границы Execution Mode
persistence_status: synced_with_final_readback_evidence
```

## Назначение

`Concepts/smoke` — production-фикстура валидации. Это не пользовательская концепция и не пример бизнес-содержания. Папка сохранена, чтобы проверять создание концепции из шаблона, локальные ссылки, registry, output model и export manifest.

## Навигация

| Файл | Роль | Состояние evidence |
|---|---|---|
| [`concept_state.md`](concept_state.md) | state фикстуры и готовность export | readback на `main` |
| [`structure.md`](structure.md) | локальное дерево | readback на `main` |
| [`page_registry.jsonl`](page_registry.jsonl) | локальный registry с владельцами и backlinks | readback на `main` |
| [`purpose.md`](purpose.md) | цель и scope фикстуры | readback на `main` |
| [`requirements.md`](requirements.md) | требования и acceptance criteria | readback на `main` |
| [`operating_model.md`](operating_model.md) | объекты, роли, инварианты, failure modes | readback на `main` |
| [`process.md`](process.md) | исполнимый dry-run scenario | readback на `main` |
| [`output.md`](output.md) | output mapping | readback на `main` |
| [`export.md`](export.md) | export manifest | readback на `main` |

## Cleanup

Alternate output/export scratch files не являются production-страницами fixture. Строгие production pages: `output.md` и `export.md`. Отсутствие orphan/stub debris проверено в `Validation/sync_report.md`.
