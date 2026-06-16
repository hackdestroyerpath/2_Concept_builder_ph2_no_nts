# Шаблоны

[← Точка входа](../README.md) | [Шаблон концепции](concept/README.md) | [Шаблон задачи](task/README.md) | [Проверка шаблонов](../Protocols/template_validation.md)

`Templates/` хранит рабочие шаблоны системы. Шаблон не является готовым объектом работы; он задаёт обязательную структуру, поля и проверочные шлюзы для новых концепций и управляемых задач.

## Управление

| Поле | Значение |
|---|---|
| Владелец | `Service Mode` |
| Источник истины | локальные `README.md` и реестры внутри `Templates/concept/` и `Templates/task/` |
| Глобальный маршрут | `README.md` → `Templates/README.md` |
| Проверка | [`Protocols/template_validation.md`](../Protocols/template_validation.md), [`Validation/final_check.md`](../Validation/final_check.md) |

## Шаблоны

| Шаблон | Назначение | Владелец | Локальный реестр |
|---|---|---|---|
| [`concept/`](concept/README.md) | структура новой концепции: состояние, локальный реестр, назначение, требования, операционная модель, процесс, результат, экспорт | `Execution Mode` под управлением `Service Mode` | [`concept/page_registry.jsonl`](concept/page_registry.jsonl) |
| [`task/`](task/README.md) | артефакты управляемой задачи: состояние, вопросы/ответы, требования, решение, контракт, отчёт, связанные файлы | `Service Mode` | [`task/page_registry.jsonl`](task/page_registry.jsonl) |

## Правила

1. Значения-заглушки заменяются при создании объекта.
2. Шаблоны меняются только через `Service Mode` и активную задачу.
3. Дочерние файлы должны быть доступны ссылками из `README.md` и локального реестра.
4. Проверка выполняется через `Protocols/template_validation.md` и фиксируется в `Validation/`.
5. Prompt-ы, архивы передачи и контрольные архивы не являются рабочим содержимым шаблона.