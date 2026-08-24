# ADÜMÜN Repository Audit Standard

Status: **CANDIDATE SUCCESSOR**  
Domain: `repository`  
Inherits: `standards/audit-standard.md`  
Predecessor: `cmartinezs/the-x-contract-registry/standards/repository-audit-standard.md`  
Audit record schema: `0.2.0`

This standard specializes the ADÜMÜN General Audit Standard for repositories.

## Domain principle

Audit the repository that actually exists before prescribing the repository that theoretically should exist. Determine **applicability** before measuring **conformance**.

## Audit sequence

1. identity & disposition;
2. nature & bounded context;
3. applicable repository standards/profiles;
4. discoverability;
5. repository structure;
6. governance & authority;
7. contracts & integrations;
8. engineering quality;
9. security & operational safety;
10. automation & agents;
11. documentation lifecycle;
12. reuse/extraction signals;
13. legacy/deprecation signals;
14. good local patterns;
15. action classification.

## Applicability

Use exactly one where required:

- `REQUIRED`
- `APPLICABLE`
- `RECOMMENDED`
- `NOT_APPLICABLE`
- `DEFERRED`

For each applicable requirement use:

- `PASS`
- `PARTIAL`
- `FAIL`
- `NOT_APPLICABLE`
- `UNKNOWN`

`UNKNOWN` is preferred over invented evidence.

## Evidence states

Use the general vocabulary:

- `CONFIRMED`
- `EVIDENCED`
- `INFERRED`
- `PROVISIONAL`
- `UNKNOWN`

## Finding severity

- `CRITICAL`
- `HIGH`
- `MEDIUM`
- `LOW`
- `INFO`

## Action priority

- `P0_NOW`
- `P1_NEXT`
- `P2_WHEN_USEFUL`
- `P3_DEFER`
- `NO_ACTION`

Severity and priority remain independent.

## Evidence rules

Non-trivial findings should reference concrete repository evidence: files, folders, workflows, contracts, metadata, issues, PRs, commits or authoritative contrast sources.

Do not infer absence merely from a conventional filename being missing. Search for semantic equivalents first.

Do not certify lifecycle, authority, consumer or deprecation relationships from naming alone.

Repository audit records must identify audited snapshot commit and observed default branch when technically applicable.

## Hosted CI financial bypass

Repository audits inherit the general financial-bypass rule. A hosted CI job that cannot start solely because of billing/payment/spending constraints is not itself repository non-conformance. Equivalent local validation of the exact revision remains required when reproducible.

## Preserve-before-replace

Before recommending standardization, ask whether the repository already solves the problem another way, whether the local pattern is safer/more mature, whether replacement would break consumers or erase provenance, and whether the standard should learn from the repository.

If so, prefer standard feedback/candidate evolution over forced normalization.

## Repository standardization maturity

- `R0 IDENTIFIED`
- `R1 DISCOVERABLE`
- `R2 MACHINE_READABLE`
- `R3 VALIDATED`
- `R4 INTEGRATED`
- `R5 GOVERNED_EVOLUTION`

This is repository-standardization maturity only; it does not replace Initiative Lifecycle state.

## Audit record shape

New repository audits use `auditVersion: 0.2.0` and must be compatible with `schemas/repository-audit-record.v0.2.schema.json` once that schema is accepted.

Historical records retain original audit versions. Re-audits receive new IDs and preserve predecessor/supersession lineage.

## Remediation

Default flow:

`AUDIT → REVIEW FINDINGS → SELECT REMEDIATION → IMPLEMENT → VALIDATE → RE-AUDIT OR RECORD REMEDIATION`

Small low-risk fixes may be executed only under explicit bounded authorization and must not erase original findings.

## Standard evolution feedback

Repository audits may produce feedback such as:

- new profile/standard candidate;
- requirement clarification;
- overly strict requirement;
- missing machine-readable field;
- useful existing local pattern;
- overlapping/duplicate standard.

Standard evolution follows the applicable governance lifecycle rather than becoming policy directly from an audit finding.
