# ADÜMÜN Audit Framework

Canonical version-control home for ADÜMÜN audit framework definitions, domain profiles, mechanisms, schemas, templates, audit registry and retained audit evidence.

Status: **CURRENT / LEGACY CUTOVER COMPLETE FOR AUDIT SCOPE**

Predecessor/incubation source: `cmartinezs/the-x-contract-registry`.

Audit semantics are provider/tool neutral. Prompts, scripts, agents, CI jobs or manual procedures are execution mechanisms, not independent audit authorities.

## Canonical structure

- `standards/` — general and domain audit semantics.
- `domains/` — domain profiles that compose with the general standard.
- `mechanisms/` — general mechanism contracts and domain implementations.
- `schemas/` — current and historical-compatible machine contracts.
- `templates/` — current audit record templates.
- `registry/audits.yaml` — operational audit program registry.
- `evidence/historical/` — immutable migrated audit evidence.
- `migration/` — cutover manifests and coverage evidence.
- `validators/validate.py` — deterministic local validation entry point.

## Validate locally

```bash
python -m pip install -r requirements-dev.txt
python validators/validate.py
```

GitHub-hosted Actions are not required when provider billing/financial constraints prevent execution. Equivalent local validation remains the preferred replay path. Historical evidence must never be rewritten merely to satisfy a newer representation.

## Historical evidence rule

Migrated audit records from `cmartinezs/the-x-contract-registry` preserve their original bytes and Git blob identity. Current registries may point to their new ADÜMÜN locations, but historical observations remain immutable and retain their original audit IDs, versions and semantics.

## Remaining predecessor scope

This cutover covers the **audit bounded context** only. The legacy repository remains active for other responsibilities until governance registries, contract registries/schemas and other remaining scopes complete their own cutovers.
