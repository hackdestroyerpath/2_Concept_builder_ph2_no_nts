# CB-002 — Common core protocols

[← Issues](../README.md) | [Protocol index](../../Protocols/protocol_index.md) | [State architecture](../../Protocols/state_architecture.md) | [Context loading](../../Protocols/context_loading.md)

## Provenance

Статус: `reconstructed_with_evidence`. Исходная цепочка выполнения не сохранила полноценный task artifact, поэтому эта страница фиксирует только факты, восстановленные из production-файлов, registry и event log.

## Scope

- архитектура состояния `Service Mode` и `Execution Mode`;
- загрузка bounded context перед действием;
- маршрутизация режима и transfer route;
- response marker как компактная проекция state.

## Evidence

| Evidence | Роль |
|---|---|
| `Protocols/state_architecture.md` | canonical state schema и mapping к маркеру |
| `Protocols/context_loading.md` | mandatory/local/referenced context |
| `Protocols/mode_routing.md` | выбор Service/Execution/blocked route |
| `Protocols/response_marker.md` | формат ответа и persistence status |
| `Issues/issue_events.jsonl` | reconstructed event trace |

## Closure rule

`CB-002` сохраняется как provenance node. Финальная проверка остаётся в `CB-P2` и `Validation/final_check.md`.