# {{concept_title}}

[← Concepts](../../Concepts/README.md) | [Структура](structure.md) | [State](concept_state.md) | [Локальный registry](page_registry.jsonl) | [Export](export.md)

## Идентификаторы

```text
concept_id: {{concept_id}}
concept_title: {{concept_title}}
status: draft | active | validation | export_ready | archived
owner_issue: {{issue_id}}
owner_mode: Execution Mode
persistence_status: template_not_instantiated
```

## Назначение

{{purpose_summary}}

## Обязательные страницы

| Страница | Назначение | Gate |
|---|---|---|
| [`concept_state.md`](concept_state.md) | текущий state концепции | active issue selected |
| [`structure.md`](structure.md) | локальное дерево | совпадает с local registry |
| [`page_registry.jsonl`](page_registry.jsonl) | local registry с metadata | без path-only rows |
| [`purpose.md`](purpose.md) | цель, проблема, границы | scope defined |
| [`requirements.md`](requirements.md) | requirements and acceptance criteria | approved or scoped |
| [`operating_model.md`](operating_model.md) | roles, objects, invariants | failure modes listed |
| [`process.md`](process.md) | рабочий process | validation hooks present |
| [`output.md`](output.md) | expected results and mapping | requirements mapped |
| [`export.md`](export.md) | export manifest | source paths and scope listed |

## Правило работы

Все изменения этой концепции выполняются через `Execution Mode`, связанный `issue`, local registry update и `validation_protocol.md`. Orphan-файлы запрещены; любой удалённый path должен быть заранее записан в local registry/evidence.
