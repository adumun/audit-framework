# Audit Execution Mechanisms

Status: **CANDIDATE SUCCESSOR**  
Predecessor: `cmartinezs/the-x-contract-registry/audits/mechanisms/README.md`

An audit mechanism is an implementation used to execute an audit. It is **not** the owner of audit semantics.

## Two-level model

```text
GENERAL MECHANISM CONTRACT
        +
DOMAIN-SPECIFIC IMPLEMENTATION
        ↓
AUDIT EXECUTION
```

- `mechanisms/general/` contains reusable mechanism contracts independent of audited domain.
- `mechanisms/domains/<domain>/` contains domain-specific implementations.

A domain implementation MUST NOT silently redefine general mechanism behavior, and a general mechanism MUST NOT embed domain semantics.

## Mechanism classes

Canonical candidate classes:

- `PROMPT`
- `SCRIPT`
- `AGENT`
- `CI_WORKFLOW`
- `MANUAL_CHECKLIST`
- `QUERY`
- `SCANNER`
- `HYBRID`

Not every class needs an implementation before evidence justifies one.

## Required behavior

Every governed mechanism MUST, when applicable:

1. declare class and version;
2. declare general vs domain-specific scope;
3. domain implementations declare implemented domain(s);
4. inherit the General Audit Standard;
5. obey selected domain profiles;
6. identify authoritative inputs/evidence;
7. preserve provenance;
8. distinguish observation, inference and unknowns;
9. produce reviewable output;
10. avoid silent destructive remediation;
11. preserve compatible machine vocabulary where analytics depend on it;
12. expose mechanism/version identity when reproducibility matters.

## Composition precedence

```text
General Audit Standard
→ General Mechanism Contract
→ Domain Profile
→ Domain Mechanism Implementation
→ Execution parameters / inputs
```

Lower layers may specialize but cannot contradict higher layers without an explicit governed exception/version.

## Versioning

General mechanism contracts and domain implementations version independently. Behavior-changing modifications that affect reproducibility, analytics or evidence interpretation require explicit version evolution.

## Migration rule

Legacy mechanisms are moved with predecessor path/SHA provenance. Moving a prompt or script does not promote it into audit authority.
