# `Scripts`

[← К главной точке входа](../README.md)

`Scripts/` содержит утверждённые production-скрипты `Concept Builder`. Скрипты не являются черновиками и не появляются ради удобства, потому что удобство без контракта быстро превращается в техдолг с улыбкой.

## Правило допуска

Скрипт создаётся только после отдельного `issue`, утверждённых requirements, solution, contract и проверки безопасности входов/выходов. Общая политика описана в [`Protocols/script_policy_protocol.md`](../Protocols/script_policy_protocol.md).

## Доступные скрипты

| Скрипт | Назначение | Side effects |
|---|---|---|
| [`validation/validate_repository.py`](validation/validate_repository.py) | Проверка production-навигации, registry, JSONL, state markers и запрета временных артефактов | read-only |

## Запуск

```bash
python3 Scripts/validation/validate_repository.py --root .
```

Выход `validation_status: valid` означает, что обязательные production-инварианты пройдены. Ошибки возвращают exit code `1`.
