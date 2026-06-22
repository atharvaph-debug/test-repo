#!/usr/bin/env python3
"""Enrichment gate: decide whether a metadata change set can auto-merge or needs HITL.

Runs in GitHub Actions on a per-run enrichment branch. For every top-level
project dir that changed (each is a self-contained eval output_dir: it holds
`catalog/`, `catalog.yaml`, and `trajectory.json`), it:

  1. Structurally validates the changed YAML (placeholder for full OKF schema
     validation -- see _validate_okf).
  2. Runs the bundled eval harness in dynamic (golden-free) mode:
     `python -m eval --output-dir <project> --json`.
  3. Applies the decision policy below.

Decision (PASS => eligible for auto-merge, HITL => human review required):
  - HITL if any structural/OKF error.
  - HITL if eval cannot score (no judge auth / error / null average).
  - HITL if any project's average_score < EVAL_THRESHOLD.
  - HITL if any judge metric is flagged failed (below its own gate).
  - else PASS.

Outputs (written to $GITHUB_OUTPUT): decision=pass|hitl, summary=<one line>.
A human-readable report is written to gate_report.md (posted as a PR comment).

Env / args:
  GATE_BASE   base ref to diff against (default: origin/<STAGING_BRANCH> or HEAD~1)
  GATE_HEAD   head ref (default: HEAD)
  EVAL_THRESHOLD  pass threshold for average_score (default 0.7)
  KC_EVAL_MODEL   judge model id (default gemini-2.5-pro)
  GOOGLE_CLOUD_PROJECT / GOOGLE_GENAI_USE_VERTEXAI  needed for the judge
"""

from __future__ import annotations

import json
import os
import subprocess
import sys

THRESHOLD = float(os.environ.get("EVAL_THRESHOLD", "0.7"))
MODEL = os.environ.get("KC_EVAL_MODEL", "gemini-2.5-pro")
REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))


def _git(*args: str) -> str:
  return subprocess.run(
      ["git", *args], cwd=REPO_ROOT, capture_output=True, text=True, check=True
  ).stdout


def _changed_files(base: str, head: str) -> list[str]:
  # Two-dot vs three-dot: use three-dot so we compare against the merge base.
  out = _git("diff", "--name-only", f"{base}...{head}")
  return [l.strip() for l in out.splitlines() if l.strip()]


def _changed_projects(files: list[str]) -> list[str]:
  """Top-level dirs that (a) changed and (b) are eval output_dirs (have catalog/)."""
  projects = set()
  for f in files:
    top = f.split("/", 1)[0]
    if top in (".github", "scripts", "eval"):
      continue
    if os.path.isdir(os.path.join(REPO_ROOT, top, "catalog")) or os.path.isfile(
        os.path.join(REPO_ROOT, top, "catalog.yaml")
    ):
      projects.add(top)
  return sorted(projects)


def _validate_okf(project: str) -> list[str]:
  """Lightweight structural validation of a project's entry YAML.

  Placeholder for full OKF-schema validation (TODO: pull the real validator
  from the source repo). For now: every `*.yaml` under the project parses, and
  each catalog entry yaml declares an id/name; each `*.overview.md` is non-empty.
  """
  import yaml  # local import so the module loads even if pyyaml is absent

  errors: list[str] = []
  proot = os.path.join(REPO_ROOT, project)
  for dirpath, _dirs, names in os.walk(proot):
    for n in names:
      p = os.path.join(dirpath, n)
      rel = os.path.relpath(p, REPO_ROOT)
      if n.endswith(".yaml"):
        try:
          data = yaml.safe_load(open(p, encoding="utf-8")) or {}
        except Exception as e:  # noqa: BLE001
          errors.append(f"{rel}: YAML parse error: {e}")
          continue
        # Entry files (not the top-level catalog.yaml manifest) should be keyed.
        if n != "catalog.yaml" and isinstance(data, dict):
          if not (data.get("id") or data.get("name")):
            errors.append(f"{rel}: entry missing 'id'/'name'")
      elif n.endswith(".overview.md"):
        if not open(p, encoding="utf-8").read().strip():
          errors.append(f"{rel}: empty overview")
  return errors


def _run_eval(project: str) -> dict:
  """`python -m eval --output-dir <project> --json` from the repo root."""
  proc = subprocess.run(
      [sys.executable, "-m", "eval", "--output-dir", project, "--json",
       "--model", MODEL],
      cwd=REPO_ROOT, capture_output=True, text=True,
  )
  if proc.returncode != 0 and not proc.stdout.strip():
    return {"error": (proc.stderr or "eval failed").strip()[-500:]}
  try:
    data = json.loads(proc.stdout)
  except json.JSONDecodeError:
    return {"error": f"could not parse eval JSON: {proc.stdout[-300:]}"}
  return data[0] if isinstance(data, list) else data


def _assess(project: str) -> dict:
  okf = _validate_okf(project)
  ev = _run_eval(project)
  avg = ev.get("average_score")
  failed = [m["name"] for m in ev.get("metrics", []) if m.get("passed") is False]
  reasons = []
  if okf:
    reasons.append(f"{len(okf)} OKF/structural error(s)")
  if "error" in ev:
    reasons.append(f"eval error: {ev['error']}")
  elif avg is None:
    reasons.append("no average_score (judge auth missing?)")
  elif avg < THRESHOLD:
    reasons.append(f"score {avg:.3f} < threshold {THRESHOLD:.2f}")
  if failed:
    reasons.append(f"metrics below gate: {', '.join(failed)}")
  return {
      "project": project, "okf_errors": okf, "average_score": avg,
      "failed_metrics": failed, "eval_error": ev.get("error"),
      "metrics": ev.get("metrics", []), "reasons": reasons,
      "passed": not reasons,
  }


def _report(results: list[dict], decision: str) -> str:
  lines = [f"## Enrichment gate: **{decision.upper()}**", ""]
  if not results:
    lines.append("_No changed metadata projects to evaluate._")
    return "\n".join(lines) + "\n"
  for r in results:
    badge = "✅ pass" if r["passed"] else "❌ needs review"
    score = "n/a" if r["average_score"] is None else f"{r['average_score']:.3f}"
    lines.append(f"### `{r['project']}` — {badge} (score {score}, threshold {THRESHOLD:.2f})")
    if r["reasons"]:
      lines.append("Reasons: " + "; ".join(r["reasons"]))
    if r["metrics"]:
      lines.append("")
      lines.append("| metric | score | passed |")
      lines.append("|---|---|---|")
      for m in r["metrics"]:
        sc = "n/a" if m.get("score") is None else f"{m['score']:.3f}"
        lines.append(f"| {m['name']} | {sc} | {'yes' if m.get('passed', True) else 'NO'} |")
    if r["okf_errors"]:
      lines.append("")
      lines.append("OKF/structural errors:")
      for e in r["okf_errors"][:20]:
        lines.append(f"- {e}")
    lines.append("")
  return "\n".join(lines) + "\n"


def main() -> int:
  staging = os.environ.get("STAGING_BRANCH", "enrichment-staging")
  base = os.environ.get("GATE_BASE") or f"origin/{staging}"
  head = os.environ.get("GATE_HEAD", "HEAD")
  try:
    files = _changed_files(base, head)
  except subprocess.CalledProcessError:
    # Base ref not available (e.g. shallow / first run) -> fall back to last commit.
    files = _changed_files("HEAD~1", head) if _git("rev-list", "--count", "HEAD").strip() != "1" else []
  projects = _changed_projects(files)
  results = [_assess(p) for p in projects]
  decision = "pass" if results and all(r["passed"] for r in results) else (
      "pass" if not results else "hitl")
  report = _report(results, decision)
  with open(os.path.join(REPO_ROOT, "gate_report.md"), "w", encoding="utf-8") as f:
    f.write(report)
  summary = (f"{decision} — {len(results)} project(s): "
             + ", ".join(f"{r['project']}={'pass' if r['passed'] else 'hitl'}"
                         for r in results)) if results else "pass — no metadata changes"
  gh_out = os.environ.get("GITHUB_OUTPUT")
  if gh_out:
    with open(gh_out, "a", encoding="utf-8") as f:
      f.write(f"decision={decision}\n")
      f.write(f"summary={summary}\n")
  print(report)
  print(f"::notice::{summary}")
  return 0  # the gate never fails the job; the DECISION drives merge vs HITL


if __name__ == "__main__":
  raise SystemExit(main())
