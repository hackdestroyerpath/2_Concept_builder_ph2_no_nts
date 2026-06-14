# Templates

[← Точка входа](../README.md) | [Concept template](concept/README.md) | [Task template](task/README.md) | [Template validation](../Protocols/template_validation.md)

`Templates/` хранит production-шаблоны системы. Шаблон не является готовым объектом работы; он задаёт обязательную структуру, поля и validation gates для новых концепций и управляемых задач.

## Управление

| Поле | Значение |
|---|---|
| Владелец | `Service Mode` |
| Источник истины | локальные README/registry внутри `Templates/concept/` и `Templates/task/` |
| Глобальный маршрут | `README.md` → `Templates/README.md` |
| Проверка | [`Protocols/template_validation.md`](../Protocols/template_validation.md), [`Validation/final_check.md`](../Validation/final_check.md) |

## Шаблоны

| Шаблон | Назначение | Owner | Registry |
|---|---|---|---|
| [`concept/`](concept/README.md) | Структура новой концепции: state, local registry, purpose, requirements, operating model, process, output, export. | `Execution Mode` template owner under `Service Mode` governance | [`concept/page_registry.jsonl`](concept/page_registry.jsonl) |
| [`task/`](task/README.md) | Артефакты управляемой задачи: state, QA, requirements, solution, contract, report, linked files. | `Service Mode` | [`task/page_registry.jsonl`](task/page_registry.jsonl) |

## Правила

1. Значения-заглушки заменяются при создании объекта.
2. Шаблоны меняются только через `Service Mode` и активный `issue`.
3. Дочерние файлы должны быть доступны ссылками из README и локального registry.
4. Проверка выполняется через `Protocols/template_validation.md` и фиксируется в `Validation/`.
5. Prompt-ы, handoff-архивы и checkpoint-и не являются template production content.
