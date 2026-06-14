# CB-005 — Execution bootstrap and concept template

[← Issues](../README.md) | [Execution bootstrap](../../Protocols/execution_bootstrap.md) | [Concept template](../../Templates/concept/README.md)

## Provenance

Статус: `reconstructed_with_evidence`. Issue описывает recoverable production scope для `Execution Mode` bootstrap и concept templates.

## Scope

- выбрать существующую концепцию или создать новую из `Templates/concept/`;
- связать `Execution Mode` с выбранной концепцией;
- требовать local registry и backlinks;
- маршрутизировать export через `Protocols/concept_export.md`.

## Evidence

| Evidence | Роль |
|---|---|
| `Protocols/execution_bootstrap.md` | выбор/создание concept scope |
| `Protocols/concept_export.md` | export manifest route |
| `Templates/concept/README.md` | template entry and child routes |
| `Concepts/README.md` | concepts entrypoint |

## Closure rule

`Execution Mode` пишет только в selected concept scope и linked execution issue. Service files меняются через `Service Mode`.