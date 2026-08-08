# 19 — Tightening Pass: Fewer Postulates, Deeper Roots

*Status: derivation document. Seven results that shrink the postulate base, push stipulations down to more primitive axioms, and discharge the two remaining criteria of docs/16. Ledger of base changes in §8. Consequences applied to docs/00, 07, 10, 11, 12, 14, 16.*

Authority: `docs/00-theory-charter.md`; builds on docs/17 (T15, T16), docs/18 (functor F, D20 at postulate grade).

---

## 1. Q1 — Operator totality (the shared lemma, named once)

Both T13 and T16 quietly used the same move: "the same event/epoch is available whatever the incoming weights, so its map is defined on the whole hosted span." Name it:

**Lemma Q1 (operator totality).** [WM2, D19-typing, A4] Structural admissibility and cost are weight-blind (WM2 has no weight terms; D19's weight terms are typed on fixed decompositions and charge updates, not admissibility). Hence the map realized by an epoch or event is defined on the entire hosted span and is state-independent; with A4, it is a single linear operator. ∎

Q1 is the license for every "for all \(\mathbf{a}\)" step below. Naming it exposes exactly where weight-blindness is load-bearing (cf. contention 7 and T17, §7).

---

## 2. B_flow is redundant: T13 rebased

**Claim.** T13 (free-epoch maps are diagonal unitary) needs neither B_flow nor R★ as inputs. **B_flow is demoted from postulate to derived.**

**Theorem T13′ (rebase).** [A4, D19 (N★), norm gauge, Q1] Free-epoch maps are diagonal unimodular (phase drift); in particular invertible.

*Proof.* By Q1 the epoch realizes one linear operator \(U\) on the span. By N★ (D19+A3 on its stated domain — fixed decomposition) every realized update preserves relative moduli; by Q1 this holds for every incoming state, so \(U\) preserves moduli on the span; with the norm gauge, absolute moduli. Apply to basis states: \(|(Ue_j)_i| = \delta_{ij}\) forces \(U e_j = u_j e_j\) with \(|u_j| = 1\). Diagonal unimodular maps are invertible. ∎

**Corollary (R★ demoted).** Invertibility of free-epoch maps is now a *consequence*, not a postulate-supported principle. The HQ postulate roster shrinks: **{A4, D19, B_flow, D12, D20} → {A4, D19, D12, D20}**.

---

## 3. T16 unified: the R-principle demoted to corollary

docs/17 proved T16a (injectivity) *from* the R-principle and then T16b (isometry) from D20. The dependence was backwards — isometry does not need injectivity as an input; it delivers it.

**Theorem T16′ (unified).** [A4, D20, O4, T15, Q1] The induced map \(M\) of a reconfiguration is an isometry (unitary at constant class count).

*Proof.* By Q1, \(M\) is one linear operator on the span. By T15 case 2 nothing is dropped; by O4 all structure persists; by D20 total weight measures total persisting structure, so \(\lVert M\mathbf{a}\rVert = \lVert\mathbf{a}\rVert\) for the realized state — hence, via Q1, for all states. A linear norm-preserving map is an isometry. ∎

**Corollary (R at reconfigurations).** Isometries are injective: "no irreversible weight loss outside projection" is now a *theorem* at reconfiguration events, not an imported principle. The R-principle survives only as the *motivation* recorded in docs/13; nothing in the theorem base cites it as a hypothesis any longer. Contention 3 (docs/07: "R and N — elevate to theorems or mark permanent semi-forced") is thereby **resolved**: N★ is a theorem on its domain (docs/17 §3); R is a corollary of T13′/T16′.

---

## 4. F2′ — weaker regularity at the ontological root

F2 (docs/14) assumed the admissible-residual set is *finite* and the disruption preorder *total*. Both hypotheses weaken:

**Lemma F2′.** [O3 + well-foundedness] If the disruption preorder on the admissible one-step residuals is **well-founded** (no infinite strictly-descending chains), minimal elements exist, and O3 licenses selecting any minimal element. Neither finiteness nor totality is required: well-foundedness is strictly weaker than finiteness, and *minimality* (nothing strictly less disruptive) suffices for O3's "prefer lower" — a total order's *minimum* was never needed.

*Proof.* Standard order theory: a well-founded preorder has minimal elements in every nonempty subset. ∎

F2 becomes the special case (finite + total ⇒ well-founded). The F-layer now rests on less.

---

## 5. RM1 — WM2's linear form pushed down to order axioms

WM2 (\(C = \alpha S + \beta B + \gamma D\)) was a stipulated formula; N1 (docs/14) correctly notes bare ordinal preference cannot fix a cardinal cost. It can, however, be fixed **up to positive scale** by named order axioms — the standard measurement-theoretic route:

**Order axioms (new, postulate grade — deliberately more primitive than WM2):**
- **AD1 (totality):** disruption comparison of reduction events is total.
- **AD2 (disjoint additivity + cancellativity):** for events at disjoint positions (well-defined by the commutation of disjoint replacements), the disruption of the combined event is the semigroup sum of the parts, and the ordered semigroup is cancellative.
- **AD3 (Archimedean):** no event is infinitely more disruptive than another; repetitions of any nonzero disruption eventually exceed any given disruption.

**Theorem RM1 (representation).** [O3, AD1–AD3] By Hölder's theorem, the ordered semigroup of disruptions embeds order-preservingly into \((\mathbb{R}_{\ge 0}, +)\), uniquely up to a positive scalar. If moreover disruption is generated by the counter increments of WM1 (each S-, B-, D-event a generator), additivity yields \(C = \alpha S + \beta B + \gamma D\) with \(\alpha, \beta, \gamma \ge 0\) the generator values. ∎

**Status change.** WM2 is **derivable via RM1**: the stipulation moves from "this formula" down to "disruption comparison is total, disjoint-additive, Archimedean" — axioms one can argue about ontologically rather than accept as a formula. N1 stands, refined: *bare* O3 fixes nothing cardinal; O3 + AD1–AD3 fixes everything up to scale (and scale is gauge).

---

## 6. L6 — the spreading lemma (docs/16 criterion C3 discharged)

**Lemma L6.** [A4, T15 definitions, CI1] An interaction-free cluster (no environment-crossing shares) is a **single** class: weights attach to share-linked residual classes (A4), and with no structural bifurcation there is exactly one class, hence exactly one weight — there are **no internal position-weights to spread**. Position and velocity live in the sequential labels (CI1), not in weights.

*Proof.* Immediate from the definitions: the class decomposition is the partition into share-linked components; an unbifurcated cluster is one component. ∎

Consequence: wave-packet spreading is not a phenomenon the WM weight layer hosts or needs to host; interference requires actual structural bifurcation (a slit event), exactly as docs/16 §2 argued informally. The continuum question (how Schrödinger-type spreading emerges from many-class limits) remains open and is now cleanly separated from the weight layer.

---

## 7. T17 — cost-decoupling / no-cheating (docs/16 criterion C4 discharged)

**Theorem T17.** [T13′, T16′, Q1, WM2] No admissible dynamics can bias Born statistics toward structurally cheap outcomes at zero cost.

*Proof.* The only weight maps are free-epoch phase drift (T13′) and reconfiguration isometries determined by the rewrite (T16′, via Q1 state-independent). Both are functions of **structure alone**; costs are weight-blind and weights are cost-blind — no admissible map takes the isolation-cost landscape as input. Hence no dynamics can steer weight toward cheap-to-select classes; the first weight-sensitive step is the D12 reading at projection, which is a reading, not a dynamics. ∎

**Bearing on contention 7.** The weight-blind selection seam is *load-bearing*: it is exactly what makes Born statistics untamperable. Any proposal to close the seam by coupling O3 to weights would reopen the cheating channel T17 closes. The seam remains open as a question of final architecture, but it now has a standing argument on the "feature" side.

---

## 8. Ledger — the base before and after

| Item | Before | After |
|---|---|---|
| B_flow | HQ postulate | **Derived** (T13′); removed from roster |
| R★ / R-principle | Principle + postulate support | **Corollary** of T13′/T16′; motivation retained in docs/13 |
| T16a/T16b | Two-step, R-dependent | **T16′ unified** [A4, D20, O4, T15, Q1] |
| F2 hypotheses | finite + total preorder | **F2′**: well-founded (partial) preorder |
| WM2 | Stipulated formula | **Derivable via RM1** from AD1–AD3 (+ WM1 generation), unique up to scale |
| docs/16 C3 (spreading) | Open criterion | **Discharged** (L6) |
| docs/16 C4 (no-cheating) | Open criterion | **Discharged** (T17) |
| Contention 3 (R and N) | Open | **Resolved** (N★ theorem-on-domain; R corollary) |
| New named axioms | — | AD1–AD3 (order axioms, strictly more primitive than what they replace); lemma Q1 |

**Net:** one postulate removed (B_flow), one principle demoted to corollary (R), one formula pushed down to order axioms (WM2 via AD1–AD3), two criteria and one contention closed. The additions (AD1–AD3, Q1) sit *below* the commitments they support — the direction "tightening" is supposed to move.

---

## 9. What this pass deliberately does not claim

- AD1–AD3 are postulates. Totality (AD1) in particular is substantive — F2′ shows the F-layer does not need it, so it is an honest *extra* strength bought for cardinality, not smuggled. **[Superseded by docs/20:** AD2 has since been derived; AD1 and AD3 are proven independent of O1–O4 and sharpened to CP and CC respectively, with the RM2 dichotomy bounding what denial yields.**]**
- D20 remains a postulate (charter §3); nothing here re-derives it.
- Born (D12) remains a reading. T17 protects it from tampering; it does not derive it.
- The φ enrichment (phase tags from binding geometry), the functor on full WM terms, and all continuum questions remain open as before.
