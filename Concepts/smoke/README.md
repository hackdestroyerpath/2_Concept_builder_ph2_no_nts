# Smoke validation fixture

[← Concepts](../README.md) | [State](concept_state.md) | [Registry](page_registry.jsonl) | [Issue CB-009](../../Issues/CB-009/README.md)

```text
concept_id: smoke
concept_title: Smoke validation fixture
owner_mode: Execution Mode
active_issue: CB-009
status: validation_fixture
purpose: проверить структуру концепции, local registry, output/export и границы Execution Mode
persistence_status: written_unverified_until_final_readback
```

## Назначение

`Concepts/smoke` — production validation fixture. Это не пользовательская концепция и не пример бизнес-содержания. Папка сохранена, чтобы проверять создание концепции из шаблона, локальные ссылки, registry, output model и export manifest.

## Навигация

| Файл | Роль |
|---|---|
| [`concept_state.md`](concept_state.md) | state fixture и export readiness |
| [`structure.md`](structure.md) | локальное дерево |
| [`page_registry.jsonl`](page_registry.jsonl) | локальный registry с владельцами и backlinks |
| [`purpose.md`](purpose.md) | цель и scope fixture |
| [`requirements.md`](requirements.md) | требования и acceptance criteria |
| [`operating_model.md`](operating_model.md) | объекты, роли, инварианты, failure modes |
| [`process.md`](process.md) | executable dry-run scenario |
| [`output.md`](output.md) | output mapping |
| [`export.md`](export.md) | export manifest |

## Cleanup

`o2.md`, alternate `output.txt` и `e.txt` не являются production-страницами fixture. Strict production pages: `output.md` and `export.md`.
