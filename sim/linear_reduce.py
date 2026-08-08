#!/usr/bin/env python3
"""
Linear reduce + free-epoch unitary weight dynamics
==================================================
Implements:
  - share_weight / linear residual algebra
  - R formalization: share-preserving invertible weight maps
  - N formalization: no relative-modulus change in free epochs
  - free-epoch unitary updates (diagonal phase and general U(n))
  - structural projection (non-unitary locus)

See docs/12-RN-formalization.md and docs/10-unitarity-from-projection.md.

Note (docs/17): N* applies to fixed-decomposition (free-epoch) updates
only. A modulus-changing map is not a free-epoch update — it corresponds
to a reconfiguration event (T15), whose induced map must be an isometry
(T16). The general-matrix step below WARNS when a proposal changes
relative moduli, so misuse as a free-epoch map stays visible.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional, Sequence, Set, Tuple
import cmath
import math
import random

# ---------------------------------------------------------------------------
# Weight vector utilities (R / N predicates)
# ---------------------------------------------------------------------------

def relative_moduli(weights: Sequence[complex]) -> Tuple[float, ...]:
    """D16: μ_i = |a_i| / ||a||_2"""
    norms = [abs(w) for w in weights]
    total = math.sqrt(sum(n * n for n in norms)) or 1.0
    return tuple(n / total for n in norms)

def moduli_equal(m1: Sequence[float], m2: Sequence[float], eps: float = 1e-9) -> bool:
    if len(m1) != len(m2):
        return False
    return all(abs(a - b) <= eps for a, b in zip(m1, m2))

def is_invertible_matrix(M: List[List[complex]], eps: float = 1e-12) -> bool:
    """Check det != 0 for small n via simple Gaussian / explicit formulas."""
    n = len(M)
    if n == 0:
        return True
    if n == 1:
        return abs(M[0][0]) > eps
    if n == 2:
        det = M[0][0] * M[1][1] - M[0][1] * M[1][0]
        return abs(det) > eps
    # fallback: successive elimination
    A = [row[:] for row in M]
    det = 1.0 + 0.0j
    for i in range(n):
        pivot = i
        for r in range(i + 1, n):
            if abs(A[r][i]) > abs(A[pivot][i]):
                pivot = r
        if abs(A[pivot][i]) <= eps:
            return False
        if pivot != i:
            A[i], A[pivot] = A[pivot], A[i]
            det = -det
        det *= A[i][i]
        for r in range(i + 1, n):
            factor = A[r][i] / A[i][i]
            for c in range(i, n):
                A[r][c] -= factor * A[i][c]
    return abs(det) > eps

def is_share_preserving(foot_before: Set[str], foot_after: Set[str]) -> bool:
    """D14: Foot unchanged (share ids)."""
    return foot_before == foot_after

def apply_matrix(M: List[List[complex]], a: List[complex]) -> List[complex]:
    n = len(a)
    return [sum(M[i][j] * a[j] for j in range(n)) for i in range(n)]

def norm2(a: Sequence[complex]) -> float:
    return sum(abs(w) ** 2 for w in a)

def normalize(a: List[complex]) -> List[complex]:
    n = math.sqrt(norm2(a)) or 1.0
    return [w / n for w in a]

# ---------------------------------------------------------------------------
# Coherent set with linear residual
# ---------------------------------------------------------------------------

@dataclass
class PathState:
    name: str
    weight: complex
    isolation_cost: float
    share_ids: Set[str] = field(default_factory=set)
    x: float = 0.0
    v: float = 0.0
    phase_rate: float = 0.0  # φ_i for diagonal unitary

@dataclass
class CoherentLinear:
    paths: List[PathState]
    maintain_cost: float

    def active(self) -> List[PathState]:
        return [p for p in self.paths if p.isolation_cost > self.maintain_cost]

    def weights(self) -> List[complex]:
        return [p.weight for p in self.active()]

    def foot(self) -> Set[str]:
        f: Set[str] = set()
        for p in self.active():
            f |= p.share_ids
        return f

    def set_weights(self, new_w: Sequence[complex]) -> None:
        active = self.active()
        assert len(new_w) == len(active)
        for p, w in zip(active, new_w):
            p.weight = w

# ---------------------------------------------------------------------------
# Free-epoch unitary updates (R + N enforced)
# ---------------------------------------------------------------------------

def free_epoch_diagonal_unitary(cs: CoherentLinear, dt: float) -> None:
    """
    Operation: phase_accumulate under R/N.
    a_i <- a_i * exp(-i φ_i dt). Preserves relative moduli and norm.
    Share footprint unchanged.
    """
    foot_before = cs.foot()
    active = cs.active()
    mu_before = relative_moduli([p.weight for p in active])
    for p in active:
        p.weight *= cmath.exp(-1j * p.phase_rate * dt)
    foot_after = cs.foot()
    mu_after = relative_moduli([p.weight for p in active])
    assert is_share_preserving(foot_before, foot_after), "R violated: Foot changed"
    assert moduli_equal(mu_before, mu_after), "N violated: relative moduli changed"

def free_epoch_unitary_matrix(cs: CoherentLinear, M: List[List[complex]]) -> None:
    """
    General free-epoch step: a <- M a.
    Rejects non-invertible, Foot-changing, or norm-changing proposals
    (norm gauge is a constraint, not a silent repair).
    Warns on relative-modulus change: under D19+A3 such a map is dominated
    by the zero-change alternative in a free epoch (docs/07 contention 1).
    """
    active = cs.active()
    n = len(active)
    assert len(M) == n and all(len(row) == n for row in M)
    assert is_invertible_matrix(M), "R violated: M not invertible"
    foot_before = cs.foot()
    a = [p.weight for p in active]
    nrm_before = norm2(a)
    a_new = apply_matrix(M, a)
    nrm_after = norm2(a_new)
    assert abs(nrm_after - nrm_before) <= 1e-9 * max(nrm_before, 1.0), \
        "norm gauge violated: M is not norm-preserving on this state"
    mu_before = relative_moduli(a)
    mu_after = relative_moduli(a_new)
    if not moduli_equal(mu_before, mu_after):
        print("   [reconfiguration] modulus-changing map: not a free-epoch "
              "update — classify as a reconfiguration event (T15/T16); "
              "see docs/17")
    cs.set_weights(a_new)
    foot_after = cs.foot()
    assert is_share_preserving(foot_before, foot_after), "R violated: Foot changed"

def structural_project(cs: CoherentLinear) -> CoherentLinear:
    """
    Operation: structural_decoherence — non-unitary locus.
    Drop paths with isolation <= maintain; renormalize surviving weights (Born gauge).
    """
    kept = [p for p in cs.paths if p.isolation_cost > cs.maintain_cost]
    new_cs = CoherentLinear(paths=kept, maintain_cost=cs.maintain_cost)
    w = new_cs.weights()
    if w:
        new_cs.set_weights(normalize(w))
    return new_cs

def born_extract(cs: CoherentLinear) -> Optional[PathState]:
    active = cs.active()
    if not active:
        return None
    weights = [abs(p.weight) ** 2 for p in active]
    total = sum(weights) or 1.0
    r = random.random() * total
    acc = 0.0
    for p, wt in zip(active, weights):
        acc += wt
        if r <= acc:
            return p
    return active[-1]

def intensity(cs: CoherentLinear) -> float:
    return abs(sum(p.weight for p in cs.active())) ** 2

# ---------------------------------------------------------------------------
# Demo
# ---------------------------------------------------------------------------

def demo():
    print("=" * 64)
    print("Linear reduce + free-epoch unitary (R/N enforced)")
    print("=" * 64)

    p1 = PathState("arm1", 1 / math.sqrt(2), isolation_cost=5.0,
                   share_ids={"common", "p1"}, phase_rate=0.0)
    p2 = PathState("arm2", 1 / math.sqrt(2), isolation_cost=5.0,
                   share_ids={"common", "p2"}, phase_rate=1.0)
    cs = CoherentLinear(paths=[p1, p2], maintain_cost=1.0)

    print("\n1. Free-epoch diagonal unitary (phase accumulate)")
    print(f"   t=0  I={intensity(cs):.4f}  μ={relative_moduli(cs.weights())}")
    for step in range(10):
        free_epoch_diagonal_unitary(cs, dt=0.1)
        if step % 3 == 2:
            print(f"   t={(step+1)*0.1:.1f}  I={intensity(cs):.4f}  "
                  f"μ={tuple(round(x, 4) for x in relative_moduli(cs.weights()))}")

    print("\n2. Norm preserved, relative moduli frozen (N)")
    print(f"   ||a||^2 = {norm2(cs.weights()):.6f}")

    print("\n3. Structural projection (non-unitary locus)")
    p1 = PathState("arm1", 1 / math.sqrt(2), 8.0, share_ids={"c", "a"})
    p2 = PathState("arm2", 1 / math.sqrt(2), 2.0, share_ids={"c", "b"})
    cs = CoherentLinear([p1, p2], maintain_cost=5.0)
    print(f"   before: active={[p.name for p in cs.active()]}")
    cs = structural_project(cs)
    print(f"   after:  active={[p.name for p in cs.active()]}  weights={cs.weights()}")

    print("\n4. Born extract after free evolution")
    p1 = PathState("arm1", 0.6 + 0.0j, 5.0, share_ids={"c"})
    p2 = PathState("arm2", 0.8 + 0.0j, 5.0, share_ids={"c"})
    cs = CoherentLinear([p1, p2], maintain_cost=1.0)
    cs.set_weights(normalize(cs.weights()))
    counts = {"arm1": 0, "arm2": 0}
    for _ in range(5000):
        ch = born_extract(cs)
        if ch:
            counts[ch.name] += 1
    print(f"   N=5000  arm1={counts['arm1']/5000:.3f}  arm2={counts['arm2']/5000:.3f}  "
          f"(expect ~{abs(cs.paths[0].weight)**2:.3f}, {abs(cs.paths[1].weight)**2:.3f})")

    print("\n5. General unitary (Hadamard) — a reconfiguration-event map (docs/17)")
    p1 = PathState("arm1", 1 / math.sqrt(2), 5.0, share_ids={"c", "a"})
    p2 = PathState("arm2", 1 / math.sqrt(2), 5.0, share_ids={"c", "b"})
    cs = CoherentLinear([p1, p2], maintain_cost=1.0)
    h = 1 / math.sqrt(2)
    H = [[complex(h), complex(h)], [complex(h), complex(-h)]]
    free_epoch_unitary_matrix(cs, H)
    print(f"   after H: μ={tuple(round(x, 4) for x in relative_moduli(cs.weights()))}  "
          f"||a||^2={norm2(cs.weights()):.6f}")
    print("   (a beam splitter is a reconfiguration event: weight-blind structural")
    print("    cost, induced isometry per T16 — docs/17)")
    print("=" * 64)

if __name__ == "__main__":
    demo()
