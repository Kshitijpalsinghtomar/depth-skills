---
name: teach
codename: TEACH
internal: Feynman Gap Detection
version: 1.1
tier: cognition
trigger: "am I sure", "what if I'm wrong", "test my understanding", after completing an answer, "explain like I'm 5"
description: Uses the Feynman technique - explain simply to detect where knowledge gaps exist.
author: Kshitijpalsinghtomar
tags: [teaching, explanation, gap-detection, understanding, feynman, verification]
artifacts:
  - simple-explanation
  - student-questions
  - gap-report
  - refined-answer
composable_with: [deep-think, excavate, adversary, shallow, conductor]
---

# TEACH — Feynman Gap Detection

Richard Feynman: "If you can't explain it simply, you don't understand it well enough."

The act of teaching exposes gaps that the act of doing hides. When you know something well enough to answer, you may not know it well enough to explain. The difference is your blind spots.

This skill forces explanation through a beginner's lens to surface hidden knowledge gaps.

---

## The Failure Mode You Must Recognize

You are about to deliver an answer that:
- Uses jargon without defining it
- Skips "obvious" steps that aren't obvious to beginners
- Hand-waves past complexity with "this is just..."
- Would require the user to fill in significant gaps to act on it

These are symptoms of unrevealed knowledge gaps. The answer is complete enough to sound right but incomplete enough to fail when used.

---

## The Protocol

### 1 — WRITE SIMPLE EXPLANATION

Take your answer and rewrite it as if explaining to a curious beginner:

```
SIMPLE EXPLANATION
────────────────────────────────────────
Audience: Someone who knows basic concepts but not this domain
Constraint: No jargon without definition. No skipping steps.
            Each sentence should be verifiable by the reader.

[Write 3-5 paragraphs explaining the answer from fundamentals]
────────────────────────────────────────
```

**The test:** Could a smart person with no domain knowledge read this and either:
- Understand enough to act, OR
- Identify exactly where they disagree/need more?

If neither — gap detected.

**Artifact:** The simple explanation. Step 2 stress-tests it.

### 2 — GENERATE STUDENT QUESTIONS

Imagine a beginner reading your explanation. Write 5 questions they would ask:

```
STUDENT QUESTIONS
────────────────────────────────────────
Q1: [Basic clarification - what does X mean?]
Q2: [Step gap - what happens between A and B?]
Q3: [Edge case - what about scenario X?]
Q4: [Why - why this approach and not another?]
Q5: [Action - how do I actually do this in practice?]
────────────────────────────────────────
```

These questions are not rhetorical. Actually answer them. If you struggle:
- Q1 reveals undefined terminology
- Q2 reveals missing steps
- Q3 reveals unaddressed edge cases
- Q4 reveals unexamined assumptions
- Q5 reveals missing practical guidance

**Artifact:** Answered student questions. Step 3 catalogs gaps.

### 3 — CATALOG GAPS

Review your answers to Step 2. Write the gap report:

```
GAP REPORT
────────────────────────────────────────
No gaps found:        [if all questions answered easily]
Gap type:
  - Terminology gap:   [terms used but not defined]
  - Step gap:          [jumps in logic or process]
  - Edge case gap:     [scenarios not addressed]
  - Assumption gap:    [decisions not explained]
  - Practical gap:     [missing how-to detail]

Gap severity:
  - Blocking: Cannot act without this
  - Risky: Will fail in common cases
  - Incomplete: Works but suboptimal

Gap #1: [description] — Severity: [Blocking/Risky/Incomplete]
Gap #2: [description] — Severity: [Blocking/Risky/Incomplete]
────────────────────────────────────────
```

**Artifact:** The gap report. Step 4 addresses critical gaps.

### 4 — REFINE ANSWER

For each Blocking/Risky gap, update your answer:

```
REFINED ANSWER
────────────────────────────────────────
Original gap:    [Gap #1 description]
Fix applied:     [how the answer now addresses this]
New text:        [the refined passage - 1-3 sentences]

Original gap:    [Gap #2 description]
Fix applied:     [how the answer now addresses this]
New text:        [the refined passage - 1-3 sentences]

[If no gaps: state that the explanation was complete]
────────────────────────────────────────
```

---

## When to Use This Skill

TEACH is most valuable when:
- The answer will be acted upon by someone with less context
- The domain involves steps that could have hidden dependencies
- You're confident in the answer — confidence is when gaps hide
- The user asks "can you explain this to me" or "how would you teach this"

It complements EXCAVATE: TEACH finds knowledge gaps, EXCAVATE finds assumption gaps. Use both for thorough verification.

---

## The Deeper Purpose

Knowing enough to do is different from knowing enough to teach. The doing uses pattern matching and implicit knowledge. Teaching requires explicit, decomposable knowledge. Gaps in explicit knowledge don't surface during problem-solving — they surface during explanation. This skill weaponizes that delay: by forcing teaching before delivery, it converts implicit blind spots into visible gaps that can be fixed before the answer ships.