# CB-003 — Issue workflow protocols

[← Issues](../README.md) | [Issue lifecycle](../../Protocols/issue_lifecycle.md) | [Issue registry](../issue_registry.jsonl)

## Provenance

Статус: `reconstructed_with_evidence`. Persisted evidence — текущие production-файлы issue workflow, registry и event log, а не выдуманная историческая approval-цепочка.

## Scope

- создание, фокусировка и продолжение issue;
- approval, discussion, rejection и cleanup decisions;
- registry/event persistence перед пользовательскими claims;
- return-anchor для безопасного resume flow.

## Evidence

| Evidence | Роль |
|---|---|
| `Protocols/issue_lifecycle.md` | lifecycle grammar |
| `Protocols/task_flow_hardening.md` | priority, approval, cleanup, provenance |
| `Issues/issue_registry.jsonl` | machine issue state |
| `Issues/issue_events.jsonl` | chronological event trace |

## Closure rule

`CB-003` остаётся provenance node. Любые будущие изменения issue workflow обновляют registry, event log и validation вместе.