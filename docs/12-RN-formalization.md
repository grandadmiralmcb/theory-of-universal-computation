# 12 — Formalization of R and N (with cost derivation status)

See also `docs/13-derive-RN-from-cost.md` for the derivation attempt from structural cost.

---

## Status summary

| Principle | Bare cost \(S,B,D\) | Extended cost D19 | Residual |
|-----------|--------------------|-------------------|----------|
| Foot fixed in free epoch | **Forced** (T12) | Forced | — |
| N★ (relative moduli frozen) | Not forced | **Forced** | — |
| Support preservation | Not forced | **Forced** | — |
| R★ full invertibility | Not forced | Partial | **B_flow** (maps are invertible flows) |

**Honest line:** R★/N★ are not theorems of the original three-counter cost. N★ and support preservation become theorems once weight-sensitive disruption (D19) is part of cost under A4. Full R★ needs a mild flow/group regularity principle.

---

## D19 — Weight-sensitive disruption (adopted when A4 active)

For a weight update \(\mathbf{a}\to\mathbf{a}'\) with topological Foot fixed:

- \(S_w = 0\) if support(\(\mathbf{a}'\))=support(\(\mathbf{a}\)), else \(\ge 1\)
- \(M_w = \|\boldsymbol{\mu}'-\boldsymbol{\mu}\|_1\)

\[
C^+ = \alpha S + \beta B + \gamma D + \alpha_w S_w + \delta M_w \qquad (\alpha_w,\delta>0)
\]

**Theorem (N from cost).** In a free epoch, A3 on \(C^+\) forces \(M_w=0\) and \(S_w=0\). ☐

---

## R formal (unchanged shape; weaker origin story)

**D13–D15.** Foot; share-preserving map; linear weight step.

**R★ under D19 + B_flow.** Free-epoch maps preserve support (D19) and are invertible flows (B_flow) \(\Rightarrow\) lie in \(\mathrm{GL}(n,\mathbb{C})\) with Foot fixed; inverse is free-epoch.

**B_flow.** Free-epoch weight updates are compositions of steps from a continuous one-parameter group of Foot-preserving maps on the active weight space.

---

## N formal (now cost-derived under D19)

**D16–D17.** Relative moduli; modulus-changing step.

**N★.** Free-epoch maps preserve \(\boldsymbol{\mu}\) because any change charges \(\delta M_w>0\) and is dominated under A3 by the zero-change alternative.

---

## T13★

Free epoch + D19 + B_flow + norm gauge \(\Rightarrow\) unitary on active subspace. Structural decoherence (path drop) remains the sole non-unitary locus.

---

## Implementation

Predicates in `sim/linear_reduce.py` still enforce Foot preservation, invertibility, and frozen moduli at the API boundary — consistent with D19+B_flow even when the simulator does not evaluate \(C^+\) numerically on every proposal.
