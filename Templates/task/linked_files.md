# Linked files

[← Task](README.md) | [Complex issues](../../Protocols/complex_and_linked_issues.md)

## Linked item

```text
link_id:
path_or_issue:
type: parent | child | dependency | attachment | output | registry | state | validation | cleanup | transfer
source:
reason:
status: proposed | required | waiting | resolved_with_evidence | removed_with_reason | blocked
owner:
blocking: yes | no
return_anchor:
notes:
```

## Dependency rule

A blocking linked item must be resolved before contract execution. Cycles are recorded as `blocked` and escalated to `complex_and_linked_issues.md`. Removed dependencies require reason and evidence.
