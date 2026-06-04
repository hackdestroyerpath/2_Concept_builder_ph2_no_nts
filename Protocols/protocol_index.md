# Реестр протоколов

[← К главной точке входа](../README.md)

`protocol_index.md` — источник истины для выбора протокола по режиму, state и действию. Агент не загружает все протоколы пачкой: он выбирает минимальный нужный файл.

## Карточки протоколов

| `protocol_id` | Файл | Режим | Когда загружать | Основной выход |
|---|---|---|---|---|
| `bootstrap_context` | [`bootstrap_context_protocol.md`](bootstrap_context_protocol.md) | общий | старт режима, восстановление state, потеря контекста | определённый режим, loaded_context, следующий протокол |
| `mode_boundary` | [`mode_boundary_protocol.md`](mode_boundary_protocol.md) | общий | проверка границ режима или transfer | разрешённый scope или остановка |
| `github_write` | [`github_write_protocol.md`](github_write_protocol.md) | общий | любое изменение production-файла, state или registry | sync-report и persistence_status |
| `response_marker` | [`response_marker_protocol.md`](response_marker_protocol.md) | общий | каждый содержательный ответ | единый marker ответа |
| `issue_lifecycle` | [`issue_lifecycle_protocol.md`](issue_lifecycle_protocol.md) | общий | создание, утверждение, обсуждение, выполнение и закрытие `issue` | обновлённые issue state/events |
| `concept_network_export` | [`concept_network_export_protocol.md`](concept_network_export_protocol.md) | `Execution Mode` | развитие или export концепции | связанная MD-сеть или production-export |

## Минимальная маршрутизация

| Событие или state | Протокол | Обязательный контекст | Нельзя загружать без причины |
|---|---|---|---|
| Новый чат или потеря контекста | `bootstrap_context` | инструкция проекта, state режима, этот индекс | весь репозиторий |
| Команда может относиться к другому режиму | `mode_boundary` | state, active_object, команда | файлы чужого режима |
| Нужно записать файл | `github_write` | целевой файл, registry, state, причина записи | development/task archive |
| Создание нового `issue` | `issue_lifecycle` | input, `Inbox/`, registry, events | закрытая история без ссылки |
| Выбор существующего `issue` | `issue_lifecycle` | issue state, reason, parent-chain | unrelated issues |
| Работа с концепцией | `concept_network_export` | входной README концепции, local registry | сервисные протоколы целиком |
| Ответ пользователю | `response_marker` | текущий state и sync status | лишний локальный контекст |

## Правило расширения

Новый протокол создаётся только если у него есть отдельный триггер, отдельные входы/выходы или отдельный набор state-изменений. Иначе раздел добавляется в существующий протокол.
