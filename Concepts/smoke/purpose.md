# Purpose

[← Smoke](README.md) | [Requirements](requirements.md)

## Проблема

Система должна доказывать, что новая концепция может быть создана из production-шаблона без ручных догадок, orphan-файлов и несвязанных registry rows.

## Цель

Подтвердить, что `Execution Mode` поддерживает:

- локальный state;
- локальный page registry;
- связанную структуру страниц;
- output model;
- export manifest;
- обратную связь с `Issues/CB-009` и финальной validation.

## Scope

```text
in_scope: template instantiation; local registry; output/export; readback validation
out_of_scope: real business concept content; development handoff; audit notes
assumption: smoke fixture remains in production only as validation evidence
```
