# Архитектура состояния

[← Реестр протоколов](protocol_index.md) | [Загрузка контекста](context_loading.md) | [Маркер ответа](response_marker.md) | [Service state](../State/service_state.md) | [Execution state](../State/execution_state.md)

## Назначение

Этот протокол задаёт единую модель состояния `Concept Builder`. State нужен как исполнимый контракт между режимом, загруженным контекстом, разрешённой областью записи, текущим `issue`, проверкой и маркером ответа.

## Источники состояния

| Файл | Режим | Назначение | Владелец |
|---|---|---|---|
| `State/service_state.md` | `Service Mode` | Состояние обслуживания системы, протоколов, реестров, validation и сервисных `issue`. | `Service Mode` |
| `State/execution_state.md` | `Execution Mode` | Состояние выбранной концепции внутри `Concepts/`, её local registry, output/export и связанного execution issue. | `Execution Mode` |

State другого режима читается как referenced context и меняется только при явном transfer, repair issue или service patch, где target path указан в контракте.

## Canonical schema

Каждый state-файл обязан содержать эти поля в блоке `text`.

| Поле | Обязательность | Смысл |
|---|---|---|
| `state_id` | обязательно | Уникальный технический идентификатор state snapshot. |
| `owner` | обязательно | Режим-владелец state-файла. |
| `active_mode` | обязательно | Активный режим: `Service Mode` или `Execution Mode`. |
| `active_object` | обязательно | Объект работы: production repo, selected concept или конкретная область. |
| `active_issue` | обязательно | Текущий `issue` или `none`, если issue ещё не создан. |
| `status` | обязательно | Рабочий статус без финального closure-claim. |
| `mode_owner` | обязательно | Режим, которому принадлежит текущая запись. |
| `mode_boundary_status` | обязательно | Проверка, что действие не смешивает области записи. |
| `dialogue_state` | обязательно | Где находится диалог/исполнение: executing, waiting, blocked, recovery. |
| `current_focus` | обязательно | Краткая формулировка текущей цели. |
| `current_stage` | обязательно | Технический stage текущего шага. |
| `required_protocols` | обязательно | Протоколы, которые должны быть загружены для действия. |
| `loaded_context_scope` | обязательно | Файлы, фактически загруженные для текущего шага. |
| `loaded_protocols` | обязательно | Протоколы, фактически прочитанные/использованные. |
| `allowed_read_scope` | обязательно | Допустимые области чтения. |
| `allowed_write_scope` | обязательно | Допустимые области записи. |
| `persistence_status` | обязательно | Состояние записи/readback: `not_written`, `written_unverified`, `readback_required`, `partial`, `blocked`, `conflict`, `failed`. Финальные ярлыки без evidence запрещены. |
| `updated_at` | обязательно | Дата обновления state. |
| `next_step` | обязательно | Следующий ограниченный шаг. |
| `return_anchor` | обязательно | Файл, с которого безопасно продолжать. |

Дополнительные поля разрешены, если они уточняют ветку, базовый SHA, instruction metadata, validation или export readiness и не конфликтуют с canonical schema.

## Mapping state ↔ response marker

| Поле маркера ответа | Canonical state source | Правило |
|---|---|---|
| `mode` | `active_mode` | Значение должно совпадать дословно. |
| `active_object` | `active_object` | Для Service — production repo; для Execution — выбранная концепция. |
| `active_issue` | `active_issue` | Не подменять `none` фиктивным issue. |
| `stage` | `current_stage` | В маркере используется короткое имя `stage`, в state — canonical `current_stage`. |
| `loaded_context` | `loaded_context_scope` | Не заявлять файлы, которые не были прочитаны. |
| `persistence_status` | `persistence_status` | Не использовать `synced`, `passed`, `Ready`, `OK` без readback/evidence. |
| `next_step` | `next_step` | Следующий bounded step, а не весь roadmap. |
| `return_anchor` | `return_anchor` | Должен указывать существующий production-файл. |

## Правила обновления

1. Перед чтением дополнительных файлов агент читает state активного режима и `Protocols/protocol_index.md`.
2. Перед записью агент сверяет `allowed_write_scope` с каждым target path.
3. Если действие меняет state, `issue`, registry или validation, эти изменения фиксируются в одном bounded patch segment.
4. После успешной записи агент перечитывает изменённые файлы из `GitHub` и обновляет `Validation/sync_report.md`.
5. `persistence_status` не может быть финальным без readback, registry/state/event coupling и validation evidence.
6. Если state противоречит команде пользователя или target path принадлежит другому режиму, агент создаёт transfer route, фиксирует `blocked`/`partial` и не пишет в чужой scope.

## Ошибки состояния

| Ошибка | Действие |
|---|---|
| `active_mode` не совпадает с target path | остановить запись, route через `mode_routing.md` |
| `active_issue` отсутствует для write-задачи | создать или восстановить issue через `issue_lifecycle.md` |
| `loaded_context_scope` не покрывает target | дочитать контекст до write |
| `current_stage` и marker `stage` расходятся | обновить state/marker, не объявлять финал |
| `next_step` ведёт мимо dependency | зафиксировать блокировку и return-anchor |

## P2-003 verification notes

P2-003 фиксирует canonical mapping между `state`, `mode`, `context_loading` и response marker. Полная финальная приёмка остаётся за P2-010: этот протокол задаёт контракт, а не объявляет весь репозиторий готовым.
