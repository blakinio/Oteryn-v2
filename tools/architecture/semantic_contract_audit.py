#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import subprocess
from pathlib import Path

E_PATHS = {
    "docs/agents/tasks/active/OTV2-20260815-alpha-client-architecture.md",
    "docs/architecture/ALPHA-CLIENT-01_NATIVE_CLIENT_ARCHITECTURE_ANALYSIS.md",
    "docs/architecture/ALPHA-CLIENT-01_NATIVE_CLIENT_ARCHITECTURE_CONTRACT_CANDIDATE.md",
}
F_PATHS = {
    "docs/agents/tasks/active/OTV2-20260815-analytics-integrity-architecture.md",
    "docs/architecture/ANL-02_GAMEPLAY_BALANCE_WORLD_ANALYTICS_ANALYSIS.md",
    "docs/architecture/ANL-02_GAMEPLAY_BALANCE_WORLD_ANALYTICS_CONTRACT_CANDIDATE.md",
    "docs/architecture/ANL-03_ECONOMY_INTEGRITY_SECURITY_ANALYTICS_ANALYSIS.md",
    "docs/architecture/ANL-03_ECONOMY_INTEGRITY_SECURITY_ANALYTICS_CONTRACT_CANDIDATE.md",
}


def die(message: str) -> None:
    raise SystemExit(f"SEMANTIC_AUDIT_FAIL: {message}")


def git(*args: str) -> str:
    p = subprocess.run(["git", *args], text=True, capture_output=True, check=False)
    if p.returncode:
        die(f"git {' '.join(args)} failed: {p.stderr.strip()}")
    return p.stdout.strip()


def read(path: str) -> str:
    p = Path(path)
    if not p.is_file():
        die(f"required file missing: {path}")
    return p.read_text(encoding="utf-8")


def require(text: str, fragment: str, label: str) -> None:
    if fragment not in text:
        die(f"{label}: missing required semantic fragment: {fragment!r}")


def require_ci(text: str, fragment: str, label: str) -> None:
    if fragment.casefold() not in text.casefold():
        die(f"{label}: missing required semantic fragment: {fragment!r}")


def require_regex(text: str, pattern: str, label: str) -> None:
    if re.search(pattern, text, re.IGNORECASE | re.DOTALL) is None:
        die(f"{label}: required semantic pattern not satisfied: {pattern}")


def forbid_regex(text: str, pattern: str, label: str) -> None:
    if re.search(pattern, text, re.IGNORECASE | re.DOTALL) is not None:
        die(f"{label}: forbidden semantic pattern present: {pattern}")


def audit_common(task: str, expected_gate_cycle: int) -> None:
    require(task, f"repair_cycles_for_current_gate: {expected_gate_cycle}", "task")
    require_ci(task, "no Codex for this continuation", "task")
    require(task, "MERGE_AUTHORITY: ARCHITECTURE_COORDINATOR_ONLY", "task")


def audit_alpha_client() -> list[str]:
    task = read("docs/agents/tasks/active/OTV2-20260815-alpha-client-architecture.md")
    analysis = read("docs/architecture/ALPHA-CLIENT-01_NATIVE_CLIENT_ARCHITECTURE_ANALYSIS.md")
    candidate = read("docs/architecture/ALPHA-CLIENT-01_NATIVE_CLIENT_ARCHITECTURE_CONTRACT_CANDIDATE.md")
    audit_common(task, 4)

    checks: list[tuple[str, str]] = [
        ("ImplementationStatus: `NOT_STARTED`", "implementation truth"),
        ("Runtime authorization: **NONE**", "runtime authority"),
        ("one-time Game Login Ticket", "admission chain"),
        ("Platform-owned Game Gateway", "gateway ownership"),
        ("FND-02 `protocol-oteryn` transport/bootstrap", "protocol boundary"),
        ("final game-owned FND-04 admission", "final admission authority"),
        ("MUST NOT bypass Game Gateway ticket redemption/route selection", "no gateway bypass"),
        ("same accepted **production protocol schemas, production codecs, sequencing and admission contracts**", "tier1 production codec path"),
        ("shared production code MUST NOT be the only oracle", "independent wire oracle"),
        ("visual scene is a **presentation projection**, not a second gameplay/world model", "scene non-authority"),
        ("Audio is a client-side **presentation-only** subsystem", "audio non-authority"),
        ("### 14.1 Oteryn Studio low-level sharing boundary", "Studio boundary"),
        ("low-level, representation-neutral, non-authoritative components", "Studio allowlist principle"),
        ("The following MUST remain product-specific", "Studio product exclusions"),
        ("Dependency direction MUST remain acyclic", "Studio dependency direction"),
        ("authoring-only state MUST be projected/exported through an accepted revisioned content schema", "Studio export seam"),
        ("negative tests proving authoring-only/server-only fields cannot enter the runtime client-safe projection", "Studio negative evidence"),
        ("Every durable setting MUST declare a semantic scope", "settings declared scope"),
        ("`ACCOUNT`", "account scope"),
        ("`OS_USER`", "OS user scope"),
        ("`INSTALLATION`", "installation scope"),
        ("`DEVICE`", "device scope"),
        ("the client MUST treat the account layer as absent rather than inventing local account authority", "account authority fail closed"),
        ("including selected audio output", "hardware device scope"),
        ("the **most restrictive valid privacy choice wins**", "restrictive privacy wins"),
        ("MUST NOT re-enable diagnostics disabled at OS-user/installation policy scope", "privacy precedence"),
        ("requires an explicit versioned migration", "settings migration"),
        ("source scope, destination scope, conflict resolution and rollback/recovery", "migration completeness"),
        ("MUST NOT silently re-enable diagnostics", "diagnostics persistence"),
    ]
    for fragment, label in checks:
        require(candidate, fragment, label)

    for fragment in (
        "Platform Identity -> one-time Game Login Ticket -> Platform-owned Game Gateway",
        "independent FND-02 wire evidence",
        "audio application-owned, bounded and presentation-only",
        "diagnostics opted out -> no automatic upload/retry, no gameplay impact",
    ):
        require(analysis, fragment, "analysis consistency")

    require_regex(
        candidate,
        r"DEVICE\s*\n\s*>\s*OS_USER\s*\n\s*>\s*ACCOUNT\s*\n\s*>\s*product default",
        "deterministic settings precedence",
    )
    require_regex(
        candidate,
        r"shared low-level components MUST NOT depend on `apps/client`, a Studio application root, live-session state or product UI",
        "shared dependency prohibition",
    )
    forbid_regex(
        candidate,
        r"(?:Gateway|Platform)\s+(?:owns|creates|mints)\s+(?:canonical\s+)?(?:GameSessionId|CharacterLease)",
        "forbidden final authority transfer",
    )
    return [
        "admission/gateway/final-game authority",
        "pre-native fail-closed runtime truth",
        "production-codec + independent wire oracle",
        "scene/audio presentation-only authority",
        "ACCOUNT/OS_USER/INSTALLATION/DEVICE settings + deterministic privacy precedence/migration",
        "Studio low-level sharing + acyclic dependency + revisioned client-safe export",
    ]


def audit_analytics_integrity() -> list[str]:
    task = read("docs/agents/tasks/active/OTV2-20260815-analytics-integrity-architecture.md")
    a2 = read("docs/architecture/ANL-02_GAMEPLAY_BALANCE_WORLD_ANALYTICS_ANALYSIS.md")
    c2 = read("docs/architecture/ANL-02_GAMEPLAY_BALANCE_WORLD_ANALYTICS_CONTRACT_CANDIDATE.md")
    a3 = read("docs/architecture/ANL-03_ECONOMY_INTEGRITY_SECURITY_ANALYTICS_ANALYSIS.md")
    c3 = read("docs/architecture/ANL-03_ECONOMY_INTEGRITY_SECURITY_ANALYTICS_CONTRACT_CANDIDATE.md")
    audit_common(task, 4)

    for fragment, label in (
        ("Runtime/client/Platform/PostgreSQL/production authority: **NONE**", "ANL-02 authority"),
        ("NO_MATERIAL_REGRESSION_SUPPORTED` is a **fail-closed disposition**", "fail-closed no-regression"),
        ("REGRESSION_EVIDENCE_INSUFFICIENT", "insufficient-evidence disposition"),
        ("quality/completeness", "quality prerequisite"),
        ("sample/exposure", "sample prerequisite"),
        ("comparability", "comparability prerequisite"),
        ("reconciliation", "reconciliation prerequisite"),
        ("privacy", "privacy prerequisite"),
        ("baseline/method/threshold", "method/provenance prerequisite"),
        ("warning-only green acceptance is forbidden", "warning cannot stay green"),
        ("proof no analytical/dashboard path can mutate gameplay", "read-only negative evidence"),
    ):
        require_ci(c2, fragment, label)

    require_regex(
        c2,
        r"If an evaluation is attempted.*?(?:fails|failed).*?REGRESSION_EVIDENCE_INSUFFICIENT",
        "attempted evaluation failure disposition",
    )
    forbid_regex(
        c2,
        r"PARTIAL.*?NO_MATERIAL_REGRESSION_SUPPORTED.*?(?:allowed|permitted|may)",
        "partial evidence green acceptance",
    )

    for fragment, label in (
        ("Runtime/client/Platform/PostgreSQL/production/enforcement authority: **NONE**", "ANL-03 authority"),
        ("read-only evidence + triage input", "read-only evidence"),
        ("Allowed **substantive evidentiary dispositions**", "substantive dispositions"),
        ("SUPPORTED_INTEGRITY_OR_DEFECT_FINDING", "integrity disposition"),
        ("SUPPORTED_SECURITY_FINDING", "security disposition"),
        ("NOT_SUPPORTED_FALSE_POSITIVE", "false-positive disposition"),
        ("INCONCLUSIVE_INSUFFICIENT_EVIDENCE", "inconclusive disposition"),
        ("DATA_QUALITY_OR_PIPELINE_FAILURE", "pipeline disposition"),
        ("DUPLICATE_OR_ALREADY_COVERED", "duplicate disposition"),
        ("`REFERRED_TO_SECURITY_GM_PRODUCT_OR_ENGINE_OWNER` is **not an evidentiary disposition**", "referral not evidence"),
        ("MUST NOT be the sole terminal analytical classification", "no naked referral"),
        ("preceding substantive disposition", "referral requires substantive outcome"),
        ("referral is never a substitute for evidentiary classification", "lifecycle referral boundary"),
        ("does not imply the target owner accepted", "referral does not imply acceptance"),
        ("does not authorize ban/mute/kick/confiscation/rollback/account action", "no sanction authority"),
        ("immutable audit record", "evidence lifecycle"),
    ):
        require_ci(c3, fragment, label)

    require_ci(a3, "referral is routing", "ANL-03 analysis consistency")
    require_ci(a3, "substantive", "ANL-03 analysis substantive disposition")
    require_ci(a2, "REGRESSION_EVIDENCE_INSUFFICIENT", "ANL-02 analysis consistency")
    require_regex(
        c3,
        r"referral.*?require.*?preceding substantive disposition.*?same review generation",
        "same-generation referral ordering",
    )
    forbid_regex(
        c3,
        r"Allowed \*\*substantive evidentiary dispositions\*\*.*?REFERRED_TO_SECURITY_GM_PRODUCT_OR_ENGINE_OWNER\s*—",
        "referral inside substantive disposition list",
    )
    return [
        "ANL-02 read-only evidence authority",
        "fail-closed no-regression prerequisites and insufficient-evidence disposition",
        "ANL-03 immutable signal/case evidence lifecycle",
        "substantive evidentiary disposition before any referral",
        "false-positive/inconclusive/data-quality outcomes",
        "no sanction/enforcement/mutation authority",
    ]


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--base-sha", required=True)
    ap.add_argument("--head-sha", required=True)
    args = ap.parse_args()

    actual = git("rev-parse", "HEAD").lower()
    expected = args.head_sha.lower()
    if actual != expected:
        die(f"checkout SHA mismatch: actual={actual} expected={expected}")

    changed = set(filter(None, git("diff", "--name-only", f"{args.base_sha}...{args.head_sha}").splitlines()))
    if changed == E_PATHS:
        profile = "ALPHA_CLIENT_01"
        checks = audit_alpha_client()
        verdict = "PASS"
    elif changed == F_PATHS:
        profile = "ANL_02_ANL_03"
        checks = audit_analytics_integrity()
        verdict = "PASS"
    else:
        profile = "NOT_APPLICABLE"
        checks = []
        verdict = "NOT_APPLICABLE"

    result = {
        "method": "dedicated deterministic independent semantic audit workflow",
        "profile": profile,
        "base_sha": args.base_sha,
        "exact_head_sha": args.head_sha,
        "changed_files": sorted(changed),
        "checks": checks,
        "verdict": verdict,
        "ai_service_used": False,
        "owner_funded_ai_used": False,
    }
    rendered = json.dumps(result, indent=2, sort_keys=True)
    print(rendered)
    print(f"SEMANTIC_AUDIT_{verdict}: profile={profile} exact_head={args.head_sha}")

    summary = Path(__import__("os").environ.get("GITHUB_STEP_SUMMARY", ""))
    if str(summary):
        summary.write_text(
            "## Architecture semantic audit\n\n"
            f"- method: dedicated deterministic independent semantic audit workflow\n"
            f"- profile: `{profile}`\n"
            f"- exact head: `{args.head_sha}`\n"
            f"- verdict: **{verdict}**\n"
            f"- owner-funded AI: `false`\n\n"
            + "\n".join(f"- PASS: {item}" for item in checks)
            + "\n",
            encoding="utf-8",
        )


if __name__ == "__main__":
    main()
