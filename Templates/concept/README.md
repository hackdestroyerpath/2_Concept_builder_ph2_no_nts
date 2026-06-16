# {{concept_title}}

[← Концепции](../../Concepts/README.md) | [Структура](structure.md) | [Состояние](concept_state.md) | [Локальный реестр](page_registry.jsonl) | [Экспорт](export.md)

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
| [`concept_state.md`](concept_state.md) | текущее состояние концепции | активная задача выбрана |
| [`structure.md`](structure.md) | локальное дерево | совпадает с локальным реестром |
| [`page_registry.jsonl`](page_registry.jsonl) | локальный реестр с метаданными | нет строк только с путём |
| [`purpose.md`](purpose.md) | цель, проблема и границы | область определена |
| [`requirements.md`](requirements.md) | требования и критерии приёмки | утверждены или ограничены |
| [`operating_model.md`](operating_model.md) | роли, объекты и инварианты | режимы отказа перечислены |
| [`process.md`](process.md) | рабочий процесс | проверочные зацепки присутствуют |
| [`output.md`](output.md) | ожидаемые результаты и сопоставление | требования сопоставлены |
| [`export.md`](export.md) | манифест экспорта | исходные пути и область перечислены |

## Правило работы

Все изменения этой концепции выполняются через `Execution Mode`, связанную задачу, обновление локального реестра и `validation_protocol.md`. Несвязанные файлы не добавляются; удалённый путь заранее фиксируется в локальном реестре и доказательствах.