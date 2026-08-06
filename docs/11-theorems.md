# 11 — Theorems from Axioms

Formal chain from stated axioms to the results the theory relies on.

See also: `docs/12-RN-formalization.md` (R★, N★), `sim/end_to_end_T6.py`, `sim/linear_reduce.py`.

**Convention.** Axioms A1–A7; definitions D1–D18; theorems T1–T14, R★, N★, T13★.

---

## Part 0 — Axioms and core definitions

### Axioms

| ID | Statement |
|----|-----------|
| **A1** | Operative substrate: structured evaluable information under `app`, `abs`, `pair`/`proj`, `eq`, `reduce`, `share`. |
| **A2** | Sequential order is a local construction of evaluators. |
| **A3** | Dynamics favor minimal structural disruption (`preferential_select`). |
| **A4** | On share-linked residuals, `linear_reduce` yields \(\sum_i a_i E_i\); weights on `share`. |
| **A5** | Local evaluators are informational patterns generating sequential projections. |
| **A6** | Unselected / not-yet-projected residuals remain real forest structure. |
| **A7** | Matter/energy are dual sequential presentations of informational excitations. |

### Definitions (selected)

**D1–D2.** Structural counters \(S,B,D\); cost \(C=\alpha S+\beta B+\gamma D\).

**D3.** \(m_{\rm struct}(E)=\alpha\,n_{\rm share}(E)+\varepsilon\).

**D5.** Velocity cost \(C(\delta v)=\tfrac12 m(\delta v)^2 + b\,\delta v\).

**D6–D9.** Coherent set, isolation/maintain costs, free epoch.

**D10–D12.** Share weight, linear residual, Born reading.

**D13–D18.** Share footprint, share-preserving map, linear weight step, relative moduli, modulus-change charge — see `docs/12-RN-formalization.md`.

---

## Part I — Classical sequential dynamics

### T1 — Structural cost well-defined
**Hyp.** A1, D1–D2. **Claim.** \(S,B,D\) unique; \(C\ge 0\). **Proof.** Share identity, binding count, binary `eq`; non-negative combination. ☐

### T2 — Preferential selection
**Hyp.** A3, finite admissible residuals. **Claim.** Argmin of \(C\) attained. **Proof.** Finite non-empty set. ☐

### T3 — Optimal velocity update
**Hyp.** D3–D5, \(m>0\). **Claim.** \(\delta v^*=-b/m\). **Proof.** Strictly convex quadratic; critical point is minimum. ☐

### T4 — Discrete sequential dynamics
**Hyp.** T3, tick \(\tau>0\). **Claim.** \(v\leftarrow v+\delta v^*\tau\), \(x\leftarrow x+v\tau\). **Proof.** Integrate preferred rate; sequential advance definition. ☐

### T5 — Continuum limit (constant bias)
**Hyp.** T4, \(b\) constant, \(\tau\to 0\). **Claim.** \(\ddot x=-b/m\). **Proof.** Difference quotients → ODEs. ☐

### T6 — Inverse share-count acceleration ratio
**Hyp.** T5; clusters with share counts \(n_A,n_B\); same \(b\); D3. **Claim.** \(a_A/a_B=m_B/m_A\). **Proof.** \(a=-b/m\); ratio of inertias. ☐

**Executable:** `sim/end_to_end_T6.py` — tree → `m_struct_from_tree` → integrator → measured ratio (no knobs).

### T7 — Projectile under constant bias
**Hyp.** T5, initial \((h,v_0)\). **Claim.** Standard kinematic landing formula with \(g_{\rm eff}=b/m\). **Proof.** Integrate. ☐

### T8 — Position-dependent bias
**Hyp.** T5 with \(b(x)=V'(x)\). **Claim.** \(m\ddot x=-V'(x)\). **Proof.** Local application of T3–T5. ☐

---

## Part II — Multi-path and decoherence

### T9 — Isolation/maintain well-defined from trees
**Hyp.** A1, D7–D8. **Claim.** Unique non-negative costs. **Proof.** Finite share intersections. ☐

### T10 — Structural decoherence criterion
**Hyp.** A3, T2, T9, D6. **Claim.** Isolation when \(C_{\rm isolate}\le C_{\rm maintain}\). **Proof.** Preferential select on the two alternatives. ☐

### T11 — Classical limit of coherence
**Hyp.** T10; rising \(N_{\rm env}\). **Claim.** Singleton → Part I dynamics. **Proof.** Iterate T10. ☐

---

## Part III — Linear weights and unitarity

### T12 — Free evolution is share-preserving
**Hyp.** D9, A3, T10. **Claim.** Free-epoch updates do not break defining shares. **Proof.** Isolation forbidden while isolation cost exceeds maintain. ☐

### R★ — Reversibility as typing constraint
**Hyp.** D13–D15. **Claim.** Free-epoch weight maps are invertible share-preserving linear maps; inverse is free-epoch. **Proof.** \(M\in\mathrm{GL}(n,\mathbb{C})\); Foot fixed. ☐

### N★ — Relative moduli frozen in free epochs
**Hyp.** D16–D18, free epoch. **Claim.** Free-epoch maps preserve \(\boldsymbol{\mu}\). **Proof.** Modulus change requires \(C>0\); free epoch forbids positive structural charge for selection-relevant change. ☐

### T13★ — Unitarity on active subspace
**Hyp.** T12, A4, R★, N★. **Claim.** Free-epoch weight evolution is unitary on active span. **Proof.** Invertible + relative-moduli frozen + norm gauge → unitary. ☐

**Executable:** `sim/linear_reduce.py` enforces R/N predicates on free-epoch steps.

### T14 — Sole non-unitary locus
**Hyp.** T13★, T10. **Claim.** Non-unitary weight maps occur only at structural projection. **Proof.** Free epochs unitary; decoherence deletes coordinates. ☐

---

## Part IV — Dependency graph

```
A1–A3 → T1 → T2 → T3 → T4 → T5 → T6, T7, T8
A1–A3 → T9 → T10 → T11, T12
T12 + A4 + R★ + N★ → T13★ → T14
```

---

## Part V — Remaining gaps

| Desired | Blocker |
|---------|---------|
| Born rule as theorem | Still D12 reading |
| Generator of \(\varphi_i\) | No structural Hamiltonian yet |
| Sequential parameter from syntax | Still evaluator convention |
| Multi-body / fields / spectra | Outside current axioms |

---

## Part VI — Status

**Proved:** T1–T12, R★, N★, T13★, T14.

**Executable:** T6 end-to-end (`sim/end_to_end_T6.py`); free-epoch unitary + projection (`sim/linear_reduce.py`); tree costs (`sim/expr_tree.py`).
