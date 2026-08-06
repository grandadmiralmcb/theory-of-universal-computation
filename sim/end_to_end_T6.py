#!/usr/bin/env python3
"""
End-to-end T6 test
==================
Expression tree → m_struct_from_tree → velocity integrator → measured
acceleration ratio under identical constant bias.

No integer share_density knobs. Prediction from T6:
  a_A / a_B = m_B / m_A
"""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
import math

# --- minimal tree language (inline to keep self-contained; mirrors expr_tree) ---

@dataclass
class Var:
    name: str

@dataclass
class Pair:
    left: object
    right: object

@dataclass
class Share:
    id: str
    content: object
    refcount: int = 1

def count_shares(term, seen=None) -> int:
    if seen is None:
        seen = set()
    if isinstance(term, Share):
        i = id(term)
        if i in seen:
            return 0
        seen.add(i)
        return 1 + count_shares(term.content, seen)
    if isinstance(term, Pair):
        return count_shares(term.left, seen) + count_shares(term.right, seen)
    return 0

def m_struct_from_tree(term, alpha=1.0, floor=0.05) -> float:
    return alpha * float(count_shares(term)) + floor

def build_cluster(n_shares: int, tag: str):
    shares = [Share(id=f"{tag}-{i}", content=Var(f"v{i}"), refcount=2) for i in range(n_shares)]
    term = shares[0] if shares else Var("empty")
    for s in shares[1:]:
        term = Pair(term, s)
    return term

# --- velocity integrator driven only by tree-derived m ---

@dataclass
class SeqState:
    x: float = 0.0
    v: float = 0.0
    m: float = 1.0
    history: List[dict] = field(default_factory=list)

def run_constant_bias(m: float, b: float, ticks: int = 200, dt: float = 0.05) -> SeqState:
    st = SeqState(m=m)
    for t in range(ticks):
        dv_star = -b / st.m
        st.v += dv_star * dt
        st.x += st.v * dt
        st.history.append({"t": (t + 1) * dt, "x": st.x, "v": st.v})
    return st

def measured_acceleration(st: SeqState) -> float:
    if not st.history:
        return 0.0
    T = st.history[-1]["t"]
    return st.history[-1]["v"] / T  # from rest: v = a T

def demo():
    print("=" * 64)
    print("End-to-end T6: tree → m_struct → measured a ratio")
    print("=" * 64)

    n_A, n_B = 3, 12
    tree_A = build_cluster(n_A, "A")
    tree_B = build_cluster(n_B, "B")
    m_A = m_struct_from_tree(tree_A)
    m_B = m_struct_from_tree(tree_B)

    b = 1.0
    pred_ratio = m_B / m_A
    print(f"\n  Trees: n_A={count_shares(tree_A)}, n_B={count_shares(tree_B)}")
    print(f"  m_A={m_A:.6f}, m_B={m_B:.6f}")
    print(f"  Predicted a_A/a_B = m_B/m_A = {pred_ratio:.6f}")

    st_A = run_constant_bias(m_A, b)
    st_B = run_constant_bias(m_B, b)
    a_A = measured_acceleration(st_A)
    a_B = measured_acceleration(st_B)
    obs_ratio = a_A / a_B if abs(a_B) > 1e-15 else float("nan")

    print(f"\n  Measured a_A={a_A:.8f}, a_B={a_B:.8f}")
    print(f"  Observed ratio a_A/a_B = {obs_ratio:.6f}")
    print(f"  Relative error = {abs(obs_ratio - pred_ratio)/pred_ratio:.2e}")

    passed = abs(obs_ratio - pred_ratio) / pred_ratio < 1e-6
    print(f"\n  T6 end-to-end: {'PASS' if passed else 'FAIL'}")
    print("=" * 64)
    return passed

if __name__ == "__main__":
    demo()
