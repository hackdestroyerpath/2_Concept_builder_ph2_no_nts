# `Issues`

[← К главной точке входа](../README.md) | [Протокол lifecycle](../Protocols/issue_lifecycle_protocol.md)

Папка `Issues/` хранит реестр, события и артефакты `issue` для `Service Mode` и, при необходимости, для работы с концепциями.

## Источники истины

| Файл | Назначение |
|---|---|
| [`issue_registry.jsonl`](issue_registry.jsonl) | активный реестр `issue`, их статусы, типы, зависимости и владельцы |
| [`issue_events.jsonl`](issue_events.jsonl) | журнал событий создания, изменения, утверждения, блокировки, закрытия и cleanup |

## Шаблон папки `issue`

```text
Issues/{issue_id}/
├── state.md
├── reason.md
├── requirements.md
├── solution.md
├── contract.md
├── output.md
├── report.md
└── attachments/
```

Папка конкретного `issue` создаётся только после появления `issue` с reason. Пустые декоративные папки не создаются.

## Минимальное правило

Перед ответом пользователю, который меняет registry или state `issue`, агент сохраняет изменения в `GitHub`, перечитывает файлы и сообщает sync-status.
