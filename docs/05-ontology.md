# 05 — The Ontology

*Status: **Speculative.** This document is a philosophical proposal, stated together with the strongest objections known to the authors. Nothing here is claimed as established.*

## 1. The interpretive thesis

The mathematical layers (documents 01–04) show that "finite expression + finite rule-set" is an adequate vocabulary for all discrete effective process. The interpretive thesis goes further:

> **(ETO-Thesis)** Discrete physical processes are not merely *modelable* as expression rewriting; the expression/rewrite description is a candidate for what such processes *are* — that is, the fundamental facts about a discrete system are structural facts of the kind the expression vocabulary expresses: compositional state, local mechanical transition, finitely specified law.

Three clarifications to keep the thesis honest:

- **"Candidate," not conclusion.** The thesis is proposed as the best available articulation of the digital-physics intuition (Zuse 1969; Fredkin 1990; Wheeler 1990; Wolfram 2002), precisely so that it can be *attacked* at a well-defined joint. The objections in §§4–5 are part of the thesis's statement, not an afterthought.
- **Structural, not material.** The claim is a form of *structural realism* (Ladyman & Ross 2007) restricted to discrete dynamics: what is real is the structure — which subexpression can rewrite to what, adjacent to which context — not any "stuff" the tree is made of. Asking *what the nodes are made of* is, on this view, a category error, the same one physics already declines for the electron.
- **Scope-limited by P1.** The thesis applies to systems whose states are finitely describable. Whether fundamental physics is such a system is an open empirical question (§5), and the thesis is conditional on it.

## 2. What the thesis explains well

The thesis earns its keep where the expression vocabulary makes otherwise-murky notions exact:

- **Part and whole.** Mereology for discrete systems becomes subexpression structure: parthood is the subtree relation, and unique decomposition (P2) settles what "the parts" are. Disputes about arbitrary undetached parts do not arise for trees as they do for regions.
- **Locality and change.** "Only part of the system changed" is exactly context-preservation (P4). The commutation lemma gives an *analysis* of causal independence: events at disjoint positions are order-indifferent, and this is provable, not stipulated.
- **Law.** A law of nature, for a discrete system, is a finite rule-set — syntactically finite, universally applicable, position-independent. The Humean/anti-Humean debate can be restated crisply: is R a summary of the trajectory, or does R *generate* it? ETO is deliberately neutral here, but it makes the question well-posed.
- **Multiple realizability without mystery.** Substrate-independence is Theorem-shaped in the framework ([04-universality.md §6](04-universality.md)): a process specification runs identically under any encoding into any universal host. What functionalists assert about minds, the framework proves about processes; whether the former reduces to the latter is left open.

## 3. Relation to prior pancomputationalisms

| Position | Claim | ETO's divergence |
|---|---|---|
| Zuse 1969; Fredkin 1990 | The universe is a cellular automaton | ETO drops the rigid lattice: trees carry their own geometry, and locality is positional, not spatial. CA are one signature choice among many (P6). |
| Wheeler 1990 ("it from bit") | Physical reality arises from binary answers to yes/no questions | ETO agrees on the primacy of discrete structure but replaces the unstructured bit with the *composed expression* — structure, not information quantity, is primitive. |
| Wolfram 2002 | Simple programs underlie natural complexity | ETO endorses the methodological point; it declines the implicit privileging of particular rule enumerations, per P6. |
| Deutsch 1985 | Physics grounds computation (Church–Turing–Deutsch principle) | ETO accepts the direction of dependence as an open question rather than inverting it; see §5 on quantum mechanics. |

The differences share a root: ETO tries to keep every ontological commitment *invariant under encoding* (P6), on the view that anything that varies with an arbitrary representational choice was never ontology in the first place.

## 4. Objection I: triviality and the representation problem

**The objection (Putnam 1988; Searle 1992).** If implementation is just the existence of a mapping from physical states to computational states, then (Putnam's theorem) every open physical system implements every finite-state automaton — and pancomputationalism is trivially true, hence empty. Relatedly: *which* expression tree is the room you are in? Any partition of the world into tree structure seems as good as any other, so the "structural facts" of §1 look observer-relative.

**Why ETO takes it seriously.** This is, in the authors' view, the strongest objection, and unanswered it is fatal: a thesis true of everything under some mapping says nothing.

**The framework's partial reply**, following the counterfactual/causal-structure tradition (Chalmers 1996; Copeland 1996; Piccinini 2015):

1. *Simulation is not implementation.* ETO's simulation notion ([04-universality.md §1](04-universality.md)) already requires more than state-mapping: steps must map to bounded step sequences, uniformly, with a computable encoding fixed in advance. Putnam-style mappings are constructed post hoc from the trajectory and support no counterfactuals; they fail clause (i) for any state the system did not actually visit.
2. *The rule-set must be projectible.* By P3 the dynamics is a finite R applying at all positions and times. An honest attribution of (e₀, R) to a physical system is a commitment about all counterfactual states matching R's left sides — a strong, falsifiable commitment, not a relabeling.
3. *What remains open.* Even granting 1–2, there may be multiple non-equivalent honest attributions to the same system (encoding-relativity deeper than P6's constant-bounded kind). Whether counterfactual constraints select a unique structure "up to encoding" is **Open Problem 5** in [06-open-problems.md](06-open-problems.md). ETO's position is that the objection converts the thesis from a metaphysical claim into a research program: characterize the equivalence class of honest attributions.

## 5. Objection II: continuity and quantum mechanics

**The objection.** Current fundamental physics is written in continuous mathematics: state spaces are Hilbert spaces, amplitudes are complex-valued, spacetime is (at least apparently) a continuum. P1 (discreteness) therefore excludes physics as we actually have it, and the thesis's antecedent fails.

**The framework's honest accounting:**

- **No refutation is offered.** ETO does not claim physics is discrete; it *conditions* on it (§1). If nature is irreducibly continuous, ETO remains a correct account of effective/discrete process — of computation — and its ontological ambition retreats to those domains.
- **The discreteness question is genuinely open.** Bounded regions carry finite maximal entropy (Bekenstein 1981); the holographic principle ('t Hooft 1993; Susskind 1995) suggests finite information density; and quantum-gravity programs (loop quantum gravity, causal sets — Bombelli et al. 1987) take discreteness seriously. None of this is settled, and ETO must not pretend otherwise.
- **Quantum specifics.** Even granting discreteness of information, quantum dynamics involves superposition and entanglement, which a single-expression state does not naturally carry. Candidate accommodations — expressions denoting quantum states symbolically; rewrite systems on tree representations of tensor networks; many-histories readings where the rewrite nondeterminism of [03-semantics.md §2](03-semantics.md) is reinterpreted — are all *unworked-out* and constitute **Open Problems 6–7**. The Church–Turing–Deutsch tradition (Deutsch 1985) and quantum-computational universality results (Bernstein & Vazirani 1997) constrain but do not decide the question.

## 6. Objection III: the gap between "can be described as" and "is"

**The objection.** Universality makes expression-rewriting descriptions *cheap* ([04-universality.md §6](04-universality.md)): everything effective has one. A description available for everything distinguishes nothing, so the "is" of the thesis adds no content beyond the "can be modeled as" already secured by mathematics.

**Reply.** The thesis's content lies not in *that* a rewriting description exists but in *which* description is attributed and what that attribution forecloses: an honest attribution (§4.2) is a package of counterfactual, locality, and invariance commitments. Two physical theories can agree on trajectories and differ on attributed structure — and the thesis says such differences can be real. This is exactly the standard dialectic of structural realism, inherited deliberately, with its standard difficulties inherited too (Ladyman & Ross 2007; van Fraassen's objections thereto).

## 7. Summary of epistemic status

| Claim | Status |
|---|---|
| Expression rewriting is universal | Theorem (document 04) |
| Universality is polynomial-overhead robust | Theorem (document 04, §5) |
| All effective dynamics is Turing-computable (P5, thesis half) | Working hypothesis, standard |
| Discrete systems are perspicuously described as (e₀, R) | Framework claim, defended in 00–03 |
| Physical processes *are* expression rewriting (ETO-Thesis) | Speculative; conditional on discreteness; open under Objections I–III |

The framework's wager is that the last row is best advanced not by assertion but by sharpening the open problems it generates — see [06-open-problems.md](06-open-problems.md).
