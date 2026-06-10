# Task flow hardening

[← Реестр протоколов](protocol_index.md)

## Назначение

Протокол описывает усиление потока задач.

## Поля

```text
priority:
approval:
provenance:
cleanup_required:
```

## Decisions

```text
approval requested
approved
rejected
cleanup required
```

## Priority

```text
low
normal
high
urgent
```

## Provenance

Источник задачи фиксируется как user request, transfer, validation finding или checkpoint follow-up.

## Result

Task registry и event log показывают каждое решение, которое меняет состояние задачи.
