# Execution Mode bootstrap

[← Реестр протоколов](protocol_index.md) | [Execution state](../State/execution_state.md) | [Concepts](../Concepts/README.md) | [Concept export](concept_export.md)

## Назначение

`execution_bootstrap` описывает безопасный вход в `Execution Mode`: выбор существующей концепции или создание новой концепции из production-шаблона. Этот протокол не меняет service-governance файлы; он только выбирает concept scope и подготавливает следующий execution route.

## Когда применяется

`execution_bootstrap` применяется, когда пользователь просит создать, выбрать или продолжить конкретную концепцию внутри `Concepts/`.

## Входные данные

```text
command:
concept_id:
concept_title:
mode:
active_issue:
source_materials:
acceptance_criteria:
```

`concept_id` должен быть коротким техническим идентификатором без пробелов. Название концепции хранится отдельно как `concept_title`.

## Required context

| Context | Purpose | Blocking condition |
|---|---|---|
| `README.md` | root route and mode selection | root route missing |
| `State/execution_state.md` | active execution object, scopes and marker fields | missing or non-canonical state |
| `Concepts/README.md` | concept inventory and smoke fixture policy | selected concept not reachable |
| `Protocols/protocol_index.md` | route matrix and next protocol | missing route card |
| `Protocols/mode_routing.md` | Service/Execution boundary check | mixed scope unresolved |
| `Templates/concept/README.md` | creation template for new concept | template route missing for create action |
| `Concepts/<concept_id>/page_registry.jsonl` | local registry for existing concept | missing local registry for continue action |

## Route matrix

| Scenario | Preconditions | Output | Next protocol |
|---|---|---|---|
| Выбрать существующую концепцию | folder exists, local registry exists, active issue known or not required for read-only | `active_object=Concepts/<concept_id>` and bounded read/write scope | `concept_export` or concept-specific work |
| Создать новую концепцию | valid concept_id, issue/provenance exists, template route exists, target folder absent | new concept folder plan and write package | `github_write_protocol` |
| Продолжить concept issue | linked issue row and event trace exist | resumed concept scope and return anchor | target concept task protocol |
| Проверить smoke fixture | `Concepts/smoke` registered as validation fixture | read-only fixture evidence | `validation_protocol` or P2-009 smoke repair |
| Mixed service/execution request | service target and concept target both present | transfer route or blocked split | `mode_routing` |

## Создание концепции

1. Проверить, что задача относится к `Execution Mode`.
2. Создать или подтвердить `issue` на создание концепции.
3. Проверить `concept_id`, чтобы не перезаписать существующую папку.
4. Скопировать структуру из `Templates/concept/` в `Concepts/<concept_id>/`.
5. Заполнить `README.md`, `structure.md`, `page_registry.jsonl` и стартовые страницы концепции.
6. Обновить `State/execution_state.md`, глобальный `Registry/page_registry.jsonl` и журналы `Issues/`.
7. Запустить `Protocols/validation_protocol.md`.

## Выбор существующей концепции

1. Найти папку `Concepts/<concept_id>/`.
2. Прочитать `Concepts/<concept_id>/README.md` и локальный `page_registry.jsonl`.
3. Проверить backlinks, output/export route и linked issue, если запись планируется.
4. Обновить `State/execution_state.md` только в рамках разрешённого Execution scope или approved service repair.
5. Вернуть маркер ответа с выбранным `active_object`.

## Protocol card

| Поле | Значение |
|---|---|
| Owner | `Execution Mode` |
| Trigger | create/select/continue concept request, smoke fixture check, export readiness request |
| Inputs | command, concept_id, concept_title, active issue, source materials, acceptance criteria |
| Required context | execution state, Concepts entry, protocol index, mode routing, local registry or concept template |
| Outputs | selected concept scope, creation plan, blocked reason or next execution protocol |
| Write scope | selected `Concepts/<concept_id>/` and linked execution issue; service files only through transfer |
| Next protocol | `concept_export`, concept task protocol, `github_write_protocol`, or `validation_protocol` |
| Blocking conditions | missing concept_id, missing local registry, target folder conflict, absent issue for write, mixed service scope |

## Блокировки

Концепция не создаётся и не выбирается для записи, если отсутствует `concept_id`, неясен режим, конфликтует путь, нет `issue` для write-action или нарушена область записи. При конфликте scope агент фиксирует transfer route, а не пишет service и execution файлы одним пакетом.

## P2-004 verification notes

P2-004 связывает `execution_bootstrap` с global protocol index, context loading, mode routing and concept export. Детальный smoke/export dry-run остаётся задачей P2-009/P2-010.