# General AGENT Mechanism Contract

Status: **CANDIDATE SUCCESSOR**

An `AGENT` mechanism is an autonomous or semi-autonomous executor operating under explicit audit standards, domain rules and authorization boundaries.

A governed agent SHOULD declare:
- mechanism class/version;
- inherited audit/domain contracts;
- tools/data sources it may access;
- observation vs remediation permissions;
- approval requirements for side effects;
- evidence/provenance output;
- stop/failure/escalation behavior.

Autonomy does not create authority. Agents MUST NOT silently broaden scope, invent evidence or perform destructive remediation outside explicit authorization.

Domain-specific agents belong under `mechanisms/domains/<domain>/agent/`.
