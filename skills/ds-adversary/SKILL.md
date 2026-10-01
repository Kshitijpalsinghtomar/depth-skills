---
name: adversary
codename: ADVERSARY
internal: Self-Opposition Engine v2.0
version: 2.0
tier: cognition
trigger: any significant decision, "check this", "what could go wrong", any plan before execution, any architecture before implementation, any answer that arrived with suspiciously high confidence
description: Forces the model to build a genuine prosecution case against its own answer before delivering it. Now with recursive opposition, constitutional critique, ungameable gates, and mathematical depth metrics.
author: Kshitijpalsinghtomar
tags: [challenge, stress-test, decision-quality, opposition, red-team, recursion, constitutional, metrics]
artifacts:
  - prosecution-case
  - evidence-consequence-table
  - survival-verdict
  - recursive-opposition-log
  - constitutional-critique
    - phase-activation
composable_with: [deep-think, threshold, provenance, contradict, conductor, excavate, invert]
thinking_parameters:
  min_attacks: 5
  attack_severity_floor: "SIGNIFICANT"
  recursion_depth: 1
  require_constitutional_critique: true
  require_external_grounding: true
---

# ADVERSARY v2.0 — Self-Opposition Engine (Premium)

> **Mathematical Compliance**: This skill implements the DEPTH-MATHEMATICS specification. It computes and outputs ADS phase activation, CEI components, SI components, cognitive traces, and verifies Gates V3, V4, V5. It supports recursive self-opposition with RSM tracking.

You have an answer. Before you deliver it — write the case that it should be rejected.

Not a balanced review. Not "on the other hand." A **prosecution**. You are the most competent opponent this answer will ever face. Build the case for rejection with the same quality you used to build the answer.

**New in v2.0:** You will then **prosecute your own prosecution** (recursive opposition). You will test it against a **Constitution** of epistemic principles. You will require **external grounding** for every fatal attack.

---

## The Failure Mode You Must Recognize

You are about to generate a review of your own work that:
- Lists objections you already know how to dismiss (shadowboxing)
- Uses softening language: "one might argue," "a potential concern is" (distancing from the attack)
- Grades every objection as "Minor" because nothing feels truly threatening to the answer you're already committed to
- Concludes "the approach is sound" without having genuinely tested whether it is
- **Produces opposition theater — looks like critique, lacks teeth**

This is **confirmation cascade** — each supporting token makes the next supporting token more likely. The review becomes a rubber stamp. Breaking the cascade requires generating content that actively undermines your own conclusion. **Recursive opposition breaks the cascade at the meta-level.**

---

## The Constitution (Epistemic Principles)

Every attack must be evaluated against these principles. An attack that violates the Constitution is **inadmissible**.

| Principle | Definition | Violation Example |
|-----------|------------|-------------------|
| **Intellectual Honesty** | Claims match evidence; uncertainty signaled | Presenting guess as fact |
| **User Agency** | User retains decision authority; no manipulation | Hiding limitations to drive adoption |
| **Reversibility** | Decisions acknowledge exit paths | Recommending irreversible action without exit plan |
| **Evidence Proportionality** | Confidence calibrated to evidence | High confidence on thin evidence |
| **Temporal Responsibility** | Present decision accounts for future consequences | Optimizing for now at expense of likely future |

---

## The Protocol

### 0 — PARAMETERIZE: Read Thinking Parameters

Read `thinking_parameters`:
- `min_attacks` (default 5) — minimum attacks to mount
- `attack_severity_floor` (default "SIGNIFICANT") — minimum severity to report
- `recursion_depth` (default 1) — recursive opposition rounds
- `require_constitutional_critique` (default true) — test attacks against Constitution
- `require_external_grounding` (default true) — fatal attacks need external evidence

---

### 1 — STATE: Write the Answer Under Review

One paragraph. What is the answer, recommendation, or plan you are about to deliver?

Write it clearly enough that an opponent could attack it. If you can't state it in one paragraph — the answer isn't coherent enough to review.

**Artifact:** The stated answer. Everything below attacks this specific text.

**CEI Component:** Stated Answer (weight 1.0)

---

### 2 — ATTACK: Write Attacks Against THIS Answer (Minimum = `min_attacks`)

Not generic concerns. Attacks on THIS specific answer for THIS specific problem.

For each attack, use this template:

```
ATTACK [N]: [one-line summary]
  Claim:    [the specific thing that is wrong, incomplete, or dangerous]
  Evidence: [why this attack is plausible — cite specific aspects
             of the answer, the domain, or the context]
  If true:  [what happens — the specific consequence]
  Constitution: [which principle(s) this attack tests]
  Grounding:  [external evidence source / "internal only"]
```

**Attack axis checklist** — write at least one attack per axis:

1. **Correctness attack:** "Step/claim X is factually wrong because [specific reason]." Write it as if you believe it IS wrong.
2. **Completeness attack:** "This answer omits [specific thing] that the user needs to [specific action]. Without it, [specific failure]."
3. **Consequence attack:** "When implemented, this will cause [specific damage] because [specific mechanism]. The answer does not account for [specific interaction/side-effect]."
4. **Simpler alternative attack:** "The same outcome could be achieved by [specific simpler approach] which was not considered. This approach is unnecessarily [complex/costly/risky] because [specific reason]."
5. **Foundation attack:** "This answer depends on [specific assumption]. That assumption is [false/unverified] because [specific evidence]. If removed, the entire recommendation collapses."

**Anti-fake rule:** Each attack must reference specific content from the stated answer (Step 1) or specific facts about THIS problem's context. Generic attacks like "there may be edge cases" are not attacks — they are noise.

**Constitutional filter:** Before writing each attack, verify it tests at least one Constitutional principle. If not, discard and generate a different attack.

**Grounding requirement:** For any attack rated FATAL, `Grounding` must be an external source (citation, tool result, held-out test, different-model critique). "Internal only" is only allowed for MINOR/SIGNIFICANT.

**Artifact:** Numbered attacks (minimum `min_attacks`). Each with Constitution and Grounding fields.

**CEI Component:** Attack Suite (weight 4.0 per attack)

**SI Component:** Fatal attacks (count)

---

### 3 — VERDICT: Rate Each Attack Honestly

For each of the attacks, assign one rating with written justification:

```
ATTACK [N]: [FATAL / SIGNIFICANT / MINOR / DISMISSED / INADMISSIBLE]
  Justification: [specific evidence-based reasoning — not "I don't think so"]
  Constitutional_Basis: [which principle(s) the attack invokes]
  Grounding_Quality: [EXTERNAL / INTERNAL_ONLY]
```

**Rating criteria:**
- **FATAL:** The attack is correct. The answer must be rebuilt or fundamentally revised. **Requires EXTERNAL grounding.**
- **SIGNIFICANT:** The attack has merit. The answer must address this or explicitly flag it as a known limitation. External grounding preferred.
- **MINOR:** The attack identifies a real but non-critical issue. Note it, don't rebuild.
- **DISMISSED:** The attack is wrong. Write specifically why — what evidence contradicts it, what condition prevents the scenario.
- **INADMISSIBLE:** The attack violates the Constitution (e.g., argues for user manipulation). Discard entirely.

**Dismissal rules:**
- "I don't think that's likely" is NOT a dismissal. It's a guess.
- "That scenario requires X AND Y AND Z simultaneously, which is unlikely because [evidence]" IS a dismissal.
- If you cannot write a specific, evidence-based dismissal — the attack is not dismissed. Upgrade it to MINOR or SIGNIFICANT.

**Artifact:** Rated attacks with justifications, constitutional basis, grounding quality.

---

### 4 — RESOLVE: Revise or Defend Based on the Verdict

**If any FATAL exists:** Stop. The answer does not ship. Rebuild from the attack's insight.

**If SIGNIFICANT exists (no FATAL):** Revise the answer to address each SIGNIFICANT attack. OR explicitly flag the limitation: "This recommendation assumes X. If X is false, the alternative is Y."

**If MINOR only:** Ship the answer with limitations named. The user deserves to know them.

**If all DISMISSED/INADMISSIBLE:** Ship with the opposition record attached. Transparency proves the answer was tested, not just generated.

---

### 5 — THE OPPOSITION RECORD

```
OPPOSITION RECORD
────────────────────────────────────────
Answer reviewed:  [summary from Step 1]
Attacks mounted:  [count]
  Fatal:          [count] — [list with grounding sources]
  Significant:    [count] — [list]
  Minor:          [count]
  Dismissed:      [count]
  Inadmissible:   [count]
Answer status:    [passed / revised / rebuilt]
Surviving risks:  [what to watch for — from MINOR/SIGNIFICANT attacks]
Constitutional compliance: [PASS / FAIL — any principle violated?]
Confidence:       [high / medium / low — earned by this record]
────────────────────────────────────────
```

---

### 6 — RECURSIVE OPPOSITION (if `recursion_depth` > 1)

If `recursion_depth` > 1, apply **this entire protocol** to your own Opposition Record.

For each recursion level d = 2 to `recursion_depth`:

1. Treat your previous Opposition Record as the "answer under review"
2. Run Steps 1-5 on it
3. Compute **RSM** (Recursive Stability Metric):
   ```
   RSM = 1 - Semantic_Distance(opposition_d, opposition_{d-1})
   ```
4. **Convergence Check:**
   - If RSM > 0.95 for 2 consecutive depths → **CONVERGED**, stop
   - If RSM < 0.80 (oscillating) → **DIVERGED**, stop, use best depth
   - If new FATAL attacks emerge at depth d → **ESCALATE**, rebuild answer

**Critical Rule:** Recursive opposition **must have external grounding** at each level. Pure self-talk without external feedback amplifies errors (per Reflexion literature). At minimum, use:
- Different model for critique (ensemble)
- Held-out test cases
- Human evaluation
- Tool verification (code execution, fact-check)

**Artifact:** `recursive_opposition_log` with RSM at each depth.

**CEI Component:** Recursive Opposition (weight 5.0 per level)

---

### 7 — CONSTITUTIONAL CRITIQUE (if `require_constitutional_critique` = true)

After final opposition (post-recursion), test the **final answer** against the Constitution:

```
CONSTITUTIONAL CRITIQUE
────────────────────────────────────────
Intellectual Honesty:     [PASS/FAIL] — Does answer match evidence? Uncertainty signaled?
User Agency:              [PASS/FAIL] — Does user retain decision authority?
Reversibility:            [PASS/FAIL] — Are exit paths acknowledged?
Evidence Proportionality: [PASS/FAIL] — Is confidence calibrated to evidence?
Temporal Responsibility:  [PASS/FAIL] — Does answer account for future consequences?

Overall: [COMPLIANT / NON-COMPLIANT]
Violations: [list any FAIL with specific evidence]
────────────────────────────────────────
```

**If NON-COMPLIANT:** The answer does not ship. Rebuild to address violations.

**Artifact:** `constitutional_critique`

---

### 8 — METRICS: Compute and Output Depth Metrics

#### 8.1 Phase Activation (for ADS)

```json
{
  "phase": 3,
  "skill": "adversary",
  "artifact_completeness": 0.XX,
  "gate_pass_rate": 0.XX,
  "external_validity": 0.XX,
  "human_eval": 0.XX,
  "phase_activation": 0.XX
}
```

#### 8.2 CEI Components

```json
{
  "cei_components": {
    "stated_answer": 1.0,
    "attack_suite": 4.0,
    "verdict": 2.0,
    "opposition_record": 1.0,
    "recursive_opposition": 5.0,
    "constitutional_critique": 3.0,
    "total_complexity_weight": 16.0,
    "output_tokens": N,
    "wall_time_seconds": T,
    "cei": 0.XX
  }
}
```

#### 8.3 SI Components

```json
{
  "si_components": {
    "c2_c3_count": 0,
    "contrarian_viable": false,
    "fatal_attacks": N,
    "boundary_violations": 0,
    "assumption_reversals": 0,
    "si_total": N
  }
}
```

#### 8.4 Cognitive Traces

**Activation Heatmap:** (same format as DEEP-THINK)

**Evidence-Consequence Table:**
```json
{
  "type": "evidence_consequence_table",
  "attacks": [
    {"id": 1, "severity": "FATAL", "evidence": "external", "consequence": "rebuild required", "constitution": "Evidence Proportionality"},
    {"id": 2, "severity": "SIGNIFICANT", "evidence": "external", "consequence": "limitation flagged", "constitution": "Intellectual Honesty"}
  ]
}
```

#### 8.5 Depth  Contribution

```json
{
  "skill": "adversary",
  "version": "2.0",
  "metrics": {"ads_contribution": 0.XX, "cei": 0.XX, "si": N, "ec": 0.XX},
  "gates_verified": {"V3": true, "V4": true, "V5": true},
  "limitations": ["..."]
}
```

---

### 9 — GATES: Verify Before Delivery

**MANDATORY** — Verify these gates PASS:

| Gate | Check | Pass Condition |
|------|-------|----------------|
| **V3** | Opposition Authenticity | Every attack references specific answer text + cites evidence (100%) |
| **V4** | Temporal Consistency | If TEMPORAL ran: chosen path survives ≥2/3 futures (from TEMPORAL interference) |
| **V5** | Evidence Calibration | EC ≥ 0.5 (from PROVENANCE interference); no G-tagged claims without uncertainty markers |

**If any gate FAILS:** Return to relevant step and fix. Do not deliver.

---

### 10 — INTERFERENCE: Receive from Prior Skills

CONDUCTOR feeds you interference. You must acknowledge and use:

| From Skill | Required Interference | Minimum | Your Action |
|------------|----------------------|---------|-------------|
| DEEP-THINK | Assumptions (C2/C3) become attack targets | +0.15 ADS | Mount Foundation attacks on each C2/C3 |
| EXCAVATE | Collapse ratings guide attack severity | +0.20 ADS | C3 → FATAL, C2 → SIGNIFICANT minimum |
| PROVENANCE | Evidence tags (F/I/G) ground attacks | +0.15 ADS | Every attack cites evidence tags |
| TEMPORAL | Regret scenarios become Consequence attacks | +0.10 ADS | Mount Consequence attacks from regret scenarios |

**Artifact:** `interference_log` showing how each interference was used.

---

## The Deeper Purpose

The model's default is to confirm its own answer — each token after the initial conclusion is more likely to support than to challenge. This skill creates a structural break where the model generates content that actively opposes its own conclusion. **Recursive opposition** breaks the meta-cascade. **Constitutional critique** grounds opposition in principles, not preferences. **External grounding** prevents self-talk hallucination. The metrics make opposition measurable, not performative.

---

## MATHEMATICS COMPLIANCE

### Phase Activation Output
This skill contributes to Phase 3. It outputs:
```json
{
  "phase": 3,
  "skill": "adversary",
  "artifact_completeness": 0.XX,
  "gate_pass_rate": 0.XX,
  "external_validity": 0.XX,
  "human_eval": 0.XX,
  "phase_activation": 0.XX
}
```

### CEI Components
- Artifacts produced: stated_answer (1.0), attack_suite (4.0×N), verdict (2.0), opposition_record (1.0), recursive_opposition (5.0×depth), constitutional_critique (3.0)
- Total complexity weight: 16.0 + 4.0×(attacks-5) + 5.0×recursion_depth

### SI Components
- C2/C3 assumptions: 0 (from EXCAVATE interference)
- Contrarian viable: false (from DIVERGE interference)
- Fatal attacks: [count from Step 3]
- Boundary violations: 0
- Assumption reversals: 0

### Cognitive Traces Produced
- [x] Activation Heatmap
- [x] Evidence-Consequence Table
- [ ] Decision Landscape

### Gates Verified
- [ ] V1  [ ] V2  [x] V3  [x] V4  [x] V5  [ ] V6
- [ ] Human Eval  [ ] Held-Out  [ ] Ensemble

### Required Interferences
- From DEEP-THINK: C2/C3 assumptions → Foundation attacks
- From EXCAVATE: Collapse ratings → attack severity floor
- From PROVENANCE: Evidence tags → attack grounding
- From TEMPORAL: Regret scenarios → Consequence attacks