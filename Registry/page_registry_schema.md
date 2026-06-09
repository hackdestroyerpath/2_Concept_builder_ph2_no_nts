# Page registry schema

[← Структура](structure.md) | [Реестр страниц](page_registry.jsonl)

## Назначение

`Registry/page_registry.jsonl` хранит машинную карту production-файлов `Concept Builder`.

## Минимальная запись

```json
{"path":"README.md","kind":"md","role":"entry","parent":null}
```

## Поля

| Поле | Обязательность | Смысл |
|---|---|---|
| `path` | да | Путь production-файла от корня репозитория. |
| `kind` | да | Тип: `md`, `jsonl`, `template`. |
| `role` | да | Роль файла в системе. |
| `parent` | да | Родительская страница или `null`. |

## Правила

1. Одна строка — один JSON-объект.
2. `path` должен указывать на существующий production-файл или шаблон.
3. Реестр обновляется вместе с созданием или удалением production-файла.
4. Проверка выполняется через `Protocols/validation_protocol.md`.
