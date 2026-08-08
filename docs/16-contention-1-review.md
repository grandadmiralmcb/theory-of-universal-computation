# 16 — Contention 1 Under Review: The N★/Interference Fork

*Status: analysis document — **superseded in outcome by `docs/17-forced-resolution-contention-1.md`**, which resolves the fork by derivation rather than recommendation: the third category of §2 is a theorem (T15), the M_w scoping turned out to be D19's own stated hypothesis, criterion C1 is discharged (T16a/b), and horns (b)/(c2) are closed by the method rules. This survey remains as the record of the option space. All four criteria are now discharged: C1 by docs/17 (T15, T16), C2 by docs/18 (`sim/splitter_rewrite.py`), C3 by L6 and C4 by T17 (docs/19).*

Authority for what is at stake: `docs/12-RN-formalization.md` (scope note), `docs/03-quantum-sector.md` §3, `docs/11-theorems.md` (N★, T13).

---

## 1. The problem, restated exactly

D19 charges any relative-modulus change (\(M_w > 0\)); A3 selects minimal cost; the zero-change alternative costs zero. Hence **no modulus-changing weight map ever occurs in a free epoch** — including every non-diagonal unitary. But interference *is* modulus change: a beam splitter converts phase differences into intensity differences. The formalism has two event categories (free-epoch map, structural projection) and the operation interference needs is neither.

**The overlooked observation that reframes the fork.** Quantum mechanics itself is "phases-only" — in the right basis. In the energy eigenbasis, free Schrödinger evolution is exactly diagonal phase drift \(a_i \mapsto a_i e^{-iE_it/\hbar}\); all modulus change in any other basis is that same drift expressed in a rotated basis; and beam splitters are *interactions*, not free evolution. So the framework's conclusion "free epochs are phase drift" is not, by itself, un-quantum. What is un-quantum is the **rigidity**: the framework fixes one decomposition (share-linked residual classes) once and for all, and charges modulus change *in that basis*. QM's diagonal basis co-rotates with the dynamics; the framework's does not. **The contention is therefore about basis rigidity, not about phase-onlyness.**

---

## 2. Horn (a): phases-only free epochs + a third event category

*The recorded horn (a), developed.*

**Move.** Keep N★. Add a third category, the **re-decomposition event**: a structural reduction that re-partitions the coherent set's residual classes without dropping any (slits splitting one class into two; a recombiner mixing two into two). Distinctions:

| Event | Decomposition | Reversible | Weight effect |
|---|---|---|---|
| Free-epoch map | constant | yes | diagonal phase drift (N★) |
| Re-decomposition | changes, nothing dropped | yes | induced linear map (see below) |
| Structural projection | class(es) dropped | no | renormalization + Born reading |

**The move that dissolves the N★ overshoot.** N★'s proof compared weight maps as if they were freely chosen actions. Under horn (a), weight maps are never freely chosen: they are either identity-on-moduli (free epochs) or *induced by* a structural reduction whose admissibility is judged by the structural cost \(C\) (S, B, D counters) — the weight transformation is supervenient bookkeeping, not an action with its own \(M_w\) bill. Formally: **scope D19's \(M_w\) clause to fixed-decomposition intervals.** (Note: this scoping is required under *every* horn — under (b) the clause is deleted, here it is restricted — so it is the one safe edit the fork licenses immediately.)

**What must then be derived (the debt).** The induced map of a re-decomposition event. Partial results available now:

- *Isometry (target lemma L0).* A re-decomposition drops nothing (reversible) and respects the norm gauge; a linear norm-preserving map is an isometry, unitary when class count is constant. So R★-style machinery extends: induced maps ∈ isometries, plausibly provable from [A4, norm gauge, reversibility of the event].
- *Symmetry pins most of the matrix (lemma L1, provable).* For a two-class event whose rewrite is symmetric under swapping the classes, the induced unitary commutes with the swap, hence (up to global phase) is \(M(\theta) = e^{i\gamma}\big(\cos\theta\, I + i\sin\theta\, P\big)\) — a **one-parameter family** with mixing ratio \(|\sin\theta|\). Symmetry + unitarity do *not* pin the balanced splitter (\(\theta = \pi/4\)); pinning \(\theta\) needs one additional structural input (e.g. a transmitted/reflected exchange symmetry of the rewrite itself). This is the precise residue of the derivation problem — smaller than "derive the Hadamard," larger than zero.

**Two-slit in this vocabulary** (the test any resolution must pass): source class → slit event (re-decomposition, 1 class → 2, induced isometry) → free flight (phase drift \(\varphi_1, \varphi_2\); N★ holds; nothing else happens, correctly) → screen event (re-decomposition into site classes; induced isometry's matrix elements carry the accumulated phases; site amplitude \(a(x) \propto a_1 e^{i\varphi_1(x)} + a_2 e^{i\varphi_2(x)}\)) → projection at a site (Born, D12). This is standard quantum mechanics repackaged — which is the point: the vocabulary hosts it without contradiction once \(M_w\) is scoped.

**The wave-packet-spreading objection, and why it may dissolve.** In QM a free particle's position-basis moduli spread with no interaction — seemingly fatal to phases-only free flight. But in this framework a free particle is **one** structural class with sequential parameters \((x, v)\), not a continuum of position-paths: absent environmental shares, nothing structurally distinguishes position alternatives, so there are no position-weights to spread. Interference requires actual structural bifurcation (a slit event). This matches decoherence lore (no environment → no preferred position basis) and is a point *for* horn (a). The honest cost: continuum wave mechanics (a Schrödinger-equation limit) must then emerge from many-class limits — open, and now visibly harder.

**Theorem impact.** T12, T12+, R★ unchanged; N★ true as scoped; T13 becomes "diagonal in the co-moving decomposition" (nearly tautological, but *correct QM* under the reframing of §1); T14 restated: projections are the only non-unitary events, re-decompositions being isometric (pending L0). New targets: L0, L1, and the \(\theta\)-pinning condition.

---

## 3. Horn (b): weaken N★ — drop the \(M_w\) charge

*The recorded horn (b), developed.*

**Move.** Delete \(\delta M_w\) from D19 (or set \(\delta = 0\)). Free-epoch maps are then constrained by support preservation + B_flow + norm gauge: linear, invertible, norm-preserving on all states ⇒ **full \(U(n)\)** is restored, and interference is hosted inside free epochs.

**Costs.**
1. *Derivation-first retreat.* The point of D19 was to get N (and with B_flow, unitarity) *from cost*. Under (b), unitarity is postulated (A4 + norm gauge + invertibility), not derived — docs/13's "N from cost" theorem is deleted as having proved the wrong thing. Honest, but a strict loss of the layer's stated achievement.
2. *The cheating problem.* If moduli move freely in free epochs, nothing in the cost layer prevents evolution from unitarily concentrating weight on the cheapest-to-keep path just before projection, biasing Born statistics at zero cost. QM avoids this because a *Hamiltonian* dictates the unitary; this framework has no Hamiltonian (the \(\varphi_i\) problem), so (b) widens exactly the freedom the framework cannot yet constrain.
3. *Loses the §1 insight.* (b) treats the fixed structural basis as the arena and buys generic rotations in it; but QM says the diagonal basis is dynamical. (b) papers over the rigidity problem instead of addressing it.

---

## 4. Horns the record missed

**(c1) Co-moving decomposition.** Charge \(M_w\) relative to the decomposition the structure itself defines at each moment; decomposition changes are structural events. This is horn (a) stated as an amendment to D19 rather than a new event category — same content, same debts. Fold into (a).

**(c2) Path-integral re-foundation (Toolbox A).** Replace per-step weight bookkeeping with history weights \(e^{iS_{\rm struct}}\): amplitudes become *evaluations of reduction histories*, not dynamical state, and N★ dissolves because there is no weight-state to charge. Toolbox A's own trigger reads: "revisit if free evolution between decoherence events needs a sum-over-paths semantics more than a linear residual algebra" — **contention 1 is precisely that named failure**, so per the Toolbox usage rule this option is now formally licensed for evaluation (not yet for adoption). It is the deepest renovation, with the best physics pedigree, and it subsumes the \(\varphi_i\) problem (phases come from the action). Its price: the entire HQ theorem stack (T12+…T14) must be rebuilt in history vocabulary.

**(c3) Instrumentalist retreat — rejected.** "Interference needn't be hosted; only coexistence + decoherence + Born matter." This fails the two-slit test: fringe *positions* are pre-projection modulus phenomena that determine where projections occur. A framework that cannot host them fails the first quantum experiment. Recorded to close the option space.

---

## 5. Interaction with the rest of the theory

- **Baryogenesis (docs/05 §3.6).** Under (a), CP violation acquires a concrete locus: complex, conjugation-asymmetric induced maps of re-decomposition events. Under (c2), it lives in the action. Under (b), it floats in the unconstrained unitary freedom. (a) and (c2) give the sharper research target.
- **Continuous gauge groups (docs/15 §2).** The \(U(n)\)-stabilizer construction needs nontrivial maps to exist somewhere; under (a) they exist at re-decomposition events, so the gauge-group program migrates there — arguably an improvement (gauge structure as a property of *interactions*, as in physics).
- **Contention 2 (gravity).** Essentially orthogonal; no horn helps or hurts it.
- **Preferred basis (docs/05 §3.1).** The claimed virtue "the tree fixes the basis" survives under (a) in refined form: the tree fixes the basis *at each moment*, and interactions change the tree. Under (b) the virtue erodes (the basis is fixed but evolution ignores it).

---

## 6. Comparative verdict

| Criterion | (a) third category | (b) drop \(M_w\) | (c2) path integral |
|---|---|---|---|
| Preserves cost-derivation achievements | yes (scoped) | no | reframed |
| Hosts interference | yes (via events) | yes (by fiat) | yes (natively) |
| Matches QM's own architecture (§1) | yes | no | yes |
| New derivation debt | L0, L1, \(\theta\)-pinning | none (but nothing derived) | rebuild HQ stack |
| Cheating problem | contained (moduli move only at costed events) | open | contained (weights not state) |
| Size of change | small–medium | small | large |

**Recommendation.** Pursue **(a)** as the active direction: it is the smallest change that preserves the most theorems, it converts the contention's counterexample (the beam splitter) into its central object of study, and §1 shows it is the direction QM itself points. Designate **(c2)** as the fallback, now formally licensed by the Toolbox rule, to be activated if and only if (a) fails criterion C1 below. Horn (b) is dominated: everything it buys, (a) or (c2) buys with fewer losses.

The one edit safe under every horn — scoping D19's \(M_w\) clause to fixed-decomposition intervals — is recommended for immediate adoption but deliberately **not applied** by this review.

## 7. Decision criteria (what settles the fork)

- **C1 (make-or-break for (a)).** Prove L0 (induced maps of re-decomposition events are isometries) from [A4, norm gauge, event reversibility], and L1 (swap symmetry ⇒ one-parameter family) — then exhibit a structural condition pinning \(\theta\) for a balanced splitter. Failure of L0/L1 ⇒ activate (c2). Failure only of \(\theta\)-pinning ⇒ (a) survives with \(\theta\) as event data (a weaker but tenable position; QM also takes splitter ratios as device parameters).
- **C2 (correspondence).** Write the two-slit account of §2 end-to-end in the formal vocabulary and extend `sim/` with an explicit splitter rewrite whose induced map is *computed from the rewrite*, not stipulated; verify fringes from Born-at-screen.
- **C3 (spreading).** Make the §2 dissolution of wave-packet spreading precise: define which class decompositions are structurally distinguished during interaction-free flight, and confirm no position-weights exist to spread.
- **C4 (no cheating).** Under the adopted horn, prove weight dynamics cannot bias Born statistics at zero cost (trivial under (a) if L0 holds; the open problem under (b)).
