#!/usr/bin/env python3
from pathlib import Path
import sys

REQUIRED_FILES = [
    "README.md",
    "LICENSE",
    "SECURITY.md",
    "ROADMAP.md",
    "CONTRIBUTING.md",
    "NOTICE",
    "OPENAI-CODEX-OSS-APPLICATION.md",
    "REVIEWER_GUIDE.md",
    "docs/project-brief.md",
    "docs/quick-brief.md",
    "docs/use-cases.md",
    "docs/architecture-overview.md",
    "docs/public-whitepaper-summary.md",
    "docs/non-goals.md",
    "docs/threat-model.md",
    "docs/governance-artifact-schema.md",
    "examples/change-record.yaml",
    "examples/minimal-governance-manifest.yaml",
]

CHECKS = {
    "README.md": ["deterministic governance", "Kubernetes", "Repository Contents"],
    "examples/change-record.yaml": ["apiVersion:", "kind: ChangeRecord", "metadata:", "spec:"],
    "examples/minimal-governance-manifest.yaml": ["apiVersion:", "kind: GovernanceManifest", "metadata:", "spec:"],
}


def main() -> int:
    errors = []

    for item in REQUIRED_FILES:
        path = Path(item)
        if not path.is_file():
            errors.append(f"missing: {item}")
        elif not path.read_text(encoding="utf-8").strip():
            errors.append(f"empty: {item}")

    for item, markers in CHECKS.items():
        path = Path(item)
        if path.is_file():
            content = path.read_text(encoding="utf-8")
            for marker in markers:
                if marker not in content:
                    errors.append(f"missing marker in {item}: {marker}")

    if errors:
        print("Validation failed")
        for error in errors:
            print(error)
        return 1

    print("Validation passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
