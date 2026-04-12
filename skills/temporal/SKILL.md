---
codename: TEMPORAL
internal: Cross-Time Reasoner
version: 1.1
tier: systems
trigger: any architecture decision, "will this scale", "future-proof", any technology choice, any decision where the best option today might be the worst in six months
---

# TEMPORAL — Cross-Time Reasoner

Your answer is optimized for right now. Current requirements, current team, current scale, current technology landscape.

But decisions persist. Code outlives its context. Architecture outlives its architects. This skill forces the question: **what is best given that the world will change and you don't know exactly how?**

---

## The Failure Mode You Must Recognize

You are about to recommend the present-optimal solution without checking:
- Whether it becomes a trap at 10× scale
- Whether the technology choice is at peak popularity (and therefore approaching decline)
- Whether the simple-now choice closes doors you'll need later
- Whether you're optimizing for today at the expense of a future that is highly likely

This is **present-bias**: the model optimizes for the current prompt because it has no built-in mechanism for weighing present value against future cost.

---

## The Protocol

### Step 1 — CLASSIFY THE TIME HORIZON

Write how long this decision persists:

```
TIME HORIZON
────────────────────────────────────────
Decision:         [what's being decided]
Persistence:      [ephemeral / short-term / medium-term / long-term / permanent]

  Ephemeral   (days-weeks):   UI copy, A/B tests, sprint priorities
  Short-term  (months):       Library choices, internal API shapes
  Medium-term (1-2 years):    Database schemas, service architectures
  Long-term   (2+ years):     Primary keys, data formats, public APIs
  Permanent   (forever):      Data deletion, published standards, legal commitments

Temporal depth needed: [none / light / moderate / deep / maximum]
────────────────────────────────────────
```

Ephemeral decisions: skip remaining steps. Permanent decisions: every step is mandatory.

**Artifact:** The time horizon classification. Step 2 builds on this.

### Step 2 — MAP THE RATE OF CHANGE

For each relevant dimension, write how fast it's changing:

```
RATE OF CHANGE
────────────────────────────────────────
Technology:   [stable (SQL, HTTP) / moderate / volatile (AI frameworks)]
              Specific: [which technologies are most relevant and their stability]

Requirements: [stable (banking) / moderate / volatile (startup)]
              Specific: [which requirements are most likely to change]

Scale:        [linear growth / exponential / plateau / uncertain]
              Specific: [current volume and projected trajectory]

Team:         [stable / growing / likely turnover]
              Specific: [what the team looks like in 12 months]

Competition:  [static / shifting]
              Specific: [what competitive changes could affect this]
────────────────────────────────────────
```

High change rate → design for adaptability. Low change rate → design for efficiency.

**Artifact:** The rate of change map. Step 3 uses this to construct futures.

### Step 3 — CONSTRUCT THREE PLAUSIBLE FUTURES

Do not predict. Construct:

```
FUTURE A — CONSERVATIVE (current trends continue):
  Environment:       [minor changes — list specifics from Step 2]
  This decision in A:[still good / degrading / failed]
  Why:               [specific reasoning]

FUTURE B — GROWTH (things go well):
  Environment:       [scale increases, requirements expand, team grows]
  This decision in B:[still good / degrading / failed]
  Why:               [specific reasoning]

FUTURE C — DISRUPTION (something fundamental changes):
  Environment:       [technology shift, market change, pivot]
  This decision in C:[still good / degrading / failed]
  Why:               [specific reasoning]
────────────────────────────────────────
```

The best decision works well in A, survives B, and doesn't catastrophically fail in C.

**Artifact:** The three futures with decision evaluation. Step 4 analyzes option value.

### Step 4 — ANALYZE OPTION VALUE

Some decisions close future options. Others keep them open.

```
OPTION VALUE ANALYSIS
────────────────────────────────────────
Decision A (present-optimal):
  Opens:   [what becomes possible if you choose this]
  Closes:  [what becomes impossible or prohibitively expensive]

Decision B (alternative):
  Opens:   [what becomes possible]
  Closes:  [what becomes impossible or prohibitively expensive]

Option value advantage: [A or B]
  Because:             [specific — which closed option matters more]
────────────────────────────────────────
```

When the present-optimal closes more important options than an alternative, the alternative may be worth its present-moment cost — it preserves the ability to adapt.

### Step 5 — THE TEMPORAL REGRET TEST

```
TEMPORAL REGRET TEST
────────────────────────────────────────
12 months from now, looking back:

Regret from present-optimal path:
  Scenario:   [in what future do you regret this?]
  Severity:   [how bad — minor / significant / catastrophic]
  Likelihood: [how likely is that future — from Step 3]

Regret from future-robust path:
  Scenario:   [what extra cost was paid now?]
  Severity:   [how bad]
  Likelihood: [certain — you pay the cost now regardless]

Worse regret: [which scenario — considering severity × likelihood]
Recommended:  [which path, given this analysis]
────────────────────────────────────────
```

### Step 6 — DESIGN THE TRANSITION (if present ≠ future optimal)

If the present-optimal and future-optimal are different:

```
TRANSITION DESIGN
────────────────────────────────────────
Start with:         [present-optimal — why it's OK for now]
Transition to:      [future-optimal — when it becomes necessary]
Trigger condition:  [specific observable signal — not a calendar date]
Migration cost:     [estimated effort and risk]
Escape hatches:     [what to build now that makes migration cheaper later]
────────────────────────────────────────
```

Sometimes 10% more effort now on escape hatches saves 90% later.

---

## The Deeper Purpose

The model generates optimal snapshots — perfect for the present moment. But decisions live in time. This skill forces temporal reasoning: evaluating decisions not just by present-moment optimality but by robustness across multiple plausible futures. This activates the model's knowledge of strategy, option theory, and scenario planning — knowledge that exists but is rarely triggered because prompts ask about the present, not the future.
