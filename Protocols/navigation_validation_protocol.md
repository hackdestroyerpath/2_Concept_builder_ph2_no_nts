# Протокол проверки навигации

[← К реестру протоколов](protocol_index.md) | [Page registry](../Registry/page_registry.jsonl)

## Цель

Проверять, что production-файлы достижимы, имеют назначение и не висят отдельными островками.

## Проверки

1. Каждый MD-файл, кроме корневого `README.md`, имеет parent.
2. Каждый вложенный MD-файл содержит обратную ссылку на parent или ближайший индекс.
3. `Registry/page_registry.jsonl` содержит запись для каждого production-файла, который участвует в навигации.
4. Ссылки в README, state, protocols и registry ведут на существующие production-пути.
5. `children`, `backlinks` и `cross_links` в registry не противоречат фактическим ссылкам.
6. Рабочие checkpoint-и, архивы задания и промежуточные отчёты не появляются в production registry.

## Выход

```text
navigation_status: valid | warnings | failed
orphan_files: []
broken_links: []
registry_mismatches: []
next_fix:
```

## Когда запускать

- после создания или удаления страницы;
- после изменения README, protocol index, state schema или registry;
- перед финальным validation report;
- перед export концепции.
