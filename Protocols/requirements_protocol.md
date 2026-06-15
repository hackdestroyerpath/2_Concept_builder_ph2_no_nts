# Requirements protocol

[← Реестр протоколов](protocol_index.md) | [Жизненный цикл issue](issue_lifecycle.md) | [Question Answer](question_answer.md) | [Issue execution](issue_execution.md)

## Назначение

Протокол описывает сбор и проверку требований перед выполнением `issue`. Требования нужны, чтобы результат проверялся фактами, а не восторженным “ну вроде похоже”.

## Минимальная запись требования

```text
requirement_id:
issue_id:
mode:
active_object:
source:
reason:
statement:
linked_questions:
linked_inputs:
linked_issues:
acceptance_criteria:
constraints:
risks:
approval_status: proposed | approved_with_scope | rejected | skipped_with_reason | blocked
approval_source:
recorded_at:
return_anchor:
```

## Requirement tree

Requirement tree должен сохранять происхождение каждого требования:

| Поле | Назначение |
|---|---|
| `requirement_id` | стабильный ID, пригодный для отчёта и matrix |
| `source` | user, state, registry, event, protocol, validation finding |
| `reason` | почему требование существует |
| `linked_questions` | QA records или skip reasons |
| `linked_inputs` | входные файлы, prompts, artifacts, repo paths |
| `linked_issues` | parent/child/dependency issue IDs |
| `acceptance_criteria` | проверяемое условие, не статусный ярлык |
| `approval_status` | состояние scope decision |

## Правила

1. Требование должно быть проверяемым по repo evidence, event log, state или validation file.
2. Если требование двусмысленно, задача переходит в `question_answer`.
3. Если задача маленькая и безопасная, отдельный QA artifact можно пропустить только с `skipped_with_reason`.
4. Production write требует перечисления target paths и validation plan.
5. Execution запрещён, пока requirements не имеют `approved_with_scope` или documented safe skip.
6. Acceptance criteria должны описывать наблюдаемый факт: readback, JSONL validity, link reachability, state/event coupling.

## Approval block

```text
approval_status:
approved_by:
approved_at:
approval_source:
blocking_questions:
scope_exclusions:
validation_plan:
```

## Выход

После проверки требований `issue` получает `requirements_scoped` или `blocked`. Если scope достаточно определён, следующий протокол — `issue_execution`.
