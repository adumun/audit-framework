# General Audit Mechanisms

Status: **CANDIDATE SUCCESSOR**  
Predecessor: `cmartinezs/the-x-contract-registry/audits/mechanisms/general/README.md`

This namespace versions mechanism contracts and reusable execution assets that are domain-independent.

## Composition

```text
GENERAL AUDIT STANDARD
        +
GENERAL MECHANISM CONTRACT
        +
DOMAIN PROFILE
        +
DOMAIN MECHANISM IMPLEMENTATION
        ↓
AUDIT EXECUTION / RECORD
```

## Canonical candidate classes

`PROMPT | SCRIPT | AGENT | CI_WORKFLOW | MANUAL_CHECKLIST | QUERY | SCANNER | HYBRID`

## General vs domain-specific

Assets belong under `general/` only when reusable without knowing the audited subject's domain semantics.

Valid general concerns include provenance/evidence capture, generic execution envelopes, common output metadata, retry/failure/partial-completion behavior and version-identification rules.

Conversation dispositions, repository conformance rules, domain scanners and other subject semantics belong under `mechanisms/domains/<domain>/`.

## Versioning

Reusable mechanism packages MUST expose a version when behavior affects reproducibility or analytics. Domain implementations MUST identify the inherited general mechanism version when one exists.

General mechanism evolution MUST NOT silently change domain audit semantics.
