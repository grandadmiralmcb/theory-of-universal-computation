# 07 — Roadmap, Open Questions & Contentions

## Theorem status (see `docs/11-theorems.md`)

| ID | Result | Status |
|----|--------|--------|
| T1–T2 | Cost well-defined; preferential select | Proved [WM1, WM2] |
| T3–T8 | Classical sequential calculus, Newton, ratio, projectile, potential | Proved [WM3, CI1–CI4] |
| T9–T11 | Isolation/maintain, decoherence, classical limit of coherence | Proved [WM1, WM2; T11 also WM4] |
| T12 | Free epoch share-preserving | Proved [WM] |
| T13 | Diagonal-unitary free epoch under all-states N★ | Contended (see contention 1) |
| T14 | Non-unitary locus = structural projection | Relative to T13 as restated |
| SM-B1 | Label conservation by typing | Proved [WM1, SB1, SB1-typing] |
| SM-B2 | Discrete WM spectrum per label class | Proved [WM1–3, SB1, SB3] (counter artifact; continuum open) |
| SM-B3 | Causal partial order of reduction events | Proved [WM1, F1] |

## Current Contentions

1. **N★ vs interference** — the D19+A3 argument forbids *all* modulus-changing free-epoch maps, including non-diagonal unitaries; beam-splitter-like recombination therefore has no category (neither free-epoch map nor projection), and the two readout rules (\(|\sum a_i|^2\) interference vs \(|a_i|^2\) Born) are unreconciled. Fork: (a) free epochs are phases-only and modulus-changing events get their own cost story, or (b) N★ is weakened and T13 redone. See docs/12 scope note, docs/03 §3. **Full fork review with horn taxonomy, decision criteria, and a recommendation: `docs/16-contention-1-review.md`** (recommends (a) with the Toolbox-A path integral as licensed fallback; horn (b) assessed as dominated).
2. **Gravitational bias coupling** — free-fall universality forces \(b_{\rm grav} = m_{\rm struct}\,g\) (docs/02 §6); not derived, and it removes the T6 ratio for gravity. T6's scope is cluster-independent (applied-force) bias only.
3. **R and N** — elevate to theorems or mark permanent semi-forced principles.
4. **Born rule** — reading vs theorem.
5. **Linear reduce** — stipulated type upgrade; not derived from real counts.
6. **Monism** — unique non-idle reading, not entailment.

## Priority order

1. Resolve contention 1: a cost locus for modulus-changing (beam-splitter) events, or a weakened N★ with T13 redone.
2. Independent operationalization of share count, so the T6 ratio becomes a test rather than a consistency check (docs/08 §3).
3. Formalize R, N in the term language.
4. Structural proxy for \(\varphi_i\).
5. Bridge targets (docs/15): Noether-style derivation of SM-B1 from SB2; the continuum-limit spectrum question (SM-B2 beyond integer counters); causal order → geometry (dimension, local Lorentz — inherited open from causal-set theory).
6. Only then Toolbox activation or further particle/field extensions beyond the SB layer.

Done since last revision: end-to-end tree → `m_struct_from_tree` → integrator pipeline (`sim/end_to_end_T6.py`, consistency-check status); `linear_reduce` + free-epoch weight updates in `sim/` (runnable as of 2026-08-08 — a syntax error had previously made it unexecutable).
