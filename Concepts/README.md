# `Execution Mode`: концепции

[← К главной точке входа](../README.md) | [Протокол концепций](../Protocols/concept_network_export_protocol.md) | [Шаблоны](templates/README.md)

`Concepts/` — входная точка `Execution Mode`. Здесь хранятся конкретные концепции как связанные MD-сети.

## Как выбрать объект работы

1. Если концепция уже существует, открыть её `Concepts/{concept_id}/README.md`.
2. Если концепции нет, создать `issue` на создание концепции через [`../Issues/README.md`](../Issues/README.md).
3. До выбора концепции держать запись на уровне `issue` и state.

## Минимальная структура концепции

```text
Concepts/{concept_id}/
├── README.md
├── about.md
├── requirements.md
├── operating_model.md
├── process.md
├── structure.md
├── page_registry.jsonl
└── attachments/        # только если attachment входит в готовую концепцию
```

## Шаблоны

Папка [`templates/`](templates/README.md) хранит формы для входного README, about, requirements, operating model, process, structure и page registry. Шаблоны копируются в активную концепцию только через утверждённый `issue`.

## Export

Production-export концепции содержит входной README, связанные MD-файлы, `structure.md`, `page_registry.jsonl` и только те attachments, которые являются частью готовой концепции.

Рабочий export со state, QA и issue-историей создаётся отдельным архивом.

## Gate export

Перед export проверяются: закрытые или отдельно помеченные `issue`, linked-связи, достижимость страниц от README, соответствие `structure.md` и `page_registry.jsonl`, согласованность requirements, operating model и process.
