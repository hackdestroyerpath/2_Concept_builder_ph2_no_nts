#!/usr/bin/env python3
"""Read-only validator for Concept Builder production repository.

Checks navigation, JSONL, registries, protocol paths, state markers and
forbidden temporary artifacts. The script does not write files or perform
network calls.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from urllib.parse import unquote

LINK_RE = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
URL_RE = re.compile(r"^[a-zA-Z][a-zA-Z0-9+.-]*:")

REQUIRED_PATHS = [
    "README.md",
    "State/service_state.md",
    "State/execution_state.md",
    "State/state_schema.md",
    "Protocols/protocol_index.md",
    "Protocols/protocol_registry.jsonl",
    "Protocols/navigation_validation_protocol.md",
    "Protocols/script_policy_protocol.md",
    "Registry/page_registry.jsonl",
    "Registry/structure.md",
    "Issues/README.md",
    "Issues/issue_registry.jsonl",
    "Issues/issue_events.jsonl",
    "Scripts/README.md",
    "Scripts/validation/README.md",
    "Scripts/validation/validate_repository.py",
]

FORBIDDEN_NAME_PARTS = [
    "checkpoint",
    "handoff",
    "executor_handoff",
    "impl_step",
    "tmp_report",
    "temporary_report",
]
FORBIDDEN_SUFFIXES = {".zip", ".tar", ".tgz", ".gz", ".7z", ".rar"}
SKIP_DIRS = {".git", "__pycache__", ".pytest_cache", ".mypy_cache", ".ruff_cache"}


@dataclass
class Result:
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)

    def error(self, message: str) -> None:
        self.errors.append(message)

    def warn(self, message: str) -> None:
        self.warnings.append(message)


def repo_files(root: Path) -> list[Path]:
    files: list[Path] = []
    for path in root.rglob("*"):
        rel_parts = path.relative_to(root).parts
        if any(part in SKIP_DIRS for part in rel_parts):
            continue
        if path.is_file():
            files.append(path)
    return sorted(files)


def rel(path: Path, root: Path) -> str:
    return path.relative_to(root).as_posix()


def parse_jsonl(path: Path, result: Result) -> list[dict]:
    records: list[dict] = []
    if not path.exists():
        result.error(f"Missing JSONL file: {path.as_posix()}")
        return records
    for line_no, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        line = raw.strip()
        if not line:
            continue
        try:
            value = json.loads(line)
        except json.JSONDecodeError as exc:
            result.error(f"Invalid JSONL at {path.as_posix()}:{line_no}: {exc.msg}")
            continue
        if not isinstance(value, dict):
            result.error(f"JSONL record is not an object at {path.as_posix()}:{line_no}")
            continue
        records.append(value)
    return records


def resolve_link(source: Path, href: str, root: Path) -> Path | None:
    raw = href.strip()
    if not raw or raw.startswith("#") or URL_RE.match(raw):
        return None
    if raw.startswith("<") and raw.endswith(">"):
        raw = raw[1:-1].strip()
    raw = raw.split()[0].split("#", 1)[0]
    if not raw:
        return None
    raw = unquote(raw)
    if raw.startswith("/"):
        return (root / raw.lstrip("/")).resolve()
    return (source.parent / raw).resolve()


def inside(path: Path, root: Path) -> bool:
    try:
        path.relative_to(root)
        return True
    except ValueError:
        return False


def template_context(path: str) -> bool:
    name = Path(path).name
    return "/templates/" in path or name.endswith("_template.md")


def validate_required(root: Path, result: Result) -> None:
    for item in REQUIRED_PATHS:
        if not (root / item).exists():
            result.error(f"Required production path missing: {item}")


def validate_forbidden(root: Path, files: list[Path], result: Result) -> None:
    for path in files:
        file_rel = rel(path, root)
        lowered = file_rel.lower()
        if any(part in lowered for part in FORBIDDEN_NAME_PARTS):
            result.error(f"Forbidden temporary artifact committed: {file_rel}")
        if path.suffix.lower() in FORBIDDEN_SUFFIXES:
            result.error(f"Forbidden archive artifact committed: {file_rel}")


def validate_jsonl(root: Path, files: list[Path], result: Result) -> None:
    for path in files:
        if path.suffix.lower() == ".jsonl":
            parse_jsonl(path, result)


def validate_markdown(root: Path, files: list[Path], result: Result) -> None:
    root_resolved = root.resolve()
    existing = {rel(path, root) for path in files}
    for path in files:
        if path.suffix.lower() != ".md":
            continue
        file_rel = rel(path, root)
        text = path.read_text(encoding="utf-8")
        for match in LINK_RE.finditer(text):
            href = match.group(1)
            target = resolve_link(path, href, root)
            if target is None:
                continue
            if not inside(target, root_resolved):
                result.error(f"Markdown link escapes repository: {file_rel} -> {href}")
                continue
            if target.is_dir():
                target = target / "README.md"
            target_rel = target.relative_to(root_resolved).as_posix()
            if target_rel not in existing:
                message = f"Broken markdown link: {file_rel} -> {href} ({target_rel})"
                if template_context(file_rel):
                    result.warn(message)
                else:
                    result.error(message)
        if file_rel != "README.md" and "←" not in text:
            result.warn(f"Markdown file has no visible parent marker: {file_rel}")


def validate_page_registry(root: Path, files: list[Path], result: Result) -> None:
    existing = {rel(path, root) for path in files}
    records = parse_jsonl(root / "Registry/page_registry.jsonl", result)
    seen: set[str] = set()
    for i, record in enumerate(records, start=1):
        path = record.get("path")
        if not isinstance(path, str) or not path:
            result.error(f"page_registry record {i} has no string path")
            continue
        if path in seen:
            result.error(f"Duplicate page_registry path: {path}")
        seen.add(path)
        if path not in existing:
            result.error(f"page_registry path does not exist: {path}")
        parent = record.get("parent")
        if parent and parent not in existing:
            result.error(f"page_registry parent missing for {path}: {parent}")
        for key in ("children", "cross_links", "backlinks"):
            values = record.get(key, [])
            if not isinstance(values, list):
                result.error(f"page_registry {path}.{key} is not a list")
                continue
            for value in values:
                if value not in existing:
                    result.error(f"page_registry {path}.{key} missing target: {value}")


def validate_protocol_registry(root: Path, result: Result) -> None:
    records = parse_jsonl(root / "Protocols/protocol_registry.jsonl", result)
    seen: set[str] = set()
    for i, record in enumerate(records, start=1):
        protocol_id = record.get("protocol_id")
        path = record.get("path")
        if not isinstance(protocol_id, str) or not protocol_id:
            result.error(f"protocol_registry record {i} has no protocol_id")
        elif protocol_id in seen:
            result.error(f"Duplicate protocol_id: {protocol_id}")
        else:
            seen.add(protocol_id)
        if not isinstance(path, str) or not path:
            result.error(f"protocol_registry record {i} has no path")
        elif not (root / path).exists():
            result.error(f"protocol_registry path missing: {path}")


def validate_state(root: Path, result: Result) -> None:
    markers = ("active_mode:", "persistence_status:", "next_step:", "return_anchor:")
    for item in ("State/service_state.md", "State/execution_state.md"):
        path = root / item
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        for marker in markers:
            if marker not in text:
                result.error(f"State file {item} is missing marker {marker}")


def run(root: Path) -> Result:
    root = root.resolve()
    result = Result()
    files = repo_files(root)
    validate_required(root, result)
    validate_forbidden(root, files, result)
    validate_jsonl(root, files, result)
    validate_markdown(root, files, result)
    validate_page_registry(root, files, result)
    validate_protocol_registry(root, result)
    validate_state(root, result)
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate Concept Builder production repository invariants.")
    parser.add_argument("--root", default=".", help="Repository root. Defaults to current directory.")
    args = parser.parse_args()
    result = run(Path(args.root))
    if result.warnings:
        print("WARNINGS:")
        for warning in result.warnings:
            print(f"- {warning}")
    if result.errors:
        print("ERRORS:")
        for error in result.errors:
            print(f"- {error}")
        print("validation_status: failed")
        return 1
    print("validation_status: valid")
    return 0


if __name__ == "__main__":
    sys.exit(main())
