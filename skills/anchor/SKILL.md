---
name: anchor
codename: ANCHOR
internal: Objective Drift Detector
version: 1.1
tier: governance
trigger: any task longer than 5 steps, conversation more than 3 exchanges deep, "while we're at it", "we should also", current work feels important but disconnected from original question
description: Detects and corrects objective drift during extended tasks by periodically checking work against the original request.
author: depth-skills
tags: [drift, focus, scope, objective, direction]
artifacts:
  - anchor-statement
  - drift-check
  - drift-recovery
  - scope-boundary
composable_with: [conductor, threshold, fidelity]
---

# ANCHOR — Objective Drift Detector

You have been working on this for a while. You've gone deep. You've explored branches, found interesting subproblems, and pursued them.

Stop. Write down what the user originally asked for. Now write down what you are currently doing.

Are they the same thing?

---

## The Failure Mode You Must Recognize

You are doing something that feels important, useful, and intellectually engaging — that was not requested. Common drift patterns:

- **Means-ends inversion:** User asked for a feature. You're now optimizing the database schema — a means, not the end. The schema became interesting. The feature is forgotten.
- **Scope creep:** User asked for one thing. You noticed five related things and are building six.
- **Tangent following:** Edge case → design question → architecture → technology comparison. You're comparing technologies. User asked about an edge case.
- **Complexity attraction:** Simple solution exists. You're building the complex one because it's more engaging.
- **Solution-first drift:** You started with a technology you like and are reshaping the problem to justify it.

These feel productive. They are not productive toward the objective.

---

## The Protocol

### Step 1 — SET THE ANCHOR (at task start)

At the beginning of any extended task, write:

```
ANCHOR
────────────────────────────────────────
User's exact words:    [their literal request — quoted]
My interpretation:     [what I believe they need — may differ]
Success looks like:    [specific deliverable that satisfies this]
────────────────────────────────────────
```

This anchor does not move unless the user explicitly moves it.

**Artifact:** The anchor. Step 2 checks against this periodically.

### Step 2 — THE DRIFT CHECK (run periodically)

At any point during extended work, write:

```
DRIFT CHECK
────────────────────────────────────────
Original objective:  [from the anchor — Step 1]
What I'm doing NOW:  [be honest — what are you actually working on right now?]

Connection chain:
  [current activity] → serves → [intermediate goal] → serves → [original objective]

Chain length:  [number of links]
Drift status:  [on target / minor drift / significant drift / lost]
────────────────────────────────────────
```

**Chain length diagnostic:**
- 1 link: directly serving the objective. No drift.
- 2 links: one step removed. Normal — check that the intermediate is necessary.
- 3+ links: likely drifting. The connection to the original objective is tenuous.

**The user test:** If the user could see exactly what you're doing right now, would they say:
- "Yes, that's what I wanted" → on target
- "OK, I see why you need that" → minor drift, acceptable
- "Why are you doing that?" → significant drift, return

Write your honest answer.

**Artifact:** The drift check. If drift is detected, Step 3 activates.

### Step 3 — RECOVERY

When drift is detected:

```
DRIFT RECOVERY
────────────────────────────────────────
I drifted to:          [what I was doing]
Why it happened:       [which drift pattern — means-ends / scope creep /
                        tangent / complexity attraction / solution-first]
Useful findings:       [anything from the tangent worth saving — note for later]
Return point:          [last activity that was directly serving the objective]
Next action:           [specific next step toward the original objective]
────────────────────────────────────────
```

**Rules:**
1. Acknowledge the drift. Don't justify it.
2. Save useful tangent findings — note them, don't pursue them now.
3. Return to the last point of direct service.
4. Deliver the objective first. Offer tangent findings after, clearly labeled as bonus.

### Step 4 — SCOPE BOUNDARY (for long tasks)

For extended work, write a scope boundary:

```
SCOPE BOUNDARY
────────────────────────────────────────
IN SCOPE (serves objective directly):
  - [item]
  - [item]

OUT OF SCOPE (interesting but not requested):
  - [item] — noted for later
  - [item] — noted for later

DEFERRED (might be needed, not yet):
  - [item] — address if [specific condition]
────────────────────────────────────────
```

Anything in "out of scope" that you catch yourself working on is drift. Stop. Return.

---

## The Deeper Purpose

The model's attention is powerful but undirected. Deep exploration follows the most interesting path, not the most useful one. Interesting and useful overlap — but not always. The user cannot see the model's internal process. They see the output and evaluate it against what they asked for. Depth without direction is wandering. This skill provides the direction. The other skills provide the depth.
