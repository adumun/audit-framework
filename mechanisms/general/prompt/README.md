# General PROMPT Mechanism Contract

Status: **CANDIDATE SUCCESSOR**

A `PROMPT` mechanism is a versioned instruction package executed by a compatible conversational/agent runtime. It does not own audit semantics.

A governed prompt SHOULD declare:
- mechanism class `PROMPT`;
- mechanism version;
- inherited audit/domain contracts;
- required inputs and accessible sources;
- expected output/evidence contract;
- side-effect/remediation boundary;
- failure/unknown behavior;
- provider/runtime assumptions when material.

Prompts MUST prefer `UNKNOWN` over fabricated evidence and MUST NOT silently perform destructive remediation unless the selected audit workflow explicitly authorizes it.

Domain-specific prompts belong under `mechanisms/domains/<domain>/prompt/` and inherit this contract.
