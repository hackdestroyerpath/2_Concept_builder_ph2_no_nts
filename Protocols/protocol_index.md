# Реестр протоколов

[← К точке входа](../README.md)

## Ядро

- `Protocols/state_architecture.md` — архитектура состояния.
- `Protocols/context_loading.md` — загрузка контекста.
- `Protocols/mode_routing.md` — маршрутизация режимов.
- `Protocols/response_marker.md` — маркер ответа.
- `Protocols/github_write_protocol.md` — синхронизация production-файлов с репозиторием.

## Следующие протоколы

- `Protocols/issue_lifecycle.md`
- `Protocols/question_answer.md`
- `Protocols/requirements_protocol.md`
- `Protocols/issue_execution.md`
- `Protocols/complex_and_linked_issues.md`
- `Protocols/concept_export.md`
- `Protocols/validation_protocol.md`

## Правило маршрутизации

Агент читает state активного режима, затем загружает только протоколы, нужные для текущего действия. Если нужный протокол отсутствует, агент фиксирует блокировку или заводит сервисное `issue`.

## Минимальный маркер ответа

```text
mode:
active_object:
active_issue:
stage:
loaded_context:
persistence_status:
next_step:
return_anchor:
```
