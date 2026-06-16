# План закрытия CB-008

[← Dry run](cb008_dry_run.md) | [Финальная проверка](final_check.md) | [Issue CB-008](../Issues/CB-008/README.md)

## Область

| Зона | Доказательство закрытия |
|---|---|
| Маршрут Service Mode | обновлены issue lifecycle, task flow и события registry |
| Шаблон задачи | обновлены локальный task registry и artifact gates |
| Восстановление GitHub | обновлены протоколы write, conflict и rollback |
| Записи событий | `service-event-000008`…`service-event-000012` фиксируют доказательства Phase 2 patch |
| Page registry | глобальный registry перестроен с owner/backlinks/source_of_truth |

## Последовательность закрытия

1. Заменить assertion-only dry-run result на сценарии с evidence.
2. Перенести действительную информацию из `Plans/cb008.md` в `Issues/CB-008/README.md` и этот файл.
3. Удалить `Plans/cb008.md` после переноса.
4. Проверить readback branch и обновить `Validation/sync_report.md`.
5. Закрывать через `Validation/final_check.md` только после того, как matrix `D-001`…`D-063` не содержит blocker.

## Статус

`closure_ready_after_readback`: этот plan действителен только вместе с финальным readback и проверкой PR/base.
