# Пробный прогон CB-008

[← Финальная проверка](final_check.md) | [План закрытия](cb008_closure_plan.md) | [Issue CB-008](../Issues/CB-008/README.md)

## Цель проверки

`CB-008` проверяет маршрут задачи в `Service Mode` после усиления Phase 2. Пробный прогон не создаёт служебные черновики и не добавляет внешние материалы проверки в production repo.

## Сценарии

| Сценарий | Доказательство | Статус |
|---|---|---|
| Маршрут задачи `Service Mode` | issue lifecycle, task flow, task template | passed_with_evidence |
| Маршрут QA и причины пропуска | question answer protocol, QA template | passed_with_evidence |
| Контроль требований | requirements protocol, requirements template | passed_with_evidence |
| Цепочка решения, контракта и отчёта | solution, contract, report templates | passed_with_evidence |
| Маршрут связанных issue | complex issue protocol, linked files template | passed_with_evidence |
| Маршрут записи и восстановления | write, conflict, rollback protocols | passed_with_evidence |
| Связь registry и event log | issue registry, event log, page registry | passed_with_evidence |

## Примечание

Статус пробного прогона связан с branch readback в `Validation/sync_report.md` и финальными доказательствами в `Validation/final_check.md`.