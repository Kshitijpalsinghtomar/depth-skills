---
name: diverge
codename: DIVERGE
internal: Path Divergence v2.0
version: 2.0
tier: cognition
trigger: what's the best way to, "how should I", design choice, architecture decision, any time the model is about to commit to one path
description: Forces generation of genuinely different solution paths before committing, preventing single-path pattern gravity. Now with MCTS exploration, independence verification (CIM), transfer testing, and mathematical depth metrics.
author: Kshitijpalsinghtomar
tags: [alternatives, exploration, architecture, pattern-gravity, options, mcts, independence, transfer, metrics]
artifacts:
  - path-map
  - divergence-test
  - stress-comparison
  - mcts-exploration-log
  - independence-verification
  - transfer-test-results
  - decision-landscape
    - phase-activation
composable_with: [deep-think, adversary, threshold, reframe, conductor, excavate, invert]
thinking_parameters:
  min_branches: 3
  min_contrarian: 1
  mcts_simulations: 10
  min_cim: 0.5
  require_transfer_test: true
  require_mcts: true
---

# DIVERGE v2.0 — Path Divergence (Premium)

> **Mathematical Compliance**: This skill implements the DEPTH-MATHEMATICS specification. It computes and outputs ADS phase activation, CEI components, SI components, cognitive traces (decision landscape, MCTS exploration log), and verifies Gates V2, V4. It uses MCTS for exploration and CIM for independence verification.

> **Best used after DEEP-THINK.** DEEP-THINK explores the solution space. DIVERGE stress-tests specific paths with MCTS-guided exploration.

The first solution you think of has the highest **pattern gravity** — most frequently activated, most consistently rewarded. It surfaces before search begins. It was retrieved from memory, not discovered through exploration.

It might be correct. But you cannot know that without seeing what else exists. And you cannot see what else exists if you've already committed.

**New in v2.0:** MCTS-guided exploration finds paths human intuition misses. CIM (Compositional Independence Metric) mathematically verifies paths are genuinely different. Transfer testing proves paths generalize.

---

## The Failure Mode You Must Recognize

You are about to present "three options" that are:
- The same architecture with different libraries (React vs Vue vs Svelte)
- The same strategy with different timelines (do it now vs later vs incrementally)
- The same approach with different parameters (cache TTL of 5min vs 10min vs 30min)

This is **convergence wearing a costume**. Three flavors of one answer is not three approaches. Real divergence requires paths that disagree about what the problem IS, not just how to implement one interpretation of it.

**Cargo cult divergence** produces path cards that look different but have CIM < 0.3. This skill rejects them.

---

## The Protocol

### 0 — PARAMETERIZE: Read Thinking Parameters

Read `thinking_parameters`:
- `min_branches` (default 3) — minimum paths to generate
- `min_contrarian` (default 1) — minimum contrarian paths
- `mcts_simulations` (default 10) — MCTS exploration depth
- `min_cim` (default 0.5) — minimum Compositional Independence Metric
- `require_transfer_test` (default true) — test on held-out tasks
- `require_mcts` (default true) — use MCTS for exploration

---

### 1 — WRITE PATHS THAT DISAGREE ABOUT WHAT MATTERS (Minimum = `min_branches`)

Each path must differ from the others on at least ONE of these dimensions:
- **Optimization target:** Path A optimizes for speed, Path B for correctness, Path C for simplicity
- **Problem framing:** Path A treats this as a scaling problem, B as a design problem, C as a workflow problem
- **Core abstraction:** Path A is event-driven, Path B is request-response, Path C is polling

**Divergence verification:** After writing all paths, compute **CIM** (Compositional Independence Metric):
```
CIM = 1 - (2 / (n(n-1))) × Σ_{i<j} Cosine_Similarity(embedding(path_i), path_j)
```
**If CIM < `min_cim`:** Discard the most similar path and generate a genuinely different one. Repeat until CIM ≥ `min_cim`.

For each path, fill in this card completely:

```
PATH [N]: [name — the principle this path follows]
────────────────────────────────────────
Optimizes for:       [specific thing — not "good performance" but "write throughput"]
Key assumption:      [the condition that must be true for this path to be correct]
What it sacrifices:  [specific capability that this path cannot provide]
Breaks when:         [specific input, scale, or condition that causes failure]
Migration cost out:  [how hard is it to switch AWAY from this path if it's wrong]
Embedding:           [vector representation for CIM computation]
────────────────────────────────────────
```

**Artifact:** Path cards (minimum `min_branches`, CIM ≥ `min_cim`).

**CEI Component:** Path Cards (weight 3.0 each)

---

### 2 — MCTS EXPLORATION (if `require_mcts` = true)

**NEW IN v2.0** — Use Monte Carlo Tree Search to explore the path space beyond human intuition.

```
MCTS EXPLORATION
────────────────────────────────────────
Root State: [current problem framing]
Simulations: [mcts_simulations]
Exploration Constant: 1.414 (sqrt(2))

For each simulation:
  1. SELECT: Traverse tree using UCB1 until leaf
  2. EXPAND: Generate child nodes (new problem framings / abstractions)
  3. SIMULATE: Rollout to terminal state (quick heuristic evaluation)
  4. BACKPROPAGATE: Update visit counts and values

Best Paths Discovered:
  [List paths found by MCTS that were not in initial set]
  For each: [framing, abstraction, UCB score, visit count]

Paths Added to Portfolio: [which MCTS paths added to Step 1 paths]
────────────────────────────────────────
```

**MCTS Node Definition:**
- **State:** Problem framing + chosen abstraction + partial path
- **Action:** Choose new framing / abstraction / optimization target
- **Reward:** Heuristic score (novelty × feasibility × potential impact)
- **Terminal:** Complete path card generated

**Artifact:** `mcts_exploration_log` with tree statistics, discovered paths, UCB scores.

**CEI Component:** MCTS Exploration (weight 5.0)

---

### 3 — STRESS EACH PATH AGAINST FIVE SCENARIOS

For EACH path (including MCTS-discovered), write one sentence per scenario:

```
STRESS TEST — PATH [N]
────────────────────────────────────────
At 10× scale:              [what degrades or fails]
If main requirement changes:[what breaks or must be rebuilt]
Debugging experience:       [what troubleshooting looks like when it goes wrong]
New developer in 6 months:  [what they struggle with]
If you're wrong about it:   [what the migration path looks like]
────────────────────────────────────────
```

**Artifact:** Stress-test answers (5 per path).

**CEI Component:** Stress Tests (weight 2.0 per path)

---

### 4 — WRITE CONTRARIAN PATHS (Minimum = `min_contrarian`)

**NEW IN v2.0** — Your paths probably share at least one unexamined assumption. Identify it and write contrarian paths that violate it.

**Finding the shared assumption:**
- Write one sentence about what all paths take for granted about the data model, the architecture, the user, or the scale
- Ask: what if that shared assumption is wrong?
- Write a path that exists in the world where it IS wrong

```
SHARED ASSUMPTION: [what all paths take for granted]
PATH [N] (contrarian): [name]
  What if:           [the shared assumption is false]
  Solution:          [what approach emerges when you remove it]
  Viability:         [realistic / stretch / moonshot]
  CIM vs Portfolio:  [CIM with existing paths — must be ≥ min_cim]
────────────────────────────────────────
```

If contrarian path is viable — you nearly committed to a shared blind spot.

**Artifact:** Contrarian paths (minimum `min_contrarian`).

**SI Component:** Contrarian viable (true/false)

---

### 5 — INDEPENDENCE VERIFICATION (CIM)

**NEW IN v2.0** — Mathematically verify path independence.

```
INDEPENDENCE VERIFICATION
────────────────────────────────────────
Paths Analyzed: [N]
Embedding Method: [sentence-transformers / custom / LLM-based]
Pairwise Similarities:
  Path 1 vs Path 2: 0.XX
  Path 1 vs Path 3: 0.XX
  Path 2 vs Path 3: 0.XX
  ...

CIM = 1 - (2 / (n(n-1))) × Σ similarities = 0.XX

Threshold: [min_cim]
Result: [PASS / FAIL]

If FAIL: [which paths too similar, what regeneration needed]
────────────────────────────────────────
```

**If FAIL:** Regenerate most similar paths until PASS.

**Artifact:** `independence_verification` with CIM score and pairwise matrix.

---

### 6 — TRANSFER TESTING (if `require_transfer_test` = true)

**NEW IN v2.0** — Test paths on held-out tasks to prove generalization.

```
TRANSFER TEST RESULTS
────────────────────────────────────────
Held-Out Tasks: [list of 3-5 tasks from different domain]
For each path:
  Path [N]: [name]
    Task 1: [score/result] — [generalizes / fails / partial]
    Task 2: [score/result] — [generalizes / fails / partial]
    ...
  Transfer Score: [average across tasks]
  Generalization: [broad / narrow / domain-specific]

Best Transfer Path: [Path N]
────────────────────────────────────────
```

**Artifact:** `transfer_test_results` — proves paths aren't overfit to current problem.

**CEI Component:** Transfer Testing (weight 4.0)

---

### 7 — SELECT AND JUSTIFY FOR THIS SPECIFIC CONTEXT

From all paths (initial + MCTS + contrarian), select one. Write:

- **Why this path fits THESE constraints** — reference specific context, not generic advantages
- **Under what conditions a different path would be better** — be specific: "If [X changes], switch to Path [N]"
- **What the chosen path sacrifices** — name it. The user deserves to know.
- **Earliest warning signal** — what is the first observable sign that this path is becoming wrong?

```
DIVERGENCE DECISION
────────────────────────────────────────
Selected:     PATH [N]
Reason:       [specific to THIS context — not "it's the best"]
Sacrifices:   [what you lose]
Switch when:  [specific trigger condition → switch to PATH [M]]
Watch for:    [earliest signal of trouble]
Reversibility:[trivial / moderate / hard] → [depth appropriate?]
CIM:          [final CIM score]
Transfer:     [transfer score]
────────────────────────────────────────
```

---

### 8 — DECISION LANDSCAPE TOPOLOGY

**NEW IN v2.0** — Visualize the decision space.

```
DECISION LANDSCAPE
────────────────────────────────────────
Paths: [list all paths with names]
Dimensions: [Present, Growth, Disruption, Long-term] (from TEMPORAL interference)
Profiles:
  Path A: [0.9, 0.6, 0.2, 0.1]  # peaks now, cliffs at disruption
  Path B: [0.6, 0.8, 0.7, 0.8]  # robust across futures
  Path C: [0.3, 0.4, 0.9, 0.7]  # contrarian, wins in disruption
  Path D: [0.7, 0.8, 0.8, 0.8]  # hybrid, best option value

Recommended: [Path D]
Escape Hatches: [trigger conditions for switching]
────────────────────────────────────────
```

**Artifact:** `decision_landscape` — for cognitive trace.

---

### 9 — METRICS: Compute and Output Depth Metrics

#### 9.1 Phase Activation (for ADS)

```json
{
  "phase": 2,
  "skill": "diverge",
  "artifact_completeness": 0.XX,
  "gate_pass_rate": 0.XX,
  "external_validity": 0.XX,
  "human_eval": 0.XX,
  "phase_activation": 0.XX
}
```

#### 9.2 CEI Components

```json
{
  "cei_components": {
    "path_cards": 3.0,
    "mcts_exploration": 5.0,
    "stress_tests": 2.0,
    "contrarian_paths": 4.0,
    "independence_verification": 3.0,
    "transfer_testing": 4.0,
    "decision_landscape": 2.0,
    "total_complexity_weight": 23.0,
    "output_tokens": N,
    "wall_time_seconds": T,
    "cei": 0.XX
  }
}
```

#### 9.3 SI Components

```json
{
  "si_components": {
    "c2_c3_count": 0,
    "contrarian_viable": true/false,
    "fatal_attacks": 0,
    "boundary_violations": 0,
    "assumption_reversals": 0,
    "si_total": 1/0
  }
}
```

#### 9.4 Cognitive Traces

**Decision Landscape:** (as above)

**MCTS Exploration Log:**
```json
{
  "type": "mcts_exploration_log",
  "root_state": "...",
  "simulations": 10,
  "nodes_explored": N,
  "best_paths_discovered": [
    {"framing": "...", "abstraction": "...", "ucb_score": 0.XX, "visits": N}
  ],
  "paths_added": [...]
}
```

#### 9.5 Depth  Contribution

```json
{
  "skill": "diverge",
  "version": "2.0",
  "metrics": {"ads_contribution": 0.XX, "cei": 0.XX, "si": N, "ec": 0.XX},
  "gates_verified": {"V2": true, "V4": true},
  "limitations": ["..."]
}
```

---

### 10 — GATES: Verify Before Delivery

**MANDATORY** — Verify these gates PASS:

| Gate | Check | Pass Condition |
|------|-------|----------------|
| **V2** | Alternative Independence | CIM ≥ `min_cim` (default 0.5) |
| **V4** | Temporal Consistency | If TEMPORAL ran: chosen path survives ≥2/3 futures (from TEMPORAL interference) |

**If any gate FAILS:** Return to relevant step and fix. Do not deliver.

---

### 11 — INTERFERENCE: Receive and Provide

**Receive from prior skills:**

| From Skill | Interference | Use |
|------------|--------------|-----|
| DEEP-THINK | Assumptions from Step 2 | Seed Path 4 (contrarian) |
| EXCAVATE | C2/C3 assumptions | Challenge shared assumptions |
| TEMPORAL | Future scenarios | Stress test dimensions |

**Provide to later skills:**

| To Skill | Interference | Minimum ADS Gain |
|----------|--------------|------------------|
| ADVERSARY | Contrarian path viability | +0.10 (SI component) |
| TEMPORAL | Path profiles across futures | +0.15 (decision landscape) |
| CONDUCTOR | CIM score, transfer results | +0.10 (selection quality) |

**Artifact:** `interference_log` (received and provided).

---

## The Deeper Purpose

Pattern gravity collapses every answer toward the most frequently-seen solution before the model has searched the alternatives. This skill forces genuine search: **MCTS-guided exploration** finds paths human intuition misses. **CIM** mathematically verifies independence. **Transfer testing** proves generalization. The best solution for a specific problem is rarely the most common solution for the general category — and you cannot find it without looking past the first match. **Now you can measure how far you looked.**

---

## MATHEMATICS COMPLIANCE

### Phase Activation Output
This skill contributes to Phase 2. It outputs:
```json
{
  "phase": 2,
  "skill": "diverge",
  "artifact_completeness": 0.XX,
  "gate_pass_rate": 0.XX,
  "external_validity": 0.XX,
  "human_eval": 0.XX,
  "phase_activation": 0.XX
}
```

### CEI Components
- Artifacts produced: path_cards (3.0×N), mcts_exploration (5.0), stress_tests (2.0×N), contrarian_paths (4.0×N), independence_verification (3.0), transfer_testing (4.0), decision_landscape (2.0)
- Total complexity weight: 23.0 + 3.0×(branches-3) + 4.0×contrarian

### SI Components
- C2/C3 assumptions: 0
- Contrarian viable: [true/false from Step 4]
- Fatal attacks: 0
- Boundary violations: 0
- Assumption reversals: 0

### Cognitive Traces Produced
- [ ] Activation Heatmap
- [ ] Assumption Dependency Graph
- [x] Decision Landscape
- [x] MCTS Exploration Log

### Gates Verified
- [ ] V1  [x] V2  [ ] V3  [x] V4  [ ] V5  [ ] V6
- [ ] Human Eval  [ ] Held-Out  [ ] Ensemble

### Required Interferences
- From DEEP-THINK: Assumptions → contrarian path seed
- From EXCAVATE: C2/C3 assumptions → shared assumption challenge
- From TEMPORAL: Future profiles → stress test dimensions