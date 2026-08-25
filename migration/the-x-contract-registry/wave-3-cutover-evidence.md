# MIG-TXCR-AUD-003 — Historical Evidence & Registry Cutover

Status: **PASS_WITH_ENVIRONMENT_LIMITATION**  
Date: 2026-08-24  
Source repository: `cmartinezs/the-x-contract-registry`  
Successor repository: `adumun/audit-framework`

## Scope

This wave migrates the historical repository-audit evidence set and the operational audit registry together so referential integrity is preserved during cutover.

Migrated historical records:

- `AUD-001--cmartinezs--the-x-contract-registry.yaml`
- `AUD-002--cmartinezs--the-x-contract-registry.yaml`
- `AUD-003--cmartinezs--powerful-brain.yaml`

Migrated registry:

- `registry/audits.yaml`

Historical compatibility schema:

- `schemas/legacy/repository-audit-record.v0.1.schema.json`

Current schemas:

- `schemas/repository-audit-record.v0.2.schema.json`
- `schemas/audit-registry.v0.2.schema.json`

## Byte-preservation evidence

Historical evidence was copied without semantic rewriting. Git blob SHA was compared between predecessor and successor.

| Audit | Legacy blob SHA | Successor blob SHA | Result |
|---|---|---|---|
| AUD-001 | `a47cf61ac6f2d46e9ec0965fbcc0abc0ac16031a` | `a47cf61ac6f2d46e9ec0965fbcc0abc0ac16031a` | PASS |
| AUD-002 | `04865b3b0166e0870c69da5ac24fbec05bfab938` | `04865b3b0166e0870c69da5ac24fbec05bfab938` | PASS |
| AUD-003 | `a68f754f328699ed7f571842b3d776c857301d00` | `a68f754f328699ed7f571842b3d776c857301d00` | PASS |

Matching Git blob SHA establishes byte-for-byte identity of the retained historical records.

## Registry reconciliation

The successor registry preserves the existing audit IDs and queue semantics while changing artifact references from the legacy `audits/...` namespace to the retained successor paths under:

`evidence/historical/the-x-contract-registry/`

The registry therefore points to existing retained artifacts and does not redefine the historical audit observations.

## Validation contract

`validators/validate.py` now covers:

1. current JSON Schema structural validity;
2. legacy v0.1 schema structural validity;
3. repository-audit template validation;
4. migrated historical records against their declared audit version;
5. audit registry against `audit-registry.v0.2.schema.json`;
6. duplicate audit IDs in retained evidence;
7. registry artifact existence;
8. registry auditId ↔ artifact auditId consistency;
9. registry repository ↔ artifact repository consistency.

YAML date objects produced by `yaml.safe_load` are normalized **in memory only** to ISO strings for JSON Schema validation. Historical files are not rewritten.

## Environment limitation

The ChatGPT container used for this migration cannot resolve `github.com`, so a fresh network clone and execution of the repository-local validator could not be performed from that container. This is recorded as an environment limitation, not as PASS evidence from a command that did not run.

Compensating cutover evidence available in this execution:

- GitHub branch contents were read directly through the installed GitHub integration;
- all three historical blob SHAs match the predecessor byte-for-byte;
- the successor registry was inspected after creation and points to the new retained evidence namespace;
- the validation contract itself is versioned in the successor repository.

A normal local checkout SHOULD execute:

```bash
python -m pip install -r requirements-dev.txt
python validators/validate.py
```

before future material audit-framework changes. This limitation does not justify rewriting or discarding preserved historical evidence.

## Cutover decision

**Audit framework historical evidence and audit-registry scope: READY_FOR_SUCCESSOR_CUTOVER.**

After this wave is merged:

- new audit-framework work belongs in `adumun/audit-framework`;
- the migrated audit scope in `cmartinezs/the-x-contract-registry` becomes `SUPERSEDED` for new normative/operational writes;
- legacy copies remain retained as predecessor history until the entire repository migration is complete;
- the legacy repository itself is **not yet globally deprecated**, because governance registries/contracts and remaining machine-contract scopes still require migration/cutover.
