# 27 — Mathematics from the Minima

*Status: derivation document. Asks how much of mathematics O1–O4 supply, and in particular how far geometry can be taken before a manifold has to be assumed. The answer is further than the framework has been claiming. **Topology, metric, measure and curvature are all derivable or definable with no geometric assumption anywhere**; what is missing is specifically manifoldlikeness. That narrows contention 9 from a vague debt to a precise question in an active area of mathematics. Executable: `sim/metric_from_cost.py`.*

Authority: `docs/00-theory-charter.md`. Spine and stage ordering: `docs/26`. Theorems: `docs/11`.

---

## 1. The branches, in one view

| Branch | Comes from | Route | Status |
|---|---|---|---|
| Category structure | O1 composition + sharing | sharing is a span, gluing is a pushout | **Conjectured** (docs/26 §7.1) |
| Propositional logic | O1 subobject lattice | lattice of parts | **Definable**, and intuitionistic rather than classical |
| Order theory | O2 | reduction chains; SM-B3's partial order | **Forced** |
| \(\mathbb{N}\) | O2 iteration | successor = one more step | **Forced** |
| \(\mathbb{R}\) | O3 + additivity + Archimedean | Hölder representation (RM1) | **Derived**, conditional on CP/CC′ |
| Non-Archimedean number | O3 without Archimedean | Hahn series (RM2) | **Derived**, the other branch |
| Topology | O2's order | Alexandrov topology on intervals | **Forced** |
| **Metric** | **O1 + O3** | **least-cost path; Lawvere enrichment** | **Forced** — §4 |
| Measure | counting structures | O4 keeps the unselected countable | **Definable** |
| **Curvature** | metric + measure | Ollivier's coarse Ricci | **Definable** — §5 |
| Manifold geometry | all of the above + TG2 | — | **Assumed. Still the gate** |

The shape of that table is the document's point. The gap is not at "geometry". It is one line lower, at "manifold".

---

## 2. From O1 — composition, sharing, and a logic

O1 gives patterns that compose and that can share substructure. Two structures sharing a part are a span \(A \leftarrow S \rightarrow B\); gluing them along the shared part is a pushout. Rewriting that respects sharing is double-pushout rewriting, which is well behaved exactly in **adhesive categories** — the carrier-representation conjecture of `docs/26` §7.1.

Once subobjects behave, the parts of a structure form a lattice, and a lattice of parts is a propositional logic. Two things are worth saying about which logic appears.

It is **not classical**, and that is the expected answer rather than a disappointment. O4 says the residuals that were not selected remain real. A logic that asserted "either this residual was selected or it was not" before selection occurred would be asserting excluded middle where the framework denies it applies. Intuitionistic logic is the one that declines to. *This is a reading rather than a theorem*, and it is offered as motivation for looking, not as a result.

---

## 3. From O2 and O3 — the two number systems, with different parents

The counting numbers come from O2. A reduction chain is an iteration, its steps are countable, and F2′'s well-foundedness gives induction. **\(\mathbb{N}\) is temporal**: it counts steps.

The real numbers come from O3, and this is already proved in the repository without having been read this way. RM1 takes the disruption order with additivity and the Archimedean property and produces, by Hölder's theorem, an embedding into \((\mathbb{R}_{\ge0}, +)\) unique up to positive scale. **\(\mathbb{R}\) is axiological**: it measures preference. RM2 says the alternative branch, dropping Archimedean, gives Hahn series instead.

That is a genuine structural claim about where the continuum enters. In most of physics the real line arrives with space and is never questioned. Here it arrives with *value*, from an ordering on how disruptive things are, and space has not been mentioned yet.

Topology arrives with the order rather than with the metric. SM-B3 gives a strict partial order on events, and an order carries the Alexandrov topology of its intervals with nothing added. **Geometry's first layer is free.**

---

## 4. The metric was already there

This is the section that changes the shape of the geometric debt.

**Definition.** For structures \(A, B\), let
\[
d(A,B) \;=\; \inf_{\text{reduction paths } A \to B}\ \sum_{\text{steps}} C(\text{step}).
\]

**Theorem MG1 (the cost structure is a metric).** [O1, O3, WM2] \(d\) satisfies
\(d(A,A)=0\), \(d \ge 0\), and \(d(A,C) \le d(A,B) + d(B,C)\).

*Proof.* The empty path gives the first. WM2's counters are non-negative, giving the second. Concatenating a path \(A\to B\) with a path \(B \to C\) is a path \(A \to C\), so the infimum over all \(A\to C\) paths is at most the sum of the two infima. ∎ (Executable: `sim/metric_from_cost.py` §1.)

**What kind of object that is.** Those are exactly Lawvere's axioms for a metric space regarded as a category enriched over \(([0,\infty], \ge, +)\): identity gives \(d(x,x)=0\) and composition gives the triangle inequality. **Symmetry and separation are additional conditions, not part of the definition.**

So the framework does not lack a metric. It has had one since O3, and it is a *generalised* metric in the precise sense — asymmetric, because reduction runs one way. That asymmetry is not damage to be repaired. It is the same directionality AT3 identified as the arrow of time, appearing in the metric where it belongs, and the sim exhibits it: on a one-way chain \(d(0,5)=5\) while \(d(5,0)\) is infinite, with identity, non-negativity and the triangle inequality all still holding.

**What the metric is on.** Configuration space, not physical space. The distance between two *structures* is the least disruption needed to turn one into the other. So the geometric question changes shape:

> Not "where does a metric come from?" — there is one. But "does physical space appear as a low-dimensional substructure of configuration-space geometry?"

---

## 5. Curvature, with no manifold

A metric together with a measure is enough for curvature, by a construction that never mentions a chart. Ollivier's coarse Ricci curvature compares the cost of transporting the neighbourhood of \(x\) onto the neighbourhood of \(y\) against the distance between them:
\[
\kappa(x,y) \;=\; 1 - \frac{W_1(m_x, m_y)}{d(x,y)}.
\]
Positive means neighbours are closer than their centres are; negative means they are further apart.

`sim/metric_from_cost.py` §2 computes this exactly, by min-cost flow rather than approximation, on structures the framework can build:

| Structure | Interior \(\kappa\) | Analytic value | Reading |
|---|---|---|---|
| Tree, branching 2 | \(-0.3333\) | \(-1/3\) | negative |
| Tree, branching 3 | \(-0.5000\) | \(-1/2\) | negative |
| Cycle | \(0.0000\) | \(0\) | flat |
| Flat lattice, 2-D | \(0.0000\) | \(0\) | flat |
| Flat lattice, 3-D | \(0.0000\) | \(0\) | flat |
| Clique, 8 nodes | \(0.5714\) | \(4/7\) | positive |

The computed values are the exact analytic ones, which is the check that the transport is right rather than merely plausible.

**Theorem MG2 (curvature is definable).** [MG1, counting measure] Ollivier curvature is well defined on any structure carrying the cost metric, needs no manifold, no chart and no dimension, and agrees with the classical answer wherever there is one. ∎

**A methodological note worth keeping.** The first run of this measurement averaged over every edge and reported binary trees as *flat*, which is the wrong sign. A finite structure is mostly boundary, and boundary edges are positively curved because mass at a leaf has nowhere to spread. Averaging over all edges reports the shape of the cut-off rather than the shape of the structure. The sim now measures interior edges and prints the all-edge figure beside it so the artefact stays visible.

**Why this matters for TH6.** The Einstein equation is a statement about Ricci curvature. If Ricci curvature is definable on the framework's own structures without a manifold, then the field equation has a chance of being *stated* — and eventually checked — on the discrete side of the TG2 gate rather than only past it. That is a research target, not a result: Ollivier's is a coarse Ricci, and relating it to the full curvature tensor takes more than is done here.

---

## 6. What is actually missing

The debt is narrower than `docs/26` §4 recorded, and the narrowing is worth stating precisely.

**Not missing:** topology (§3), metric (§4), measure, curvature (§5).

**Missing: manifoldlikeness.** That the metric space is locally like \(\mathbb{R}^n\), with a dimension, and with Lorentzian rather than Riemannian signature.

The sim makes the limit concrete rather than rhetorical: flat 2-D and flat 3-D lattices both return \(\kappa = 0\) exactly. **Curvature does not know its own dimension.** So curvature narrows the debt without discharging it, and dimension needs the separate estimators of `docs/26` §4.

**The named target.** There is an existing branch of mathematics shaped exactly like what this framework has: a causal order together with a separation function obeying a *reverse* triangle inequality. **Lorentzian length spaces** (Kunzinger–Sämann) are the synthetic account of Lorentzian geometry, standing to Lorentzian manifolds as metric length spaces stand to Riemannian ones. The framework supplies a causal order (SM-B3) and a cost (MG1). So the question to ask is not the vague one:

> ~~Does a manifold emerge from the reduction order?~~
> **Is the structure a Lorentzian length space?**

That is precise, it is answerable, and it is being worked on by people who are not us. Recording it is the most useful thing this document does for contention 9.

**One caution about the signature.** The cost metric's asymmetry and the reverse triangle inequality of Lorentzian separation are both expressions of one-way-ness, and it is tempting to identify them. They are not obviously the same thing: an asymmetric metric still has \(d(A,C) \le d(A,B)+d(B,C)\), while Lorentzian separation reverses that inequality. Whether the framework's cost can be turned into a time-separation function with the reverse inequality is open, and it is the first thing to check on the Lorentzian-length-space route.

---

## 7. Labels

| Result | Label |
|---|---|
| **MG1** the cost structure is a Lawvere metric | Forced given WM2 |
| **MG2** curvature is definable, and correct where checkable | Forced given MG1 |
| \(\mathbb{N}\) from iteration, topology from the order | Forced |
| \(\mathbb{R}\) from Hölder (RM1) | Derived, conditional on CP and CC′ |
| Adhesive-category carrier | Conjectured |
| Intuitionistic rather than classical logic | Reading |
| Physical space inside configuration-space geometry | Open |
| Manifoldlikeness, dimension, signature | **Assumed (TG2). The gate is here and nowhere earlier** |

---

## 8. Executable

`sim/metric_from_cost.py`:

1. **MG1** — identity, non-negativity and the triangle inequality verified on structure graphs; asymmetry exhibited on a one-way chain, where \(d(0,5)=5\) and \(d(5,0)\) is unreachable.
2. **MG2** — Ollivier curvature by exact min-cost flow, reproducing \(-1/3\), \(-1/2\), \(0\), \(0\), \(0\) and \(4/7\) analytically, with the all-edge average printed alongside to keep the boundary artefact visible.
3. **The limit** — 2-D and 3-D flat lattices both returning exactly zero, which is the numerical form of "curvature does not know its own dimension".
