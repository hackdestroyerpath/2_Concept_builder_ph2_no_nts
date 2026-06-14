# Linked files

[← Task](README.md) | [Complex issues](../../Protocols/complex_and_linked_issues.md)

## Linked item

```text
link_id:
path_or_issue:
type: parent | child | dependency | attachment | output | registry | state | validation
source:
reason:
status: proposed | required | optional | resolved | removed_with_reason | blocked
owner:
blocking:
notes:
```

## Dependency rule

A blocking linked item must be resolved before contract execution. Cycles are recorded as `blocked` and escalated to `complex_and_linked_issues.md`.
