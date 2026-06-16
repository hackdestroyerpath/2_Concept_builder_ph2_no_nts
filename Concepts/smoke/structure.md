# Структура `smoke`

[← Проверочный пример](README.md) | [Реестр](page_registry.jsonl)

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

## Удалённые пути

| Путь | Причина |
|---|---|
| `o2.md` | несвязанный или пустой файл; не входит в шаблон концепции и не имеет роли в локальном реестре |
| `output.txt` | не является рабочей Markdown-страницей |
| `e.txt` | не является рабочей страницей экспорта |

## Правило целостности

Локальное дерево считается валидным только если `page_registry.jsonl` содержит те же рабочие страницы, обратные ссылки и владельца `Execution Mode`.