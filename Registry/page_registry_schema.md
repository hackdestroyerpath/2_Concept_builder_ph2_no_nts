# Page registry schema

[← Структура](structure.md) | [Реестр страниц](page_registry.jsonl) | [Validation](../Validation/navigation_check.md)

## Назначение

`Registry/page_registry.jsonl` — машинная карта production-файлов `Concept Builder`. Реестр нужен не только для списка путей, а для проверки навигации, владельцев, backlinks, источников истины и orphan/debris cleanup.

## Запись JSONL

Каждая строка — один JSON-объект.

```json
{"path":"README.md","title":"Точка входа","type":"markdown","owner":"Service Mode","parent":null,"children":["Protocols/protocol_index.md"],"cross_links":["Validation/final_check.md"],"backlinks":[],"description":"Главная карта системы.","source_of_truth":"production","navigation_status":"reachable"}
```

## Обязательные поля

| Поле | Тип | Смысл |
|---|---|---|
| `path` | string | Путь production-файла от корня репозитория. |
| `title` | string | Человекочитаемое название страницы. |
| `type` | string | `markdown`, `jsonl`, `template`, `state`, `validation`, `issue_artifact`. |
| `owner` | string | `Service Mode`, `Execution Mode` или конкретный production-owner. |
| `parent` | string/null | Родительская reachable-страница. |
| `children` | array | Дочерние страницы, которые должны быть достижимы из текущей. |
| `cross_links` | array | Функциональные ссылки вне дерева. |
| `backlinks` | array | Страницы, которые должны ссылаться назад или входить в маршрут. |
| `description` | string | Роль файла в системе. |
| `source_of_truth` | string | Где подтверждается актуальность файла: `production`, `state`, `issue_registry`, `validation`, `template_registry`, `concept_registry`. |
| `navigation_status` | string | `reachable`, `local_reachable`, `registered_exception`, `removed_with_reason`, `blocked`. |

## Исключения

`Plans/`, `Closure/`, `Issues/cb89.md`, `Concepts/smoke/o2.md`, patch-handoff, Phase 1 audit, prompt-ы, checkpoint-и и исходный handoff-архив не должны иметь активных production-записей. Если путь удалён с причиной, причина фиксируется в `Validation/final_check.md` и `Issues/issue_events.jsonl`, а не в активном navigation tree.

## Проверки

1. Все MD/JSONL production-файлы имеют запись.
2. Каждая запись указывает существующий файл или documented removed path в evidence, но removed path не должен оставаться активным production-файлом.
3. Каждая MD-страница достижима от `README.md`, mode entry или local concept/template entry.
4. Backlinks проверяются по `Validation/navigation_check.md`.
5. Реестр обновляется в том же patch-сегменте, что и state/events/validation.
