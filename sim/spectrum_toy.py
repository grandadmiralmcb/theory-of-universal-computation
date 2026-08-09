#!/usr/bin/env python3
"""
Labeled-share toy: conservation by typing, spectrum from cost landscape,
dark-sector stability
=====================================================================
Executable demonstrations for docs/15-sm-bridge.md (SB1, SB1-typing, SB3;
theorems SM-B1, SM-B2). Mechanism only — no Standard-Model value is
predicted or fitted.

  1. SM-B1' property test: total charge is invariant under long random
     sequences of conserving moves (merge / split / pair-create /
     pair-annihilate), and a deliberately violating move (deleting a
     charged share) breaks it. Since the adoption of ST1 + CC'
     (charter, docs/21 §5), "admissible" means V=0 (zero top-stratum
     violation charge), not typing fiat: this move set is the derived
     V=0 stratum, and every configuration here admits a conserving
     continuation, so conditional conservation (SM-B1') coincides with
     absolute conservation on this domain. The stratified selection
     mechanism itself is exercised in sim/stratified_cost.py §4.
  2. Two-phase toy spectrum: minimal excitation of charge Q is
     Q unit shares when lambda > alpha_m/2 (exact linear m(Q)); for
     lambda < alpha_m/2 the optimum clumps into shares of characteristic
     charge ~sqrt(alpha_m/lambda) (single merged share only at small Q).
     Spectrum shape — including the emergent charge quantum — is a
     property of the cost landscape.
  3. Dark sector: a cluster neutral in the 'interacting' label but
     charged in a second conserved label is stable and has m_struct > 0
     with no interacting-label handle; a fully neutral cluster decays.
"""

from __future__ import annotations
import random
from dataclasses import dataclass
from typing import Iterator, List, Optional, Tuple

Charge = Tuple[int, int]  # (q_interacting, q_dark)

ALPHA_M = 1.0   # WM3 inertia coefficient (alpha_m in the docs)
EPS = 0.05      # WM3 floor


@dataclass
class ShareNode:
    q: Charge


def qsum(shares: List[ShareNode]) -> Charge:
    return (sum(s.q[0] for s in shares), sum(s.q[1] for s in shares))


def m_struct(shares: List[ShareNode]) -> float:
    return ALPHA_M * len(shares) + EPS


def rest_cost(shares: List[ShareNode], lam: float) -> float:
    """SB3 toy rest cost: alpha_m * n_share + lambda * sum |q|^2 + eps.
    The tension form is toy data, not theory (docs/15 §3)."""
    tension = sum(s.q[0] ** 2 + s.q[1] ** 2 for s in shares)
    return ALPHA_M * len(shares) + lam * tension + EPS


# ---------------------------------------------------------------------------
# SB1-typing: admissible moves (each preserves the label sum by construction)
# ---------------------------------------------------------------------------

def mv_merge(sh: List[ShareNode]) -> Optional[List[ShareNode]]:
    if len(sh) < 2:
        return None
    i, j = random.sample(range(len(sh)), 2)
    merged = ShareNode((sh[i].q[0] + sh[j].q[0], sh[i].q[1] + sh[j].q[1]))
    return [s for k, s in enumerate(sh) if k not in (i, j)] + [merged]


def mv_split(sh: List[ShareNode]) -> Optional[List[ShareNode]]:
    if not sh:
        return None
    i = random.randrange(len(sh))
    q0, q1 = sh[i].q
    a0, a1 = random.randint(-2, 2), random.randint(-2, 2)
    parts = [ShareNode((a0, a1)), ShareNode((q0 - a0, q1 - a1))]
    return [s for k, s in enumerate(sh) if k != i] + parts


def mv_pair_create(sh: List[ShareNode]) -> List[ShareNode]:
    q = (random.randint(-1, 1), random.randint(-1, 1))
    return sh + [ShareNode(q), ShareNode((-q[0], -q[1]))]


def mv_pair_annihilate(sh: List[ShareNode]) -> Optional[List[ShareNode]]:
    for i in range(len(sh)):
        for j in range(i + 1, len(sh)):
            if sh[i].q[0] == -sh[j].q[0] and sh[i].q[1] == -sh[j].q[1]:
                return [s for k, s in enumerate(sh) if k not in (i, j)]
    return None


def mv_delete_charged(sh: List[ShareNode]) -> Optional[List[ShareNode]]:
    """INADMISSIBLE under SB1-typing — included to show typing does the work."""
    charged = [k for k, s in enumerate(sh) if s.q != (0, 0)]
    if not charged:
        return None
    i = random.choice(charged)
    return [s for k, s in enumerate(sh) if k != i]


def demo_conservation(steps: int = 2000, seed: int = 7) -> None:
    random.seed(seed)
    sh = [ShareNode((1, 0)), ShareNode((0, 1)), ShareNode((-1, 0))]
    Q0 = qsum(sh)
    violations = 0
    moves = [mv_merge, mv_split, mv_pair_create, mv_pair_annihilate]
    for _ in range(steps):
        out = random.choice(moves)(sh)
        if out is None:
            continue
        sh = out
        if qsum(sh) != Q0:
            violations += 1
    print(f"   {steps} random admissible moves from charge {Q0}: "
          f"violations = {violations} (SM-B1 requires 0)")
    bad = mv_delete_charged(sh)
    if bad is not None:
        print(f"   one INADMISSIBLE move (delete charged share): "
              f"{qsum(sh)} -> {qsum(bad)}  — conservation fails, as it must")


# ---------------------------------------------------------------------------
# SB3: two-phase toy spectrum
# ---------------------------------------------------------------------------

def partitions(n: int, max_part: Optional[int] = None) -> Iterator[List[int]]:
    if max_part is None:
        max_part = n
    if n == 0:
        yield []
        return
    for p in range(min(n, max_part), 0, -1):
        for rest in partitions(n - p, p):
            yield [p] + rest


def min_cost_for_charge(Q: int, lam: float) -> Tuple[float, List[int]]:
    """Minimal rest cost over configurations of total interacting charge Q.
    Positive parts suffice: adding a (+a,-a) pair only raises cost."""
    best: Optional[Tuple[float, List[int]]] = None
    for parts in partitions(Q):
        sh = [ShareNode((p, 0)) for p in parts]
        c = rest_cost(sh, lam)
        if best is None or c < best[0]:
            best = (c, parts)
    assert best is not None
    return best


def demo_spectrum() -> None:
    for lam, label in [
        (1.0, "lambda=1.0 > alpha_m/2  ->  unit-share phase, m(Q) = (alpha_m+lambda)Q + eps"),
        (0.2, "lambda=0.2 < alpha_m/2  ->  clumped phase, share charge ~ sqrt(alpha_m/lambda) ~ 2.2"),
    ]:
        print(f"\n   {label}")
        print("   Q   min rest cost   minimal configuration (share charges)")
        for Q in range(1, 6):
            c, parts = min_cost_for_charge(Q, lam)
            print(f"   {Q}   {c:12.2f}    {parts}")


# ---------------------------------------------------------------------------
# SB3: stability search and dark sector
# ---------------------------------------------------------------------------

def is_stable(sh: List[ShareNode], lam: float) -> bool:
    """No admissible move lowers rest cost. Checked against: all pairwise
    merges, all annihilations, removal of fully-neutral shares, and binary
    splits with components in [-2, 2] (sufficient for the unit-charge
    configurations used here)."""
    c0 = rest_cost(sh, lam)
    n = len(sh)
    for i in range(n):
        for j in range(i + 1, n):
            if sh[i].q[0] == -sh[j].q[0] and sh[i].q[1] == -sh[j].q[1]:
                rest = [s for k, s in enumerate(sh) if k not in (i, j)]
                if rest_cost(rest, lam) < c0:
                    return False
            merged = [s for k, s in enumerate(sh) if k not in (i, j)] + \
                     [ShareNode((sh[i].q[0] + sh[j].q[0], sh[i].q[1] + sh[j].q[1]))]
            if rest_cost(merged, lam) < c0:
                return False
    for i in range(n):
        if sh[i].q == (0, 0):
            rest = [s for k, s in enumerate(sh) if k != i]
            if rest_cost(rest, lam) < c0:
                return False
        q0, q1 = sh[i].q
        for a0 in range(-2, 3):
            for a1 in range(-2, 3):
                parts = [ShareNode((a0, a1)), ShareNode((q0 - a0, q1 - a1))]
                cand = [s for k, s in enumerate(sh) if k != i] + parts
                if rest_cost(cand, lam) < c0:
                    return False
    return True


def demo_dark(lam: float = 1.0) -> None:
    dark = [ShareNode((0, 1)), ShareNode((0, 1))]
    Qi, Qd = qsum(dark)
    print(f"   dark cluster {[s.q for s in dark]}:")
    print(f"     interacting charge = {Qi}, dark charge = {Qd}")
    print(f"     m_struct = {m_struct(dark):.2f}  "
          f"(inertia, label-blind) — no interacting-label handle")
    print(f"     stable under admissible moves? {is_stable(dark, lam)}")
    neutral = [ShareNode((0, 0)), ShareNode((0, 0))]
    print(f"   fully neutral cluster {[s.q for s in neutral]}: "
          f"stable? {is_stable(neutral, lam)}  "
          f"(decays — no conserved label protects it)")


def demo() -> None:
    print("=" * 64)
    print("Labeled-share toy: typing conservation, spectrum, dark sector")
    print("=" * 64)
    print("\n1. SM-B1 property test (conservation by typing)")
    demo_conservation()
    print("\n2. Two-phase toy spectrum (mechanism demo — no SM values)")
    demo_spectrum()
    print("\n3. Dark sector: conserved label + inertia, no interacting handle")
    demo_dark()
    print("=" * 64)


if __name__ == "__main__":
    demo()
