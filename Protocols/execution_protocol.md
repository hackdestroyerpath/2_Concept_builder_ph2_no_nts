# Протокол выполнения `issue`

[← К реестру протоколов](protocol_index.md)

## Цель

Выполнить `issue` только после утверждённых requirements, solution и contract.

## Входы

- `contract.md` со статусом `approved`;
- `solution.md`;
- `requirements.md`;
- зависимости issue;
- allowed write scope текущего режима.

## Процесс simple issue

1. Перечитать `contract.md` и affected paths.
2. Проверить, что нет активной блокирующей зависимости.
3. Выполнить только действия, указанные в contract.
4. Записать production-файлы результата.
5. Создать или обновить `output.md`.
6. Создать `report.md` с проверкой contract.
7. Записать event выполнения.
8. Перечитать изменённые файлы и обновить issue state.

## Output

`output.md` содержит:

- что создано или изменено;
- ссылки на production-файлы;
- какие requirements покрыты;
- что осталось вне scope;
- риски и дальнейшие действия.

## Report

`report.md` содержит сверку: requirement → action → output → verification.

## Выход

Обновлённые production-файлы, `output.md`, `report.md`, event и статус `completed` или `blocked`.
