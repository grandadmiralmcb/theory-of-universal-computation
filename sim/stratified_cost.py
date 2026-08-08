#!/usr/bin/env python3
"""
Stratified (lexicographic) cost: the ¬CC variant developed
==========================================================
Executable companion to docs/21-stratified-variant.md (contention 8).

A stratified cost is a tuple (hi, lo) compared lexicographically:
minimize hi first; break ties on lo. Per RM2 (docs/20 §5) this is the
only alternative shape to the one-currency (Archimedean) cost.

Demonstrations:
  1. Lex selection = constraint-then-cost: the top stratum acts as a
     hard constraint (exact rule), the floor as ordinary cost.
  2. TS1 (classical viability): splitting CI4's velocity-cost terms
     across strata degenerates dynamics — inertial-term-on-top freezes
     motion; bias-term-on-top produces grid-edge runaway. Newtonian
     dynamics requires its ingredients to share one stratum.
  3. TS2 (decoherence freeze): with the identity flag D on top, the
     isolation/maintain comparison is decided at the top stratum, so
     no amount of environmental share pressure ever triggers
     projection — the classical limit of coherence (T11) is lost.
     Observed classicality therefore forces the dynamical floor to be
     one-currency.
  4. TS4 (typing as top stratum): replacing SB1-typing's admissibility
     rule with a top-stratum violation charge reproduces conservation
     exactly when conserving alternatives exist — and degrades
     gracefully (minimal violation) when they do not, which brute
     typing cannot even express.
"""

from __future__ import annotations
import math
from typing import List, Sequence, Tuple

Strat = Tuple[float, float]  # (hi, lo), lexicographic


def lex_min(candidates: Sequence[Tuple[Strat, object]]) -> Tuple[Strat, object]:
    """Operation: stratified preferential_select (argmin in lex order)."""
    return min(candidates, key=lambda c: (c[0][0], c[0][1]))


# ---------------------------------------------------------------------------
# 1. Constraint-then-cost
# ---------------------------------------------------------------------------

def demo_lex_select() -> None:
    candidates = [
        ((1.0, 0.1), "violates exact rule, cheap floor"),
        ((0.0, 5.0), "respects rule, expensive floor"),
        ((0.0, 2.0), "respects rule, moderate floor"),
    ]
    cost, label = lex_min(candidates)
    print(f"   candidates: {[(c[0], c[1]) for c in candidates]}")
    print(f"   selected: {cost} — {label}")
    print("   -> top stratum is a hard constraint; floor is ordinary cost")


# ---------------------------------------------------------------------------
# 2. TS1 — classical viability
# ---------------------------------------------------------------------------

def demo_classical_viability(m: float = 5.0, b: float = 1.0, dt: float = 0.05) -> None:
    grid = [i * 0.001 for i in range(-200, 201)]  # candidate dv increments

    def pick(cost_of_dv) -> float:
        return lex_min([(cost_of_dv(dv), dv) for dv in grid])[1]

    # (a) co-stratal (one-currency floor): CI4 as usual
    dv_a = pick(lambda dv: (0.0, 0.5 * m * dv * dv / dt + b * dv))
    # (b) inertial term on top
    dv_b = pick(lambda dv: (0.5 * m * dv * dv / dt, b * dv))
    # (c) bias term on top
    dv_c = pick(lambda dv: (b * dv, 0.5 * m * dv * dv / dt))

    print(f"   analytic one-currency increment: dv* = -(b/m)dt = {-(b/m)*dt:.4f}")
    print(f"   (a) both terms in floor:  dv = {dv_a:+.4f}  (Newtonian)")
    print(f"   (b) inertial term on top: dv = {dv_b:+.4f}  (frozen — dv=0 uniquely minimizes top)")
    print(f"   (c) bias term on top:     dv = {dv_c:+.4f}  (grid-edge runaway — top unbounded below)")
    print("   -> TS1: viable stratifications keep all CI4 ingredients co-stratal")


# ---------------------------------------------------------------------------
# 3. TS2 — decoherence freeze under D-top stratification
# ---------------------------------------------------------------------------

def demo_decoherence_freeze() -> None:
    # expr_tree demo shapes: C_iso has (S=1, B=0, D=1); C_maint has (S=1+env, B=0, D=0)
    alpha, gamma = 1.0, 2.0

    def iso_one_currency() -> float:
        return alpha * 1 + gamma * 1

    def maint_one_currency(env: int) -> float:
        return alpha * (1 + env)

    def iso_strat() -> Strat:      # D on top
        return (1.0, alpha * 1)

    def maint_strat(env: int) -> Strat:
        return (0.0, alpha * (1 + env))

    print("   env    one-currency verdict        D-top stratified verdict")
    for env in (0, 5, 50, 5000):
        oc = "decohere" if iso_one_currency() <= maint_one_currency(env) else "coherent"
        st = "decohere" if iso_strat() <= maint_strat(env) else "coherent"
        print(f"   {env:5d}  iso {iso_one_currency():5.1f} vs {maint_one_currency(env):7.1f}: {oc:9s}"
              f"  iso {iso_strat()} vs {maint_strat(env)}: {st}")
    print("   -> TS2: with D on top, no environmental pressure ever triggers")
    print("      projection; T11 (classical limit of coherence) is lost.")
    print("      Observed classicality forces the dynamical floor to be one-currency.")


# ---------------------------------------------------------------------------
# 4. TS4 — typing as top stratum
# ---------------------------------------------------------------------------

def demo_typing_as_stratum() -> None:
    # Candidates for reducing a labeled cluster; V = label-violation units (top),
    # floor = structural cost. SB1-typing admissibility = "V must be 0".
    print("   case 1: conserving alternatives exist")
    candidates = [
        ((0.0, 4.0), "conserving merge (V=0)"),
        ((0.0, 6.0), "conserving pair-annihilation path (V=0)"),
        ((1.0, 1.0), "delete charged share (V=1, cheap floor)"),
    ]
    cost, label = lex_min(candidates)
    print(f"     selected: {label}  {cost}")
    print("     -> conservation reproduced without a typing rule (SM-B1 behavior)")

    print("   case 2: forced violation (no conserving move exists)")
    candidates = [
        ((2.0, 1.0), "double violation (V=2)"),
        ((1.0, 3.0), "single violation (V=1)"),
    ]
    cost, label = lex_min(candidates)
    print(f"     selected: {label}  {cost}")
    print("     -> graceful degradation: minimal violation selected;")
    print("        brute typing deadlocks here (no admissible move at all)")


def demo() -> None:
    print("=" * 68)
    print("Stratified (lexicographic) cost — the ¬CC variant (docs/21)")
    print("=" * 68)
    print("\n1. Lex selection = constraint-then-cost")
    demo_lex_select()
    print("\n2. TS1 — classical viability under stratification")
    demo_classical_viability()
    print("\n3. TS2 — decoherence freeze when the identity flag sits on top")
    demo_decoherence_freeze()
    print("\n4. TS4 — SB1-typing recovered as a top stratum (and generalized)")
    demo_typing_as_stratum()
    print("=" * 68)


if __name__ == "__main__":
    demo()
