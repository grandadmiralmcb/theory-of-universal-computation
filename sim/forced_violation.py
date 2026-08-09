#!/usr/bin/env python3
"""
Forced-violation states: reachability, minimal-violation selection,
and asymmetry from floor tie-breaking
====================================================================
Executable companion to docs/22-forced-violation.md (the open question
inherited from contention 8's closure: are forced-violation states
physically realized?).

Definitions (ST1 + CC', adopted):
  FV state  = a state that is V=0-stuck (no conserving redex) but not
              fully normal (violating redexes exist). Selection there
              is lex-min: minimal violation V first, floor cost second.

Toy: a linear chain of cells — charged shares (|q| <= CAP), vacuum
slots, and 'clamps' (structures that must absorb a neighboring share,
destroying its charge: V = |q|). Locality: redexes involve adjacent
cells only.

Demonstrations:
  1. Progress in open configurations: with slots available and no
     clamps, every reachable state has a conserving redex — charge is
     absolutely conserved along the whole run (SM-B1' = SM-B1 here).
  2. FV reachability: packing + clamps break progress — a state whose
     only redexes are clamp absorptions is V=0-stuck. Brute typing
     deadlocks there; ST1 selects the minimal violation and continues.
  3. Minimal-step selection rule: offered V=1 and V=2 violation
     channels, selection takes V=1 — forced violations change charge
     by the minimal step.
  4. Asymmetry from floor tie-breaking: at V-ties between conjugate
     channels (+q vs -q destruction), the Archimedean floor decides.
     A conjugation-symmetric floor yields zero net charge drift over
     an ensemble; an asymmetric floor yields systematic drift — the
     C/CP-counterpart of the Sakharov mechanism sketch (docs/22 §5).
"""

from __future__ import annotations
import random
from dataclasses import dataclass
from typing import List, Optional, Tuple

CAP = 2  # per-share charge capacity


@dataclass
class Cell:
    kind: str            # 'q' | 'slot' | 'clamp'
    q: int = 0


def Q(chain: List[Cell]) -> int:
    return sum(c.q for c in chain if c.kind == "q")


# ---------------------------------------------------------------------------
# Redex enumeration: (V, floor, description, apply)
# ---------------------------------------------------------------------------

def redexes(chain: List[Cell], asym: float = 0.0):
    """All available moves. V = violation units (top stratum);
    floor = structural cost; asym = extra floor cost for destroying
    NEGATIVE charge (conjugation asymmetry lives in the floor only)."""
    out = []
    n = len(chain)
    for i in range(n - 1):
        a, b = chain[i], chain[i + 1]
        # annihilate adjacent conjugates (V=0)
        if a.kind == "q" and b.kind == "q" and a.q == -b.q and a.q != 0:
            out.append((0, 1.0, f"annihilate ({a.q},{b.q}) at {i}",
                        _apply_pair(i, Cell("slot"), Cell("slot"))))
        # merge adjacent shares within capacity (V=0)
        if a.kind == "q" and b.kind == "q" and a.q + b.q != 0 and abs(a.q + b.q) <= CAP:
            out.append((0, 1.5, f"merge ({a.q},{b.q}) at {i}",
                        _apply_pair(i, Cell("q", a.q + b.q), Cell("slot"))))
        # pair-create into two adjacent slots (V=0)
        if a.kind == "slot" and b.kind == "slot":
            out.append((0, 2.5, f"pair-create at {i}",
                        _apply_pair(i, Cell("q", 1), Cell("q", -1))))
        # split a share into an adjacent slot (V=0)
        if a.kind == "q" and abs(a.q) == 2 and b.kind == "slot":
            half = a.q // 2
            out.append((0, 2.0, f"split {a.q} at {i}",
                        _apply_pair(i, Cell("q", half), Cell("q", half))))
        # clamp absorptions (V = |q| destroyed)
        for j, k in ((i, i + 1), (i + 1, i)):
            c, s = chain[j], chain[k]
            if c.kind == "clamp" and s.kind == "q" and s.q != 0:
                v = abs(s.q)
                floor = 3.0 + (asym if s.q < 0 else 0.0)
                out.append((v, floor, f"clamp absorbs {s.q:+d} at {k}",
                            _apply_one(k, Cell("slot"))))
    return out


def _apply_pair(i: int, new_a: Cell, new_b: Cell):
    def go(chain: List[Cell]) -> List[Cell]:
        out = [Cell(c.kind, c.q) for c in chain]
        out[i], out[i + 1] = new_a, new_b
        return out
    return go


def _apply_one(i: int, new_c: Cell):
    def go(chain: List[Cell]) -> List[Cell]:
        out = [Cell(c.kind, c.q) for c in chain]
        out[i] = new_c
        return out
    return go


def step(chain: List[Cell], asym: float = 0.0,
         rng: Optional[random.Random] = None):
    """One tick of stratified selection: lex-min (V, floor); random
    tie-break among exact ties."""
    rs = redexes(chain, asym)
    if not rs:
        return None, None
    best = min(rs, key=lambda r: (r[0], r[1]))
    ties = [r for r in rs if r[0] == best[0] and abs(r[1] - best[1]) < 1e-12]
    choice = (rng or random).choice(ties)
    return choice[3](chain), choice


def fmt(chain: List[Cell]) -> str:
    return "[" + " ".join(
        {"q": f"{c.q:+d}", "slot": "·", "clamp": "#"}[c.kind] for c in chain) + "]"


# ---------------------------------------------------------------------------
# Demos
# ---------------------------------------------------------------------------

def demo_progress(seed: int = 3) -> None:
    rng = random.Random(seed)
    chain = [Cell("q", 1), Cell("slot"), Cell("q", -1), Cell("q", 2),
             Cell("slot"), Cell("q", -2), Cell("slot")]
    q0, viol = Q(chain), 0
    for _ in range(200):
        nxt, choice = step(chain, rng=rng)
        if nxt is None:
            break
        if choice[0] > 0:
            viol += 1
        chain = nxt
    print(f"   open configuration, 200 ticks: violations selected = {viol}, "
          f"charge {q0} -> {Q(chain)}  (absolute conservation)")
    print("   -> progress holds here: a conserving redex always exists")


def demo_fv_reachability() -> None:
    chain = [Cell("q", 1), Cell("clamp"), Cell("q", -1)]
    rs = redexes(chain)
    conserving = [r for r in rs if r[0] == 0]
    print(f"   state {fmt(chain)}: conserving redexes = {len(conserving)}, "
          f"violating redexes = {len(rs) - len(conserving)}")
    print("   -> V=0-stuck but not normal: a FORCED-VIOLATION state.")
    print("      Brute typing: deadlock (no admissible move at all).")
    nxt, choice = step(chain, rng=random.Random(0))
    print(f"      ST1: selects '{choice[2]}' (V={choice[0]}) -> {fmt(nxt)}")


def demo_minimal_step() -> None:
    chain = [Cell("q", 2), Cell("clamp"), Cell("q", 1)]
    nxt, choice = step(chain, rng=random.Random(0))
    print(f"   state {fmt(chain)}: channels V=2 (absorb +2) and V=1 (absorb +1)")
    print(f"   selected: '{choice[2]}' (V={choice[0]}) -> {fmt(nxt)}")
    print("   -> forced violations take the minimal charge step")


def demo_asymmetry(n_trials: int = 2000) -> None:
    def run_ensemble(asym: float, seed: int) -> int:
        """Net charge change of the FIRST forced violation per event —
        the statistic the V-tie-break controls. (Running to exhaustion
        would let the clamp eat both neighbors, hiding the order.)"""
        rng = random.Random(seed)
        net = 0
        for _ in range(n_trials):
            s = rng.choice([1, -1])
            chain = [Cell("q", s), Cell("clamp"), Cell("q", -s)]
            while True:
                q_before = Q(chain)
                nxt, choice = step(chain, asym=asym, rng=rng)
                if nxt is None:
                    break
                chain = nxt
                if choice[0] > 0:          # first violation: record and stop
                    net += Q(chain) - q_before
                    break
        return net

    net_sym = run_ensemble(0.0, seed=42)
    net_asym = run_ensemble(0.5, seed=42)
    print(f"   {n_trials} FV events, conjugate V-tie (+1 vs -1 destruction):")
    print(f"   conjugation-symmetric floor:  net charge drift = {net_sym:+d}")
    print(f"   asymmetric floor (+0.5 to destroy negative): drift = {net_asym:+d}")
    print("   -> asymmetry needs only a finite floor bias at V-ties;")
    print("      the top stratum stays exactly conjugation-symmetric")


def demo() -> None:
    print("=" * 68)
    print("Forced-violation states (docs/22): reachability, selection, drift")
    print("=" * 68)
    print("\n1. Progress in open configurations (conservation absolute)")
    demo_progress()
    print("\n2. FV reachability: packing + clamps break progress")
    demo_fv_reachability()
    print("\n3. Minimal-step selection rule")
    demo_minimal_step()
    print("\n4. Asymmetry from floor tie-breaking (Sakharov C/CP counterpart)")
    demo_asymmetry()
    print("=" * 68)


if __name__ == "__main__":
    demo()
