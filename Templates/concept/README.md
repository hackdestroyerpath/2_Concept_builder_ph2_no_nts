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

| Страница | Назначение | Контроль |
|---|---|---|
| [`concept_state.md`](concept_state.md) | текущий state концепции | active issue выбран |
| [`structure.md`](structure.md) | локальное дерево | совпадает с local registry |
| [`page_registry.jsonl`](page_registry.jsonl) | local registry с metadata | без path-only rows |
| [`purpose.md`](purpose.md) | цель, проблема и границы | scope определён |
| [`requirements.md`](requirements.md) | requirements и критерии приёмки | approved или scoped |
| [`operating_model.md`](operating_model.md) | роли, объекты и инварианты | failure modes перечислены |
| [`process.md`](process.md) | рабочий process | validation hooks присутствуют |
| [`output.md`](output.md) | ожидаемые результаты и mapping | requirements сопоставлены |
| [`export.md`](export.md) | export manifest | source paths и scope перечислены |

## Правило работы

Все изменения этой концепции выполняются через `Execution Mode`, связанный `issue`, обновление local registry и `validation_protocol.md`. Orphan-файлы запрещены; удалённый path заранее записывается в local registry/evidence.
