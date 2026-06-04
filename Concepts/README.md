# `Execution Mode`: концепции

[← К главной точке входа](../README.md) | [Протокол концепций](../Protocols/concept_network_export_protocol.md)

`Concepts/` — входная точка `Execution Mode`. Здесь хранятся конкретные концепции как связанные MD-сети.

## Как выбрать объект работы

1. Если концепция уже существует, открыть её `Concepts/{concept_id}/README.md`.
2. Если концепции нет, создать `issue` на создание концепции через [`../Issues/README.md`](../Issues/README.md).
3. До выбора концепции не писать в `Concepts/{concept_id}/`.

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

## Export

Production-export концепции не включает рабочие `Issues/`, QA-историю, `Inbox/`, checkpoint-и и временные state-файлы. Рабочий export со state создаётся отдельным архивом.
