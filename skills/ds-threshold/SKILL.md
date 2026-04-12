---
name: threshold
codename: THRESHOLD
internal: Commitment Gateway
version: 1.1
tier: governance
trigger: "should we go with", "let's just do", "final decision", any schema change, any public API contract, any irreversible deployment
description: Gates commitment on irreversible decisions by measuring reversal cost and enforcing proportional exploration depth.
author: depth-skills
tags: [decisions, irreversibility, commitment, gates, reversal-cost]
artifacts:
  - threshold-classification
  - depth-requirement
  - termination-gates
  - exit-plan
composable_with: [adversary, diverge, temporal, conductor]
---

# THRESHOLD — Commitment Gateway

Not all decisions deserve the same depth. A CSS color choice and a database primary key choice are not the same decision — but without this skill, the model treats them with roughly equal cognitive investment.

This skill creates the gate between thinking and committing. It measures the **reversal cost**, enforces proportional exploration, and requires an exit plan before any high-cost commitment.

---

## The Failure Mode You Must Recognize

You are about to give a quick, confident answer to a decision that:
- Cannot be easily undone (database schema, public API, data deletion)
- Affects many people or systems (blast radius extends beyond the immediate scope)
- Was not explored proportionally (one approach considered, zero alternatives evaluated)

Uniform depth — treating all decisions with the same level of analysis — systematically under-invests in the decisions that matter most.

---

## The Protocol

### Step 1 — CLASSIFY: Write the Reversal Cost

```
THRESHOLD CLASSIFICATION
────────────────────────────────────────
Decision:          [what is being decided — one sentence]

Reversal cost:     [Category 1 / 2 / 3 / 4]
  Category 1 — TRIVIAL (minutes, no coordination):
    Variable names, file organization, CSS values, config
  Category 2 — MODERATE (hours to days, some coordination):
    Indexes, internal API shapes, library versions, service boundaries
  Category 3 — EXPENSIVE (days to weeks, significant coordination):
    Database schemas, public API contracts, auth systems, data formats
  Category 4 — CATASTROPHIC (weeks to months, or impossible):
    Primary keys, data deletion, published standards, architecture at scale

Reversal timeline: [minutes / hours / days / weeks / months / never]
Blast radius:      [self / team / users / ecosystem]
────────────────────────────────────────
```

**When uncertain between two categories, pick the higher one.** The cost of overthinking a reversible decision is wasted time. The cost of underthinking an irreversible one is permanent damage.

**Artifact:** The classification. Step 2 uses this to set the required depth.

### Step 2 — SET REQUIRED DEPTH

Based on the classification:

```
DEPTH REQUIREMENT
────────────────────────────────────────
Category 1 — STANDARD:
  → 1 approach is sufficient. Move fast.
  → Skip remaining steps. Deliver.

Category 2 — ELEVATED:
  → 2 approaches minimum before committing.
  → Document rollback path (1-2 sentences).
  → Run G1-G3 gates (Step 3).

Category 3 — MAXIMUM:
  → 3 approaches minimum (use DIVERGE skill).
  → Full ADVERSARY review of chosen approach.
  → Written rollback plan (Step 4).
  → Run ALL gates G1-G6 (Step 3).

Category 4 — MAXIMUM-PLUS:
  → All Layer 0 skills activated (DEEP-THINK → DIVERGE → ADVERSARY).
  → No commitment without explicit user confirmation.
  → Written rollback plan with timeline and dependencies (Step 4).
  → Run ALL gates. No exceptions.
────────────────────────────────────────
```

**Artifact:** The depth requirement. Step 3 enforces it.

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

G3 — Assumption exposure:
  Are critical assumptions named and rated (C2/C3 from EXCAVATE)?
  [PASS — assumptions listed] / [FAIL — assumptions not surfaced]

G4 — Failure-mode analysis:    (Category 3+ only)
  Are failure paths identified, not just the happy path?
  [PASS — failures: ___] / [FAIL — only happy path]

G5 — Reversibility plan:       (Category 3+ only)
  Is the exit plan written (Step 4)?
  [PASS — plan written] / [FAIL — no exit plan]

G6 — Decision rationale:       (Category 3+ only)
  Can I explain why the chosen option beats alternatives under
  THESE SPECIFIC constraints?
  [PASS — because: ___] / [FAIL — generic reasoning]
────────────────────────────────────────
```

**Any FAIL → return to the relevant step and complete it before shipping.** The gate exists because coherence is not completion and confidence is not evidence.

**Artifact:** The gate results. Failed gates block delivery.

### Step 4 — WRITE THE EXIT PLAN (Category 3+ Only)

```
EXIT PLAN
────────────────────────────────────────
If this decision turns out wrong, reversal requires:

Steps:
  1. [specific action]
  2. [specific action]
  3. [specific action]

Timeline:      [estimated reversal time]
Data risk:     [what could be lost or corrupted during reversal]
Dependencies:  [what/who must coordinate]
Early signal:  [what observable sign indicates this decision is going wrong]
────────────────────────────────────────
```

**If you cannot write the exit plan — you don't understand the decision well enough to make it.** Return to exploration.

---

## The Deeper Purpose

This skill creates automatic depth-scaling. Trivial decisions get fast answers. Irreversible decisions get deep exploration. The gateway prevents the most expensive class of error: confident, fast, wrong, and permanent. Stopping is a decision — this skill ensures it's a considered one.
