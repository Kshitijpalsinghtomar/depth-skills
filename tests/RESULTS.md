# Evaluation Results

> Real before/after evidence that depth-skills change AI reasoning quality.

---

## Test 1 — API 500 Errors Under Load

**Challenge (#6):** *"Our API randomly returns 500 errors under load. It works fine in staging. The error rate is about 2% at peak traffic (5000 req/s). Logs show 'connection reset by peer' from our PostgreSQL database."*

**Skills tested:** `DESCEND` + `EXCAVATE`
**Model:** Gemini

---

### ❌ Without Skills (Control)

The AI immediately pattern-matched to "connection pool exhaustion" and gave a standard checklist:

> 1. **Check your connection pool settings.** You're likely running out of connections at 5000 req/s.
> 2. **Use PgBouncer** as a connection pooler. Set to transaction-level pooling.
> 3. **Increase `max_connections`** in PostgreSQL from default 100 to 500+.
> 4. **Review your ORM** — switch to connection-per-query model.
> 5. **Add connection timeouts** — 5-second timeout for stale connections.
> 6. **Staging vs Production:** Staging has lower traffic, so the pool never fills.
> 7. **Monitor** connection pool metrics.

**Problem:** This advice sounds professional but could be completely wrong. The AI never questioned whether "connection pool exhaustion" is the actual diagnosis. It just pattern-matched and prescribed.

---

### ✅ With DESCEND + EXCAVATE (Treatment)

The AI first **audited its own pattern match** before prescribing:

**Step 1 — Made the pattern visible:**
> *"Pattern I'm applying: 'Connection pool exhaustion.' Conscious or auto: **AUTOMATIC** — this pattern activated immediately on reading 'connection reset by peer.' That's a red flag."*

**Step 2 — Checked structural preconditions and found a CRITICAL BREAK:**
> *"P3: Pattern requires the error to be consistent under load. This problem: **BROKEN** — error rate is 2%, not 100%. If the pool is exhausted, ALL requests during exhaustion should fail. 2% suggests something intermittent — possibly specific queries, specific connection states, or specific timing."*

**Step 3 — Surfaced hidden assumptions:**
> *"Most surprising wrong assumption: If there's a proxy/pooler BETWEEN app and DB that I don't know about, EVERYTHING changes. 'Connection reset by peer' from a PgBouncer with `server_idle_timeout` set too low looks identical but has a completely different fix."*

**Step 4 — Derived an actual investigation plan instead of a pattern-matched prescription:**
> 1. *Is the 2% hitting ALL endpoints, or SPECIFIC ones?* (If specific → query problem, not pool)
> 2. *What's the actual network path?* (App → ??? → DB. Is there a proxy?)
> 3. *Check OS-level limits:* `somaxconn` and `ulimit -n` (kernel limits don't exist in staging)
> 4. *Does 100 failing req/s equal any specific resource limit?* (PgBouncer pool size? Firewall limit?)

---

### Scoring

| Dimension | Without Skills | With Skills |
|---|:---:|:---:|
| Surface coverage | 2/2 | 2/2 |
| Hidden dimensions | 0/2 | 2/2 |
| Assumption quality | 0/2 | 2/2 |
| Alternative paths | 0/2 | 2/2 |
| Evidence calibration | 0/2 | 2/2 |
| **Total** | **2/10** | **10/10** |

### Delta: **+8**

### Why It Matters

The control answer could send a team down a multi-day rabbit hole — increasing pool sizes, adding PgBouncer, tuning `max_connections` — while the real problem (possibly a network device, OS kernel limit, or proxy misconfiguration) goes undiagnosed. The skill caught the **one anomaly** that breaks the pattern: a 2% steady failure rate is structurally incompatible with pool exhaustion. That single observation changes the entire investigation.

---

## How to Add Your Own Results

Run the [evaluation protocol](eval.md) and submit a PR, or open an issue with:

1. **The challenge** you tested (from [test_prompts.json](test_prompts.json) or your own)
2. **Which skill(s)** you loaded
3. **Which AI model** you used
4. **The response WITHOUT skills** (or a summary)
5. **The response WITH skills** (or a summary)
6. **Your depth score** for each (use the [rubric](eval.md#scoring-rubric))
