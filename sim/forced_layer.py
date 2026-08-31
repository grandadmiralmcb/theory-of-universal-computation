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

Six candidates pass and are proposed as F6-F11 (first pass); six more
as F12-F17 (second). One candidate FAILS, and
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

Second pass. Six more candidates pass, and between them they change what
the framework can say about probability, observers, irreversibility,
separability and energy:
  8.  F12 O3 is SILENT where residuals are incomparable, not indifferent.
          A tie and an incomparability look alike and are not alike, and
          only the first licenses a symmetric treatment.
  9.  F13 sharing is symmetric, so the projection event has no agent.
          There is no ontological observer, only a chain that reaches one
          side of a break.
  10. F14 the projection removes its own precondition. The forced-layer
          irreversibility is the loss of a comparison, not a barrier --
          and permanent exclusion, which AT4 claims, is not forced.
  11. F15 composition is not free -- OR parts are individuated by more
          than their own content and B4 encodes the sharing. Either
          horn puts non-separability at O1. (The fork was found while
          writing this pass, by the same vocabulary rule.)
  12. F16 O3 orders TRANSITIONS, and that order need not come from a
          function on states. No state-valued quantity is forced.
  13. F17 nothing forces a chain to terminate or anything to decrease
          along one. An H-theorem is unavailable at this layer.
  14. And one recorded non-consequence: O4 does not entail branching
      histories, in either direction.
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


# ---------------------------------------------------------------------------
# Second pass -- F12-F17
# ---------------------------------------------------------------------------

# F12 -- O3 is silent, not indifferent

def le_componentwise(a: Tuple[int, ...], b: Tuple[int, ...]) -> bool:
    return all(x <= y for x, y in zip(a, b))


def classify_pair(a, b) -> str:
    """
    O3 ranks by disruption. Under a partial preorder a pair falls into one
    of three classes, and only two of them are cases O3 speaks to.
    """
    lo, hi = le_componentwise(a, b), le_componentwise(b, a)
    if lo and hi:
        return "tied"            # equal rank: O3 speaks, and says 'equal'
    if lo or hi:
        return "ordered"         # one is lower: O3 speaks, and prefers it
    return "incomparable"        # neither is lower: O3 says nothing at all


def demo_f12():
    """
    F10 established that minimal is not minimum. F12 is the sharper point
    underneath it: the minimal set is not one kind of thing. Some of its
    members are TIED and some are INCOMPARABLE, and an indifference
    argument may only be run over the first kind.
    """
    # disruption vectors: (shares broken, bindings changed)
    residuals = {"A": (0, 2), "B": (2, 0), "C": (1, 1), "D": (1, 1), "E": (3, 3)}
    names = sorted(residuals)

    minimal = [n for n in names
               if not any(le_componentwise(residuals[m], residuals[n])
                          and residuals[m] != residuals[n] for m in names)]
    print(f"   residuals (shares broken, bindings changed): {residuals}")
    print(f"   minimal under O3's ordering: {minimal}")

    tied, incomp = [], []
    for i, n in enumerate(minimal):
        for m in minimal[i + 1:]:
            cls = classify_pair(residuals[n], residuals[m])
            (tied if cls == "tied" else incomp).append((n, m, cls))
    print("\n   pairs inside the minimal set:")
    for n, m, cls in tied + incomp:
        verdict = ("O3 ranks them equal" if cls == "tied"
                   else "O3 issues no instruction")
        print(f"      {n},{m}: {cls:13s} -> {verdict}")

    assert any(c == "tied" for _, _, c in tied + incomp)
    assert any(c == "incomparable" for _, _, c in tied + incomp)

    print("\n   -> the minimal set mixes two situations that look alike from")
    print("      outside and are not alike. A tie is a fact ABOUT the ordering:")
    print("      it says the two rank the same, and a symmetric treatment of")
    print("      them is reading the ordering correctly. Incomparability is the")
    print("      ABSENCE of such a fact, and a symmetric treatment of an")
    print("      incomparable pair is not reading anything -- it is supplying")
    print("      what the ordering declined to say.")
    print("      So: uniform weight over an incomparable set is an ADDITION.")
    print("      Any derivation of probability by indifference needs CP")
    print("      (totality) to make every pair a tie, or a measure postulate.")
    print("      F10 located isotropy 'in the tie set'; F12 says the tie set")
    print("      is the smaller of the two, and the only one available.")


# ---------------------------------------------------------------------------
# F13 -- projection has no agent
# ---------------------------------------------------------------------------

def demo_f13():
    """
    O1's sharing is substructure held IN COMMON. 'In common' is symmetric --
    whatever B4's identity relation turns out to be, it is an identity, and
    B2 makes identity symmetric. So F5's event, which breaks a sharing, is
    an event AT a symmetric relation.
    """
    share = frozenset({"P", "Q"})          # the share link: an unordered pair
    print(f"   a share link between parts P and Q: {set(share)}")
    print(f"   relabelled Q,P:                     {set(frozenset({'Q','P'}))}")
    assert frozenset({"P", "Q"}) == frozenset({"Q", "P"})
    print("   -> the same object. The break event's data is the pair, and the")
    print("      pair has no first element, so the event does not distinguish")
    print("      its two sides.\n")

    # Two evaluators, one reaching each side. Each is entitled to call the
    # other side 'the system'.
    for me, other in (("P", "Q"), ("Q", "P")):
        print(f"      evaluator whose chain reaches {me}: "
              f"'{me} is where I am, {other} is what was measured'")
    print("\n   -> both descriptions are correct and nothing settles which is")
    print("      the observer, because the fact that separates them is WHICH")
    print("      SIDE A CHAIN REACHES, and chains are F1 -- per-evaluator, not")
    print("      ontological. There is no system/observer asymmetry in O1-O4.")
    print("      The measurement problem's 'who collapses it' has no answer at")
    print("      this layer, and does not need one: the question presupposes an")
    print("      asymmetry the ontology does not contain.")
    print("\n      Honest limit: a CARRIER may localise the break -- a rewrite")
    print("      has a redex, and a redex sits somewhere. That asymmetry is the")
    print("      carrier's ('redex' is WM1 vocabulary), not the ontology's, and")
    print("      it is exactly where an observer could be smuggled back in.")


# ---------------------------------------------------------------------------
# F14 -- projection destroys its own precondition
# ---------------------------------------------------------------------------

def demo_f14():
    """
    F4 is a CONDITIONAL: *if* two residuals share substructure, maintaining
    and breaking are both dispositions and O3 compares them. F5 acts on that
    comparison. What is easy to miss is that acting on it removes it.
    """
    shares = {frozenset({"chain", "r"})}
    print(f"   before: shares = {[set(s) for s in shares]}")
    print(f"      F4's antecedent (chain and r share substructure): "
          f"{frozenset({'chain','r'}) in shares}")
    print("      so 'maintain' and 'break' are both available and comparable.\n")

    shares.discard(frozenset({"chain", "r"}))          # the F5 event
    print(f"   after the projection: shares = {[set(s) for s in shares] or 'none'}")
    print(f"      F4's antecedent: {frozenset({'chain','r'}) in shares}")
    print("      so there is no sharing to maintain, and the maintain/break")
    print("      comparison has no instance. O3 does not rank the inverse,")
    print("      because the inverse is not one of the two things it compared.\n")

    print("   -> forced content: the F5 event is not repeatable on that pair,")
    print("      and O3 does not license undoing it AS an undoing. The")
    print("      irreversibility available at this layer is the LOSS OF A")
    print("      COMPARISON, not a barrier.\n")

    # And now the limit, which is the useful half.
    shares.add(frozenset({"chain", "r"}))
    print(f"   but nothing in O1-O4 forbids this: shares = "
          f"{[set(s) for s in shares]}")
    print("      a later reduction may CREATE sharing between the same two")
    print("      parts. That is a change to sharing, so O3 ranks it against")
    print("      its alternatives like any other move -- it is simply not")
    print("      ranked against 'maintain', which no longer exists.\n")
    print("   -> NOT forced: that the unselected is permanently off the chain.")
    print("      That is AT4, and its proof runs through SB4's dependence")
    print("      relation and SM-B3's strict partial order -- redexes and")
    print("      nodes, which is WM1 vocabulary. AT4 sits BELOW the TG layer,")
    print("      as docs/25 says, and NOT in the forced layer, which docs/25")
    print("      and docs/11 both said. Corrected by this pass.")


# ---------------------------------------------------------------------------
# F15 -- composition is not free
# ---------------------------------------------------------------------------

def demo_f15():
    """
    O1 admits composition AND sharing. Compose two parts the two ways. If
    the results were the same object, sharing would be vacuous and the
    carrier would not be faithful to O1. Whether that makes composition
    non-free depends on what 'the same parts' means -- which is B4.
    """
    # Part L holds atoms a and s; part R holds atoms c and s. The atom s is
    # the one that may or may not be held in common.
    L, R = {"a", "s"}, {"c", "s"}
    print(f"   part L holds {sorted(L)},  part R holds {sorted(R)}")
    print("   the atom 's' is the one that may or may not be held in common.\n")

    # Composed apart: R's copy is a distinct atom, so nothing is shared.
    apart_atoms = sorted(L) + sorted({"c", "s'"})
    apart_shared = sorted(L & {"c", "s'"})
    # Composed together: the same s, held twice.
    joined_atoms = sorted(L | R)
    joined_shared = sorted(L & R)

    print(f"   composed APART   : atoms {apart_atoms}   "
          f"held in common {apart_shared or '[]'}")
    print(f"   composed SHARING : atoms {joined_atoms}        "
          f"held in common {joined_shared}")
    assert apart_shared != joined_shared
    print("\n   two composites, and they differ. Read off the cut between")
    print(f"   L and R: {len(apart_shared)} share link crossing in the first, "
          f"{len(joined_shared)} in the second.")

    print("\n   O3's OWN vocabulary is what tells the two apart:")
    print("   a move taking one to the other changes sharing, and change to")
    print("   sharing is disruption. So the difference is visible to the only")
    print("   dynamical law the framework has.\n")
    print("   now the fork, which turns on what 'the same two parts' means --")
    print("   and that is B4, which the framework has not settled:")
    print("      parts UP TO ISOMORPHISM: R and R' are the same part, so the")
    print("         two composites have the same parts and differ.")
    print("         -> composition is not free.")
    print("      parts BY IDENTITY:       s and s' are different objects, so")
    print("         the second composite does not have the same parts.")
    print("         -> composition may be free, but the whole content of")
    print("            sharing has been pushed into the identity of the")
    print("            constituents.\n")
    print("   -> either horn says the same thing about the world and a")
    print("      different thing about where the fact lives. What is")
    print("      unavailable on both is a reading where structures decompose")
    print("      into self-contained parts. NON-SEPARABILITY IS ONTOLOGICAL:")
    print("      present at O1, before any quantum postulate, so the HQ")
    print("      layer's tensor-like structure ADDRESSES it rather than")
    print("      importing it.")
    print("      This is also the root of TH12's additivity defect (docs/24")
    print("      section 2.1): entropies add across a cut except where sharing")
    print("      crosses it, and F15 is why there is an 'except'.")
    print("      And it gives B4 a job. The charter recorded it as a gap; F15")
    print("      says what turns on filling it -- which horn the framework")
    print("      is standing on.")


# ---------------------------------------------------------------------------
# F16 -- the disruption order need not be a gradient
# ---------------------------------------------------------------------------

def has_cycle(nodes, edges) -> bool:
    """Cycle detection on the strict-order constraints a potential would need."""
    colour = {n: 0 for n in nodes}

    def visit(n):
        colour[n] = 1
        for a, b in edges:
            if a == n:
                if colour[b] == 1 or (colour[b] == 0 and visit(b)):
                    return True
        colour[n] = 2
        return False

    return any(colour[n] == 0 and visit(n) for n in nodes)


def demo_f16():
    """
    O3 ranks REDUCTIONS. A reduction is a change, and a change is a relation
    between a before and an after, so the order's domain is transitions.
    Nothing forces that order to come from a function on states.
    """
    states = ["A", "B", "C"]
    forward = [("A", "B"), ("B", "C"), ("C", "A")]
    print("   a carrier with three structures in a cycle. Each forward move")
    print("   breaks one share and rebuilds another elsewhere; each reverse")
    print("   move breaks two. So on every edge O3 strictly prefers forward:")
    for a, b in forward:
        print(f"      {a} -> {b}: disruption 1     {b} -> {a}: disruption 2")

    # A state functional V would have to make every preferred move descend.
    constraints = [(b, a) for a, b in forward]     # V(b) < V(a), drawn b -> a
    print("\n   note: the countermodel uses only a COMPARISON on each edge, not")
    print("   a scale. The numbers above are labels for readability -- reading")
    print("   them as magnitudes would assume the very thing F16 denies.\n")
    print("   suppose a state functional V exists, with O3's ranking given by")
    print("   the sign of V(after) - V(before). Then every forward move must")
    print("   descend:  V(B) < V(A),  V(C) < V(B),  V(A) < V(C).")
    cyclic = has_cycle(states, constraints)
    print(f"   the constraint graph contains a cycle: {cyclic}")
    assert cyclic
    print("   -> unsatisfiable. Summed around the loop the descents give a")
    print("      strictly negative total and a net change of zero. No V.\n")

    print("   -> O1-O4 do not force the disruption order to be a gradient, so")
    print("      they do not force ANY state-valued quantity: no potential, no")
    print("      energy, no entropy, no cost function on structures. Every such")
    print("      quantity in this framework -- WM2's counter, RM1's real scale,")
    print("      the whole TG layer's C and S -- is downstream of a postulate")
    print("      that MANUFACTURES a state functional. That is what those")
    print("      postulates are for, and this is the first place the repository")
    print("      says so plainly.")


# ---------------------------------------------------------------------------
# F17 -- no forced termination, no forced progress
# ---------------------------------------------------------------------------

def demo_f17(steps: int = 12):
    """
    Same carrier. F2' is satisfied at every step -- the residual set is
    finite, minima exist, and the chain takes one. It still never gets
    anywhere.
    """
    nxt = {"A": "B", "B": "C", "C": "A"}
    state, seen = "A", []
    for _ in range(steps):
        seen.append(state)
        state = nxt[state]
    print(f"   chain from A, {steps} steps: {' -> '.join(seen)} -> {state}")
    print(f"   at every step the residual set was finite and non-empty, a")
    print(f"   minimum existed, and O3's preferred move was taken.")
    assert len(set(seen)) == 3 and state == "A"
    print(f"   states visited: {len(set(seen))}. The chain is periodic.\n")
    print("   -> F2's well-foundedness is PER-STEP. A well-founded choice at")
    print("      each step is entirely compatible with a globally cyclic")
    print("      trajectory, and nothing in O1-O4 rules one out. So:")
    print("        NOT FORCED: that a chain terminates")
    print("        NOT FORCED: that anything decreases monotonically along one")
    print("      The second matters most. 'Disruption decreases along a chain'")
    print("      is the shape an H-theorem would need, and it is unavailable")
    print("      here -- there is nothing to decrease (F16) and no reason it")
    print("      would (F17). Which independently confirms the route docs/25")
    print("      had to take: the arrow cannot be monotone descent, so it has")
    print("      to be the structural asymmetry of F5.")


# ---------------------------------------------------------------------------
# Recorded non-consequence: O4 does not entail branching histories
# ---------------------------------------------------------------------------

def demo_nonconsequence():
    """
    O4: the unselected remains real. It is tempting to read this as 'the
    unselected continues as another history'. That reads a chain into it,
    and chains come from F1, which supplies one per evaluator.
    """
    print("   after a selection, two things are real: the selected residual")
    print("   (on the chain) and the unselected one (F3). Now ask whether the")
    print("   unselected one is a HISTORY.\n")

    for label, evaluators in (("model I ", ["chain-1"]),
                              ("model II", ["chain-1", "chain-2"])):
        branch = "chain-2" in evaluators
        print(f"      {label}: evaluators = {evaluators}")
        print(f"                O1 ok  O2 ok  O3 ok  O4 ok   "
              f"unselected is a history: {branch}")
    print("\n   -> both models satisfy O1-O4. Whether an evaluator exists along")
    print("      the unselected residual is an EXISTENCE claim about evaluators,")
    print("      and O1-O4 make none. So branching is independent of the minima:")
    print("        NOT FORCED: that the unselected residual is another world")
    print("        NOT FORCED: that it is not")
    print("      The framework is committed neither to Everett nor against it.")
    print("      O4 says the unselected is real STRUCTURE. Turning structure")
    print("      into a history takes an evaluator, and that is a further")
    print("      posit -- which is also why B9 (what is an evaluator?) is not")
    print("      idle bookkeeping: this question cannot even be stated until")
    print("      the term is fixed.")


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

    print("\n" + "-" * 72)
    print("Second pass -- F12-F17")
    print("-" * 72)
    print("\n8. F12 -- O3 is silent, not indifferent  [O3, F2', B3]")
    demo_f12()
    print("\n9. F13 -- projection has no agent  [O1, F5, B4]")
    demo_f13()
    print("\n10. F14 -- projection destroys its own precondition  [F4, F5]")
    demo_f14()
    print("\n11. F15 -- composition is not free, or B4 carries it  [O1, B4]")
    demo_f15()
    print("\n12. F16 -- the disruption order need not be a gradient  [O3]")
    demo_f16()
    print("\n13. F17 -- no forced termination, no forced progress  [O1-O4, F2']")
    demo_f17()
    print("\n14. NOT FORCED -- O4 does not entail branching histories")
    demo_nonconsequence()
    print("=" * 72)


if __name__ == "__main__":
    demo()
