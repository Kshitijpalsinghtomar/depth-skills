---
name: threshold
codename: THRESHOLD
internal: Commitment Gateway v2.0
version: 2.0
tier: governance
trigger:
  - "should we go with"
  - "let's just do"
  - "final decision"
  - "any schema change"
  - "any public API contract"
  - "any irreversible deployment"
description: Gates commitment on irreversible decisions by measuring reversal cost and enforcing proportional exploration depth. Now with reversal cost functions, commitment s, early warning signals, and mathematical depth metrics.
author: Kshitijpalsinghtomar
tags: [decisions, irreversibility, commitment, gates, reversal-cost, s, early-warning, metrics]
artifacts:
  - threshold-classification
  - depth-requirement
  - termination-gates
  - exit-plan
  - reversal-cost-function
    - early-warning-signals
    - phase-activation
composable_with:
  - adversary
  - diverge
  - temporal
  - conductor
  - negative-space
  - provenance
thinking_parameters:
  require_reversal_cost_function: true
  require_commitment_: true
  require_early_warning: true
  require_gate_enforcement: true
---

# THRESHOLD v2.0 — Commitment Gateway (Premium)

> **Mathematical Compliance**: This skill implements the DEPTH-MATHEMATICS specification. It computes and outputs ADS phase activation, CEI components, SI components, cognitive traces (reversal cost function, commitment , early warning signals), and verifies Gates V1-V6. It provides the final commitment verdict for the Depth .

Not all decisions deserve the same depth. A CSS color choice and a database primary key choice are not the same decision — but without this skill, the model treats them with roughly equal cognitive investment.

This skill creates the gate between thinking and committing. It measures the **reversal cost**, enforces proportional exploration, and requires an exit plan before any high-cost commitment. **Now it quantifies reversal cost as a function, produces verifiable commitment s, and defines early warning signals.**

---

## The Failure Mode You Must Recognize

You are about to give a quick, confident answer to a decision that:
- Cannot be easily undone (database schema, public API, data deletion)
- Affects many people or systems (blast radius extends beyond the immediate scope)
- Was not explored proportionally (one approach considered, zero alternatives evaluated)

Uniform depth — treating all decisions with the same level of analysis — systematically under-invests in the decisions that matter most.

**New failure mode in v2.0:** **Reversal cost handwaving** — "hard to undo" without quantification. **Commitment theater** — gates that look strict but lack enforcement. **Early warning absence** — no observable signals to detect a wrong decision before it's too late.

---

## The Protocol

### 0 — PARAMETERIZE: Read Thinking Parameters

Read `thinking_parameters`:
- `require_reversal_cost_function` (default true) — quantify reversal cost mathematically
- `require_commitment_` (default true) — produce verifiable commitment 
- `require_early_warning` (default true) — define observable early warning signals
- `require_gate_enforcement` (default true) — enforce all gates before commitment

---

### Step 1 — CLASSIFY: Write the Reversal Cost Function

**NEW IN v2.0** — Reversal cost is not a category. It's a **function**.

```
THRESHOLD CLASSIFICATION
────────────────────────────────────────
Decision:          [what is being decided — one sentence]

Reversal Cost Function R(t):
  R(t) = C_fixed + C_variable(t) + C_opportunity(t) + C_risk(t)

  Where:
  C_fixed = [one-time costs: migration tooling, data transformation, downtime]
  C_variable(t) = [ongoing costs: parallel run, dual-write, performance penalty]
  C_opportunity(t) = [foregone benefits: what you can't do while reversing]
  C_risk(t) = [probability × impact of reversal failure]

  Parameters:
    t = time since commitment [days]
    R(0) = [immediate reversal cost]
    R(30) = [cost at 30 days]
    R(90) = [cost at 90 days]
    R(365) = [cost at 1 year]
    R(∞) = [permanent cost — if never fully reversible]

Reversal Timeline: [minutes / hours / days / weeks / months / never]
Blast Radius:      [self / team / users / ecosystem]
Category:          [1 / 2 / 3 / 4] — derived from R(∞)

  Category 1 — TRIVIAL (R(∞) < $1K equivalent, minutes-hours):
    Variable names, file organization, CSS values, config
  Category 2 — MODERATE (R(∞) $1K-$100K, hours-days):
    Indexes, internal API shapes, library versions, service boundaries
  Category 3 — EXPENSIVE (R(∞) $100K-$1M, days-weeks):
    Database schemas, public API contracts, auth systems, data formats
  Category 4 — CATASTROPHIC (R(∞) > $1M or impossible, weeks-never):
    Primary keys, data deletion, published standards, architecture at scale

When uncertain between two categories, pick the higher one.
The cost of overthinking a reversible decision is wasted time.
The cost of underthinking an irreversible one is permanent damage.

────────────────────────────────────────
```

**Artifact:** The reversal cost function with parameters and category.

**CEI Component:** Reversal Cost Function (weight 4.0)

---

### Step 2 — SET REQUIRED DEPTH (Proportional to Reversal Cost)

Based on the classification:

```
DEPTH REQUIREMENT
────────────────────────────────────────
Category 1 — STANDARD:
  → 1 approach is sufficient. Move fast.
  → Skip remaining steps. Deliver.
  ADS Target: 0.20

Category 2 — ELEVATED:
  → 2 approaches minimum before committing.
  → Document rollback path (1-2 sentences).
  → Run G1-G3 gates (Step 3).
  ADS Target: 0.45

Category 3 — MAXIMUM:
  → 3 approaches minimum (use DIVERGE skill).
  → Full ADVERSARY review of chosen approach.
  → Written rollback plan (Step 4).
  → Run ALL gates G1-G6 (Step 3).
  ADS Target: 0.70

Category 4 — MAXIMUM-PLUS:
  → All Layer 0 skills activated (DEEP-THINK → DIVERGE → ADVERSARY).
  → No commitment without explicit user confirmation.
  → Written rollback plan with timeline and dependencies (Step 4).
  → Run ALL gates. No exceptions.
  ADS Target: 0.85

────────────────────────────────────────
```

**Artifact:** The depth requirement with ADS targets.

---

### Step 3 — RUN THE TERMINATION GATES

Before any answer ships at Category 2+, these gates must pass. Write the result for each required gate:

```
TERMINATION GATES
────────────────────────────────────────
G1 — Problem fidelity:
  Can I restate the user's intent (not just their words)?
  [PASS — restatement: ___] / [FAIL — unclear because ___]

G2 — Alternative coverage:
  Were at least [2/3] materially different approaches considered?
  [PASS — approaches: ___] / [FAIL — only [N] considered]
  CIM Check: [CIM score ≥ 0.5? PASS/FAIL]

G3 — Assumption exposure:
  Are critical assumptions named and rated (C2/C3 from EXCAVATE)?
  [PASS — assumptions listed] / [FAIL — assumptions not surfaced]

G4 — Failure-mode analysis:    (Category 3+ only)
  Are failure paths identified, not just the happy path?
  [PASS — failures: ___] / [FAIL — only happy path]
  NEGATIVE-SPACE Check: [failure taxonomy complete? PASS/FAIL]

G5 — Reversibility plan:       (Category 3+ only)
  Is the exit plan written (Step 4)?
  [PASS — plan written] / [FAIL — no exit plan]
  Reversal Cost Function: [R(t) defined? PASS/FAIL]

G6 — Decision rationale:       (Category 3+ only)
  Can I explain why the chosen option beats alternatives under
  THESE SPECIFIC constraints?
  [PASS — because: ___] / [FAIL — generic reasoning]
  PROVENANCE Check: [EC ≥ 0.5? PASS/FAIL]

G7 — Early warning signals:    (Category 3+ only, NEW)
  Are observable early warning signals defined?
  [PASS — signals: ___] / [FAIL — no signals]
  Monitoring Plan: [dashboards/alerts defined? PASS/FAIL]

G8 — Commitment :   (Category 4 only, NEW)
  Is the commitment  written (Step 5)?
  [PASS —  written] / [FAIL — no ]
  User Confirmation: [explicit confirmation received? PASS/FAIL]

────────────────────────────────────────
```

**Any FAIL → return to the relevant step and complete it before shipping.** The gate exists because coherence is not completion and confidence is not evidence.

**Artifact:** The gate results. Failed gates block delivery.

**CEI Component:** Termination Gates (weight 3.0)

---

### Step 4 — WRITE THE EXIT PLAN (Category 3+ Only)

```
EXIT PLAN
────────────────────────────────────────
If this decision turns out wrong, reversal requires:

Reversal Cost Function: R(t) = [from Step 1]

Steps:
  1. [specific action — e.g., "disable feature flag X"]
  2. [specific action — e.g., "run migration script Y in reverse"]
  3. [specific action — e.g., "restore database from snapshot Z"]
  4. [specific action — e.g., "notify stakeholders via channel W"]
  5. [specific action — e.g., "verify system health via dashboard V"]

Timeline:      [estimated reversal time at t=0, t=30, t=90]
  R(0): [time]
  R(30): [time]
  R(90): [time]

Data Risk:     [what could be lost or corrupted during reversal]
  Data Loss Risk: [NONE / LOW / MEDIUM / HIGH]
  Corruption Risk: [NONE / LOW / MEDIUM / HIGH]
  Recovery Procedure: [how to recover if corruption occurs]

Dependencies:  [what/who must coordinate]
  Internal Teams: [list]
  External Vendors: [list]
  User Communication: [required?]

Early Signals: [what observable sign indicates this decision is going wrong]
  Signal 1: [metric/threshold] — Detection: [dashboard/alert] — Action: [what to do]
  Signal 2: [metric/threshold] — Detection: [dashboard/alert] — Action: [what to do]
  Signal 3: [metric/threshold] — Detection: [dashboard/alert] — Action: [what to do]

Monitoring Plan:
  Dashboards: [list]
  Alerts: [list]
  Review Cadence: [daily/weekly/monthly]
  Owner: [role/person]

────────────────────────────────────────
```

**If you cannot write the exit plan — you don't understand the decision well enough to make it.** Return to exploration.

**Artifact:** The exit plan with reversal cost function, timeline, data risk, dependencies, early signals, and monitoring plan.

**CEI Component:** Exit Plan (weight 4.0)

---

### Step 5 — COMMITMENT  (Category 4 Only, NEW)

**NEW IN v2.0** — Verifiable, auditable commitment record.

```
COMMITMENT 
────────────────────────────────────────
 ID: cc_<timestamp>_<hash>
Decision: [what is being committed to]
Category: [4 — CATASTROPHIC]
Reversal Cost: R(∞) = [value] — [Category 4 justification]

Chosen Option: [name]
Alternatives Considered: [list with CIM scores]
  Option A: [name] — CIM: 0.XX — Rejected because: [specific]
  Option B: [name] — CIM: 0.XX — Rejected because: [specific]

Gate Results:
  G1: PASS — [restatement]
  G2: PASS — [approaches, CIM: 0.XX]
  G3: PASS — [assumptions]
  G4: PASS — [failures]
  G5: PASS — [exit plan, R(t)]
  G6: PASS — [rationale, EC: 0.XX]
  G7: PASS — [early signals]
  G8: PASS — [this ]

Early Warning Signals:
  1. [metric] ≥ [threshold] → [action]
  2. [metric] ≥ [threshold] → [action]
  3. [metric] ≥ [threshold] → [action]

Monitoring:
  Dashboard: [URL]
  Alerts: [list]
  Review Cadence: [weekly]
  Owner: [role/person]

User Confirmation:
  Confirmed By: [user identifier]
  Timestamp: [ISO 8601]
  Acknowledgment: "I understand this decision is Category 4 (CATASTROPHIC reversal cost).
                   I have reviewed the exit plan, early warning signals, and alternatives.
                   I authorize this commitment."

Expiration: [date or condition for re-evaluation]
────────────────────────────────────────
```

**Artifact:** `commitment_` — the final gate for Category 4 decisions.

**CEI Component:** Commitment  (weight 5.0)

---

### Step 6 — EARLY WARNING SIGNALS (if `require_early_warning` = true)

**NEW IN v2.0** — Observable signals that a decision is going wrong, defined BEFORE commitment.

```
EARLY WARNING SIGNALS
────────────────────────────────────────
For the chosen option, define signals that would indicate the decision is failing:

Signal 1: [Name]
  Metric: [specific measurable metric — e.g., "p99 latency > 500ms"]
  Threshold: [specific value — e.g., "> 500ms for 5 consecutive minutes"]
  Detection: [how measured — e.g., "Datadog dashboard 'API Latency'"]
  Lead Time: [how early this signal appears before catastrophic failure — e.g., "2 weeks"]
  False Positive Rate: [estimated — e.g., "5%"]
  Action: [specific response — e.g., "trigger rollback procedure Phase 1"]
  Owner: [who responds]

Signal 2: [Name]
  ...

Signal 3: [Name]
  ...

Signal Validation:
  Each signal must be:
  - Observable (measurable without human judgment)
  - Specific (threshold is a number, not "feels slow")
  - Actionable (triggers a defined response)
  - Early (appears before irreversible damage)
  - Low noise (false positive rate < 20%)

Composite Early Warning Index:
  EWI = Σ (Signal_Weight × Signal_Active) / Σ Signal_Weight
  If EWI > 0.7 → ESCALATE (trigger review/rollback)
────────────────────────────────────────
```

**Artifact:** `early_warning_signals` with metrics, thresholds, detection, lead times, actions, and composite index.

**CEI Component:** Early Warning Signals (weight 3.0)

---

### 7 — METRICS: Compute and Output Depth Metrics

#### 7.1 Phase Activation (for ADS)

```json
{
  "phase": 5,
  "skill": "threshold",
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
    "threshold_classification": 2.0,
    "depth_requirement": 1.0,
    "termination_gates": 3.0,
    "exit_plan": 4.0,
    "reversal_cost_function": 4.0,
    "commitment_": 5.0,
    "early_warning_signals": 3.0,
    "total_complexity_weight": 22.0,
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
    "si_total": 0
  }
}
```

#### 7.4 Cognitive Traces

**Reversal Cost Function:**
```json
{
  "type": "reversal_cost_function",
  "decision": "...",
  "category": 3,
  "function": "R(t) = C_fixed + C_variable(t) + C_opportunity(t) + C_risk(t)",
  "parameters": {
    "C_fixed": 10000,
    "C_variable_daily": 500,
    "C_opportunity_daily": 2000,
    "C_risk_probability": 0.1,
    "C_risk_impact": 50000
  },
  "values": {
    "R(0)": 10000,
    "R(30)": 85000,
    "R(90)": 265000,
    "R(365)": 1000000,
    "R(inf)": 1500000
  },
  "blast_radius": "users",
  "category": 3
}
```

**Commitment :** (as defined in Step 5)

**Early Warning Signals:**
```json
{
  "type": "early_warning_signals",
  "signals": [
    {"name": "Latency Spike", "metric": "p99_latency", "threshold": 500, "unit": "ms",
     "detection": "Datadog", "lead_time_days": 14, "fpr": 0.05, "action": "rollback_phase1"},
    {"name": "Error Rate", "metric": "error_rate", "threshold": 0.01, "unit": "ratio",
     "detection": "PagerDuty", "lead_time_days": 7, "fpr": 0.02, "action": "investigate"}
  ],
  "composite_ewi": 0.0,
  "escalation_threshold": 0.7
}
```

#### 7.5 Depth  Contribution

```json
{
  "skill": "threshold",
  "version": "2.0",
  "metrics": {"ads_contribution": 0.XX, "cei": 0.XX, "si": 0, "ec": 0.XX},
  "gates_verified": {"V1": true, "V2": true, "V3": true, "V4": true, "V5": true, "V6": true},
  "limitations": ["..."]
}
```

---

### 8 — GATES: Verify Before Delivery

**MANDATORY** — Verify these gates PASS (all categories as applicable):

| Gate | Check | Pass Condition |
|------|-------|----------------|
| **V1** | Problem Fidelity | Restatement captures user intent |
| **V2** | Alternative Coverage | ≥2/3 approaches with CIM ≥ 0.5 |
| **V3** | Assumption Exposure | C2/C3 assumptions named and rated |
| **V4** | Failure-Mode Analysis | Failure paths identified (NEGATIVE-SPACE) |
| **V5** | Reversibility Plan | Exit plan + R(t) written |
| **V6** | Decision Rationale | Specific rationale + EC ≥ 0.5 |
| **V7** | Early Warning Signals | Observable signals with thresholds defined |
| **V8** | Commitment  | Category 4:  + user confirmation |

**If any gate FAILS:** Return to relevant step and fix. Do not deliver.

---

### 9 — INTERFERENCE: Receive and Provide

**Receive from prior skills:**

| From Skill | Interference | Use |
|------------|--------------|-----|
| TEMPORAL | Regret scenarios | Inform reversal cost function |
| NEGATIVE-SPACE | Critical silences | Define early warning signals |
| PROVENANCE | EC score | Gate G6 threshold |
| DIVERGE | CIM score | Gate G2 threshold |
| ADVERSARY | Fatal attacks | Inform failure-mode analysis |

**Provide to later skills:**

| To Skill | Interference | Minimum ADS Gain |
|----------|--------------|------------------|
| CONDUCTOR | Final commitment verdict | +0.15 |
| META-LEARNING | Decision patterns for policy learning | +0.10 |

**Artifact:** `interference_log` (received and provided).

---

## The Deeper Purpose

This skill creates automatic depth-scaling. Trivial decisions get fast answers. Irreversible decisions get deep exploration. **The gateway prevents the most expensive class of error: confident, fast, wrong, and permanent.** Now it quantifies reversal cost as a function, produces verifiable commitment s, and defines observable early warning signals. Stopping is a decision — this skill ensures it's a considered, measurable, and auditable one.

---

## MATHEMATICS COMPLIANCE

### Phase Activation Output
This skill contributes to Phase 5. It outputs:
```json
{
  "phase": 5,
  "skill": "threshold",
  "artifact_completeness": 0.XX,
  "gate_pass_rate": 0.XX,
  "external_validity": 0.XX,
  "human_eval": 0.XX,
  "phase_activation": 0.XX
}
```

### CEI Components
- Artifacts produced: threshold_classification (2.0), depth_requirement (1.0), termination_gates (3.0), exit_plan (4.0), reversal_cost_function (4.0), commitment_ (5.0), early_warning_signals (3.0)
- Total complexity weight: 22.0

### SI Components
- C2/C3 assumptions: 0
- Contrarian viable: false
- Fatal attacks: 0
- Boundary violations: 0
- Assumption reversals: 0

### Cognitive Traces Produced
- [x] Reversal Cost Function
- [x] Commitment 
- [x] Early Warning Signals
- [ ] Decision Landscape

### Gates Verified
- [x] V1  [x] V2  [x] V3  [x] V4  [x] V5  [x] V6
- [x] V7  [x] V8 (Category 4)
- [ ] Human Eval  [ ] Held-Out  [ ] Ensemble

### Required Interferences
- From TEMPORAL: Regret scenarios → reversal cost function
- From NEGATIVE-SPACE: Critical silences → early warning signals
- From PROVENANCE: EC score → Gate G6
- From DIVERGE: CIM score → Gate G2
- From ADVERSARY: Fatal attacks → Gate G4