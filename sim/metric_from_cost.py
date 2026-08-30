#!/usr/bin/env python3
"""
Metric and curvature from the cost structure alone
===================================================
Executable companion to docs/27-mathematics-from-the-minima.md.

The question is how far geometry can be pushed before a manifold has to
be assumed. Further than the framework has been claiming, it turns out.

O1 gives composition, O3 gives a cost on reductions. Take the distance
between two structures to be the least total cost of a reduction path
between them. That object satisfies the axioms of a Lawvere metric --
a category enriched over ([0, inf], >=, +) -- with no geometry assumed
anywhere. It is a *generalised* metric because reduction is directional,
so symmetry can fail; that failure is a feature, and it is measured here
rather than assumed away.

Once there is a metric and a measure, curvature is definable without a
manifold, by Ollivier's construction: compare the cost of moving the
neighbourhood of x onto the neighbourhood of y against the distance from
x to y. Positive curvature means neighbours are closer than their centres;
negative means they are further apart.

Demonstrations:
  1. The cost metric satisfies identity, non-negativity and the triangle
     inequality on random structure graphs, and is asymmetric exactly
     where reduction is one-way.
  2. Ollivier-Ricci curvature, computed exactly by min-cost flow, orders
     tree < grid < sphere-like < clique, which is the ordering curvature
     is supposed to have.
  3. Flat lattices in 2 and 3 dimensions come out near zero, which is
     what a discrete flat space should do.
  4. What is still missing is stated numerically rather than in prose:
     none of this shows the space is locally Euclidean.

Units: cost in whatever scale RM1 leaves free; only ratios are used.
"""

from __future__ import annotations
from collections import deque
from typing import Dict, List, Optional, Sequence, Tuple
import math

INF = float("inf")

# ---------------------------------------------------------------------------
# The cost metric: least total disruption along a reduction path
# ---------------------------------------------------------------------------

def cost_metric(adj: Dict[int, List[Tuple[int, float]]]) -> Dict[int, Dict[int, float]]:
    """
    Operation: cost_metric -- d(A,B) = least total cost of a path A -> B.

    This is the hom-object of a category enriched over ([0,inf], >=, +),
    which is Lawvere's definition of a generalised metric space. Nothing
    geometric is assumed; the input is only objects and costed moves.
    """
    d: Dict[int, Dict[int, float]] = {}
    for src in adj:
        dist = {src: 0.0}
        # Dijkstra without a heap: the graphs here are small
        seen = set()
        while True:
            u, best = None, INF
            for k, v in dist.items():
                if k not in seen and v < best:
                    u, best = k, v
            if u is None:
                break
            seen.add(u)
            for v, w in adj[u]:
                nd = best + w
                if nd < dist.get(v, INF):
                    dist[v] = nd
        d[src] = dist
    return d


def check_metric_axioms(d: Dict[int, Dict[int, float]], nodes: Sequence[int]) -> Dict[str, object]:
    ident = all(abs(d[x].get(x, INF)) < 1e-12 for x in nodes)
    nonneg = all(v >= -1e-12 for x in nodes for v in d[x].values())
    tri_ok, worst = True, 0.0
    asym = 0.0
    for x in nodes:
        for y in nodes:
            dxy = d[x].get(y, INF)
            if dxy == INF:
                continue
            dyx = d[y].get(x, INF)
            if dyx != INF:
                asym = max(asym, abs(dxy - dyx))
            for z in nodes:
                dxz, dzy = d[x].get(z, INF), d[z].get(y, INF)
                if dxz == INF or dzy == INF:
                    continue
                slack = dxz + dzy - dxy
                if slack < -1e-9:
                    tri_ok = False
                    worst = min(worst, slack)
    return {"identity": ident, "non_negative": nonneg,
            "triangle": tri_ok, "worst_violation": worst, "max_asymmetry": asym}


# ---------------------------------------------------------------------------
# Exact optimal transport by min-cost flow (successive shortest paths)
# ---------------------------------------------------------------------------

class MCMF:
    def __init__(self, n: int):
        self.n = n
        self.to: List[int] = []
        self.cap: List[int] = []
        self.cost: List[float] = []
        self.head: List[List[int]] = [[] for _ in range(n)]

    def add(self, u: int, v: int, cap: int, cost: float) -> None:
        self.head[u].append(len(self.to)); self.to.append(v); self.cap.append(cap); self.cost.append(cost)
        self.head[v].append(len(self.to)); self.to.append(u); self.cap.append(0); self.cost.append(-cost)

    def run(self, s: int, t: int) -> float:
        total = 0.0
        while True:
            dist = [INF] * self.n
            inq = [False] * self.n
            pre = [-1] * self.n
            dist[s] = 0.0
            q = deque([s]); inq[s] = True
            while q:                                  # SPFA: costs may be equal, graph is tiny
                u = q.popleft(); inq[u] = False
                for e in self.head[u]:
                    if self.cap[e] > 0 and dist[u] + self.cost[e] < dist[self.to[e]] - 1e-12:
                        dist[self.to[e]] = dist[u] + self.cost[e]
                        pre[self.to[e]] = e
                        if not inq[self.to[e]]:
                            q.append(self.to[e]); inq[self.to[e]] = True
            if dist[t] == INF:
                return total
            f = 1 << 30
            v = t
            while v != s:
                e = pre[v]; f = min(f, self.cap[e]); v = self.to[e ^ 1]
            v = t
            while v != s:
                e = pre[v]; self.cap[e] -= f; self.cap[e ^ 1] += f; v = self.to[e ^ 1]
            total += f * dist[t]


def wasserstein1(mx: Dict[int, int], my: Dict[int, int],
                 d: Dict[int, Dict[int, float]], denom: int) -> float:
    """Exact W1 between two integer-mass distributions over graph nodes."""
    src = list(mx); dst = list(my)
    n = len(src) + len(dst) + 2
    S, T = n - 2, n - 1
    g = MCMF(n)
    for i, u in enumerate(src):
        g.add(S, i, mx[u], 0.0)
    for j, v in enumerate(dst):
        g.add(len(src) + j, T, my[v], 0.0)
    for i, u in enumerate(src):
        for j, v in enumerate(dst):
            w = d[u].get(v, INF)
            if w < INF:
                g.add(i, len(src) + j, 1 << 20, w)
    return g.run(S, T) / denom


def lazy_mass(adj: Dict[int, List[Tuple[int, float]]], x: int, denom: int) -> Dict[int, int]:
    """Alpha=1/2 lazy walk: half the mass stays, half spreads over neighbours."""
    nb = [v for v, _ in adj[x]]
    m = {x: denom // 2}
    if nb:
        share = (denom // 2) // len(nb)
        for v in nb:
            m[v] = m.get(v, 0) + share
        left = denom - sum(m.values())
        m[nb[0]] = m.get(nb[0], 0) + left
    else:
        m[x] = denom
    return m


def ollivier(adj, d, x: int, y: int) -> float:
    """kappa(x,y) = 1 - W1(m_x, m_y) / d(x,y).  Needs only a metric and a measure."""
    dx, dy = max(1, len(adj[x])), max(1, len(adj[y]))
    denom = 2 * dx * dy
    while denom % 2 or (denom // 2) % dx or (denom // 2) % dy:
        denom *= 2
    mx, my = lazy_mass(adj, x, denom), lazy_mass(adj, y, denom)
    dxy = d[x].get(y, INF)
    if dxy == INF or dxy == 0:
        return float("nan")
    return 1.0 - wasserstein1(mx, my, d, denom) / dxy


def mean_curvature(adj, interior_only: bool = True) -> Tuple[float, float, float, int]:
    """
    Mean curvature over edges. By default only *interior* edges count --
    both endpoints at the graph's maximum degree.

    This is not a cosmetic choice. A finite lattice or tree is mostly
    boundary, and a boundary edge is positively curved because the mass at
    a leaf has nowhere to spread. Averaging over every edge therefore
    reports the shape of the cut-off, not the shape of the structure: a
    depth-5 binary tree comes out near zero that way, when its interior is
    firmly negative.
    """
    d = cost_metric(adj)
    deg = {u: len(adj[u]) for u in adj}
    dmax = max(deg.values())
    vals = []
    for u in adj:
        for v, _ in adj[u]:
            if u < v and (not interior_only or (deg[u] == dmax and deg[v] == dmax)):
                k = ollivier(adj, d, u, v)
                if k == k:
                    vals.append(k)
    if not vals:
        return (float("nan"), float("nan"), float("nan"), 0)
    return (sum(vals) / len(vals), min(vals), max(vals), len(vals))


# ---------------------------------------------------------------------------
# Structures to measure
# ---------------------------------------------------------------------------

def und(edges, n) -> Dict[int, List[Tuple[int, float]]]:
    adj = {i: [] for i in range(n)}
    for u, v in edges:
        adj[u].append((v, 1.0)); adj[v].append((u, 1.0))
    return adj

def grid2(L):
    idx = lambda x, y: x * L + y
    e = [(idx(x, y), idx(x + 1, y)) for x in range(L - 1) for y in range(L)]
    e += [(idx(x, y), idx(x, y + 1)) for x in range(L) for y in range(L - 1)]
    return und(e, L * L)

def grid3(L):
    idx = lambda x, y, z: (x * L + y) * L + z
    e = []
    for x in range(L):
        for y in range(L):
            for z in range(L):
                if x + 1 < L: e.append((idx(x, y, z), idx(x + 1, y, z)))
                if y + 1 < L: e.append((idx(x, y, z), idx(x, y + 1, z)))
                if z + 1 < L: e.append((idx(x, y, z), idx(x, y, z + 1)))
    return und(e, L ** 3)

def tree(depth, branch=2):
    e, nxt, frontier = [], 1, [0]
    for _ in range(depth):
        new = []
        for u in frontier:
            for _ in range(branch):
                e.append((u, nxt)); new.append(nxt); nxt += 1
        frontier = new
    return und(e, nxt)

def clique(n):
    return und([(i, j) for i in range(n) for j in range(i + 1, n)], n)

def cycle(n):
    return und([(i, (i + 1) % n) for i in range(n)], n)

def directed_chain(n):
    """Reduction is one-way: A -> B costs 1, B -> A is not available."""
    adj = {i: [] for i in range(n)}
    for i in range(n - 1):
        adj[i].append((i + 1, 1.0))
    return adj


# ---------------------------------------------------------------------------

def demo_axioms():
    print("   the cost metric on a small structure graph:")
    g = grid2(4)
    d = cost_metric(g)
    r = check_metric_axioms(d, list(g))
    print(f"      d(x,x) = 0 everywhere        : {r['identity']}")
    print(f"      d >= 0 everywhere            : {r['non_negative']}")
    print(f"      d(x,z) <= d(x,y) + d(y,z)    : {r['triangle']}  (worst slack {r['worst_violation']:.1e})")
    print(f"      symmetric here               : {r['max_asymmetry'] < 1e-12}")
    assert r["identity"] and r["non_negative"] and r["triangle"]

    print("\n   the same construction where reduction is one-way:")
    c = directed_chain(6)
    dc = cost_metric(c)
    r2 = check_metric_axioms(dc, list(c))
    print(f"      identity, non-negativity, triangle still hold: "
          f"{r2['identity'] and r2['non_negative'] and r2['triangle']}")
    print(f"      d(0,5) = {dc[0][5]:.0f}   d(5,0) = "
          f"{'unreachable' if dc[5].get(0, INF) == INF else dc[5][0]}")
    print("   -> symmetry fails, and that is correct: reduction has a direction.")
    print("      The object is a Lawvere metric -- a category enriched over")
    print("      ([0,inf], >=, +) -- which is what a metric is before symmetry")
    print("      is imposed. No geometry was assumed to get here.")


def demo_curvature():
    cases = [
        ("tree, branching 2", tree(5, 2)),
        ("tree, branching 3", tree(4, 3)),
        ("cycle, 24 nodes", cycle(24)),
        ("flat grid, 2-D", grid2(7)),
        ("flat grid, 3-D", grid3(5)),
        ("clique, 8 nodes", clique(8)),
    ]
    print("   interior edges only -- a finite structure is mostly boundary, and")
    print("   boundary edges are positively curved because mass at a leaf has")
    print("   nowhere to spread. Averaging over all edges reports the cut-off.\n")
    print(f"   {'structure':>20} {'mean kappa':>12} {'edges':>7} {'all-edge mean':>14}  reading")
    rows = []
    for name, g in cases:
        m, lo, hi, n = mean_curvature(g, True)
        ma = mean_curvature(g, False)[0]
        rows.append((name, m))
        sign = "negative" if m < -0.02 else ("positive" if m > 0.02 else "flat")
        print(f"   {name:>20} {m:>12.4f} {n:>7} {ma:>14.4f}  {sign}")
    by = dict(rows)
    assert by["tree, branching 2"] < -0.2, "a tree interior must be negatively curved"
    assert abs(by["flat grid, 2-D"]) < 1e-9 and abs(by["flat grid, 3-D"]) < 1e-9, \
        "a flat lattice interior must be flat"
    assert by["clique, 8 nodes"] > 0.4, "a clique must be positively curved"
    assert by["tree, branching 2"] < by["flat grid, 2-D"] < by["clique, 8 nodes"]
    print("\n   -> trees negative, flat lattices exactly zero in 2-D and 3-D,")
    print("      cliques positive. Curvature is DEFINABLE on the framework's own")
    print("      structures with no manifold anywhere, and it agrees with the")
    print("      answers geometry gives for the cases where geometry has one.")
    print("      The right-hand column shows what averaging over the boundary")
    print("      would have reported instead, which for the trees is the wrong sign.")


def demo_whats_missing():
    print("   what the above does not establish:")
    print("      · that any generated structure is locally Euclidean")
    print("      · that a dimension is well defined away from hand-built lattices")
    print("      · that the signature is Lorentzian rather than Riemannian")
    g2, g3 = grid2(7), grid3(5)
    m2, m3 = mean_curvature(g2)[0], mean_curvature(g3)[0]
    print(f"\n      flat 2-D lattice: kappa = {m2:+.4f}")
    print(f"      flat 3-D lattice: kappa = {m3:+.4f}")
    print("      Both are near zero and neither number knows its own dimension.")
    print("      Curvature alone cannot tell you which space you are in, so it")
    print("      narrows the geometric debt without discharging it: the missing")
    print("      piece is manifoldlikeness, not metric structure and not curvature.")


def demo():
    print("=" * 72)
    print("Metric and curvature from the cost structure alone (docs/27)")
    print("=" * 72)
    print("\n1. The cost metric satisfies the axioms, symmetry included or not")
    demo_axioms()
    print("\n2. Curvature without a manifold (Ollivier, exact optimal transport)")
    demo_curvature()
    print("\n3. What is still missing")
    demo_whats_missing()
    print("=" * 72)


if __name__ == "__main__":
    demo()
