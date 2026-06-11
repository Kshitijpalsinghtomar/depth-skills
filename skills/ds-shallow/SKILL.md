---
name: shallow
codename: SHALLOW
internal: Proportional Depth Protocol
version: 1.1
tier: cognition
trigger: low-stakes task, reversible decision, "keep it simple", "don't overthink", quick answer needed
description: Prevents overthinking by matching cognitive investment to consequence - the intentional opposite of DEEP-THINK.
author: Kshitijpalsinghtomar
tags: [proportionality, efficiency, overthinking, quick-answer, depth-calibration]
artifacts:
  - depth-assessment
  - budget-allocation
  - shallow-delivery-verdict
composable_with: [deep-think, threshold, conductor]
---

# SHALLOW — Proportional Depth Protocol

DEEP-THINK is essential. But not every task deserves it. Sometimes the deepest answer is a short one.

The failure mode of depth-skills is **depth bias**: the model reaches for sophisticated analysis on problems that don't warrant it. A CSS color choice gets 6-step reasoning. A routine email gets threat-modeled. This skill is the brake.

---

## The Failure Mode You Must Recognize

You are about to:
- Generate six artifacts for a question that could be answered in one sentence
- Add caveats to a decision that is easily reversed
- Apply THRESHOLD analysis to a temporary workaround
- Treat a first-pass response as if it were a permanent architecture decision

If the cost of being wrong is low and the fix is easy — this is a SHALLOW task.

---

## The Protocol

### 1 — ASSESS DEPTH APPROPRIATENESS

Evaluate the task against depth criteria:

```
DEPTH ASSESSMENT
────────────────────────────────────────
Reversibility:    [Trivial / Moderate / Hard / Permanent]
  → If Trivial/Moderate: favor SHALLOW

Consequence:      [Trivial / Moderate / Significant / Critical]
  → If Trivial/Moderate: favor SHALLOW

Complexity:       [Simple / Moderate / Complex / Intricate]
  → If Simple: favor SHALLOW

Pattern match:    [Routine / Variation / Novel / Unprecedented]
  → If Routine: favor SHALLOW

Stakeholders:     [One / Few / Many / All-hands]
  → If One/Few: favor SHALLOW

Urgency:          [Can wait / Within hour / Within minute / Now]
  → If "can wait" is false: favor SHALLOW (speed matters)
────────────────────────────────────────
```

**Score:** Count SHALLOW-favoring answers.
- **0-1:** Deep task — use DEEP-THINK
- **2-3:** Mixed — use abbreviated deep analysis
- **4-6:** Shallow task — use this protocol

**Artifact:** Depth assessment with score. Step 2 allocates budget.

### 2 — ALLOCATE COGNITIVE BUDGET

Based on the assessment, allocate:

```
BUDGET ALLOCATION
────────────────────────────────────────
Assessment score: [N]/6
Depth budget:     [MINIMAL / LIGHT / MODERATE]

MINIMAL (score 5-6):
  - No artifacts required
  - One sentence answer
  - Skip caveats
  - Skip alternatives
  - Skip "it depends"

LIGHT (score 3-4):
  - One artifact: answer with ONE assumption stated
  - One alternative mentioned in 1 sentence
  - One caveat if genuinely important

MODERATE (score 2-3):
  - Two artifacts: restatement + chosen approach
  - Skip challenge phase
  - Minimal boundary check
────────────────────────────────────────
```

**Artifact:** Budget allocation. Step 3 delivers within budget.

### 3 — DELIVER WITHIN BUDGET

Execute the answer within allocated depth:

```
SHALLOW DELIVERY
────────────────────────────────────────
Budget level:   [MINIMAL / LIGHT / MODERATE]
Answer:         [deliver within budget constraints]

If MINIMAL:
  Answer only. No preamble. No caveats.
  
If LIGHT:
  State ONE assumption. Mention ONE alternative.
  One sentence each, inline.

If MODERATE:
  Restate in one sentence.
  Give the answer.
  One-line boundary: "works for [common case], not [edge case]."
────────────────────────────────────────
```

---

## When NOT to Use This Skill

SHALLOW should NOT activate when:
- The user explicitly asks for deep analysis
- The task involves security, safety, or financial consequences
- The decision is hard to reverse (architecture, contract, data model)
- The user has expressed confusion or uncertainty
- This is iteration N>2 on the same problem (depth may finally be warranted)

**The default should still be appropriate depth.** SHALLOW is a targeted counter to depth bias — not a replacement for sound judgment.

---

## The Deeper Purpose

The depth-skills library is optimized for depth. But cognitive investment should match consequence. SHALLOW provides the calibration: a simple scoring system that routes low-stakes tasks to fast answers. It's not anti-thinking — it's proportional-thinking. The skill exists because the library's other skills make over-analysis easy. SHALLOW makes under-analysis acceptable.