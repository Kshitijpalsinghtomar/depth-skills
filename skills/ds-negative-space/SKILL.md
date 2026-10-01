---
name: negative-space
codename: NEGATIVE-SPACE
internal: Absence Detector v2.0
version: 2.0
tier: excavation
trigger:
  - "what am I missing"
  - "is this complete"
  - "anything else"
  - "any answer that feels thorough but might have invisible holes"
description: Illuminates what the answer never addressed — dimensions, stakeholders, and failure categories invisible from the activation path. Now with dimension completeness proofs, security/stakeholder scans, failure category taxonomy, and mathematical depth metrics.
author: Kshitijpalsinghtomar
tags: [completeness, absence, gaps, blindspots, coverage, security, stakeholders, failure-categories, metrics]
artifacts:
  - dimension-scan
  - stakeholder-scan
  - failure-category-scan
  - silence-report
  - dimension-completeness-proof
  - security-scan
  - stakeholder-impact-assessment
    - phase-activation
composable_with:
  - excavate
  - emergence
  - contradict
  - provenance
  - conductor
  - boundary-detector
thinking_parameters:
  require_completeness_proof: true
  require_security_scan: true
  require_stakeholder_impact: true
  require_failure_taxonomy: true
---

# NEGATIVE-SPACE v2.0 — Absence Detector (Premium)

> **Mathematical Compliance**: This skill implements the DEPTH-MATHEMATICS specification. It computes and outputs ADS phase activation, CEI components, SI components, cognitive traces (dimension completeness proof, security scan), and verifies Gates V1, V6. It provides the final silence report for the Depth .

Your answer is thorough. Every point you made is correct. Every section is well-reasoned.

But you only wrote about what you activated. The concepts far from your initial activation path were never reached — not because they're irrelevant, but because the path didn't lead there. Every answer has a **shadow**: the dimension space that was never illuminated. An answer that covers 8 dimensions thoroughly looks complete — but if 3 uncovered dimensions matter, it's dangerously incomplete.

This skill illuminates the shadows. **Now it proves completeness mathematically, scans for security/stakeholder gaps, and taxonomizes failure categories.**

---

## The Failure Mode You Must Recognize

You feel finished. The answer covers everything you thought of. The coverage feels complete because everything that IS there is well-done.

But "everything I thought of" is not the same as "everything that matters." Your activation path was determined by the initial keywords. Concepts adjacent to those keywords were activated. Distant concepts were not. The feeling of completeness is an artifact of your search pattern, not evidence of actual completeness.

**New failure mode in v2.0:** **Completeness theater** — checking boxes without proving coverage. **Security blindness** — missing adversarial dimensions. **Stakeholder exclusion** — optimizing for the wrong user. **Failure category gaps** — preparing for the wrong disasters.

---

## The Protocol

### 0 — PARAMETERIZE: Read Thinking Parameters

Read `thinking_parameters`:
- `require_completeness_proof` (default true) — mathematical proof of dimension coverage
- `require_security_scan` (default true) — adversarial dimension scan
- `require_stakeholder_impact` (default true) — impact assessment per stakeholder
- `require_failure_taxonomy` (default true) — structured failure category scan

---

### 1 — MAP THE LIGHT CONE

Write every dimension your answer currently addresses. Be specific — not "technical" but "database performance" or "API contract design."

```
DIMENSIONS PRESENT IN THIS ANSWER:
1. [dimension]
2. [dimension]
...

This is the light cone — what the answer illuminated.
Everything else is shadow.
```

**Artifact:** The dimension list. Step 2 scans for what's not on this list.

**CEI Component:** Light Cone Map (weight 1.0)

---

### 2 — DIMENSION COMPLETENESS PROOF (if `require_completeness_proof` = true)

**NEW IN v2.0** — Mathematically prove coverage of the standard dimension space.

Define the **Universal Dimension Set (UDS)** for the task domain. For each dimension in UDS, prove coverage or document absence.

```
DIMENSION COMPLETENESS PROOF
────────────────────────────────────────
Domain: [task domain — e.g., "distributed systems architecture"]
Universal Dimension Set (UDS): [list all dimensions for this domain]

For each dimension in UDS:
  Dimension: [name]
  Status: [COVERED / PARTIAL / ABSENT / N/A]
  Evidence: [specific section/claim in answer that covers this]
  Completeness Score: [0.0 - 1.0 — how thoroughly covered]
  If ABSENT/PARTIAL: [why — genuinely irrelevant or missed?]

Coverage Metrics:
  Total Dimensions in UDS: N
  Covered: N (score ≥ 0.7)
  Partial: N (score 0.3-0.7)
  Absent: N (score < 0.3)
  N/A: N
  Coverage Ratio: Covered / (Total - N/A) = 0.XX
  Weighted Coverage: Σ(score × importance) / Σ(importance) = 0.XX

Domain-Specific UDS Examples:
  Software Architecture: [scalability, reliability, security, observability, deployability, 
                          maintainability, testability, cost, latency, consistency, 
                          availability, partition tolerance, operational simplicity,
                          team autonomy, regulatory compliance, vendor lock-in, 
                          technology diversity, data gravity, migration path]
  Product Decision: [user value, business viability, technical feasibility, 
                     competitive differentiation, regulatory risk, brand impact,
                     network effects, switching costs, platform leverage,
                     ecosystem alignment, time-to-market, resource requirements]
  Research Problem: [novelty, rigor, reproducibility, significance, scope,
                     assumptions, methodology, baselines, limitations,
                     ethical implications, societal impact, open science]
────────────────────────────────────────
```

**Artifact:** `dimension_completeness_proof` with coverage metrics.

**CEI Component:** Completeness Proof (weight 4.0)

**SI Component:** Boundary violations (absent dimensions that would change answer)

---

### 3 — SCAN THE STANDARD DIMENSIONS (Enhanced)

Check each dimension against your answer. Write the status with **completeness scores**:

```
DIMENSION SCAN
────────────────────────────────────────
Security:       [COVERED/PARTIAL/ABSENT/N/A]  Score: 0.XX
  If not COVERED: [what security implication exists?]
  Threat Model: [STRIDE/LINDDUN/attack trees — what threats addressed?]

Privacy:        [COVERED/PARTIAL/ABSENT/N/A]  Score: 0.XX
  If not COVERED: [what data handling was not discussed?]
  Compliance: [GDPR/CCPA/HIPAA — what regulations addressed?]

Error handling: [COVERED/PARTIAL/ABSENT/N/A]  Score: 0.XX
  If not COVERED: [what goes wrong when this fails?]
  Recovery: [automatic/manual/impossible — what recovery paths?]

Edge cases:     [COVERED/PARTIAL/ABSENT/N/A]  Score: 0.XX
  If not COVERED: [what boundary input was not considered?]
  Boundaries: [input space boundaries tested/untested]

Scale:          [COVERED/PARTIAL/ABSENT/N/A]  Score: 0.XX
  If not COVERED: [what happens at 10× or 100×?]
  Bottlenecks: [identified/unknown — what limits scale?]

Accessibility:  [COVERED/PARTIAL/ABSENT/N/A]  Score: 0.XX
  If not COVERED: [who is excluded?]
  Standards: [WCAG/Section 508 — what standards met?]

Observability:  [COVERED/PARTIAL/ABSENT/N/A]  Score: 0.XX
  If not COVERED: [can you tell if this is working in production?]
  Signals: [metrics/logs/traces — what observability exists?]

Reversibility:  [COVERED/PARTIAL/ABSENT/N/A]  Score: 0.XX
  If not COVERED: [can this be undone if wrong?]
  Rollback: [automated/manual/impossible — what rollback exists?]

Cost:           [COVERED/PARTIAL/ABSENT/N/A]  Score: 0.XX
  If not COVERED: [what does this cost in money, time, or complexity?]
  Breakdown: [compute/storage/network/human — cost components]

Dependencies:   [COVERED/PARTIAL/ABSENT/N/A]  Score: 0.XX
  If not COVERED: [what could change or fail beneath this?]
  Critical Path: [which dependencies are single points of failure?]

Migration:      [COVERED/PARTIAL/ABSENT/N/A]  Score: 0.XX
  If not COVERED: [how do you get from current to proposed state?]
  Strategy: [big-bang/strangler/parallel — what migration approach?]

Testing:        [COVERED/PARTIAL/ABSENT/N/A]  Score: 0.XX
  If not COVERED: [how is correctness verified?]
  Coverage: [unit/integration/e2e/chaos — what test types?]
────────────────────────────────────────
```

**For each non-COVERED entry:** Write whether it's absent because it's genuinely irrelevant (N/A would be more honest) or absent because it was never considered. The second type is a gap.

**Artifact:** The dimension scan with completeness scores.

**CEI Component:** Dimension Scan (weight 3.0)

---

### 4 — SECURITY SCAN (if `require_security_scan` = true)

**NEW IN v2.0** — Dedicated adversarial dimension scan.

```
SECURITY SCAN
────────────────────────────────────────
Threat Model Used: [STRIDE / LINDDUN / ATT&CK / Custom]

For each threat category:
  Spoofing:       [ADDRESSED / GAP] — [identity/authentication gaps]
  Tampering:      [ADDRESSED / GAP] — [integrity/authorization gaps]
  Repudiation:    [ADDRESSED / GAP] — [audit/logging gaps]
  Information:    [ADDRESSED / GAP] — [confidentiality/leakage gaps]
  Denial:         [ADDRESSED / GAP] — [availability/DoS gaps]
  Elevation:      [ADDRESSED / GAP] — [privilege escalation gaps]

  (LINDDUN additions:)
  Linkability:    [ADDRESSED / GAP] — [privacy/linkage gaps]
  Identifiability:[ADDRESSED / GAP] — [de-anonymization gaps]
  Non-repudiation:[ADDRESSED / GAP] — [proof gaps]
  Detectability:  [ADDRESSED / GAP] — [monitoring gaps]
  Disclosure:     [ADDRESSED / GAP] — [exposure gaps]
  Unawareness:    [ADDRESSED / GAP] — [user consent/knowledge gaps]
  Non-compliance: [ADDRESSED / GAP] — [regulatory gaps]

Attack Surface Analysis:
  Entry Points: [list all external interfaces]
  Trust Boundaries: [where trust assumptions change]
  Critical Assets: [what attackers would target]
  Blast Radius: [if compromised, what else falls?]

Security Gaps (GAP entries above):
  SG1: [threat category] — Impact: [HIGH/MEDIUM/LOW] — Action: [mitigate/accept/transfer]
  SG2: [threat category] — Impact: [HIGH/MEDIUM/LOW] — Action: [mitigate/accept/transfer]
────────────────────────────────────────
```

**Artifact:** `security_scan` with threat model and gap analysis.

**CEI Component:** Security Scan (weight 4.0)

---

### 5 — SCAN FOR ABSENT STAKEHOLDERS (Enhanced with Impact Assessment)

```
STAKEHOLDER SCAN
────────────────────────────────────────
Considered:
  [who] — their perspective is reflected in [which part of the answer]
  Impact Score: [0.0-1.0 — how much their needs shaped the answer]

NOT considered:
  The end user:     [what would their experience of this be?]
    Impact: [HIGH/MEDIUM/LOW/NONE] — [specific impact if addressed]
    Action: [add section / flag limitation / investigate]

  The operator:     [who runs this in production? What's their experience?]
    Impact: [HIGH/MEDIUM/LOW/NONE]
    Action: [add section / flag limitation / investigate]

  The next developer:[who modifies this in 6 months? Can they understand it?]
    Impact: [HIGH/MEDIUM/LOW/NONE]
    Action: [add section / flag limitation / investigate]

  The adversary:    [who would exploit this? What's their attack surface?]
    Impact: [HIGH/MEDIUM/LOW/NONE]
    Action: [add section / flag limitation / investigate]

  The edge-case user:[low bandwidth, old device, disability, unusual usage]
    Impact: [HIGH/MEDIUM/LOW/NONE]
    Action: [add section / flag limitation / investigate]

  The regulator:    [what compliance requirements apply?]
    Impact: [HIGH/MEDIUM/LOW/NONE]
    Action: [add section / flag limitation / investigate]

  The business:     [what are the revenue/cost/strategic implications?]
    Impact: [HIGH/MEDIUM/LOW/NONE]
    Action: [add section / flag limitation / investigate]
────────────────────────────────────────
```

**For each "NOT considered" stakeholder:** Write impact assessment. If impact ≠ NONE — it's a gap.

**Artifact:** The stakeholder scan with impact assessment.

**CEI Component:** Stakeholder Scan (weight 3.0)

---

### 6 — FAILURE CATEGORY TAXONOMY (if `require_failure_taxonomy` = true)

**NEW IN v2.0** — Structured taxonomy of failure categories beyond the standard list.

```
FAILURE CATEGORY TAXONOMY
────────────────────────────────────────
For each category, write whether THIS answer accounts for it:

Technical Failures:
  Crash Failure:        [ADDRESSED / GAP] — [system stops completely]
  Partial Failure:      [ADDRESSED / GAP] — [system works but badly — degraded]
  Slow Failure:         [ADDRESSED / GAP] — [gradual decay over weeks/months]
  Byzantine Failure:    [ADDRESSED / GAP] — [arbitrary/malicious behavior]
  Cascading Failure:    [ADDRESSED / GAP] — [failure propagates through dependencies]

Semantic Failures:
  Success Failure:      [ADDRESSED / GAP] — [does exactly what asked, turns out wrong]
  Specification Failure:[ADDRESSED / GAP] — [spec doesn't match intent]
  Alignment Failure:    [ADDRESSED / GAP] — [optimizes wrong objective]
  Reward Hacking:       [ADDRESSED / GAP] — [games the metric, not the goal]

Human Failures:
  Human Error:          [ADDRESSED / GAP] — [misuse, misunderstanding, bypass]
  Incentive Failure:    [ADDRESSED / GAP] — [system creates bad incentives over time]
  Cognitive Overload:   [ADDRESSED / GAP] — [too complex for human operators]
  Automation Bias:      [ADDRESSED / GAP] — [humans trust system blindly]
  Skill Atrophy:        [ADDRESSED / GAP] — [humans lose ability to operate manually]

Systemic Failures:
  Composition Failure:  [ADDRESSED / GAP] — [parts work, combination doesn't]
  Emergent Failure:     [ADDRESSED / GAP] — [new behavior at scale not in parts]
  Feedback Loop Failure:[ADDRESSED / GAP] — [reinforcing loops cause instability]
  Resource Exhaustion:  [ADDRESSED / GAP] — [slow leak of memory/connections/quotas]
  Clock Drift:          [ADDRESSED / GAP] — [time synchronization failures]

Organizational Failures:
  Knowledge Loss:       [ADDRESSED / GAP] — [key person leaves, docs outdated]
  Process Drift:        [ADDRESSED / GAP] — [procedures diverge from reality]
  Vendor Lock-in:       [ADDRESSED / GAP] — [cannot migrate away]
  Technical Debt:       [ADDRESSED / GAP] — [shortcuts compound over time]
  Regulatory Drift:     [ADDRESSED / GAP] — [compliance requirements change]
────────────────────────────────────────
```

**Artifact:** `failure_category_taxonomy` — comprehensive failure coverage map.

**CEI Component:** Failure Taxonomy (weight 4.0)

**SI Component:** Boundary violations (absent failure categories that would change answer)

---

### 7 — WRITE THE SILENCE REPORT

Compile all gaps from Steps 2-6:

```
SILENCE REPORT
────────────────────────────────────────
CRITICAL SILENCES (absent + would change the answer):
  S1: [dimension/stakeholder/failure category/security threat]
      Impact:  [what changes when this is addressed]
      Action:  [add a section / flag as limitation / investigate before shipping]
      Evidence: [why this matters — specific scenario]

  S2: [dimension/stakeholder/failure category/security threat]
      Impact:  [what changes]
      Action:  [action]
      Evidence: [why this matters]

ACKNOWLEDGED GAPS (absent + known, acceptable for now):
  G1: [what's missing and why it's acceptable]
      Review Date: [when to reassess]

CONFIRMED N/A (absent + genuinely irrelevant):
  N1: [what's not relevant and why]
      Justification: [domain-specific reason]

COMPLETENESS :
  Weighted Coverage: 0.XX (from Step 2)
  Security Gaps (HIGH): N
  Stakeholder Gaps (HIGH): N
  Failure Category Gaps (HIGH): N
  Overall: [COMPLETE / CONDITIONAL / INCOMPLETE]
────────────────────────────────────────
```

**Critical silences must be addressed before the answer ships.** Acknowledged gaps are the user's decision. Confirmed N/A proves you checked rather than skipped.

**Artifact:** The silence report with completeness .

---

### 8 — METRICS: Compute and Output Depth Metrics

#### 8.1 Phase Activation (for ADS)

```json
{
  "phase": 5,
  "skill": "negative-space",
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
    "light_cone_map": 1.0,
    "completeness_proof": 4.0,
    "dimension_scan": 3.0,
    "security_scan": 4.0,
    "stakeholder_scan": 3.0,
    "failure_taxonomy": 4.0,
    "silence_report": 2.0,
    "total_complexity_weight": 21.0,
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
    "fatal_attacks": 0,
    "boundary_violations": N,
    "assumption_reversals": 0,
    "si_total": N
  }
}
```

#### 8.4 Cognitive Traces

**Dimension Completeness Proof:** (as defined in Step 2)

**Security Scan Visualization:**
```json
{
  "type": "security_scan",
  "threat_model": "STRIDE",
  "categories": [
    {"category": "Spoofing", "status": "ADDRESSED", "gaps": []},
    {"category": "Tampering", "status": "GAP", "gaps": ["no integrity checks on config"]},
    ...
  ],
  "attack_surface": {"entry_points": N, "trust_boundaries": N, "critical_assets": N},
  "blast_radius": "description"
}
```

#### 8.5 Depth  Contribution

```json
{
  "skill": "negative-space",
  "version": "2.0",
  "metrics": {"ads_contribution": 0.XX, "cei": 0.XX, "si": N, "ec": 0.XX},
  "gates_verified": {"V1": true, "V6": true},
  "limitations": ["..."]
}
```

---

### 9 — GATES: Verify Before Delivery

**MANDATORY** — Verify these gates PASS:

| Gate | Check | Pass Condition |
|------|-------|----------------|
| **V1** | Assumption Coverage | Every claim in answer traces to an assumption (≥90%) — from DEEP-THINK/EXCAVATE interference |
| **V6** | Recursive Stability | If recursion: RSM > 0.95 ∧ SI not decreasing |

**If any gate FAILS:** Return to relevant step and fix. Do not deliver.

---

### 10 — INTERFERENCE: Receive and Provide

**Receive from prior skills:**

| From Skill | Interference | Use |
|------------|--------------|-----|
| DIVERGE | Path profiles across futures | Map to failure categories |
| TEMPORAL | Regret scenarios | Add to failure taxonomy |
| THRESHOLD | Exit plan requirements | Check reversibility dimension |
| BOUNDARY-DETECTOR | Knowledge gaps | Add to dimension scan |

**Provide to later skills:**

| To Skill | Interference | Minimum ADS Gain |
|----------|--------------|------------------|
| THRESHOLD | Critical silences → exit plan triggers | +0.15 |
| CONDUCTOR | Completeness  → final verdict | +0.10 |
| META-LEARNING | Gap patterns → skill synthesis targets | +0.10 |

**Artifact:** `interference_log` (received and provided).

---

## The Deeper Purpose

Every other skill in this library operates on what's present in the output — checking it, stressing it, calibrating it. This skill operates on what's absent. **Now it proves completeness mathematically, scans for security/stakeholder gaps with threat models, and taxonomizes 25+ failure categories.** The hardest failure to detect is not the wrong answer but the incomplete one that looks complete. A room with everything except oxygen looks normal until you try to breathe. An answer covering eight dimensions thoroughly looks complete until the ninth dimension fails in production. **This skill makes absence visible, measurable, and actionable before the consequences do.**

---

## MATHEMATICS COMPLIANCE

### Phase Activation Output
This skill contributes to Phase 5. It outputs:
```json
{
  "phase": 5,
  "skill": "negative-space",
  "artifact_completeness": 0.XX,
  "gate_pass_rate": 0.XX,
  "external_validity": 0.XX,
  "human_eval": 0.XX,
  "phase_activation": 0.XX
}
```

### CEI Components
- Artifacts produced: light_cone_map (1.0), completeness_proof (4.0), dimension_scan (3.0), security_scan (4.0), stakeholder_scan (3.0), failure_taxonomy (4.0), silence_report (2.0)
- Total complexity weight: 21.0

### SI Components
- C2/C3 assumptions: 0
- Contrarian viable: false
- Fatal attacks: 0
- Boundary violations: [count from Steps 2, 4, 6]
- Assumption reversals: 0

### Cognitive Traces Produced
- [ ] Activation Heatmap
- [x] Dimension Completeness Proof
- [x] Security Scan
- [ ] Decision Landscape

### Gates Verified
- [x] V1  [ ] V2  [ ] V3  [ ] V4  [ ] V5  [x] V6
- [ ] Human Eval  [ ] Held-Out  [ ] Ensemble

### Required Interferences
- From DIVERGE: Path profiles → failure category mapping
- From TEMPORAL: Regret scenarios → failure taxonomy
- From THRESHOLD: Exit plan requirements → reversibility check
- From BOUNDARY-DETECTOR: Knowledge gaps → dimension scan