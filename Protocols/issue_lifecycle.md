# Жизненный цикл issue

[← Реестр протоколов](protocol_index.md) | [State](../State/service_state.md) | [Task flow hardening](task_flow_hardening.md)

## Назначение

Протокол описывает путь задачи от появления до закрытия. `issue` — единица управляемой работы.

## Статусы

| Статус | Значение |
|---|---|
| `draft` | Задача зафиксирована, но ещё не готова к работе. |
| `approval_requested` | Требуется утверждение перед записью. |
| `question_answer` | Требуется уточнение. |
| `requirements` | Собираются и проверяются требования. |
| `ready` | Есть достаточно данных для решения. |
| `in_progress` | Задача выполняется. |
| `review` | Результат записан и ожидает проверки. |
| `done` | Задача закрыта и синхронизирована. |
| `rejected` | Задача отклонена. |
| `blocked` | Продолжение остановлено с причиной. |

## Обязательные поля записи

```json
{"issue_id":"CB-000","mode":"Service Mode","status":"draft","title":"...","stage":"..."}
```

Минимальные поля: `issue_id`, `mode`, `status`, `title`, `stage`.

## Переходы

```text
draft -> approval_requested -> requirements -> ready -> in_progress -> review -> done
draft -> question_answer -> requirements
any -> blocked
any -> rejected
blocked -> draft
```

## События

Каждое значимое изменение пишется в `Issues/issue_events.jsonl`: создание, смена статуса, approval, discussion, rejection, запись решения, cleanup, блокировка, закрытие.

## Правила закрытия

`done` разрешён только после записи результата, обновления связанных реестров, контрольного чтения из `GitHub` и обновления state.
