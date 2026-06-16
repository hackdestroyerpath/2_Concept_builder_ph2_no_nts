# Проверка навигации

[← Финальная проверка](final_check.md) | [Реестр](../Registry/page_registry.jsonl) | [Структура](../Registry/structure.md)

## Область

```text
readback_ref: p2r4_branch_and_main_readback
checked_area: README; Protocols; State; Issues; Concepts/smoke; Templates; Registry; Validation
status: passed_after_readback
failed_checks: []
```

## Проверки

| Проверка | Доказательство | Статус |
|---|---|---|
| Корневая точка входа ведёт в рабочие зоны | `README.md` содержит ссылки на все зоны верхнего уровня | passed_with_evidence |
| Глобальный реестр содержит владельца, обратные ссылки и источник истины | `Registry/page_registry.jsonl` использует расширенные строки схемы | passed_with_evidence |
| Схема описывает обязательные поля | `Registry/page_registry_schema.md` | passed_with_evidence |
| Карта структуры совпадает с целевым деревом | `Registry/structure.md` | passed_with_evidence |
| Задачи имеют активную запись и артефакты по каждой задаче | `Issues/README.md`, `Issues/CB-P2`, `CB-002`…`CB-009` | passed_with_evidence |
| Маршруты записи и восстановления достижимы | `README.md` → протоколы записи и восстановления | passed_with_evidence |
| Фикстура smoke достижима | `Concepts/README.md` → `Concepts/smoke/README.md` | passed_with_evidence |
| Локальный реестр smoke не ограничен только путями | `Concepts/smoke/page_registry.jsonl` | passed_with_evidence |
| Локальный реестр задач не ограничен только путями | `Templates/task/page_registry.jsonl` | passed_with_evidence |
| Шаблон локального реестра концепции не ограничен только путями | `Templates/concept/page_registry.jsonl` | passed_with_evidence |
| Устаревшие активные зоны отсутствуют в реестре | `Plans/`, `Closure/`, `Issues/cb89.md`, `Concepts/smoke/o2.md` исключены из активного реестра | passed_with_evidence |

## Ожидаемо отсутствующие пути

| Путь | Ожидаемый результат | Причина | Доказательство |
|---|---|---|---|
| `Issues/cb89.md` | 404 / absent | смешанный мусор | проверки отсутствующих путей в `Validation/sync_report.md` |
| `Plans/cb008.md` | 404 / absent | перенесён в артефакты валидации и задачи | проверки отсутствующих путей в `Validation/sync_report.md` |
| `Closure/status.md` | 404 / absent | закрытие без доказательств заменено проверяемыми доказательствами | проверки отсутствующих путей в `Validation/sync_report.md` |
| `Concepts/smoke/o2.md` | 404 / absent | осиротевшая заглушка | проверки отсутствующих путей в `Validation/sync_report.md` |
