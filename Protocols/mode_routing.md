# Маршрутизация режимов

[← Реестр протоколов](protocol_index.md) | [Загрузка контекста](context_loading.md) | [Архитектура состояния](state_architecture.md)

## Назначение

Этот протокол выбирает `Service Mode`, `Execution Mode`, transfer route или блокировку. Он предотвращает смешивание service-governance с работой над конкретной концепцией.

## Режимы

| Режим | Объект работы | Разрешённая запись | State |
|---|---|---|---|
| `Service Mode` | Сама система `Concept Builder`: инструкции, протоколы, state, registry, validation, service issues, templates. | `README.md`, `Instructions/`, `Protocols/`, `State/service_state.md`, `Issues/`, `Inbox/`, `Registry/`, `Validation/`, `Templates/` при service issue. | `State/service_state.md` |
| `Execution Mode` | Выбранная концепция внутри `Concepts/` и её linked execution issue. | `Concepts/<active_concept>/`, local registry/output/export и связанный execution issue. | `State/execution_state.md` |

## Decision matrix

| Сигнал | Режим | Действие |
|---|---|---|
| Target path в `Protocols/`, `Instructions/`, `Registry/`, `Validation/`, `Templates/`, `Inbox/` | `Service Mode` | выполнить service protocol и обновить service state/events |
| Target path `State/service_state.md` | `Service Mode` | разрешено только service issue или service patch |
| Target path `State/execution_state.md` | `Execution Mode`, либо `Service Mode` для repair patch | если repair, записать причину в active service issue |
| Target path `Concepts/<id>/...` | `Execution Mode` | выбрать concept, прочитать local registry, проверить issue link |
| Пользователь просит создать/вести концепцию | `Execution Mode` | запуск через `execution_bootstrap.md` |
| Пользователь просит изменить правила системы | `Service Mode` | создать/продолжить service issue |
| В одном запросе есть service и execution изменения | transfer / split | не выполнять смешанную запись одним scope |
| Нет active issue для write | blocked или issue lifecycle | не писать production files без reason/provenance |

## Transfer rule

Если задача текущего режима обнаруживает работу другого режима:

1. Остановить write по чужому scope.
2. Зафиксировать причину в active issue или event log.
3. Создать transfer route: `service_to_execution`, `execution_to_service` или `blocked_mixed_scope`.
4. Обновить state только разрешённого режима.
5. Продолжить только после явного выбранного режима и достаточного контекста.

## P2-003 mode boundary check

| Проверка | Evidence |
|---|---|
| Service patch P2-003 меняет service protocols, instructions, state и validation | `State/service_state.md`, `Issues/CB-P2/README.md`, `Validation/sync_report.md` |
| Execution state меняется только как canonical repair target P2-003 | `State/execution_state.md`, `Validation/final_check.md` |
| Работа с `Concepts/smoke` не выполняется как пользовательская концепция | `State/execution_state.md`, `Concepts/README.md` |
| Следующий execution dry-run остаётся заблокирован до explicit Execution Mode action | `State/execution_state.md` |

## Ошибка маршрутизации

Если режим невозможно выбрать без риска, агент пишет `persistence_status: blocked`, указывает `return_anchor`, не меняет чужой scope и не объявляет готовность.
