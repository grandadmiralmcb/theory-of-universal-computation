# 28 — The Forced Layer, Audited

*Status: derivation document, two passes. Runs the audit `docs/26` §7 opened. Six results carried the entire framework — F1–F5 with the F2′ tightening — which is thin for a foundation.*

*First pass (§§2–9): **six new forced results, F6–F11**, roughly doubling the layer. **One standing claim rejected** by countermodel — "structure cannot cease", asserted as forced in `docs/26` stage 0. Two candidates examined and not promoted.*

*Second pass (§§10–11): **six more, F12–F17**, most of them marking what O1–O4 **decline** to determine rather than what they give. The framework has no ontological observer (F13), no forced state-valued quantity of any kind (F16), no forced monotone progress (F17), and no instruction at all where residuals are incomparable (F12). One recorded non-consequence: O4 does not entail branching histories, in either direction. **One standing claim corrected** — AT4 was placed in the forced layer by `docs/25` and `docs/11` and belongs below TG instead. Two further unstated assumptions found and added to the charter ledger as B9 and B10, the second opening contention 14. Executable: `sim/forced_layer.py`.*

Authority: `docs/00-theory-charter.md`, including §6's background ledger. Spine: `docs/26`. Existing forced layer: `docs/14` Part I.

---

## 1. The test

A result forced by O1–O4 must be statable and provable in **every faithful carrier** of O1. A result holding only for finite terms is using WM1 and belongs one layer down.

This makes the audit a discovery procedure rather than a catalogue, and it cuts both ways: it promotes results whose proofs never touch a carrier, and it rejects results whose proofs turn out to depend on one. Both happened.

**What every result below still uses.** B2, the classical metalanguage, since these are ordinary proofs. Results quantifying over admissible reductions also inherit **B3** — admissibility is used throughout the framework and defined nowhere — so they are forced *relative to whatever admissibility turns out to be*. That is not a defect of these results specifically; it is the framework's, and it is contention 12.

---

## 2. F6 — No global order

**Claim.** [O2, F1] Where two events lie on no common evaluator chain, nothing determines an order between them.

**Derivation.** F1 makes order a per-chain construction: an order between two events obtains when some chain places one after the other. O2 denies that sequential order is a global parameter of the structure. So for events on no common chain there is no order-determining fact — not an unknown one, none. ∎

**Consequences.**
- **There is no global "now".** Simultaneity across such events is not merely unknown; there is no fact of the matter.
- **There is no privileged global state.** What exists is the structure and the chains, not a sequence of world-states.
- This is the precise content of "background independence is native to O2", which `docs/05` §3.2 asserts without deriving.

### 2.1 What was claimed here first, and why it was withdrawn

The first version of F6 claimed more: that **every linearisation of the dependence order yields the same outcome**, cited as [O2, B8]. That does not follow, and the audit's own test rejects it on two counts.

**Dependence is not ontological.** The relation is defined by **SB4**, a postulate, and in carrier language: \(e \prec_1 e'\) iff the redex of \(e'\) contains a node created by \(e\). Redexes and nodes are WM1 vocabulary. A claim phrased in terms of that relation is not phrased in O1–O4.

**Commutation is a carrier property.** Outcome-invariance requires disjoint reductions to commute. WM1 has that as a lemma, and **SM-B3's own proof sketch says so**, resting on "trace-equivalence of independent steps, per Lemma-3.4-style commutation". Another faithful carrier of O1 need not have it.

| Claim | Status |
|---|---|
| Independent events are not ordered | **Forced** — F6, from O2 and F1 |
| All linearisations yield the same outcome | **Not forced.** Carrier-level; holds in WM1 by a commutation lemma |

The sim's §1 demonstrates the second in a carrier where composition is set union, which commutes trivially. That **confirms** the claim where it holds; it does not establish it in general, and the sim now says so.

**This is the third instance in as many passes**, after MG1's missing sequential-additivity and MG2's asymmetry failure. Each time the move was the same: recognise a structure, then import the setting it lives in without noticing. Charter §6 predicted this would recur and it recurred within one commit of being written. The practical lesson is narrow and worth stating: **before claiming a result forced, check the vocabulary of its statement, not only of its proof.** F6's first version could have been rejected by reading it, since "dependence order" is SB4's phrase and SB4 is a postulate.

---

## 3. F7 — Selection is non-destructive

**Claim.** [O4] Selecting one residual from an admissible set leaves the totality of real structure unchanged.

**Derivation.** Immediate from O4: the unselected remain real. The selected one is real. Nothing is subtracted. ∎

This is weaker than it may look, and §8 is about exactly how much weaker.

---

## 4. F8 — Accessibility is proper

**Claim.** [F1, F2, O4] If at any point along a chain two or more residuals are admissible, then the chain is a **proper** subset of what is real: no evaluator's record contains all real structure.

**Derivation.** F2 gives a selection from the admissible set. F1 makes the chain the record of successive selections, so it contains one residual per step. O4 keeps the unselected ones real. With two or more admissible at some step, the real structure strictly exceeds the chain. ∎

**What this is the root of.** TH3 (horizon reduction) currently carries [F1, F3/O4, SB4, SM-B3, A4]. Its ontological core — that an evaluator's access is a restriction rather than a totality — needs **none of SB4, SM-B3 or A4**. So the "experienced world is an interface, not the substrate" reading rests on something forced, while the machinery it was stated with is not. That relocation is the point of the audit.

---

## 5. F9 — Preference is structurally determined

**Claim.** [O3, analytic] The disruption ordering depends only on the change-set: what sharing, binding and observational identity were altered. Nothing else can enter it.

**Derivation.** O3's own parenthetical defines disruption as change to sharing, binding, or observational identity. A ranking that varied while the change-set was held fixed would not be a ranking of disruption. Analytic to the definition, not an empirical claim. ∎

**What this is the root of.** T17's cost-decoupling — that no admissible dynamics can bias Born statistics toward cheap outcomes — currently carries [T13′, T16′, Q1, WM2]. Weight-blindness, the load-bearing part, is F9 and needs none of them. Contention 7's "the seam is a feature" argument likewise stands on something forced.

**The weak form only.** That *isomorphic* change-sets rank **equally** is stronger. It is PC, and `docs/20` §2 derives it from O2 plus **SI**, which that document calls a reading. F9 claims only that non-structural data cannot enter, not that structurally-alike changes rank alike.

---

## 6. F10 — Selection need not be unique

**Claim.** [F2′] O3 licenses selecting *a* minimal residual and does not single one out. Under a partial preorder minimal elements need not be unique; under a total preorder distinct residuals may still be equivalent. Either way, **determinism of selection is not forced.**

**Derivation.** F2′ replaces minimum with minimality over a well-founded partial preorder, and minimal elements of a partial order are generally several. `docs/20` §4's own countermodel — componentwise order on \(\mathbb{N}^k\) — exhibits the case. ∎

**Why this matters beyond bookkeeping.** Two open problems turn on it. Whether O3's selection is deterministic is the Church–Rosser question of `docs/26` stage 2. And the preferred-frame risk in `docs/25` and `docs/27` §6 was that a deterministic argmin might pick out a frame; F10 says the framework does not require one, so **the tie set is where any isotropy would have to live**. That was speculation when written and is now resting on a forced result.

---

## 7. F11 — Order carries no orientation

**Claim.** [O2] The converse of a strict partial order is a strict partial order. So the order O2 constructs fixes which events neighbour which, and fixes nothing about which end is the past.

**Derivation.** Irreflexivity and transitivity are preserved under converse; F1's chain condition is reversal-invariant. ∎

**Promotion.** This is AT2, stated in `docs/25` inside the AT layer. It is a fact about orders and no working model enters, so it belongs in the forced layer. The AT layer's own account is unaffected: AT3 and AT4 still supply the orientation, and they need the HQ layer or F5 respectively.

---

## 8. Rejected — "structure cannot cease"

`docs/26` stage 0 states the split as an **assumed origin and a forced persistence**, arguing that O3 ranks reductions rather than configurations and that "there is also no move to reach it by: reduction rewrites structure, and the calculus has no global annihilation operator."

**The second clause is a fact about WM1, not about O1–O4**, and the audit's test catches it.

**Countermodel.** Take structures to be finite multisets of atoms, some atoms held in common by two parts. Composition is union; sharing is an atom held by two parts; reduction includes a rule that discards one atom; disruption prefers discarding fewest shared atoms; and the results of unselected reductions remain real. This satisfies O1, O2, O3 and O4. In it the empty structure is reachable in finitely many steps. ∎ (Executable: `sim/forced_layer.py` §7.)

**What survives.** O4 constrains **selection**, saying the residuals not chosen remain real. It says nothing about whether a reduction may destroy what it acts upon. So:

| Claim | Status |
|---|---|
| Selection is non-destructive | **Forced** — F7 |
| Structure cannot cease | **Not forced.** Holds in WM1, whose rule set has no annihilation rule |

`docs/26` stage 0 is corrected accordingly. The "why not nothing" argument keeps its first leg — O3 ranks moves and not configurations, so nothing is never a cheap option — and loses the claim that no move could reach it. That leg was carrying more weight than it could bear.

---

## 9. Examined and not promoted

**TH12a, disjoint additivity.** `docs/20` §3 grounds AD2 in M1/M2, PC and IND, and states plainly that the non-analytic residue is **SI and SC, both readings**. A result resting on two readings is not forced. It remains derived-modulo-readings, which is where `docs/20` already put it; the audit confirms rather than changes this.

**TH2's ordinal form**, that isolating a region disturbs only what crosses its boundary. This is forced *given a definition of isolation as severing exactly the crossing links*, and the definition is doing the work: another carrier could define an isolation move that also disturbs interior structure. Definitional rather than forced. Not promoted.

Recording the failures matters as much as the promotions. A test that only ever promotes is not a test.

---

## 10. Second pass — F12–F17

The first pass looked for results the framework was already using and attributing to postulates. This one asks a different question: what do O1–O4 **decline** to say? Six of the seven results below are of that kind, and they turn out to be the more useful direction. A forced layer that only ever adds claims tells you what the ontology gives you. A forced layer that also marks its silences tells you where every later postulate has to do its work, and that is the map the framework has been missing.

### 10.1 F12 — O3 is silent, not indifferent

**Claim.** [O3, F2′, B3] Where two admissible residuals are **incomparable** under the disruption ordering, O1–O4 determine no selection between them — and this is a different situation from a **tie**, which they do determine something about.

**Derivation.** F2′ permits the ordering to be a partial preorder. Under a partial preorder a pair may stand in three relations: one strictly lower, both equal, or neither related. O3's directive is "prefer those of lower structural disruption". On the first it prefers; on the second it says the two rank alike; on the third its antecedent has no instance, so it issues no instruction. ∎

**Why the distinction carries weight.** A tie is a positive fact *about* the ordering: it says these two rank the same, and treating them symmetrically is reading the ordering correctly. Incomparability is the *absence* of such a fact, and treating an incomparable pair symmetrically is not reading anything — it is supplying what the ordering declined to say.

So a uniform measure over an incomparable set is an addition, not a consequence. **Any derivation of probability by an indifference principle needs CP** — totality, which converts every incomparable pair into a tie — or an explicit measure postulate. This bears directly on contention 4: the Born rule's status as reading-versus-theorem depends on which of the two sets the symmetry argument is being run over, and until now the framework had no vocabulary for the difference.

It also sharpens F10. F10 observed that minimal is not minimum and located any isotropy "in the tie set". F12 adds that the minimal set is not homogeneous: it is a tie set and an incomparable set sitting together, and only the first is available for that argument. *(Executable §8: a residual set whose minimal elements comprise one tied pair and five incomparable ones.)*

### 10.2 F13 — Projection has no agent

**Claim.** [O1, F5, B4] Sharing is symmetric, so the F5 event does not distinguish its two sides. There is no ontological system/observer asymmetry.

**Derivation.** O1's sharing is substructure held **in common**. Whatever B4's identity criterion turns out to be, it is an identity, and under B2 identity is symmetric; so "L and R share s" and "R and L share s" are the same fact. F5 breaks that fact. An event whose entire content is the removal of a symmetric relation has no first argument. ∎

**Consequence.** The system/observer split is a **chain-relative labelling**, not an ontological one. What separates the two sides after a projection is which of them an evaluator's chain reaches — and chains are F1, constructed per evaluator. Two evaluators reaching opposite sides of the same break each describe the other side as "what was measured", and both are correct.

The measurement problem's "who collapses it" therefore has no answer at this layer and does not need one: the question presupposes an asymmetry the ontology does not contain. This is a dissolution rather than a solution, and it is worth being clear that dissolutions are cheaper than solutions and prove less.

**Honest limit.** A carrier may localise the break — a rewrite has a redex and a redex sits somewhere. That asymmetry belongs to the carrier ("redex" is WM1 vocabulary), not to O1–O4. It is also precisely where an observer could be smuggled back in without anyone noticing, which is the reason to have stated F13 at all.

### 10.3 F14 — Projection destroys its own precondition

**Claim.** [F4, F5] The F5 event removes the sharing whose presence is F4's antecedent, so after it the maintain-versus-break comparison has no instance and O3 does not rank the inverse *as an inverse*.

**Derivation.** F4 is conditional: *if* two residuals share substructure, then maintaining and breaking are both dispositions and O3 compares them. F5 selects the break. After it the two no longer share, the antecedent is false, and the comparison F5 acted on is gone. ∎

**What this gives.** An irreversibility at the forced layer, and a precise one: **the loss of a comparison**, not a barrier. The event is not repeatable on that pair, and nothing licenses undoing it in the sense of restoring the ranked alternative, because the ranked alternative no longer exists.

**What this does not give, and the correction it forces.** It does **not** establish that the unselected is permanently off the chain. Nothing in O1–O4 forbids a later reduction from *creating* sharing between the same two parts; creating sharing is a change to sharing, so O3 ranks it against its alternatives like any other move — it is simply not ranked against "maintain". Permanent exclusion is **AT4**, and AT4's proof runs through SM-B3, whose \(\prec\) is SB4's dependence relation stated in redexes and nodes. That is WM1 vocabulary.

| Claim | Status |
|---|---|
| The projection removes its own precondition; O3 does not rank the inverse as an inverse | **Forced** — F14 |
| The unselected is permanently off the chain | **Not forced.** AT4; needs SB4/SM-B3, hence WM1 |

`docs/25` §4 said AT4 moves the arrow "out of the postulational TG layer **and into the forced layer**", and `docs/11`'s AT4 row called \(\Delta S_{\rm gen}\ge 0\) the readout of a "forced-layer ratchet". Both are a layer too far and both are corrected. AT4's substantive claim survives untouched — the arrow sits **below TG**, so it outlives the geometric limit — and that was always the load-bearing half. *(Executable §10.)*

**This is the fourth instance of the pattern**, after MG1, MG2 and F6's own trim. It was found by the rule §2.1 ended with — check the vocabulary of a claim's statement — applied to a claim written before that rule existed. The rule works. What is sobering is that it had to be applied by hand, one claim at a time, and that nothing yet prevents the fifth instance.

### 10.4 F15 — Composition is not free, or B4 carries the difference

**Claim.** [O1, B4] A structure is not determined by the isomorphism types of its parts — *or else* parts are individuated by more than their own content, and B4's identity criterion is where the sharing is encoded. One of the two holds, and the framework has never said which.

**Derivation.** O1 admits composition **and** sharing of substructure. A carrier in which nothing is ever held in common does not admit sharing, so it is not faithful. Given that sharing is realizable, take two parts and compose them twice: once with a substructure held in common, once with distinct isomorphic copies. The two composites differ, and they differ in a respect O3 registers — a move from one to the other changes sharing, and change to sharing is disruption.

Then the fork, which turns on what "the same two parts" means:

- **Parts up to isomorphism.** The two composites have the same parts and are not the same structure. Composition is not free.
- **Parts by identity.** The copies are different objects, so the second composite does not have the same parts, and composition may be free — but then the whole content of sharing has been pushed down into the identity of the constituents. ∎

**Either horn gives the same thing about the world**, and different things about where the fact lives — in the composition, or in the identity criterion. What is unavailable on both is a reading in which structures decompose into self-contained parts. That is what this result is for, and it does not depend on which horn is taken.

**This also shows B4 to be load-bearing rather than merely undefined.** It was recorded in charter §6 as a gap: nothing says what makes two holders hold the same thing. F15 says what turns on filling it — the identity criterion is what decides whether sharing is a fact about composition or a fact about constituents. B4 has a job now, which is more than it had.

*Corrected within this pass.* F15 was first written flat: "a structure is not determined by its decomposition, full stop." The fork was found by the rule §2.1 ends with, applied to a claim written twenty minutes earlier — "the same two parts" is not O-vocabulary until B4 says what sameness is. Worth recording because the previous four instances were all caught retrospectively, and this is the first caught before it was published.

**Consequence.** **Non-separability is ontological.** It is present at O1, before any quantum postulate, and the HQ layer's tensor-like structure is *addressing* something already there rather than importing it. This is worth stating because the reverse reading — that the framework helps itself to entanglement by analogy — is the natural suspicion, and it is wrong at this particular point.

It is also the root of **TH12's additivity defect**. `docs/24` §2.1 finds that entropies add across a cut except where sharing crosses it. F15 says why there is an "except": the cut does not decompose the structure, so there is nothing for additivity to be additive over. The defect is not a correction term bolted onto a clean law; it is the law's domain showing through.

*(Executable §11: the two composites, and the fork read off the cut between them.)*

### 10.5 F16 — The disruption order need not be a gradient

**Claim.** [O3] O3 orders **transitions**, and nothing forces that order to be induced by a function on structures. No state-valued quantity is forced by O1–O4.

**Derivation.** O3 ranks reductions by their disruption, and disruption is defined as *change* to sharing, binding or observational identity. A change is a relation between a before and an after, so the ordering's domain is pairs, not structures. Whether such an ordering comes from a potential is a further question, and the answer is no in general.

**Countermodel.** Three structures in a cycle, where each forward move breaks one share and rebuilds another and each reverse move breaks two, so O3 strictly prefers forward on every edge. A state functional \(V\) reproducing the ranking would need \(V(B)<V(A)\), \(V(C)<V(B)\) and \(V(A)<V(C)\). Summed around the loop the descents are strictly negative and the net change is zero. No such \(V\) exists. ∎ *(Executable §12: the constraint graph is checked for a cycle rather than argued.)*

**What this changes.** Every state-valued quantity in the framework — WM2's counter, RM1's real-valued scale, the TG layer's \(C\) and \(S\), and therefore the entire thermodynamic and gravitational apparatus of `docs/24` — is downstream of a postulate that **manufactures a state functional**. That is what those postulates are for. The repository has never said so plainly, and the omission is a large part of why the quantitative chain reads as less basic than it claims: a reader watching numbers appear out of an ordering is right to want to know where the numbers came from, and the honest answer is that they came from WM2 and RM1, doing exactly the job F16 shows has to be done by something.

This also explains, rather than merely records, why `docs/20`'s AD-chain needed CC′ and the Hölder representation. Manufacturing a scale from an order is what RM1 *is*.

### 10.6 F17 — No forced termination, no forced progress

**Claim.** [O1–O4, F2′] Nothing forces an evaluator chain to terminate, and nothing forces any quantity to decrease monotonically along one.

**Derivation.** F2′'s well-foundedness is a condition on the **per-step** residual set: it guarantees minima exist at each step. A well-founded choice at every step is compatible with a globally periodic trajectory — the countermodel of §10.5 is one, and O3's preferred move is taken at every step of it. And by F16 there need not be any state quantity for a monotonicity claim to be about. ∎ *(Executable §13.)*

**Consequence.** The shape an H-theorem would need — disruption decreasing along a chain — is unavailable at this layer, twice over: there is nothing to decrease, and no reason it would. This **independently confirms the route `docs/25` was forced to take.** AT1′ already showed that deriving order from an entropy gradient is circular; F17 adds that deriving *orientation* from monotone descent is not available either, because descent is not forced. What remains is the structural asymmetry of F5, which is what AT3 and AT4 use. The arrow's route through projection was presented in `docs/25` as the better option. F17 upgrades it to the only one.

FV2's undecidability of reachable V=0-stuckness (`docs/22` §3) sits on the same fact, and the connection is worth naming: a framework whose chains need not terminate cannot expect its progress questions to be decidable.

### 10.7 Recorded non-consequence — O4 does not entail branching histories

O4 says the unselected remains real. It is tempting to read this as "the unselected continues as another history", and that reading adds a chain. Chains come from F1, which supplies one **per evaluator**, and O1–O4 assert the existence of no evaluators at all.

Two models make the point. In the first, one evaluator exists and its chain runs along the selected residual; the unselected residual is real structure and no chain runs along it. In the second, a further evaluator exists whose chain does. Both satisfy O1, O2, O3 and O4. ∎ *(Executable §14.)*

| Claim | Status |
|---|---|
| The unselected residual remains real | **Forced** — F3 |
| The unselected residual is another world | **Not forced** |
| The unselected residual is *not* another world | **Not forced either** |

The framework is committed neither to Everett nor against it, and should stop sounding as if it leans. Turning real structure into a history takes an evaluator, and that is a further posit — which is also why the ledger gap below is not idle bookkeeping. The question cannot be settled, or even sharply asked, until "evaluator" is fixed.

---

## 11. Two more unstated assumptions

The first pass took the B-ledger as given. This one hit two gaps in it, both of the same species as B3: a term the framework uses constantly and defines nowhere. They are added to charter §6 as **B9** and **B10**.

**B9 — what an evaluator is.** O2 says sequential order is "constructed locally by **evaluators**". Nothing anywhere says what makes something an evaluator. Two readings are available and they are not equivalent:

- *Deflationary:* an evaluator **is** a chain. O2 then reads "order is constructed locally by chains of successive reduction", which is nearly tautological and entirely harmless.
- *Inflationary:* an evaluator is a locus that *has* a chain — something with a perspective, an accessible past, a horizon.

The framework's prose slides between them. F8 ("no chain holds all real structure") and TH3 ("an evaluator whose accessible past is proper") are stated inflationally, and F13 says the ontology supplies no such locus. **The deflationary reading is the one F13 recommends and the one the forced results actually need** — every F-result above can be restated with "chain" in place of "evaluator" without loss. Talk of observers as things is then a façon de parler, and the framework should say so rather than leaving the reader to notice.

**B10 — observational identity.** O3's own parenthetical defines disruption as "change to sharing, binding, or **observational identity**". The third term is undefined, and unlike the first two it is not obviously ontological: identity *as seen by an observation* presupposes an observation. By F13 the ontology supplies no observer.

Two ways out, and the framework has never chosen:

1. **Chain-relative.** Observational identity is identity relative to what a chain can reach. Then the change-set is chain-relative, so the disruption ordering is too — and **F9 survives but means less than it reads**: preference is determined by the change-set, and the change-set is not evaluator-independent. Whether O3 then ranks the same way for every chain is an open question and nobody has asked it.
2. **A further primitive.** Observational identity is absolute, in which case it is a third ontological notion sitting inside O3's parenthetical without its own line in the charter.

This is recorded as **contention 14**. It is the sharpest thing the second pass found, because it sits inside the statement of the only dynamical law the framework has — and because option 1 would make an already-forced result (F9) quietly conditional.

---

## 12. The forced layer after both passes

| ID | Claim | From |
|---|---|---|
| F1 | Local sequential chains exist | O2 |
| F2 / F2′ | Minimal-disruption residual exists | O3 + well-foundedness |
| F3 | Unselected remains real | O4 |
| F4 | Co-dependence admits disruption comparison | O1, O3 |
| F5 | Structural projection when break ≤ maintain | F4, O3 |
| **F6** | **No global order: independent events are unordered; no global now, no global state** | **O2, F1** |
| **F7** | **Selection is non-destructive** | **O4** |
| **F8** | **Accessibility is proper; no chain holds all of it** | **F1, F2, O4** |
| **F9** | **Preference is structurally determined** | **O3, analytic** |
| **F10** | **Selection need not be unique** | **F2′** |
| **F11** | **Order carries no orientation** | **O2** |
| **F12** | **O3 is silent, not indifferent, where residuals are incomparable** | **O3, F2′, B3** |
| **F13** | **Projection has no agent; there is no ontological observer** | **O1, F5, B4** |
| **F14** | **Projection destroys its own precondition** | **F4, F5** |
| **F15** | **Composition is not free; non-separability is ontological** | **O1, B4** |
| **F16** | **The disruption order need not be a gradient; no state quantity is forced** | **O3** |
| **F17** | **No forced termination, no forced progress** | **O1–O4, F2′** |

Six entries become eighteen across the two passes.

**What the two passes did differently.** The first added claims and relocated load: F8 under TH3, F9 under T17, F11 out of the AT layer. The second mostly marks **silences** — F12, F14's limit, F16, F17 and the branching non-consequence all say what O1–O4 decline to determine. That turns out to be the more useful direction, because a silence is where a postulate has to stand, and the framework's postulates were not previously matched to the gaps they fill. Three matchings fall out immediately:

| Silence | What stands in it |
|---|---|
| No selection among incomparable residuals (F12) | CP, or a measure postulate — and this is the ground of contention 4 |
| No state-valued quantity (F16) | WM2's counter and RM1's Hölder representation. This is what those postulates are **for** |
| No forced monotone descent (F17) | Nothing does — which is why the arrow had to come from F5's structure (`docs/25`) |

**Corrections this pass made to standing claims.** AT4's layer, in both `docs/25` §4 and `docs/11` (§10.3). That is the fourth instance of recognition-imported-setting, after MG1, MG2 and F6.

**What the audit does not claim.** No new physics, and no discharge of any contention — it opened one (14). Every result above still sits on B2; those touching admissibility sit on B3, and F13 and F15 sit on B4, all of which remain undefined. Two further undefined terms were found inside the framework's own primitives and are now B9 and B10. A larger forced layer is not the same as a better-founded one. Contention 12 is still the deepest thing in the way, and contention 14 is now beside it.
