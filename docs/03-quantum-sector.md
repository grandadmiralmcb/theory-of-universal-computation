# 03 — Quantum Sector

Structural multi-path coherence, isolation-cost decoherence, **linear reduce on share-weighted residuals**, **unitarity constraints from structural projection**, velocity coupling, and a toolbox of alternative complexifications.

Every derivation names the operation performed.

---

## 0. Shared substrate

\[
C = \alpha S + \beta B + \gamma D \qquad (\text{real, non-negative})
\]

Preferential low-disruption sequentialization governs structural selection. Classical sequential calculus: `docs/02-dynamics.md`. Unitarity derivation: `docs/10-unitarity-from-projection.md`.

---

## 1. Active direction — linear `reduce` + weighted `share`

### 1.1–1.3 Weighted share, linear reduce, coherent sets

**`share_weight`:** `share` carries \(a\in\mathbb{C}\) (or U(1)).

**`linear_reduce`:** \(\sum_i a_i E_i\) on share-linked residuals.

**`coherent_set` / `isolation_cost` / `maintain_cost` / `structural_decoherence`:** real structural counts; drop path when isolation ≤ maintain.

### 1.4 Interference

**`path_recombine`**, **`intensity`**, **`visibility_amplitude`:** as before.

### 1.5 Phase accumulation

**`phase_accumulate`:** \(a_i \leftarrow a_i e^{-i\varphi_i\tau}\) with \(\varphi_i\) from sequential / binding context.

### 1.6 Born extraction

**`born_extract`:** \(P(i)=|a_i|^2/\sum|a_j|^2\) at structural selection (reading, not derived from real cost alone).

### 1.7 Classical limit of coherence

Environmental share density → structural decoherence → singleton → classical sequential calculus.

---

## 2. Unitarity from structural projection (summary)

Full derivation: `docs/10-unitarity-from-projection.md`.

**Free epoch:** isolation > maintain for all paths in \(\mathcal{C}\); no share-breaking.

| Step | Operation / principle | Result |
|------|----------------------|--------|
| 1 | `share_preserve` | Free evolution does not act by discarding paths |
| 2 | Assumption R (reversibility of share-preserving reduce) | \(U_\tau\) invertible on active weights |
| 3 | Principle N (no cost-free relative-modulus change) | Relative \(|a_i|\) frozen; norm fixable |
| 4 | Invertible + norm-preserving linear maps | **Unitary** on active subspace |
| 5 | `structural_decoherence` | Non-unitary projection when isolation fails |

**Forced:** free evolution is share-preserving; unitarity fails exactly at structural projection.  
**Semi-forced:** invertibility (R), frozen relative moduli (N).  
**Still open:** concrete generator for \(\varphi_i\); Born rule as theorem.

Thus unitary free evolution and non-unitary selection are two regimes of one dynamics: share-preserving linear reduce vs isolation-cost projection — the same bipartition as textbook QM, with selection identified with structural decoherence.

---

## 3. Velocity coupling

**`attach_sequential_state`** (COM or path-wise), **`preferential_select`**, **`sequential_tick`**, **`path_recombine_with_velocity`**, **`com_from_amplitudes`:** as before. Weights evolve unitarily in free epochs; sequential parameters evolve under real structural cost.

---

## 4. Thought toolbox

See `docs/09-complexification-toolbox.md`. Entries A–F retained; do not activate without a named failure of the active direction.

---

## 5. Named operation register

| Operation | Role |
|-----------|------|
| `share_weight` | complex weight on `share` |
| `linear_reduce` | weighted sum of residuals |
| `share_preserve` | free-epoch constraint (no share break) |
| `coherent_set` / `isolation_cost` / `maintain_cost` | structural multi-path |
| `structural_decoherence` | non-unitary projection |
| `path_recombine` / `intensity` / `visibility_amplitude` | interference |
| `phase_accumulate` | unitary phase motion (diagonal case) |
| `born_extract` | \(|a|^2\) reading at selection |
| `attach_sequential_state` / `sequential_tick` | sequential dynamics |
| `classical_limit_of_coherence` | decoherence → classical trajectory |

---

## 6. Status

**Closed / advanced**
- Structural multi-path + decoherence.
- Linear reduce + weighted share (active).
- Unitarity as unique linear weight dynamics compatible with share preservation, reversibility of non-destructive reduce, and cost as sole selection currency (semi-forced principles R, N).
- Non-unitary locus = structural projection only.

**Open**
- Executable `linear_reduce` + free-epoch unitary evolution in `sim/`.
- Formalize R and N inside the term language (eliminate semi-forced status).
- Generator for \(\varphi_i\); Born as theorem if possible.
- Multi-cluster forces, fields, spectra.
