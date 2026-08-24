# General SCRIPT Mechanism Contract

Status: **CANDIDATE SUCCESSOR**

A `SCRIPT` mechanism is deterministic executable tooling used to collect, validate, normalize or evaluate audit evidence without owning audit semantics.

A governed script SHOULD declare:
- mechanism class/version;
- runtime/tool requirements;
- input/output contract;
- deterministic validation behavior where feasible;
- failure/partial-completion behavior;
- provenance emitted with results;
- destructive-operation boundary.

Scripts MUST fail closed on ambiguous governed values where the applicable standard requires exact semantics. Domain-specific scripts belong under `mechanisms/domains/<domain>/script/`.
