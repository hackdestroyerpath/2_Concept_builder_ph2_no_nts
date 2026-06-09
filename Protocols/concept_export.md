# Concept export

[← Реестр протоколов](protocol_index.md) | [Execution state](../State/execution_state.md) | [Concepts](../Concepts/README.md)

## Назначение

Протокол описывает подготовку export-результата для выбранной концепции. Export — это проверяемый production-вывод, сформированный из утверждённых файлов концепции.

## Когда применяется

`concept_export` применяется в `Execution Mode`, когда у концепции есть утверждённые требования, рабочая структура, связанные страницы и критерии готовности.

## Минимальная структура export

```text
concept_id:
concept_title:
source_paths:
export_scope:
audience:
output_format:
acceptance_criteria:
validation_status:
```

## Разрешённые источники

Export собирается только из production-файлов выбранной концепции внутри `Concepts/` и связанных с ней реестров. Черновики, вложенные архивы, промежуточные отчёты и материалы задания не входят в export без явного переноса в production.

## Этапы

1. Проверить выбранный `active_object` в `State/execution_state.md`.
2. Проверить связанные `issue` и требования.
3. Определить список source paths.
4. Сформировать export-файл или export-раздел в разрешённой области концепции.
5. Проверить ссылки, полноту и критерии готовности.
6. Обновить state, registry и event log.

## Правила качества

- Export должен иметь ясную аудиторию и формат.
- Export не должен ссылаться на несуществующие страницы.
- Export не должен смешивать несколько концепций без связанного `issue`.
- Export получает статус `ready` только после validation protocol.

## Блокировки

Если концепция не выбрана, требования отсутствуют или source paths невалидны, export не создаётся. Агент переводит `issue` в `question_answer`, `requirements` или `blocked`.
