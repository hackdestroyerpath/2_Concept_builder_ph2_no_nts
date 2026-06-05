# Process `{concept_id}`

[← К концепции](README.md)

## Назначение

Описать, как агент развивает, проверяет и экспортирует концепцию.

## Основной цикл изменения

```text
input → issue → requirements → solution/contract → file changes → validation → report → roll-up
```

## Процесс развития

| Step | Input | Action | Output | Gate |
|---|---|---|---|---|
| 1 | request | create or select issue | issue state/reason | registry decision |
| 2 | reason and QA | build requirements | requirements.md | approval |
| 3 | requirements | build solution and contract | solution.md, contract.md | approval |
| 4 | contract | update concept files | changed MD files | validation |
| 5 | output/report | close issue | roll-up summary | cleanup |

## Проверка изменений

- входной README ведёт ко всем страницам;
- каждая страница имеет обратную ссылку;
- `structure.md` соответствует файлам;
- `page_registry.jsonl` соответствует файлам и ссылкам;
- requirements связаны с изменёнными элементами;
- operating model не противоречит process.

## Export gate

Concept export возможен только после проверки navigation, requirements, operating model, process и linked issue status.
