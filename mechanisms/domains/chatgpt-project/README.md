# ChatGPT Project Audit Mechanisms

Status: **CANDIDATE / PILOT**

Domain: `chatgpt-project`  
Domain profile: `domains/chatgpt-project.md`

The initial mechanism family is prompt-based and migrated from the legacy incubation package `cmartinezs/the-x-contract-registry/prompts/project-governance/`.

Current pilot stages:
- P1 — conversation structure audit;
- P1b — persistence/read-model projection to Google Drive;
- P2 — knowledge-branch extraction and lineage.

These prompts are execution mechanisms only. General/domain audit semantics remain owned by `standards/audit-standard.md` and `domains/chatgpt-project.md`.

No mechanism in this package may archive/delete conversations, mutate canonical project state, delete Drive files or perform other destructive remediation unless a later explicitly authorized remediation stage permits it.
