#!/usr/bin/env python3
"""
The arrow of time: order is prior, orientation is entropic
===========================================================
Executable companion to docs/25-time-and-the-arrow.md (AT1-AT6).

The claim under test is NOT "time is emergent from the entropy gradient"
flat. In this framework sequential order is forced by O2 (F1 chains,
SM-B3's partial order) with no entropy anywhere in sight, so deriving
*order* from entropy would be circular. What entropy supplies is the
missing half: a strict partial order carries no orientation, and the
gradient is what says which end is the past.

Demonstrations:
  1. AT2 (order without orientation): a chain of free-epoch and
     reconfiguration events leaves S_rel exactly invariant, and every
     such event has an admissible inverse. Run the chain backwards and
     nothing distinguishes it. No arrow.
  2. AT3 (projection orients): the projection event is non-isometric,
     S_rel strictly drops, and the map is NOT injective -- two distinct
     pre-states with identical post-states are exhibited, so no inverse
     exists. Orientation lives here and nowhere else.
  3. AT4 (the ratchet is exclusion, not the number): after projection
     breaks a share link, no chain-reachable structure ever reaches the
     dropped residual again. The asymmetry is structural (F5 + SM-B3),
     one layer below the entropy that measures it.
  4. AT5 (the arrow's density tracks decoherence): sweeping WM4's
     environmental share pressure moves the fraction of oriented ticks
     from ~0 (isolated: chain nearly reversible) to 1 (classical:
     saturated with projection). T11 read in the temporal ledger.
  5. AT6 (duration needs a ratchet): a purely isometric clock recurs --
     its readings repeat with the rotation period, certifying no elapsed
     duration -- while a projection counter is strictly monotone.

Units: nats throughout; s0 = 1 per severed share.
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import Any, List, Optional, Sequence, Set, Tuple
import cmath
import math
import random

Mat = List[List[complex]]

# ---------------------------------------------------------------------------
# 2x2 state machinery (mirrors sim/thermo_gravity.py; kept self-contained so
# each sim runs standalone, per sim/README.md)
# ---------------------------------------------------------------------------

def _herm_eig_2x2(m: Mat) -> Tuple[List[float], List[List[complex]]]:
    a, d, b = m[0][0].real, m[1][1].real, m[0][1]
    if abs(b) <= 1e-14:
        return [a, d], [[1.0 + 0j, 0j], [0j, 1.0 + 0j]]
    half = 0.5 * (a + d)
    disc = math.sqrt(0.25 * (a - d) ** 2 + abs(b) ** 2)
    vals = [half + disc, half - disc]
    v = [b, complex(vals[0] - a, 0.0)]
    nrm = math.sqrt(sum(abs(x) ** 2 for x in v))
    v0 = [x / nrm for x in v]
    return vals, [v0, [-v0[1].conjugate(), v0[0].conjugate()]]


def rel_entropy_q(rho: Mat, sigma: Mat) -> float:
    rv, _ = _herm_eig_2x2(rho)
    sv, sw = _herm_eig_2x2(sigma)
    term1 = sum(l * math.log(l) for l in rv if l > 1e-15)
    term2 = 0.0
    for lam, v in zip(sv, sw):
        if lam <= 1e-15:
            continue
        acc = 0j
        for i in range(2):
            for j in range(2):
                acc += v[i].conjugate() * rho[i][j] * v[j]
        term2 += math.log(lam) * acc.real
    return term1 - term2


def conj_map(u: Mat, rho: Mat) -> Mat:
    n = len(u)
    out = [[0j for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            acc = 0j
            for a in range(n):
                for b in range(n):
                    acc += u[i][a] * rho[a][b] * u[j][b].conjugate()
            out[i][j] = acc
    return out


def dagger(u: Mat) -> Mat:
    return [[u[j][i].conjugate() for j in range(len(u))] for i in range(len(u))]


def rot(theta: float) -> Mat:
    return [[math.cos(theta) + 0j, -math.sin(theta) + 0j],
            [math.sin(theta) + 0j, math.cos(theta) + 0j]]


def phase(p1: float, p2: float) -> Mat:
    """A free-epoch map: diagonal unimodular (T13')."""
    return [[cmath.exp(1j * p1), 0j], [0j, cmath.exp(1j * p2)]]


def dephase(rho: Mat) -> Mat:
    """The record a structural projection leaves (T14')."""
    return [[rho[i][j] if i == j else 0j for j in range(2)] for i in range(2)]


def select(rho: Mat, k: int) -> Mat:
    """The outcome: class k survives, renormalised."""
    p = rho[k][k].real
    assert p > 1e-12, "cannot select a class of zero weight"
    out = [[0j, 0j], [0j, 0j]]
    out[k][k] = 1.0 + 0j
    return out


# ---------------------------------------------------------------------------
# 1. AT2 — order carries no orientation
# ---------------------------------------------------------------------------

def demo_order_without_orientation() -> None:
    rho: Mat = [[0.70 + 0j, 0.30 + 0.10j], [0.30 - 0.10j, 0.30 + 0j]]
    sigma: Mat = [[0.55 + 0j, 0.10 - 0.05j], [0.10 + 0.05j, 0.45 + 0j]]
    events = [("free epoch  (T13' diagonal)", phase(0.7, -1.9)),
              ("reconfig    (T16' isometry)", rot(0.6)),
              ("free epoch  (T13' diagonal)", phase(-0.4, 2.2)),
              ("reconfig    (T16' isometry)", rot(-1.1))]

    base = rel_entropy_q(rho, sigma)
    print(f"   {'event':>30} {'S_rel':>12} {'inverse admissible?':>21}")
    print(f"   {'(initial)':>30} {base:>12.9f} {'-':>21}")
    r, s = rho, sigma
    for name, u in events:
        prev = r
        r, s = conj_map(u, r), conj_map(u, s)
        val = rel_entropy_q(r, s)
        # the inverse is the adjoint, itself an admissible event of the same type
        back = conj_map(dagger(u), r)
        invertible = max(abs(back[i][j] - prev[i][j])
                         for i in range(2) for j in range(2)) < 1e-12
        print(f"   {name:>30} {val:>12.9f} "
              f"{('yes (adjoint)' if invertible else 'NO'):>21}")
        assert abs(val - base) < 1e-10
        assert invertible

    print("\n   running the same chain BACKWARDS through the adjoints:")
    for name, u in reversed(events):
        r, s = conj_map(dagger(u), r), conj_map(dagger(u), s)
    err = max(abs(r[i][j] - rho[i][j]) for i in range(2) for j in range(2))
    print(f"      returned to the initial state, max error {err:.2e}")
    assert err < 1e-12
    print("   -> S_rel constant at every step and the reversed history is equally")
    print("      admissible. F1/SM-B3 order is invariant under reversal: it fixes")
    print("      WHICH events neighbour which, and says nothing about which end is")
    print("      the past. There is no arrow here to find.")


# ---------------------------------------------------------------------------
# 2. AT3 — projection is where orientation lives
# ---------------------------------------------------------------------------

def demo_projection_orients() -> None:
    rho: Mat = [[0.70 + 0j, 0.30 + 0.10j], [0.30 - 0.10j, 0.30 + 0j]]
    sigma: Mat = [[0.55 + 0j, 0.10 - 0.05j], [0.10 + 0.05j, 0.45 + 0j]]
    base = rel_entropy_q(rho, sigma)
    deph = rel_entropy_q(dephase(rho), dephase(sigma))
    sel = rel_entropy_q(select(rho, 0), select(sigma, 0))
    print(f"      S_rel before projection        = {base:.9f}")
    print(f"      after the record (dephasing)   = {deph:.9f}   [strictly down]")
    print(f"      after the outcome (selection)  = {sel:.9f}   [down to zero]")
    assert deph < base - 1e-9 and sel < deph + 1e-12

    print("\n   the map has no inverse — two distinct pre-states, one post-state:")
    alt: Mat = [[0.40 + 0j, 0.20 - 0.35j], [0.20 + 0.35j, 0.60 + 0j]]
    a, b = select(rho, 0), select(alt, 0)
    same = max(abs(a[i][j] - b[i][j]) for i in range(2) for j in range(2))
    print(f"      rho[0][0] = {rho[0][0].real:.2f},  alt[0][0] = {alt[0][0].real:.2f}"
          f"   -> identical outputs (max diff {same:.1e})")
    assert same < 1e-15
    print("   -> non-injective, so no admissible map runs it backwards. The chain")
    print("      can be traversed one way only, and that is what an arrow IS.")
    print("      By T14' this is the ONLY event type with the property.")


# ---------------------------------------------------------------------------
# 3. AT4 — the ratchet is exclusion; entropy measures it
# ---------------------------------------------------------------------------

@dataclass
class Share:
    id: str
    content: Any = None

@dataclass
class Node:
    """A residual class holding share links, by object identity."""
    name: str
    shares: List[Share]


def reachable_shares(nodes: Sequence[Node]) -> Set[int]:
    out: Set[int] = set()
    for n in nodes:
        for s in n.shares:
            out.add(id(s))
    return out


def demo_exclusion_is_stable() -> None:
    link_B = Share("chain<->B")
    link_C = Share("chain<->C")
    own = Share("chain-own")
    chain = Node("chain", [own, link_B, link_C])
    B = Node("B", [link_B])
    C = Node("C", [link_C])

    def co_dependent(x: Node, y: Node) -> bool:
        return bool(reachable_shares([x]) & reachable_shares([y]))

    print(f"   before projection: chain<->B co-dependent = {co_dependent(chain, B)},"
          f"  chain<->C = {co_dependent(chain, C)}")
    assert co_dependent(chain, B) and co_dependent(chain, C)

    # F5: selection isolates the chain's residual by breaking the shared links
    chain.shares = [own]
    print(f"   after  projection: chain<->B co-dependent = {co_dependent(chain, B)},"
          f"  chain<->C = {co_dependent(chain, C)}")
    assert not co_dependent(chain, B) and not co_dependent(chain, C)

    print("\n   advancing the chain 200 further steps (new structure each step):")
    for t in range(200):
        chain.shares.append(Share(f"chain-step-{t}"))
        assert not co_dependent(chain, B) and not co_dependent(chain, C)
    print(f"      chain now holds {len(chain.shares)} shares; B and C reachable: "
          f"{co_dependent(chain, B) or co_dependent(chain, C)}")
    print("   -> B and C remain REAL (O4/F3) but are permanently off this chain.")
    print("      Re-inclusion would need a data-dependence path, and the projection")
    print("      is exactly what removed it (SM-B3: causal exclusion is stable).")
    print("      The asymmetry is structural — F5 + O4 + SM-B3, all forced-layer.")
    print("      dS_gen >= 0 is the READOUT of this ratchet, not its source.")


# ---------------------------------------------------------------------------
# 4. AT5 — the arrow's density tracks decoherence
# ---------------------------------------------------------------------------

def projects(n_cross: int, n_env: int, alpha: float = 1.0,
             beta: float = 0.0, gamma: float = 2.0) -> bool:
    """T10: isolate when C_isolate <= C_maintain (WM4 charges env to maintain)."""
    c_isolate = alpha * n_cross + gamma
    c_maintain = alpha * (n_cross + n_env)
    return c_isolate <= c_maintain


def demo_arrow_density(ticks: int = 4000) -> None:
    rng = random.Random(20260830)
    print(f"   {'env coupling':>13} {'mean n_env':>11} {'oriented ticks':>15} {'regime':>26}")
    for lam in (0.05, 0.5, 1.0, 2.0, 5.0, 20.0, 100.0, 1000.0):
        oriented = 0
        tot = 0
        for _ in range(ticks):
            n_env = int(rng.expovariate(1.0 / lam))
            tot += n_env
            if projects(n_cross=3, n_env=n_env):
                oriented += 1
        frac = oriented / ticks
        regime = ("isolated: near-reversible" if frac < 0.05
                  else "classical: saturated" if frac > 0.95
                  else "intermediate")
        print(f"   {lam:>13.2f} {tot / ticks:>11.2f} {frac:>14.1%} {regime:>26}")
    print("   -> temporal orientation is exactly as dense as decoherence. This is")
    print("      not a new hypothesis: it is T11 (rising maintain cost => classical")
    print("      sequentialization) read in the temporal ledger. It explains why the")
    print("      arrow is macroscopically ubiquitous and microscopically absent.")


# ---------------------------------------------------------------------------
# 5. AT6 — duration needs a ratchet
# ---------------------------------------------------------------------------

def demo_clock(steps: int = 12) -> None:
    u = rot(2.0 * math.pi / 8.0)
    period = 4          # conjugation by rot(pi) = -I is the identity on states
    rho: Mat = [[1.0 + 0j, 0j], [0j, 0j]]
    print("   an isometric clock (rotation by 2pi/8), reading = <0|rho|0>,")
    print("   against a projective counter that ratchets once per tick:")
    readings: List[float] = []
    r = rho
    print(f"   {'step':>6} {'isometric reading':>19} {'projection count':>18}")
    for t in range(steps + 1):
        readings.append(r[0][0].real)
        print(f"   {t:>6} {r[0][0].real:>19.6f} {t:>18}")
        r = conj_map(u, r)
    for t in range(steps + 1 - period):
        assert abs(readings[t] - readings[t + period]) < 1e-9
    assert max(readings) - min(readings) > 0.5, "the reading must actually vary"
    print(f"\n      the reading revisits every value with period {period}:"
          f" step 0 = {readings[0]:.3f},"
          f" step {period} = {readings[period]:.3f},"
          f" step {2 * period} = {readings[2 * period]:.3f}")
    print("   -> the isometric reading varies but REPEATS: it cannot distinguish")
    print(f"      t from t+{period}, so it certifies no elapsed duration. Only")
    print("      the projection count is monotone. A clock must ratchet, and by AT3")
    print("      the framework has exactly one ratchet. Measurable duration is")
    print("      counted by projection events -- i.e. by accumulated dS_gen.")


# ---------------------------------------------------------------------------

def demo() -> None:
    print("=" * 74)
    print("The arrow of time: order is prior, orientation is entropic (docs/25)")
    print("=" * 74)
    print("\n1. AT2 — a chain of isometric events carries no orientation")
    demo_order_without_orientation()
    print("\n2. AT3 — structural projection is where orientation lives")
    demo_projection_orients()
    print("\n3. AT4 — the ratchet is exclusion; the entropy gradient measures it")
    demo_exclusion_is_stable()
    print("\n4. AT5 — the arrow's density tracks decoherence")
    demo_arrow_density()
    print("\n5. AT6 — duration needs a ratchet")
    demo_clock()
    print("=" * 74)


if __name__ == "__main__":
    demo()
