# Протокол `solution` и `contract`

[← К реестру протоколов](protocol_index.md)

## Цель

Сформировать проверяемый план решения и contract выполнения после утверждения requirements.

## Входы

- `requirements.md` со статусом `approved`;
- `reason.md`;
- QA, если проводился;
- зависимости issue;
- mode scope и allowed write scope.

## `solution`

`solution.md` описывает:

- краткий подход;
- альтернативы и почему они не выбраны;
- затрагиваемые production-файлы;
- порядок действий;
- риски и ограничения;
- критерии готовности.

## `contract`

`contract.md` фиксирует:

```yaml
contract_id: CTR-...
issue_id:
requirements_ref:
allowed_actions:
allowed_paths:
expected_outputs:
verification_steps:
dependencies:
approval_status: proposed | approved | changed
```

## Процесс

1. Проверить, что requirements утверждены.
2. Создать `solution.md`.
3. Создать `contract.md`.
4. Сохранить оба файла до ответа.
5. Показать пользователю краткий план, paths и критерии проверки.
6. После утверждения перевести issue в `ready_for_execution`.

## Выход

Сохранённые `solution.md` и `contract.md`, event, обновлённый issue state и marker с `dialogue_state: awaiting_solution_decision` или `ready_for_execution`.
