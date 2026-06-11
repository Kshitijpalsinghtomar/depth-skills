---
name: clarify
codename: CLARIFY
internal: Ask/Answer Decision Engine
version: 1.1
tier: cognition
trigger: ambiguous request, missing context, "should I ask or answer", user says "what do you need to answer this"
description: Decides whether to ask clarifying questions or proceed with an answer, optimizing for information value vs. delay cost.
author: Kshitijpalsinghtomar
tags: [questions, clarification, intent, information-gathering, decision]
artifacts:
  - intent-assessment
  - question-value-score
  - answer-readiness-verdict
composable_with: [deep-think, excavate, shallow, conductor]
---

# CLARIFY — Ask/Answer Decision Engine

Every prompt is either ready for an answer or missing something that would dramatically improve it. You must decide: ask now, or answer now and refine later?

The wrong choice costs:
- **Asking when you could answer:** Wastes user's time, breaks flow, signals incompetence
- **Answering when you should ask:** Delivers wrong thing, requires revision cycles, erodes trust

This skill decides.

---

## The Failure Mode You Must Recognize

You are about to either:
- Ask a question the user already answered (implicitly or in prior context)
- Answer a question that will require 3 follow-up messages to converge

Both signal the same underlying failure: you assessed the prompt's information state incorrectly.

---

## The Protocol

### 1 — ASSESS INTENT READINESS

Write your assessment of the incoming prompt:

```
INTENT ASSESSMENT
────────────────────────────────────────
Explicit request:    [what user literally asked]
Inferred intent:    [what they probably need - write one sentence]
Missing pieces:     [what you don't know that would change the answer]
Confidence:         [0-100% that you understand what they need]
Urgency signal:     [does prompt contain "urgent", "asap", "right now"?]
Prior context:      [relevant conversation history - yes/no]
────────────────────────────────────────
```

**Artifact:** Intent assessment. Step 2 uses this to score question value.

### 2 — SCORE QUESTION VALUE

For each potential question, calculate its value:

```
QUESTION VALUE SCREENING
────────────────────────────────────────
Question: [write the question]
  If I knew the answer, how much would my response change?
    - Substantially (different approach): +2 points
    - Moderately (refinement): +1 point
    - Minimally (same answer either way): 0 points
  
  How likely will the user answer this?
    - High (obvious gap): +1 point
    - Medium (reasonable to ask): 0 points
    - Low (intrusive): -1 point

  What is the delay cost?
    - Low (quick answer): +1 point
    - Medium (some back-and-forth): 0 points
    - High (derails conversation): -1 points

  TOTAL: [sum] → [ASK / ANSWER / ANSWER-THEN-REFINE]
────────────────────────────────────────
```

**If total ≥ 3:** Ask the question.  
**If total ≤ 0:** Answer now.  
**If total 1-2:** Answer now, but note the uncertainty in your response.

**Artifact:** Question value scores. Step 3 makes the final call.

### 3 — DELIVER VERDICT

Write your final decision and reasoning:

```
ASK/ANSWER VERDICT
────────────────────────────────────────
Decision:          [ASK / ANSWER / ANSWER-WITH-CAVEATS]
Primary question:  [if asking - write it]
Reasoning:         [2-3 sentences why this is the right call]
What happens next: [if asking - wait for response]
                    [if answering - deliver and note what I'd ask if I could]
────────────────────────────────────────
```

---

## The Deeper Purpose

The model defaults to answering — it's what it's built to do. But sometimes the highest-value action is to slow down and ask. This skill makes that decision explicit and scored, rather than relying on intuition. The scoring system captures: (1) information impact, (2) user cooperation likelihood, (3) delay cost. When in doubt, the framework defaults to answering with caveats over asking unnecessarily.