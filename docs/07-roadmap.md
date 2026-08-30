# 07 — Roadmap, Open Questions & Contentions

## Theorem status (see `docs/11-theorems.md`)

| ID | Result | Status |
|----|--------|--------|
| T1–T2 | Cost well-defined; preferential select | Proved [WM1, WM2] |
| T3–T8 | Classical sequential calculus, Newton, ratio, projectile, potential | Proved [WM3, CI1–CI4] |
| T9–T11 | Isolation/maintain, decoherence, classical limit of coherence | Proved [WM1, WM2; T11 also WM4] |
| T12 | Free epoch share-preserving | Proved [WM] |
| T13 | Diagonal-unitary free epoch | Proved [R★, N★, norm gauge] (docs/17) |
| T15 | Event trichotomy: free map / reconfiguration / projection | Proved [WM1, A4, O4, F5] |
| T16a/b | Reconfiguration maps injective; isometric | Proved [A4, R-principle] / [+ D20, O4] |
| T14′ | Non-isometric change ⇔ structural projection | Proved [T13, T15, T16b, T10] |
| SM-B1 | Label conservation by typing | Proved [WM1, SB1, SB1-typing] |
| SM-B2 | Discrete WM spectrum per label class | Proved [WM1–3, SB1, SB3] (counter artifact; continuum open) |
| SM-B3 | Causal partial order of reduction events | Proved [WM1, F1] |
| T13′/T16′ | Free epochs diagonal; reconfigurations isometric — B_flow and R demoted to derived | Proved (docs/19 §§2–3) |
| T17 | Cost-decoupling: Born statistics untamperable by dynamics | Proved [T13′, T16′, Q1, WM2] |
| L6 | Spreading lemma: single class ⇒ no internal position-weights | Proved [A4, T15, CI1] |
| RM1 | WM2's linear form from order axioms AD1–AD3 (Hölder) | Proved conditionally (docs/19 §5) |
| F2′ | Minimal residuals under well-founded partial preorder | Proved [O3 + well-foundedness] |
| TH1–TH2 | Only relative entropy is observable; area law is WM2's own shape | Proved [RM1, CI4, WM1] / [WM1, WM2] (docs/24 §§1–2) |
| TH3–TH5 | Horizon reduction; structural monotonicity; first law of entanglement | Proved [F3/SB4/A4] / [T15, T13′, T16′, T14′] / [TG1, A4] |
| TH6–TH7 | Einstein equation by two routes; \(G=1/(4s_0\eta_N)\) | Proved [TG1–TG5] — **conditional on TG2**, the unsolved continuum limit |
| TH8 | Weak equivalence principle from one shared counter | Proved [WM3, TH2, TG1, TG2] — **closes contention 2** |
| TH9–TH11 | Generalized second law; area theorem + merger inequality; Bekenstein | Proved [TH4, SM-B3] / [TH5] |
| TH12 | Additivity on disjoint systems (= AD2); defect = mutual information = \(2s_0N_{\rm cross}\) | Proved [WM1, WM2, AD2] (docs/24 §2.1) |
| AT1–AT2 | Order forced by O2 and prior to entropy; order fixes no orientation | Proved [O2, F1, SM-B3] (docs/25) |
| AT3–AT4 | Orientation lives at projection alone; the ratchet is F5 + stable exclusion | Proved [TH4, T14′] / [F5, O4, SM-B3] — **arrow sits below the TG stack** |
| AT5–AT6 | Arrow density = decoherence density; duration counted by projection events | Proved [T10, T11, WM4] / [AT3, TH5] |

## Current Contentions

1. **N★ vs interference — RESOLVED by derivation (`docs/17-forced-resolution-contention-1.md`).** The fork dissolved: the event trichotomy (T15) is a theorem of case exhaustion; N★ never applied across reconfigurations (D19's \(M_w\) is typed on a fixed decomposition — its own stated hypothesis); reconfiguration maps are injective (T16a, forced) and isometric (T16b, forced given the D20 explication). Horn (b) was barred as unforced revision of an unrefuted commitment; the Toolbox-A license lapsed with the named failure discharged. Survey of the option space preserved in `docs/16-contention-1-review.md`. Residue is construction, not choice: the induced-map functor / splitter rewrite (docs/17 §7).
2. **Gravitational bias coupling — RESOLVED conditionally (`docs/24-thermodynamics-gravity.md`, TH8).** \(b_{\rm grav}=m_{\rm struct}\,g\) is now **derived**, not imposed by observation: the entropic bias is proportional to the cluster's share count (TH2/TH8), and WM3's inertia is the same share count — one counter, two roles, so \(g_{\rm eff}\) is cluster-independent. Residue: (i) the derivation runs through **TG2**, the unsolved continuum limit, so it is conditional; (ii) **TH8-ε** — WM3's floor \(\varepsilon\) predicts a residual violation \(\eta_E\simeq(\varepsilon/\alpha_m)|n_1^{-1}-n_2^{-1}|\), which is only harmless if \(\varepsilon\) is small at macroscopic share counts (never independently measured — docs/08 §3's standing debt). T6's scope is unchanged and now *explained*: a gravitational bias is not cluster-independent precisely because it is proportional to the counter T6 divides by.
3. **R and N — RESOLVED (docs/19 §§2–3).** N★ is a theorem on its stated domain (docs/17 §3); R is now a *corollary* of T13′ (free epochs: diagonal unimodular, invertible) and T16′ (reconfigurations: isometric, injective). B_flow demoted from postulate to derived.
4. **Born rule** — reading vs theorem.
5. **Linear reduce** — stipulated type upgrade; not derived from real counts.
6. **Monism** — unique non-idle reading, not entailment.
7. **Weight-blind selection seam** (adversarial review of T15/T16; `docs/18` §4) — O3 never sees weights outside projection: which reconfiguration occurs is selected on weight-blind structural cost, the induced map transforms weights as passengers, and interferometric device structure is external data. Entailed by D19's typing, but open whether it is final or whether selection should couple to weights (any coupling must survive N★ on fixed decompositions). **T17 (docs/19 §7) puts a standing argument on the "feature" side: the seam is exactly what makes Born statistics untamperable — closing it would reopen the cheating channel.**
8. **One currency — CLOSED by adoption (2026-08-08, owner decision).** CC′ + ST1 are charter postulates: exact strata above one Archimedean dynamical floor, with conservation typing as the derived V=0 behavior of a top-stratum charge (docs/21; TS1–TS4). Consequences applied: SM-B1 → SM-B1′ (conservation conditional on non-forced states), RM1 reads the floor. The inherited question — **are forced-violation states physically realized?** — has been developed (`docs/22-forced-violation.md`): it is a **progress-theorem question** about the conserving fragment (FV1), undecidable in general (FV2), with derived minimal-violation phenomenology and all three Sakharov counterparts identified (FV3). The progress analysis has been **performed** (`docs/23-progress-analysis.md`): duplication is charge-safe via sharing (PA0); FV states are **reachable** in the raw calculus (PA2, explicit term); progress holds on the charge-relevant λI-class (PA1, sketch); realization relocates to the initial class (PA3) — a boundary-condition question. Successor probe: **is the SB3 ground configuration charge-relevant?** CP's status remains the analogous weaker question.
9. **The geometric limit (TG2)** — new with docs/24, and the largest single debt in the framework. Everything in docs/24 §§5–7 (Einstein equation, \(G\), the area theorem's continuum form) is conditional on a coarse-graining of the SB4 order to a Lorentzian manifold with a finite share-per-area density. This is the causal-set continuum problem (dimension, local Lorentz), inherited **unsolved** from docs/15 §4. The TG layer does not weaken it; it raises the stakes, because more now rests on it.
10. **The past hypothesis** — new with docs/25. AT3/AT4 give the arrow its direction but say nothing about why the initial class was far from equilibrium. This relocates exactly as PA3 relocated forced-violation realization (docs/23 §4): a **boundary-condition question**, not a dynamical one. Two of the framework's open problems now have the same shape, and the shared probe is the same — the structure of the initial class.
11. **Is \(\varepsilon\) real?** — WM3's inertia floor was a convenience; TH8-ε turns it into a WEP-violation prediction that grows for lighter bodies. Either operationalize \(\varepsilon\) (which would also discharge docs/08 §3) or establish that the entropic bias carries the same floor, making TH8 exact.

## Priority order

0. **The forced-layer audit** (`docs/26` §7) — opened, not done. Six forced results carry the framework. The test is carrier-invariance: a result forced by O1–O4 must be provable in every faithful carrier of O1, so anything holding only for finite terms is using WM1. Candidates for promotion are listed in `docs/26` §7.2 (TH12a, AT2, TH2's ordinal form, stage-zero persistence). Settling the carrier-representation conjecture (`docs/26` §7.1 — that O1's carriers are objects of an adhesive category) would make the test mechanical.

1. ~~Construct the induced-map functor~~ **Discharged at toy level** (`docs/18`, `sim/splitter_rewrite.py`): moduli computed from routing fractions (D20); the symmetric recombiner's Hadamard pinned up to gauge by the T16b isometry filter; Mach-Zehnder fringes end to end. Remaining: lift F from unit-share granularity to full WM terms; phase tags from binding geometry (φ enrichment). (The spreading lemma is done — L6, docs/19 §6.)
2. Independent operationalization of share count, so the T6 ratio becomes a test rather than a consistency check (docs/08 §3).
3. ~~Formalize R, N in the term language~~ **Done** — R and N are theorems/corollaries (docs/19 §§2–3); remaining term-language work folds into the functor lift (item 1).
4. Structural proxy for \(\varphi_i\).
5. ~~Ontological grounding of the order axioms AD1–AD3~~ **Discharged to its floor (docs/20):** AD2 derived (M1/M2 analytic + PC from O2/SI + IND from O2/SC); AD1 and AD3 proven **independent** of O1–O4 by countermodels and sharpened to **CP** (universal comparability) and **CC** (common currency), with the RM2 Hölder/Hahn dichotomy showing exactly what each denial yields. The classical quantitative chain's stipulation content is now two bits (Q2). Residue: the status of the readings SI/SC, and contention 8.
6. Bridge targets (docs/15): Noether-style derivation of SM-B1 from SB2; the continuum-limit spectrum question (SM-B2 beyond integer counters); causal order → geometry (dimension, local Lorentz — inherited open from causal-set theory, and now the TG layer's gate, contention 9).
7. **Rewrite `docs/06-axiology.md`** against RM1/RM2/CC′/ST1 (`docs/26` §3). The framework's value theory is built and its axiology document still points at a discarded axiom set.
8. **Apply the presentation rule** (`docs/26` §8): one dimension for order, two for structure, three only past the TG2 gate. First correction it forces — `learn/counting-the-world.html` renders TH2's cut counter in 3D, which implies metric area where TH2 uses only a graph cut.
9. **TG/AT-layer priorities (docs/24–25):** (a) TG2 — any statistic on reduction-event orders yielding a finite share-per-area density is the gate on the whole layer; (b) settle \(\varepsilon\) per contention 11; (c) test whether T10's isolation argmin reproduces the quantum-extremal-surface prescription over cuts (docs/24 §8) — the framework's own selection principle and the holographic one have the same shape; (d) derive the Unruh normalization (TG3) rather than importing Bisognano–Wichmann; (e) probe the initial class jointly for contention 10 (past hypothesis) and contention 8's successor question (is the SB3 ground configuration charge-relevant?) — both are now boundary-condition questions about the same object.
10. Only then Toolbox activation or further particle/field extensions beyond the SB layer.

Done since last revision: end-to-end tree → `m_struct_from_tree` → integrator pipeline (`sim/end_to_end_T6.py`, consistency-check status); `linear_reduce` + free-epoch weight updates in `sim/` (runnable as of 2026-08-08 — a syntax error had previously made it unexecutable).
