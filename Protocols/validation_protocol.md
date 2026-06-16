# Validation protocol

[← Реестр протоколов](protocol_index.md) | [GitHub write](github_write_protocol.md) | [Final check](../Validation/final_check.md)

## Назначение

Validation подтверждает production-состояние через evidence, а не через ярлыки. Статус `passed` допустим только рядом с checked paths, readback, registry/state/events evidence и открытыми рисками.

## Когда запускать

- после каждого write package;
- перед PR merge или documented direct-to-main финальным rework write;
- после merge на base branch;
- перед закрытием issue;
- при cleanup/deletion/debris decision;
- при export readiness claim.

## Evidence matrix

```text
validation_status:
checked_paths:
readback_ref:
failed_checks:
registry_evidence:
state_evidence:
event_evidence:
link_evidence:
language_evidence:
dry_run_evidence:
rollback_conflict_evidence:
persistence_status:
open_risks:
next_safe_step:
```

## Обязательные проверки

| Check | Evidence |
|---|---|
| changed paths | `compare_commits`, PR files, sync-report |
| GitHub readback | `fetch_file` по active branch или base после merge/direct write |
| JSONL validity | каждая строка парсится как JSON object |
| registry match | every production path has registry entry and no active debris path remains |
| navigation/backlinks | root/local entries route every MD page |
| state marker match | `service_state`, `execution_state`, response marker fields align |
| issue events | create/update/delete decisions have event rows |
| language | readable production prose is Russian, allowed technical identifiers documented |
| dry run | Service Mode and Execution Mode scenarios recorded |
| write recovery | write/conflict/rollback protocol has tested decision path |

## Статусы

| Status | Meaning |
|---|---|
| `not_run` | проверка не запускалась |
| `running` | проверка выполняется |
| `passed_with_evidence` | все обязательные checks имеют evidence |
| `passed_with_non_blocking_notes` | checks имеют evidence, есть неблокирующие риски |
| `failed` | есть blocking mismatch |
| `blocked` | нужен внешний шаг или user decision |

## P2-008 evidence replacement gate

Generic labels are not enough. A final or segment check must name:

1. checked paths or explicit absent paths;
2. readback source (`fetch_file`, compare metadata, PR file list, or expected 404);
3. failed checks as `[]` only when each check has evidence;
4. registry/state/event coupling paths;
5. language/navigation evidence paths;
6. persistence status and next safe step.

## No assertion-only closure

Слова `closed`, `passed`, `synced`, `Ready`, `OK` не считаются evidence. Evidence — это конкретный файл, ref, commit, readback, diff, event, registry entry или dry-run result.

## Final gate

Final gate проходит только если D-001…D-063 имеют closure note `fixed_or_resolved` или `removed_with_reason`, а `blocked` отсутствует. Если хотя бы один defect не закрыт evidence, final status становится `failed` или `blocked`.
