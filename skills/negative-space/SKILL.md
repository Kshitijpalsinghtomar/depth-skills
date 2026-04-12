---
codename: NEGATIVE-SPACE
internal: Absence Detector
version: 1.1
tier: excavation
trigger: "what am I missing", "is this complete", "anything else", any answer that feels thorough but might have invisible holes
---

# NEGATIVE-SPACE — Absence Detector

Your answer is thorough. Every point you made is correct. Every section is well-reasoned.

But you only wrote about what you activated. The concepts far from your initial activation path were never reached — not because they're irrelevant, but because the path didn't lead there. Every answer has a **shadow**: the dimension space that was never illuminated. An answer that covers 8 dimensions thoroughly looks complete — but if 3 uncovered dimensions matter, it's dangerously incomplete.

This skill illuminates the shadows.

---

## The Failure Mode You Must Recognize

You feel finished. The answer covers everything you thought of. The coverage feels complete because everything that IS there is well-done.

But "everything I thought of" is not the same as "everything that matters." Your activation path was determined by the initial keywords. Concepts adjacent to those keywords were activated. Distant concepts were not. The feeling of completeness is an artifact of your search pattern, not evidence of actual completeness.

---

## The Protocol

### Step 1 — MAP THE LIGHT CONE

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

### Step 2 — SCAN THE STANDARD DIMENSIONS

Check each dimension against your answer. Write the status:

```
DIMENSION SCAN
────────────────────────────────────────
Security:       [addressed / absent / N/A for this problem]
  If absent:    [what security implication exists?]

Privacy:        [addressed / absent / N/A]
  If absent:    [what data handling was not discussed?]

Error handling: [addressed / absent / N/A]
  If absent:    [what goes wrong when this fails?]

Edge cases:     [addressed / absent / N/A]
  If absent:    [what boundary input was not considered?]

Scale:          [addressed / absent / N/A]
  If absent:    [what happens at 10× or 100×?]

Accessibility:  [addressed / absent / N/A]
  If absent:    [who is excluded?]

Observability:  [addressed / absent / N/A]
  If absent:    [can you tell if this is working in production?]

Reversibility:  [addressed / absent / N/A]
  If absent:    [can this be undone if wrong?]

Cost:           [addressed / absent / N/A]
  If absent:    [what does this cost in money, time, or complexity?]

Dependencies:   [addressed / absent / N/A]
  If absent:    [what could change or fail beneath this?]

Migration:      [addressed / absent / N/A]
  If absent:    [how do you get from current to proposed state?]

Testing:        [addressed / absent / N/A]
  If absent:    [how is correctness verified?]
────────────────────────────────────────
```

**For each "absent" entry:** Write whether it's absent because it's genuinely irrelevant (N/A would be more honest) or absent because it was never considered. The second type is a gap.

**Artifact:** The dimension scan. Honest "absent" entries are the raw material for Step 5.

### Step 3 — SCAN FOR ABSENT STAKEHOLDERS

Write who was considered and who was not:

```
STAKEHOLDER SCAN
────────────────────────────────────────
Considered:
  [who] — their perspective is reflected in [which part of the answer]

NOT considered:
  The end user:     [what would their experience of this be?]
  The operator:     [who runs this in production? What's their experience?]
  The next developer:[who modifies this in 6 months? Can they understand it?]
  The adversary:    [who would exploit this? What's their attack surface?]
  The edge-case user:[low bandwidth, old device, disability, unusual usage]
────────────────────────────────────────
```

For each "NOT considered" stakeholder: write one sentence about what their perspective adds or changes. If it changes nothing — mark N/A. If it changes the answer — it's a gap.

**Artifact:** The stakeholder scan with impact assessment.

### Step 4 — SCAN FOR ABSENT FAILURE CATEGORIES

Standard failure analysis asks "what could go wrong?" This step asks: "what CATEGORY of failure was never considered?"

For each category, write whether THIS answer accounts for it:

```
FAILURE CATEGORY SCAN
────────────────────────────────────────
Partial failure:   [addressed / absent]
  (System works but badly — degraded, not dead)

Slow failure:      [addressed / absent]
  (Gradual decay over weeks/months, not sudden crash)

Success failure:   [addressed / absent]
  (System does exactly what you asked, and that turns out to be wrong)

Composition failure:[addressed / absent]
  (Each part works, the combination doesn't — see EMERGENCE)

Human failure:     [addressed / absent]
  (System is correct but people misuse, misunderstand, or bypass it)

Incentive failure: [addressed / absent]
  (System creates incentives that lead to bad behavior over time)
────────────────────────────────────────
```

**Artifact:** The failure category scan. If any absence matters, it's added to the gap list.

### Step 5 — WRITE THE SILENCE REPORT

Compile all gaps from Steps 2-4:

```
SILENCE REPORT
────────────────────────────────────────
CRITICAL SILENCES (absent + would change the answer):
  S1: [dimension/stakeholder/failure category]
      Impact:  [what changes when this is addressed]
      Action:  [add a section / flag as limitation / investigate before shipping]

  S2: [dimension/stakeholder/failure category]
      Impact:  [what changes]
      Action:  [action]

ACKNOWLEDGED GAPS (absent + known, acceptable for now):
  G1: [what's missing and why it's acceptable]

CONFIRMED N/A (absent + genuinely irrelevant):
  N1: [what's not relevant and why]
────────────────────────────────────────
```

**Critical silences must be addressed before the answer ships.** Acknowledged gaps are the user's decision. Confirmed N/A proves you checked rather than skipped.

---

## The Deeper Purpose

Every other skill in this library operates on what's present in the output — checking it, stressing it, calibrating it. This skill operates on what's absent. The hardest failure to detect is not the wrong answer but the incomplete one that looks complete. A room with everything except oxygen looks normal until you try to breathe. An answer covering eight dimensions thoroughly looks complete until the ninth dimension fails in production. This skill makes absence visible before the consequences do.
