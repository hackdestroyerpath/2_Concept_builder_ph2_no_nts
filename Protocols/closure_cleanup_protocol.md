# Протокол закрытия и cleanup `issue`

[← К реестру протоколов](protocol_index.md) | [Issues](../Issues/README.md)

## Цель

Закрыть выполненный `issue`, свернуть результат наверх и очистить временные материалы без потери provenance.

## Условия закрытия

- `output.md` создан;
- `report.md` показывает покрытие contract;
- блокирующие linked-связи решены или явно исключены с reason;
- parent issue получил roll-up, если он есть;
- registry и events перечитаны после записи.

## Процесс

1. Загрузить `state.md`, `output.md`, `report.md`, registry и events.
2. Сверить report с contract.
3. Обновить status: `completed` или `closed`.
4. Если есть parent, записать roll-up summary в parent context.
5. Пометить временные attachments и input как cleanup candidates.
6. Сохранить provenance: input refs, decision refs, output refs и report refs.
7. Обновить registry и events.
8. Предложить следующий `issue` по приоритету.

## Cleanup policy

Отклонённые и закрытые `issue` не удаляются механически. Сначала проверяются зависимости, ссылки из requirements/output/report и parent-chain. После проверки можно архивировать или сжать подробности в summary.

## Выход

Закрытый `issue`, roll-up, список cleanup candidates и marker с return anchor.
