#!/usr/bin/env python3
"""
Toy Structural Sequential Simulator
===================================
Expression-Tree Ontology — first executable discrete calculus.

Implements a minimal version of the reduced primitives and the structural
cost proxy (S, B, D) so that sequential trajectories under constant bias
can be computed tick-by-tick.

This is deliberately simplified: the expression language is tiny, reduction
is restricted to sequential-parameter updates, and share density is modeled
by an integer that contributes directly to S. The goal is to make the
structural continuum limit and the inverse-acceleration prediction
executable inside pure theory before any laboratory mapping is attempted.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional, Tuple
import copy

# ---------------------------------------------------------------------------
# Cost weights (can be varied later; ratios matter more than absolute scale)
# ---------------------------------------------------------------------------
ALPHA = 1.0   # weight of share disruption S
BETA  = 0.5   # weight of binding residual B
GAMMA = 2.0   # weight of observational inequivalence D

# ---------------------------------------------------------------------------
# Minimal expression representation
# ---------------------------------------------------------------------------

@dataclass
class Expr:
    """Base class for toy expressions."""
    pass

@dataclass
class Seq(Expr):
    """A sequential cluster with a position x and a share-density."""
    x: float
    share_density: int          # how many independent shares must be disturbed to change x
    name: str = "cluster"

@dataclass
class Bias(Expr):
    """Constant ambient bias context. Positive bias prefers decreasing x."""
    strength: float

@dataclass
class Pair(Expr):
    left: Expr
    right: Expr

# ---------------------------------------------------------------------------
# Structural cost of a proposed sequential step
# ---------------------------------------------------------------------------

def structural_cost(
    current: Seq,
    proposed_x: float,
    bias: Optional[Bias] = None,
) -> Tuple[float, dict]:
    """
    Compute C = αS + βB + γD for a proposed change of sequential parameter.

    S is proportional to share_density * |dx|  (more shares → higher disruption)
    B is a small residual binding cost (kept simple)
    D is 1 if the step goes against the bias direction, else 0
    """
    dx = proposed_x - current.x
    S = current.share_density * abs(dx)
    B = 0.1 * abs(dx)               # minimal binding residual
    D = 0.0
    if bias is not None and bias.strength != 0:
        # steps against the preferred direction incur extra disruption
        preferred_direction = -1.0 if bias.strength > 0 else 1.0
        if dx * preferred_direction < 0:
            D = abs(dx) * abs(bias.strength)

    C = ALPHA * S + BETA * B + GAMMA * D
    breakdown = {"S": S, "B": B, "D": D, "C": C, "dx": dx}
    return C, breakdown

# ---------------------------------------------------------------------------
# Sequential evaluator
# ---------------------------------------------------------------------------

@dataclass
class SequentialState:
    cluster: Seq
    bias: Optional[Bias] = None
    velocity: float = 0.0
    tick: int = 0
    history: List[dict] = field(default_factory=list)

class SequentialEvaluator:
    """
    Local sequential evaluator that repeatedly chooses the lowest-cost
    residual (here restricted to small changes in x).
    """

    def __init__(self, state: SequentialState, step_size: float = 0.1):
        self.state = state
        self.step_size = step_size

    def possible_moves(self) -> List[float]:
        """Candidate sequential advances (toy: three possibilities)."""
        x = self.state.cluster.x
        h = self.step_size
        return [x - h, x, x + h]

    def tick(self) -> dict:
        """Perform one sequential tick: select lowest-C move and update state."""
        candidates = []
        for proposed_x in self.possible_moves():
            C, breakdown = structural_cost(
                self.state.cluster, proposed_x, self.state.bias
            )
            candidates.append((C, proposed_x, breakdown))

        # preferential low-disruption sequentialization
        candidates.sort(key=lambda t: t[0])
        best_C, best_x, best_breakdown = candidates[0]

        old_x = self.state.cluster.x
        dx = best_x - old_x

        # update velocity (simple discrete derivative)
        self.state.velocity = dx / self.step_size if self.step_size != 0 else 0.0
        self.state.cluster.x = best_x
        self.state.tick += 1

        record = {
            "tick": self.state.tick,
            "x": best_x,
            "dx": dx,
            "velocity": self.state.velocity,
            "cost": best_C,
            "breakdown": best_breakdown,
            "share_density": self.state.cluster.share_density,
        }
        self.state.history.append(record)
        return record

    def run(self, n_ticks: int) -> List[dict]:
        for _ in range(n_ticks):
            self.tick()
        return self.state.history

# ---------------------------------------------------------------------------
# Analysis helpers
# ---------------------------------------------------------------------------

def estimate_m_struct(cluster: Seq, bias: Optional[Bias] = None, dx: float = 1.0) -> float:
    """Finite-difference estimate of structural inertia."""
    C_plus, _  = structural_cost(cluster, cluster.x + dx, bias)
    C_0, _     = structural_cost(cluster, cluster.x, bias)
    # second-order style measure of resistance to change
    return (C_plus - C_0) / (dx ** 2) if dx != 0 else float("inf")

def run_comparison(share_a: int = 5, share_b: int = 20, bias_strength: float = 1.0, ticks: int = 30):
    """
    Run two clusters that differ only in share density under identical bias
    and report the inverse-acceleration relation predicted by the theory.
    """
    print("=" * 60)
    print("Toy Structural Sequential Simulator")
    print("Inverse-acceleration prediction test")
    print("=" * 60)

    bias = Bias(strength=bias_strength)

    cluster_a = Seq(x=0.0, share_density=share_a, name="A")
    cluster_b = Seq(x=0.0, share_density=share_b, name="B")

    m_a = estimate_m_struct(cluster_a, bias)
    m_b = estimate_m_struct(cluster_b, bias)
    print(f"\nStructural inertia estimates:")
    print(f"  Cluster A (share_density={share_a}): m_struct ≈ {m_a:.4f}")
    print(f"  Cluster B (share_density={share_b}): m_struct ≈ {m_b:.4f}")
    print(f"  Predicted acceleration ratio aA/aB = mB/mA ≈ {m_b/m_a:.4f}")

    eval_a = SequentialEvaluator(SequentialState(cluster=cluster_a, bias=bias))
    eval_b = SequentialEvaluator(SequentialState(cluster=cluster_b, bias=bias))

    hist_a = eval_a.run(ticks)
    hist_b = eval_b.run(ticks)

    # crude acceleration estimate from final velocity / time
    # (under constant bias we expect roughly constant acceleration)
    final_v_a = hist_a[-1]["velocity"]
    final_v_b = hist_b[-1]["velocity"]
    # using tick count as time proxy
    a_a = final_v_a / ticks
    a_b = final_v_b / ticks

    print(f"\nAfter {ticks} ticks under bias={bias_strength}:")
    print(f"  Cluster A final x={hist_a[-1]['x']:.3f}, v={final_v_a:.4f}, approx a={a_a:.6f}")
    print(f"  Cluster B final x={hist_b[-1]['x']:.3f}, v={final_v_b:.4f}, approx a={a_b:.6f}")
    if a_b != 0:
        print(f"  Observed acceleration ratio aA/aB ≈ {a_a/a_b:.4f}")
        print(f"  (Theory predicted ≈ {m_b/m_a:.4f})")
    print("=" * 60)
    return hist_a, hist_b

# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    run_comparison(share_a=5, share_b=20, bias_strength=1.0, ticks=40)
