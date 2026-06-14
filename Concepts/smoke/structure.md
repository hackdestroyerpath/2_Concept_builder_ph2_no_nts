# Smoke structure

[← Smoke](README.md) | [Registry](page_registry.jsonl)

```text
smoke/
├── README.md
├── concept_state.md
├── structure.md
├── page_registry.jsonl
├── purpose.md
├── requirements.md
├── operating_model.md
├── process.md
├── output.md
└── export.md
```

## Removed paths

| Path | Reason |
|---|---|
| `o2.md` | orphan/stub, не входит в concept template и не имеет linked registry role |
| `output.txt` | не является production markdown page |
| `e.txt` | не является production export page |

## Integrity rule

Локальное дерево считается валидным только если `page_registry.jsonl` содержит те же production pages, backlinks и owner `Execution Mode`.
