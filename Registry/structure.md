# Структура production-репозитория

[← К главной точке входа](../README.md) | [Реестр страниц](page_registry.jsonl)

```text
Concept-Builder/
├── README.md
├── Instructions/
│   ├── concept_builder_execution_instructions.md
│   └── concept_builder_service_instructions.md
├── Protocols/
│   ├── protocol_index.md
│   ├── protocol_registry.jsonl
│   ├── bootstrap_context_protocol.md
│   ├── context_loading_protocol.md
│   ├── mode_boundary_protocol.md
│   ├── command_parsing_protocol.md
│   ├── persistence_event_protocol.md
│   ├── state_transition_protocol.md
│   ├── github_write_protocol.md
│   ├── navigation_validation_protocol.md
│   ├── response_marker_protocol.md
│   ├── issue_lifecycle_protocol.md
│   ├── issue_intake_protocol.md
│   ├── issue_registry_decision_protocol.md
│   ├── issue_focus_protocol.md
│   ├── issue_prioritization_protocol.md
│   ├── qa_protocol.md
│   ├── requirements_protocol.md
│   ├── solution_contract_protocol.md
│   ├── execution_protocol.md
│   ├── complex_issue_protocol.md
│   ├── linked_issue_protocol.md
│   ├── closure_cleanup_protocol.md
│   ├── concept_network_export_protocol.md
│   └── script_policy_protocol.md
├── State/
│   ├── state_schema.md
│   ├── service_state.md
│   └── execution_state.md
├── Issues/
│   ├── README.md
│   ├── issue_registry.jsonl
│   ├── issue_events.jsonl
│   └── templates/
│       ├── README.md
│       ├── issue_state_template.md
│       ├── reason_template.md
│       ├── question_answer_template.md
│       ├── requirements_template.md
│       ├── solution_template.md
│       ├── contract_template.md
│       ├── output_template.md
│       └── report_template.md
├── Concepts/
│   ├── README.md
│   └── templates/
│       ├── README.md
│       ├── concept_readme_template.md
│       ├── about_template.md
│       ├── requirements_template.md
│       ├── operating_model_template.md
│       ├── process_template.md
│       ├── structure_template.md
│       └── page_registry_template.jsonl
├── Inbox/
│   └── README.md
└── Registry/
    ├── structure.md
    ├── page_registry.jsonl
    └── validation_report.md
```

`Scripts/` отсутствует в базовой реализации. Решение о production-скриптах описано в [`Protocols/script_policy_protocol.md`](../Protocols/script_policy_protocol.md): скрипт создаётся только через отдельный `issue`, requirements, solution, contract и проверку.
