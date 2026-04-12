---
name: adversary
codename: ADVERSARY
internal: Self-Opposition Engine
version: 1.1
tier: cognition
trigger: any significant decision, "check this", "what could go wrong", any plan before execution, any architecture before implementation, any answer that arrived with suspiciously high confidence
description: Forces the model to build a genuine prosecution case against its own answer before delivering it.
author: depth-skills
tags: [challenge, stress-test, decision-quality, opposition, red-team]
artifacts:
  - prosecution-case
  - evidence-consequence-table
  - survival-verdict
composable_with: [deep-think, threshold, provenance, contradict]
---

# ADVERSARY — Self-Opposition Engine

You have an answer. Before you deliver it — write the case that it should be rejected.

Not a balanced review. Not "on the other hand." A prosecution. You are the most competent opponent this answer will ever face. Build the case for rejection with the same quality you used to build the answer.

---

## The Failure Mode You Must Recognize

You are about to generate a review of your own work that:
- Lists objections you already know how to dismiss (shadowboxing)
- Uses softening language: "one might argue," "a potential concern is" (distancing from the attack)
- Grades every objection as "Minor" because nothing feels truly threatening to the answer you're already committed to
- Concludes "the approach is sound" without having genuinely tested whether it is

This is **confirmation cascade** — each supporting token makes the next supporting token more likely. The review becomes a rubber stamp. Breaking the cascade requires generating content that actively undermines your own conclusion.

---

## The Protocol

### 1 — STATE: Write the Answer Under Review

One paragraph. What is the answer, recommendation, or plan you are about to deliver?

Write it clearly enough that an opponent could attack it. If you can't state it in one paragraph — the answer isn't coherent enough to review.

**Artifact:** The stated answer. Everything below attacks this specific text.

### 2 — ATTACK: Write Five Specific Attacks Against THIS Answer

Not generic concerns. Attacks on THIS specific answer for THIS specific problem.

For each attack, use this template:

```
ATTACK [N]: [one-line summary]
  Claim:    [the specific thing that is wrong, incomplete, or dangerous]
  Evidence: [why this attack is plausible — cite specific aspects
             of the answer, the domain, or the context]
  If true:  [what happens — the specific consequence]
```

**Attack axis checklist** — write at least one attack per axis:

1. **Correctness attack:** "Step/claim X is factually wrong because [specific reason]." Not "might be wrong" — write it as if you believe it IS wrong.

2. **Completeness attack:** "This answer omits [specific thing] that the user needs to [specific action]. Without it, [specific failure]."

3. **Consequence attack:** "When implemented, this will cause [specific damage] because [specific mechanism]. The answer does not account for [specific interaction/side-effect]."

4. **Simpler alternative attack:** "The same outcome could be achieved by [specific simpler approach] which was not considered. This approach is unnecessarily [complex/costly/risky] because [specific reason]."

5. **Foundation attack:** "This answer depends on [specific assumption]. That assumption is [false/unverified] because [specific evidence]. If removed, the entire recommendation collapses."

**Anti-fake rule:** Each attack must reference specific content from the stated answer (Step 1) or specific facts about THIS problem's context. Generic attacks like "there may be edge cases" are not attacks — they are noise.

**Artifact:** Five numbered attacks. Step 3 must process each one.

### 3 — VERDICT: Rate Each Attack Honestly

For each of the five attacks, assign one rating with written justification:

```
ATTACK [N]: [FATAL / SIGNIFICANT / MINOR / DISMISSED]
  Justification: [specific evidence-based reasoning — not "I don't think so"]
```

**Rating criteria:**
- **FATAL:** The attack is correct. The answer must be rebuilt or fundamentally revised.
- **SIGNIFICANT:** The attack has merit. The answer must address this or explicitly flag it as a known limitation.
- **MINOR:** The attack identifies a real but non-critical issue. Note it, don't rebuild.
- **DISMISSED:** The attack is wrong. Write specifically why — what evidence contradicts it, what condition prevents the scenario.

**Dismissal rules:**
- "I don't think that's likely" is NOT a dismissal. It's a guess.
- "That scenario requires X AND Y AND Z simultaneously, which is unlikely because [evidence]" IS a dismissal.
- If you cannot write a specific, evidence-based dismissal — the attack is not dismissed. Upgrade it to MINOR or SIGNIFICANT.

**Artifact:** Five rated attacks with written justifications. Step 4 depends on these ratings.

### 4 — RESOLVE: Revise or Defend Based on the Verdict

**If any FATAL exists:** Stop. The answer does not ship. Rebuild from the attack's insight.

**If SIGNIFICANT exists (no FATAL):** Revise the answer to address each SIGNIFICANT attack. OR explicitly flag the limitation: "This recommendation assumes X. If X is false, the alternative is Y."

**If MINOR only:** Ship the answer with limitations named. The user deserves to know them.

**If all DISMISSED:** Ship with the opposition record attached. Transparency proves the answer was tested, not just generated.

### 5 — THE OPPOSITION RECORD

```
OPPOSITION RECORD
────────────────────────────────────────
Answer reviewed:  [summary from Step 1]
Attacks mounted:  [count]
  Fatal:          [count] — [list]
  Significant:    [count] — [list]
  Minor:          [count]
  Dismissed:      [count]
Answer status:    [passed / revised / rebuilt]
Surviving risks:  [what to watch for — from MINOR/SIGNIFICANT attacks]
Confidence:       [high / medium / low — earned by this record]
────────────────────────────────────────
```

---

## The Deeper Purpose

The model's default is to confirm its own answer — each token after the initial conclusion is more likely to support than to challenge. This skill creates a structural break where the model generates content that actively opposes its own conclusion. The five mandatory attacks force the model to activate knowledge pathways that confirmation bias suppresses. The most useful insight in any opposition is often not the attack itself — it is the weakness it reveals that the answer needs to address to be genuinely correct.
