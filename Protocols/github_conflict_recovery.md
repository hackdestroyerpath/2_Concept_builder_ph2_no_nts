# GitHub conflict recovery

[← Реестр протоколов](protocol_index.md) | [GitHub write protocol](github_write_protocol.md)

## Purpose

This protocol covers conflict handling and recovery for GitHub writes.

## Before update

```text
fetch_file:
read current sha:
prepare full replacement:
write with sha:
read back:
```

## Conflict

If update returns conflict, fetch the file again, take the fresh sha, compare intended content with current content, then retry once with a new full replacement.

## Recovery

If a write result is unclear, verify actual state by reading the file or commit before repeating the action.

## Safe stop

If verification fails twice, stop writes, mark status as `blocked`, and report the last known file state.
