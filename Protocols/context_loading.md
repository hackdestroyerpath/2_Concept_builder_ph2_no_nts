# Загрузка контекста

[← Реестр протоколов](protocol_index.md) | [Архитектура состояния](state_architecture.md) | [Маршрутизация режимов](mode_routing.md) | [Маркер ответа](response_marker.md)

## Назначение

Протокол задаёт исполнимый порядок чтения файлов перед действием агента. Цель — загрузить достаточный контекст для текущего bounded step, не читать весь репозиторий и не смешивать `Service Mode` с `Execution Mode`.

## Базовый порядок

1. Прочитать `README.md` как глобальную карту маршрутов.
2. Прочитать state активного режима.
3. Прочитать `Protocols/protocol_index.md`.
4. Применить `Protocols/mode_routing.md`, если команда или target path могут относиться к другому режиму.
5. Прочитать только протоколы, нужные текущему действию.
6. Прочитать active issue, registry/events и validation anchors, если действие меняет production-файлы.
7. После write перечитать изменённые файлы из `GitHub` и зафиксировать evidence в `Validation/sync_report.md`.

## Уровни контекста

| Уровень | Загружать | Примеры | Запрет |
|---|---|---|---|
| `mandatory` | Всегда для текущего действия. | `README.md`, state активного режима, `Protocols/protocol_index.md`. | Нельзя пропустить без `blocked`. |
| `local` | Локальный объект работы. | Active issue, selected concept, local registry. | Не читать чужой объект без ссылки. |
| `referenced` | Только по ссылке из state/contract/registry. | Зависимый issue, validation anchor, output. | Не расширять scope молча. |
| `optional` | Только если повышает качество и есть причина. | Дополнительный протокол или concept detail. | Не подменяет mandatory. |
| `excluded` | Не загружать без отдельной причины. | Внешние handoff/audit/checkpoint материалы. | Не писать в production repo. |

## Context route matrix

| Действие | Mandatory context | Local context | Referenced context | Next protocol |
|---|---|---|---|---|
| Service write | `README.md`; `State/service_state.md`; `Protocols/protocol_index.md`; `mode_routing`; `github_write_protocol` | active issue, registry/events, target files | validation anchors, dependent protocols | target service protocol |
| State repair | `README.md`; relevant state; `state_architecture`; `response_marker` | active issue, sync-report | other mode state if explicitly referenced | validation |
| Existing issue resume | `README.md`; active state; issue registry; event log | `Issues/<active_issue>/README.md` | sync-report return anchor | target task protocol |
| GitHub conflict | active state; target file; branch diff; sync-report | active issue/event trace | rollback protocol if unsafe | conflict recovery |
| Execution concept selection | `README.md`; `State/execution_state.md`; `Concepts/README.md`; `execution_bootstrap` | selected concept README and local registry | linked execution issue | concept work |
| Concept export | execution state; selected concept local registry; `concept_export` | output/export/source pages | validation protocol | validation |
| Final validation | root README; active state; registry; events; final/sync reports | changed paths and issue artifact | language/navigation checks | response marker |

## Service Mode context

Минимальный набор перед service-write:

```text
README.md
State/service_state.md
Protocols/protocol_index.md
Protocols/context_loading.md
Protocols/mode_routing.md
Protocols/github_write_protocol.md
Issues/issue_registry.jsonl
Issues/issue_events.jsonl
Issues/<active_issue>/README.md
Validation/final_check.md
Validation/sync_report.md
```

Дополнительно читаются target protocols, registry/schema, templates, inbox или validation files, если они входят в текущий contract.

## Execution Mode context

Минимальный набор перед работой с выбранной концепцией:

```text
README.md
State/execution_state.md
Concepts/README.md
Concepts/<active_concept>/README.md
Concepts/<active_concept>/page_registry.jsonl
Protocols/protocol_index.md
Protocols/execution_bootstrap.md
Protocols/concept_export.md
```

Файлы конкретной концепции читаются только после выбора `active_object` и проверки `allowed_write_scope`.

## Existing issue resume context

| Evidence | Обязательность | Причина |
|---|---|---|
| active issue в state | обязательно | определяет mode и target task |
| registry row | обязательно | хранит status/current_task/return_anchor |
| latest event | обязательно | подтверждает последний persisted action |
| issue artifact | обязательно | хранит scoped report и next step |
| sync-report | обязательно после GitHub write | даёт branch, changed paths and readback status |

Если любой элемент отсутствует или противоречит остальным, action переходит в `partial`/`blocked`, а запись target files не выполняется до восстановления focus.

## Protocol card

| Поле | Значение |
|---|---|
| Owner | `Service Mode` |
| Trigger | новый запрос, recovery, existing issue resume, pre-write read |
| Inputs | command, active state, target paths, active issue, changed paths |
| Required context | root README, active state, protocol index, mode routing, target protocol |
| Outputs | loaded context set, skipped context with reason, blocked state if mandatory context missing |
| Write scope | read-only; state updates выполняются только через target task |
| Next protocol | `mode_routing`, active target protocol, `validation_protocol` |
| Blocking conditions | missing mandatory file, stale state/registry focus, mixed scope without transfer |

## Dry-run P2-004

| Scenario | Вход | Ожидаемый context set | Результат P2-004 |
|---|---|---|---|
| Service patch | `CB-P2`, target `Protocols/protocol_index.md` | README, service state, protocol index, context/mode/write protocols, issue registry/events, CB-P2, final/sync | route подтверждён; scope остаётся `Service Mode` |
| Existing issue resume | `CB-P2`, current_task=`P2-004` | state + registry row + event + issue artifact + sync-report | продолжение P2-004 без нового issue |
| Execution fixture read | `Concepts/smoke`, export readiness | README, execution state, Concepts entry, smoke README/local registry, execution bootstrap, concept export | route подтверждён; service write запрещён без transfer |
| Mixed request | service protocol + selected concept content | сначала `mode_routing.md`, затем split/transfer | смешанный write без transfer блокируется |

## Ограничение объёма

Если файл не нужен для решения текущей задачи, он не загружается. Если без него нельзя проверить запись, файл загружается после записи для readback evidence. Отсутствующий mandatory file фиксируется как `blocked`; агент не заменяет его догадкой.