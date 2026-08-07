# 11 — Theorems and Derivations (charter-aligned)

Authority: **`docs/00-theory-charter.md`**.  
This file scopes every result to the **working model**, a **continuum idealization**, or the **hosted quantum layer**. Nothing is labeled a theorem of the bare ontology beyond what the charter allows.

**Scopes**

| Tag | Meaning |
|-----|--------|
| **WM** | Finite working model (terms, integer \(S,B,D\), discrete ticks) |
| **CI** | Continuum idealization (\(x\in\mathbb{R}\), \(\tau\to 0\), smooth \(b\) or \(V\)) |
| **HQ** | Hosted quantum layer (A4 linear weights; D19; B_flow) |
| **ONT** | Carrier-independent ontological commitment (charter §2) — not a formal theorem |

---

## Part 0 — Axioms by scope

### Ontological commitments (ONT — not formal axioms for deduction)

| ID | Statement |
|----|-----------|
| O1 | Structured evaluable information exists. |
| O2 | Sequential order is constructed locally by evaluation. |
| O3 | Dynamics prefer lower structural disruption. |
| O4 | Unprojected structure remains real. |

### Working-model axioms (WM)

| ID | Statement |
|----|-----------|
| **A1** | Structure is represented by finite terms under `app`, `abs`, `pair`/`proj`, `eq`, `reduce`, `share`. |
| **A2** | Sequential labels used by an evaluator are local constructs (not global forest parameters). |
| **A3** | Among admissible one-step residuals, select minimal structural cost \(C\) (or \(C^+\) when D19 applies). |
| **A5** | Evaluators are themselves term-representable patterns that produce sequential projections. |
| **A6** | Residuals not selected remain in the finite forest. |

### Continuum idealization postulates (CI) — not WM theorems

| ID | Statement |
|----|-----------|
| **CI1** | Sequential motion is tracked by a real parameter \(x\) and velocity \(v\). |
| **CI2** | Tick duration \(\tau\to 0\) with \(t=n\tau\) yields differential limits of discrete updates. |
| **CI3** | Bias may be given by a smooth function \(b(x)\) or potential \(V\) with \(b=V'\). |

### Hosted quantum layer (HQ)

| ID | Statement |
|----|-----------|
| **A4** | On share-linked residuals, reduction may yield \(\sum_i a_i E_i\) with \(a_i\in\mathbb{C}\) on shares. |
| **D19** | Extended cost charges support collapse \(S_w\) and relative-modulus change \(M_w\): \(C^+=C+\alpha_w S_w+\delta M_w\). |
| **B_flow** | Free-epoch weight updates are compositions of steps from a continuous one-parameter group of Foot-preserving maps on the active weight space. |
| **D12** | Born reading at structural projection: \(P(i)=|a_i|^2/\sum_j|a_j|^2\) (reading, not derived). |

---

## Part I — Structural cost (WM)

### T1 — Structural cost well-defined [WM]

**Hyp.** A1; counters \(S\) (shares broken/duplicated), \(B\) (binding change), \(D\in\{0,1\}\) (`eq` failure); \(C=\alpha S+\beta B+\gamma D\), \(\alpha,\beta,\gamma>0\).

**Claim.** For any one-step reduction on a finite term, \(S,B,D\) are uniquely determined and \(C\ge 0\).

**Proof.** Finite term graph: Share nodes by object identity; open `abs` sites countable; `eq` binary under the strategy. Non-negative combination. ☐

### T2 — Preferential selection attains minimum [WM]

**Hyp.** A3; finite non-empty set of admissible residuals.

**Claim.** There exists at least one residual of minimal \(C\) (or \(C^+\)).

**Proof.** Real-valued function on a finite non-empty set attains its minimum. ☐

---

## Part II — Classical sequential calculus (WM + CI)

### D3 — Structural inertia [WM]

\(m_{\rm struct}(E)=\alpha\,n_{\rm share}(E)+\varepsilon\), \(\varepsilon>0\). Tree-computable (`m_struct_from_tree`).

### D5 — Velocity cost [WM + CI1]

\(C(\delta v)=\tfrac12 m(\delta v)^2 + b\,\delta v\) with \(m=m_{\rm struct}\).

### T3 — Optimal velocity update [WM + CI1]

**Hyp.** D3, D5; \(m>0\).

**Claim.** \(\arg\min_{\delta v} C(\delta v) = -b/m\).

**Proof.** Strictly convex quadratic in \(\delta v\); critical point \(\delta v^*=-b/m\). ☐

### T4 — Discrete sequential step [WM + CI1]

**Hyp.** T3; tick \(\tau>0\).

**Claim.** Preferential sequentialization on sequential labels implements
\[
v \leftarrow v + \delta v^*\tau, \qquad x \leftarrow x + v\tau
\]
(up to integrator convention).

**Proof.** Integrate preferred rate over \(\tau\); position advance is the sequential-label update under maintained velocity. ☐

### T5 — Continuum limit under constant bias [WM + CI1 + CI2]

**Hyp.** T4; \(b\) constant; continuum idealization CI2.

**Claim.** In the limit, \(\dot v = -b/m\), \(\dot x = v\), hence \(\ddot x = -b/m\).

**Proof.** Difference quotients from T4 converge under CI2 to the stated ODEs.  
**Scope note:** This is a theorem *of the idealization*, not a WM identity. ☐

### T6 — Inverse share-count acceleration ratio [WM + CI]

**Hyp.** T5; two finite clusters with share counts \(n_A,n_B\); same constant \(b\); D3.

**Claim.** \(a_A/a_B = m_B/m_A = (\alpha n_B+\varepsilon)/(\alpha n_A+\varepsilon)\).

**Proof.** From T5, \(a=-b/m\). Ratio of accelerations is inverse ratio of inertias. ☐

**Executable:** `sim/end_to_end_T6.py` (tree → \(m\) → measured ratio; no knobs).

### T7 — Projectile kinematics [CI under T5]

**Hyp.** T5; \(x(0)=h\), \(v(0)=v_0\); \(g_{\rm eff}=b/m\).

**Claim.** Standard constant-acceleration landing formula with that \(g_{\rm eff}\).

**Proof.** Integrate ODEs. ☐

### T8 — Position-dependent bias [CI under T5 + CI3]

**Hyp.** \(b(x)=V'(x)\).

**Claim.** \(m\ddot x = -V'(x)\).

**Proof.** Local application of T3–T5 with CI3. ☐

---

## Part III — Multi-path structure and decoherence (WM)

### D6–D8 — Coherent set, isolation cost, maintain cost [WM]

As in prior definitions: isolation cost from cross-member Share identity; maintain cost from cross links + \(N_{\rm env}\).

### T9 — Isolation/maintain well-defined [WM]

**Hyp.** A1; finite terms.

**Claim.** \(C_{\rm isolate}\) and \(C_{\rm maintain}\) are unique non-negative reals for finite coherent-set candidates.

**Proof.** Finite Share intersections and bindings. ☐

### T10 — Structural decoherence criterion [WM]

**Hyp.** A3, T2, T9.

**Claim.** If \(C_{\rm isolate}(E_i)\le C_{\rm maintain}\), preferential selection isolates \(E_i\) (path leaves the coherent set).

**Proof.** Binary choice maintain vs isolate; A3 selects the cheaper (or equal) alternative. ☐

### T11 — Classical limit of coherence [WM + sequential calculus]

**Hyp.** T10; \(N_{\rm env}\) rises until only one path remains isolable-expensive.

**Claim.** Coherent set becomes a singleton; subsequent dynamics are preferential sequentialization on that path (Part II).

**Proof.** Iterate T10; apply T2–T4 to the survivor. ☐

### T12 — Free epoch is share-topology-preserving [WM]

**Hyp.** Free epoch = isolation costs still exceed maintain for all active paths; A3, T10.

**Claim.** Free-epoch steps do not break defining shares of the coherent set (Foot fixed).

**Proof.** Breaking such a share is isolation; forbidden by T10 while free epoch holds. ☐

**Note:** T12 is the *only* fragment of former “R” forced by bare \(S,B,D\) cost. Invertibility of weight maps is not included. (See Part IV.)

---

## Part IV — Hosted quantum layer (HQ)

Results below **depend on A4, D19, B_flow** as stated. They are not theorems of A1–A3 + bare \(C\) alone (`docs/13-derive-RN-from-cost.md`).

### T12+ — Support preservation in free epochs [HQ: D19]

**Hyp.** A3, D19, free epoch, A4.

**Claim.** Free-epoch maps do not collapse weight support (\(S_w=0\)).

**Proof.** Support collapse charges \(\alpha_w S_w>0\). Zero-support-change alternative has lower \(C^+\) when topology is fixed; A3 selects it. ☐

### N★ — Relative moduli frozen in free epochs [HQ: D19]

**Hyp.** A3, D19, free epoch.

**Claim.** Free-epoch maps preserve relative moduli \(\boldsymbol{\mu}\) (\(M_w=0\)).

**Proof.** Relative-modulus change charges \(\delta M_w>0\); A3 prefers \(M_w=0\). ☐

### R★ — Invertibility of free-epoch weight maps [HQ: D19 + B_flow]

**Hyp.** T12, T12+, B_flow, A4.

**Claim.** Free-epoch weight maps lie in \(\mathrm{GL}(n,\mathbb{C})\) on the active subspace; inverse is free-epoch.

**Proof.** B_flow: maps are compositions of group elements \(\Rightarrow\) invertible, inverse in the group. T12: Foot fixed. T12+: support preserved. ☐

**Bare-cost status:** Not a theorem of \(S,B,D\) alone (weights invisible to those counters).

### T13 — Unitarity on the active subspace [HQ]

**Hyp.** R★, N★; norm gauge (Born reading is ray-dependent).

**Claim.** Free-epoch weight evolution is unitary on the span of active path weights.

**Proof.** Invertible linear maps preserving relative moduli, after fixing \(\|\mathbf{a}\|_2\), are unitary on that finite-dimensional space. ☐

### T14 — Sole non-unitary locus [HQ]

**Hyp.** T13, T10.

**Claim.** Within the hosted layer, weight dynamics are unitary in free epochs and non-unitary precisely at structural projection (path drop).

**Proof.** T13 in free epochs; T10 deletes coordinates — projection, not unitary. No other non-unitary mechanism in the layer. ☐

### Born reading [HQ — not a theorem]

**D12.** At structural projection, \(P(i)=|a_i|^2/\sum_j|a_j|^2\).

**Status.** Stipulated reading of weights at the irreversible event. Not derived from A3 or D19.

---

## Part V — Dependency graph (scoped)

```
ONT O1–O4          (commitments, not deduction base)

WM:  A1–A3 → T1 → T2
WM+CI: T2, D3, D5 → T3 → T4 →[CI2] T5 → T6, T7, T8[CI3]
WM:  A1,A3 → T9 → T10 → T11, T12

HQ:  A4, D19, A3, T12 → T12+, N★
HQ:  T12+, B_flow → R★ →[N★] T13 →[T10] T14
HQ:  D12 (Born reading; non-derived)
```

---

## Part VI — Explicit non-theorems (corrected)

| Former overclaim | Correct status |
|------------------|----------------|
| Finite trees are the ontology | Working model only (charter) |
| \(\ddot x=-b/m\) is a pure WM theorem | WM discrete steps + CI idealization |
| R★/N★ from bare \(S,B,D\) | False; N★/support from D19; R★ needs B_flow |
| Unitarity from structural projection alone | Needs HQ package (A4, D19, B_flow) |
| Born rule derived | Reading D12 |
| Amplitudes from share counts | Hosted A4 |
| Monism / consciousness theorems | Preferred reading / open |

---

## Part VII — Executable links

| Result | Artifact |
|--------|----------|
| T1, T9, D3 | `sim/expr_tree.py` |
| T6 end-to-end | `sim/end_to_end_T6.py` |
| T3–T5, T8 toys | `sim/toy_simulator.py` |
| T12+, N★, T13-style free epoch, T14 projection | `sim/linear_reduce.py` |

---

## Part VIII — Status

**Proved in WM:** T1, T2, T9, T10, T11, T12.  
**Proved in WM+CI:** T3, T4, T5, T6, T7, T8 (idealization tagged).  
**Proved in HQ under A4+D19+B_flow:** T12+, N★, R★, T13, T14.  
**Not proved:** Born, \(\varphi_i\) generator, sequential \(x\) from syntax alone, continuum carrier without CI postulates, monism.
