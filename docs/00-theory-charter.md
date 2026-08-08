# 00 — Theory Charter (derivation-first)

**Rule:** Claim only what is forced by stated ontological minima or by explicitly numbered postulates. Everything else is working model, idealization, or open.

Companion derivation spine: `docs/14-derivation-from-ontology.md`.

---

## 1. Ontological minima (O1–O4)

These are the only ontological commitments. They are **assumptions**, not theorems.

| ID | Statement |
|----|-----------|
| **O1** | There exists structured, evaluable information: patterns that admit composition, sharing of substructure, and reduction under strategies. |
| **O2** | Sequential order is not a global parameter of the structure; it is constructed locally by evaluators through successive reduction. |
| **O3** | When multiple admissible reductions are available, dynamics prefer those of lower structural disruption (disruption = change to sharing, binding, or observational identity). |
| **O4** | Structure not selected by a given sequentialization remains real; non-selection is not non-existence. |

**Preferred reading (not forced):** informational monism — unique non-idle reading of O1–O4. Not used as a premise in derivations.

---

## 2. What O1–O4 force (and what they do not)

### Forced (see `docs/14-derivation-from-ontology.md`)

- **F1** Local sequential trajectories exist as finite or transfinite chains of reductions (from O2).
- **F2** If the set of admissible one-step residuals is finite and non-empty and disruption is a total preorder, a minimal-disruption residual exists and is selectable (from O3).
- **F3** Unselected residuals persist as real structure alongside the selected trajectory (from O4).
- **F4** If co-dependence is realized by shared substructure, then breaking that sharing is a form of disruption; maintaining it is another; O3 compares them when both are admissible (from O1+O3).
- **F5** When breaking co-dependence is ranked no more disruptive than maintaining it, selection may isolate a residual (structural projection event) (from F4+O3).

### Not forced by O1–O4 alone

- Finite expression trees as the only carrier
- Integer cost formula \(C=\alpha S+\beta B+\gamma D\)
- Real sequential parameter \(x\), velocity, continuum ODEs
- \(m_{\rm struct} \propto\) share count (definitional in WM, not forced)
- Complex weights, linear residuals, unitarity, Born rule
- Consciousness, monism as theorem, spacetime, fields

---

## 3. Controlled extensions (explicit, not smuggled)

Each extension is a **postulate**, used only when stated in a theorem’s hypotheses.

| ID | Postulate | Role |
|----|-----------|------|
| **WM1** | Carrier is finite terms under `app`,`abs`,`pair`/`proj`,`eq`,`reduce`,`share` | Working model |
| **WM2** | Disruption measured by \(C=\alpha S+\beta B+\gamma D\) | Quantitative WM cost |
| **CI1** | Sequential labels include real \((x,v)\) | Continuum kinematics |
| **CI2** | Continuum limit of discrete ticks | ODE idealization |
| **CI3** | Smooth bias / potential \(b(x)\), \(V\) | Force law idealization |
| **WM3** | \(m_{\rm struct}=\alpha_m n_{\rm share}+\varepsilon\) (\(\alpha_m\) distinct from the WM2 counter weight \(\alpha\)) | Inertia proxy in WM |
| **WM4** | Environmental monitoring is charged to the maintain ledger only: environment-crossing shares raise \(C_{\rm maintain}\), not \(C_{\rm isolate}\) | Decoherence asymmetry (drives T11) |
| **CI4** | Sequential-state changes are charged the per-tick functional \(C_\tau(\delta v)=m_{\rm struct}(\delta v)^2/2\tau+b_{\rm struct}\,\delta v\); not an instance of WM2 (it is signed relative to the null change; the additive gauge \(b^2\tau/2m\) restores non-negativity without changing selection) | Velocity-form dynamics |
| **A4** | Share-linked residuals may form \(\sum a_i E_i\), \(a_i\in\mathbb{C}\) | Hosted linear layer |
| **D19** | Extended cost charges support collapse and relative-modulus change | Weight-sensitive cost |
| **B_flow** | Free-epoch weight maps are invertible flows | Regularity for R |
| **D12** | Born reading \(P\propto\|a\|^2\) at projection | Probability reading |

No theorem may treat these as forced by O1–O4.

---

## 4. Layers

1. **Ontology** — O1–O4 only.
2. **Forced corollaries** — F1–F5.
3. **Working model (WM)** — WM1–WM3; finite trees; executable tests.
4. **Continuum idealization (CI)** — CI1–CI4 on top of WM sequential calculus.
5. **Hosted quantum (HQ)** — A4, D19, B_flow, D12; structural projection (F5) as irreversible locus.

---

## 5. Authority

`docs/14-derivation-from-ontology.md` is the derivation spine.  
`docs/11-theorems.md` must list hypotheses including every postulate used.  
Older text that claims amplitudes, unitarity, continuum Newton, or finite trees as forced by ontology alone is **void**.
