# ADÜMÜN General Audit Standard

Status: **CANDIDATE SUCCESSOR**  
Predecessor: `cmartinezs/the-x-contract-registry/standards/audit-standard.md`  
Migration: `MIG-TXCR-AUD-001`

This standard defines rules that apply to every formal audit in ADÜMÜN regardless of subject or execution mechanism.

## 1. Audit definition

An audit is a bounded, evidence-backed examination of a subject against explicit rules, expectations, risks or questions, producing durable findings independently reviewable from the execution mechanism.

An audit is not defined by whether it is performed by a person, prompt, script, agent, CI workflow, query or scanner.

## 2. Composition

Every formal audit MUST declare:

1. audited subject and stable subject identity;
2. purpose and scope;
3. explicit non-scope where ambiguity is possible;
4. one or more applicable domain profiles;
5. execution mechanism class and applicable mechanism versions;
6. authoritative sources and source precedence;
7. evidence captured or referenced;
8. findings and uncertainty;
9. recommended actions or explicit no-action outcome;
10. audit identity/version/time;
11. supersession relationship when re-auditing prior evidence.

Concrete executions compose:

```text
GENERAL AUDIT STANDARD
→ GENERAL MECHANISM CONTRACT
→ DOMAIN PROFILE
→ DOMAIN MECHANISM IMPLEMENTATION
→ EXECUTION INPUTS
```

## 3. Evidence epistemic state

Material claims SHOULD use one of:

- `CONFIRMED`
- `EVIDENCED`
- `INFERRED`
- `PROVISIONAL`
- `UNKNOWN`

`UNKNOWN` is preferred over invented evidence.

## 4. Provenance and authority

Every material claim MUST remain traceable to evidence or reasoning source.

Audit registration never transfers semantic authority from the audited bounded context into the audit framework.

## 5. Applicability

General rules apply to all audits. Domain rules apply only when the corresponding domain profile is selected. Audits MUST NOT penalize a subject for a demonstrably non-applicable rule.

## 6. Mechanism independence and versioning

Mechanisms implement audits; they do not own audit semantics.

Mechanisms are versioned at two levels:

1. general mechanism contract;
2. domain mechanism implementation.

Equivalent mechanisms auditing the same domain against equivalent authoritative inputs SHOULD converge on compatible evidence states, findings and decisions.

Mechanism-specific convenience fields MAY exist but MUST NOT silently redefine general/domain vocabulary.

## 7. Historical evidence

Audit evidence is immutable historical observation.

Remediation, validation or later knowledge MUST NOT rewrite an earlier audit as though its original observation had been different. Re-audits receive new identities and MAY supersede earlier records while preserving them.

## 8. Audit versus remediation

Default lifecycle:

```text
AUDIT
→ REVIEW FINDINGS
→ SELECT REMEDIATION
→ IMPLEMENT
→ VALIDATE
→ RE-AUDIT OR RECORD REMEDIATION
```

Audit and remediation are separate concerns unless an explicitly authorized domain/mechanism permits bounded reversible fixes. Such fixes must remain traceable and cannot erase original findings.

## 9. Financial bypass for provider-hosted validation

A provider-hosted validation mechanism, including GitHub Actions, MUST NOT become a mandatory completion gate when unavailable specifically because of a verified billing/financial restriction external to the audited change.

This is a **validation-environment bypass, not a validation bypass**.

When it applies:

- execute the same validation contract locally or in another accepted non-billable environment when technically possible;
- validate the exact revision under review;
- retain commands, environment/tool versions, result, timestamp and revision/commit as durable evidence where material;
- treat local failures as blocking;
- distinguish `HOSTED_VALIDATION_UNAVAILABLE_FINANCIAL` from a real validation failure;
- mark irreproducible provider-only checks `UNKNOWN` or `DEFERRED`, never `PASS` by assumption.

## 10. Contradictions and uncertainty

Audits MUST surface unresolved contradictions instead of selecting a winner without evidence. Conflicting sources SHOULD be evaluated through explicit authority/freshness rules from the applicable domain profile.

## 11. Severity and priority

Severity and action priority are separate dimensions:

- severity = consequence/risk of the finding;
- priority = when action should occur considering consequence, cost, dependencies and context.

## 12. Output and analytics

Formal audits SHOULD produce machine-readable output when repeated aggregation, trend analysis, automation or re-audit comparison is expected. Stable IDs, enums and schema versions SHOULD be preferred over free-form synonyms.

Human-readable reports MAY be companion projections/evidence.

## 13. Authority boundary

This standard governs how audits are conducted and represented. It does not own the canonical truth of the audited domain.

## 14. Minimum completion rule

An audit is complete only when:

- scope and subject are identifiable;
- applicable rules are known;
- mechanism identity/version is known when relevant;
- evidence is sufficient for each material claim or explicitly `UNKNOWN`;
- required validation has passed in an accepted environment when validation applies;
- findings are reviewable;
- historical evidence is persisted or durably referenced;
- destructive remediation has not been silently performed as observation.

## 15. Independent bounded context

The predecessor standard required promotion to an independent repository once evidence demonstrated multiple domains/mechanisms, independent schemas/consumers and a distinct lifecycle. That evidence now exists. `adumun/audit-framework` is therefore the successor bounded context; the former incubation home remains lineage only during migration.

## Successor status

This document remains **CANDIDATE SUCCESSOR** until domain profiles, mechanisms, schemas and audit registry migration complete the framework cutover.
