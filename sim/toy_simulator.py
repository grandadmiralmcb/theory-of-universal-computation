#!/usr/bin/env python3
"""
Toy Structural Sequential Simulator
===================================
Expression-Tree Ontology — discrete sequential calculus.

Supports:
  - constant bias (uniform field)
  - position-dependent bias from a structural potential V(x)

Under a potential the continuum limit is
    m_struct * ẍ = - dV/dx

The simulator selects lowest-structural-cost velocity updates at each tick
and tracks a simple energy-like quantity to check approximate conservation
when the bias is derivable from a potential.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Callable, List, Optional, Tuple
import math

ALPHA = 1.0

@dataclass
class Seq:
    x: float = 0.0
    v: float = 0.0
    share_density: int = 1
    name: str = "cluster"

@dataclass
class Bias:
    """
    Bias context.
    - If strength is set and potential is None: constant bias (old behavior).
    - If potential is set: b(x) = dV/dx (force = -dV/dx in the continuum).
    """
    strength: float = 0.0
    potential: Optional[Callable[[float], float]] = None
    force: Optional[Callable[[float], float]] = None  # if provided, used directly as -dV/dx

    def b_at(self, x: float) -> float:
        """Return the local structural bias strength at position x.

        Convention: continuum equation is ẍ = -b(x)/m
        so b(x) = +dV/dx when force = -dV/dx.
        """
        if self.force is not None:
            return -self.force(x)          # b = -force
        if self.potential is not None:
            # numerical derivative of V
            eps = 1e-6
            dV = (self.potential(x + eps) - self.potential(x - eps)) / (2 * eps)
            return dV
        return self.strength

def m_struct(cluster: Seq) -> float:
    return ALPHA * float(cluster.share_density) + 0.05

def cost_of_dv(cluster: Seq, dv: float, bias: Optional[Bias]) -> Tuple[float, dict]:
    m = m_struct(cluster)
    b = bias.b_at(cluster.x) if bias is not None else 0.0
    C = 0.5 * m * (dv ** 2) + b * dv
    return C, {"m": m, "b": b, "dv": dv, "C": C}

@dataclass
class SequentialState:
    cluster: Seq
    bias: Optional[Bias] = None
    tick: int = 0
    history: List[dict] = field(default_factory=list)

class SequentialEvaluator:
    def __init__(self, state: SequentialState, dt: float = 0.05,
                 dv_candidates: Optional[List[float]] = None):
        self.state = state
        self.dt = dt
        # finer grid for better approximation of continuous optimum
        self.dv_candidates = dv_candidates or [i * 0.02 for i in range(-50, 51)]

    def tick(self) -> dict:
        candidates = []
        for dv in self.dv_candidates:
            C, breakdown = cost_of_dv(self.state.cluster, dv, self.state.bias)
            candidates.append((C, dv, breakdown))

        candidates.sort(key=lambda t: t[0])
        best_C, best_dv, best_breakdown = candidates[0]

        m = best_breakdown["m"]
        b = best_breakdown["b"]
        dv_star = -b / m if m != 0 else 0.0

        self.state.cluster.v += best_dv
        self.state.cluster.x += self.state.cluster.v * self.dt
        self.state.tick += 1

        # structural energy analogue: kinetic + potential
        V = 0.0
        if self.state.bias is not None and self.state.bias.potential is not None:
            V = self.state.bias.potential(self.state.cluster.x)
        elif self.state.bias is not None and self.state.bias.force is not None:
            # only known for simple analytic cases; leave 0 if unknown
            V = 0.0
        T = 0.5 * m * (self.state.cluster.v ** 2)
        E = T + V

        record = {
            "tick": self.state.tick,
            "x": self.state.cluster.x,
            "v": self.state.cluster.v,
            "dv_chosen": best_dv,
            "dv_star": dv_star,
            "cost": best_C,
            "m_struct": m,
            "b_struct": b,
            "T": T,
            "V": V,
            "E": E,
            "share_density": self.state.cluster.share_density,
        }
        self.state.history.append(record)
        return record

    def run(self, n_ticks: int) -> List[dict]:
        for _ in range(n_ticks):
            self.tick()
        return self.state.history

# ---------------------------------------------------------------------------
# Experiments
# ---------------------------------------------------------------------------

def run_constant_bias_comparison(
    share_a: int = 5,
    share_b: int = 20,
    bias_strength: float = 1.0,
    ticks: int = 50,
    dt: float = 0.1,
):
    print("=" * 64)
    print("Constant bias — inverse-acceleration test")
    print("=" * 64)

    bias = Bias(strength=bias_strength)
    cluster_a = Seq(x=0.0, v=0.0, share_density=share_a, name="A")
    cluster_b = Seq(x=0.0, v=0.0, share_density=share_b, name="B")

    m_a, m_b = m_struct(cluster_a), m_struct(cluster_b)
    print(f"  A: m={m_a:.4f}  predicted a={-bias_strength/m_a:.6f}")
    print(f"  B: m={m_b:.4f}  predicted a={-bias_strength/m_b:.6f}")
    print(f"  Predicted ratio aA/aB = {m_b/m_a:.4f}")

    eval_a = SequentialEvaluator(SequentialState(cluster=cluster_a, bias=bias), dt=dt)
    eval_b = SequentialEvaluator(SequentialState(cluster=cluster_b, bias=bias), dt=dt)
    hist_a, hist_b = eval_a.run(ticks), eval_b.run(ticks)

    a_a = hist_a[-1]["v"] / (ticks * dt)
    a_b = hist_b[-1]["v"] / (ticks * dt)
    print(f"  Observed aA={a_a:.6f}, aB={a_b:.6f}, ratio={a_a/a_b if a_b else float('nan'):.4f}")
    print("=" * 64)
    return hist_a, hist_b

def run_harmonic(
    share_density: int = 10,
    k: float = 1.0,
    x0: float = 1.0,
    v0: float = 0.0,
    ticks: int = 400,
    dt: float = 0.05,
):
    """Harmonic potential V = ½ k x²  →  force = -k x  →  b(x) = k x."""
    print("=" * 64)
    print("Position-dependent bias — harmonic oscillator")
    print("=" * 64)

    def V(x: float) -> float:
        return 0.5 * k * x * x

    def force(x: float) -> float:
        return -k * x

    bias = Bias(potential=V, force=force)
    cluster = Seq(x=x0, v=v0, share_density=share_density, name="osc")
    m = m_struct(cluster)
    omega = math.sqrt(k / m)
    T_period = 2 * math.pi / omega

    print(f"  m_struct={m:.4f}, k={k}, ω={omega:.4f}, period≈{T_period:.4f}")
    print(f"  initial x={x0}, v={v0}")

    evaluator = SequentialEvaluator(SequentialState(cluster=cluster, bias=bias), dt=dt)
    hist = evaluator.run(ticks)

    # report a few samples and energy drift
    E0 = hist[0]["E"]
    E_final = hist[-1]["E"]
    E_min = min(r["E"] for r in hist)
    E_max = max(r["E"] for r in hist)

    print(f"\n  t=0     x={hist[0]['x']:+.4f}  v={hist[0]['v']:+.4f}  E={hist[0]['E']:.6f}")
    mid = len(hist)//4
    print(f"  t~T/4   x={hist[mid]['x']:+.4f}  v={hist[mid]['v']:+.4f}  E={hist[mid]['E']:.6f}")
    mid2 = len(hist)//2
    print(f"  t~T/2   x={hist[mid2]['x']:+.4f}  v={hist[mid2]['v']:+.4f}  E={hist[mid2]['E']:.6f}")
    print(f"  final   x={hist[-1]['x']:+.4f}  v={hist[-1]['v']:+.4f}  E={hist[-1]['E']:.6f}")
    print(f"\n  Energy: E0={E0:.6f}, final={E_final:.6f}, range=[{E_min:.6f}, {E_max:.6f}]")
    print(f"  Relative drift ≈ {(E_max - E_min)/max(abs(E0),1e-12):.4e}")
    print("=" * 64)
    return hist

if __name__ == "__main__":
    import math
    run_constant_bias_comparison()
    print()
    run_harmonic()
