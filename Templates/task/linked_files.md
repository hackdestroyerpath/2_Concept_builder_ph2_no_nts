# Связанные файлы

[← Задача](README.md) | [Сложные задачи](../../Protocols/complex_and_linked_issues.md)

## Связанный элемент

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

## Правило зависимости

Блокирующий связанный элемент должен быть решён до исполнения контракта. Циклы записываются как `blocked` и передаются в `complex_and_linked_issues.md`. Удалённые зависимости требуют причины и доказательства.