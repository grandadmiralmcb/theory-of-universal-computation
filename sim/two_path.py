#!/usr/bin/env python3
"""
Two-path structural + amplitude toy
===================================
Executable fragment of the quantum sector formalisms.

Operations implemented by name:
  coherent_set, isolation_cost, maintain_cost, structural_decoherence,
  amplitude_weight, path_recombine, intensity, visibility_amplitude,
  born_extract, classical_limit_of_coherence (via raising maintain cost).
"""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
import cmath
import math
import random

@dataclass
class Path:
    name: str
    amplitude: complex
    isolation_cost: float   # C_isolate for this path

@dataclass
class CoherentSet:
    paths: List[Path]
    maintain_cost: float    # C_maintain for the whole set

    def active(self) -> List[Path]:
        return [p for p in self.paths if p.isolation_cost > self.maintain_cost]

def structural_decoherence(cs: CoherentSet) -> CoherentSet:
    """Operation: structural_decoherence"""
    kept = [p for p in cs.paths if p.isolation_cost > cs.maintain_cost]
    return CoherentSet(paths=kept, maintain_cost=cs.maintain_cost)

def path_recombine(cs: CoherentSet) -> complex:
    """Operation: path_recombine — sum amplitudes of active paths"""
    return sum((p.amplitude for p in cs.active()), complex(0))

def intensity(a_tot: complex) -> float:
    """Operation: intensity"""
    return abs(a_tot) ** 2

def visibility_amplitude(cs: CoherentSet) -> float:
    """Operation: visibility_amplitude (two-path formula when both active)"""
    active = cs.active()
    if len(active) < 2:
        return 0.0
    a1, a2 = active[0].amplitude, active[1].amplitude
    num = 2 * abs(a1) * abs(a2)
    den = abs(a1)**2 + abs(a2)**2
    return num / den if den > 0 else 0.0

def born_extract(cs: CoherentSet) -> Optional[Path]:
    """Operation: born_extract — sample one path with P ~ |a|^2"""
    active = cs.active()
    if not active:
        return None
    weights = [abs(p.amplitude)**2 for p in active]
    total = sum(weights)
    if total <= 0:
        return random.choice(active)
    r = random.random() * total
    acc = 0.0
    for p, w in zip(active, weights):
        acc += w
        if r <= acc:
            return p
    return active[-1]

def demo():
    print("=" * 64)
    print("Two-path structural + amplitude toy")
    print("=" * 64)

    # Equal amplitudes, relative phase π/2 initially for illustration
    p1 = Path("path1", amplitude=cmath.exp(1j * 0.0) / math.sqrt(2), isolation_cost=5.0)
    p2 = Path("path2", amplitude=cmath.exp(1j * math.pi / 2) / math.sqrt(2), isolation_cost=5.0)
    cs = CoherentSet(paths=[p1, p2], maintain_cost=1.0)

    print("\n1. Coherent set (isolation > maintain for both)")
    print(f"   active paths: {[p.name for p in cs.active()]}")
    a_tot = path_recombine(cs)
    print(f"   a_tot = {a_tot:.4f}, intensity = {intensity(a_tot):.4f}")
    print(f"   visibility_amplitude = {visibility_amplitude(cs):.4f}")

    print("\n2. Interference vs relative phase")
    for phi_deg in [0, 60, 90, 120, 180]:
        phi = math.radians(phi_deg)
        p2.amplitude = cmath.exp(1j * phi) / math.sqrt(2)
        a_tot = path_recombine(cs)
        I = intensity(a_tot)
        V = visibility_amplitude(cs)
        print(f"   Δφ={phi_deg:3d}°  I={I:.4f}  V={V:.4f}")

    print("\n3. Structural decoherence (raise maintain_cost)")
    cs.maintain_cost = 6.0   # now isolation (5) <= maintain (6)
    cs2 = structural_decoherence(cs)
    print(f"   active after decoherence: {[p.name for p in cs2.active()]}")
    print(f"   visibility_amplitude = {visibility_amplitude(cs2):.4f}")

    print("\n4. Born extraction on a still-coherent set (reset maintain)")
    cs.maintain_cost = 1.0
    p2.amplitude = 1 / math.sqrt(2)
    counts = {"path1": 0, "path2": 0}
    N = 5000
    for _ in range(N):
        # restore both paths each trial
        trial = CoherentSet(
            paths=[
                Path("path1", 1/math.sqrt(2), 5.0),
                Path("path2", 1/math.sqrt(2), 5.0),
            ],
            maintain_cost=1.0,
        )
        chosen = born_extract(trial)
        if chosen:
            counts[chosen.name] += 1
    print(f"   N={N}  path1={counts['path1']/N:.3f}  path2={counts['path2']/N:.3f}  (expect ~0.5 each)")

    print("\n5. Classical limit of coherence (unequal isolation + high maintain)")
    # path2 becomes cheap to isolate (environmentally distinguished)
    p1 = Path("path1", 1/math.sqrt(2), isolation_cost=10.0)
    p2 = Path("path2", 1/math.sqrt(2), isolation_cost=2.0)
    cs = CoherentSet(paths=[p1, p2], maintain_cost=5.0)
    cs = structural_decoherence(cs)
    print(f"   surviving paths: {[p.name for p in cs.active()]}")
    print(f"   (path2 isolated → single-path classical regime)")
    print("=" * 64)

if __name__ == "__main__":
    demo()
