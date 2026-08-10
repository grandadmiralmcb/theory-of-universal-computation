#!/usr/bin/env python3
"""
Progress analysis of the WM conserving fragment
===============================================
Executable companion to docs/23-progress-analysis.md — the successor
target of docs/22 §6: does the actual working-model calculus (app, abs,
pair/proj with labeled shares under ST1) admit reachable forced-
violation states?

Mini sharing calculus:
  Var | Abs(x, body) | App(f, a) | Pair(a, b) | Proj(i, t) | SRef(share)
Shares are objects with identity and integer charge; SRef nodes are
references. Substitution copies term structure but REUSES Share objects
— sharing is by reference, so duplication of a reference never
duplicates charge (PA0).

Violation accounting: a step's V = total |q| of charged shares present
before but unreachable after (support diff by object identity). The
only V>0 channels are DISCARDS: K-redexes (argument dropped because
the bound variable does not occur) and unprojected pair components.

Demonstrations:
  1. PA0 — duplication is charge-safe: (\\x. <x,x>) S duplicates the
     REFERENCE; Q counts the share once; conserved.
  2. PA2 — reachable forced violation: (\\f. f S)(\\x. c) has only a
     conserving redex, but ONE conserving step yields (\\x. c) S whose
     only redex discards the charged share. Progress fails for the
     unrestricted calculus, non-trivially.
  3. Projection discard: proj1 <c, S> destroys S (V=1); the projected-
     side variant keeps it (V=0).
  4. Reference subtlety: discarding one reference to a still-shared
     share is conserving (V=0) — only the LAST reference's loss
     destroys charge.
  5. Charge-relevance checker (conservative, lambda-I-style): accepts
     only terms where no charged share can flow to a discard position;
     dynamic audit confirms V=0 runs on accepted terms. Incompleteness
     shown honestly (a safe higher-order term is rejected).
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import List, Optional, Set, Tuple

# ---------------------------------------------------------------------------
# Terms
# ---------------------------------------------------------------------------

class Share:
    def __init__(self, name: str, q: int):
        self.name, self.q = name, q

    def __repr__(self):
        return f"{self.name}({self.q:+d})" if self.q else f"{self.name}(0)"


@dataclass
class Var:
    name: str


@dataclass
class Abs:
    x: str
    body: object


@dataclass
class App:
    f: object
    a: object


@dataclass
class Pair:
    a: object
    b: object


@dataclass
class Proj:
    i: int
    t: object


@dataclass
class SRef:
    share: Share


def show(t) -> str:
    if isinstance(t, Var):
        return t.name
    if isinstance(t, Abs):
        return f"(\\{t.x}. {show(t.body)})"
    if isinstance(t, App):
        return f"({show(t.f)} {show(t.a)})"
    if isinstance(t, Pair):
        return f"<{show(t.a)}, {show(t.b)}>"
    if isinstance(t, Proj):
        return f"proj{t.i} {show(t.t)}"
    if isinstance(t, SRef):
        return repr(t.share)
    return "?"


def fv(t) -> Set[str]:
    if isinstance(t, Var):
        return {t.name}
    if isinstance(t, Abs):
        return fv(t.body) - {t.x}
    if isinstance(t, App):
        return fv(t.f) | fv(t.a)
    if isinstance(t, Pair):
        return fv(t.a) | fv(t.b)
    if isinstance(t, Proj):
        return fv(t.t)
    return set()


def support(t, out: Optional[dict] = None) -> dict:
    """Distinct Share objects reachable in t (by identity)."""
    if out is None:
        out = {}
    if isinstance(t, SRef):
        out[id(t.share)] = t.share
    elif isinstance(t, Abs):
        support(t.body, out)
    elif isinstance(t, App):
        support(t.f, out), support(t.a, out)
    elif isinstance(t, Pair):
        support(t.a, out), support(t.b, out)
    elif isinstance(t, Proj):
        support(t.t, out)
    return out


def Q(t) -> int:
    return sum(s.q for s in support(t).values())


def subst(t, x: str, n):
    """Capture-naive substitution (examples use distinct names).
    Share objects are REUSED — sharing is by reference."""
    if isinstance(t, Var):
        return n if t.name == x else t
    if isinstance(t, Abs):
        return t if t.x == x else Abs(t.x, subst(t.body, x, n))
    if isinstance(t, App):
        return App(subst(t.f, x, n), subst(t.a, x, n))
    if isinstance(t, Pair):
        return Pair(subst(t.a, x, n), subst(t.b, x, n))
    if isinstance(t, Proj):
        return Proj(t.i, subst(t.t, x, n))
    return t


# ---------------------------------------------------------------------------
# Reduction: enumerate redexes, apply, account violations by support diff
# ---------------------------------------------------------------------------

def redexes(t, path=()) -> List[Tuple[tuple, str]]:
    out = []
    if isinstance(t, App) and isinstance(t.f, Abs):
        kind = "beta" if t.f.x in fv(t.f.body) else "beta-K(discard)"
        out.append((path, kind))
    if isinstance(t, Proj) and isinstance(t.t, Pair):
        out.append((path, f"proj{t.i}(discard other)"))
    if isinstance(t, Abs):
        out += redexes(t.body, path + ("b",))
    if isinstance(t, App):
        out += redexes(t.f, path + ("f",)) + redexes(t.a, path + ("a",))
    if isinstance(t, Pair):
        out += redexes(t.a, path + ("a",)) + redexes(t.b, path + ("b",))
    if isinstance(t, Proj):
        out += redexes(t.t, path + ("t",))
    return out


def apply_at(t, path):
    if not path:
        if isinstance(t, App) and isinstance(t.f, Abs):
            return subst(t.f.body, t.f.x, t.a)
        if isinstance(t, Proj) and isinstance(t.t, Pair):
            return t.t.a if t.i == 1 else t.t.b
        raise ValueError("no redex at path")
    h, rest = path[0], path[1:]
    if isinstance(t, Abs):
        return Abs(t.x, apply_at(t.body, rest))
    if isinstance(t, App):
        return App(apply_at(t.f, rest), t.a) if h == "f" else App(t.f, apply_at(t.a, rest))
    if isinstance(t, Pair):
        return Pair(apply_at(t.a, rest), t.b) if h == "a" else Pair(t.a, apply_at(t.b, rest))
    if isinstance(t, Proj):
        return Proj(t.i, apply_at(t.t, rest))
    raise ValueError("bad path")


def step(t):
    """Stratified selection: lex-min (V, leftmost-outermost order)."""
    cands = []
    for idx, (path, kind) in enumerate(redexes(t)):
        t2 = apply_at(t, path)
        lost = {i: s for i, s in support(t).items() if i not in support(t2)}
        V = sum(abs(s.q) for s in lost.values())
        cands.append((V, idx, kind, t2, lost))
    if not cands:
        return None
    return min(cands, key=lambda c: (c[0], c[1]))


def run(t, cap: int = 40, verbose: bool = False):
    violations = 0
    for _ in range(cap):
        r = step(t)
        if r is None:
            break
        V, _, kind, t2, lost = r
        if verbose:
            note = f"  V={V}" + (f" destroys {list(lost.values())}" if V else "")
            print(f"     {show(t)}  --[{kind}]-->  {show(t2)}{note}")
        violations += 1 if V > 0 else 0
        t = t2
    return t, violations


# ---------------------------------------------------------------------------
# Conservative charge-relevance checker (lambda-I relativized to charge)
# ---------------------------------------------------------------------------

def has_charge(t) -> bool:
    return any(s.q != 0 for s in support(t).values())


def charge_relevant(t) -> bool:
    """Conservative static check: no charged share may sit in a discard
    position (K-redex argument; unprojected pair component) or flow to
    an unknown consumer. Incomplete by design, like any type system."""
    if isinstance(t, App):
        if isinstance(t.f, Abs):
            if t.f.x not in fv(t.f.body) and has_charge(t.a):
                return False
            return charge_relevant(t.f.body) and charge_relevant(t.a)
        # unknown consumer of a charged argument: reject conservatively
        if has_charge(t.a):
            return False
        return charge_relevant(t.f) and charge_relevant(t.a)
    if isinstance(t, Proj):
        if isinstance(t.t, Pair):
            dropped = t.t.b if t.i == 1 else t.t.a
            if has_charge(dropped):
                return False
            return charge_relevant(t.t.a) and charge_relevant(t.t.b)
        if has_charge(t.t):
            return False
        return charge_relevant(t.t)
    if isinstance(t, Abs):
        return charge_relevant(t.body)
    if isinstance(t, Pair):
        return charge_relevant(t.a) and charge_relevant(t.b)
    return True


# ---------------------------------------------------------------------------
# Demos
# ---------------------------------------------------------------------------

def demo():
    print("=" * 68)
    print("Progress analysis of the WM conserving fragment (docs/23)")
    print("=" * 68)

    print("\n1. PA0 — duplication is charge-safe (sharing by reference)")
    S = Share("S", 1)
    t = App(Abs("x", Pair(Var("x"), Var("x"))), SRef(S))
    print(f"   {show(t)}   Q = {Q(t)}")
    t2, v = run(t)
    print(f"   -> {show(t2)}   Q = {Q(t2)}, violations = {v}")
    print("   (two references, one share: contraction conserves charge for free)")

    print("\n2. PA2 — reachable forced violation (progress fails, non-trivially)")
    S = Share("S", 1)
    C = Share("c", 0)
    t = App(Abs("f", App(Var("f"), SRef(S))), Abs("x", SRef(C)))
    print(f"   initial: {show(t)}   Q = {Q(t)}  (only redex is conserving)")
    tt, v = run(t, verbose=True)
    print(f"   final Q = {Q(tt)}, violations = {v}")
    print("   -> one conserving step reaches a state whose ONLY redex is a")
    print("      charged discard: a forced-violation state of the real calculus")

    print("\n3. Projection discard vs projection keep")
    S = Share("S", 1)
    C = Share("c", 0)
    bad = Proj(1, Pair(SRef(C), SRef(S)))
    good = Proj(1, Pair(SRef(S), SRef(C)))
    for name, t in (("proj1 <c, S>", bad), ("proj1 <S, c>", good)):
        t2, v = run(t)
        print(f"   {name}: -> {show(t2)}  violations = {v}")

    print("\n4. Discarding one reference to a still-shared share is conserving")
    S = Share("S", 1)
    C = Share("c", 0)
    t = Pair(SRef(S), App(Abs("x", SRef(C)), SRef(S)))
    print(f"   {show(t)}   Q = {Q(t)}")
    t2, v = run(t)
    print(f"   -> {show(t2)}   Q = {Q(t2)}, violations = {v}")
    print("   (the K-redex drops a reference, not the share: V = 0)")

    print("\n5. Charge-relevance checker vs dynamic audit")
    S1, S2, S3, S4 = (Share("S", 1) for _ in range(4))
    C1, C2 = Share("c", 0), Share("c", 0)
    cases = [
        ("K-redex on charge", App(Abs("x", SRef(C1)), SRef(S1))),
        ("proj discards charge", Proj(1, Pair(SRef(C2), SRef(S2)))),
        ("relevant use", App(Abs("x", Pair(Var("x"), Var("x"))), SRef(S3))),
        ("safe higher-order (rejected: checker incompleteness)",
         App(Abs("f", App(Var("f"), SRef(S4))), Abs("y", Pair(Var("y"), Var("y"))))),
    ]
    print("   case                                              checker  audit-violations")
    for name, t in cases:
        ok = charge_relevant(t)
        _, v = run(t)
        print(f"   {name:49s} {'PASS' if ok else 'FAIL':7s} {v}")
    print("   -> accepted terms audit clean (PA1 pattern); rejections are")
    print("      conservative — the last case is safe but unprovable statically")
    print("=" * 68)


if __name__ == "__main__":
    demo()
