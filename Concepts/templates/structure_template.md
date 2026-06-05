# Structure `{concept_id}`

[← К концепции](README.md) | [Page registry](page_registry.jsonl)

```text
Concepts/{concept_id}/
├── README.md
├── about.md
├── requirements.md
├── operating_model.md
├── process.md
├── structure.md
├── page_registry.jsonl
└── attachments/
```

## Navigation rules

- `README.md` является входной точкой концепции.
- Каждый MD-файл имеет обратную ссылку на README или ближайший parent.
- `page_registry.jsonl` содержит запись для каждой страницы концепции.
- Attachments входят в production-export только если на них есть ссылка из MD-файлов.

## Validation

| Check | Status | Notes |
|---|---|---|
| README links to core pages | pending |  |
| backlinks exist | pending |  |
| registry matches files | pending |  |
| requirements linked to model/process | pending |  |
