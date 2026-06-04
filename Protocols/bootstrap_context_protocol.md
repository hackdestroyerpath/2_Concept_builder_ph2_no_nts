# Протокол bootstrap и загрузки контекста

[← К реестру протоколов](protocol_index.md)

## Цель

Восстановить минимальный рабочий контекст без загрузки всего репозитория.

## Шаги

1. Определить проект `ChatGPT`: `Concept Builder Service Mode` или `Concept Builder`.
2. Загрузить входную страницу режима: `README.md` для `Service Mode`, `Concepts/README.md` для `Execution Mode`.
3. Загрузить соответствующий state: `State/service_state.md` или `State/execution_state.md`.
4. Загрузить `Protocols/protocol_index.md`.
5. Определить `active_mode`, `active_object`, `active_issue`, `dialogue_state`, `allowed_read_scope`, `allowed_write_scope`.
6. Выбрать один следующий протокол по state/action.
7. Зафиксировать `loaded_context` в ответном marker.

## Уровни контекста

| Уровень | Правило |
|---|---|
| `mandatory` | state режима, активный `issue`, protocol index |
| `local` | файлы текущего объекта или текущей концепции |
| `referenced` | только файлы, явно указанные в state, contract или dependency |
| `optional` | только если повышает качество и причина названа |
| `excluded` | чужой режим, весь репозиторий, закрытая история без ссылки |

## Выход

Обновлённый рабочий контекст и следующий протокол. Если режим неясен, агент не пишет файлы и возвращает `persistence_status: blocked`.
