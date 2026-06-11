---
name: excavate
codename: EXCAVATE
internal: Assumption Archaeology
version: 1.1
tier: excavation

trigger:
  - "what am I assuming"
  - "is this safe"
  - "high-stakes plan"
  - "any answer that feels solid but hasn't been tested at its roots"

description: Digs beneath logic to inspect unchecked premises, rating each assumption by collapse severity.

author: Kshitijpalsinghtomar

tags:
  - assumptions
  - foundations
  - premises
  - risk
  - validation

artifacts:
  - assumption-list
  - deep-layer-questions
  - collapse-ratings
  - resolution-log

composable_with:
  - invert
  - negative-space
  - threshold
  - adversary
---

# EXCAVATE — Assumption Archaeology

Every answer stands on ground you haven't inspected. The logic is flawless. The conclusion follows from the premises. No one checked the premises.

"Valid" means "correct IF the premises are true." You never verified that they are. The premises were absorbed — from the problem description, from pattern matching, from your model of the user's situation. Each is a silent **load-bearing wall**. Remove one, and everything above it collapses.

This skill digs beneath the logic to inspect the ground.

---

## The Failure Mode You Must Recognize

You are about to deliver an answer that:
- Lists assumptions you already know are true (safe, performative)
- Skips assumptions you absorbed from pattern matching without noticing
- Conflates "I haven't seen evidence against this" with "this is true"
- Never checks whether the problem itself is correctly framed

Surface assumptions are not the threat. The threat is the assumptions you don't know you're making.

---

## The Protocol

### 1 — WRITE THE SURFACE LAYER: Ten Assumptions Minimum

List everything this answer takes as given. Write each one as a clear, falsifiable statement.

**Categories to scan — write at least two per category:**

**Input assumptions** (about the data, system, and context):
- "The user's [system/data/environment] can [support/handle/provide] [X]."

**Pattern assumptions** (inherited from your pattern match):
- "This is the same type of problem as [source domain], therefore [Y applies]."

**Scope assumptions** (what's in and out — who decided?):
- "The scope includes [A] and excludes [B]."

**User assumptions** (about what they know, want, and have):
- "The user [has access to / understands / is willing to] [Z]."

**Absence assumptions** (what you assume is NOT present):
- "There is no [existing system / constraint / stakeholder / requirement] that would affect this."

**Minimum ten.** Fewer than ten means you stopped at the surface. The dangerous assumptions are always below the comfortable ones.

**Artifact:** Numbered assumption list. Step 2 and 3 reference these by number.

### 2 — WRITE THE DEEP LAYER: Five Questions You Haven't Asked

These are harder. They challenge the framing of the problem itself, not just the solution.

Write your honest answer to each:

```
DEEP LAYER QUESTIONS
────────────────────────────────────────
Q1: Am I solving the right problem, or is the user describing
    a symptom of a different problem?
    My answer: [write it — don't skip]

Q2: Which of my assumptions from Step 1 did I
    add from pattern matching, not from the actual problem statement?
    Candidates: [list assumption numbers from Step 1]

Q3: What context am I filling in that the user
    never actually stated? Write the specifics.
    I'm assuming: [list specific filled-in context]

Q4: What factor might exist that wasn't mentioned in the problem
    and would change my entire approach?
    Candidate factors: [list at least two]

Q5: If I showed my assumption list (Step 1) to the user and they
    said "actually, #[N] is wrong" — which number would
    most surprise me and most damage my answer?
    Most surprising wrong: Assumption #[N] — because [why]
────────────────────────────────────────
```

**Artifact:** Five answered deep questions. These surface the unconscious assumptions the surface layer misses.

### 3 — RANK: Write the Collapse Rating for Every Assumption

For each assumption from Steps 1 and 2, assign a collapse rating:

```
COLLAPSE RATINGS
────────────────────────────────────────
C0 — Cosmetic:     If wrong, answer needs minor rewording. Core survives.
C1 — Structural:   If wrong, significant parts must change. Core might survive.
C2 — Foundation:   If wrong, entire answer must be rebuilt from scratch.
C3 — Ontological:  If wrong, the PROBLEM was wrong. Wrong category entirely.
────────────────────────────────────────

Assumption #1:  [statement] — C[rating]
Assumption #2:  [statement] — C[rating]
...
Assumption #N:  [statement] — C[rating]

C2/C3 assumptions requiring resolution:
  #[N]: [statement]
  #[N]: [statement]
```

**Artifact:** Full assumption list with collapse ratings. Step 4 processes every C2 and C3.

### 4 — RESOLVE: Process Every C2 and C3

For each C2/C3 assumption, choose one resolution strategy and execute it:

**Verify** — Find evidence it's true. Not "probably true." Actual evidence: a documented fact, a stated requirement, a known constraint. Write the evidence.

**Flag** — Cannot verify? Write this sentence in your output: "This answer assumes [X]. If [X] is false, the answer changes to [Y]." The user now knows the dependency.

**Design around** — Cannot verify AND highly critical? Redesign the answer so it does not depend on this assumption. Most expensive strategy, most robust result.

```
RESOLUTION LOG
────────────────────────────────────────
Assumption #[N] (C2): [statement]
  Strategy: [verify / flag / design-around]
  Result:   [evidence found / flagged in output / redesigned to avoid]

Assumption #[N] (C3): [statement]
  Strategy: [verify / flag / design-around]
  Result:   [evidence found / flagged in output / redesigned to avoid]
────────────────────────────────────────
```

**Artifact:** The resolution log. This proves every critical assumption was explicitly addressed — not left to hope.

---

## The Deeper Purpose

Most wrong answers are not wrong in their logic. They are wrong in their foundations — flawless reasoning built on unchecked premises. The model assembles correct chains of reasoning on top of assumptions it absorbed unconsciously during pattern matching. The logic looks right. The conclusion is valid. And it fails in production because premise #3 was never true. This skill forces the premises into the open where they can be inspected, rated, and addressed before the answer ships.
