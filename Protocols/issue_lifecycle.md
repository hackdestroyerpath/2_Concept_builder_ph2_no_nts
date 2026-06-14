# Жизненный цикл issue

[← Реестр протоколов](protocol_index.md) | [State](../State/service_state.md) | [Issues](../Issues/README.md) | [Task flow hardening](task_flow_hardening.md)

## Назначение

`Issue` — единица управляемой production-работы. Issue должен иметь reason, provenance, approval/skip decision, dependencies, cleanup status, evidence anchors and return-anchor.

## Статусы

| Статус | Значение |
|---|---|
| `proposed` | задача зафиксирована, но scope ещё не утверждён |
| `approval_requested` | требуется explicit approval |
| `question_answer` | требуется уточнение или skip reason |
| `requirements` | собираются проверяемые требования |
| `approved` | requirements/contract approved |
| `executing` | выполняется запись или анализ |
| `validation` | результат записан, идёт readback/evidence gate |
| `fixed_with_evidence` | закрыто с named evidence |
| `reconstructed_with_evidence` | legacy baseline восстановлен из repo-фактов |
| `cleanup_removed` | path/issue удалён с reason |
| `blocked` | продолжение остановлено с причиной |
| `rejected` | задача отклонена |

## Обязательные поля registry row

```json
{"issue_id":"CB-000","type":"service","mode":"Service Mode","status":"proposed","priority":"normal","reason":"","provenance":"","approval":"","dependencies":[],"cleanup":"retain","current_refs":[],"return_anchor":""}
```

## Переходы

```text
proposed -> approval_requested -> requirements -> approved -> executing -> validation -> fixed_with_evidence
proposed -> question_answer -> requirements
any -> blocked
any -> rejected
blocked -> proposed only with new reason/event
legacy -> reconstructed_with_evidence only when repo evidence exists
```

## События

Каждое значимое изменение пишется в `Issues/issue_events.jsonl`: creation, status change, approval, discussion, rejection, write, cleanup, validation, rollback, closure.

## Закрытие

`fixed_with_evidence` разрешён только после записи результата, обновления registry/state/events, контрольного чтения из `GitHub`, validation report и explicit remaining risks. Одного слова `done` недостаточно.
