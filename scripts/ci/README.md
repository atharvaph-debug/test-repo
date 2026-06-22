# Enrichment gate (CI) — what it is and how to set it up

This repo holds enrichment **metadata** only. The agent pushes each run to a
`kc-enrichment/**` branch. The `enrichment-gate` workflow then evaluates the
change set and either **auto-merges** it into the staging branch or routes it to
**human review (HITL)**.

```
agent push (kc-enrichment/**)
  -> enrichment-gate.yml
       - OKF/structural validation of changed project(s)
       - eval harness (dynamic, golden-free) per changed project dir
       - decision: pass -> open PR + enable auto-merge into staging
                   hitl -> open PR + label needs-hitl + request CODEOWNERS
  -> merge to enrichment-staging
  -> deploy-to-kc.yml (placeholder: kcmd push to Knowledge Catalog)
```

The eval harness is **bundled** under `eval/` for now (it is self-contained:
deps are `google-genai`, `google-auth`, `pyyaml`). Eventually pull it from the
source repo instead of vendoring it here.

## One-time GitHub + GCP setup

### 1. Branches & labels
- Ensure the staging branch exists (default `enrichment-staging`).
- Point the agent at it: `KC_VCS_GITHUB_BASE_BRANCH=enrichment-staging`,
  `KC_VCS_GITHUB_BRANCH_PREFIX=kc-enrichment`.
- Create labels: `automerge`, `needs-hitl`.

### 2. Actions permissions (repo Settings -> Actions -> General)
- Workflow permissions: **Read and write**.
- Check **Allow GitHub Actions to create and approve pull requests**.

### 3. Auto-merge & branch protection (repo Settings)
- Settings -> General -> enable **Allow auto-merge**.
- Branch protection on `enrichment-staging`: **require status checks** and add
  the `gate` job as required. Do NOT require approvals globally (a HITL PR is
  held simply by not enabling auto-merge; a human merges it manually).

### 4. GCP Workload Identity Federation (for the Vertex/Gemini judge)
- Enable the Vertex AI API on the project.
- Create a service account with role `roles/aiplatform.user`.
- Create a WIF pool + provider for GitHub OIDC (`token.actions.githubusercontent.com`),
  restricted to this repo (attribute condition on `repository`).
- Grant the GitHub principal permission to impersonate the SA.

### 5. Repo secrets & variables (Settings -> Secrets and variables -> Actions)
Secrets:
- `GCP_WIF_PROVIDER` = `projects/<num>/locations/global/workloadIdentityPools/<pool>/providers/<provider>`
- `GCP_SA_EMAIL`     = `<sa>@<project>.iam.gserviceaccount.com`

Variables:
- `GCP_PROJECT`     = your project id (judge runs Vertex here)
- `KC_EVAL_MODEL`   = e.g. `gemini-2.5-pro`
- `EVAL_THRESHOLD`  = e.g. `0.7`
- `STAGING_BRANCH`  = `enrichment-staging`

### 6. CODEOWNERS
Edit `.github/CODEOWNERS` with the real reviewers (optionally per project dir).

## Tuning the decision
`scripts/ci/run_gate.py` is the policy. Today: HITL on any OKF/structural error,
any project below `EVAL_THRESHOLD`, any judge metric below its gate, or if the
judge can't score; otherwise auto-merge. A regression-vs-staging check (compare
each entry's new score to its current score on staging) is the natural next
addition.
