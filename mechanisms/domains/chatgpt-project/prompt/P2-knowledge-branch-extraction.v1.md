# P2 — Knowledge Branch Extraction & Lineage Audit

Status: **CANDIDATE MIGRATED MECHANISM**  
Domain: `chatgpt-project`  
Mechanism class: `PROMPT`  
Mechanism version: `1.0.0-migrated`  
Predecessor: `cmartinezs/the-x-contract-registry/prompts/project-governance/P2-knowledge-branch-extraction.md`  
Predecessor blob: `89f89015157210ffe5b4fde589fa57441a22185e`

Apply, in order:
1. `standards/audit-standard.md`;
2. `mechanisms/general/prompt/README.md`;
3. `domains/chatgpt-project.md`;
4. this extraction procedure.

P2 assumes P1 evidence exists. It audits semantic knowledge across conversations; it does not repeat P1 unless required to interpret evidence.

## Fundamental unit

`1 conversation != 1 topic`.

The minimum unit of analysis is the **KNOWLEDGE BRANCH**: an independently meaningful idea, decision, requirement, capability, feature, architecture choice, standard, process, research result, assumption, constraint, risk, task, roadmap item, canon element, asset, experiment or open question.

## Objectives

- extract and normalize knowledge branches;
- preserve origin/occurrences;
- classify type and lifecycle state;
- detect duplicates, overlaps and contradictions;
- reconstruct lineage;
- determine project fit and candidate canonical destination;
- identify knowledge at risk;
- surface transversal knowledge and emerging initiatives;
- produce machine-readable reusable evidence.

## Branch types

`IDEA | DECISION | REQUIREMENT | CAPABILITY | FEATURE | ARCHITECTURE | STANDARD | PROCESS | RESEARCH | ASSUMPTION | CONSTRAINT | RISK | TASK | ROADMAP_ITEM | CANON | ASSET | EXPERIMENT | OPEN_QUESTION | OTHER`

Avoid `OTHER` where a specific type applies.

## Branch lifecycle

`EMERGING | EXPLORING | PROPOSED | ACCEPTED | CANONICAL | IMPLEMENTED | VALIDATED | PAUSED | REJECTED | SUPERSEDED | OBSOLETE | UNCERTAIN`

Never collapse `ACCEPTED`, `CANONICAL`, `IMPLEMENTED` and `VALIDATED` into the same meaning.

## Stable identity

Use stable IDs independent of titles, for example `BR-<PROJECT>-0001`. Renaming does not create a new branch identity.

A branch record should retain:
- stable ID/type/title/summary/status/confidence;
- origin and occurrences;
- project-fit classification;
- canonicality/evidence/source;
- relationships;
- knowledge-risk flag/severity;
- recommended action/destination.

## Relationships

Prefer specific relations:

`DERIVED_FROM | REFINES | EXTENDS | REPLACES | SUPERSEDES | IMPLEMENTS | VALIDATES | REJECTS | CONTRADICTS | OVERLAPS | DUPLICATES | DEPENDS_ON | ENABLES | RELATED_TO`

Use `RELATED_TO` only when a more precise relation is not justified.

## Deduplication

Classify candidate clusters as:

`EXACT_DUPLICATE | SEMANTIC_DUPLICATE | OVERLAPPING | EVOLUTION | INDEPENDENT`

Do not erase origins. When consolidation is justified, preserve all predecessor occurrences/lineage.

Do not treat similar branches as duplicates until intention, domain, actor, time, scope, outcome, constraints and dependencies have been compared.

## Contradictions

Classify contradictions as:

`RESOLVED | UNRESOLVED | POSSIBLE_CONFLICT`

Do not pick a winner without evidence. Consider authority, time, explicit decisions, implementation and supersession.

## Knowledge at risk

Flag material branches existing only in conversation history, especially decisions, canon, architecture, standards, critical requirements and rationale.

Priority:
- `P0` loss could cause contradiction, incorrect implementation or loss of fundamental canon;
- `P1` important knowledge needing near-term consolidation;
- `P2` reusable/historical value;
- `P3` optional value.

## Scope / destination

Project-fit scope:

`PROJECT | TRANSVERSAL | OTHER_PROJECT | NEW_INITIATIVE | UNCERTAIN`

Candidate destination examples:

`PROJECT_CANON | PROJECT_DOCUMENTATION | PROJECT_ROADMAP | PROJECT_ARCHITECTURE | PROJECT_REQUIREMENTS | PROJECT_REGISTRY | PROJECT_BACKLOG | GITHUB | GOOGLE_DRIVE | PORTFOLIO_STANDARD | SHARED_CAPABILITY | OTHER_PROJECT:<name> | NEW_INITIATIVE | ARCHIVE | NO_PERSISTENCE_NEEDED | UNCERTAIN`

Do not create a new document/initiative for every interesting idea.

## Required views / deliverables

Return in this order:

A. Extraction Summary  
B. Knowledge Branch Inventory  
C. Project Knowledge Map  
D. Duplicate Clusters  
E. Contradiction Register  
F. Lineage Map  
G. Cross-Project / Transversal Findings  
H. Knowledge at Risk  
I. Conversation → Branch Matrix  
J. Archive Readiness  
K. Recommended Canonical Model  
L. `P3_CANONICAL_RECONCILIATION_INPUT`

Archive readiness vocabulary:

`SAFE_TO_ARCHIVE | ARCHIVE_AFTER_BRANCH_PERSISTENCE | KEEP_ACTIVE | KEEP_AS_REFERENCE | REVIEW`

P2 must not archive anything.

## Machine-readable artifact

Produce a stable structured artifact containing at minimum project/execution metadata, metrics, branches, duplicate clusters, contradictions, relationships, knowledge risks, conversation-branch matrix, archive readiness, emerging initiatives, transversal knowledge and recommended actions.

If a prior artifact exists, reconcile identities rather than assigning new IDs to the same branches. Preserve lineage and update state.

## Execution mode

`EXTRACT → NORMALIZE → CLASSIFY → DEDUPLICATE → RELATE → FORMALIZE → ASSESS → PERSIST`

No destructive migration, project merge, conversation archive or document deletion is authorized by P2.

Principle:

**Conversations are evidence of thought/execution; they are not the canonical knowledge model.**
