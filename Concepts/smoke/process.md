# Процесс

[← Проверочный пример](README.md) | [Операционная модель](operating_model.md) | [Результат](output.md)

## Сценарий пробного прогона

1. Загрузить `State/execution_state.md` и выбрать `Concepts/smoke` как активный объект.
2. Проверить `README.md`, `concept_state.md`, `structure.md`, `page_registry.jsonl`.
3. Проверить страницы `purpose`, `requirements`, `operating_model`, `process`, `output`, `export`.
4. Проверить, что локальный реестр содержит владельца, обратные ссылки и источник истины.
5. Проверить отсутствие бесхозных, лишних или заглушечных страниц.
6. Сформировать сопоставление результата и манифест экспорта.
7. Перед закрытием перечитать файлы из `GitHub` и записать результат в `Validation/final_check.md`.

## Проверочные крючки

```text
readback_paths: Concepts/smoke/README.md; Concepts/smoke/page_registry.jsonl; Concepts/smoke/output.md; Concepts/smoke/export.md
expected_absent_paths: Concepts/smoke/o2.md; Concepts/smoke/output.txt; Concepts/smoke/e.txt
linked_issue: CB-009
```

Кодовый блок сохраняет технические поля и пути. Читаемая проверка: перечитать рабочие страницы `smoke`, подтвердить отсутствие лишних путей и связь с `CB-009`.