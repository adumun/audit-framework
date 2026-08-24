# P1 — Conversation Audit

Status: **CANDIDATE MIGRATED MECHANISM**  
Domain: `chatgpt-project`  
Mechanism class: `PROMPT`  
Mechanism version: `1.0.0-migrated`  
Predecessor: `cmartinezs/the-x-contract-registry/prompts/project-governance/P1-conversation-audit.md`  
Predecessor blob: `1dd7a770ebbe6b52d42edf469d18757e9ea150f6`

Apply, in order:
1. `standards/audit-standard.md`;
2. `mechanisms/general/prompt/README.md`;
3. `domains/chatgpt-project.md`;
4. this procedure.

Higher-authority rules win on conflict.

## Objective

Perform a complete structural and operational audit of the current ChatGPT Project. Evaluate the set of conversations as a workspace, not as isolated chats.

For every identifiable conversation assign exactly one disposition when evidence supports it:

`KEEP | KEEP_BUT_RENAME | REPOSITION | SPLIT | MERGE | MOVE | PROMOTE_TO_PROJECT | ARCHIVE | ARCHIVE_AFTER_CONSOLIDATION | REVIEW_MANUALLY`

Do not force a classification under uncertainty.

## Required analysis

First reconstruct the project's actual purpose, scope, included initiatives/products, workstreams, canonical artifacts, repositories, Drive locations, decisions/standards, current state, completed work and open work.

Distinguish:
- Project = stable unit of work;
- Workstream = line of work within the project;
- Task = concrete activity;
- Conversation = operational context that may touch one or more of the above.

Then inventory all accessible conversations and capture at minimum:
- current name;
- inferred purpose;
- workstream;
- operational state;
- last significant result;
- open work;
- canonical knowledge presence;
- duplication;
- scope contamination;
- proposed disposition;
- confidence.

Evaluate belonging, current utility, better destination, transversal nature, mixed initiatives/domains, duplication, naming quality, real pending work and unpersisted knowledge.

Explicitly detect:
- omnibus conversations;
- duplicates;
- orphan conversations;
- zombie conversations;
- misplaced work;
- scope contamination;
- knowledge at risk.

## Archive rule

A conversation is `ARCHIVE` only when:
1. objective ended or is no longer relevant;
2. no active pending work remains;
3. important decisions are persisted;
4. reusable knowledge is documented;
5. it is not the only source of truth;
6. no operational reason requires it visible.

If conditions 3–5 are not satisfied, use `ARCHIVE_AFTER_CONSOLIDATION` and identify what must be rescued first.

## Knowledge risk

Mark `KNOWLEDGE_AT_RISK` when relevant decisions, canon, architecture, standards, processes, research, configuration, prompts, roadmaps, URLs/resources, audit results, known debt or materially relevant discarded decisions exist only in conversation history.

## Project health

Use one:

`HEALTHY | HEALTHY_WITH_MINOR_CLEANUP | NEEDS_REORGANIZATION | FRAGMENTED | CONSOLIDATION_REQUIRED`

## Required deliverables

Return in this order:

A. Project Snapshot  
B. Conversation Inventory  
C. Findings  
D. Proposed Conversation Architecture  
E. Redistribution Map  
F. Archive Candidates  
G. Knowledge Recovery  
H. Recommended Actions (`P0`–`P3`)  
I. Final Decision

Final Decision must include counts for each disposition and answer:

> ¿Este Proyecto de ChatGPT está actualmente bien organizado?

with `YES | YES_WITH_CLEANUP | NO`, followed by a maximum five-line explanation.

## Restrictions

- Do not archive merely because a conversation is old.
- Do not preserve merely because it is long.
- Do not assume each conversation is a workstream.
- Do not over-fragment.
- Do not confuse chat history with canonical documentation.
- Do not destroy useful historical information.
- Do not claim consolidation when knowledge only lives in chat.
- Mark inaccessible evidence explicitly.
- Reduce entropy rather than moving it elsewhere.

## Execution mode

This stage is observational audit, not migration or remediation:

`INVENTORY → ANALYZE → CLASSIFY → PROPOSE → PRIORITIZE`

No destructive changes are authorized by P1.
