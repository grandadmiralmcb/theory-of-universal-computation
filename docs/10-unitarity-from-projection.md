# 10 — Unitarity and Structural Projection (charter-aligned)

Authority: `docs/00-theory-charter.md`, `docs/11-theorems.md`, `docs/13-derive-RN-from-cost.md`.

---

## Scope

Unitarity is a theorem of the **hosted quantum layer (HQ)**, not of bare working-model cost.

**Required:** A4 (linear weights), D19 (extended cost), free epoch (T12), norm gauge. (B_flow was demoted to derived — docs/19 §2; invertibility now follows from T13′.)

**Not required to be claimed:** derivation of A4 or Born from integer \(S,B,D\).

---

## Pipeline (named)

1. **T12** [WM] — free epoch \(\Rightarrow\) Foot fixed (bare cost).
2. **T12+** [HQ/D19] — support frozen.
3. **N★** [HQ/D19] — relative moduli frozen.
4. **R★** [HQ/D19+B_flow] — invertible free-epoch weight maps.
5. **T13** [HQ] — invertible + moduli frozen (all states) + norm gauge \(\Rightarrow\) **diagonal** unitary on the active subspace (phase drift). Under the trajectory-only reading of N★, unitarity does not follow. See docs/12 scope note.
6. **T14** [HQ] — structural decoherence (T10) = sole non-unitary locus (relative to T13 as restated).

---

## Conceptual content

Irreversibility is tied to structural payment (isolation). Free evolution under maintained co-dependence does not silently erase weight information (R) or reweight selection odds at zero cost (N under D19). That is consistency of the hybrid, packaged as unitarity after norm fix.

Caveat: as derived, the same cost argument that freezes moduli also forbids beam-splitter-like recombination in free epochs — the operation interference phenomenology requires. See docs/07 contention 1.

---

## Status line

| Claim | Status |
|-------|--------|
| Foot fixed in free epoch | WM theorem (T12) |
| Support / moduli frozen | HQ theorems under D19 |
| Invertibility | HQ under B_flow |
| Unitarity | Diagonal-unitary under full package (all-states N★); general unitarity contended (docs/07 contention 1) |
| Born | Reading, not theorem |
