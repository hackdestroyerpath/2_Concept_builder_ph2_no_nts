# Вопросы и ответы

[← Задача](README.md) | [Requirements](requirements.md) | [Протокол](../../Protocols/question_answer.md)

## Вопрос или skip reason

```text
question_id:
issue_id:
status: open | answered | skipped_with_reason | blocked
missing_decision:
why_it_blocks_or_does_not_block:
blocking_scope: none | requirements | contract | write | validation | transfer
options:
default_if_no_answer:
answer:
answer_source:
recorded_at:
transferred_to_requirements: yes | no
return_anchor:
```

## Правила

1. Вопрос задаётся только если ответ влияет на scope, risk, output или validation.
2. Если агент продолжает без вопроса, он фиксирует `skipped_with_reason`.
3. Ответ переносится в `requirements.md` или `contract.md`, если меняет scope.
4. Нельзя переводить задачу к contract, если blocking question остаётся `open`.
5. Skip reason должен назвать source и почему пропуск не расширяет scope.
