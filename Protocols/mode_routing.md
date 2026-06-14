# Маршрутизация режимов

[← Реестр протоколов](protocol_index.md) | [Загрузка контекста](context_loading.md) | [Архитектура состояния](state_architecture.md) | [Маркер ответа](response_marker.md)

## Назначение

`mode_routing` выбирает `Service Mode`, `Execution Mode`, transfer route или `blocked`. Протокол не только различает папки; он связывает user intent, target paths, active state, issue focus и следующий исполнимый protocol card.

## Режимы и области записи

| Режим | Объект работы | Разрешённая запись | State | Следующий core protocol |
|---|---|---|---|---|
| `Service Mode` | Сама система `Concept Builder`: инструкции, протоколы, state, registry, validation, service issues, templates. | `README.md`, `Instructions/`, `Protocols/`, `State/service_state.md`, service-repair `State/execution_state.md`, `Issues/`, `Inbox/`, `Registry/`, `Validation/`, `Templates/` при service issue. | `State/service_state.md` | `issue_lifecycle` или target service protocol |
| `Execution Mode` | Выбранная концепция внутри `Concepts/` и её linked execution issue. | `Concepts/<active_concept>/`, local registry, state/output/export и связанный execution issue. | `State/execution_state.md` | `execution_bootstrap` или `concept_export` |

## Decision matrix

| Сигнал | Режим | Required context | Действие | Blocking condition |
|---|---|---|---|---|
| Target path в `Protocols/`, `Instructions/`, `Registry/`, `Validation/`, `Templates/`, `Inbox/` | `Service Mode` | service state, active service issue, target protocol | выполнить service route и обновить service state/events | отсутствует active issue для write |
| Target path `State/service_state.md` | `Service Mode` | service state, issue registry/events | разрешено только service issue или service patch | команда относится к selected concept |
| Target path `State/execution_state.md` | `Execution Mode`, либо `Service Mode` для repair patch | execution state, reason for repair | если repair, записать причину в active service issue | repair reason отсутствует |
| Target path `Concepts/<id>/...` | `Execution Mode` | execution state, concept README, local registry | выбрать concept, проверить linked issue, затем писать только concept scope | concept не выбран или нет local registry |
| Пользователь просит создать/вести концепцию | `Execution Mode` | `Concepts/README.md`, templates, execution state | запуск через `execution_bootstrap.md` | нет `concept_id` или issue/provenance |
| Пользователь просит изменить правила системы | `Service Mode` | service state, protocol index, issue registry | создать/продолжить service issue | нет reason/provenance |
| В одном запросе есть service и execution изменения | transfer / split | оба state-файла, route matrix | выполнить только разрешённый scope; второй scope — отдельным route | смешанная запись одним пакетом |
| Existing issue указан пользователем или state | active issue mode | state, registry row, last event, issue artifact | resume flow вместо нового issue | registry/event/artifact расходятся |
| Нельзя выбрать режим без риска | `blocked` | command and state evidence | записать причину, return anchor, не писать | ambiguity unresolved |

## Existing issue focus/resume flow

| Шаг | Действие | Evidence | Следующий протокол |
|---|---|---|---|
| 1 | Взять `active_issue` из state активного режима | `State/service_state.md` или `State/execution_state.md` | `issue_lifecycle` |
| 2 | Найти строку issue в registry | `Issues/issue_registry.jsonl` | `task_flow_hardening` |
| 3 | Сверить последний event и current_task | `Issues/issue_events.jsonl` | active task contract |
| 4 | Открыть issue artifact | `Issues/<issue_id>/README.md` | target protocol |
| 5 | Проверить return anchor и sync-report | `Validation/sync_report.md` или concept report | `context_loading` |
| 6 | При расхождении state/registry/event | фиксировать `partial` или `blocked` | `state_architecture` + `validation_protocol` |

Resume flow запрещает создавать параллельный service issue, если текущий `CB-P2` уже содержит branch, active task, event trace и return anchor.

## Transfer rule

Если задача текущего режима обнаруживает работу другого режима:

1. Остановить write по чужому scope.
2. Зафиксировать причину в active issue или event log.
3. Создать route: `service_to_execution`, `execution_to_service` или `blocked_mixed_scope`.
4. Обновить только state разрешённого режима.
5. Продолжить после явного выбранного режима и достаточного контекста.

## Protocol card

| Поле | Значение |
|---|---|
| Owner | `Service Mode` |
| Trigger | target path, user intent, active issue focus, mixed-scope signal |
| Inputs | command, active state, target paths, issue registry row, last event |
| Required context | `README.md`, active state, `Protocols/protocol_index.md`, target issue or concept entry |
| Outputs | selected mode, transfer route, blocked reason, next protocol |
| Write scope | только state/event update для active issue; content write выполняет следующий target protocol |
| Next protocol | `issue_lifecycle`, `execution_bootstrap`, `state_architecture`, target service protocol |
| Blocking conditions | missing issue reason, mixed scope, missing concept id, missing local registry, state/registry drift |

## P2-004 mode boundary check

| Проверка | Evidence |
|---|---|
| Service patch P2-004 меняет protocol index, routing, context loading and execution bootstrap through service issue | `State/service_state.md`, `Issues/CB-P2/README.md`, `Validation/sync_report.md` |
| Execution state не меняется в этом segment | `State/execution_state.md` readback from P2-003 remains referenced context |
| Existing issue resume route описан и связан с state/registry/events | this file, `Protocols/protocol_index.md`, `Issues/issue_registry.jsonl` |
| Следующий protocol repair route остаётся `P2-005` only after P2-004 readback | `Validation/sync_report.md` |

## Ошибка маршрутизации

Если режим невозможно выбрать без риска, агент пишет `persistence_status: blocked`, указывает `return_anchor`, не меняет чужой scope и не объявляет готовность.