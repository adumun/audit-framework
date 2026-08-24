# MIG-TXCR-AUD-002 — Audit Migration Wave 2 Coverage

Status: **PASS_WITH_OPEN_WORK**  
Date: 2026-08-24

## Scope

Wave 2 establishes the execution architecture required before historical audit evidence and the operational audit registry can move without broken references.

Migrated/adapted:
- `domains/chatgpt-project.md`;
- `mechanisms/README.md`;
- `mechanisms/general/README.md`;
- general `PROMPT`, `SCRIPT`, `AGENT` mechanism contracts;
- repository-domain mechanism namespace;
- ChatGPT Project mechanism package;
- migrated P1, P1b and P2 prompt implementations with predecessor blob provenance;
- repository audit record v0.2 template;
- audit registry v0.2 JSON Schema under ADÜMÜN namespace;
- deterministic local validator and development dependencies.

## Semantic coverage

### ChatGPT Project domain
Preserved:
- project container != canonical project entity;
- conversation != canonical knowledge;
- multi-branch conversation model;
- conversation placement vs knowledge placement separation;
- archive only after knowledge preservation;
- lineage-preserving deduplication;
- transversal/cross-project surfacing;
- P1/P1b/P2 pilot stages and non-destructive boundary;
- disposition and knowledge-lifecycle vocabularies.

### Mechanism model
Preserved:
- mechanism != semantic authority;
- two-level general/domain versioning;
- canonical mechanism classes;
- inheritance precedence;
- explicit evidence/provenance and side-effect boundaries;
- prompts/scripts/agents as interchangeable implementation classes subject to the same audit semantics.

### Prompt migration
P1, P1b and P2 are adapted successor mechanisms rather than byte-for-byte copies. Each retains the exact predecessor path and blob SHA. The adaptation removes obsolete legacy paths and binds execution to the new ADÜMÜN standard/domain/mechanism hierarchy while preserving substantive pilot semantics.

### Template / registry schema
- repository audit template retains v0.2 sentinel semantics and predecessor provenance;
- audit registry schema moves artifact references from legacy `audits/...` to `evidence/historical|current/...`;
- registry itself is intentionally NOT migrated in Wave 2 because its current artifact references still point to legacy audit records.

## Validation evidence

Executed locally against the candidate schema/template semantics:
- `schemas/repository-audit-record.v0.2.schema.json` → JSON Schema Draft 2020-12 check: PASS;
- `schemas/audit-registry.v0.2.schema.json` → JSON Schema Draft 2020-12 check: PASS;
- `templates/repository-audit-record.v0.2.yaml` against repository audit schema → PASS.

The first validation run correctly exposed a YAML typing defect: unquoted `auditedAt: 1970-01-01` was parsed as a date object rather than a schema string. The template was corrected to `auditedAt: "1970-01-01"` and the validation then passed.

## Open work / Wave 3 gate

Wave 3 must migrate, atomically enough to preserve references:
- historical audit records, preserving content/provenance;
- legacy v0.1 audit schema compatibility;
- `registry/audits.yaml` with the same audit IDs and corrected artifact paths;
- current/historical evidence namespace;
- referential-integrity validation between registry and evidence;
- focused campaigns/subplans where their evidence relationships require it.

Until Wave 3 passes, legacy audit evidence/registry remain authoritative historical/operational sources for their existing records.
