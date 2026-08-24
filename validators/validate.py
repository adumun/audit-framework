#!/usr/bin/env python3
"""Deterministic local validation for the ADÜMÜN Audit Framework."""
from __future__ import annotations

import json
import sys
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
REPO_AUDIT_SCHEMA = ROOT / "schemas" / "repository-audit-record.v0.2.schema.json"
AUDIT_REGISTRY_SCHEMA = ROOT / "schemas" / "audit-registry.v0.2.schema.json"
REPO_AUDIT_TEMPLATE = ROOT / "templates" / "repository-audit-record.v0.2.yaml"


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def load_yaml(path: Path):
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def validate_document(document: dict, schema: dict) -> list[str]:
    validator = Draft202012Validator(schema)
    errors = []
    for error in sorted(validator.iter_errors(document), key=lambda e: list(e.path)):
        location = ".".join(str(p) for p in error.absolute_path) or "$"
        errors.append(f"{location}: {error.message}")
    return errors


def main() -> int:
    failures = 0
    schemas = [REPO_AUDIT_SCHEMA, AUDIT_REGISTRY_SCHEMA]

    for path in schemas:
        try:
            schema = load_json(path)
            Draft202012Validator.check_schema(schema)
            print(f"PASS schema {path.relative_to(ROOT)}")
        except Exception as exc:
            print(f"FAIL schema {path.relative_to(ROOT)}: {exc}")
            failures += 1

    try:
        template = load_yaml(REPO_AUDIT_TEMPLATE)
        schema = load_json(REPO_AUDIT_SCHEMA)
        errors = validate_document(template, schema)
        if errors:
            print(f"FAIL template {REPO_AUDIT_TEMPLATE.relative_to(ROOT)}")
            for error in errors:
                print(f"  - {error}")
            failures += 1
        else:
            print(f"PASS template {REPO_AUDIT_TEMPLATE.relative_to(ROOT)}")
    except Exception as exc:
        print(f"FAIL template validation: {exc}")
        failures += 1

    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
