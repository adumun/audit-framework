# AGENTS.md

## Purpose
This repository is the canonical version-control home for the ADÜMÜN Audit Framework once migration cutover is complete.

## Mandatory rules
1. Audit semantics are governed by accepted standards/domain profiles, not by prompts, scripts, agents, CI jobs or provider tooling.
2. Historical audit evidence is immutable. Never rewrite an earlier observation to reflect remediation or later knowledge.
3. Re-audits receive new IDs and preserve predecessor/supersession lineage.
4. `UNKNOWN` is preferred over invented evidence.
5. General audit rules compose with domain-specific rules; domain profiles may add constraints but not silently weaken general requirements.
6. Mechanisms are versioned generally and by domain.
7. Validation must remain executable locally when technically possible. GitHub-hosted Actions are not mandatory evidence under verified financial/provider constraints.
8. Provider unavailability must not be misreported as a subject defect.
9. Material changes use branches and PRs.
10. Do not accumulate dependent PRs in the same workstream. Merge/close prerequisite PR N before opening PR N+1 unless an explicit stacked/parallel exception documents dependency, merge order and conflict handling.
11. Migration does not create authority automatically; preserve predecessor links and migration coverage evidence.
12. Jira/MCP is deferred until post-migration operating maturity and must never become audit semantic authority.
