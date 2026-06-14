# CB-004 — Final service protocols

[← Issues](../README.md) | [Write protocol](../../Protocols/github_write_protocol.md) | [Validation protocol](../../Protocols/validation_protocol.md)

## Provenance

Статус: `reconstructed_with_evidence`. Эта страница связывает ранее сохранённые service protocols с явным issue artifact и registry row.

## Scope

- production/development classifier;
- write preflight и readback;
- conflict recovery и rollback route;
- validation gates;
- template validation.

## Evidence

| Evidence | Роль |
|---|---|
| `Protocols/github_write_protocol.md` | write package, classifier, readback |
| `Protocols/github_conflict_recovery.md` | conflict decision path |
| `Protocols/rollback_protocol.md` | rollback trigger and evidence |
| `Protocols/validation_protocol.md` | validation gate |
| `Protocols/template_validation.md` | template compatibility check |

## Closure rule

Service protocol не принимается по одиночному ярлыку. Нужны route, state, event и validation evidence.