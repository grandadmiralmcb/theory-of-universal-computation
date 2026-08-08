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
| **T12+, N★, R★, T13** | Support/moduli frozen in free epochs; free-epoch maps diagonal-unitary | HQ theorems (scope resolved — docs/17) |
| **T15, T16** | Event trichotomy; reconfiguration events induce isometries | HQ theorems (docs/17) |
| **T10, T14** | Structural projection = non-unitary locus | WM + HQ |
| **D12** Born reading | \(P\propto\|a\|^2\) at projection | Reading, not theorem |
| **`phase_accumulate`** | Diagonal phase from sequential history | Enrichment for \(\varphi_i\) |

---

## 2. Structural multi-path (WM — solid)

`coherent_set`, `isolation_cost`, `maintain_cost`, `structural_decoherence` (T9–T12). Classical limit of coherence (T11).

---

## 3. Interference (HQ)

`path_recombine`, `intensity`, `visibility_amplitude` — available once A4 is active. Not derived from integer share counts.

**Resolved (docs/17).** Recombination is a **reconfiguration event** (T15): a structural rewrite that re-partitions the coherent set's classes without dropping any. Its induced weight map is an isometry (T16b), and its cost is the ordinary weight-blind structural cost — N★ never applied across it (D19's \(M_w\) is typed on a fixed decomposition). The former "two readout rules" were one rule: screen intensity at site \(x\) is \(|(M_{\rm screen}\mathbf{a})_x|^2\) — the interference sum is a matrix element of the screen's reconfiguration isometry, followed by Born (D12) at projection. Outstanding construction (not decision): compute a concrete splitter's \(M\) from its rewrite in `sim/` (docs/17 §7).

---

## 4. Velocity coupling

COM / path-wise sequential state on coherent sets; `com_from_amplitudes`; classical continuation after projection. Sequential part is WM+CI; weights are HQ.

---

## 5. Toolbox

`docs/09-complexification-toolbox.md` — alternatives A–F. Activate only on named failure of the hosted package.

---

## 6. Status

**Solid (WM):** multi-path coexistence, isolation-cost decoherence, classical limit of coherence.  
**Hosted (HQ):** linear weights; free-epoch *diagonal* unitarity (T13) + reconfiguration isometries (T16, docs/17); non-isometry only at projection (T14′); Born reading.  
**Open:** Born as theorem; \(\varphi_i\) from binding geometry; the induced-map functor for concrete splitter rewrites (docs/17 §7); continuum residual families / fields.
