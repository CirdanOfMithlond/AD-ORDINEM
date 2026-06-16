# AD-ORDINEM

AD-ORDINEM is a public technical specification and reference architecture for deterministic governance of Kubernetes and Linux infrastructure.

The project addresses a recurring problem in modern platform engineering: infrastructure change is often executed through fragmented controllers, scripts, templates, CI/CD layers, GitOps patterns, and manual procedures that make intent, mutation, rollback, evidence, and accountability difficult to reconstruct as one coherent governance path.

AD-ORDINEM proposes an External Governance Model in which structural authority is kept outside the runtime plane and expressed through versioned governance artifacts, change-coupled evidence, deterministic rollback semantics, and inspectable operational records.

## Public Repository Scope

This repository publishes the public specification layer of AD-ORDINEM.

It currently includes architecture notes, governance model definitions, reference examples, draft governance manifests, change-record structures, public review notes, roadmap material, and contribution guidance.

## Core Concepts

AD-ORDINEM is built around three architectural axes:

- **Shell-TerRing**: an external operational foundation designed to preserve governance execution continuity and resilience independently from runtime state.
- **External Governance Model**: an orchestration paradigm that separates governance authority from in-cluster runtime execution.
- **Philologic Operative Language**: a declarative grammar through which infrastructure can be described, versioned, reviewed, and governed as an inspectable structure.

## Why This Matters

Kubernetes governance, rollback, backup, auditability, release safety, and evidence production are still frequently distributed across multiple tools and operational layers.

AD-ORDINEM aims to make these concerns explicit, deterministic, reviewable, and reusable by treating infrastructure change as a declared, inspectable, and reversible governance event rather than as an opaque operational mutation.

## Current Status

Status: early public specification.

The public layer is intended to make the architecture reviewable and discussable while further work is prepared.

## Repository Contents

- `OPENAI-CODEX-OSS-APPLICATION.md`: application-oriented project brief.
- `REVIEWER_GUIDE.md`: fast review path for evaluators.
- `docs/project-brief.md`: concise project brief.
- `docs/quick-brief.md`: short reviewer summary.
- `docs/use-cases.md`: public use cases.
- `docs/architecture-overview.md`: public architecture overview.
- `docs/public-whitepaper-summary.md`: public summary of the technical white paper.
- `docs/publication-boundary.md`: repository publication scope.
- `docs/non-goals.md`: explicit exclusions and scope limits.
- `docs/threat-model.md`: public review notes.
- `docs/governance-artifact-schema.md`: artifact structure notes.
- `examples/README.md`: examples directory guide.
- `examples/change-record.yaml`: illustrative change-record artifact.
- `examples/minimal-governance-manifest.yaml`: illustrative governance manifest.
- `schemas/README.md`: schema roadmap.
- `SECURITY.md`: security scope and reporting policy.
- `ROADMAP.md`: staged public roadmap.
- `CONTRIBUTING.md`: contribution boundaries and review standard.
- `MAINTAINERS.md`: maintainer information.
- `CHANGELOG.md`: public specification change log.
- `NOTICE`: project notice and license boundary.

## Planned Work

- publish additional public governance examples;
- define validation rules for governance artifacts;
- define rollback and evidence-pack structures;
- add documentation consistency checks;
- progressively convert the public specification into usable implementation-neutral open-source assets.

## Intended Audience

- platform engineers;
- SRE teams;
- DevOps engineers;
- Kubernetes operators;
- infrastructure architects;
- security and compliance engineers;
- maintainers working on governance, rollback, drift, auditability, and infrastructure evidence.

## License

Code examples and public reference artifacts are licensed under Apache-2.0.

Specification text, documentation, terminology, architectural descriptions, and white-paper-derived material are copyright Luca Arrighi unless expressly stated otherwise.

## Maintainer

This repository is maintained by Luca Arrighi as the primary maintainer of the AD-ORDINEM architecture.
