# 03 — Quantum Sector (charter-aligned)

Authority: `docs/00-theory-charter.md`, `docs/11-theorems.md`.

**Label:** Hosted quantum layer (HQ) — linear residuals and Born reading under structural constraints. Not a derivation of QM from bare disruption counts.

---

## 0. Shared substrate

Working model cost \(C\); preferential sequentialization (A3). Classical sequential calculus: Part II of theorems. Continuum results tagged CI.

---

## 1. Hosted package

| Piece | Role | Status |
|-------|------|--------|
| **A4** `linear_reduce` / `share_weight` | Residuals \(\sum a_i E_i\), \(a_i\in\mathbb{C}\) | Hosted type upgrade |
| **D19** | Charge \(S_w\), \(M_w\) | Extended cost when A4 active |
| **B_flow** | Free-epoch maps invertible flows | Regularity |
| **T12** | Foot fixed in free epoch | WM theorem |
| **T12+, N★, R★, T13** | Support/moduli frozen; free-epoch maps diagonal-unitary under the all-states reading of N★ | HQ theorems (T13 scope contended — docs/07 contention 1) |
| **T10, T14** | Structural projection = non-unitary locus | WM + HQ |
| **D12** Born reading | \(P\propto\|a\|^2\) at projection | Reading, not theorem |
| **`phase_accumulate`** | Diagonal phase from sequential history | Enrichment for \(\varphi_i\) |

---

## 2. Structural multi-path (WM — solid)

`coherent_set`, `isolation_cost`, `maintain_cost`, `structural_decoherence` (T9–T12). Classical limit of coherence (T11).

---

## 3. Interference (HQ)

`path_recombine`, `intensity`, `visibility_amplitude` — available once A4 is active. Not derived from integer share counts.

**Open contradiction (contention 1).** Recombination is a modulus-changing operation, and N★ (via D19 + A3) forbids modulus change in free epochs — so beam-splitter-like events currently have **no category**: they are neither free-epoch maps nor structural projections. Until resolved, `path_recombine` is a readout formula, not a dynamical step, and the two readout rules in play (\(|\sum_i a_i|^2\) for interference, \(|a_i|^2\) for Born) are unreconciled. See `docs/07-roadmap.md` contention 1 and the scope note in `docs/12-RN-formalization.md`.

---

## 4. Velocity coupling

COM / path-wise sequential state on coherent sets; `com_from_amplitudes`; classical continuation after projection. Sequential part is WM+CI; weights are HQ.

---

## 5. Toolbox

`docs/09-complexification-toolbox.md` — alternatives A–F. Activate only on named failure of the hosted package.

---

## 6. Status

**Solid (WM):** multi-path coexistence, isolation-cost decoherence, classical limit of coherence.  
**Hosted (HQ):** linear weights; free-epoch *diagonal* unitarity under D19+B_flow (general unitarity contended — docs/07 contention 1); Born reading.  
**Open:** Born as theorem; \(\varphi_i\) from binding geometry; a cost locus for modulus-changing (beam-splitter) events; continuum residual families / fields.
