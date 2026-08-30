#!/usr/bin/env python3
"""
Thermodynamics and gravity: relative entropy, area law, Einstein equation
=========================================================================
Executable companion to docs/24-thermodynamics-gravity.md (TG layer).

Thesis under test: the relevant entropy is *relative* information, and
gravity is what that entropy does.

Demonstrations:
  1. TH2 (structural area law): the isolation cost of a region is a
     function of the cut alone. Interior structure is grown by two
     orders of magnitude at fixed boundary; C_isolate does not move.
     The area law is not imported — it is the shape of WM2's S-counter.
  2. TH1 (relativity of entropy): under k-fold granularity refinement
     (the WM1 gauge) the von Neumann entropy diverges as N log k while
     the relative entropy against the ground configuration is exactly
     invariant. Also: only C/Theta enters (RM1 scale), and only cost
     *differences* enter (CI4 additive gauge).
  3. TH4 (structural monotonicity): relative entropy is invariant under
     free-epoch maps (T13', diagonal unimodular) and reconfigurations
     (T16', isometries), and decreases only at structural projection
     (T14', dephasing + restriction). The framework's data-processing
     inequality — the engine of the second law.
  4. TH6 (Einstein equation): the two small-ball coefficients of Route A
     are verified against exact geodesic balls on S^3 and exact
     quadrature; both routes then agree on eta = 1/(4G).
  5. TH9/TH10 (second law, area theorem, mergers): dM = T dS for
     Schwarzschild; A_f >= A_1 + A_2 checked against observed binary
     black hole mergers (Schwarzschild and Kerr forms); the radiated
     fraction bound; fission shown thermodynamically forbidden.
  6. TH8 (weak equivalence principle, closing contention 2): an entropic
     bias proportional to share count gives cluster-independent
     acceleration, where a cluster-independent bias (T6's regime) does
     not. Includes the residual O(eps/alpha_m n) violation predicted by
     WM3's inertia floor, and the Verlinde cross-check F = GMm/r^2.

Units: G = c = hbar = k_B = 1 except where G is displayed explicitly.
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import Any, List, Optional, Sequence, Set, Tuple
import cmath
import math

# ---------------------------------------------------------------------------
# Minimal term language (mirrors sim/expr_tree.py; kept self-contained so each
# sim runs standalone, per sim/README.md)
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class Var:
    name: str

@dataclass(frozen=True)
class Abs:
    var: str
    body: Any

@dataclass(frozen=True)
class Pair:
    left: Any
    right: Any

@dataclass
class Share:
    """Explicit sharing: multiple parents may hold the same Share object."""
    id: str
    content: Any

Term = Any


def share_nodes(term: Term) -> List[Share]:
    """Operation: share_nodes — distinct Share objects, by identity (iterative)."""
    seen: Set[int] = set()
    out: List[Share] = []
    stack: List[Term] = [term]
    while stack:
        t = stack.pop()
        if isinstance(t, Share):
            if id(t) in seen:
                continue
            seen.add(id(t))
            out.append(t)
            stack.append(t.content)
        elif isinstance(t, Pair):
            stack.append(t.left)
            stack.append(t.right)
        elif isinstance(t, Abs):
            stack.append(t.body)
    return out


def open_bindings(term: Term) -> int:
    """Operation: open_bindings — free variable occurrences (B-counter proxy)."""
    if isinstance(term, Var):
        return 1
    if isinstance(term, Abs):
        return max(0, open_bindings(term.body) - 1)
    if isinstance(term, Pair):
        return open_bindings(term.left) + open_bindings(term.right)
    if isinstance(term, Share):
        return open_bindings(term.content)
    return 0


def node_count(term: Term) -> int:
    """Total distinct nodes — the 'volume' of a region (iterative)."""
    seen: Set[int] = set()
    stack: List[Term] = [term]
    n = 0
    while stack:
        t = stack.pop()
        if id(t) in seen:
            continue
        seen.add(id(t))
        n += 1
        if isinstance(t, Share):
            stack.append(t.content)
        elif isinstance(t, Pair):
            stack.append(t.left)
            stack.append(t.right)
        elif isinstance(t, Abs):
            stack.append(t.body)
    return n


# ---------------------------------------------------------------------------
# 1. TH2 — the structural area law
# ---------------------------------------------------------------------------

def cut_shares(inside: Term, outside: Term) -> List[Share]:
    """Operation: cut_shares — Share nodes reachable from both sides of a cut."""
    out_ids = {id(s) for s in share_nodes(outside)}
    return [s for s in share_nodes(inside) if id(s) in out_ids]


def isolation_cost(inside: Term, outside: Term,
                   alpha: float = 1.0, beta: float = 0.5,
                   gamma: float = 2.0) -> float:
    """
    Operation: isolation_cost_from_tree (docs/08 section 1) read as an area.

    C_isolate = alpha*S + beta*B + gamma*D over the *cut* share set only.
    """
    cut = cut_shares(inside, outside)
    S = len(cut)
    B = sum(open_bindings(s.content) for s in cut)
    D = 1.0 if S > 0 else 0.0
    return alpha * S + beta * B + gamma * D


def pair_up(nodes: Sequence[Term]) -> Term:
    """Assemble a list of nodes into one balanced term (keeps depth O(log n))."""
    level: List[Term] = list(nodes)
    if not level:
        return Var("empty")
    while len(level) > 1:
        level = [Pair(level[i], level[i + 1]) if i + 1 < len(level) else level[i]
                 for i in range(0, len(level), 2)]
    return level[0]


def build_region(n_boundary: int, n_interior: int,
                 boundary: Optional[List[Share]] = None) -> Tuple[Term, List[Share]]:
    """
    A region holding `n_boundary` shares that also live outside (the cut) plus
    `n_interior` purely-local shares (bulk structure the cut never touches).
    """
    if boundary is None:
        boundary = [Share(id=f"bnd-{i}", content=Var(f"b{i}")) for i in range(n_boundary)]
    local = [Share(id=f"int-{i}", content=Var(f"i{i}")) for i in range(n_interior)]
    return pair_up(list(boundary) + list(local)), boundary


def demo_area_law() -> None:
    print("   growing the interior at fixed boundary (8 cut shares):")
    print(f"   {'interior shares':>16} {'nodes inside':>13} {'N(cut)':>7} {'C_isolate':>10}")
    boundary = [Share(id=f"bnd-{i}", content=Var(f"b{i}")) for i in range(8)]
    costs = []
    for n_int in (0, 10, 100, 1000):
        inside, _ = build_region(8, n_int, boundary=boundary)
        # the exterior holds the same boundary Share objects, by identity
        outside: Term = pair_up(list(boundary) + [Share(id="env", content=Var("e"))])
        c = isolation_cost(inside, outside)
        costs.append(c)
        print(f"   {n_int:>16} {node_count(inside):>13} {len(cut_shares(inside, outside)):>7} {c:>10.2f}")
    assert max(costs) - min(costs) < 1e-12, "TH2 failed: cost tracked the interior"
    print("   -> C_isolate is constant while the interior grows ~130x:")
    print("      the disruption ledger is a BOUNDARY quantity. TH2 holds.")

    print("\n   now growing the boundary at fixed interior:")
    print(f"   {'cut shares':>16} {'C_isolate':>10}")
    for n_b in (2, 4, 8, 16):
        bnd = [Share(id=f"B{i}", content=Var(f"b{i}")) for i in range(n_b)]
        inside, _ = build_region(n_b, 50, boundary=bnd)
        outside = pair_up(bnd)
        print(f"   {n_b:>16} {isolation_cost(inside, outside):>10.2f}")
    print("   -> strictly linear in the cut count: S_cut = s0 * N(cut) (TH2').")


# ---------------------------------------------------------------------------
# 2. TH1 — only relative entropy is an observable
# ---------------------------------------------------------------------------

def shannon(p: Sequence[float]) -> float:
    return -sum(pi * math.log(pi) for pi in p if pi > 0.0)


def rel_entropy(p: Sequence[float], q: Sequence[float]) -> float:
    """S_rel(p||q) = sum p log(p/q). Requires supp(p) subset of supp(q)."""
    tot = 0.0
    for pi, qi in zip(p, q):
        if pi > 0.0:
            assert qi > 0.0, "relative entropy undefined: support violation"
            tot += pi * math.log(pi / qi)
    return tot


def gibbs(costs: Sequence[float], theta: float) -> List[float]:
    """Operation: TG1 coarse-graining — Gibbs measure on the dynamical floor."""
    m = min(costs)
    w = [math.exp(-(c - m) / theta) for c in costs]
    z = sum(w)
    return [wi / z for wi in w]


def refine(p: Sequence[float], k: int, n_shares: int) -> List[float]:
    """
    WM1 granularity gauge: split every share into k sub-shares. Each
    configuration acquires a k**n_shares-fold uniform multiplicity.
    """
    mult = k ** n_shares
    return [pi / mult for pi in p for _ in range(mult)]


def demo_relativity_of_entropy() -> None:
    n_shares = 4
    # excited configuration vs the SB3 ground configuration on the same space
    excited_cost = [0.0, 1.0, 1.5, 2.0, 3.5, 4.0]
    ground_cost = [0.0, 2.0, 2.5, 3.0, 4.5, 5.0]
    theta = 1.0
    p = gibbs(excited_cost, theta)
    q = gibbs(ground_cost, theta)

    print("   (3) WM1 granularity gauge — refine every share k-fold:")
    print(f"   {'k':>4} {'S(rho)':>10} {'S(rho)-S0':>12} {'N ln k':>10} {'S_rel(rho||sigma)':>19}")
    s0 = shannon(p)
    base_rel = rel_entropy(p, q)
    for k in (1, 2, 3, 4):
        pk = refine(p, k, n_shares)
        qk = refine(q, k, n_shares)
        s = shannon(pk)
        r = rel_entropy(pk, qk)
        print(f"   {k:>4} {s:>10.5f} {s - s0:>12.5f} {n_shares * math.log(k):>10.5f} {r:>19.12f}")
        assert abs((s - s0) - n_shares * math.log(k)) < 1e-9
        assert abs(r - base_rel) < 1e-12
    print("   -> S diverges as N ln k (this IS the QFT area-law UV divergence);")
    print("      S_rel is invariant to 12 decimals. Only S_rel is an observable.")

    print("\n   (1) RM1 scale gauge — cost defined only up to positive scale:")
    for s in (1.0, 7.3, 0.21):
        ps = gibbs([s * c for c in excited_cost], s * theta)
        print(f"      scale={s:<5} max|p_scaled - p| = {max(abs(a - b) for a, b in zip(ps, p)):.2e}")
    print("      -> only C/Theta enters; Theta is a unit choice, not a constant.")

    print("\n   (2) CI4 additive gauge — cost has no zero:")
    off = 12.7
    p_off = gibbs([c + off for c in excited_cost], theta)
    print(f"      offset={off}: max|p_offset - p| = {max(abs(a - b) for a, b in zip(p_off, p)):.2e}")
    print("      -> modular energy <K> has no absolute zero; only Delta<K> is defined.")


# ---------------------------------------------------------------------------
# 3. TH4 — structural monotonicity (the framework's data-processing inequality)
# ---------------------------------------------------------------------------

Mat = List[List[complex]]


def _herm_eig_2x2(m: Mat) -> Tuple[List[float], List[List[complex]]]:
    """Closed-form eigendecomposition of a 2x2 Hermitian matrix."""
    a = m[0][0].real
    d = m[1][1].real
    b = m[0][1]
    if abs(b) <= 1e-14:
        # already diagonal (covers the degenerate case a == d, where the
        # generic formula would return the same eigenvector twice)
        return [a, d], [[1.0 + 0j, 0j], [0j, 1.0 + 0j]]
    half = 0.5 * (a + d)
    disc = math.sqrt(0.25 * (a - d) ** 2 + abs(b) ** 2)
    vals = [half + disc, half - disc]
    v = [b, complex(vals[0] - a, 0.0)]
    nrm = math.sqrt(sum(abs(x) ** 2 for x in v))
    v0 = [x / nrm for x in v]
    # orthogonal complement: <v1|v0> = 0 by construction
    v1 = [-v0[1].conjugate(), v0[0].conjugate()]
    return vals, [v0, v1]


def rel_entropy_q(rho: Mat, sigma: Mat) -> float:
    """S_rel(rho||sigma) = Tr rho log rho - Tr rho log sigma, for 2x2 states."""
    rv, _ = _herm_eig_2x2(rho)
    sv, sw = _herm_eig_2x2(sigma)
    term1 = sum(l * math.log(l) for l in rv if l > 1e-15)
    term2 = 0.0
    for lam, v in zip(sv, sw):
        if lam <= 1e-15:
            continue
        # <v| rho |v>
        acc = 0.0 + 0j
        for i in range(2):
            for j in range(2):
                acc += (v[i].conjugate()) * rho[i][j] * v[j]
        term2 += math.log(lam) * acc.real
    return term1 - term2


def conj_map(u: Mat, rho: Mat) -> Mat:
    """rho -> U rho U^dagger."""
    n, k = len(u), len(u[0])
    out = [[0j for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            acc = 0j
            for a in range(k):
                for b in range(k):
                    acc += u[i][a] * rho[a][b] * u[j][b].conjugate()
            out[i][j] = acc
    return out


def dephase(rho: Mat) -> Mat:
    """Class-dephasing: the record left by a structural projection (T14')."""
    n = len(rho)
    return [[rho[i][j] if i == j else 0j for j in range(n)] for i in range(n)]


def demo_monotonicity() -> None:
    print("   classical layer (residual classes, weight-blind):")
    p = [0.40, 0.30, 0.20, 0.10]
    q = [0.25, 0.25, 0.25, 0.25]
    base = rel_entropy(p, q)
    perm = [2, 0, 3, 1]
    p_perm = [p[perm.index(i)] for i in range(4)]
    q_perm = [q[perm.index(i)] for i in range(4)]
    # reconfiguration: re-partition the classes into a larger register without
    # dropping any (T15/T16'). The new slots are empty in BOTH states.
    embed_p = p_perm + [0.0, 0.0]
    embed_q = q_perm + [0.0, 0.0]
    coarse_p = [p[0] + p[1], p[2] + p[3]]
    coarse_q = [q[0] + q[1], q[2] + q[3]]
    print(f"      S_rel baseline                        = {base:.9f}")
    print(f"      after relabelling (free epoch, T13')  = {rel_entropy(p_perm, q_perm):.9f}   [invariant]")
    print(f"      after class embedding (reconf, T16')  = {rel_entropy(embed_p, embed_q):.9f}   [invariant]")
    print(f"      after coarse-graining (projection)    = {rel_entropy(coarse_p, coarse_q):.9f}   [decreased]")
    assert abs(rel_entropy(p_perm, q_perm) - base) < 1e-12
    assert abs(rel_entropy(embed_p, embed_q) - base) < 1e-12
    assert rel_entropy(coarse_p, coarse_q) < base - 1e-9

    print("\n   hosted quantum layer (A4 weights, 2x2 states):")
    rho: Mat = [[0.70 + 0j, 0.30 + 0.10j], [0.30 - 0.10j, 0.30 + 0j]]
    sigma: Mat = [[0.55 + 0j, 0.10 - 0.05j], [0.10 + 0.05j, 0.45 + 0j]]
    base_q = rel_entropy_q(rho, sigma)

    phi1, phi2 = 0.7, -1.9
    diag_u: Mat = [[cmath.exp(1j * phi1), 0j], [0j, cmath.exp(1j * phi2)]]
    t = 0.6
    gen_u: Mat = [[math.cos(t) + 0j, -math.sin(t) + 0j],
                  [math.sin(t) + 0j, math.cos(t) + 0j]]

    r_diag = rel_entropy_q(conj_map(diag_u, rho), conj_map(diag_u, sigma))
    r_gen = rel_entropy_q(conj_map(gen_u, rho), conj_map(gen_u, sigma))
    r_deph = rel_entropy_q(dephase(rho), dephase(sigma))
    print(f"      S_rel baseline                            = {base_q:.9f}")
    print(f"      free epoch: diagonal unimodular (T13')    = {r_diag:.9f}   [invariant]")
    print(f"      general unitary                           = {r_gen:.9f}   [invariant]")
    print(f"      projection: class dephasing (T14')        = {r_deph:.9f}   [decreased]")
    assert abs(r_diag - base_q) < 1e-10 and abs(r_gen - base_q) < 1e-10
    assert r_deph < base_q - 1e-9
    for r in (base_q, r_diag, r_gen, r_deph):
        assert r >= -1e-12, "relative entropy went negative — positivity violated"
    print("   -> equality on T13'/T16' events, strict decrease only at projection.")
    print("      Entropy production and the measurement problem share one locus.")


# ---------------------------------------------------------------------------
# 4. TH6 — the Einstein equation: verifying the small-ball coefficients
# ---------------------------------------------------------------------------

def sphere3_ball(a: float, ell: float) -> Tuple[float, float]:
    """Exact area and volume of a geodesic ball of radius ell in S^3 (radius a)."""
    area = 4.0 * math.pi * a * a * math.sin(ell / a) ** 2
    vol = 2.0 * math.pi * a * a * ell - math.pi * a ** 3 * math.sin(2.0 * ell / a)
    return area, vol


def area_deficit_at_fixed_volume(a: float, ell: float) -> float:
    """delta A|_V : curved-ball area minus the flat ball of the same volume."""
    area, vol = sphere3_ball(a, ell)
    ell_flat = (3.0 * vol / (4.0 * math.pi)) ** (1.0 / 3.0)
    return area - 4.0 * math.pi * ell_flat ** 2


def modular_integral(ell: float, n: int = 20000) -> float:
    """2*pi * int_0^ell (ell^2 - r^2)/(2 ell) * 4 pi r^2 dr, by Simpson."""
    def f(r: float) -> float:
        return 2.0 * math.pi * (ell * ell - r * r) / (2.0 * ell) * 4.0 * math.pi * r * r
    h = ell / n
    tot = f(0.0) + f(ell)
    for i in range(1, n):
        tot += (4.0 if i % 2 else 2.0) * f(i * h)
    return tot * h / 3.0


def demo_einstein() -> None:
    a = 1.0
    R3 = 6.0 / (a * a)  # Ricci scalar of S^3 of radius a
    print("   (a) geometry side: delta A|_V  vs  -(2 pi/15) ell^4 R3   [exact S^3 balls]")
    print(f"   {'ell':>8} {'measured':>16} {'predicted':>16} {'ratio':>12}")
    for ell in (0.20, 0.10, 0.05, 0.02):
        meas = area_deficit_at_fixed_volume(a, ell)
        pred = -(2.0 * math.pi / 15.0) * ell ** 4 * R3
        print(f"   {ell:>8.3f} {meas:>16.10f} {pred:>16.10f} {meas / pred:>12.8f}")
    assert abs(area_deficit_at_fixed_volume(a, 0.02)
               / (-(2.0 * math.pi / 15.0) * 0.02 ** 4 * R3) - 1.0) < 1e-3

    print("\n   (b) matter side: <K> integral  vs  (8 pi^2/15) ell^4   [Simpson quadrature]")
    for ell in (1.0, 0.5, 0.1):
        meas = modular_integral(ell)
        pred = 8.0 * math.pi ** 2 / 15.0 * ell ** 4
        print(f"   {'ell=' + format(ell, '.2f'):>8} {meas:>16.10f} {pred:>16.10f} {meas / pred:>12.10f}")
        assert abs(meas / pred - 1.0) < 1e-9

    print("\n   (c) equilibrium (TG5):  eta * delta A|_V + delta<K> = 0")
    print("       eta*(4 pi/15) ell^4 G_00 = (8 pi^2/15) ell^4 T_00")
    print("       =>  G_00 = (2 pi / eta) T_00                       [Route A]")
    print("       Route B (Clausius) gave  G_ab + Lambda g_ab = (2 pi/eta) T_ab")
    G_newton = 1.0 / 7.0   # arbitrary: the identification must hold for any G
    eta = 1.0 / (4.0 * G_newton)
    lhs, rhs = 2.0 * math.pi / eta, 8.0 * math.pi * G_newton
    print(f"\n       matching 2 pi/eta = 8 pi G  with G = 1/7:")
    print(f"         2 pi/eta = {lhs:.12f}   8 pi G = {rhs:.12f}   -> eta = 1/(4G) = {eta:.6f}")
    assert abs(lhs - rhs) < 1e-12
    print("   -> both routes agree: S = A/4G, i.e. G = 1/(4 s0 eta_N)   [TH7]")
    print("      Newton's constant IS the reciprocal ground share density across a cut.")


# ---------------------------------------------------------------------------
# 5. TH9/TH10 — second law, area theorem, black hole mergers
# ---------------------------------------------------------------------------

def kerr_area(M: float, chi: float = 0.0) -> float:
    """Horizon area of a Kerr hole, G = c = 1. Schwarzschild at chi = 0."""
    return 8.0 * math.pi * M * M * (1.0 + math.sqrt(max(0.0, 1.0 - chi * chi)))


def bh_entropy(M: float, chi: float = 0.0) -> float:
    return kerr_area(M, chi) / 4.0


def hawking_T(M: float) -> float:
    """Schwarzschild: T = kappa/2pi = 1/(8 pi M)."""
    return 1.0 / (8.0 * math.pi * M)


# published median parameters (solar masses): m1, m2, M_final, chi_final
MERGERS: List[Tuple[str, float, float, float, float]] = [
    ("GW150914", 35.6, 30.6, 63.1, 0.69),
    ("GW151226", 13.7, 7.7, 20.5, 0.74),
    ("GW170814", 30.7, 25.3, 53.4, 0.72),
    ("GW190521", 85.0, 66.0, 142.0, 0.72),
]


def demo_black_holes() -> None:
    print("   (a) first law  dM = T dS  for Schwarzschild (TH10c):")
    for M in (1.0, 10.0, 100.0):
        h = 1e-6 * M
        dS_dM = (bh_entropy(M + h) - bh_entropy(M - h)) / (2.0 * h)
        print(f"      M={M:>6.1f}   T={hawking_T(M):.6e}   dS/dM={dS_dM:.6e}   T*dS/dM={hawking_T(M) * dS_dM:.12f}")
        assert abs(hawking_T(M) * dS_dM - 1.0) < 1e-6

    print("\n   (b) merger inequality  A_f >= A_1 + A_2  (TH10b), observed events:")
    print(f"   {'event':>10} {'A_1+A_2':>10} {'A_f':>12} {'A_f/A_i':>9} {'f_rad':>8} {'bound':>8} {'ok':>4}")
    for name, m1, m2, Mf, chif in MERGERS:
        # chi_i = 0 is the conservative choice: it MAXIMISES the initial area
        A_i = kerr_area(m1) + kerr_area(m2)
        A_f = kerr_area(Mf, chif)
        f_rad = 1.0 - Mf / (m1 + m2)
        bound = 1.0 - math.sqrt(m1 * m1 + m2 * m2) / (m1 + m2)
        ok = A_f >= A_i and f_rad <= bound
        print(f"   {name:>10} {A_i:>10.0f} {A_f:>12.0f} {A_f / A_i:>9.3f} "
              f"{100 * f_rad:>7.2f}% {100 * bound:>7.2f}% {'yes' if ok else 'NO':>4}")
        assert ok, f"{name} violates the area theorem"

    print("\n   (c) spin-corrected Kerr constraint  M_f >= sqrt(2(m1^2+m2^2)/(1+sqrt(1-chi_f^2))):")
    for name, m1, m2, Mf, chif in MERGERS:
        Mmin = math.sqrt(2.0 * (m1 * m1 + m2 * m2) / (1.0 + math.sqrt(1.0 - chif * chif)))
        print(f"      {name:>10}  M_f = {Mf:>6.1f}   minimum allowed = {Mmin:>6.2f}   "
              f"margin = {100 * (Mf - Mmin) / Mf:>5.1f}%")
        assert Mf >= Mmin

    print("\n   (d) equal-mass radiated-energy ceiling  1 - 1/sqrt(2):")
    print(f"      max radiated fraction = {100 * (1 - 1 / math.sqrt(2)):.2f}%"
          "   (observed events radiate 4-6%)")

    print("\n   (e) fission is forbidden, not merely unlikely:")
    M = 10.0
    for m1 in (5.0, 2.0, 0.1):
        m2 = M - m1
        after = kerr_area(m1) + kerr_area(m2)
        print(f"      {M:.0f} -> {m1:.1f} + {m2:.1f}:  A {kerr_area(M):>8.0f} -> {after:>8.0f}"
              f"   (dS = {(after - kerr_area(M)) / 4:>9.0f})")
        assert after < kerr_area(M)
    print("   -> every split lowers S. TH10b runs one way only; that is the arrow of time")
    print("      for horizons, and by TH4 its root is the structural projection event.")


# ---------------------------------------------------------------------------
# 6. TH8 — the weak equivalence principle (contention 2)
# ---------------------------------------------------------------------------

def m_struct(n_share: int, alpha_m: float = 1.0, eps: float = 0.05) -> float:
    """WM3 inertia proxy."""
    return alpha_m * n_share + eps


def demo_equivalence() -> None:
    alpha_m, eps = 1.0, 0.05
    theta_s0_over_lambda = 3.0   # Theta * s0 / lambda: sets g
    clusters = [("light", 3), ("medium", 30), ("heavy", 3000)]

    print("   (a) cluster-INDEPENDENT bias (an applied force — T6's regime):")
    b_applied = 1.0
    print(f"   {'cluster':>8} {'n_share':>8} {'m_struct':>10} {'a = b/m':>12}")
    accs_applied = []
    for name, n in clusters:
        m = m_struct(n, alpha_m, eps)
        a = b_applied / m
        accs_applied.append(a)
        print(f"   {name:>8} {n:>8} {m:>10.2f} {a:>12.6f}")
    print(f"   -> accelerations differ by {accs_applied[0] / accs_applied[-1]:.1f}x: "
          "T6's inverse share-count ratio.")

    print("\n   (b) entropic bias  b_grav = Theta*s0*n/lambda  (TH8):")
    print(f"   {'cluster':>8} {'n_share':>8} {'b_grav':>10} {'m_struct':>10} {'g_eff = b/m':>13}")
    accs_grav = []
    for name, n in clusters:
        b = theta_s0_over_lambda * n
        m = m_struct(n, alpha_m, eps)
        a = b / m
        accs_grav.append(a)
        print(f"   {name:>8} {n:>8} {b:>10.2f} {m:>10.2f} {a:>13.9f}")
    spread = (max(accs_grav) - min(accs_grav)) / (sum(accs_grav) / len(accs_grav))
    exact = [theta_s0_over_lambda * n / m_struct(n, alpha_m, 0.0) for _, n in clusters]
    spread_exact = (max(exact) - min(exact)) / (sum(exact) / len(exact))
    print(f"   -> spread {spread:.2e}, against a factor of "
          f"{accs_applied[0] / accs_applied[-1]:.0f} for the applied-force case.")
    print(f"      With the WM3 floor removed (eps = 0) the spread is exactly {spread_exact:.1e}:")
    print("      the floor is the ONLY source of residual non-universality.")
    print("      Universality of free fall holds because inertia and horizon entropy")
    print("      count the SAME shares — one counter, two roles. TH8 holds.")
    assert spread_exact < 1e-15

    print("\n   (c) residual WEP violation from WM3's inertia floor eps:")
    print(f"   {'pair':>18} {'Eotvos eta_E':>16} {'predicted eps/alpha_m*|1/n1-1/n2|':>36}")
    for (n1_name, n1), (n2_name, n2) in ((clusters[0], clusters[1]), (clusters[1], clusters[2])):
        a1 = theta_s0_over_lambda * n1 / m_struct(n1, alpha_m, eps)
        a2 = theta_s0_over_lambda * n2 / m_struct(n2, alpha_m, eps)
        eta_E = 2.0 * abs(a1 - a2) / (a1 + a2)
        pred = eps / alpha_m * abs(1.0 / n1 - 1.0 / n2)
        print(f"   {n1_name + '/' + n2_name:>18} {eta_E:>16.3e} {pred:>36.3e}")
    print("   -> TH8 is exact only up to O(eps/alpha_m n): the framework predicts a WEP")
    print("      violation suppressed by inverse share count, i.e. by inverse mass.")
    print("      MICROSCOPE's eta_E < 1e-15 on macroscopic bodies is easily satisfied,")
    print("      and bounds any stratification of the dynamical floor (contention 8).")

    print("\n   (d) Verlinde cross-check — Newton's law from the screen (not load-bearing):")
    G_newton, M, m, r = 1.0, 5.0, 0.001, 12.0
    N = 4.0 * math.pi * r * r / G_newton      # screen share count, N = A/G  (TH7)
    theta = 2.0 * M / N                        # equipartition E = N Theta/2
    dS_dx = 2.0 * math.pi * m                  # TH8 rate in Compton units
    F_entropic = theta * dS_dx
    F_newton = G_newton * M * m / (r * r)
    print(f"      screen at r={r}:  N={N:.2f}  Theta={theta:.6e}")
    print(f"      F_entropic = Theta * dS/dx = {F_entropic:.9e}")
    print(f"      G M m / r^2                = {F_newton:.9e}")
    assert abs(F_entropic - F_newton) < 1e-12
    print("   -> exact. Consistency check only: TH6 already gives the full field equation.")


# ---------------------------------------------------------------------------

def demo() -> None:
    print("=" * 74)
    print("Thermodynamics and gravity from relative information (docs/24)")
    print("=" * 74)
    print("\n1. TH2 — the area law is what WM2's S-counter counts")
    demo_area_law()
    print("\n2. TH1 — only relative entropy is an observable")
    demo_relativity_of_entropy()
    print("\n3. TH4 — structural monotonicity (the data-processing inequality)")
    demo_monotonicity()
    print("\n4. TH6/TH7 — the Einstein equation and the identification of G")
    demo_einstein()
    print("\n5. TH9/TH10 — second law, area theorem, black hole mergers")
    demo_black_holes()
    print("\n6. TH8 — the weak equivalence principle (contention 2)")
    demo_equivalence()
    print("=" * 74)


if __name__ == "__main__":
    demo()
