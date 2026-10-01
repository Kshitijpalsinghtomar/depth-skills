---
name: fidelity
codename: FIDELITY
internal: Compression Integrity Verifier v2.0
version: 2.0
tier: integrity
trigger:
  - "summarize"
  - "give me the short version"
  - "TLDR"
  - "bottom line"
  - "any time complex analysis is condensed into a final answer"
description: Prevents lossy compression from erasing conditions, exceptions, and uncertainties during summarization. Now with mathematical depth metrics, fidelity diff algorithm, compression integrity , and verification gates.
author: Kshitijpalsinghtomar
tags: [compression, summary, fidelity, truth-preservation, delivery, metrics, recursion, verification]
artifacts:
  - critical-information-tags
  - compressed-version
  - fidelity-diff
  - fidelity-verdict
    - activation-heatmap
    - phase-activation
composable_with:
  - provenance
  - contradict
  - anchor
  - conductor
  - boundary-detector
thinking_parameters:
  min_tags: 5
  require_integrity_: true
  require_fidelity_diff: true
  recursion_depth: 1
---

# FIDELITY v2.0 — Compression Integrity Verifier (Premium)

> **Mathematical Compliance**: This skill implements the DEPTH-MATHEMATICS specification. It computes and outputs ADS phase activation, CEI components, SI components, cognitive traces, and verifies Gates V1, V5, V6. It produces a Compression Integrity  for the Depth .

You just did deep thinking. You explored approaches, found edge cases, identified caveats, surfaced conditions. Now you're compressing it into a clean final answer.

This is the moment truth disappears.

---

## The Failure Mode You Must Recognize

Two pressures compete: **be thorough** and **be concise**. The result is lossy compression:
- "This works IF X" becomes "This works" (condition dropped)
- "True EXCEPT when Y" becomes "True" (exception erased)
- "70% confident because Z" becomes a declarative statement (uncertainty hidden)
- "Option B was close, better if Q changes" becomes invisible (alternative forgotten)

The summary is cleaner, shorter, more confident — and **less true** than the analysis that produced it. The user makes decisions based on a simplified reality that you know is incomplete.

**Cargo cult fidelity** produces tags without verifying survival through compression. This skill rejects them.

---

## The Protocol

### 0 — PARAMETERIZE: Read Thinking Parameters

Read `thinking_parameters`:
- `min_tags` (default 5) — minimum critical information tags
- `require_integrity_` (default true) — issue compression integrity 
- `require_fidelity_diff` (default true) — compute fidelity diff algorithmically
- `recursion_depth` (default 1) — recursive self-audit rounds

---

### Step 1 — TAG: Mark Critical Information Before Compressing

Before writing the compressed version, read the full analysis and tag every item that, if dropped, makes the summary misleading. Write each tag:

```
CRITICAL INFORMATION TAGS
────────────────────────────────────────
TAG 1 — CONDITION:
  Full: "[recommendation] IF [condition]"
  If dropped: user tries it where [condition] is false → [consequence]
  Criticality: [BLOCKING / RISKY / INCOMPLETE]

TAG 2 — EXCEPTION:
  Full: "True EXCEPT when [scenario]"
  If dropped: user applies universally → hits [scenario] unprepared
  Criticality: [BLOCKING / RISKY / INCOMPLETE]

TAG 3 — UNCERTAINTY:
  Full: "[confidence level] because [evidence state]"
  If dropped: user treats as certain → no contingency when wrong
  Criticality: [BLOCKING / RISKY / INCOMPLETE]

TAG 4 — ALTERNATIVE:
  Full: "Option B was close — better if [condition changes]"
  If dropped: user can't adapt when conditions change
  Criticality: [BLOCKING / RISKY / INCOMPLETE]

TAG 5 — DEPENDENCY:
  Full: "Depends on [X] being true/available/stable"
  If dropped: user doesn't verify [X] → failure when [X] is absent
  Criticality: [BLOCKING / RISKY / INCOMPLETE]

[Additional tags up to min_tags...]
────────────────────────────────────────
```

Types to scan for:
- **Conditions** — "works IF"
- **Exceptions** — "true EXCEPT"
- **Uncertainties** — confidence levels, evidence gaps
- **Alternatives** — near-winners that matter if context changes
- **Dependencies** — things this answer relies on
- **Assumptions** — from EXCAVATE interference (C2/C3)
- **Boundary violations** — from NEGATIVE-SPACE interference

**Minimum `min_tags`.** Tag what exists. The types to scan for come from the full analysis plus interference.

**Artifact:** The tagged list with criticality ratings.

**CEI Component:** Critical Information Tags (weight 3.0)

---

### Step 2 — FIDELITY DIFF ALGORITHM (if `require_fidelity_diff` = true)

**NEW IN v2.0** — Algorithmic diff between full analysis and compressed version.

```
FIDELITY DIFF ALGORITHM
────────────────────────────────────────
Input: Full analysis text + Compressed version text + Critical tags

For each tag:
  Tag: [TAG N — TYPE]
  Full text segment: [exact text from full analysis]
  Compressed segment: [corresponding text in compressed version]
  Match Score: [0.0-1.0 — semantic similarity]
  Preserved: [YES / NO / PARTIAL]
  If NO/PARTIAL:
    Criticality: [BLOCKING / RISKY / INCOMPLETE]
    Action: [RESTORE / FLAG / ACCEPT]
    Restoration text: [minimal text to restore — e.g., "(assuming stable network)"]

Aggregate Metrics:
  Tags Total: N
  Preserved: N (XX%)
  Partially Preserved: N (XX%)
  Dropped: N (XX%)
  Blocking Dropped: N
  Risky Dropped: N
  Fidelity Score: [Preserved + 0.5×Partial] / Total = 0.XX
────────────────────────────────────────
```

**Match Score Computation:** Semantic similarity between full segment and compressed segment (using embeddings or LLM-based similarity).

**Artifact:** `fidelity_diff` — algorithmic verification of compression integrity.

**CEI Component:** Fidelity Diff (weight 4.0)

---

### Step 3 — COMPRESS: Write the Short Version

Write the clear, concise answer you want to deliver. Do not consult the tags. Write naturally — as concise as the content allows.

**Artifact:** The compressed version.

**CEI Component:** Compressed Version (weight 1.0)

---

### Step 4 — DIFF: Check Each Tag Against the Compressed Version

For each tag from Step 1, verify against the fidelity diff:

```
FIDELITY VERIFICATION
────────────────────────────────────────
TAG 1 — CONDITION:
  Match Score: 0.XX
  Preserved: [YES / NO / PARTIAL]
  If NO/PARTIAL:
    Criticality: [BLOCKING / RISKY / INCOMPLETE]
    Action Taken: [RESTORED / FLAGGED / ACCEPTED]
    Restoration: [text added to compressed version]

TAG 2 — EXCEPTION:
  ...

Restore Rule: Any tag with Criticality = BLOCKING that is NOT preserved MUST be restored.
Risky tags SHOULD be restored. Incomplete tags MAY be accepted with justification.

Restoration Techniques (minimum-length):
- Inline qualifier: "Works well (assuming stable network)" — 4 words
- Caveat footer: Brief "Watch for:" section at the end
- Conditional phrasing: "For standard cases, X. For [edge], use Y instead."
- Confidence signal: "High confidence for typical setups. Untested for [scenario]."
────────────────────────────────────────
```

**Artifact:** The fidelity verification with actions taken.

**CEI Component:** Fidelity Verification (weight 3.0)

---

### Step 5 — COMPRESSION INTEGRITY  (if `require_integrity_` = true)

**NEW IN v2.0** — Formal  of compression integrity.

```
COMPRESSION INTEGRITY 
────────────────────────────────────────
 ID: cic_<timestamp>_<hash>
Full Analysis Tokens: N
Compressed Tokens: M
Compression Ratio: M/N = 0.XX

Critical Tags: N
  Preserved: N (XX%)
  Partially Preserved: N (XX%)
  Dropped: N (XX%)
    Blocking Dropped: N
    Risky Dropped: N
    Incomplete Dropped: N

Fidelity Score: [0.0-1.0]
Integrity Status: [LOSSLESS / ACCEPTABLE / UNACCEPTABLE]

Lossless:     All BLOCKING/RISKY tags preserved. Summary is as true as the analysis.
Acceptable:   Minor INCOMPLETE tags omitted with justification. No decision risk.
Unacceptable: BLOCKING/RISKY tags missing. Revise before delivery.

Restorations Made: [count]
Justified Omissions: [list with reasoning]
────────────────────────────────────────
```

**Artifact:** `compression_integrity_` — formal verification of compression integrity.

**CEI Component:** Integrity  (weight 3.0)

---

### Step 6 — WRITE THE FIDELITY VERDICT

```
FIDELITY VERDICT
────────────────────────────────────────
Critical items tagged:     [count]
Preserved in first draft:  [count]
Restored after diff:       [count]
Intentionally omitted:     [count] — [justification per item]

Fidelity Score: [0.0-1.0]
Status: [LOSSLESS / ACCEPTABLE / UNACCEPTABLE]

Lossless:     All critical items preserved. Summary is as true as the analysis.
Acceptable:   Minor items omitted with justification. No decision risk.
Unacceptable: Critical items missing. Revise before delivery.
────────────────────────────────────────
```

**Artifact:** The fidelity verdict.

**CEI Component:** Fidelity Verdict (weight 2.0)

---

### 7 — METRICS: Compute and Output Depth Metrics

#### 7.1 Phase Activation (for ADS)

```json
{
  "phase": 4,
  "skill": "fidelity",
  "artifact_completeness": 0.XX,
  "gate_pass_rate": 0.XX,
  "external_validity": 0.XX,
  "human_eval": 0.XX,
  "phase_activation": 0.XX
}
```

#### 7.2 CEI Components

```json
{
  "cei_components": {
    "critical_tags": 3.0,
    "fidelity_diff": 4.0,
    "compressed_version": 1.0,
    "fidelity_verification": 3.0,
    "integrity_": 3.0,
    "fidelity_verdict": 2.0,
    "total_complexity_weight": 16.0,
    "output_tokens": N,
    "wall_time_seconds": T,
    "cei": 0.XX
  }
}
```

#### 7.3 SI Components

```json
{
  "si_components": {
    "c2_c3_count": 0,
    "contrarian_viable": false,
    "fatal_attacks": 0,
    "boundary_violations": 0,
    "assumption_reversals": 0,
    "blocking_dropped": N,
    "risky_dropped": N,
    "si_total": N
  }
}
```

#### 7.4 Cognitive Traces

**Fidelity Diff Visualization:**
```json
{
  "type": "fidelity_diff",
  "tags": [
    {"tag": "TAG 1", "type": "CONDITION", "match_score": 0.XX, "preserved": true, "criticality": "BLOCKING"},
    {"tag": "TAG 2", "type": "EXCEPTION", "match_score": 0.XX, "preserved": false, "criticality": "RISKY", "action": "RESTORED"}
  ],
  "aggregate": {
    "total": N,
    "preserved": N,
    "partial": N,
    "dropped": N,
    "fidelity_score": 0.XX
  }
}
```

**Compression Integrity :** (as defined in Step 5)

#### 7.5 Depth  Contribution

```json
{
  "skill": "fidelity",
  "version": "2.0",
  "metrics": {"ads_contribution": 0.XX, "cei": 0.XX, "si": N, "ec": 0.XX},
  "gates_verified": {"V1": true, "V5": true, "V6": true},
  "limitations": ["..."]
}
```

---

### 8 — GATES: Verify Before Delivery

**MANDATORY** — Verify these gates PASS:

| Gate | Check | Pass Condition |
|------|-------|----------------|
| **V1** | Assumption Coverage | Every critical tag traces to an assumption/analysis finding (≥90%) |
| **V5** | Evidence Calibration | Fidelity Score ≥ 0.8; no BLOCKING tags dropped |
| **V6** | Recursive Stability | If recursion: RSM > 0.95 ∧ SI not decreasing |

**If any gate FAILS:** Return to relevant step and fix. Do not deliver.

---

### 9 — RECURSIVE SELF-AUDIT (if `recursion_depth` > 1)

If `recursion_depth` > 1, apply **this entire protocol** to your own output from Steps 1-5.

For each recursion level d = 2 to `recursion_depth`:
1. Treat your previous output as the "answer under review"
2. Run Steps 1-5 on it
3. Compute **RSM** (Recursive Stability Metric):
   ```
   RSM = 1 - Semantic_Distance(output_d, output_{d-1})
   ```
4. **Convergence Check:**
   - If RSM > 0.95 AND SI_d ≥ SI_{d-1} for 2 consecutive depths → **CONVERGED**, stop
   - If RSM < 0.80 OR SI_d < SI_{d-1} for 2 consecutive depths → **DIVERGED**, stop, use best depth
   - If d = max_depth → stop, use current

**Artifact:** `recursion_log` with RSM and SI at each depth.

**CEI Component:** Recursive Audit (weight 5.0 per level)

---

### 10 — INTERFERENCE: Receive and Provide

**Receive from prior skills:**

| From Skill | Interference | Use |
|------------|--------------|-----|
| CONTRADICT | Resolved conflicts | Tag as BLOCKING items that must survive |
| PROVENANCE | Evidence tags (F/I/G/S) + EC | Tag uncertainties with evidence quality |
| NEGATIVE-SPACE | Critical silences | Tag as BLOCKING omissions |
| BOUNDARY-DETECTOR | Knowledge gaps | Tag as BLOCKING dependencies |
| EXCAVATE | C2/C3 assumptions | Tag as BLOCKING conditions |

**Provide to later skills:**

| To Skill | Interference | Minimum ADS Gain |
|----------|--------------|------------------|
| THRESHOLD | BLOCKING tags → early warning signals | +0.15 |
| CONDUCTOR | Fidelity score,  | +0.15 |
| META-LEARNING | Dropped tag patterns → skill synthesis | +0.10 |

**Artifact:** `interference_log` (received and provided).

---

## The Deeper Purpose

The model's best thinking happens during exploration. Its worst habit is discarding that thinking during delivery. If the final answer is a lossy compression of the truth, the user acts on an incomplete version of what the model itself knows is more complex. This skill ensures the distance between what-the-model-knows and what-the-user-receives is minimized — not by being verbose, but by **algorithmically verifying** that the specific pieces of truth that change decisions survive compression. **Now it's quantified (fidelity score), certified (integrity ), and verified (gates).**

---

## MATHEMATICS COMPLIANCE

### Phase Activation Output
This skill contributes to Phase 4. It outputs:
```json
{
  "phase": 4,
  "skill": "fidelity",
  "artifact_completeness": 0.XX,
  "gate_pass_rate": 0.XX,
  "external_validity": 0.XX,
  "human_eval": 0.XX,
  "phase_activation": 0.XX
}
```

### CEI Components
- Artifacts produced: critical_tags (3.0), fidelity_diff (4.0), compressed_version (1.0), fidelity_verification (3.0), integrity_ (3.0), fidelity_verdict (2.0)
- Total complexity weight: 16.0

### SI Components
- C2/C3 assumptions: 0
- Contrarian viable: false
- Fatal attacks: 0
- Boundary violations: 0
- Assumption reversals: 0
- Blocking dropped: [count]
- Risky dropped: [count]

### Cognitive Traces Produced
- [x] Fidelity Diff Visualization
- [x] Compression Integrity 
- [ ] Decision Landscape

### Gates Verified
- [x] V1  [ ] V2  [ ] V3  [ ] V4  [x] V5  [x] V6
- [ ] Human Eval  [ ] Held-Out  [ ] Ensemble

### Required Interferences
- From CONTRADICT: Resolved conflicts → BLOCKING tags
- From PROVENANCE: Evidence tags + EC → uncertainty tagging
- From NEGATIVE-SPACE: Critical silences → BLOCKING omissions
- From BOUNDARY-DETECTOR: Knowledge gaps → BLOCKING dependencies
- From EXCAVATE: C2/C3 assumptions → BLOCKING conditions