# Связанные файлы

[← Задача](README.md) | [Complex issues](../../Protocols/complex_and_linked_issues.md)

## Связанный item

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

## Правило dependency

Blocking linked item должен быть resolved до исполнения contract. Cycles записываются как `blocked` и эскалируются в `complex_and_linked_issues.md`. Удалённые dependencies требуют reason и evidence.
