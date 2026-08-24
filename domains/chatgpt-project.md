# Audit Domain Profile — ChatGPT Project

Status: **CANDIDATE SUCCESSOR / PILOT**  
Domain ID: `chatgpt-project`  
Inherits: `standards/audit-standard.md`  
Predecessor: `cmartinezs/the-x-contract-registry/audits/domains/chatgpt-project.md`

This profile applies the ADÜMÜN General Audit Standard to ChatGPT Projects, their conversations and the knowledge that emerges across those conversations.

## 1. Domain purpose

Determine whether a ChatGPT Project is coherently organized and whether its conversations contain fragmented, duplicated, misplaced, superseded or at-risk knowledge that should be reconciled or persisted elsewhere.

## 2. Domain principles

1. A ChatGPT Project is a work/context container, not automatically the canonical project entity.
2. A conversation is evidence of exploration/execution, not canonical knowledge by default.
3. One conversation may contain multiple independent knowledge branches.
4. Conversation placement and knowledge placement are separate questions.
5. Archive readiness depends on preservation of relevant knowledge, not conversation age.
6. Deduplication must preserve lineage/provenance.
7. Repeated conversational claims are not automatically canonical; authoritative persistence must be checked.
8. Cross-project/transversal knowledge must be surfaced rather than forced into the current container.

## 3. Pilot workflow

```text
P1   Conversation structure audit
P1b  Persistence / read-model projection
P2   Knowledge branch extraction + lineage
P3   Canonical reconciliation            (planned)
P4   Cleanup / remediation plan           (planned)
P5   Execute + verify                     (planned)
```

These labels describe the current pilot workflow, not mandatory mechanism identities. Prompts, scripts, agents or hybrid mechanisms may implement equivalent stages while preserving the same domain semantics.

## 4. Conversation dispositions

Candidate controlled vocabulary:

`KEEP | KEEP_BUT_RENAME | REPOSITION | SPLIT | MERGE | MOVE | PROMOTE_TO_PROJECT | ARCHIVE | ARCHIVE_AFTER_CONSOLIDATION | REVIEW_MANUALLY`

Vocabulary changes that affect analytics require explicit version evolution.

## 5. Knowledge-branch lifecycle

Candidate controlled vocabulary:

`EMERGING | EXPLORING | PROPOSED | ACCEPTED | CANONICAL | IMPLEMENTED | VALIDATED | PAUSED | REJECTED | SUPERSEDED | OBSOLETE | UNCERTAIN`

Important distinctions:

`ACCEPTED != CANONICAL != IMPLEMENTED != VALIDATED`

## 6. Expected outputs

Depending on stage and mechanism, machine-readable projections may include:

- conversation inventory/disposition;
- conversation health;
- knowledge-risk register;
- knowledge branches;
- duplicate clusters;
- contradiction register;
- lineage relationships;
- archive readiness;
- cross-project/transversal findings;
- canonical reconciliation candidates;
- recommended actions.

Generated projections do not become canonical project knowledge merely because they are machine-readable.

## 7. Evidence sources

Depending on availability and scope, evidence may include:

- ChatGPT Project conversations;
- prior audit outputs;
- Google Drive files/folders;
- project repositories/source code;
- portfolio/knowledge registries;
- decisions, standards, roadmaps and canonical-state artifacts;
- other authoritative project/domain sources.

Source precedence follows the audited initiative/domain authority model. Conversation recency does not override stronger authority by default.

## 8. Mechanisms

The first real implementation is prompt-based. Its predecessor source is `cmartinezs/the-x-contract-registry/prompts/project-governance/`.

During this migration, those prompts are rehomed under:

`mechanisms/domains/chatgpt-project/prompt/`

They are mechanisms only. They do not define this domain or the general audit framework.

Future scripts, agents, connector scanners or hybrid pipelines must inherit this profile and the general audit standard.

## 9. Remediation boundary

P1 and P2 are observational/extractive. They must not automatically archive conversations, merge ChatGPT Projects, delete Drive folders, rewrite canonical project state or perform other destructive remediation.

Changes belong to explicit later remediation stages with authorization, evidence and verification.

## 10. Authority status

This profile remains a **CANDIDATE SUCCESSOR / PILOT** until its mechanisms, persisted artifacts and repeated executions demonstrate compatibility in the new Audit Framework bounded context.
