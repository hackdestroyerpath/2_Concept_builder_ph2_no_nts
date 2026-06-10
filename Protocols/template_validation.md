# Template validation

[← Реестр протоколов](protocol_index.md) | [Validation protocol](validation_protocol.md) | [Templates](../Templates/README.md)

## Назначение

Протокол задаёт проверку production-шаблонов перед их использованием. Шаблон считается готовым только если его можно безопасно скопировать, заполнить и проверить без скрытых решений.

## Область проверки

```text
Templates/concept/
Templates/issue/
Registry/page_registry.jsonl
Registry/page_registry_schema.md
```

## Проверки concept template

```text
required_files_present:
local_page_registry_valid:
internal_links_ok:
placeholders_known:
instantiation_rules_defined:
execution_state_compatible:
export_validation_compatible:
```

## Проверки issue template

```text
required_files_present:
artifact_roles_defined:
question_answer_ready:
requirements_ready:
solution_contract_report_ready:
attachments_manifest_ready:
issue_lifecycle_compatible:
```

## Placeholder policy

Placeholder допустим в шаблоне, если при инстанцировании есть правило его замены или он явно разрешён на стадии `draft`.

Минимальные placeholder-ы:

```text
{{issue_id}}
{{concept_id}}
{{concept_title}}
{{status}}
{{owner_issue}}
```

## Статусы

| Статус | Значение |
|---|---|
| `template_valid` | Шаблон готов к использованию. |
| `template_valid_with_notes` | Шаблон готов, но есть неблокирующие замечания. |
| `template_invalid` | Есть блокирующая ошибка. |
| `not_checked` | Проверка не запускалась. |

## Выход

Результат проверки фиксируется в отчёте агента, `Issues/issue_events.jsonl` и, если нужно, в state активного режима.
