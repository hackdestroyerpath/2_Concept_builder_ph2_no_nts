# Concept Builder

`Concept Builder` — production-система для управления концепциями через два режима работы, state, протоколы, `issue`, связанные MD-сети и проверяемую запись в `GitHub`.

## Быстрый вход

| Действие | Куда перейти | Что загрузить |
|---|---|---|
| Обслуживание системы | этот `README.md` | `State/service_state.md`, `Protocols/protocol_index.md` |
| Работа с концепциями | [`Concepts/README.md`](Concepts/README.md) | `State/execution_state.md`, нужную концепцию |
| Выбор протокола | [`Protocols/protocol_index.md`](Protocols/protocol_index.md) | Только протокол, нужный для текущего state/action |
| Проверка структуры | [`Registry/page_registry.jsonl`](Registry/page_registry.jsonl) | Реестр страниц и [`Registry/structure.md`](Registry/structure.md) |

## Режимы

| Режим | Объект работы | Разрешённая запись | Главный state |
|---|---|---|---|
| `Service Mode` | сама система `Concept Builder` | сервисные файлы, протоколы, инструкции, state, registry и service `issue` | [`State/service_state.md`](State/service_state.md) |
| `Execution Mode` | конкретные концепции внутри `Concepts/` | файлы выбранной концепции, её `issue`, state и output | [`State/execution_state.md`](State/execution_state.md) |

Смешение режимов запрещено. Если задача относится к другому режиму, агент фиксирует transfer-issue или останавливает запись до явного решения.

## Верхняя структура

| Путь | Назначение | Источник истины |
|---|---|---|
| [`Instructions/`](Instructions/concept_builder_service_instructions.md) | короткие инструкции проектов `ChatGPT` для ручной синхронизации | два файла инструкций |
| [`Protocols/`](Protocols/protocol_index.md) | маршрутизация и процедурные протоколы | `Protocols/protocol_index.md` |
| [`State/`](State/state_schema.md) | состояние режимов и активных объектов | `State/service_state.md`, `State/execution_state.md` |
| [`Issues/`](Issues/README.md) | registry, events и артефакты `issue` | `Issues/issue_registry.jsonl`, `Issues/issue_events.jsonl` |
| [`Concepts/`](Concepts/README.md) | концепции как связанные MD-сети | README конкретной концепции |
| [`Inbox/`](Inbox/README.md) | временное хранение входных материалов до закрытия связанных `issue` | исходный input и attachments |
| [`Registry/`](Registry/structure.md) | карта файлов и навигационный контракт | `Registry/page_registry.jsonl` |

`Scripts/` не создан. Production-скрипты допускаются только после отдельного утверждённого `issue`, контракта входов/выходов и проверки безопасности.

## Стартовое меню `Service Mode`

1. Создать новый `issue` из входного текста или файлов.
2. Взять существующий `issue` из [`Issues/issue_registry.jsonl`](Issues/issue_registry.jsonl).

Команды `1` и `2` действуют только для последнего показанного меню. В других состояниях агент обязан восстановить `dialogue_state` перед интерпретацией короткой команды.

## Правила записи

Перед любой записью агент применяет [`Protocols/github_write_protocol.md`](Protocols/github_write_protocol.md): preflight, production-only filter, запись, перечитывание, проверка ссылок/state/реестров и sync-report. Рабочие материалы реализации, checkpoint-архивы, исходное задание и промежуточные отчёты не являются production-файлами и не загружаются в этот репозиторий.

## Маркер ответа

Каждый содержательный ответ агента завершает или содержит marker из [`Protocols/response_marker_protocol.md`](Protocols/response_marker_protocol.md): `mode`, `active_object`, `active_issue`, `stage`, `loaded_context`, `persistence_status`, `next_step`, `return_anchor`.
