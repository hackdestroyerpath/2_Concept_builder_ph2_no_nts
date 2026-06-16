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

`Concepts/smoke` — production validation fixture. Это не пользовательская концепция и не пример бизнес-содержания. Папка сохранена, чтобы проверять создание концепции из шаблона, локальные ссылки, registry, output model и export manifest.

## Навигация

| Файл | Роль | Evidence state |
|---|---|---|
| [`concept_state.md`](concept_state.md) | state fixture и export readiness | read back on `main` |
| [`structure.md`](structure.md) | локальное дерево | read back on `main` |
| [`page_registry.jsonl`](page_registry.jsonl) | локальный registry с владельцами и backlinks | read back on `main` |
| [`purpose.md`](purpose.md) | цель и scope fixture | read back on `main` |
| [`requirements.md`](requirements.md) | требования и acceptance criteria | read back on `main` |
| [`operating_model.md`](operating_model.md) | объекты, роли, инварианты, failure modes | read back on `main` |
| [`process.md`](process.md) | executable dry-run scenario | read back on `main` |
| [`output.md`](output.md) | output mapping | read back on `main` |
| [`export.md`](export.md) | export manifest | read back on `main` |

## Cleanup

Alternate output/export scratch files не являются production-страницами fixture. Strict production pages: `output.md` and `export.md`. Отсутствие orphan/stub debris проверено в `Validation/sync_report.md`.
