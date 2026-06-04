# `Inbox`

[← К главной точке входа](../README.md) | [К протоколам](../Protocols/protocol_index.md)

`Inbox/` — временное production-хранилище входных материалов: точки входа и attachments, нужные для создания или обработки `issue`.

## Нормализация пути

Production-путь верхнего уровня: `Inbox/`. Термин `inbox` в протоколах означает этот же рабочий узел, а не отдельную папку `inbox/`.

## Структура входа

```text
Inbox/{input_id}/
├── entrypoint.md
├── attachments/
└── intake_summary.md
```

`input_id` создаётся только при реальном новом входе. Материалы остаются до закрытия связанных `issue` и проверки provenance.
