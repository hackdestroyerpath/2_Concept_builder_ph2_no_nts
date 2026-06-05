# Протокол требований

[← К реестру протоколов](protocol_index.md)

## Цель

Сформировать проверяемые requirements до solution и выполнения.

## Входы

- `reason.md` активного `issue`;
- `question_answer.md`, если QA проводился;
- входные материалы и attachments;
- зависимости и scope режима.

## Структура требования

```yaml
requirement_id: REQ-...
text:
source:
reason:
status: proposed | approved | rejected | changed
links:
  issue_id:
  question_id:
  input_ref:
  parent_requirement:
verification:
```

## Процесс

1. Собрать требования из reason, input, QA и зависимостей.
2. Сгруппировать требования деревом: обязательные, ограничения, критерии результата, проверки.
3. Указать provenance для каждого требования.
4. Сохранить `requirements.md` до ответа.
5. Показать пользователю краткую таблицу требований и спорные места.
6. После утверждения перевести requirements в `approved` и открыть solution stage.

## Gate

Выполнение не начинается без утверждённых requirements или явного contract, который фиксирует, почему требования уже утверждены ранее.

## Выход

Сохранённый файл `requirements.md`, обновлённый issue state и marker с `dialogue_state: awaiting_requirements_decision` или переходом к solution.
