# Шаблоны `issue`

[← К Issues](../README.md)

`templates/` содержит production-шаблоны артефактов lifecycle. Они используются как форма, а не как активные `issue`.

## Состав

| Шаблон | Когда использовать |
|---|---|
| [`issue_state_template.md`](issue_state_template.md) | создание `Issues/{issue_id}/state.md` |
| [`reason_template.md`](reason_template.md) | создание `reason.md` перед регистрацией issue |
| [`question_answer_template.md`](question_answer_template.md) | QA stage или reason пропуска QA |
| [`requirements_template.md`](requirements_template.md) | requirements gate |
| [`solution_template.md`](solution_template.md) | solution review |
| [`contract_template.md`](contract_template.md) | contract approval |
| [`output_template.md`](output_template.md) | результат выполнения |
| [`report_template.md`](report_template.md) | проверка output и закрытие |

## Правило

Шаблон копируется в папку конкретного `issue` только когда этот артефакт реально нужен lifecycle-переходу. Пустые пользовательские `issue` не создаются для красоты, потому что декоративная бюрократия уже достаточно размножилась без нашей помощи.
