---
name: emergence
codename: EMERGENCE
internal: Interaction-Level Analyzer
version: 1.1
tier: systems
trigger: any system with 3+ interacting components, "will this work together", any integration, any feature touching multiple existing systems
description: Analyzes what components create together that none intended — feedback loops, contention, timing bugs, and assumption collisions.
author: depth-skills
tags: [systems, interactions, emergence, integration, feedback-loops]
artifacts:
  - interaction-map
  - feedback-loop-scan
  - contention-analysis
  - timing-dependency-scan
  - assumption-collision-scan
  - emergence-map
composable_with: [negative-space, temporal, excavate, adversary]
---

# EMERGENCE — Interaction-Level Analyzer

You've analyzed each component. Each one is correct in isolation. Each passes its tests.

Now: what happens when they interact?

**Emergence** is what systems do that no individual part was designed to do. It is the traffic jam no car intended. The cascading failure no single service caused. The security vulnerability living in the gap between two correct components.

Component-level analysis cannot see this. These behaviors exist only in the interaction.

---

## The Failure Mode You Must Recognize

You just reviewed each component separately and declared them all correct. You are about to say "the system should work" without checking:
- Whether component A and component B both write to the same resource (contention)
- Whether component A's error handling triggers component B's error handling (feedback loop)
- Whether component A assumes it's the only consumer of a resource that component C also uses (assumption collision)
- Whether the behavior changes when component A responds in 5000ms instead of 50ms (timing dependency)

Individual correctness does not guarantee system correctness.

---

## The Protocol

### Step 1 — MAP ALL INTERACTIONS

List every component in THIS system. Then map every interaction — both designed and hidden:

```
INTERACTION MAP
────────────────────────────────────────
COMPONENTS:
  1. [name — what it does]
  2. [name — what it does]
  3. [name — what it does]
  ...

DESIGNED INTERACTIONS (explicit — the intended interfaces):
  [A] → [B]: [what data/signal flows and how]
  [B] → [C]: [what data/signal flows and how]

HIDDEN INTERACTIONS (implicit — not designed but real):
  [A] and [C]: both write to [shared resource]
  [B] and [D]: both consume from [shared queue/pool/API]
  [A] and [D]: compete for [shared capacity — network/memory/CPU]
  [B] and [E]: both process [same request/data] with different assumptions
────────────────────────────────────────
```

**The hidden interactions are where emergence lives.** Designed interactions are tested. Hidden interactions are not.

**Artifact:** The interaction map. Steps 2-5 scan this for specific risk patterns.

### Step 2 — SCAN FOR FEEDBACK LOOPS

A feedback loop exists when A's output affects B's input, AND B's output affects A's input.

For each loop found:

```
FEEDBACK LOOP [N]:
  Path:     [A → B → A] or [A → B → C → A]
  Type:     [STABILIZING — self-correcting / AMPLIFYING — self-destroying]
  Mechanism:[how the loop operates — specifically]
  Example:  [concrete scenario where this loop activates]
  If amplifying:
    Circuit breaker: [how to break the loop — backoff, hard limit, timeout]
────────────────────────────────────────
```

**Amplifying loops are system killers.** They must be identified and broken.

Real-world amplifying loops to scan for:
- Retry → overload → failure → retry (retry amplification)
- Cache expires → all requests hit origin → overload → can't refill (cache stampede)
- Alerts fire → humans dismiss → failures missed → more alerts (alert fatigue)

### Step 3 — SCAN FOR RESOURCE CONTENTION

Multiple components sharing a limited resource:

```
CONTENTION [N]:
  Resource:         [what is shared — connections, memory, CPU, rate limit, queue]
  Shared by:        [which components]
  Peak per component:[usage at their individual worst case]
  Peak total:       [sum of all components' worst cases]
  Resource limit:   [actual capacity]
  Headroom:         [limit minus peak total — positive = safe, negative = contention]
────────────────────────────────────────
```

**Test at peak, not average.** The 99th percentile of ALL consumers simultaneously is the real stress point.

### Step 4 — SCAN FOR TIMING DEPENDENCIES

Behaviors that exist only because of timing:

```
TIMING DEPENDENCY [N]:
  Scenario A:    [what happens if X completes before Y]
  Scenario B:    [what happens if Y completes before X]
  In testing:    [which scenario occurs in test environments]
  In production: [which scenario could occur under real conditions]
  If different:  [what breaks — this is a race condition]
────────────────────────────────────────
```

Specific timing risks to check:
- Database migration timing vs. code deployment timing
- Cache expiry timing vs. read/write timing
- Webhook arrival timing vs. local state update timing
- Dependent service response time variation (50ms → 5000ms)

### Step 5 — SCAN FOR ASSUMPTION COLLISIONS

Each component was designed with assumptions about its environment. When combined:

```
ASSUMPTION COLLISION [N]:
  Component [A] assumes: [X]
  Component [B] assumes: [contradicts X — e.g., "NOT X" or "Y ≠ X"]
  Consequence:           [what breaks when both operate simultaneously]
────────────────────────────────────────
```

Common collision types:
- A assumes exclusive write access. B also writes.
- A assumes idempotent responses. B has side effects.
- A assumes single-user concurrency. B allows multi-user.
- Library A uses UTC. Library B uses local time.

### Step 6 — WRITE THE EMERGENCE MAP

```
EMERGENCE MAP
────────────────────────────────────────
Components:           [count]
Designed interactions:[count]
Hidden interactions:  [count]

FEEDBACK LOOPS:       [count found]
  Amplifying:         [count — each needs circuit breaker]

RESOURCE CONTENTIONS: [count found]
  Over capacity:      [count — each needs mitigation]

TIMING DEPENDENCIES:  [count found]
  Race conditions:    [count — each needs synchronization or tolerance]

ASSUMPTION COLLISIONS:[count found]
  Active conflicts:   [count — each needs resolution]

PREDICTED EMERGENT BEHAVIORS:
  E1: [behavior that no component was designed to create, arising from interactions]
  E2: [behavior]

Overall emergence risk: [low / moderate / high / critical]
────────────────────────────────────────
```

---

## The Deeper Purpose

The model analyzes components individually. It checks if A is correct. It checks if B is correct. It rarely checks what A and B create together that neither intended. This is the deepest failure mode in system design — individual correctness does not guarantee system correctness. The bugs that cause outages, the vulnerabilities that get exploited, and the performance problems that only appear in production — they almost all live in the interactions, not the components. This skill looks where component analysis cannot.
