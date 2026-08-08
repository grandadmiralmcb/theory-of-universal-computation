# 17 — Contention 1 Resolved by Derivation

*Status: derivation document. Resolves the fork surveyed in `docs/16-contention-1-review.md` by entailment from prior commitments. **No new postulate is introduced**; §5 lists exactly which priors carry the load, and §4 flags the single explication (a definition, not new physics) the chain requires. Consequences applied to docs/03, 07, 11, 12, 13.*

---

## 0. The demand

Fork resolutions must be forced by the axiomatic roots — O1–O4, F1–F5, the adopted postulates (WM, CI, HQ, SB), the definitions D12–D19, and the method rules of the charter — not chosen by taste. This document shows they are.

---

## 1. The decomposition was never free to be rigid

The decomposition of a coherent set into "paths" was never an independent choice: classes **are** the share-linked components of the persisting residual set. That is prior commitment, not new content — O1 supplies sharing, O4 supplies persistence of the unselected, and the class structure is a *function* of the evolving term. Reductions rewrite share structure (O1, WM1). Therefore **the decomposition co-moves with the structure by definition.** The "basis rigidity" diagnosed in docs/16 §1 was an artifact of presentation — nothing in the corpus ever committed to a frozen decomposition.

---

## 2. The event trichotomy is a theorem

**Theorem T15 (event trichotomy).** [WM1, A4, O4, F5] Every reduction event bearing on a coherent set is exactly one of:

1. **Free-epoch map** — the class decomposition is unchanged;
2. **Reconfiguration** — the decomposition changes and every class's structure persists (into the new classes);
3. **Structural projection** — some class ceases to be maintained (F5).

Mixed events factor as (3)∘(2).

*Proof.* The decomposition after the event either equals the decomposition before (case 1) or differs. If it differs, either all prior class structure persists (O4 bookkeeping: nothing isolated-and-dropped — case 2) or some does not, which is precisely F5's projection (case 3); an event doing both factors into a projection composed with a reconfiguration of the survivors. Exhaustive by construction. ∎

*Non-emptiness of case 2.* WM1 admits reductions that reassociate shared substructure across two classes without isolating any residual; such an event changes the partition and drops nothing. (A slit: one class → two. A recombiner: two → two, re-partitioned.)

The prior formalism recognized only cases 1 and 3. **The "missing category" of contention 1 was an incomplete case analysis, not a modeling freedom.** Horn (a) of docs/16 is not adopted — it is derived.

---

## 3. N★ never applied across reconfigurations

D19's modulus clause is stated, in `docs/12-RN-formalization.md`, **"for a weight update \(\mathbf{a}\to\mathbf{a}'\) with topological Foot fixed."** Moreover \(M_w = \lVert\boldsymbol{\mu}'-\boldsymbol{\mu}\rVert_1\) requires a common index set for \(\boldsymbol{\mu}\) and \(\boldsymbol{\mu}'\) — the same classes on both sides. Across a reconfiguration the class set itself changes: the comparison \(M_w\) invokes is **not well-typed** there, and the same holds for \(S_w\) (support is indexed by classes).

Consequently:

- **N★ is true, and always was, on its stated domain** (fixed decomposition). Free-epoch maps are diagonal phase drift (T13). Nothing here is revised.
- **"N★ forbids beam splitters" was a scope error**: a beam splitter is a reconfiguration (T15 case 2), where the cost comparison N★'s proof invokes does not exist. No cost clause of the corpus ever charged — or could charge — a reconfiguration's weight effect, because the weight terms of D19 are undefined across it. Its admissibility is governed by the **weight-blind** structural cost (WM2), as with every structural reduction.

This is a *reading* of D19's own hypothesis, not an amendment to it. The "M_w scoping" that docs/16 recommended as an edit turns out to require no edit: the scoping was already in the definition.

---

## 4. The induced map: what is forced, and the one explication

A reconfiguration is a structural rewrite. Its admissibility and cost are weight-blind (§3), so the *same* event is available whatever the incoming weights; and A4 makes reduction **linear** on share-linked residuals. Hence the event induces a single linear map \(M\) on the hosted span, determined by the rewrite (by how it redistributes shared substructure over the new classes), independent of the incoming state.

**Theorem T16a (forced).** [A4, R-principle, T15] Induced maps of reconfigurations are **injective** linear maps determined by the rewrite.

*Proof.* Linearity and rewrite-determination as above. Injectivity: the R-principle as stated in `docs/13-derive-RN-from-cost.md` — *"weight dynamics must not smuggle irreversible loss; irreversibility is reserved for structural projection"* — quantifies over all non-projection weight dynamics. B_flow formalized it for the only non-projection category then recognized (free epochs); T15 exhibits the second category, and the principle's stated content extends verbatim: a non-injective \(M\) would destroy weight distinctions without a projection. ∎

**D20 (explication).** *Weight is a measure of persisting structure*: \(|a_i|^2\) quantifies the persisting residual structure of class \(i\), of which D12's Born reading at projection is the selection-time special case.

D20 is the one sentence in this resolution that is an **explication rather than a strict entailment**. It adds no new physics: it names what D12 already treats \(|a|^2\) as (a weight *of a persisting alternative* — O4's persistence is what makes the Born reading coherent between projections at all). But honesty requires flagging it: a reader who refuses D20 keeps T16a and loses only T16b.

**Theorem T16b (forced given D20).** [A4, T15, T16a, D20, O4] Induced maps are **isometries** (unitary when the class count is unchanged).

*Proof.* By D20 and O4, total persisting-structure weight is conserved by any event that drops nothing: \(\lVert M\mathbf{a}\rVert = \lVert\mathbf{a}\rVert\) for the realized state. By weight-blind admissibility (§3) the same event occurs for every incoming \(\mathbf{a}\) in the span, so the identity holds for all \(\mathbf{a}\). A linear norm-preserving map is an isometry; at constant class count, unitary. ∎

**Corollary T14′.** [T13, T15, T16b, T10] Non-isometric weight change occurs at structural projection and **nowhere else**.

*Proof.* Trichotomy (T15); case 1 is diagonal-unitary (T13); case 2 is isometric (T16b); case 3 drops weight and renormalizes. ∎

**Readout reconciliation (corollary).** The "two readout rules" of the former contention were one rule: screen intensity at site \(x\) is \(|(M_{\rm screen}\mathbf{a})_x|^2\) — the interference formula \(|\sum_i a_i e^{i\varphi_i}|^2\) is a matrix element of the screen's reconfiguration isometry, followed by D12 at projection. There was never a second rule.

---

## 5. The ledger: what forced what

| Conclusion | Forced by | Status |
|---|---|---|
| Decomposition co-moves | O1, O4, WM1 | definitional |
| T15 trichotomy | WM1, A4, O4, F5 | theorem (case exhaustion) |
| N★ scope; reconfigurations uncharged by weight terms | D19's stated hypothesis + typing of \(M_w, S_w\); WM2 weight-blindness | reading, no edit |
| T16a injectivity | A4, R-principle (as stated, docs/13) | theorem |
| D20 | explication of D12 × O4 | **the one added sentence** |
| T16b isometry | A4, T15, T16a, D20, O4 | theorem given D20 |
| T14′ | T13, T15, T16b, T10 | corollary |

No postulate was added. The residual conventional element (overall norm scale) is empirically empty given D12's renormalization at projection.

---

## 6. The horns, disposed of by method

- **(a)** — not chosen: **derived**. T15/T16 are its content.
- **(b)** (delete the \(M_w\) charge) — would revise a prior commitment (D19) that, read on its stated domain, is *not refuted*. Barred by the charter's derivation-first rule. Closed.
- **(c2)** (Toolbox-A path integral) — its license required a named failure of the active direction (Toolbox usage rule); the failure is discharged by §§2–4. **License lapsed**; Toolbox stays closed.
- **(c3)** — already rejected (fails the two-slit test; docs/16 §4).

The fork is resolved without any act of preference.

---

## 7. What remains is construction, not choice

1. **The induced-map functor** (docs/16 criterion C2): for a concrete splitter rewrite, compute \(M\) from the share bookkeeping of the rewrite and verify it is the isometry T16b requires; then fringes from D12 at the screen. The mixing ratio of a given splitter is **device data** (fixed by that device's rewrite), exactly as in laboratory QM — determination of \(M\) by the rewrite means no theory-level freedom remains. Target: `sim/` splitter demo.
2. **Spreading precision** (criterion C3): state formally that an environment-disconnected class carries no internal position-weights; docs/16 §2's dissolution then becomes a lemma.
3. **Continuum limits** — dense sequences of reconfigurations → continuous generators (Schrödinger-type limits): the standing CI-style idealization question, now well-posed but open.
4. **Born as theorem** — D12 (and now D20) remain readings; unchanged by this resolution.
