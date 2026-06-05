# Реестр протоколов

[← К главной точке входа](../README.md) | [Машинный registry](protocol_registry.jsonl)

`protocol_index.md` — человекочитаемый источник истины для выбора протокола по режиму, state и действию. Агент загружает минимальный нужный протокол, а не весь каталог.

## Карточки протоколов

| `protocol_id` | Файл | Режим | Когда загружать | Основной выход |
|---|---|---|---|---|
| `bootstrap_context` | [`bootstrap_context_protocol.md`](bootstrap_context_protocol.md) | общий | старт режима, восстановление state | режим, объект, первичный route |
| `context_loading` | [`context_loading_protocol.md`](context_loading_protocol.md) | общий | выбор объёма контекста | `loaded_context`, return anchor |
| `mode_boundary` | [`mode_boundary_protocol.md`](mode_boundary_protocol.md) | общий | проверка режима и scope | разрешённый read/write scope |
| `command_parsing` | [`command_parsing_protocol.md`](command_parsing_protocol.md) | общий | короткая, числовая или неполная команда | однозначное действие или уточнение |
| `persistence_event` | [`persistence_event_protocol.md`](persistence_event_protocol.md) | общий | изменение state, registry, issue или production-файла | event record |
| `state_transition` | [`state_transition_protocol.md`](state_transition_protocol.md) | общий | любой lifecycle/state-переход | обновлённый state и reason |
| `github_write` | [`github_write_protocol.md`](github_write_protocol.md) | общий | запись production-файла | sync-report |
| `navigation_validation` | [`navigation_validation_protocol.md`](navigation_validation_protocol.md) | общий | проверка ссылок, registry и сирот | navigation status |
| `response_marker` | [`response_marker_protocol.md`](response_marker_protocol.md) | общий | каждый содержательный ответ | marker состояния |
| `issue_lifecycle` | [`issue_lifecycle_protocol.md`](issue_lifecycle_protocol.md) | общий | обзор цепочки `issue` | lifecycle route |
| `issue_intake` | [`issue_intake_protocol.md`](issue_intake_protocol.md) | общий | новый входной материал | proposed issue registry |
| `issue_registry_decision` | [`issue_registry_decision_protocol.md`](issue_registry_decision_protocol.md) | общий | решение по кандидатам `issue` | approved/rejected/discussion route |
| `issue_focus` | [`issue_focus_protocol.md`](issue_focus_protocol.md) | общий | выбор одного `issue` | локальный issue context |
| `issue_prioritization` | [`issue_prioritization_protocol.md`](issue_prioritization_protocol.md) | общий | выбор следующего `issue` | recommended next issue |
| `qa` | [`qa_protocol.md`](qa_protocol.md) | общий | уточнения перед requirements | вопросы/ответы или reason пропуска |
| `requirements` | [`requirements_protocol.md`](requirements_protocol.md) | общий | формирование требований | approved requirements gate |
| `solution_contract` | [`solution_contract_protocol.md`](solution_contract_protocol.md) | общий | план и contract | approved execution contract |
| `execution` | [`execution_protocol.md`](execution_protocol.md) | общий | выполнение simple issue | output и report |
| `complex_issue` | [`complex_issue_protocol.md`](complex_issue_protocol.md) | общий | decomposition крупного issue | child issues и roll-up plan |
| `linked_issue` | [`linked_issue_protocol.md`](linked_issue_protocol.md) | общий | dependency между issue | relation record и unblock route |
| `closure_cleanup` | [`closure_cleanup_protocol.md`](closure_cleanup_protocol.md) | общий | закрытие issue и cleanup | closed issue, roll-up, cleanup candidates |
| `concept_network_export` | [`concept_network_export_protocol.md`](concept_network_export_protocol.md) | `Execution Mode` | развитие или export концепции | связанная MD-сеть или export |

## Минимальная маршрутизация

| Событие или state | Протокол | Обязательный контекст | Контекст вне фокуса |
|---|---|---|---|
| Новый чат или потеря контекста | `bootstrap_context` | инструкция проекта, state режима, этот индекс | весь репозиторий |
| Выбор объёма чтения | `context_loading` | active mode, active object, return anchor | все issues и все concepts |
| Команда может относиться к другому режиму | `mode_boundary` | state, active object, команда | файлы чужого режима |
| Короткая команда | `command_parsing` | `dialogue_state`, `active_menu_id`, последнее меню | догадки без state |
| Изменение state или артефакта | `persistence_event` → `github_write` → `navigation_validation` | affected paths, reason, registry | development/task archive |
| Создание нового `issue` | `issue_intake` | input, `Inbox/`, registry, events | закрытая история без ссылки |
| Решение по кандидатам | `issue_registry_decision` | registry, reason выбранных issue | unrelated issues |
| Выбор существующего `issue` | `issue_focus` | issue state, reason, parent-chain | вся папка Issues |
| Требуются уточнения | `qa` | reason, issue state, input refs | unrelated attachments |
| Нужны требования | `requirements` | reason, QA, input refs | solution до gate |
| Нужен план выполнения | `solution_contract` | approved requirements, dependencies, scope | execution до approval |
| Выполнение simple issue | `execution` | approved contract, affected paths | действия вне contract |
| Выполнение complex issue | `complex_issue` | parent requirements, decomposition plan | циклический parent-chain |
| Dependency | `linked_issue` | relation summary и required output | полная история другого issue |
| Закрытие | `closure_cleanup` | output, report, registry, parent-chain | cleanup без provenance |
| Export концепции | `concept_network_export` | concept README, local registry, state | рабочий state в production export |
| Ответ пользователю | `response_marker` | текущий state и sync status | лишний локальный контекст |

## Машинный registry

Файл [`protocol_registry.jsonl`](protocol_registry.jsonl) содержит компактные записи `protocol_id`, `path`, `mode`, `stage` и `next` для автоматической проверки маршрутов.

## Правило расширения

Новый протокол создаётся только если у него есть отдельный триггер, отдельные входы/выходы или отдельный набор state-изменений. Иначе раздел добавляется в существующий протокол.
