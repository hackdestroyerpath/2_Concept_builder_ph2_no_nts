# Template validation

[← Реестр протоколов](protocol_index.md) | [Templates](../Templates/README.md)

## Purpose

Проверка production-шаблонов перед использованием.

## Scope

- `Templates/concept/`
- `Templates/task/`
- `Registry/page_registry.jsonl`
- `Registry/page_registry_schema.md`

## Concept checks

- обязательные файлы есть;
- локальный `page_registry.jsonl` валиден;
- внутренние ссылки рабочие;
- placeholder-ы известны;
- `concept_state.md` совместим с `Execution Mode`;
- `export.md` совместим с validation.

## Task checks

- обязательные файлы есть;
- роли артефактов определены;
- QA, requirements, solution, contract и report присутствуют;
- linked files описаны;
- шаблон совместим с lifecycle задачи.

## Result

```text
template_valid
template_valid_with_notes
template_invalid
not_checked
```

Результат проверки фиксируется в отчёте агента, event log и state при необходимости.
