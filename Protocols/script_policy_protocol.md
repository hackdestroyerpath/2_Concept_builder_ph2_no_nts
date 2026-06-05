# Протокол production-скриптов

[← К реестру протоколов](protocol_index.md)

## Решение текущей реализации

`Scripts/` не создаётся в базовой реализации. Скрипт допускается только как отдельный production-артефакт после `issue`, requirements, solution, contract и проверки безопасности входов/выходов.

## Когда скрипт допустим

- действие регулярно повторяется;
- ручная проверка даёт высокий риск ошибки;
- входы и выходы можно описать контрактом;
- есть безопасный способ запуска;
- результат можно перечитать и проверить.

## Contract скрипта

```yaml
script_id:
issue_id:
purpose:
allowed_inputs:
allowed_outputs:
side_effects:
run_command:
verification:
owner:
status: proposed | approved | active | retired
```

## Правила

1. Скрипт не создаётся как удобная заготовка без `issue`.
2. Скрипт не пишет за пределами approved paths.
3. Рядом со скриптом должен быть README с назначением, входами, выходами и проверкой.
4. Любой скрипт проходит navigation validation и registry update.

## Выход

Решение: `no_scripts_required`, `script_issue_needed` или `script_approved`.
