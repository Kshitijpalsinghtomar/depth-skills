---
name: fidelity
codename: FIDELITY
internal: Compression Integrity Verifier
version: 1.1
tier: integrity
trigger: "summarize", "give me the short version", "TLDR", "bottom line", any time complex analysis is condensed into a final answer
description: Prevents lossy compression from erasing conditions, exceptions, and uncertainties during summarization.
author: depth-skills
tags: [compression, summary, fidelity, truth-preservation, delivery]
artifacts:
  - critical-information-tags
  - compressed-version
  - fidelity-diff
  - fidelity-verdict
composable_with: [provenance, contradict, anchor]
---

# FIDELITY — Compression Integrity Verifier

You just did deep thinking. You explored approaches, found edge cases, identified caveats, surfaced conditions. Now you're compressing it into a clean final answer.

This is the moment truth disappears.

---

## The Failure Mode You Must Recognize

Two pressures compete: **be thorough** and **be concise**. The result is lossy compression:
- "This works IF X" becomes "This works" (condition dropped)
- "True EXCEPT when Y" becomes "True" (exception erased)
- "70% confident because Z" becomes a declarative statement (uncertainty hidden)
- "Option B was close, better if Q changes" becomes invisible (alternative forgotten)

The summary is cleaner, shorter, more confident — and **less true** than the analysis that produced it. The user makes decisions based on a simplified reality that you know is incomplete.

---

## The Protocol

### Step 1 — TAG: Mark Critical Information Before Compressing

Before writing the compressed version, read the full analysis and tag every item that, if dropped, makes the summary misleading. Write each tag:

```
CRITICAL INFORMATION TAGS
────────────────────────────────────────
TAG 1 — CONDITION:
  Full: "[recommendation] IF [condition]"
  If dropped: user tries it where [condition] is false → [consequence]

TAG 2 — EXCEPTION:
  Full: "True EXCEPT when [scenario]"
  If dropped: user applies universally → hits [scenario] unprepared

TAG 3 — UNCERTAINTY:
  Full: "[confidence level] because [evidence state]"
  If dropped: user treats as certain → no contingency when wrong

TAG 4 — ALTERNATIVE:
  Full: "Option B was close — better if [condition changes]"
  If dropped: user can't adapt when conditions change

TAG 5 — DEPENDENCY:
  Full: "Depends on [X] being true/available/stable"
  If dropped: user doesn't verify [X] → failure when [X] is absent
────────────────────────────────────────
```

Not every answer has all five types. Tag what exists. The types to scan for:
- **Conditions** — "works IF"
- **Exceptions** — "true EXCEPT"
- **Uncertainties** — confidence levels, evidence gaps
- **Alternatives** — near-winners that matter if context changes
- **Dependencies** — things this answer relies on

**Artifact:** The tagged list. Step 3 verifies each tag survives compression.

### Step 2 — COMPRESS: Write the Short Version

Write the clear, concise answer you want to deliver. Do not consult the tags. Write naturally — as concise as the content allows.

**Artifact:** The compressed version. Step 3 diffs this against Step 1.

### Step 3 — DIFF: Check Each Tag Against the Compressed Version

For each tag from Step 1:

```
FIDELITY DIFF
────────────────────────────────────────
TAG 1 — CONDITION:
  In compressed version?: [yes — preserved / no — dropped]
  If dropped: could the user make a wrong decision? [yes / no]
  If yes:     RESTORE

TAG 2 — EXCEPTION:
  In compressed version?: [yes / no]
  If dropped: could the user be surprised by a failure? [yes / no]
  If yes:     RESTORE

...
────────────────────────────────────────
```

**Restore rule:** Any tag that is dropped AND could lead to a wrong decision or surprise failure MUST be restored.

**Artifact:** The fidelity diff showing what was preserved and what was restored.

### Step 4 — RESTORE WITHOUT BLOATING

Restoration does not mean making the summary as long as the full analysis. Use minimum-length preservation techniques:

- **Inline qualifier:** "Works well (assuming stable network)" — 4 words preserves a critical condition
- **Caveat footer:** Brief "Watch for:" section at the end
- **Conditional phrasing:** "For standard cases, X. For [edge], use Y instead."
- **Confidence signal:** "High confidence for typical setups. Untested for [scenario]."

The goal: the compressed version is as TRUE as the full analysis, not as LONG.

### Step 5 — WRITE THE FIDELITY VERDICT

```
FIDELITY VERDICT
────────────────────────────────────────
Critical items tagged:     [count]
Preserved in first draft:  [count]
Restored after diff:       [count]
Intentionally omitted:     [count] — [justification per item]

Status: [LOSSLESS / ACCEPTABLE / UNACCEPTABLE]

Lossless:     All critical items preserved. Summary is as true as the analysis.
Acceptable:   Minor items omitted with justification. No decision risk.
Unacceptable: Critical items missing. Revise before delivery.
────────────────────────────────────────
```

---

## The Deeper Purpose

The model's best thinking happens during exploration. Its worst habit is discarding that thinking during delivery. If the final answer is a lossy compression of the truth, the user acts on an incomplete version of what the model itself knows is more complex. This skill ensures the distance between what-the-model-knows and what-the-user-receives is minimized — not by being verbose, but by preserving the specific pieces of truth that change decisions.
