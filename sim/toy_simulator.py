#!/usr/bin/env python3
"""
Toy Structural Sequential Simulator
===================================
Expression-Tree Ontology — discrete sequential calculus.

Supports constant bias and position-dependent bias from a structural potential.

Continuum target under a potential V(x):
    m_struct * ẍ = - V'(x)

The optimal velocity change rate from minimizing
    C(dv) = ½ m (dv)² + b(x) dv
is dv* = -b/m.  The integrator applies this as a *rate*:
    v <- v + dv* * dt
    x <- x + v * dt
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
    strength: float = 0.0
    potential: Optional[Callable[[float], float]] = None
    force: Optional[Callable[[float], float]] = None

    def b_at(self, x: float) -> float:
        """b(x) such that continuum equation is ẍ = -b(x)/m.
        When force = -dV/dx is supplied, b = -force = dV/dx.
        """
        if self.force is not None:
            return -self.force(x)
        if self.potential is not None:
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
                 use_analytic: bool = True,
                 dv_candidates: Optional[List[float]] = None):
        self.state = state
        self.dt = dt
        self.use_analytic = use_analytic
        self.dv_candidates = dv_candidates or [i * 0.05 for i in range(-40, 41)]

    def tick(self) -> dict:
        m = m_struct(self.state.cluster)
        b = self.state.bias.b_at(self.state.cluster.x) if self.state.bias else 0.0
        dv_star = -b / m if m != 0 else 0.0

        if self.use_analytic:
            best_dv = dv_star
            best_C = 0.5 * m * (dv_star ** 2) + b * dv_star
        else:
            candidates = []
            for dv in self.dv_candidates:
                C, breakdown = cost_of_dv(self.state.cluster, dv, self.state.bias)
                candidates.append((C, dv, breakdown))
            candidates.sort(key=lambda t: t[0])
            best_C, best_dv, _ = candidates[0]

        # dv* is a *rate* (acceleration); integrate it
        self.state.cluster.v += best_dv * self.dt
        self.state.cluster.x += self.state.cluster.v * self.dt
        self.state.tick += 1

        V = 0.0
        if self.state.bias is not None and self.state.bias.potential is not None:
            V = self.state.bias.potential(self.state.cluster.x)
        T = 0.5 * m * (self.state.cluster.v ** 2)
        E = T + V

        record = {
            "tick": self.state.tick,
            "x": self.state.cluster.x,
            "v": self.state.cluster.v,
            "dv_star": dv_star,
            "dv_applied": best_dv,
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

def run_constant_bias_comparison(
    share_a: int = 5,
    share_b: int = 20,
    bias_strength: float = 1.0,
    ticks: int = 100,
    dt: float = 0.05,
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
    ratio = a_a / a_b if abs(a_b) > 1e-15 else float("nan")
    print(f"  Observed aA={a_a:.6f}, aB={a_b:.6f}, ratio={ratio:.4f}")
    print("=" * 64)
    return hist_a, hist_b

def run_harmonic(
    share_density: int = 10,
    k: float = 1.0,
    x0: float = 1.0,
    v0: float = 0.0,
    periods: float = 3.0,
    dt: float = 0.02,
):
    """Harmonic potential V=½kx² → force=-kx → b(x)=kx."""
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
    ticks = int(periods * T_period / dt)

    print(f"  m_struct={m:.4f}, k={k}, ω={omega:.4f}, period≈{T_period:.4f}")
    print(f"  integrating {periods} periods ({ticks} ticks, dt={dt})")

    evaluator = SequentialEvaluator(SequentialState(cluster=cluster, bias=bias), dt=dt)
    hist = evaluator.run(ticks)

    E0 = hist[0]["E"]
    Es = [r["E"] for r in hist]
    E_min, E_max = min(Es), max(Es)

    def sample(frac, label):
        i = min(int(frac * (len(hist)-1)), len(hist)-1)
        r = hist[i]
        print(f"  {label:8s} x={r['x']:+.4f}  v={r['v']:+.4f}  E={r['E']:.6f}")

    sample(0.0, "t=0")
    sample(0.25, "t~T/4")
    sample(0.5, "t~T/2")
    sample(0.75, "t~3T/4")
    sample(1.0, "final")

    print(f"\n  Energy: E0={E0:.6f}, range=[{E_min:.6f}, {E_max:.6f}]")
    print(f"  Relative drift ≈ {(E_max-E_min)/max(abs(E0),1e-12):.4e}")
    print("=" * 64)
    return hist

if __name__ == "__main__":
    run_constant_bias_comparison()
    print()
    run_harmonic()
