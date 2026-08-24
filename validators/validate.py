#!/usr/bin/env python3
"""Deterministic local validation for the ADÜMÜN Audit Framework."""
from __future__ import annotations

import datetime as dt
import json
import sys
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
REPO_AUDIT_SCHEMA_V02 = ROOT / "schemas" / "repository-audit-record.v0.2.schema.json"
REPO_AUDIT_SCHEMA_V01 = ROOT / "schemas" / "legacy" / "repository-audit-record.v0.1.schema.json"
AUDIT_REGISTRY_SCHEMA = ROOT / "schemas" / "audit-registry.v0.2.schema.json"
REPO_AUDIT_TEMPLATE = ROOT / "templates" / "repository-audit-record.v0.2.yaml"
AUDIT_REGISTRY = ROOT / "registry" / "audits.yaml"


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def _normalize_yaml_scalars(value):
    """Normalize YAML-native temporal scalars for JSON Schema validation only.

    Historical files are preserved byte-for-byte. PyYAML may deserialize an unquoted
    ISO date as datetime.date; JSON Schema expects the serialized JSON/YAML contract
    value to be a string, so validation operates on the equivalent ISO string in memory.
    """
    if isinstance(value, (dt.datetime, dt.date)):
        return value.isoformat()
    if isinstance(value, dict):
        return {k: _normalize_yaml_scalars(v) for k, v in value.items()}
    if isinstance(value, list):
        return [_normalize_yaml_scalars(v) for v in value]
    return value


def load_yaml(path: Path):
    return _normalize_yaml_scalars(yaml.safe_load(path.read_text(encoding="utf-8")))


def validate_document(document: dict, schema: dict) -> list[str]:
    validator = Draft202012Validator(schema)
    errors = []
    for error in sorted(validator.iter_errors(document), key=lambda e: list(e.path)):
        location = ".".join(str(p) for p in error.absolute_path) or "$"
        errors.append(f"{location}: {error.message}")
    return errors


def report_validation(label: str, document: dict, schema: dict) -> int:
    errors = validate_document(document, schema)
    if errors:
        print(f"FAIL {label}")
        for error in errors:
            print(f"  - {error}")
        return 1
    print(f"PASS {label}")
    return 0


def validate_historical_evidence() -> int:
    failures = 0
    schema_v01 = load_json(REPO_AUDIT_SCHEMA_V01)
    schema_v02 = load_json(REPO_AUDIT_SCHEMA_V02)
    evidence_root = ROOT / "evidence" / "historical"

    audit_ids: dict[str, Path] = {}
    for path in sorted(evidence_root.rglob("*.yaml")):
        try:
            document = load_yaml(path)
            version = document.get("auditVersion")
            audit_id = document.get("auditId")
            schema = schema_v01 if version == "0.1.0" else schema_v02 if version == "0.2.0" else None
            if schema is None:
                print(f"FAIL evidence {path.relative_to(ROOT)}: unsupported auditVersion {version!r}")
                failures += 1
                continue
            failures += report_validation(f"evidence {path.relative_to(ROOT)}", document, schema)
            if audit_id:
                if audit_id in audit_ids:
                    print(f"FAIL duplicate auditId {audit_id}: {audit_ids[audit_id].relative_to(ROOT)} and {path.relative_to(ROOT)}")
                    failures += 1
                else:
                    audit_ids[audit_id] = path
        except Exception as exc:
            print(f"FAIL evidence {path.relative_to(ROOT)}: {exc}")
            failures += 1
    return failures


def validate_registry_and_references() -> int:
    failures = 0
    registry = load_yaml(AUDIT_REGISTRY)
    registry_schema = load_json(AUDIT_REGISTRY_SCHEMA)
    failures += report_validation(f"registry {AUDIT_REGISTRY.relative_to(ROOT)}", registry, registry_schema)

    seen_ids: set[str] = set()
    for item in registry.get("queue", []):
        audit_id = item.get("auditId")
        artifact = item.get("artifact")
        if audit_id:
            if audit_id in seen_ids:
                print(f"FAIL registry duplicate auditId {audit_id}")
                failures += 1
            seen_ids.add(audit_id)
        if artifact:
            path = ROOT / artifact
            if not path.is_file():
                print(f"FAIL registry artifact missing: {artifact}")
                failures += 1
                continue
            evidence = load_yaml(path)
            if evidence.get("auditId") != audit_id:
                print(f"FAIL registry artifact identity: {artifact} contains {evidence.get('auditId')!r}, expected {audit_id!r}")
                failures += 1
            else:
                print(f"PASS registry artifact {audit_id} -> {artifact}")

    for item in registry.get("queue", []):
        source = item.get("supersedesAuditId")
        target = item.get("supersededByAuditId")
        for relation_name, ref in (("supersedesAuditId", source), ("supersededByAuditId", target)):
            if ref and ref not in seen_ids:
                print(f"FAIL registry {relation_name} unresolved: {ref}")
                failures += 1

    return failures


def main() -> int:
    failures = 0
    schemas = [REPO_AUDIT_SCHEMA_V02, REPO_AUDIT_SCHEMA_V01, AUDIT_REGISTRY_SCHEMA]

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
        schema = load_json(REPO_AUDIT_SCHEMA_V02)
        failures += report_validation(f"template {REPO_AUDIT_TEMPLATE.relative_to(ROOT)}", template, schema)
    except Exception as exc:
        print(f"FAIL template validation: {exc}")
        failures += 1

    try:
        failures += validate_historical_evidence()
    except Exception as exc:
        print(f"FAIL historical evidence validation: {exc}")
        failures += 1

    try:
        failures += validate_registry_and_references()
    except Exception as exc:
        print(f"FAIL registry validation: {exc}")
        failures += 1

    if failures:
        print(f"VALIDATION FAILED: {failures} failure(s)")
        return 1
    print("VALIDATION PASSED")
    return 0


if __name__ == "__main__":
    sys.exit(main())
