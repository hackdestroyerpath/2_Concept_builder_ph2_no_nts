# Operating model

[← Smoke](README.md) | [Process](process.md)

## Объекты

| Object | Role |
|---|---|
| concept pages | production-pages fixture |
| local registry | navigation and ownership contract |
| concept state | Execution Mode state snapshot |
| output page | result mapping |
| export manifest | export readiness evidence |
| linked issue `CB-009` | service/execution provenance bridge |

## Роли

| Role | Responsibility |
|---|---|
| `Execution Mode` | владеет содержимым fixture и export readiness |
| `Service Mode` | валидирует registry, cleanup и final evidence |

## Инварианты

1. Каждая production-page fixture имеет registry entry.
2. `README.md` route-доступен из `Concepts/README.md`.
3. `output.md` и `export.md` существуют как strict markdown pages.
4. Orphan/stub files не остаются в active tree.

## Failure modes

| Failure | Response |
|---|---|
| missing page | validation failed |
| path-only registry | validation failed |
| English-only user prose | language check failed |
| orphan file | cleanup required |
