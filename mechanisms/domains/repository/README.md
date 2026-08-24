# Repository Audit Mechanisms

Status: **CANDIDATE SUCCESSOR**  
Domain: `repository`

This namespace contains repository-domain implementations of general audit mechanism classes.

Repository mechanisms inherit, in order:
1. `standards/audit-standard.md`;
2. the applicable general mechanism class contract under `mechanisms/general/`;
3. `standards/domains/repository.md`;
4. the concrete mechanism implementation/version.

Repository scanners, validators, prompts or agents must audit actual repository evidence, preserve snapshot/revision provenance, respect applicability before conformance and distinguish provider-financial unavailability from engineering failure.

The mixed legacy `scripts/validate_registry.py` is **not** copied here wholesale because it spans audit, governance and contract-registry responsibilities. It will be split by bounded context during later migration waves.
