# Протокол `complex issue`

[← К реестру протоколов](protocol_index.md)

## Цель

Разложить крупный `issue` на дочерние задачи так, чтобы родитель сохранял цель, return anchor и условия закрытия.

## Когда применять

- один `issue` имеет несколько независимых outputs;
- решение требует разных owners или scopes;
- выполнение одним contract создаёт высокий риск потери контекста;
- часть работ может блокироваться внешней зависимостью.

## Процесс

1. Проверить утверждённые requirements родителя.
2. Создать decomposition plan: дочерние `issue`, их цель, scope и ожидаемый output.
3. Проверить отсутствие циклов в parent-chain.
4. Создать child issues в registry со ссылкой на parent.
5. Для каждого child issue сохранить `state.md` и `reason.md`.
6. Перевести родителя в `waiting_children` или `executing` с roll-up plan.
7. После закрытия child issue добавить summary в parent `report.md`.
8. Закрыть parent только после выполнения условий roll-up.

## Roll-up summary

```yaml
child_issue_id:
status:
covered_requirements:
output_ref:
report_ref:
impact_on_parent:
remaining_risks:
next_parent_action:
```

## Ограничители

Глубина вложенности должна быть минимальной. Если decomposition не даёт ясных child outputs, issue остаётся simple и получает более строгий contract.
