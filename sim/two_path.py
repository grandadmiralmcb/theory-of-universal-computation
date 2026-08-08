#!/usr/bin/env python3
"""
Two-path structural + amplitude + velocity coupling toy
=======================================================
Operations: coherent_set, isolation/maintain costs, structural_decoherence,
amplitude weights, path_recombine, intensity, visibility, born_extract,
attach_sequential_state (path-wise), preferential_select, sequential_tick,
phase_accumulate, path_recombine_with_velocity, com_from_amplitudes,
classical_limit_of_coherence.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional, Tuple
import cmath
import math
import random

@dataclass
class Path:
    name: str
    amplitude: complex
    isolation_cost: float
    x: float = 0.0
    v: float = 0.0
    m: float = 1.0
    phase_rate: float = 0.0   # φ_i for phase_accumulate

@dataclass
class CoherentSet:
    paths: List[Path]
    maintain_cost: float

    def active(self) -> List[Path]:
        return [p for p in self.paths if p.isolation_cost > self.maintain_cost]

def structural_decoherence(cs: CoherentSet) -> CoherentSet:
    kept = [p for p in cs.paths if p.isolation_cost > cs.maintain_cost]
    return CoherentSet(paths=kept, maintain_cost=cs.maintain_cost)

def path_recombine(cs: CoherentSet) -> complex:
    return sum((p.amplitude for p in cs.active()), complex(0))

def intensity(a_tot: complex) -> float:
    return abs(a_tot) ** 2

def visibility_amplitude(cs: CoherentSet) -> float:
    active = cs.active()
    if len(active) < 2:
        return 0.0
    a1, a2 = active[0].amplitude, active[1].amplitude
    den = abs(a1)**2 + abs(a2)**2
    return (2 * abs(a1) * abs(a2) / den) if den > 0 else 0.0

def born_extract(cs: CoherentSet) -> Optional[Path]:
    active = cs.active()
    if not active:
        return None
    weights = [abs(p.amplitude)**2 for p in active]
    total = sum(weights)
    r = random.random() * total if total > 0 else 0.0
    acc = 0.0
    for p, w in zip(active, weights):
        acc += w
        if r <= acc:
            return p
    return active[-1]

def preferential_select_dv(m: float, b: float, dt: float) -> float:
    """δv* = -(b/m)·dt (CI4 per-tick increment)"""
    return -(b / m) * dt if m != 0 else 0.0

def sequential_tick_path(p: Path, b: float, dt: float) -> None:
    """path-wise preferential_select + sequential_tick"""
    dv_star = preferential_select_dv(p.m, b, dt)
    p.v += dv_star
    p.x += p.v * dt

def phase_accumulate(p: Path, dt: float) -> None:
    """a <- a * exp(-i φ dt)"""
    p.amplitude *= cmath.exp(-1j * p.phase_rate * dt)

def com_from_amplitudes(cs: CoherentSet) -> Tuple[float, float]:
    """amplitude-weighted mean position and velocity"""
    active = cs.active()
    if not active:
        return 0.0, 0.0
    w = [abs(p.amplitude)**2 for p in active]
    W = sum(w) or 1.0
    x = sum(wi * p.x for wi, p in zip(w, active)) / W
    v = sum(wi * p.v for wi, p in zip(w, active)) / W
    return x, v

def demo():
    print("=" * 64)
    print("Two-path + velocity coupling")
    print("=" * 64)

    # Two paths, same initial x,v; different phase rates (path-dependent binding proxy)
    p1 = Path("arm1", amplitude=1/math.sqrt(2), isolation_cost=5.0, x=0.0, v=0.0, m=1.0, phase_rate=0.0)
    p2 = Path("arm2", amplitude=1/math.sqrt(2), isolation_cost=5.0, x=0.0, v=0.0, m=1.0, phase_rate=1.0)
    cs = CoherentSet(paths=[p1, p2], maintain_cost=1.0)

    dt = 0.1
    # Constant bias on both arms (COM-like motion) but differential phase
    b = 0.5
    print("\n1. Path-wise sequential ticks under common bias + phase_accumulate")
    for step in range(10):
        for p in cs.active():
            sequential_tick_path(p, b, dt)
            phase_accumulate(p, dt)
        a_tot = path_recombine(cs)
        I = intensity(a_tot)
        x_com, v_com = com_from_amplitudes(cs)
        if step % 3 == 0:
            print(f"   t={step*dt:.1f}  x_com={x_com:+.3f}  v_com={v_com:+.3f}  I={I:.4f}  V={visibility_amplitude(cs):.3f}")

    print("\n2. Differential bias (which-path sequential distinction)")
    p1 = Path("arm1", 1/math.sqrt(2), 5.0, x=0.0, v=0.0, m=1.0, phase_rate=0.0)
    p2 = Path("arm2", 1/math.sqrt(2), 5.0, x=0.0, v=0.0, m=1.0, phase_rate=0.0)
    cs = CoherentSet(paths=[p1, p2], maintain_cost=1.0)
    for step in range(15):
        sequential_tick_path(p1, b=0.2, dt=dt)   # weak bias arm1
        sequential_tick_path(p2, b=1.0, dt=dt)   # strong bias arm2
        if step % 5 == 4:
            print(f"   t={(step+1)*dt:.1f}  x1={p1.x:+.3f} v1={p1.v:+.3f}  x2={p2.x:+.3f} v2={p2.v:+.3f}")
    print("   (trajectories diverge → isolation typically becomes cheap in a fuller model)")

    print("\n3. Recombine with velocity (com_from_amplitudes)")
    # Reset equal amplitudes, different positions
    p1 = Path("arm1", 1/math.sqrt(2), 5.0, x=1.0, v=0.5, m=1.0)
    p2 = Path("arm2", 1/math.sqrt(2), 5.0, x=-1.0, v=-0.2, m=1.0)
    cs = CoherentSet(paths=[p1, p2], maintain_cost=1.0)
    x_com, v_com = com_from_amplitudes(cs)
    print(f"   weighted COM: x={x_com:+.3f}, v={v_com:+.3f}")

    print("\n4. Born extract carries surviving velocity")
    chosen = born_extract(cs)
    if chosen:
        print(f"   selected {chosen.name}: x={chosen.x:+.3f}, v={chosen.v:+.3f}")

    print("\n5. Classical limit: raise maintain_cost, survivor continues sequentially")
    p1 = Path("arm1", 1/math.sqrt(2), isolation_cost=8.0, x=0.0, v=0.0, m=1.0)
    p2 = Path("arm2", 1/math.sqrt(2), isolation_cost=2.0, x=0.0, v=0.0, m=1.0)
    cs = CoherentSet(paths=[p1, p2], maintain_cost=5.0)
    cs = structural_decoherence(cs)
    print(f"   survivors: {[p.name for p in cs.active()]}")
    for p in cs.active():
        for _ in range(5):
            sequential_tick_path(p, b=1.0, dt=0.1)
        print(f"   after classical ticks: x={p.x:+.3f}, v={p.v:+.3f}")
    print("=" * 64)

if __name__ == "__main__":
    demo()
