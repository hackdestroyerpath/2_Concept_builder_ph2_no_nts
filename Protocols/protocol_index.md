# Реестр протоколов

[← К точке входа](../README.md)

## Ядро

- `Protocols/state_architecture.md`
- `Protocols/context_loading.md`
- `Protocols/mode_routing.md`
- `Protocols/response_marker.md`
- `Protocols/github_write_protocol.md`
- `Protocols/github_conflict_recovery.md`

## Issue workflow

- `Protocols/issue_lifecycle.md`
- `Protocols/question_answer.md`
- `Protocols/requirements_protocol.md`
- `Protocols/issue_execution.md`
- `Protocols/complex_and_linked_issues.md`
- `Protocols/task_flow_hardening.md`

## Templates

- `Protocols/template_validation.md`
- `Templates/concept/README.md`
- `Templates/task/README.md`

## Execution bootstrap

- `Protocols/execution_bootstrap.md`
- `Templates/README.md`

## Concept and validation

- `Protocols/concept_export.md`
- `Protocols/validation_protocol.md`

## Правило маршрутизации

Агент читает state активного режима и загружает только протоколы, нужные для текущего действия. Для создания или выбора концепции используется `execution_bootstrap`. После записи агент запускает validation protocol.

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
