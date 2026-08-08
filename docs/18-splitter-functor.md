# 18 — The Splitter Functor: Induced Maps Computed from Rewrites

*Status: construction + theorem document, written in response to the adversarial review of T15/T16 (pressures P1–P4, dispositioned in §5). Executable: `sim/splitter_rewrite.py`.*

Authority: `docs/17-forced-resolution-contention-1.md` (T15, T16a/b), `docs/00-theory-charter.md` (D20 is now postulate-grade — see §5/P2).

---

## 1. The functor F (unit-share granularity)

**Data of a reconfiguration rewrite.** The event describes each old class \(i\) as \(n_i\) **unit shares** (structure quanta at the event's own granularity), and specifies a **routing**: every unit goes to exactly one new class, carrying an **orientation tag** \(t_u\) (a phase — device data from binding geometry).

**Domain restriction (channel-disjointness).** At most one unit per (old class → new class) pair. Outside this domain, coherent same-class stacking inflates the persisting-structure measure (§4) — such routings encode intra-class merges and are not pure reconfigurations.

**Definition (F).**
\[
M_{ji} \;=\; \sum_{u\,:\,i\to j} \frac{t_u}{\sqrt{n_i}}
\qquad\Longrightarrow\qquad
|M_{ji}|^2 \;=\; \frac{\#\{u : i \to j\}}{n_i}
\;\;\text{(routed fraction, on the domain)}.
\]

**What determines what:**

| Component of \(M\) | Determined by | Status |
|---|---|---|
| Moduli \(|M_{ji}|^2\) | Routing fractions — D20 applied at unit granularity | Forced given D20 + granularity |
| Phases \(\arg M_{ji}\) | Orientation tags | Device data, filtered by T16b (§2) |
| Unit granularity \(n_i\) | The event's own description | WM modeling data (class weights are granularity-independent, since only fractions enter) |

---

## 2. Results (executable, `sim/splitter_rewrite.py`)

**L2 (splitter).** The symmetric 1→2 routing (2 units, one per arm, trivial tags) yields \(M = (1/\sqrt2,\ 1/\sqrt2)^{\mathsf T}\) — computed, isometric.

**L3 (recombiner pinning).** For the symmetric 2→2 routing (each class one unit per detector), enumerate all \(\pm1\) tag assignments: exactly the **odd-sign-flip half** (8 of 16) passes the T16b isometry filter, and **every survivor equals the Hadamard up to diagonal \(\pm1\) gauge**. The balanced beam splitter is therefore **derived**: moduli from routing (D20), phase structure pinned up to gauge by the isometry requirement. The θ-pinning residue of docs/16 §2 is discharged for the symmetric case — symmetry fixes the moduli, T16b fixes the tag class.

**L4 (Mach-Zehnder).** Splitter → free-epoch diagonal drift (N★ holds; nothing else happens, correctly) → derived recombiner → Born at detectors gives \(P(C) = \cos^2(\varphi/2)\) exactly, visibility 1; Monte Carlo agrees. **The framework hosts a working interferometer with no stipulated matrix.**

**L5 (negative cases — the filter does real work).**
- A 2→1 **merge** admits no isometric induced map (no isometry \(\mathbb{C}^2 \to \mathbb{C}^1\) exists): class-count-decreasing events always contain a projection component; T15 classifies them as (3)∘(2). Derived, not stipulated.
- A **non-channel-disjoint** routing (all units to one detector) inflates a column norm to 2 — a D20 violation exhibiting exactly why the domain restriction exists.

---

## 3. What this discharges, and what remains

**Discharged.**
- "Determined by the rewrite" (T16a) is no longer a promissory note *on the functor's domain*: \(M\) is computed from (routing, tags), moduli are forced, and in the symmetric case the tags are pinned up to gauge.
- Criterion C2 of docs/16 (a concrete splitter with fringes from Born-at-screen).

**Remaining, stated plainly.**
- **Tags are still device data** outside the symmetric case: T16b constrains but does not always pin them. The φ enrichment (phases from binding geometry) remains the open derivation.
- **Granularity** is event data: F is defined at the event's own unit decomposition. Only routed fractions enter the moduli, so class weights are granularity-independent — but a principled account of what fixes an event's granularity is open.
- The functor is exhibited for the **unit-share toy**, not for arbitrary WM terms. Lifting F to the full term language (docs/08's real-tree standard) is the next structural debt.

---

## 4. The selection seam (pressure P3, recorded)

The review's sharpest architectural point: **O3 never sees weights outside projection.** Cost is weight-blind (WM2; D19's weight terms are typed on fixed decompositions), so *which* reconfiguration occurs is selected on structural cost alone, and the induced map transforms weights as passengers. Interferometric structure (which devices exist, where) is external data — exactly as the Hamiltonian and apparatus are external data in laboratory QM, but the seam deserves its own ledger entry rather than an analogy:

- It is **entailed** by the corpus as it stands (weight-blindness is not a slip; it is D19's typing).
- It is recorded as **contention 7** in `docs/07-roadmap.md`: is weight-blind selection final, or should O3 couple to weights outside projection? Any coupling would have to survive N★ on fixed decompositions, which sharply constrains the possibilities.

---

## 5. Adversarial-review dispositions (P1–P4)

| Pressure | Disposition |
|---|---|
| **P1** — build the splitter or drop "determined by the rewrite" | **Built** (§§1–2, `sim/splitter_rewrite.py`). The claim is kept, scoped to F's domain; residual device data stated in §3. |
| **P2** — D20 as a named postulate, same grade as A4 | **Adopted.** D20 now has a charter §3 row; hypothesis lists cite it at postulate grade. docs/17's "no new postulate" headline is amended accordingly (see the addendum there): the honest count is one postulate (D20), one principle-extension (R to case 2), one construction obligation (F — now discharged at toy level). |
| **P3** — how does O3 select reconfigurations if cost is weight-blind? | **Recorded as contention 7** (§4). Not resolved; named. |
| **P4** — don't let D20 promote \(\|a\|^2\) into ontology / derive Born silently | **Guarded.** D20 supplies *meaning* (weight measures persisting structure), not *probability*: \(P \propto |a|^2\) at projection remains the non-derived reading D12. The charter row says so explicitly. |

Also accepted from the review: **T15 is a classification of outcomes, not a dynamical theorem** — it does not entail that type-2 rewrites occur or are preferred (occurrence is governed by structural cost and device structure; contention 7); and the (3)∘(2) factorization of mixed events is bookkeeping convention, not forced temporal order. Both notes now appear where T15 is stated.
