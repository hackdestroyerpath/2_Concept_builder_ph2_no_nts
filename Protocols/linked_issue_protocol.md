# Протокол связанных `issue`

[← К реестру протоколов](protocol_index.md)

## Цель

Описывать зависимости между самостоятельными `issue` без смешения их локальных контекстов.

## Типы связей

| Тип | Значение |
|---|---|
| `blocked_by` | текущий `issue` ждёт другой `issue` |
| `blocks` | текущий `issue` нужен другому `issue` |
| `uses_output_of` | текущий `issue` использует результат другого `issue` |
| `related_to` | смысловая связь без блокировки |
| `duplicates_or_overlaps` | возможное пересечение задач |

## Запись связи

```yaml
relation_id: LINK-...
source_issue:
target_issue:
relation_type:
blocking: true | false | conditional
required_output_ref:
unblock_condition:
status: active | resolved | obsolete
reason:
```

## Процесс

1. Загрузить state текущего `issue` и краткое summary target issue.
2. Не загружать полную историю target issue без прямой причины.
3. Записать связь в state текущего `issue` и registry.
4. Если связь блокирующая, поставить `dependency_status: waiting_dependency`.
5. После появления нужного output обновить связь и пересчитать следующий шаг.
6. Каждое изменение связи фиксировать в events.

## Выход

Обновлённые state, registry, event и безопасный следующий `issue` или переход к выполнению.
