# Question Answer

[← Task](README.md) | [Requirements](requirements.md) | [Protocol](../../Protocols/question_answer.md)

## Вопрос или skip reason

```text
question_id:
status: open | answered | skipped_with_reason
missing_decision:
why_it_blocks_or_does_not_block:
options:
default_if_no_answer:
answer:
answer_source:
recorded_at:
```

## Правила

1. Вопрос задаётся только если ответ влияет на scope, risk, output или validation.
2. Если агент продолжает без вопроса, он фиксирует `skipped_with_reason`.
3. Ответ переносится в `requirements.md` или `contract.md`, если меняет scope.
4. Нельзя закрывать задачу, если blocking question остаётся `open`.
