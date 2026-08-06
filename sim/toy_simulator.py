#!/usr/bin/env python3
"""
Toy Structural Sequential Simulator
===================================
Expression-Tree Ontology — first executable discrete calculus.

Structural cost is applied to *changes of sequential velocity*.
Under constant bias the lowest-cost update recovers
    Δv = -b_struct / m_struct
exactly as required by the continuum limit derived from the
preferential low-disruption axiom.

Share density enters only through m_struct, so two clusters that
differ solely in share density must obey the inverse-acceleration
ratio a1/a2 = m2/m1.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional, Tuple

# ---------------------------------------------------------------------------
# Structural weights
# ---------------------------------------------------------------------------
ALPHA = 1.0   # share-disruption contribution to inertia

# ---------------------------------------------------------------------------
# Minimal cluster representation
# ---------------------------------------------------------------------------

@dataclass
class Seq:
    """Sequential cluster: position, velocity, share density."""
    x: float = 0.0
    v: float = 0.0
    share_density: int = 1
    name: str = "cluster"

@dataclass
class Bias:
    """Constant ambient bias (structural force)."""
    strength: float          # positive → accelerates in -x direction

# ---------------------------------------------------------------------------
# Structural inertia and cost of a velocity change
# ---------------------------------------------------------------------------

def m_struct(cluster: Seq) -> float:
    """
    Structural inertia proportional to share density.
    (In a fuller model this would be <S> for a unit change of trajectory.)
    """
    return ALPHA * float(cluster.share_density) + 0.05   # small floor so m > 0

def cost_of_dv(cluster: Seq, dv: float, bias: Optional[Bias]) -> Tuple[float, dict]:
    """
    Cost of changing sequential velocity by dv.

    C(dv) = ½ m_struct (dv)² + b_struct * dv

    The linear term encodes the constant bias (preferred direction of acceleration).
    Minimizing C with respect to dv recovers dv* = -b / m, the discrete form of
    the continuum equation ä = -b/m.
    """
    m = m_struct(cluster)
    b = bias.strength if bias is not None else 0.0
    # sign convention: positive b favors negative acceleration
    C = 0.5 * m * (dv ** 2) + b * dv
    return C, {"m": m, "b": b, "dv": dv, "C": C}

# ---------------------------------------------------------------------------
# Sequential evaluator (velocity-update form)
# ---------------------------------------------------------------------------

@dataclass
class SequentialState:
    cluster: Seq
    bias: Optional[Bias] = None
    tick: int = 0
    history: List[dict] = field(default_factory=list)

class SequentialEvaluator:
    def __init__(self, state: SequentialState, dt: float = 0.1, dv_candidates: Optional[List[float]] = None):
        self.state = state
        self.dt = dt
        # candidate velocity changes the evaluator is allowed to consider
        self.dv_candidates = dv_candidates or [-0.5, -0.2, -0.1, 0.0, 0.1, 0.2, 0.5]

    def tick(self) -> dict:
        candidates = []
        for dv in self.dv_candidates:
            C, breakdown = cost_of_dv(self.state.cluster, dv, self.state.bias)
            candidates.append((C, dv, breakdown))

        candidates.sort(key=lambda t: t[0])
        best_C, best_dv, best_breakdown = candidates[0]

        # optimal continuous choice (for reference)
        m = best_breakdown["m"]
        b = best_breakdown["b"]
        dv_star = -b / m if m != 0 else 0.0

        # apply the discrete choice
        self.state.cluster.v += best_dv
        self.state.cluster.x += self.state.cluster.v * self.dt
        self.state.tick += 1

        record = {
            "tick": self.state.tick,
            "x": self.state.cluster.x,
            "v": self.state.cluster.v,
            "dv_chosen": best_dv,
            "dv_star": dv_star,
            "cost": best_C,
            "m_struct": m,
            "share_density": self.state.cluster.share_density,
        }
        self.state.history.append(record)
        return record

    def run(self, n_ticks: int) -> List[dict]:
        for _ in range(n_ticks):
            self.tick()
        return self.state.history

# ---------------------------------------------------------------------------
# Comparison experiment
# ---------------------------------------------------------------------------

def run_comparison(
    share_a: int = 5,
    share_b: int = 20,
    bias_strength: float = 1.0,
    ticks: int = 50,
    dt: float = 0.1,
):
    print("=" * 64)
    print("Toy Structural Sequential Simulator")
    print("Velocity-update form — inverse-acceleration test")
    print("=" * 64)

    bias = Bias(strength=bias_strength)

    cluster_a = Seq(x=0.0, v=0.0, share_density=share_a, name="A")
    cluster_b = Seq(x=0.0, v=0.0, share_density=share_b, name="B")

    m_a = m_struct(cluster_a)
    m_b = m_struct(cluster_b)
    a_pred_a = -bias_strength / m_a
    a_pred_b = -bias_strength / m_b

    print(f"\nStructural inertia:")
    print(f"  A (share={share_a}): m = {m_a:.4f}  → predicted a = {a_pred_a:.6f}")
    print(f"  B (share={share_b}): m = {m_b:.4f}  → predicted a = {a_pred_b:.6f}")
    print(f"  Predicted ratio aA/aB = mB/mA = {m_b/m_a:.4f}")

    eval_a = SequentialEvaluator(SequentialState(cluster=cluster_a, bias=bias), dt=dt)
    eval_b = SequentialEvaluator(SequentialState(cluster=cluster_b, bias=bias), dt=dt)

    hist_a = eval_a.run(ticks)
    hist_b = eval_b.run(ticks)

    # measured average acceleration from velocity change
    v_a = hist_a[-1]["v"]
    v_b = hist_b[-1]["v"]
    a_meas_a = v_a / (ticks * dt)
    a_meas_b = v_b / (ticks * dt)

    print(f"\nAfter {ticks} ticks (dt={dt}):")
    print(f"  A: final x={hist_a[-1]['x']:.4f}, v={v_a:.4f}, measured a≈{a_meas_a:.6f}")
    print(f"  B: final x={hist_b[-1]['x']:.4f}, v={v_b:.4f}, measured a≈{a_meas_b:.6f}")
    if abs(a_meas_b) > 1e-12:
        print(f"  Observed ratio aA/aB ≈ {a_meas_a/a_meas_b:.4f}")
        print(f"  Theory predicted     ≈ {m_b/m_a:.4f}")
    print("=" * 64)
    return hist_a, hist_b

if __name__ == "__main__":
    run_comparison(share_a=5, share_b=20, bias_strength=1.0, ticks=50, dt=0.1)
