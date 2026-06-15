# Question Answer

[← Реестр протоколов](protocol_index.md) | [Жизненный цикл issue](issue_lifecycle.md) | [Requirements protocol](requirements_protocol.md)

## Назначение

`Question Answer` используется, когда безопасное выполнение `issue` зависит от недостающего решения. Протокол не превращает догадки агента в production-решения: вопрос, ответ или причина пропуска должны быть сохранены в issue artifact, event log или task report.

## Когда запускать

1. Команда пользователя неполная или двусмысленная.
2. Неясен режим: `Service Mode` или `Execution Mode`.
3. Неясен объект работы, целевой файл, область записи или критерий готовности.
4. Есть конфликт между state, protocol, issue registry и командой пользователя.
5. Продолжение может изменить production-файлы без проверяемого основания.

## Формат решения

```text
question_id:
issue_id:
mode:
active_object:
missing_decision:
why_it_blocks_or_does_not_block:
blocking_scope: none | requirements | contract | write | validation | transfer
options:
default_if_no_answer:
answer:
answer_source:
recorded_at:
status: open | answered | skipped_with_reason | blocked
transferred_to_requirements: yes | no
return_anchor:
```

## Persisted skip reason

Если вопрос не задаётся, потому что безопасное значение можно вывести из state, протокола или утверждённого контракта, агент записывает `skipped_with_reason` и указывает:

- источник допущения;
- почему допущение не расширяет scope;
- куда перенесён критерий проверки;
- какой файл или event хранит это решение.

## Правила минимальности

1. Вопрос задаётся только если ответ меняет scope, risk, output или validation.
2. Нельзя задавать серию вопросов из любопытства.
3. Blocking question остаётся blocker до ответа или documented skip reason.
4. Ответ, меняющий scope, переносится в `requirements_protocol` и contract.
5. Если пользователь пишет `продолжай`, агент использует последнее безопасное допущение и фиксирует его в event/report.

## Выходы

| Ситуация | Выход | Следующий протокол |
|---|---|---|
| Ответ получен | answer recorded with source | `requirements_protocol` |
| Вопрос безопасно пропущен | `skipped_with_reason` recorded | `requirements_protocol` |
| Ответ блокирует scope | `blocked` with return anchor | user decision or `issue_lifecycle` |
| Нужен transfer | transfer decision recorded | `complex_and_linked_issues` |
