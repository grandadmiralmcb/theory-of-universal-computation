# 26 — The Outward Spine

*Status: organising document. `docs/14` derives outward from O1–O4 as far as physics. This one continues the same spine through the stages it never reached, in dependency order: origin, distinction, computation, value, geometry, ontology. Each stage states what it derives, from what, under which label, and what is still empty. It also fixes the presentation rule (§8) and opens the forced-layer audit (§7).*

Authority: `docs/00-theory-charter.md`. Derivation spine for the physics stages: `docs/14`. Theorems with hypotheses: `docs/11`.

**Why an ordering.** The repository grew historically — the quantum sector early, thermodynamics late — so its numbering records when things were written rather than what rests on what. The stages below are ordered so that each uses only the stages before it. Nothing is re-derived here; the work is placing existing results on the rungs they actually occupy, and making the empty rungs visible as rungs rather than as absences.

---

## 0. Stage zero — origin and persistence

The question that precedes every other stage is why there is any structure at all, and it has a sharp form in this framework rather than only a rhetorical one.

**The sharp form.** O3 prefers lower disruption. Nothing appears to be the least disruptive arrangement available, so why does the world not collapse into it?

**Why it does not.** O3 ranks *reductions*, not configurations. Cost in WM2 is charged to a step, so a configuration has no cost to compare while sitting still, and "nothing is cheapest" is a category error rather than a competing option. There is also no move to reach it by: reduction rewrites structure, and the calculus has no global annihilation operator. Nothing does not lose the competition; it does not enter it.

**Why structure cannot cease.** O4 says non-selection is not non-existence. Selection is the only thing the dynamics does, and it removes nothing — it makes structure inaccessible to a chain, which is what AT3 turns into the arrow of time. So no admissible history reaches the empty state from a non-empty one.

**The honest split.**

| Claim | Label |
|---|---|
| There is structure | **Assumed** — this is O1, and it is an existence assertion |
| Structure cannot cease | **Forced** — from O4 plus the absence of an annihilation move |

The framework derives the persistence and not the origin. Any presentation that blurs this is overclaiming.

**How much better the origin gets (reading, not theorem).** O1 does not assert that there are things; it asserts that there are distinctions, which is thinner, since a distinction is a relation rather than a substance. Its denial is correspondingly harder to occupy: a state of total non-distinction cannot distinguish itself from any other state, and to obtain rather than not obtain is already to be one way rather than another. So the alternative to O1 is not a rival state of affairs that happens not to hold, but something that fails to be a determinate alternative. This has the shape of a derivation and is not one — it leans on "distinction" in a way that may equivocate between the logical and the structural sense. It sits beside informational monism as a **preferred reading**.

**The quantitative answer.** There is one non-reading result bearing on how far the framework sits from nothing, and it is already proved. The ground configuration is not empty: by TH7 it has a definite share density across any cut, and matching to the Einstein equation fixes that density at \(1/4G\). Read in this direction, TH7 says the least structured state the theory permits is densely woven, and that gravity is feeble in exact proportion. The nearest thing to nothing here has a measured value.

---

## 1. Stage one — distinction, and the bit

**Derives:** the binary distinction, then Shannon's measure.
**From:** O1's `eq`, plus F2.

`eq` is observational identity, and it is a relation that holds or fails. Its range is therefore two-valued, and that range *is* the bit. Nothing binary is assumed anywhere in the framework: WM2's \(D\) counter is literally this relation's value, one if the residual fails `eq` and zero otherwise.

Shannon's measure then arrives by counting. F2 gives a non-empty admissible set; specifying which residual was selected takes some number of binary distinctions; that count is the entropy. TH1 then says which part of the measure survives as an observable — differences against a reference, never an absolute — and identifies the QFT entanglement-entropy divergence as WM1's granularity gauge.

| Result | Label |
|---|---|
| Distinction is two-valued | **Forced** — `eq` is a relation, and a relation holds or fails |
| The cardinal measure (counting distinctions) | **Assumed** — needs the counting apparatus, WM1/WM2 |
| Only relative measures are observable | **Forced given those** — TH1 |

**Machine:** a comparator. Two things in, one lamp out, lit for same and dark for different. This is the first machine in the course because the bit comes *out* of it rather than going in.
**Figure:** flat.

---

## 2. Stage two — computation

**Derives:** that the world is a rewriting system whose evaluation constructs its own order.
**From:** O1 + O2. This stage is close to definitional rather than analogical, and the framework has been drawing on it without ever claiming it.

O1 says structure reduces under strategies, which is a rewriting system. F1 says the record of successive reductions is a chain, which is a trace. O2 then supplies the sentence the stage turns on:

> Computation does not happen in time. The computation *is* the time.

SM-B3 adds that reduction events form a strict partial order under data dependence, which is the causal structure of a concurrent computation in the event-structure sense.

**Already harvested without being placed here.** FV2 is the undecidability of reachable stuck states, which is the halting problem for the conserving fragment. PA1 and PA2 are progress and preservation, which are the standard type-theoretic pair. Both were derived for other purposes and belong on this rung.

**Not harvested, and load-bearing.** Confluence. Whether O3's selection is deterministic is the Church–Rosser question for this system, and it is not idle: a deterministic argmin is exactly the kind of rule that can pick out a preferred frame, which is the standing risk in stage four. If genuine ties survive under F2′'s partial preorder, isotropy would have to live in the tie set rather than in the selection. **Open, and the most valuable unclaimed result in this stage.**

**Machine:** a punch, a socket and a plug. `abs` removes a part and leaves a socket; `app` is the plug; a redex is a socket with its matching plug in front of it; `reduce` is pushing it home.
**Figure:** flat, and one-dimensional for the chain itself, since an F1 chain is a line and AT2 is the observation that a line has no preferred end.

---

## 3. Stage three — value

**Derives:** a cardinal value structure, and the distinction between an inviolable rule and a priced tendency.
**From:** O3, plus the grounding in `docs/20`.

O3 is a preference relation rather than a metaphor for one. `docs/20` grounds its axioms: M1/M2 are analytic to reading disruption as amount of change, PC follows from O2 with structural individuation, IND from local selection with selection coherence. RM1 then yields a cardinal value function unique up to positive scale.

That is a representation theorem of exactly the kind proved for preference in measurement theory, and RM2's dichotomy is the framework's own form of a classical result: preferences are either representable by a real-valued function or they are lexicographic, with no third shape. CC′ and ST1 then say what the world's value structure looks like — finitely many exact strata above one Archimedean floor — and derive conservation laws as the top stratum by TS4.

**What this has that ordinary decision theory does not.** The preference is not an agent's. It is the dynamics. So the claim is not that valuing agents exist in the world but that the world has a value structure, and that physics's conservation laws are its inviolable clauses while forces are its priced ones.

**State of the documentation.** `docs/06-axiology.md` is a pre-rebuild orphan, marked superseded, still referring to a discarded axiom set. The material that would fill it was built in `docs/19`–`docs/21` and never connected to it. **This is the stage where the framework is furthest ahead of its own documents, and `docs/06` should be rewritten against RM1/RM2/CC′/ST1 rather than removed.**

**The limit, which the orphaned document already stated correctly.** An objective ranking of configurations is not ethics. The step from a ranking to an "ought" needs a bridge principle the framework does not contain, and that remains true.

**Machine:** a two-pan balance for the floor, with a latch above it for the exact strata. The latch is not a heavier weight; it cannot be outweighed at any finite ratio, which is what lexical dominance means.
**Figure:** flat.

---

## 4. Stage four — geometry

**Derives:** nothing yet, and this is the gate.
**From:** SB4 and counting, plus TG2, which is assumed.

What exists: SM-B3 gives a causal order, and by Malament's theorem a causal order fixes the metric up to a conformal factor, with counting fixing the factor. TG2's second clause — that the ground cut count converges to \(\eta_N A\) — is the statement that the share graph has an area law, which is measurable on any generated graph without solving any continuum limit.

**The debt is four debts, not one,** and separating them is most of what this section contributes:

| Sub-problem | Status |
|---|---|
| Dimension | Three independent estimators (volume growth, spectral, Myrheim–Meyer). Agreement is the manifoldlike signature |
| Area law | Measurable now: volume grows as \(r^d\), cut as \(r^{d-1}\). A locality budget rather than a yes/no |
| Manifoldlikeness | Where causal sets are stuck. We have two resources they lack: a dynamics that is not a free choice, and a share graph giving adjacency independent of the order |
| Local Lorentz invariance | Deepest. Causal sets get it from Poisson sprinkling; a deterministic argmin may instead select a frame. See stage two on confluence |

**Machine:** none. This stage has no primitive of its own; it is the previous stages viewed at a scale where a metric is assumed to exist.
**Figure:** three-dimensional, and this is the only stage that earns it. See §8.

---

## 5. Stage five — ontology

**Derives:** nothing. Everything here is a reading.

Informational monism is recorded in the charter as the unique non-idle reading of O1–O4 and is explicitly not used as a premise. The phenomenological link — the experienced world as a high-coherence sequential interface to a larger structure — is a reading in `docs/01`.

What the earlier stages do supply is structural and worth separating from the hard problem. T11 says definiteness is purchased rather than free, F3 says the alternatives not experienced remain real, TH3 says an evaluator's access is a restriction rather than a totality, and AT5 says temporal direction is as dense as decoherence. Together these describe the *shape* of an interface without touching why there is something it is like to occupy one. The hard problem is untouched, and the charter says so.

---

## 6. The spine in one view

```
O1–O4
 │
 ├─ stage 0  origin assumed (O1) · persistence forced (O4) · vacuum density measured (TH7)
 ├─ stage 1  eq ──> distinction ──> bit ──> counting ──> TH1 relative measures     [flat]
 ├─ stage 2  O1+O2 ──> rewriting ──> F1 trace ──> SM-B3 event order                [flat / 1-D chain]
 │             harvested: FV2, PA1, PA2      open: confluence
 ├─ stage 3  O3 ──> docs/20 grounding ──> RM1 cardinal value ──> RM2 dichotomy     [flat]
 │             ──> CC′/ST1 exact strata above a priced floor ──> conservation
 ├─ stage 4  SB4 + counting + TG2 ──> metric, area, Einstein eq                    [3-D]
 │             four sub-debts, separated above
 └─ stage 5  readings only: monism, interface, hard problem untouched
```

---

## 7. The forced-layer audit (opened, not completed)

The forced layer is F1–F5 with the F2′ tightening. Six results carry everything else, which is thin for a foundation and is the reason for this audit.

**The test.** A result forced by O1–O4 must be statable and provable in *every* faithful carrier of O1. If it holds only for finite terms it is using WM1 and belongs one layer down. This turns the audit into a discovery procedure rather than a catalogue, and it needs the carrier question settled enough to say what "faithful" means (§7.1).

### 7.1 Carriers

WM1's finite terms are the charter's default lab bench and explicitly not the substrate. Other carriers that appear to model O1 faithfully:

| Carrier | What it makes native |
|---|---|
| Term graphs / DAGs (WM1) | Executable counters; the current sims |
| Hypergraph rewriting (DPO) | Sharing as shared nodes; the no-dangling-edge condition is the \(B\) counter |
| Adhesive categories | The likely right level of generality: term graphs, hypergraphs, typed graphs and Petri nets are all adhesive, and DPO rewriting is well-behaved exactly there |
| String diagrams / dagger-compact | Share-versus-copy as structure rather than implementation (PA0's content, stated at the right level) |
| Proof nets | \(B\) is the net's boundary; PA1's λI discipline is linearity |
| Von Neumann algebras | TH1, TH4, TH5, TH11 native; TG3 possibly derivable rather than postulated, at the cost of the executable character |

**Conjecture (carrier representation).** O1's carriers are the objects of an adhesive category and O1-reduction is DPO rewriting in it, with WM1 one object of one such category. If this holds it is the analogue of RM1 for the carrier, and it makes the audit's test mechanical.

### 7.2 Candidates for promotion

| Candidate | Currently | Why it may be forced |
|---|---|---|
| **TH12a** disjoint additivity | [WM1, WM2, AD2] | AD2 was already traced to O2 through PC and IND (`docs/20` §3); the residue is the readings SI and SC, not the working model |
| **AT2** order carries no orientation | [SM-B3] | A fact about strict partial orders and their converses; no carrier detail enters |
| **TH2** boundary-only isolation cost | [WM1, WM2] | The *ordinal* form ("isolating a region disturbs only what crosses it") may need O1's sharing alone; the cardinal form needs WM2 |
| **Stage 0** persistence | unlisted | O4 plus the absence of an annihilation move; appears carrier-independent |

Each needs the test actually applied, which is the audit's work and is not done here.

---

## 8. Presentation rule: dimension tracks label

The framework's figures should carry information about the status of what they show, and one rule does it:

> **One dimension for order. Two for structure. Three only where geometry is assumed.**

- **One-dimensional** — an F1 chain. A line, walkable in either direction, which is AT2's content shown rather than stated.
- **Two-dimensional** — terms, sharing, cuts, boundary counts, additivity. These are graph facts and need no geometry. A flat drawing also *strains* at sharing, since a node with two parents cannot be drawn as a tree without crossing lines or duplicating, and that strain is the same one that makes sharing non-trivial.
- **Three-dimensional** — only past the TG2 gate: metric area, horizons, the field equation.

**A correction this rule forces.** `learn/counting-the-world.html` renders the TH2 cut counter as a three-dimensional sphere. TH2 needs no third dimension: it says isolation cost is a function of the cut alone, which is a statement about a graph. Drawing it as a glowing ball implies "area" in the metric sense, which is exactly what TG2 assumes and TH2 does not use. The scene should be flat, with the spherical version reappearing later as the *geometric reading* of the same count, at the point where the label changes. Filed as work against the course.

**Machines.** Each primitive is a device drawn in one consistent visual grammar: comparator (`eq`), junction beside its impostor the copier (`share`), punch and socket and plug (`abs`, `app`, `reduce`), bundler and selector (`pair`, `proj`). The counters are then read off the machines: \(S\) counts junctions broken, \(B\) counts sockets left open, \(D\) is whether the comparator's lamp changed.

**What the machinery is.** Nothing, and the course should say so rather than let the reader suspect small brass devices underneath. The machines are one more carrier in the sense of §7.1, chosen because a reader already has intuitions for it. What is real is what survives changing the drawing, which is exactly the audit's test stated as a picture.

---

## 9. Non-purchases of this document

It derives no new physics. It re-orders existing results by dependency, separates stage four's single recorded debt into four, records stage three's documentation gap, states the presentation rule and the correction it forces, and opens the audit without completing it. Stages zero and five remain as they were: an assumed origin with a forced persistence, and readings.
