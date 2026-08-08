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

**D13 (Foot).** For a coherent set with active members \(\{E_i\}\), the Foot is the set of share identities carried by active members: \(\mathrm{Foot} = \bigcup_i \mathrm{shares}(E_i)\).

**D14 (Share-preserving map).** A weight update whose Foot before and after are equal as sets.

**D15 (Linear weight step).** An update \(\mathbf{a} \mapsto M\mathbf{a}\) with \(M\) linear on the active weight space, leaving path identities and the Foot untouched.

**R★ under D19 + B_flow.** Free-epoch maps preserve support (D19) and are invertible flows (B_flow) \(\Rightarrow\) lie in \(\mathrm{GL}(n,\mathbb{C})\) with Foot fixed; inverse is free-epoch.

**B_flow.** Free-epoch weight updates are compositions of steps from a continuous one-parameter group of Foot-preserving maps on the active weight space.

---

## N formal (now cost-derived under D19)

**D16 (Relative moduli).** \(\mu_i = |a_i| / \lVert\mathbf{a}\rVert_2\).

**D17 (Modulus-changing step).** A step with \(\lVert\boldsymbol{\mu}' - \boldsymbol{\mu}\rVert_1 > 0\).

**N★.** Free-epoch maps preserve \(\boldsymbol{\mu}\) because any change charges \(\delta M_w>0\) and is dominated under A3 by the zero-change alternative.

**Scope (adversarial review, 2026-08-08).** The argument proves more than intended: *any* modulus-changing free-epoch map is dominated by the zero-change alternative — including every non-diagonal unitary (a Hadamard maximally changes \(\boldsymbol{\mu}\)). Read across all states, N★ therefore confines free epochs to diagonal phase drift, and T13's "unitary" is the diagonal subgroup; read along the realized trajectory only, invertibility + norm gauge do **not** imply unitarity (many non-unitary invertible maps preserve one vector's moduli and norm). Beam-splitter-like recombination has no category in the present formalism — neither free-epoch map nor projection. This is contention 1 in `docs/07-roadmap.md`.

---

## T13★

Free epoch + D19 + B_flow + norm gauge \(\Rightarrow\) **diagonal** unitary on the active subspace under the all-states reading of N★ (see scope note above); the general-unitary form is contended. Structural decoherence (path drop) remains the sole non-unitary locus relative to the restated T13.

---

## Implementation

Predicates in `sim/linear_reduce.py` still enforce Foot preservation, invertibility, and frozen moduli at the API boundary — consistent with D19+B_flow even when the simulator does not evaluate \(C^+\) numerically on every proposal.

As of 2026-08-08 the file actually runs (a syntax error had made every earlier "executable" claim for it unverified). The general-matrix step now rejects norm-changing proposals outright and warns on relative-modulus change instead of silently permitting it; the demo exercises a Hadamard to display the contention.
