#!/usr/bin/env python3
"""
Splitter rewrite: the induced map computed from share bookkeeping
=================================================================
Discharges docs/17 §7 item 1 / docs/16 criterion C2, under adversarial
pressure P1 ("exhibit M computed from the rewrite, or drop 'determined
by the rewrite'"). Formal companion: docs/18-splitter-functor.md.

The functor F (unit-share granularity):
  - a class = a set of unit shares (structure quanta of the event's own
    description; class weights are granularity-independent)
  - a reconfiguration rewrite = a routing of every unit to a new class,
    each route carrying an orientation tag (a phase) — device data from
    binding geometry
  - DOMAIN: channel-disjoint routings (at most one unit per
    (old class -> new class) pair); outside the domain, coherent
    same-class stacking inflates the persisting-structure measure
    (demonstrated in demo 4) — such routings encode intra-class merges
    and are not pure reconfigurations
  - induced map:  M[j][i] = sum_{units u: i->j} tag(u) / sqrt(n_i)
    * moduli: |M[j][i]|^2 = (units of i routed to j) / n_i — the routed
      fraction. This is postulate D20 applied at unit granularity:
      weight measures persisting structure.
    * phases: orientation tags — device data (the phi enrichment)
  - FILTER (T16b): F(rewrite) must be an isometry; tag assignments that
    fail are not admissible reconfigurations.

Demonstrations:
  1. 1->2 symmetric splitter: M = (1/sqrt2, 1/sqrt2)^T computed from
     routing; isometric.
  2. 2->2 symmetric recombiner: enumerate ALL +-1 tag assignments;
     exactly the odd-sign-flip half passes the isometry filter, and
     every survivor equals the Hadamard up to diagonal +-1 gauge.
     The beam-splitter matrix is derived = routing moduli (D20) +
     isometry-admissible tags. Nothing is stipulated.
  3. Mach-Zehnder end to end: splitter -> free-epoch phase drift ->
     recombiner -> Born at detectors. Fringes P(C) = cos^2(phi/2),
     visibility 1; Monte Carlo agrees.
  4. Negative cases: a 2->1 merge admits no isometric induced map
     (dimension) — merges always contain a projection component; a
     non-channel-disjoint routing inflates weight (D20 violation).
"""

from __future__ import annotations
import cmath
import itertools
import math
import random
from dataclasses import dataclass
from typing import Dict, List, Sequence, Tuple

Matrix = List[List[complex]]


@dataclass(frozen=True)
class Route:
    old_cls: str
    unit: int
    new_cls: str
    tag: complex  # orientation tag (phase) — device data


def induced_map(routes: Sequence[Route], old_order: Sequence[str],
                new_order: Sequence[str]) -> Matrix:
    """Operation F: rewrite -> linear map, per the docstring."""
    n: Dict[str, int] = {c: 0 for c in old_order}
    for r in routes:
        n[r.old_cls] += 1
    M: Matrix = [[0j] * len(old_order) for _ in new_order]
    for r in routes:
        i = old_order.index(r.old_cls)
        j = new_order.index(r.new_cls)
        M[j][i] += r.tag / math.sqrt(n[r.old_cls])
    return M


def channel_disjoint(routes: Sequence[Route]) -> bool:
    seen = set()
    for r in routes:
        key = (r.old_cls, r.new_cls)
        if key in seen:
            return False
        seen.add(key)
    return True


def gram(M: Matrix) -> Matrix:
    rows, cols = len(M), len(M[0])
    return [[sum(M[k][i].conjugate() * M[k][j] for k in range(rows))
             for j in range(cols)] for i in range(cols)]


def is_isometry(M: Matrix, eps: float = 1e-9) -> bool:
    G = gram(M)
    return all(abs(G[i][j] - (1 if i == j else 0)) <= eps
               for i in range(len(G)) for j in range(len(G)))


def matvec(M: Matrix, a: Sequence[complex]) -> List[complex]:
    return [sum(M[j][i] * a[i] for i in range(len(a))) for j in range(len(M))]


def fmt(M: Matrix) -> str:
    return "  ".join("[" + ", ".join(f"{x.real:+.3f}{x.imag:+.3f}i" for x in row) + "]"
                     for row in M)


# ---------------------------------------------------------------------------
# 1. Splitter 1 -> 2
# ---------------------------------------------------------------------------

def demo_splitter() -> Matrix:
    routes = [Route("S", 1, "A", 1), Route("S", 2, "B", 1)]
    M = induced_map(routes, ["S"], ["A", "B"])
    print("   routing: S has 2 units; unit1->A, unit2->B (tags +1)")
    print(f"   computed M = {fmt(M)}")
    print(f"   |M_A|^2 = {abs(M[0][0])**2:.3f}, |M_B|^2 = {abs(M[1][0])**2:.3f}"
          f"  (routed fractions 1/2, 1/2 — D20)")
    print(f"   isometry (T16b filter): {is_isometry(M)}")
    return M


# ---------------------------------------------------------------------------
# 2. Recombiner 2 -> 2: the filter pins the Hadamard up to gauge
# ---------------------------------------------------------------------------

HAD = [[1 / math.sqrt(2), 1 / math.sqrt(2)],
       [1 / math.sqrt(2), -1 / math.sqrt(2)]]


def equal(Ma: Matrix, Mb: Matrix, eps: float = 1e-9) -> bool:
    return all(abs(Ma[j][i] - Mb[j][i]) <= eps
               for j in range(len(Ma)) for i in range(len(Ma[0])))


def hadamard_up_to_gauge(M: Matrix) -> bool:
    """M == diag(u,v) . HAD . diag(p,q) for signs u,v,p,q?"""
    for u, v, p, q in itertools.product((1, -1), repeat=4):
        G = [[u * HAD[0][0] * p, u * HAD[0][1] * q],
             [v * HAD[1][0] * p, v * HAD[1][1] * q]]
        if equal(M, G):
            return True
    return False


def recombiner_with_tags(tags: Tuple[int, int, int, int]) -> Matrix:
    t1, t2, t3, t4 = tags
    routes = [Route("A", 1, "C", t1), Route("A", 2, "D", t2),
              Route("B", 1, "C", t3), Route("B", 2, "D", t4)]
    return induced_map(routes, ["A", "B"], ["C", "D"])


def demo_recombiner() -> Matrix:
    print("   routing: A{u1->C, u2->D}, B{u1->C, u2->D}; tags in {+1,-1}^4")
    survivors = []
    for tags in itertools.product((1, -1), repeat=4):
        M = recombiner_with_tags(tags)
        if is_isometry(M):
            survivors.append((tags, M))
    print(f"   tag assignments: 16 total, {len(survivors)} pass the isometry filter")
    all_had = all(hadamard_up_to_gauge(M) for _, M in survivors)
    odd_flip = all((t[0] * t[1] * t[2] * t[3]) == -1 for t, _ in survivors)
    print(f"   every survivor has an odd number of sign flips: {odd_flip}")
    print(f"   every survivor equals Hadamard up to diagonal +-1 gauge: {all_had}")
    canon = recombiner_with_tags((1, 1, 1, -1))
    print(f"   canonical survivor (tags +,+,+,-): M = {fmt(canon)}")
    print("   -> moduli forced by routing (D20); phases pinned up to gauge by")
    print("      the T16b filter. The Hadamard is derived, not stipulated.")
    return canon


# ---------------------------------------------------------------------------
# 3. Mach-Zehnder end to end
# ---------------------------------------------------------------------------

def demo_mach_zehnder(M1: Matrix, M2: Matrix) -> None:
    print("   pipeline: source --M1--> arms --phase drift (free epoch)--> --M2--> detectors --Born")
    print("   phi/pi    P(C)      P(D)     expected cos^2(phi/2)")
    for k in range(0, 9):
        phi = k * math.pi / 4
        a = matvec(M1, [1.0 + 0j])
        a = [a[0], a[1] * cmath.exp(1j * phi)]      # diagonal drift, N* holds
        out = matvec(M2, a)
        pC, pD = abs(out[0]) ** 2, abs(out[1]) ** 2
        print(f"   {phi/math.pi:5.2f}   {pC:7.4f}   {pD:7.4f}     {math.cos(phi/2)**2:7.4f}")
    phi = math.pi / 3
    a = matvec(M1, [1.0 + 0j])
    a = [a[0], a[1] * cmath.exp(1j * phi)]
    out = matvec(M2, a)
    pC = abs(out[0]) ** 2
    random.seed(11)
    hits = sum(1 for _ in range(5000) if random.random() < pC)
    print(f"   Monte Carlo Born at phi=pi/3: P(C) observed {hits/5000:.3f}, "
          f"predicted {pC:.3f}")
    print("   visibility = 1 (fringes from phase drift + derived recombiner)")


# ---------------------------------------------------------------------------
# 4. Negative cases
# ---------------------------------------------------------------------------

def demo_negative() -> None:
    merge = [Route("A", 1, "C", 1), Route("B", 1, "C", 1)]
    Mm = induced_map(merge, ["A", "B"], ["C"])
    print(f"   2->1 merge: M = {fmt(Mm)}; isometry: {is_isometry(Mm)}")
    print("     (no isometry C^2 -> C^1 exists — merges always contain a")
    print("      projection component; T15 classifies them as (3) o (2))")
    lossy = [Route("A", 1, "C", 1), Route("A", 2, "C", 1),
             Route("B", 1, "C", 1), Route("B", 2, "C", 1)]
    Ml = induced_map(lossy, ["A", "B"], ["C", "D"])
    print(f"   non-channel-disjoint routing (all 4 units -> C): "
          f"channel_disjoint = {channel_disjoint(lossy)}")
    print(f"     M = {fmt(Ml)}; column norm^2 of A = {abs(Ml[0][0])**2:.1f} "
          f"(weight inflated — D20 violated; outside F's domain)")


def demo() -> None:
    print("=" * 68)
    print("Splitter rewrite: induced map computed from share bookkeeping")
    print("=" * 68)
    print("\n1. Splitter (1 -> 2), M computed from routing")
    M1 = demo_splitter()
    print("\n2. Recombiner (2 -> 2): isometry filter pins Hadamard up to gauge")
    M2 = demo_recombiner()
    print("\n3. Mach-Zehnder interferometer, end to end")
    demo_mach_zehnder(M1, M2)
    print("\n4. Negative cases (the filter and domain do real work)")
    demo_negative()
    print("=" * 68)


if __name__ == "__main__":
    demo()
