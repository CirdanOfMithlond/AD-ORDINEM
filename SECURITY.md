# Security Policy

## Security Scope

AD-ORDINEM concerns infrastructure governance, Kubernetes operations, rollback, evidence generation, and operational control boundaries. Even at specification stage, the project is security-relevant because its future implementation may interact with privileged operational paths.

Security-sensitive areas include:

* shell execution;
* Kubernetes manifests;
* CI workflows;
* governance records;
* rollback metadata;
* backup and restore coordination;
* secrets boundaries;
* node and runtime state transitions;
* evidence-pack generation.

## Reporting Security Issues

Please do not open public issues for sensitive vulnerabilities.

Until a dedicated security contact is published, security concerns may be reported to the maintainer by private email.

## Current Security Status

The repository is currently an early public specification and example repository. It does not yet provide a production implementation.

## Security Goals

The project aims to support:

* explicit governance boundaries;
* deterministic change records;
* inspectable rollback paths;
* reduced controller sprawl;
* clearer separation between architectural intent and runtime mutation;
* safer review of privileged operational workflows.

## Non-Goals

This repository does not currently provide production-ready automation.

Do not use public examples as production deployment artifacts without independent review, adaptation, and testing.
