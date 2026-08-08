# 13 — Derive R★ and N★ from Cost (charter-aligned)

Authority: `docs/00-theory-charter.md`.

---

## Result (unchanged, restated)

**Bare cost** \(C=\alpha S+\beta B+\gamma D\) forces only **Foot preservation** in free epochs (T12). Weights are invisible to \(S,B,D\).

**Extended cost D19** (when A4 active):
\[
C^+ = C + \alpha_w S_w + \delta M_w
\]
forces **support preservation** and **N★** (relative moduli frozen) by A3.

**Full R★** still needs **B_flow** (free-epoch maps are invertible flows).

Pure derivation of R★/N★ from the original three counters is **impossible**. That is a fixed negative result, not an open gap.

**Companion overshoot (fixed, 2026-08-08).** The same D19+A3 argument that yields N★ also forbids every modulus-changing free-epoch map — including the non-diagonal unitaries interference requires. The derivation is sound; its conclusion is narrower than "unitarity": diagonal phase drift. See the scope note in `docs/12-RN-formalization.md` and contention 1 in `docs/07-roadmap.md`.

---

## Scorecard

| Claim | Bare \(C\) | D19 | + B_flow |
|-------|-----------|-----|----------|
| Foot fixed | Yes (T12) | Yes | Yes |
| Support frozen | No | Yes (T12+) | Yes |
| N★ moduli frozen | No | Yes | Yes |
| R★ invertibility | No | Partial | Yes |
| Unitarity (T13) | No | No | Yes (+ norm gauge) |

---

## Conceptual note on R

R means: while co-dependence is still cheap to maintain, weight dynamics must not smuggle irreversible loss. Irreversibility is reserved for structural projection. That is a coherence requirement on the hosted weight layer, implemented by D19 (no silent support collapse) + B_flow (updates are reversible flows).

See also conceptual discussion in conversation history / charter §4.
