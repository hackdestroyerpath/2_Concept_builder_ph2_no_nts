# Issue execution

[← Реестр протоколов](protocol_index.md) | [Жизненный цикл issue](issue_lifecycle.md) | [Requirements protocol](requirements_protocol.md) | [GitHub write protocol](github_write_protocol.md)

## Назначение

Протокол описывает выполнение `issue` после того, как requirements и contract дают проверяемый scope. Execution не начинается из ощущения “и так понятно”; этот вид спорта уже слишком дорого обходился production-файлам.

## Вход

```text
issue_id:
mode:
active_object:
requirements:
qa_or_skip_reason:
solution_summary:
contract_id:
approved_contract:
allowed_scope:
target_paths:
acceptance_criteria:
validation_plan:
rollback_plan:
return_anchor:
```

## Предварительные gates

| Gate | Требование | Блокировка |
|---|---|---|
| Requirements | `approved_with_scope` или `skipped_with_reason` | unresolved question |
| Solution | changed paths, risks and alternatives recorded | unsafe ambiguity |
| Contract | target paths, operation, validation plan, rollback plan | contract absent |
| Linked files | dependencies known and no unresolved cycle | dependency blocker |
| Write package | pre-sha and classifier recorded | stale or unsafe write |

## Этапы выполнения

1. Перевести `issue` в `in_progress` через registry/state/event coupling.
2. Сформировать solution: подход, target paths, state/registry/event/validation effects.
3. Сформировать contract: exact paths, operation, validation plan, rollback plan.
4. Выполнить только pre-registered writes в разрешённой области.
5. Перечитать изменённые файлы из `GitHub`.
6. Проверить acceptance criteria по evidence, а не по словам статуса.
7. Обновить реестры, журнал событий, state и sync-report.
8. Перевести `issue` в `review_required`, `fixed_with_evidence` или `blocked`.

## Report

Отчёт по выполнению должен включать:

```text
issue_id:
contract_id:
changed_paths:
commit_sha_or_branch_head:
readback_ref:
validation_result:
registry_result:
state_result:
event_result:
open_risks:
next_step:
return_anchor:
```

## Блокировки

Если запись, readback, registry/state/event coupling или validation не выполнены, `issue` получает `blocked` или `review_required`, но не финальный статус.
