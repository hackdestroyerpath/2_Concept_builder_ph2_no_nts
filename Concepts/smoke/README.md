# Фикстура валидации smoke

[← Концепции](../README.md) | [State](concept_state.md) | [Registry](page_registry.jsonl) | [Issue CB-009](../../Issues/CB-009/README.md)

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

`Concepts/smoke` — production-фикстура валидации. Это не пользовательская концепция и не пример бизнес-содержания. Папка сохранена, чтобы проверять создание концепции из шаблона, локальные ссылки, registry, модель output и манифест export.

## Навигация

| Файл | Роль | Состояние доказательств |
|---|---|---|
| [`concept_state.md`](concept_state.md) | state фикстуры и готовность export | readback после P2R3 |
| [`structure.md`](structure.md) | локальное дерево | readback после P2R3 |
| [`page_registry.jsonl`](page_registry.jsonl) | локальный registry с владельцами и backlinks | readback после P2R3 |
| [`purpose.md`](purpose.md) | цель и scope фикстуры | readback после P2R3 |
| [`requirements.md`](requirements.md) | требования и критерии приёмки | readback после P2R3 |
| [`operating_model.md`](operating_model.md) | объекты, роли, инварианты и failure modes | readback после P2R3 |
| [`process.md`](process.md) | исполнимый сценарий проверки | readback после P2R3 |
| [`output.md`](output.md) | mapping для output | readback после P2R3 |
| [`export.md`](export.md) | манифест export | readback после P2R3 |

## Cleanup

Альтернативные scratch-файлы output/export не являются production-страницами fixture. Строгие production pages: `output.md` и `export.md`. Отсутствие orphan/stub debris проверено в `Validation/sync_report.md`.