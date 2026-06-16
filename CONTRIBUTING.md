
FILE: CONTRIBUTING.md

# Contributing

AD-ORDINEM is currently in early public specification stage.

Contributions are welcome where they improve clarity, terminology, examples, validation logic, security review, or implementation-neutral documentation.

## Contribution Areas

Useful contributions include:

* terminology corrections;
* documentation improvements;
* security review notes;
* Kubernetes governance examples;
* validation schema suggestions;
* issue triage;
* roadmap feedback;
* non-sensitive reference implementations.

## Boundaries

Please do not submit:

* production secrets;
* customer-specific infrastructure data;
* proprietary deployment material;
* unsafe automation;
* destructive shell commands;
* privileged Kubernetes operations without clear safety notes.

## Review Standard

Contributions should preserve the project’s core principles:

* determinism;
* auditability;
* rollback safety;
* explicit governance boundaries;
* separation between architectural intent and runtime mutation;
* implementation-neutral clarity.

---

FILE: docs/architecture-overview.md

# Architecture Overview

AD-ORDINEM is a deterministic governance architecture for Kubernetes and Linux infrastructure.

It separates structural governance from runtime mutation and treats infrastructure change as a versioned, inspectable, and reversible governance event rather than as a loose operational side effect.

## Problem Statement

Modern Kubernetes environments frequently combine controllers, GitOps tools, scripts, CI pipelines, templates, and manual procedures. These layers may be individually useful, but together they can make it difficult to establish a single authoritative path for infrastructure intent, change, evidence, rollback, and accountability.

AD-ORDINEM responds to this problem by defining an external governance model in which structural authority is declared, versioned, reviewed, and evidenced outside the runtime plane.

## Architectural Axes

### Shell-TerRing

Shell-TerRing is the external operational foundation intended to preserve governance continuity independently from the runtime state.

### External Governance Model

The External Governance Model separates governance authority from in-cluster execution and constrains infrastructure mutation through declared, reversible, and inspectable pathways.

### Philologic Operative Language

The Philologic Operative Language is the declarative grammar through which infrastructure is described, reviewed, versioned, and governed.

## Governance Objectives

AD-ORDINEM aims to support:

* deterministic change records;
* rollback-aware infrastructure evolution;
* change-coupled evidence;
* explicit governance boundaries;
* reduced controller sprawl;
* inspectable operational traceability;
* safer security review for privileged workflows.

## Current Repository Scope

This repository publishes public, non-sensitive specification material and example artifacts.

The reference implementation is being prepared separately and will be published progressively when the public boundary is stable.

---

FILE: docs/non-goals.md

# Non-Goals

This repository is intentionally limited in scope.

## Not a Production Distribution

The repository does not currently provide production-ready automation.

## Not a Replacement for Kubernetes Security Review

AD-ORDINEM is a governance architecture and specification. It does not replace standard Kubernetes hardening, secrets management, access control, network policy, vulnerability scanning, or incident-response practices.

## Not a Generic GitOps Wrapper

AD-ORDINEM is not intended to be a cosmetic wrapper around existing GitOps tools. Its focus is structural governance, declared change units, rollback semantics, evidence generation, and separation between governance authority and runtime mutation.

## Not a Disclosure of Sensitive Implementation Details

This public repository deliberately excludes private implementation details, unsafe operational scripts, secrets, customer-specific material, and premature automation.

## Not Legal, Compliance, or Audit Advice

The repository may discuss auditability, evidence, governance, and compliance-adjacent infrastructure concepts. It does not provide legal, compliance, or audit advice.
