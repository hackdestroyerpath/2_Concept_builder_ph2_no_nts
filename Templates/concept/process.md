# Процесс

[← Концепция](README.md) | [Операционная модель](operating_model.md)

## Основной поток

```text
trigger:
steps:
decisions:
outputs:
validation:
```

## Исключения

```text
known_failures:
fallbacks:
manual_review:
```

## Проверка

Процесс готов, когда шаги можно выполнить без скрытых решений и каждый выход связан с требованиями. Технические ключи в блоках оставлены как поля шаблона.