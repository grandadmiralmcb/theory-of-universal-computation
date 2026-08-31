# 28 — The Forced Layer, Audited

*Status: derivation document. Runs the audit `docs/26` §7 opened. Six results carried the entire framework — F1–F5 with the F2′ tightening — which is thin for a foundation. **Six new forced results are proposed (F6–F11), roughly doubling the layer. One standing claim is rejected**, with a countermodel: "structure cannot cease" was asserted as forced in `docs/26` stage 0 and is not. Two further candidates are examined and not promoted, with reasons. Executable: `sim/forced_layer.py`.*

Authority: `docs/00-theory-charter.md`, including §6's background ledger. Spine: `docs/26`. Existing forced layer: `docs/14` Part I.

---

## 1. The test

A result forced by O1–O4 must be statable and provable in **every faithful carrier** of O1. A result holding only for finite terms is using WM1 and belongs one layer down.

This makes the audit a discovery procedure rather than a catalogue, and it cuts both ways: it promotes results whose proofs never touch a carrier, and it rejects results whose proofs turn out to depend on one. Both happened.

**What every result below still uses.** B2, the classical metalanguage, since these are ordinary proofs. Results quantifying over admissible reductions also inherit **B3** — admissibility is used throughout the framework and defined nowhere — so they are forced *relative to whatever admissibility turns out to be*. That is not a defect of these results specifically; it is the framework's, and it is contention 12.

---

## 2. F6 — Interleaving independence

**Claim.** [O2, B8] Let a finite set of events carry a dependence order. Every total order extending it produces the same outcome and the same causal order, and nothing in O1–O4 distinguishes one such linearisation from another.

**Derivation.** O2 says sequential order is constructed locally by successive reduction and is not a global parameter. Events not related by dependence are therefore not ordered by anything: no evaluator's chain relates them, and there is no global parameter left to appeal to. Independent events commute, so the outcome is invariant across linearisations, and the dependence order is invariant by construction. ∎

**Consequences, which are larger than the statement.**
- **There is no global "now".** Simultaneity across independent events is not merely unknown; there is no fact of the matter.
- **There is no privileged global state.** What exists is the partial order and the structure, not a sequence of world-states.
- This is the precise content of "background independence is native to O2", which `docs/05` §3.2 asserts without deriving.

The proof sketch of SM-B3 already leans on this ("∐ depends only on the local chains and share links, not on the interleaving") without it having been stated as a result.

*B8 is named because the enumeration argument is for finite event sets; infinite orders need a limit argument not given here.*

---

## 3. F7 — Selection is non-destructive

**Claim.** [O4] Selecting one residual from an admissible set leaves the totality of real structure unchanged.

**Derivation.** Immediate from O4: the unselected remain real. The selected one is real. Nothing is subtracted. ∎

This is weaker than it may look, and §8 is about exactly how much weaker.

---

## 4. F8 — Accessibility is proper

**Claim.** [F1, F2, O4] If at any point along a chain two or more residuals are admissible, then the chain is a **proper** subset of what is real: no evaluator's record contains all real structure.

**Derivation.** F2 gives a selection from the admissible set. F1 makes the chain the record of successive selections, so it contains one residual per step. O4 keeps the unselected ones real. With two or more admissible at some step, the real structure strictly exceeds the chain. ∎

**What this is the root of.** TH3 (horizon reduction) currently carries [F1, F3/O4, SB4, SM-B3, A4]. Its ontological core — that an evaluator's access is a restriction rather than a totality — needs **none of SB4, SM-B3 or A4**. So the "experienced world is an interface, not the substrate" reading rests on something forced, while the machinery it was stated with is not. That relocation is the point of the audit.

---

## 5. F9 — Preference is structurally determined

**Claim.** [O3, analytic] The disruption ordering depends only on the change-set: what sharing, binding and observational identity were altered. Nothing else can enter it.

**Derivation.** O3's own parenthetical defines disruption as change to sharing, binding, or observational identity. A ranking that varied while the change-set was held fixed would not be a ranking of disruption. Analytic to the definition, not an empirical claim. ∎

**What this is the root of.** T17's cost-decoupling — that no admissible dynamics can bias Born statistics toward cheap outcomes — currently carries [T13′, T16′, Q1, WM2]. Weight-blindness, the load-bearing part, is F9 and needs none of them. Contention 7's "the seam is a feature" argument likewise stands on something forced.

**The weak form only.** That *isomorphic* change-sets rank **equally** is stronger. It is PC, and `docs/20` §2 derives it from O2 plus **SI**, which that document calls a reading. F9 claims only that non-structural data cannot enter, not that structurally-alike changes rank alike.

---

## 6. F10 — Selection need not be unique

**Claim.** [F2′] O3 licenses selecting *a* minimal residual and does not single one out. Under a partial preorder minimal elements need not be unique; under a total preorder distinct residuals may still be equivalent. Either way, **determinism of selection is not forced.**

**Derivation.** F2′ replaces minimum with minimality over a well-founded partial preorder, and minimal elements of a partial order are generally several. `docs/20` §4's own countermodel — componentwise order on \(\mathbb{N}^k\) — exhibits the case. ∎

**Why this matters beyond bookkeeping.** Two open problems turn on it. Whether O3's selection is deterministic is the Church–Rosser question of `docs/26` stage 2. And the preferred-frame risk in `docs/25` and `docs/27` §6 was that a deterministic argmin might pick out a frame; F10 says the framework does not require one, so **the tie set is where any isotropy would have to live**. That was speculation when written and is now resting on a forced result.

---

## 7. F11 — Order carries no orientation

**Claim.** [O2] The converse of a strict partial order is a strict partial order. So the order O2 constructs fixes which events neighbour which, and fixes nothing about which end is the past.

**Derivation.** Irreflexivity and transitivity are preserved under converse; F1's chain condition is reversal-invariant. ∎

**Promotion.** This is AT2, stated in `docs/25` inside the AT layer. It is a fact about orders and no working model enters, so it belongs in the forced layer. The AT layer's own account is unaffected: AT3 and AT4 still supply the orientation, and they need the HQ layer or F5 respectively.

---

## 8. Rejected — "structure cannot cease"

`docs/26` stage 0 states the split as an **assumed origin and a forced persistence**, arguing that O3 ranks reductions rather than configurations and that "there is also no move to reach it by: reduction rewrites structure, and the calculus has no global annihilation operator."

**The second clause is a fact about WM1, not about O1–O4**, and the audit's test catches it.

**Countermodel.** Take structures to be finite multisets of atoms, some atoms held in common by two parts. Composition is union; sharing is an atom held by two parts; reduction includes a rule that discards one atom; disruption prefers discarding fewest shared atoms; and the results of unselected reductions remain real. This satisfies O1, O2, O3 and O4. In it the empty structure is reachable in finitely many steps. ∎ (Executable: `sim/forced_layer.py` §7.)

**What survives.** O4 constrains **selection**, saying the residuals not chosen remain real. It says nothing about whether a reduction may destroy what it acts upon. So:

| Claim | Status |
|---|---|
| Selection is non-destructive | **Forced** — F7 |
| Structure cannot cease | **Not forced.** Holds in WM1, whose rule set has no annihilation rule |

`docs/26` stage 0 is corrected accordingly. The "why not nothing" argument keeps its first leg — O3 ranks moves and not configurations, so nothing is never a cheap option — and loses the claim that no move could reach it. That leg was carrying more weight than it could bear.

---

## 9. Examined and not promoted

**TH12a, disjoint additivity.** `docs/20` §3 grounds AD2 in M1/M2, PC and IND, and states plainly that the non-analytic residue is **SI and SC, both readings**. A result resting on two readings is not forced. It remains derived-modulo-readings, which is where `docs/20` already put it; the audit confirms rather than changes this.

**TH2's ordinal form**, that isolating a region disturbs only what crosses its boundary. This is forced *given a definition of isolation as severing exactly the crossing links*, and the definition is doing the work: another carrier could define an isolation move that also disturbs interior structure. Definitional rather than forced. Not promoted.

Recording the failures matters as much as the promotions. A test that only ever promotes is not a test.

---

## 10. The forced layer after this pass

| ID | Claim | From |
|---|---|---|
| F1 | Local sequential chains exist | O2 |
| F2 / F2′ | Minimal-disruption residual exists | O3 + well-foundedness |
| F3 | Unselected remains real | O4 |
| F4 | Co-dependence admits disruption comparison | O1, O3 |
| F5 | Structural projection when break ≤ maintain | F4, O3 |
| **F6** | **Interleaving independence; no global now or global state** | **O2, B8** |
| **F7** | **Selection is non-destructive** | **O4** |
| **F8** | **Accessibility is proper; no chain holds all of it** | **F1, F2, O4** |
| **F9** | **Preference is structurally determined** | **O3, analytic** |
| **F10** | **Selection need not be unique** | **F2′** |
| **F11** | **Order carries no orientation** | **O2** |

Six results become twelve. Three of the new ones relocate load off postulates that were carrying it unnecessarily: F8 under TH3, F9 under T17, F11 out of the AT layer.

**What the audit does not claim.** No new physics, and no discharge of any contention. Every result above still sits on B2, and those touching admissibility sit on B3, which remains undefined. A larger forced layer is not the same as a better-founded one, and contention 12 is still the deepest thing in the way.
