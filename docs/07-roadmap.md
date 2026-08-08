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

## Current Contentions

1. **N★ vs interference — RESOLVED by derivation (`docs/17-forced-resolution-contention-1.md`).** The fork dissolved: the event trichotomy (T15) is a theorem of case exhaustion; N★ never applied across reconfigurations (D19's \(M_w\) is typed on a fixed decomposition — its own stated hypothesis); reconfiguration maps are injective (T16a, forced) and isometric (T16b, forced given the D20 explication). Horn (b) was barred as unforced revision of an unrefuted commitment; the Toolbox-A license lapsed with the named failure discharged. Survey of the option space preserved in `docs/16-contention-1-review.md`. Residue is construction, not choice: the induced-map functor / splitter rewrite (docs/17 §7).
2. **Gravitational bias coupling** — free-fall universality forces \(b_{\rm grav} = m_{\rm struct}\,g\) (docs/02 §6); not derived, and it removes the T6 ratio for gravity. T6's scope is cluster-independent (applied-force) bias only.
3. **R and N — RESOLVED (docs/19 §§2–3).** N★ is a theorem on its stated domain (docs/17 §3); R is now a *corollary* of T13′ (free epochs: diagonal unimodular, invertible) and T16′ (reconfigurations: isometric, injective). B_flow demoted from postulate to derived.
4. **Born rule** — reading vs theorem.
5. **Linear reduce** — stipulated type upgrade; not derived from real counts.
6. **Monism** — unique non-idle reading, not entailment.
7. **Weight-blind selection seam** (adversarial review of T15/T16; `docs/18` §4) — O3 never sees weights outside projection: which reconfiguration occurs is selected on weight-blind structural cost, the induced map transforms weights as passengers, and interferometric device structure is external data. Entailed by D19's typing, but open whether it is final or whether selection should couple to weights (any coupling must survive N★ on fixed decompositions). **T17 (docs/19 §7) puts a standing argument on the "feature" side: the seam is exactly what makes Born statistics untamperable — closing it would reopen the cheating channel.**

## Priority order

1. ~~Construct the induced-map functor~~ **Discharged at toy level** (`docs/18`, `sim/splitter_rewrite.py`): moduli computed from routing fractions (D20); the symmetric recombiner's Hadamard pinned up to gauge by the T16b isometry filter; Mach-Zehnder fringes end to end. Remaining: lift F from unit-share granularity to full WM terms; phase tags from binding geometry (φ enrichment). (The spreading lemma is done — L6, docs/19 §6.)
2. Independent operationalization of share count, so the T6 ratio becomes a test rather than a consistency check (docs/08 §3).
3. ~~Formalize R, N in the term language~~ **Done** — R and N are theorems/corollaries (docs/19 §§2–3); remaining term-language work folds into the functor lift (item 1).
4. Structural proxy for \(\varphi_i\).
5. Ontological grounding of the order axioms AD1–AD3 (docs/19 §5): argue or refute totality, disjoint additivity, and Archimedeanness of disruption comparison from the nature of O3's preference — the last stipulations beneath the classical chain.
6. Bridge targets (docs/15): Noether-style derivation of SM-B1 from SB2; the continuum-limit spectrum question (SM-B2 beyond integer counters); causal order → geometry (dimension, local Lorentz — inherited open from causal-set theory).
7. Only then Toolbox activation or further particle/field extensions beyond the SB layer.

Done since last revision: end-to-end tree → `m_struct_from_tree` → integrator pipeline (`sim/end_to_end_T6.py`, consistency-check status); `linear_reduce` + free-epoch weight updates in `sim/` (runnable as of 2026-08-08 — a syntax error had previously made it unexecutable).
