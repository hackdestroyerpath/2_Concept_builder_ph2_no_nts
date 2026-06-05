# Протокол сети концепции и export

[← К реестру протоколов](protocol_index.md) | [Вход `Execution Mode`](../Concepts/README.md) | [Шаблоны концепции](../Concepts/templates/README.md)

## Сеть концепции

Каждая концепция внутри `Concepts/{concept_id}/` хранится как связанная MD-сеть с одним входным `README.md`.

Обязательные смысловые блоки:

- `about` — назначение, аудитория и границы;
- `requirements` — утверждённые требования и provenance;
- `operating_model` — рабочая модель концепции;
- `process` — порядок развития, проверки и export;
- `structure.md` — карта страниц и ссылок;
- `page_registry.jsonl` — машинная карта файлов и связей.

## Создание концепции

1. Создать или выбрать `issue` на новую концепцию.
2. Утвердить requirements и contract.
3. Выбрать стабильный `concept_id`.
4. Скопировать шаблоны из `Concepts/templates/` в `Concepts/{concept_id}/`.
5. Заполнить README, about, requirements, operating model и process.
6. Создать `structure.md` и `page_registry.jsonl` конкретной концепции.
7. Проверить навигацию и записать event.

## Навигация

Каждый MD-файл должен быть достижим из входного README концепции. Каждая вложенная страница имеет обратную ссылку. Cross-links создаются только по функциональной причине. Attachment входит в production-export только при ссылке из MD-файла.

## Production export

Production-export включает только готовую концепцию:

```text
README.md
about.md
requirements.md
operating_model.md
process.md
structure.md
page_registry.jsonl
attachments/       # только если attachment является частью готовой концепции
```

Рабочий export со state, `Issues/`, QA-историей и `Inbox/` создаётся отдельным архивом и не смешивается с production-export.

## Gate export

Перед export должны быть проверены:

- входной README ведёт ко всем страницам;
- `structure.md` и `page_registry.jsonl` соответствуют файлам;
- requirements, operating model и process согласованы;
- открытые `issue` закрыты или явно вынесены из export scope;
- linked-связи не блокируют готовность;
- language и navigation validation пройдены.

## Работа за пределами окна контекста

Агент работает уровнями: обзор → локальный участок → детали → roll-up → возврат наверх. На каждом уровне загружается только контекст, достаточный для текущего действия.
