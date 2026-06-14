# Inbox

[← Точка входа](../README.md) | [Issues](../Issues/README.md) | [Issue registry](../Issues/issue_registry.jsonl) | [Events](../Issues/issue_events.jsonl)

`Inbox/` — временное хранилище входных материалов до их привязки к `issue`, переноса в production-совместимое место или очистки. Это staging-зона, а не кладбище файлов, хотя человечество явно старалось.

## Управление

| Поле | Значение |
|---|---|
| Владелец | `Service Mode` |
| Источник истины | `Issues/README.md`, `Issues/issue_registry.jsonl`, `Issues/issue_events.jsonl` |
| Глобальный маршрут | `README.md` → `Inbox/README.md` |
| Разрешённое содержимое | только входящие материалы с последующей классификацией |

## Правила

1. Входные материалы получают связь с `issue` до ответа агента.
2. Материалы не становятся частью готовой концепции автоматически.
3. После закрытия связанных `issue` выполняется cleanup или перенос с сохранением provenance.
4. Рабочие checkpoint-архивы реализации сюда не помещаются.
5. Development-материалы Phase 2 patch, audit, prompt-ы и исходный handoff-архив не загружаются в production repo.
