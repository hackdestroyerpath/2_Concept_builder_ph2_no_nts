# Шаблоны концепции

[← К `Concepts`](../README.md)

`templates/` содержит формы для новой связанной MD-сети концепции. Это не активная концепция, а набор production-шаблонов.

## Состав

| Шаблон | Назначение |
|---|---|
| [`concept_readme_template.md`](concept_readme_template.md) | входной README конкретной концепции |
| [`about_template.md`](about_template.md) | назначение, аудитория и границы |
| [`requirements_template.md`](requirements_template.md) | утверждённые требования и provenance |
| [`operating_model_template.md`](operating_model_template.md) | рабочая модель концепции |
| [`process_template.md`](process_template.md) | процесс развития и проверки концепции |
| [`structure_template.md`](structure_template.md) | карта файлов концепции |
| [`page_registry_template.jsonl`](page_registry_template.jsonl) | машинный реестр страниц концепции |

## Правило использования

Новая концепция создаётся через `issue`: сначала reason и requirements, затем сеть файлов. Шаблоны копируются в `Concepts/{concept_id}/` только после выбора `concept_id` и утверждения contract.
