# Repository validation

[← К Scripts](../README.md)

## Назначение

`validate_repository.py` проверяет production-инварианты `Concept Builder` без записи файлов и без сетевых вызовов.

## Входы

| Input | Значение |
|---|---|
| `--root` | Корень репозитория. По умолчанию `.` |
| Файлы репозитория | Только локальное чтение |

## Выходы

| Output | Значение |
|---|---|
| `validation_status: valid` | Fatal violations не найдены |
| `validation_status: failed` | Найдены ошибки, exit code `1` |
| `WARNINGS` | Нефатальные замечания, например отсутствие явного parent marker |

## Проверки

- обязательные production-пути существуют;
- все `*.jsonl` парсятся построчно;
- Markdown-ссылки не битые и не выходят из репозитория;
- `Registry/page_registry.jsonl` указывает на существующие файлы;
- `Protocols/protocol_registry.jsonl` указывает на существующие протоколы;
- `State/service_state.md` и `State/execution_state.md` содержат ключевые markers;
- checkpoint, handoff, implementation archive и похожие временные артефакты не попали в production.

## Запуск локально

```bash
python3 Scripts/validation/validate_repository.py --root .
```

## GitHub Actions

Workflow: [`../../.github/workflows/concept-builder-validation.yml`](../../.github/workflows/concept-builder-validation.yml).
