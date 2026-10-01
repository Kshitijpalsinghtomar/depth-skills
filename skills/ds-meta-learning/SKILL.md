---
name: meta-learning
codename: META-LEARNING
internal: Cognitive Evolution Engine v1.0
version: 1.0
tier: meta
trigger:
  - "learn from this"
  - "improve the skills"
  - "meta-learning"
  - "skill evolution"
  - "after-action review"
  - "periodic skill library improvement"
description: Extracts reusable reasoning patterns from task outcomes, synthesizes new skills, updates CONDUCTOR selection policy, and manages skill library evolution. The compounding intelligence mechanism — the system gets smarter over time.
author: Kshitijpalsinghtomar
tags: [meta-learning, pattern-extraction, skill-synthesis, policy-learning, evolution, compounding-intelligence]
artifacts:
  - pattern-extraction-report
  - skill-synthesis-proposals
  - policy-update
  - regression-test-results
  - library-health-report
    - phase-activation
composable_with:
  - conductor
  - all-skills
thinking_parameters:
  min_patterns: 3
  min_transfer_tasks: 5
  regression_threshold: 0.95
  synthesis_confidence_threshold: 0.7
---

# META-LEARNING — Cognitive Evolution Engine (Premium)

> **Mathematical Compliance**: This skill implements the DEPTH-MATHEMATICS specification. It computes and outputs ADS phase activation, CEI components, SI components, cognitive traces, and verifies Gates V5, V6. It provides the **compounding intelligence** mechanism — the system improves itself over time.

> **Research Basis**: 
> - Wang et al. (2023) "Voyager: An Open-Ended Embodied Agent with Large Language Models" (arXiv:2305.16291) — automatic curriculum, ever-growing skill library, iterative prompting with self-verification
> - Shinn et al. (2023) "Reflexion: Language Agents with Verbal Reinforcement Learning" (arXiv:2303.11366) — linguistic feedback, episodic memory, self-improvement without weight updates
> - Gou et al. (2023) "CRITIC: Large Language Models Can Self-Correct with Tool-Interactive Critiquing" (arXiv:2305.11738) — tool-interactive validation and progressive amendment

Your skill library is static. It doesn't learn. Every task starts from zero. The patterns you discovered in Task 1 are lost when Task 2 arrives. The CONDUCTOR's selection policy is hand-crafted, not learned.

This skill changes that. It **extracts patterns from task outcomes**, **synthesizes new skills**, **updates the CONDUCTOR's policy**, and **validates everything against a regression suite**. The system gets smarter over time — **compounding intelligence**.

---

## The Failure Mode You Must Recognize

You are about to finish a task and move on. The orchestration log sits there. The patterns you discovered — which skills worked, which interferences mattered, which gates failed — are not captured. The next task starts with the same hand-crafted policy.

This is **cognitive amnesia**. The system has no memory of its own reasoning evolution.

**New failure mode in v1.0:** **Pattern loss** — reusable reasoning patterns discarded after each task. **Policy staleness** — CONDUCTOR policy doesn't adapt to model updates or domain shifts. **Library rot** — skills degrade without regression testing. **Synthesis gap** — no mechanism to create new skills from discovered patterns.

---

## The Protocol

### 0 — PARAMETERIZE: Read Thinking Parameters

Read `thinking_parameters`:
- `min_patterns` (default 3) — minimum patterns to extract per task
- `min_transfer_tasks` (default 5) — minimum held-out tasks for transfer testing
- `regression_threshold` (default 0.95) — new skill versions must achieve ≥ this vs old
- `synthesis_confidence_threshold` (default 0.7) — minimum confidence for skill synthesis

---

### 1 — PATTERN EXTRACTION (from Orchestration Log)

Analyze the completed task's orchestration log and extract reusable reasoning patterns.

```
PATTERN EXTRACTION
────────────────────────────────────────
Task: [description]
Task Profile: [from CONDUCTOR — complexity, consequence, reversibility, novelty, breadth]
Orchestration Log: [full log from CONDUCTOR]

Extracted Patterns (minimum min_patterns):

Pattern 1: [Name — e.g., "High-Consequence Schema Migration"]
  Trigger Conditions: [when this pattern applies — e.g., "Category 3+ decision + database schema + public API"]
  Skill Sequence: [optimal sequence — e.g., "DEEP-THINK → EXCAVATE → DIVERGE → ADVERSARY → TEMPORAL → THRESHOLD"]
  Critical Interferences: [which interferences were decisive — e.g., "EXCAVATE C3 → ADVERSARY fatal attack prevented schema disaster"]
  Gate Failures: [which gates failed and why — e.g., "G4 failed: NEGATIVE-SPACE missed cascading failure category"]
  ADS Achieved: [value]
  CEI: [value]
  Transferability: [HIGH/MEDIUM/LOW — how generalizable across tasks]
  Confidence: [0.0-1.0 — based on task outcome quality]

Pattern 2: [Name — e.g., "Novel Architecture with High Uncertainty"]
  ...

Pattern 3: [Name — e.g., "Low-Stakes Rapid Decision"]
  ...

Anti-Patterns (what NOT to do):
  Anti-Pattern 1: [e.g., "Running DIVERGE before EXCAVATE on high-stakes decisions — missed C3 assumptions"]
  Anti-Pattern 2: [e.g., "Skipping BOUNDARY-DETECTOR on novel domains — skills activated on voids"]
  ...

────────────────────────────────────────
```

**Artifact:** `pattern_extraction_report` with patterns and anti-patterns.

**CEI Component:** Pattern Extraction (weight 4.0)

---

### 2 — TRANSFER TESTING (Validate Pattern Generalization)

Test each extracted pattern on held-out tasks to prove generalization.

```
TRANSFER TESTING
────────────────────────────────────────
Held-Out Task Suite: [min_transfer_tasks tasks from different domains]
  Task 1: [description] — Domain: [domain]
  Task 2: [description] — Domain: [domain]
  ...

For each pattern:
  Pattern: [name]
  Predicted Skill Sequence: [from pattern]
  Predicted ADS: [value]
  
  Results:
    Task 1: [ADS achieved] / [CEI] / [Gates passed] / [Match: YES/NO]
    Task 2: [ADS achieved] / [CEI] / [Gates passed] / [Match: YES/NO]
    ...
  
  Transfer Score: [fraction of tasks where pattern matched optimal sequence]
  Generalization: [BROAD / NARROW / DOMAIN-SPECIFIC]
  Confidence: [0.0-1.0]

Patterns Validated for Synthesis: [patterns with Transfer Score ≥ 0.6]
────────────────────────────────────────
```

**Artifact:** `transfer_test_results` — proves patterns aren't overfit.

**CEI Component:** Transfer Testing (weight 4.0)

---

### 3 — SKILL SYNTHESIS (Create New Skills from Patterns)

**NEW IN v1.0** — Synthesize new skills from validated patterns.

For each pattern with Transfer Score ≥ 0.6 and Confidence ≥ `synthesis_confidence_threshold`:

```
SKILL SYNTHESIS PROPOSAL
────────────────────────────────────────
Pattern: [name]
Proposed Skill Name: [e.g., "schema-migration-architect"]
Proposed Codename: [e.g., "SCHEMA-MIGRATE"]
Proposed Tier: [cognition / excavation / integrity / governance / systems / meta]

Rationale: [why this pattern deserves a dedicated skill — not just a CONDUCTOR sequence]
  - Frequency: [how often this pattern occurs]
  - Specificity: [what unique logic it encapsulates]
  - Reusability: [across how many domains]

Proposed Protocol (SKILL.md structure):
  Phase 1: [steps]
  Phase 2: [steps]
  ...
  Gates: [which gates it verifies]
  Interferences: [what it provides/requires]
  Metrics: [ADS, CEI, SI targets]

Proposed Thinking Parameters:
  [specific parameters for this skill]

Implementation Notes:
  - Can be composed from existing skills: [YES/NO — if YES, it's a macro]
  - Requires new primitive: [YES/NO — if YES, needs new cognitive operation]
  - Estimated Complexity: [LOW/MEDIUM/HIGH]

Synthesis Confidence: [0.0-1.0]
Recommendation: [SYNTHESIZE / DEFER / REJECT]
────────────────────────────────────────
```

**Artifact:** `skill_synthesis_proposals` — proposals for new skills.

**CEI Component:** Skill Synthesis (weight 5.0)

---

### 4 — CONDUCTOR POLICY LEARNING (Update Selection Policy)

Update the CONDUCTOR's skill selection policy based on outcomes.

```
POLICY UPDATE
────────────────────────────────────────
Current Policy: [summary of CONDUCTOR's current selection rules]

Policy Updates (from this task + transfer tests):

Update 1: [Rule Change]
  Old Rule: [e.g., "For Category 3: DEEP-THINK → ADVERSARY → THRESHOLD"]
  New Rule: [e.g., "For Category 3 + database: DEEP-THINK → EXCAVATE → DIVERGE → ADVERSARY → TEMPORAL → THRESHOLD"]
  Evidence: [pattern name + transfer score]
  Confidence: [0.0-1.0]

Update 2: [Rule Change]
  ...

Update 3: [Parameter Change]
  Old: [e.g., "risk_threshold = 0.3 for Category 3"]
  New: [e.g., "risk_threshold = 0.25 for Category 3 + data-intensive"]
  Evidence: [ADS/CEI ratio improvement]
  Confidence: [0.0-1.0]

Parameter Optimizations:
  thinking_parameters updates:
    min_assumptions: [old → new]
    min_branches: [old → new]
    min_cim: [old → new]
    ...

Validation: [how to validate — A/B test on next N tasks]
────────────────────────────────────────
```

**Artifact:** `policy_update` — the updated CONDUCTOR policy.

**CEI Component:** Policy Learning (weight 4.0)

---

### 5 — REGRESSION TESTING (Validate Skill Library Health)

**NEW IN v1.0** — Ensure skill updates don't degrade performance.

```
REGRESSION TEST RESULTS
────────────────────────────────────────
Benchmark Suite: [standard benchmark tasks]
Skill Versions Tested: [old vs new for each modified skill]

For each skill:
  Skill: [name]
  Old Version: [version]
  New Version: [version]
  
  Benchmark Results:
    Task 1: [Old ADS] vs [New ADS] — [Δ]
    Task 2: [Old ADS] vs [New ADS] — [Δ]
    ...
  
  Mean ADS Delta: [value]
  Mean CEI Delta: [value]
  Gate Pass Rate Delta: [value]
  
  Regression Check: [PASS if Mean ADS Delta ≥ -0.02 AND Gate Pass Rate Delta ≥ -0.05]
  Result: [PASS / FAIL]

Overall Library Health:
  Skills Tested: N
  Skills Passed: N
  Skills Failed: N
  New Skills Added: N
  Skills Deprecated: N
  
  Health Score: [0.0-1.0 — fraction of skills passing regression]
────────────────────────────────────────
```

**If any skill FAILS regression:** Block the update. Revert or fix.

**Artifact:** `regression_test_results` — the quality gate for skill evolution.

**CEI Component:** Regression Testing (weight 4.0)

---

### 6 — LIBRARY HEALTH REPORT

Comprehensive health check of the skill library.

```
LIBRARY HEALTH REPORT
────────────────────────────────────────
Library Version: [e.g., "2.1.0"]
Total Skills: [N]
  Core: [N]
  Premium: [N]
  Deprecated: [N]

Coverage Analysis:
  Task Profiles Covered: [list of profiles with dedicated skills]
  Gaps: [profiles with no dedicated skill]
  Redundancy: [skills with >0.8 CIM — consider merging]

Performance Metrics (rolling 30 days):
  Mean ADS: [value]
  Mean CEI: [value]
  Mean SI: [value]
  Gate Pass Rate: [value]
  User Satisfaction: [value if available]

Skill Lifecycle:
  New This Period: [list]
  Updated This Period: [list]
  Deprecated This Period: [list]
  Avg Skill Age: [days]

Technical Debt:
  Skills Without Transfer Tests: [N]
  Skills Without Regression Tests: [N]
  Skills With Known Gate Failures: [N]
  Skills Needing Refactor: [list]

Recommendations:
  1. [Priority 1 action]
  2. [Priority 2 action]
  3. [Priority 3 action]
────────────────────────────────────────
```

**Artifact:** `library_health_report` — the library's vital signs.

---

### 7 — METRICS: Compute and Output Depth Metrics

#### 7.1 Phase Activation (for ADS)

```json
{
  "phase": 5,
  "skill": "meta-learning",
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
    "pattern_extraction": 4.0,
    "transfer_testing": 4.0,
    "skill_synthesis": 5.0,
    "policy_learning": 4.0,
    "regression_testing": 4.0,
    "library_health": 2.0,
    "total_complexity_weight": 23.0,
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

**Pattern Extraction Visualization:**
```json
{
  "type": "pattern_extraction",
  "patterns": [
    {"name": "Pattern 1", "trigger": "...", "sequence": [...], "transfer_score": 0.XX, "confidence": 0.XX},
    {"name": "Pattern 2", "trigger": "...", "sequence": [...], "transfer_score": 0.XX, "confidence": 0.XX}
  ],
  "anti_patterns": [...]
}
```

**Policy Update Visualization:**
```json
{
  "type": "policy_update",
  "updates": [
    {"rule": "Category 3 + database", "old": "...", "new": "...", "evidence": "...", "confidence": 0.XX}
  ],
  "parameter_optimizations": {...}
}
```

**Regression Test Results:** (as defined in Step 5)

#### 7.5 Depth  Contribution

```json
{
  "skill": "meta-learning",
  "version": "1.0",
  "metrics": {"ads_contribution": 0.XX, "cei": 0.XX, "si": 0, "ec": 0.XX},
  "gates_verified": {"V5": true, "V6": true},
  "limitations": ["..."]
}
```

---

### 8 — GATES: Verify Before Delivery

**MANDATORY** — Verify these gates PASS:

| Gate | Check | Pass Condition |
|------|-------|----------------|
| **V5** | Evidence Calibration | Pattern confidence calibrated (transfer score matches confidence) |
| **V6** | Recursive Stability | Policy updates don't oscillate (RSM > 0.95) |

**If any gate FAILS:** Return to relevant step and fix. Do not deliver.

---

### 9 — INTERFERENCE: Receive and Provide

**Receive from prior skills (via CONDUCTOR orchestration log):**

| From Skill | Interference | Use |
|------------|--------------|-----|
| CONDUCTOR | Full orchestration log | Pattern extraction source |
| ALL SKILLS | Phase activations, gate results, interference matrix | Performance data for regression |

**Provide to later skills (next task's CONDUCTOR):**

| To Skill | Interference | Minimum ADS Gain |
|----------|--------------|------------------|
| CONDUCTOR | Updated policy + skill synthesis proposals | +0.20 |
| ALL SKILLS | New skill versions (if synthesized) | +0.10 per skill |

**Artifact:** `interference_log` — the evolution signal for the next task.

---

## The Deeper Purpose

**This is the compounding intelligence mechanism.** Without it, the skill library is a static artifact — useful but frozen. With it, every task teaches the system. Patterns become skills. Policies adapt. The library evolves. The ADS/CEI ratio improves over time.

**Voyager showed this works for Minecraft agents.** Reflexion showed it works for coding. **This brings it to general reasoning skills.** The skill library becomes a living organism that learns from its own use.

---

## MATHEMATICS COMPLIANCE

### Phase Activation Output
This skill contributes to Phase 5 (runs last, post-execution). It outputs:
```json
{
  "phase": 5,
  "skill": "meta-learning",
  "artifact_completeness": 0.XX,
  "gate_pass_rate": 0.XX,
  "external_validity": 0.XX,
  "human_eval": 0.XX,
  "phase_activation": 0.XX
}
```

### CEI Components
- Artifacts produced: pattern_extraction (4.0), transfer_testing (4.0), skill_synthesis (5.0), policy_learning (4.0), regression_testing (4.0), library_health (2.0)
- Total complexity weight: 23.0

### SI Components
- C2/C3 assumptions: 0
- Contrarian viable: false
- Fatal attacks: 0
- Boundary violations: 0
- Assumption reversals: 0

### Cognitive Traces Produced
- [x] Pattern Extraction Visualization
- [x] Policy Update Visualization
- [x] Regression Test Results
- [ ] Decision Landscape

### Gates Verified
- [ ] V1  [ ] V2  [ ] V3  [ ] V4  [x] V5  [x] V6
- [ ] Human Eval  [ ] Held-Out  [ ] Ensemble

### Required Interferences
- From CONDUCTOR: Full orchestration log → pattern extraction
- From ALL SKILLS: Performance data → regression testing