# Contributing

AD-ORDINEM is currently in early public specification stage.

Contributions are welcome where they improve clarity, terminology, examples, validation logic, security review, or implementation-neutral documentation.

## Contribution Areas

Useful contributions include:

- terminology corrections;
- documentation improvements;
- security review notes;
- Kubernetes governance examples;
- validation schema suggestions;
- issue triage;
- roadmap feedback;
- non-sensitive reference implementations.

## Boundaries

Please do not submit:

- production secrets;
- customer-specific infrastructure data;
- proprietary deployment material;
- unsafe automation;
- destructive shell commands;
- privileged Kubernetes operations without clear safety notes;
- private implementation details not intended for public release.

## Review Standard

Contributions should preserve the project’s core principles:

- determinism;
- auditability;
- rollback safety;
- explicit governance boundaries;
- separation between architectural intent and runtime mutation;
- implementation-neutral clarity.

## Security-Sensitive Contributions

If a contribution concerns privileged shell execution, Kubernetes permissions, secrets boundaries, rollback, backup, restore, or governance authority, it should be treated as security-sensitive and reviewed conservatively.
