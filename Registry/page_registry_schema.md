# Схема реестра страниц

[← Структура](structure.md) | [Реестр страниц](page_registry.jsonl) | [Навигационная проверка](../Validation/navigation_check.md)

## Назначение

`Registry/page_registry.jsonl` — машинная карта production-файлов `Concept Builder`. Реестр является navigation contract: по нему проверяются достижимость страниц, владельцы, backlinks, источники истины, локальные registry и отсутствие orphan/debris файлов.

## Формат JSONL

Каждая строка — один JSON-объект. Порядок строк повторяет утверждённое production-дерево: root, top-level routes, вложенные узлы, validation.

```json
{"path":"README.md","title":"Точка входа Concept Builder","type":"markdown","owner":"Service Mode","parent":null,"children":["Protocols/protocol_index.md"],"cross_links":["Validation/final_check.md"],"backlinks":[],"description":"Главная карта системы и маршрутов.","source_of_truth":"production","navigation_status":"reachable"}
```

## Обязательные поля

| Поле | Тип | Смысл | Проверка P2-002 |
|---|---|---|---|
| `path` | string | Путь production-файла от корня репозитория или локальный путь внутри local registry. | существует в утверждённом дереве или описан как удалённое исключение вне active registry |
| `title` | string | Человекочитаемое русское название страницы; technical identifiers допускаются. | не пустое, не является `OK`/`Ready`/`closed` |
| `type` | string | Класс файла: `markdown`, `jsonl`, `template`, `state`, `validation`, `issue_artifact`. | соответствует роли файла |
| `owner` | string | Владелец: `Service Mode`, `Execution Mode` или конкретный production-owner. | согласован с root README и state |
| `parent` | string/null | Родительская reachable-страница. | `null` только у `README.md`; остальные родители должны существовать |
| `children` | array | Дочерние страницы, достижимые из текущей страницы. | каждый child должен иметь registry entry или documented exception |
| `cross_links` | array | Функциональные ссылки вне прямого дерева. | ссылки используются для протоколов, validation, state и issue anchors |
| `backlinks` | array | Страницы, которые должны ссылаться назад или входить в маршрут. | проверяются по `Validation/navigation_check.md` |
| `description` | string | Роль файла в системе. | описывает production-назначение, а не статус-ярлык |
| `source_of_truth` | string | Источник актуальности: `production`, `state`, `issue_registry`, `validation`, `template_registry`, `concept_registry`. | согласован с владельцем и назначением |
| `navigation_status` | string | `reachable`, `local_reachable`, `registered_exception`, `removed_with_reason`, `blocked`. | активные production-файлы должны быть `reachable` или `local_reachable` |

## Правила для глобального реестра

1. Глобальный `Registry/page_registry.jsonl` покрывает все активные production-файлы из `Registry/structure.md`.
2. Любая MD-страница должна быть достижима от `README.md`, mode entry или local concept/template entry.
3. `children`, `cross_links` и `backlinks` не заменяют actual links in files; они задают проверяемый контракт для readback.
4. `source_of_truth` фиксирует, где находится authority для файла: state, issue registry, validation, template registry или concept registry.
5. Строки global registry не должны регистрировать patch-handoff, Phase 1 audit, prompt-ы, checkpoint-и или исходный handoff-архив.

## Правила для local registry

| Local registry | Scope | Parent в global registry | Статус |
|---|---|---|---|
| `Concepts/smoke/page_registry.jsonl` | локальная сеть smoke fixture | `Concepts/smoke/README.md` | `local_reachable` для child pages |
| `Templates/concept/page_registry.jsonl` | шаблон новой концепции | `Templates/concept/README.md` | `local_reachable` для child templates |
| `Templates/task/page_registry.jsonl` | шаблон управляемой задачи | `Templates/task/README.md` | `local_reachable` для child templates |

В local registry поле `path` пишется относительно локального root. Backlink `README.md` означает локальный README, а `../../...` используется только для выхода к global routes.

## Исключения и debris

`Plans/`, `Closure/`, `Issues/cb89.md`, `Concepts/smoke/o2.md`, patch-handoff, Phase 1 audit, prompt-ы, checkpoint-и и исходный handoff-архив не имеют активных production-записей. Если путь удалён с причиной, причина фиксируется в `Registry/structure.md`, `Validation/final_check.md`, `Validation/sync_report.md` и `Issues/issue_events.jsonl`.

## Проверки P2-002

1. Все production MD/JSONL/state/template/validation/issue files имеют registry entry.
2. Каждый parent/child/cross-link/backlink указывает существующий active production path или documented external/local route.
3. Local registries не являются path-only: каждая строка содержит owner, parent, backlinks, source_of_truth и navigation_status.
4. `Templates/task/README.md` содержит clickable routes к child artifacts.
5. Финальный статус не объявляется до P2-010; P2-002 только фиксирует navigation contract и readback evidence.
