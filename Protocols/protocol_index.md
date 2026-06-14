# Реестр протоколов

[← Точка входа](../README.md) | [Service state](../State/service_state.md) | [Execution state](../State/execution_state.md) | [Validation](../Validation/final_check.md)

## Назначение

`Protocols/protocol_index.md` — диспетчерская карта протоколов `Concept Builder`. Этот файл не является простым списком Markdown-страниц: он выбирает следующий исполнимый протокол по режиму, действию, входным данным, ожидаемому выходу и условию блокировки.

## Базовая route matrix

| Контур | Входной сигнал | Первый протокол | Требуемый контекст | Выход | Следующий протокол |
|---|---|---|---|---|---|
| Общий core | любой новый запрос | [`context_loading.md`](context_loading.md) | `README.md`, active state, этот индекс | bounded context set | [`mode_routing.md`](mode_routing.md) |
| Общий core | target path или user intent | [`mode_routing.md`](mode_routing.md) | command, active state, target paths | `Service Mode`, `Execution Mode`, transfer или `blocked` | target protocol |
| Общий core | state/marker drift | [`state_architecture.md`](state_architecture.md) + [`response_marker.md`](response_marker.md) | state files, marker fields, sync report | canonical state and marker mapping | [`validation_protocol.md`](validation_protocol.md) |
| Issue pipeline | новый или существующий service issue | [`issue_lifecycle.md`](issue_lifecycle.md) | registry, events, active issue artifact | issue row, event, state update | [`question_answer.md`](question_answer.md) или [`requirements_protocol.md`](requirements_protocol.md) |
| Issue pipeline | неясные требования | [`question_answer.md`](question_answer.md) | user question, known facts, skip reason if any | questions/answers or persisted skip reason | [`requirements_protocol.md`](requirements_protocol.md) |
| Issue pipeline | требования готовы | [`requirements_protocol.md`](requirements_protocol.md) | source, reason, acceptance criteria | approved/scoped requirements | [`issue_execution.md`](issue_execution.md) |
| Issue pipeline | simple issue execution | [`issue_execution.md`](issue_execution.md) | requirements, solution, contract, target paths | output/report and validation plan | [`github_write_protocol.md`](github_write_protocol.md) |
| Issue pipeline | linked issue or dependency | [`complex_and_linked_issues.md`](complex_and_linked_issues.md) | dependency graph, parent/child refs, return anchor | ready/waiting/roll-up state | [`issue_execution.md`](issue_execution.md) |
| Issue pipeline | priority, approval, cleanup transition | [`task_flow_hardening.md`](task_flow_hardening.md) | priority, approval, provenance, cleanup decision | safe lifecycle transition | [`validation_protocol.md`](validation_protocol.md) |
| GitHub write | production write package | [`github_write_protocol.md`](github_write_protocol.md) | classifier, pre-sha, target paths, validation plan | write/readback/sync-report | [`github_conflict_recovery.md`](github_conflict_recovery.md) или [`validation_protocol.md`](validation_protocol.md) |
| GitHub write | conflict, 409, mismatched SHA | [`github_conflict_recovery.md`](github_conflict_recovery.md) | expected/actual SHA, branch diff, changed paths | retry, rebuild, rollback или blocked | [`rollback_protocol.md`](rollback_protocol.md) или write retry |
| GitHub write | unsafe persisted write | [`rollback_protocol.md`](rollback_protocol.md) | pre/post SHA, changed paths, reason | rollback event and validation evidence | [`validation_protocol.md`](validation_protocol.md) |
| Templates | template check or instantiation | [`template_validation.md`](template_validation.md) | template README, local registry, task/concept rules | compatibility result | issue pipeline or validation |
| Execution | создать, выбрать или продолжить концепцию | [`execution_bootstrap.md`](execution_bootstrap.md) | execution state, `Concepts/README.md`, local registry | selected concept scope | [`concept_export.md`](concept_export.md) или concept work |
| Execution | export readiness or production export | [`concept_export.md`](concept_export.md) | source paths, scope, audience, format, output evidence | export manifest | [`validation_protocol.md`](validation_protocol.md) |
| Validation | closure, merge, acceptance, dry-run | [`validation_protocol.md`](validation_protocol.md) | changed paths, registry, state, events, language checks | evidence matrix and next safe step | [`response_marker.md`](response_marker.md) |

## Existing issue focus/resume flow

| Шаг | Проверка | Источник истины | Следующий route |
|---|---|---|---|
| 1 | Найти active issue в state | `State/service_state.md` или `State/execution_state.md` | `issue_lifecycle` |
| 2 | Проверить registry row | `Issues/issue_registry.jsonl` | `task_flow_hardening` |
| 3 | Проверить последний event | `Issues/issue_events.jsonl` | active task contract |
| 4 | Открыть issue artifact | `Issues/<issue_id>/README.md` | target protocol |
| 5 | Сверить return anchor | `Validation/sync_report.md` или issue artifact | продолжение bounded step |
| 6 | Если focus расходится | state/registry/events mismatch | `state_architecture` + `validation_protocol`, без финального closure |

Existing issue не создаётся заново, если есть `issue_id`, registry row, event trace и return anchor. В этом случае агент продолжает текущий bounded step, а не открывает параллельный issue.

## Protocol cards

| Protocol | Owner | Trigger | Inputs | Required context | Outputs | Write scope | Next protocol | Blocking conditions |
|---|---|---|---|---|---|---|---|---|
| `context_loading` | Service Mode | любой запрос или recovery | command, active state, target paths | README, active state, protocol index | loaded context set | read-only, кроме state update через target task | `mode_routing` | mandatory context missing |
| `mode_routing` | Service Mode | target path, user intent, mixed scope | active object, requested action, target paths | state, route matrix | selected mode or transfer | state/event only through active issue | target protocol | mixed service/execution write without transfer |
| `state_architecture` | Service Mode | state drift, missing field, marker mismatch | state files, marker, issue refs | service/execution state, response marker | canonical field map | `State/` under approved repair scope | `response_marker` or validation | unresolved owner boundary |
| `response_marker` | Service Mode | every response tail | canonical state fields | state and sync-report | compact marker | no production write unless active task updates state | validation or next turn | missing persistence status |
| `github_write_protocol` | Service Mode | production write package | classifier, operation, pre-sha, paths | target files, state, issue, validation | post-sha, readback, sync-report | only active mode write scope | conflict recovery or validation | development file or missing validation plan |
| `github_conflict_recovery` | Service Mode | 409, stale SHA, mismatched readback | expected/actual sha, branch diff | target file, branch diff, sync-report | retry/rebuild/blocked decision | no blind write | rollback or write retry | unsafe overwrite risk |
| `rollback_protocol` | Service Mode | unsafe persisted write | pre/post sha, changed paths, reason | events, sync report, affected files | rollback event and validation | affected production paths only by approved rollback | validation | rollback would remove validated output |
| `issue_lifecycle` | Service Mode | create/focus/approve/reject/cleanup | reason, priority, provenance | registry, events, issue artifact | issue row and event | `Issues/` and state | QA, requirements, or task flow | issue without reason or provenance |
| `question_answer` | Service Mode | uncertainty affects execution | questions, known facts, skip reason | active issue and requirements context | persisted QA or skip reason | task artifact or event | requirements | unresolved blocker question |
| `requirements_protocol` | Service Mode | before execution | sources, reasons, acceptance | issue artifact and QA | requirement tree | task artifact | issue execution | unapproved or unscoped requirement |
| `issue_execution` | Service Mode | approved contract | requirements, solution, target paths | task templates, protocol refs | solution/contract/report | approved target paths | github write | contract absent |
| `complex_and_linked_issues` | Service Mode | dependency or child issue | dependency graph, child refs | registry and linked files | waiting/ready/roll-up | issue artifacts only | issue execution | cycle or unresolved child output |
| `task_flow_hardening` | Service Mode | status transition | priority, approval, cleanup | registry/events/issue | safe transition | registry/events/state | validation | missing approval or cleanup reason |
| `template_validation` | Service Mode | template change or instantiation | template files, local registry | templates and validation protocol | compatibility result | `Templates/` under service issue | issue execution or validation | missing child route or placeholder leak |
| `execution_bootstrap` | Execution Mode | create/select/continue concept | concept id, title, active issue | execution state, Concepts entry, local registry | selected concept scope | selected concept folder and linked execution issue | concept export or concept work | missing concept id, issue or local registry |
| `concept_export` | Execution Mode | export readiness or user export | source paths, audience, format | concept files, output, local registry | export manifest | selected concept export file | validation | output/export readiness drift |
| `validation_protocol` | Service Mode | before closure, merge, or next phase | changed paths, registry, state, events | final check, navigation/language checks, sync report | evidence matrix | `Validation/` and state/event coupling | response marker | assertion-only closure |

## Failure routes

| Failure | Immediate protocol | Required action |
|---|---|---|
| Mandatory context missing | `context_loading` | mark `blocked`, record missing path, do not write |
| Mode ambiguity | `mode_routing` | split into service/execution route or block mixed write |
| State/marker mismatch | `state_architecture` | repair state/marker in active issue, then validate |
| Existing issue cannot be resumed | `issue_lifecycle` | restore registry/event/issue artifact coupling before target write |
| Write SHA conflict | `github_conflict_recovery` | read latest file, compare branch diff, retry only safe bounded payload |
| Validation evidence absent | `validation_protocol` | keep status `partial` or `blocked`, do not claim closure |

## P2-004 validation notes

P2-004 фиксирует route matrix и protocol cards для common core, issue pipeline, GitHub write, validation, execution bootstrap и concept export. Полная финальная приёмка остаётся за P2-010; этот индекс только задаёт исполнимую маршрутизацию.