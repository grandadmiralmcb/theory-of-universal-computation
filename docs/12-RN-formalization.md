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

**B_flow.** Free-epoch weight updates are compositions of steps from a continuous one-parameter group of Foot-preserving maps on the active weight space. **[Demoted 2026-08-08: no longer a postulate.** T13′ (docs/19 §2) obtains diagonal-unimodular free-epoch maps — hence invertibility — from A4 + D19 + norm gauge + Q1 alone; B_flow's content is now a consequence, retained here for the historical record.**]**

---

## N formal (now cost-derived under D19)

**D16 (Relative moduli).** \(\mu_i = |a_i| / \lVert\mathbf{a}\rVert_2\).

**D17 (Modulus-changing step).** A step with \(\lVert\boldsymbol{\mu}' - \boldsymbol{\mu}\rVert_1 > 0\).

**D20 (Weight as measure of persisting structure).** \(|a_i|^2\) quantifies the persisting residual structure of class \(i\); D12's Born reading at projection is its selection-time special case. (Originally an explication of D12 × O4 — docs/17 §4; **upgraded to a named postulate**, charter §3, per adversarial review: hypothesis lists cite it at the same grade as A4. It supplies meaning, not probability — Born remains the non-derived D12.)

**N★.** Free-epoch maps preserve \(\boldsymbol{\mu}\) because any change charges \(\delta M_w>0\) and is dominated under A3 by the zero-change alternative.

**Scope (resolved 2026-08-08 — `docs/17-forced-resolution-contention-1.md`).** The adversarial review initially read this argument as forbidding all modulus-changing maps, leaving beam splitters with no category (former contention 1). The resolution is a *reading of this section's own hypothesis*: the clause above is stated **"with topological Foot fixed,"** and \(M_w, S_w\) are typed on a common class index set — so the comparison N★ invokes is undefined across a decomposition change. By the event trichotomy (T15): free-epoch maps (fixed decomposition) are diagonal phase drift, exactly as N★ says; **reconfigurations** (decomposition changes, nothing dropped) are structural events, weight-blind in cost (WM2), whose induced maps are injective (T16a) and isometric given D20 (T16b); projections drop weight. N★ is true on its stated domain and constrains nothing else.

---

## T13★

Free epoch + D19 + B_flow + norm gauge \(\Rightarrow\) **diagonal** unitary on the active subspace under the all-states reading of N★ (see scope note above); the general-unitary form is contended. Structural decoherence (path drop) remains the sole non-unitary locus relative to the restated T13.

---

## Implementation

Predicates in `sim/linear_reduce.py` still enforce Foot preservation, invertibility, and frozen moduli at the API boundary — consistent with D19+B_flow even when the simulator does not evaluate \(C^+\) numerically on every proposal.

As of 2026-08-08 the file actually runs (a syntax error had made every earlier "executable" claim for it unverified). The general-matrix step now rejects norm-changing proposals outright and warns on relative-modulus change instead of silently permitting it; the demo exercises a Hadamard to display the contention.
