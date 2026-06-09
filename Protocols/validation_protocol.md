# Validation protocol

[← Реестр протоколов](protocol_index.md) | [GitHub write protocol](github_write_protocol.md) | [Issue execution](issue_execution.md)

## Назначение

Протокол задаёт обязательную проверку production-состояния после изменений. Validation нужен, чтобы `synced` означал проверенную запись, а не оптимистичную надпись на развалинах.

## Когда запускать

Validation запускается после каждого этапа, который меняет production-файлы, state, реестры, `issue` или export.

## Минимальные проверки

```text
changed_paths_present:
github_readback_ok:
jsonl_valid:
markdown_links_ok:
state_marker_match:
registry_updated:
issue_events_updated:
acceptance_criteria_met:
```

## Проверка GitHub

1. Перечитать каждый изменённый файл из `GitHub`.
2. Проверить наличие ключевых строк.
3. Проверить, что `sha` изменился для обновлённых файлов.
4. Если перечитать файл нельзя, статус не может быть `synced`.

## Проверка JSONL

Каждая строка JSONL-файла должна быть отдельным валидным JSON-объектом. Пустой JSONL-файл допустим только для явно пустого реестра.

## Проверка ссылок

Markdown-ссылки на production-файлы должны вести на существующие файлы или на явно запланированные файлы, отмеченные в `Protocols/protocol_index.md`.

## Итоговые статусы

| Статус | Значение |
|---|---|
| `passed` | Проверки пройдены. |
| `passed_with_notes` | Проверки пройдены, есть неблокирующие замечания. |
| `failed` | Есть блокирующая ошибка. |
| `not_run` | Проверка не запускалась. |

## Отчёт validation

```text
validation_status:
checked_paths:
failed_checks:
notes:
persistence_status:
```

Если validation failed, агент не закрывает `issue` как `done`.
