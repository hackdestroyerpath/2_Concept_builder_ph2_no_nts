# Реестр протоколов

[← Точка входа](../README.md) | [Service state](../State/service_state.md) | [Validation](../Validation/final_check.md)

## Routing matrix

| Mode | Action | Protocol | Output | Next |
|---|---|---|---|---|
| any | загрузить контекст | [`context_loading.md`](context_loading.md) | loaded context set | mode routing |
| any | выбрать режим | [`mode_routing.md`](mode_routing.md) | Service, Execution, transfer или blocked | target protocol |
| any | исправить state/marker drift | [`state_architecture.md`](state_architecture.md), [`response_marker.md`](response_marker.md) | canonical fields | validation |
| Service | создать или продолжить issue | [`issue_lifecycle.md`](issue_lifecycle.md) | registry row, event, state update | QA или requirements |
| Service | уточнить требования | [`question_answer.md`](question_answer.md) | questions/answers или skip reason | requirements |
| Service | утвердить требования | [`requirements_protocol.md`](requirements_protocol.md) | requirements tree | execution |
| Service | выполнить simple issue | [`issue_execution.md`](issue_execution.md) | solution, contract, output, report | validation |
| Service | выполнить complex/linked issue | [`complex_and_linked_issues.md`](complex_and_linked_issues.md) | dependency state and roll-up | execution |
| Service | применить approval/priority/cleanup | [`task_flow_hardening.md`](task_flow_hardening.md) | safe lifecycle transition | validation |
| Service | записать production file | [`github_write_protocol.md`](github_write_protocol.md) | readback and sync-report | conflict or validation |
| Service | разобрать write conflict | [`github_conflict_recovery.md`](github_conflict_recovery.md) | retry, rebuild, rollback or user decision | rollback/write |
| Service | откатить небезопасную запись | [`rollback_protocol.md`](rollback_protocol.md) | rollback event and validation | validation |
| Service | проверить template | [`template_validation.md`](template_validation.md) | semantic compatibility | execution |
| Execution | выбрать concept | [`execution_bootstrap.md`](execution_bootstrap.md) | selected concept scope | concept protocol |
| Execution | собрать export | [`concept_export.md`](concept_export.md) | export manifest | validation |
| any | закрыть проверку | [`validation_protocol.md`](validation_protocol.md) | evidence matrix | response marker |

## Protocol cards

| Protocol | Owner | Trigger | Inputs | Outputs | Blocking condition |
|---|---|---|---|---|---|
| `context_loading` | Service | любой новый action | state, command, active issue | loaded/skipped context | missing state without recovery route |
| `mode_routing` | Service | target path or user intent | active object, requested action | mode or transfer | mixed service/execution scope |
| `state_architecture` | Service | field drift | state files, marker | canonical schema | unresolved owner boundary |
| `response_marker` | Service | every response | state fields | final marker | missing persistence status |
| `github_write_protocol` | Service | file write | classifier, sha, operation, target paths | post sha, readback, sync-report | development file or missing validation plan |
| `github_conflict_recovery` | Service | API conflict or mismatched readback | expected/actual state | retry, rebuild, rollback, blocked | unsafe scope |
| `rollback_protocol` | Service | unsafe persisted write | pre/post sha, paths, reason | rollback event and validation | rollback would remove validated user output |
| `issue_lifecycle` | Service | create/focus/approve/reject/cleanup | reason, priority, provenance | registry and event | issue without reason |
| `question_answer` | Service | uncertainty affects quality | open questions or skip reason | persisted QA artifact | missing requirements gate |
| `requirements_protocol` | Service | before execution | source, reason, acceptance criteria | approved requirements | unapproved requirement |
| `issue_execution` | Service | approved contract | requirements, solution, contract | output and report | contract absent |
| `complex_and_linked_issues` | Service | dependency or parent issue | dependency graph | waiting/ready/roll-up | cycle or missing output |
| `task_flow_hardening` | Service | status transition | priority, approval, cleanup | safe transition | missing provenance |
| `template_validation` | Service | template instantiation | template registry | compatibility result | missing child route |
| `execution_bootstrap` | Execution | concept work | concept id or creation request | active concept scope | local registry missing |
| `concept_export` | Execution | export check | source paths, scope, audience, format | export manifest | readiness drift |
| `validation_protocol` | Service | before closure or merge | changed paths, registry, state, events, language | evidence matrix | assertion-only closure |
