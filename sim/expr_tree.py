#!/usr/bin/env python3
"""
Expression-tree structural costs
================================
Compute m_struct and isolation costs from actual term structure
(not integer knobs).

Minimal term language:
  Var, Abs, App, Pair, Share

Operations:
  count_shares, share_nodes, m_struct_from_tree,
  isolation_cost_from_tree, maintain_cost_from_tree
"""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Set, Tuple
import itertools

# ---------------------------------------------------------------------------
# Term language
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class Var:
    name: str

@dataclass(frozen=True)
class Abs:
    var: str
    body: Any

@dataclass(frozen=True)
class App:
    fun: Any
    arg: Any

@dataclass(frozen=True)
class Pair:
    left: Any
    right: Any

@dataclass
class Share:
    """Explicit sharing: multiple parents can hold the same Share object."""
    id: str
    content: Any
    # runtime: how many external references currently depend on this node
    refcount: int = 1

Term = Any

def count_shares(term: Term, seen: Optional[Set[int]] = None) -> int:
    """Operation: count_shares — number of distinct Share nodes in the tree."""
    if seen is None:
        seen = set()
    if isinstance(term, Share):
        i = id(term)
        if i in seen:
            return 0
        seen.add(i)
        return 1 + count_shares(term.content, seen)
    if isinstance(term, Abs):
        return count_shares(term.body, seen)
    if isinstance(term, App):
        return count_shares(term.fun, seen) + count_shares(term.arg, seen)
    if isinstance(term, Pair):
        return count_shares(term.left, seen) + count_shares(term.right, seen)
    return 0

def share_nodes(term: Term, seen: Optional[Set[int]] = None) -> List[Share]:
    """Collect distinct Share node objects."""
    if seen is None:
        seen = set()
    out: List[Share] = []
    if isinstance(term, Share):
        i = id(term)
        if i in seen:
            return out
        seen.add(i)
        out.append(term)
        out.extend(share_nodes(term.content, seen))
        return out
    if isinstance(term, Abs):
        return share_nodes(term.body, seen)
    if isinstance(term, App):
        return share_nodes(term.fun, seen) + share_nodes(term.arg, seen)
    if isinstance(term, Pair):
        return share_nodes(term.left, seen) + share_nodes(term.right, seen)
    return out

def open_bindings(term: Term) -> int:
    """Rough count of Abs nodes (binding sites)."""
    if isinstance(term, Abs):
        return 1 + open_bindings(term.body)
    if isinstance(term, App):
        return open_bindings(term.fun) + open_bindings(term.arg)
    if isinstance(term, Pair):
        return open_bindings(term.left) + open_bindings(term.right)
    if isinstance(term, Share):
        return open_bindings(term.content)
    return 0

# ---------------------------------------------------------------------------
# Structural inertia from the tree
# ---------------------------------------------------------------------------

def m_struct_from_tree(term: Term, alpha: float = 1.0, floor: float = 0.05) -> float:
    """
    Operation: m_struct_from_tree

    Structural inertia = alpha * (number of distinct Share nodes)
    + small floor so m > 0 even for share-free terms.

    Note: `alpha` here is WM3's inertia coefficient (written α_m in the
    docs), distinct from the WM2 cost-counter weight α; the defaults
    coinciding at 1.0 is incidental.

    Rationale: changing the sequential trajectory of a cluster requires
    disturbing each independent shared sub-expression that participates
    in the cluster's identity under sequential probing.
    """
    return alpha * float(count_shares(term)) + floor

# ---------------------------------------------------------------------------
# Isolation / maintain costs from the tree
# ---------------------------------------------------------------------------

def isolation_cost_from_tree(
    path_term: Term,
    shared_with: List[Term],
    alpha: float = 1.0,
    beta: float = 0.5,
    gamma: float = 2.0,
) -> float:
    """
    Operation: isolation_cost_from_tree

    Cost to isolate path_term from other members of a coherent set:
    break every Share node that appears in both path_term and any other
    member (by object identity).
    """
    path_shares = {id(s): s for s in share_nodes(path_term)}
    other_ids: Set[int] = set()
    for t in shared_with:
        for s in share_nodes(t):
            other_ids.add(id(s))

    # shares that must be broken = intersection
    to_break = [s for i, s in path_shares.items() if i in other_ids]
    S = len(to_break)
    # binding residual opened by breaking those shares (proxy: bindings inside them)
    B = sum(open_bindings(s.content) for s in to_break)
    D = 1.0 if S > 0 else 0.0   # breaking shared structure changes observational identity
    return alpha * S + beta * B + gamma * D

def maintain_cost_from_tree(
    members: List[Term],
    env_share_count: int = 0,
    alpha: float = 1.0,
    beta: float = 0.5,
) -> float:
    """
    Operation: maintain_cost_from_tree

    Ongoing cost of keeping all cross-member share links + optional
    environmental shares intact.

    `env_share_count` is an integer proxy knob, not tree-derived (see
    docs/08 §1 remaining gap). Charging the environment to the maintain
    ledger only is postulate WM4 (docs/00 §3); it is what drives T11.
    """
    # all distinct shares that appear in more than one member
    id_to_count: Dict[int, int] = {}
    id_to_share: Dict[int, Share] = {}
    for t in members:
        seen_local: Set[int] = set()
        for s in share_nodes(t):
            i = id(s)
            if i in seen_local:
                continue
            seen_local.add(i)
            id_to_count[i] = id_to_count.get(i, 0) + 1
            id_to_share[i] = s

    cross = [id_to_share[i] for i, c in id_to_count.items() if c >= 2]
    S = len(cross) + env_share_count
    B = sum(open_bindings(s.content) for s in cross)
    return alpha * S + beta * B

# ---------------------------------------------------------------------------
# Demo: inertia ratio from real trees (parameter-free prediction)
# ---------------------------------------------------------------------------

def build_cluster(n_shares: int, tag: str) -> Term:
    """Build a cluster with exactly n_shares independent Share nodes."""
    shares = [Share(id=f"{tag}-{i}", content=Var(f"v{i}"), refcount=2) for i in range(n_shares)]
    # nest them in pairs so the whole thing is one term
    term: Term = shares[0] if shares else Var("empty")
    for s in shares[1:]:
        term = Pair(term, s)
    return term

def demo():
    print("=" * 64)
    print("Expression-tree structural costs")
    print("=" * 64)

    # --- (1) m_struct from trees ---
    tree_a = build_cluster(3, "A")
    tree_b = build_cluster(12, "B")
    m_a = m_struct_from_tree(tree_a)
    m_b = m_struct_from_tree(tree_b)
    print(f"\n1. m_struct from actual Share counts")
    print(f"   cluster A: shares={count_shares(tree_a)}, m_struct={m_a:.4f}")
    print(f"   cluster B: shares={count_shares(tree_b)}, m_struct={m_b:.4f}")
    print(f"   predicted aA/aB = mB/mA = {m_b/m_a:.4f}")

    # --- isolation costs ---
    # two paths that share some nodes
    common = Share(id="common", content=Var("c"), refcount=2)
    path1 = Pair(common, Share(id="p1-only", content=Var("x"), refcount=1))
    path2 = Pair(common, Share(id="p2-only", content=Var("y"), refcount=1))
    c_iso_1 = isolation_cost_from_tree(path1, [path2])
    c_iso_2 = isolation_cost_from_tree(path2, [path1])
    c_maint = maintain_cost_from_tree([path1, path2], env_share_count=0)
    print(f"\n2. Isolation / maintain from trees")
    print(f"   C_isolate(path1)={c_iso_1:.4f}")
    print(f"   C_isolate(path2)={c_iso_2:.4f}")
    print(f"   C_maintain={c_maint:.4f}")
    print(f"   coherent? both isolation > maintain: {c_iso_1 > c_maint and c_iso_2 > c_maint}")

    # environmental shares raise maintain cost
    c_maint_env = maintain_cost_from_tree([path1, path2], env_share_count=5)
    print(f"   C_maintain with env_shares=5: {c_maint_env:.4f}")
    print(f"   decoheres? {c_iso_1 <= c_maint_env or c_iso_2 <= c_maint_env}")

    # --- (3) parameter-free prediction ---
    # Under identical bias, acceleration ratio equals inverse m_struct ratio
    # computed from Share counts alone — no free m parameter.
    print(f"\n3. Parameter-free prediction")
    print(f"   Given only the expression trees of A and B (Share counts 3 vs 12),")
    print(f"   under identical constant bias the theory requires")
    print(f"   a_A / a_B = {m_b/m_a:.6f}")
    print(f"   This ratio is fixed by tree structure; it cannot be tuned away")
    print(f"   without changing alpha/floor equally for both (cancels in the ratio).")
    print("=" * 64)

if __name__ == "__main__":
    demo()
