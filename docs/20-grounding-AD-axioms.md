# 20 — Grounding AD1–AD3 in the Ontological Minima

*Status: derivation document. Discharges roadmap priority 5 to the extent derivation permits, and proves exactly where it does not: AD2 decomposes into grounded sub-principles; **AD1 and AD3 are independent of O1–O4** (countermodels in §§4–5) and are sharpened into two named principles — CP (universal comparability) and CC (common currency) — with a dichotomy theorem (RM2) and precise denial profiles. The stipulation content of the entire classical quantitative chain is thereby reduced to two bits.*

Authority: `docs/00-theory-charter.md`; refines docs/19 §5.

---

## 0. Result in one view

| Axiom | Fate |
|---|---|
| **AD2** (disjoint additivity + cancellativity) | **Grounded** — decomposes into PC (from O2 + SI), M1/M2 (analytic to O3's "disruption = change"), and IND (from O2's localism + SC). §3 |
| **AD1** (totality) | **Independent of O1–O4** (countermodel §4). Sharpened to **CP**; denial keeps all qualitative dynamics (F2′) and loses only the single global cost scale. |
| **AD3** (Archimedean) | **Independent of O1–O4** (countermodel §5). Sharpened to **CC**; the RM2 dichotomy shows denial yields a coherent *stratified-cost* theory variant (Hahn embedding) rather than incoherence. |

---

## 1. The change-set semantics of disruption

O3's parenthetical *defines* disruption: change to sharing, binding, or observational identity. Formalize: every reduction event \(e\) has a **change-set** \(\Delta(e)\) — the set of sharing/binding/identity facts it alters. Two principles are analytic to reading "disruption" as *amount of change*:

- **M1 (change monotonicity).** \(\Delta(e) \subseteq \Delta(e')\) (up to structural isomorphism) \(\Rightarrow e \preceq e'\).
- **M2 (strict).** Proper inclusion \(\Rightarrow\) strict comparison.

*Grounding status:* deniable only by reading disruption as non-gradable — which O3's own comparative ("prefer **lower**") already excludes. Treated as forced-by-meaning.

## 2. Position covariance from O2

- **SI (structural individuation).** Patterns are individuated by their structure: isomorphic change-sets are the *same* change. (Constitutive of an informational ontology — a pattern *is* its structure; the docs/01 preferred reading says as much.)
- **PC (position covariance).** Disruption comparison depends only on the isomorphism type of the change-set, not on *where* it occurs. *Derivation:* location-sensitivity would require a distinguished global labeling of positions; O2 denies that sequential order — or any global coordinate — is a parameter of the structure, and SI leaves nothing but structure to individuate by. ∎ (mod SI)

For finite change-sets, PC + SI reduce a change-set to its **multiset of change types** — a vector in \(\mathbb{N}^k\) — and disjoint composition to vector addition.

## 3. AD2 grounded (decomposed)

For position-disjoint events, \(\Delta(e \sqcup e') = \Delta(e) \uplus \Delta(e')\) (locality; commutation of disjoint replacements). AD2's content splits into three:

1. **Congruence** (the combined disruption depends only on the parts' disruptions): from PC + SI. ∎
2. **Monotonicity** (adding disjoint change never lowers disruption): from M1. ∎
3. **Translation invariance / cancellativity** (\(e \prec e' \Leftrightarrow e \sqcup f \prec e' \sqcup f\) for disjoint \(f\)): **not** derivable from PC + M alone (counterexample: rank by \(x + y + xy\) on \(\mathbb{N}^2\) — total, strictly monotone, iso-invariant, *not* translation-invariant). It is grounded separately:
   - **SC (selection coherence).** Global preference restricted to a local competition agrees with the local preference.
   - **IND (independence of disjoint context).** For disjoint \(f\): \(e \prec e' \Leftrightarrow e \sqcup f \prec e' \sqcup f\). *Derivation:* selection is performed by local evaluators (O2); an evaluator at the site of the \(e\)-vs-\(e'\) competition has no access to unrelated \(f\); if the global comparison flipped under \(\sqcup f\), O3's preference would disagree with every local selection — contradicting SC. ∎ (mod SC)

**Verdict.** AD2 holds given {M1, M2, PC, IND}, of which the non-analytic residue is SI and SC — both readings of O1/O2 (structure-individuation; local selection coheres with global preference) rather than new physics. AD2 is retired from the charter's postulate row and re-listed as derived.

## 4. AD1 is independent: the partial-order countermodel

Take the disruption order to be **componentwise order on \(\mathbb{N}^k\)** (change-set inclusion up to iso). This satisfies O1–O4, M1/M2, PC, IND (vector order is translation-invariant), and is cancellative — but **not total**: (2 sharing-changes, 0 identity-changes) and (0, 1) are incomparable. All qualitative dynamics survives: F2′ needs only well-founded partial preorders; minimal-disruption selection, T2, T9–T12, T15, T16′ are untouched.

**CP (universal comparability)** — the sharpened residue of AD1: any two disruptions are comparable. What CP alone buys: the possibility of a *single* cost scale. What its denial costs: Szpilrajn extensions to total orders exist but are non-canonical, so cardinal cost becomes a representational *choice* — cost talk is chart-relative, physics (selection) is not.

## 5. AD3 is independent: the lexicographic countermodel

Take the **lexicographic order on \(\mathbb{N}^2\)** (identity-changes lexically dominate sharing-changes) with vector addition. This satisfies O1–O4, M1/M2, PC, IND, AD1 (total), cancellativity — but is **non-Archimedean**: \(n\) sharing-changes never reach one identity-change, for any \(n\).

**Theorem RM2 (dichotomy).** [AD1, AD2] A totally ordered, cancellative, translation-invariant disruption semigroup is either **Archimedean** — then Hölder embeds it in \((\mathbb{R}_{\ge 0}, +)\) uniquely up to scale (RM1; WM2's form) — or **stratified** — then a Hahn-type embedding places it in a lexicographic product of reals, and cost is a priority-ranked vector. ∎ (Hölder; Hahn)

**CC (common currency)** — the sharpened residue of AD3: no change-type infinitely outweighs another; all disruption is in one currency. Three notes:

- The corpus already speaks this language: docs/01's matter/energy unity is asserted "under common currency." CC elevates that phrase to its load-bearing role.
- Denying CC is *coherent*: the stratified variant is a real alternative theory in which, e.g., observational-identity changes lexically dominate. RM2 says these are the only two shapes.
- CC has an empirical flavor: any finite calibration cannot distinguish an infinite priority from a huge finite one (a large-but-finite \(\gamma\) in WM2 approximates lexical dominance to any tested precision). CC is the closure assumption that priorities are finite — analogous in status to Archimedean axioms in measurement theory generally.

## 6. Q2 — the separation theorem

**Theorem Q2.** [O1–O4, M1/M2, PC, IND] The qualitative theory — F1–F5 with F2′, minimal-disruption selection, T2, T9–T12, the trichotomy T15, and (given the weight-layer postulates A4/D19/D20) T13′/T16′/T14′/T17 — requires **neither CP nor CC**. CP + CC are needed **exactly** for the cardinal representation (RM1) and hence for the quantitative classical chain (T3–T8, the T6 ratio).

*Proof sketch.* Inspection of hypothesis lists: no qualitative theorem cites AD axioms; RM1's proof uses totality (Hölder's hypothesis) and Archimedeanness essentially, and T3–T8 consume the numeric \(C\). ∎

**Reading.** The stipulation content of the entire classical quantitative sector is now **two bits**: CP (there is one comparison) and CC (there is one currency). Everything else in that sector is grounded in the minima, the change-semantics of O3, or explicit WM/CI modeling choices already on the ledger.

## 7. Ledger and residue

| Item | Before this pass | After |
|---|---|---|
| AD2 | Postulate | **Derived** from M1/M2 + PC + IND (residual readings: SI, SC) |
| AD1 | Postulate | **CP**, proven independent (§4), named, denial profile stated |
| AD3 | Postulate | **CC**, proven independent (§5), named, RM2 dichotomy + denial profile |
| RM1 | [O3, AD1–AD3, WM1] | Restated: [M1/M2, PC, IND, CP, CC, WM1] |
| Classical-chain stipulations | "AD1–AD3" (a block) | **CP + CC** (two principles, each with an exact alternative) |

**Residue, honestly:** SI and SC are readings of O1/O2 — arguably constitutive, but a determined skeptic can price them; they are named so the price is visible. CP and CC are genuine commitments; RM2 guarantees there is no third option to look for. Whether the *stratified* (¬CC) variant deserves parallel development is a legitimate open question — it is the one place in the classical sector where O1–O4 permit a structurally different theory.

**Update (2026-08-08):** the stratified variant was developed (docs/21) and the question resolved by synthesis and adoption: **CC′** (exact strata above one Archimedean floor) supersedes CC as a charter postulate, with TS1/TS2 supplying the phenomenological argument that the *dynamical floor* must be Archimedean. This document's independence proofs stand unchanged; CC's role is now played by CC′'s floor clause.
