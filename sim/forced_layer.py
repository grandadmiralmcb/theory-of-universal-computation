#!/usr/bin/env python3
"""
The forced layer, audited
=========================
Executable companion to docs/28-forced-layer-audit.md.

Six results carried the whole framework: F1-F5 with the F2' tightening.
This runs the audit docs/26 section 7 opened, using carrier-invariance as
the test: a result forced by O1-O4 must hold in every faithful carrier,
so anything holding only for finite terms is using WM1 and belongs one
layer down.

Six candidates pass and are proposed as F6-F11. One candidate FAILS, and
the failure is the more useful half of the exercise: "structure cannot
cease" was claimed in docs/26 stage 0 as forced from O4, and a countermodel
here shows it is not. O4 constrains selection, not reduction.

Demonstrations:
  1. F6  no global order -- and, separately, the carrier-level fact that
         in THIS carrier every linearisation yields the same outcome.
         The first is forced; the second is not, and the demo is honest
         about which is which (docs/28 section 2.1).
  2. F7  selection is non-destructive, and the sharper claim is not.
  3. F8  accessibility is proper: no chain holds all real structure.
  4. F9  preference is structurally determined.
  5. F10 selection need not be unique -- minimal is not minimum.
  6. F11 order carries no orientation (AT2 promoted out of the AT layer).
  7. The REJECTION: a carrier satisfying O1-O4 in which reduction reaches
     the empty structure, so persistence is forced-given-WM1 and not
     forced by the minima.
"""

from __future__ import annotations
from itertools import permutations
from typing import Dict, FrozenSet, List, Sequence, Set, Tuple


# ---------------------------------------------------------------------------
# F6 -- interleaving independence
# ---------------------------------------------------------------------------

def linearisations(events: Sequence[str], dep: Dict[str, Set[str]]) -> List[Tuple[str, ...]]:
    """Every total order extending the dependence order."""
    out = []
    for p in permutations(events):
        pos = {e: i for i, e in enumerate(p)}
        if all(pos[d] < pos[e] for e in events for d in dep.get(e, ())):
            out.append(p)
    return out


def run(order: Sequence[str], ops: Dict[str, Tuple[str, str]]) -> FrozenSet[Tuple[str, str]]:
    """
    Apply events in the given order. Each event adds one share link.
    Independent events touch disjoint sites, so they commute.
    """
    state: Set[Tuple[str, str]] = set()
    for e in order:
        state.add(ops[e])
    return frozenset(state)


def causal_closure(events, dep) -> FrozenSet[Tuple[str, str]]:
    reach = {e: set(dep.get(e, ())) for e in events}
    changed = True
    while changed:
        changed = False
        for e in events:
            for d in list(reach[e]):
                for dd in reach.get(d, ()):
                    if dd not in reach[e]:
                        reach[e].add(dd); changed = True
    return frozenset((d, e) for e in events for d in reach[e])


def demo_f6():
    events = ["a", "b", "c", "d"]
    dep = {"c": {"a"}, "d": {"b"}}          # a<c and b<d; a,b and c,d independent
    ops = {"a": ("x", "p"), "b": ("y", "q"), "c": ("x", "r"), "d": ("y", "s")}
    lins = linearisations(events, dep)
    outs = {run(l, ops) for l in lins}
    caus = {causal_closure(events, dep) for _ in lins}
    print(f"      dependence order: a < c,  b < d   (a,b independent; c,d independent)")
    print(f"      distinct linearisations : {len(lins)}")
    print(f"      distinct outcomes       : {len(outs)}")
    print(f"      distinct causal orders  : {len(caus)}")
    assert len(lins) > 1 and len(outs) == 1 and len(caus) == 1
    print("\n   FORCED (F6, from O2 + F1): more than one sequentialisation exists")
    print("   and nothing determines an order between a and b. Not an unknown")
    print("   order -- none. Hence no global 'now' and no privileged global state.")
    print("\n   NOT FORCED: that the outcome is the same across linearisations.")
    print("   That needs disjoint reductions to COMMUTE, which is a property of")
    print("   the carrier. Here composition is set union, which commutes")
    print("   trivially, so the one outcome above CONFIRMS the claim in a carrier")
    print("   that has it -- it does not establish it in general. WM1 has it as a")
    print("   lemma and SM-B3's proof sketch cites that lemma. See docs/28 s2.1;")
    print("   'dependence order' is itself SB4's phrase, and SB4 is a postulate.")


# ---------------------------------------------------------------------------
# F7 -- selection is non-destructive (and the sharper claim is not)
# ---------------------------------------------------------------------------

def demo_f7():
    admissible = {"r1", "r2", "r3"}
    print(f"      admissible residuals at this state : {sorted(admissible)}")
    for chosen in sorted(admissible):
        persisting = admissible - {chosen}          # O4: the rest remain real
        total = {chosen} | persisting
        print(f"        select {chosen}: on-chain {{{chosen}}}, "
              f"still real {sorted(persisting)}, total {len(total)}")
        assert total == admissible
    print("   -> whichever is selected, the totality of real structure is unchanged.")
    print("      That is all O4 gives, and it is genuinely forced.")


# ---------------------------------------------------------------------------
# F8 -- accessibility is proper
# ---------------------------------------------------------------------------

def demo_f8(depth: int = 4, branch: int = 2):
    """A chain makes one selection per step; O4 keeps the rest real."""
    chain, real = [], set()
    node = ()
    for _ in range(depth):
        options = [node + (i,) for i in range(branch)]
        real.update(options)
        node = options[0]                            # some minimal one is selected
        chain.append(node)
    print(f"      after {depth} selections, {branch} options each:")
    print(f"        events on the chain : {len(chain)}")
    print(f"        events that are real: {len(real)}")
    assert set(chain) < real
    print("   -> the chain is a PROPER subset of what is real. No evaluator's")
    print("      record contains all real structure. This is the root of horizons")
    print("      (TH3), of the measurement account, and of the interface reading,")
    print("      and it needs neither SB4 nor A4 -- only F1, F2 and O4.")


# ---------------------------------------------------------------------------
# F9 -- preference is structurally determined
# ---------------------------------------------------------------------------

def demo_f9():
    """
    O3 defines disruption as change to sharing, binding or identity. So a
    preference that varied while the change-set was held fixed would not be
    a preference over disruption at all. Analytic, not empirical.
    """
    def change_set(ev):
        return (ev["shares_broken"], ev["bindings_opened"], ev["identity_changed"])

    a = {"shares_broken": 2, "bindings_opened": 1, "identity_changed": True,
         "weight": 0.9, "label": "alpha", "position": 17}
    b = {"shares_broken": 2, "bindings_opened": 1, "identity_changed": True,
         "weight": 0.1, "label": "omega", "position": 3}
    print(f"      event A change-set {change_set(a)}  non-structural data: weight .9, 'alpha', pos 17")
    print(f"      event B change-set {change_set(b)}  non-structural data: weight .1, 'omega', pos 3")
    assert change_set(a) == change_set(b)
    print("   -> identical change-sets. O3 ranks disruption, and disruption is")
    print("      defined as these changes, so nothing else can enter the ranking.")
    print("      This is the root of T17's weight-blindness, which currently")
    print("      carries [WM2, D19-typing, A4] and needs none of them.")
    print("      Note the WEAK form only: that isomorphic change-sets rank EQUALLY")
    print("      is stronger (PC), and needs the reading SI (docs/20 section 2).")


# ---------------------------------------------------------------------------
# F10 -- selection need not be unique
# ---------------------------------------------------------------------------

def demo_f10():
    """Under a partial preorder, minimal is not minimum."""
    # componentwise order on N^2 -- docs/20 section 4's own countermodel
    cand = {"r1": (2, 0), "r2": (0, 1), "r3": (3, 2)}
    def leq(x, y): return x[0] <= y[0] and x[1] <= y[1]
    minimal = [k for k, v in cand.items()
               if not any(leq(w, v) and w != v for u, w in cand.items() if u != k)]
    print(f"      residual disruptions (componentwise order): {cand}")
    print(f"      minimal elements: {sorted(minimal)}")
    assert len(minimal) > 1
    print("   -> two minimal residuals and no minimum. O3 licenses selecting A")
    print("      minimal one; it does not single one out. So selection is not")
    print("      forced to be deterministic, and the tie set is where any")
    print("      isotropy would have to live (docs/26 stage 2, docs/27 section 6).")


# ---------------------------------------------------------------------------
# F11 -- order carries no orientation
# ---------------------------------------------------------------------------

def demo_f11():
    events = ["e1", "e2", "e3", "e4"]
    rel = {("e1", "e2"), ("e2", "e3"), ("e1", "e3"), ("e1", "e4")}
    conv = {(b, a) for a, b in rel}
    def strict_partial(r, dom):
        irrefl = all((x, x) not in r for x in dom)
        trans = all((a, c) in r for a, b in r for b2, c in r if b == b2)
        return irrefl and trans
    print(f"      relation      is a strict partial order: {strict_partial(rel, events)}")
    print(f"      its converse  is a strict partial order: {strict_partial(conv, events)}")
    assert strict_partial(rel, events) and strict_partial(conv, events)
    print("   -> both. Irreflexivity and transitivity survive reversal, so the")
    print("      order fixes which events neighbour which and says nothing about")
    print("      which end is the past. Promoted out of the AT layer: it is a fact")
    print("      about orders, and no working model enters.")


# ---------------------------------------------------------------------------
# The rejection: persistence is NOT forced
# ---------------------------------------------------------------------------

def demo_rejection():
    """
    docs/26 stage 0 says structure cannot cease, citing O4 plus the absence
    of an annihilation move. The second clause is a fact about WM1, not
    about O1-O4. Here is a carrier that satisfies the minima and annihilates.
    """
    print("   carrier: finite multisets of atoms, some atoms shared between parts.")
    print("     O1 composition = union; sharing = an atom held by two parts. ok")
    print("     O2 order built by successive reduction steps.               ok")
    print("     O3 prefer the reduction removing fewest shared atoms.       ok")
    print("     O4 unselected reductions' results remain real.              ok")
    print("   reduction rule: 'discard' removes one atom.\n")
    state = {"a", "b", "c"}
    step = 0
    while state:
        drop = sorted(state)[0]
        state = state - {drop}
        step += 1
        print(f"      step {step}: discard {drop!r} -> {sorted(state) if state else 'EMPTY'}")
    assert state == set()
    print("\n   -> the empty structure is reachable, in a carrier meeting O1-O4.")
    print("      O4 says the residuals NOT SELECTED remain real. It says nothing")
    print("      about whether a reduction may destroy what it acts on. So:")
    print("        FORCED     : selection is non-destructive (F7)")
    print("        NOT FORCED : structure cannot cease")
    print("      The stronger claim needs WM1's rule set, which has no")
    print("      annihilation rule. docs/26 stage 0 overstated it, and this")
    print("      countermodel is the audit's test doing its job.")


def demo():
    print("=" * 72)
    print("The forced layer, audited (docs/28)")
    print("=" * 72)
    print("\n1. F6 -- no global order  [O2, F1]  (and one carrier-level rider)")
    demo_f6()
    print("\n2. F7 -- selection is non-destructive  [O4]")
    demo_f7()
    print("\n3. F8 -- accessibility is proper  [F1, F2, O4]")
    demo_f8()
    print("\n4. F9 -- preference is structurally determined  [O3, analytic]")
    demo_f9()
    print("\n5. F10 -- selection need not be unique  [F2']")
    demo_f10()
    print("\n6. F11 -- order carries no orientation  [O2]")
    demo_f11()
    print("\n7. REJECTED -- 'structure cannot cease' is not forced by O1-O4")
    demo_rejection()
    print("=" * 72)


if __name__ == "__main__":
    demo()
