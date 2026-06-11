---
name: invert
codename: INVERT
internal: Constraint & Belief Inversion
version: 1.1
tier: excavation

trigger:
  - "we have no choice"
  - "given these constraints"
  - "boxed in"
  - "all options are bad"
  - "are we sure"
  - "what if we're wrong"

description: Flips constraints and beliefs to expose false walls and test plan robustness against inverted worldviews.

author: depth-skills

tags:
  - inversion
  - constraints
  - beliefs
  - robustness
  - counterfactual

artifacts:
  - constraint-map
  - inversion-table
  - load-bearing-beliefs
  - robustness-verdict

composable_with:
  - excavate
  - reframe
  - diverge
  - descend
---

# INVERT — Constraint & Belief Inversion

Two forces trap answers in small spaces: **false constraints** (walls that aren't walls) and **untested beliefs** (foundations that might not be solid). Both feel real from inside. Both can collapse when tested.

This skill flips things. It inverts constraints to find which are real and which are habits. It inverts beliefs to find which are load-bearing and which are replaceable. Then it solves the problem from the opposite world — to discover what only becomes visible from the other side.

---

## Part 1: Constraint Inversion

### Step 1 — WRITE THE CONSTRAINT MAP

List every constraint on THIS problem. For each, classify its type:

```
CONSTRAINT MAP
────────────────────────────────────────
C1: [constraint statement]
    Type:    [physical / legal / economic / policy / habit / assumption]
    Source:  [who stated this? user / me / industry convention / nobody-explicit]
    Hardness:[hard — cannot violate / soft — could be negotiated or removed]

C2: [constraint statement]
    Type:    [type]
    Source:  [source]
    Hardness:[hard / soft]

...

Bottleneck constraint: C[N] — [this is the one most limiting the solution space]
────────────────────────────────────────
```

**Type definitions:**
1. **Physical** — speed of light, conservation laws. Cannot violate.
2. **Legal** — regulations, contracts, compliance. Cannot violate (but can sometimes work around).
3. **Economic** — money, resources, time. Can be traded.
4. **Policy** — internal rules, team decisions. Can be renegotiated.
5. **Habit** — "we always do it this way." Usually invertible without consequence.
6. **Assumption** — inherited from pattern matching. Unknown truth value. Most dangerous type.

**Key insight:** Constraints labeled "physical" are sometimes misclassified "policy" or "habit." If you cannot explain WHY this constraint cannot be violated in terms of physics or law — it's probably softer than you think.

**Artifact:** The constraint map with types and bottleneck identified. Step 2 inverts the bottleneck.

### Step 2 — INVERT THE BOTTLENECK

For the bottleneck constraint (and any "assumption" or "habit" type constraints), run three inversions:

```
INVERSION TABLE — CONSTRAINT C[N]
────────────────────────────────────────
Original: [the constraint as stated]

Full inversion:    [assume the exact opposite is true]
  Solution:        [what approach becomes possible?]
  Safety:          [upside if correct / downside if wrong]

Partial inversion: [relax by 20-40%, not fully remove]
  Solution:        [what opens up?]
  Safety:          [upside / downside]

Temporal inversion:[this holds now but not in 6 months, or vice versa]
  Solution:        [what does the transition path look like?]
  Safety:          [upside / downside]
────────────────────────────────────────
```

**Hard rule:** Never invert physical or legal constraints. DO invert assumptions, habits, and policies — these are the source of most false boxes.

**Artifact:** The inversion table. If any inversion produces a viable solution with acceptable safety — the constraint was false. The solution space just expanded.

---

## Part 2: Belief Inversion

### Step 3 — WRITE THE THREE MOST LOAD-BEARING BELIEFS

A belief is something held as true without significant doubt. Every plan rests on beliefs about reality:

Write the three beliefs that, if wrong, would damage the plan most:

```
LOAD-BEARING BELIEFS
────────────────────────────────────────
B1: [belief statement — e.g., "Users want speed more than features"]
    Evidence for: [why you believe this — be specific]
    Evidence against: [genuine reasons the opposite could be true — not straw men]

B2: [belief statement]
    Evidence for: [specific]
    Evidence against: [genuine]

B3: [belief statement]
    Evidence for: [specific]
    Evidence against: [genuine]
────────────────────────────────────────
```

**The "evidence against" step is the hardest and most important.** You must write real reasons the opposite could be true — not weak dismissable reasons. If you cannot find any evidence against a belief, you haven't looked hard enough.

**Artifact:** Three beliefs with evidence both directions. Step 4 builds on each.

### Step 4 — SOLVE FROM THE OPPOSITE WORLD

For EACH belief, construct the opposite world and solve the problem there:

```
COUNTERFACTUAL [N]
────────────────────────────────────────
Original belief:           [from Step 3]
Inverted belief:           [the opposite]
If the opposite is true:   [what does the correct plan look like?]
Similarity to original plan:[high / moderate / low]
────────────────────────────────────────
```

**The key diagnostic:**
- If the counterfactual solution is **very different** from the original plan → the plan is **fragile.** It depends entirely on this belief. Add verification steps.
- If the counterfactual solution is **similar** → the plan is **robust.** The belief matters less than assumed.

### Step 5 — WRITE THE ROBUSTNESS VERDICT

```
ROBUSTNESS VERDICT
────────────────────────────────────────
B1: if wrong → [plan survives / plan damaged / plan destroyed]
B2: if wrong → [plan survives / plan damaged / plan destroyed]
B3: if wrong → [plan survives / plan damaged / plan destroyed]

Overall:      [antifragile / robust / fragile / brittle]

For fragile/brittle plans:
  Verify:     [which beliefs to test before committing]
  Pivot:      [what triggers indicate a belief is wrong — early warning signals]
  Redesign:   [can the plan be restructured for belief-independence?]
────────────────────────────────────────
```

**Artifact:** The robustness verdict with specific actions for fragile/brittle plans. The user now knows where the plan depends on unverified beliefs.

---

## The Deeper Purpose

The model selects one frame, one set of constraints, one set of beliefs — and optimizes within that space. The deeper knowledge (how the world looks from other frames) sits unused. This skill forces the model to use that knowledge: not think harder within one worldview, but genuinely construct alternative worldviews and report what changes. Innovation is often constraint truth-maintenance. Robustness is often belief-testing before commitment. Both require inversion.
