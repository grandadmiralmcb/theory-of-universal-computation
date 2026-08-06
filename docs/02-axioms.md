# 02 — Axioms

*Status: Stable (the postulates' wording); their interpretation is discussed in [05-ontology.md](05-ontology.md)*

The framework's commitments are stated as six postulates. They are deliberately separated so that each can be accepted or denied independently, and each is annotated with its *load* — what breaks if it is dropped. P1–P4 are structural and are simply true *of the formalism* defined in [01-foundations.md](01-foundations.md) and [03-semantics.md](03-semantics.md); their postulate status concerns their application to systems outside the formalism. P5 and P6 are substantive.

---

## P1 — Discreteness

> **The state of any system within the framework's scope is a finite expression over some signature.**

*Load.* P1 fixes the framework's scope to discrete, finitely-describable states. It excludes genuinely infinite or continuum-valued states from direct representation (they may still be represented *approximately* or *symbolically* — e.g., an expression denoting π — but the state itself is finite).

*Deniability.* A reader who holds that physical states are irreducibly continuous denies that the framework's scope includes physics; the mathematics of documents 01–04 is unaffected. This is the central battleground of [05-ontology.md §5](05-ontology.md).

## P2 — Compositionality

> **Every expression is either an atom or an operator applied, in order, to expressions; and this decomposition is unique.**

*Load.* P2 is Proposition 2.3 of [01-foundations.md](01-foundations.md) elevated to a scope claim: systems in scope decompose uniquely into parts. Structural induction, denotational semantics, and the locality postulate P4 all consume it.

*Deniability.* Denying P2 while keeping P1 yields string- or graph-based ontologies (Post systems; graph rewriting). These are computationally equivalent ([04-universality.md §5](04-universality.md)) but forfeit unique decomposition; the framework regards that as a loss of perspicuity, not of power.

## P3 — Dynamics as rewriting

> **Every state transition is the application of a rewrite rule from a fixed, finite rule-set at a single position.**

*Load.* P3 makes rewriting the *sole* dynamical primitive: there is no separate notion of "machine," "processor," or "control" — control state, if a system has one, is itself part of the expression. The finiteness of the rule-set is essential: it is what makes the dynamics finitely specifiable.

*Deniability.* Admitting infinite rule-sets or oracle steps yields hypercomputational variants; the framework explicitly declines these (see [04-universality.md §6](04-universality.md)).

## P4 — Locality

> **A rewrite at position p modifies only the subexpression at p; the surrounding context is preserved identically.**

*Load.* P4 is what makes "part of the system changed, the rest did not" exact rather than metaphorical, via contexts ([01-foundations.md §5](01-foundations.md)). Together with Lemma 3.4 (commutation of disjoint replacements) it grounds the framework's account of parallelism: transitions at disjoint positions are order-independent.

*Deniability.* Global rewrite formalisms (e.g., whole-state transition functions, as in cellular automata presented monolithically) deny P4 at the level of description while typically satisfying it at the level of implementation. The framework treats P4 as a constraint on *admissible descriptions*.

## P5 — Universality

> **The admissible rule-sets include computationally universal ones; the framework identifies "possible dynamics" with "Turing-computable dynamics."**

*Load.* P5 imports the Church–Turing thesis as a framework commitment. Its mathematical half is a theorem ([04-universality.md](04-universality.md): expression rewriting simulates Turing machines and vice versa). Its thesis half — that computability *exhausts* effective dynamics — is, like the Church–Turing thesis itself, not provable and is held as a working hypothesis with the usual overwhelming inductive support.

*Deniability.* Denying P5 in the upward direction (more than Turing) is hypercomputation; in the downward direction (less than Turing — e.g., only terminating rule-sets) yields total fragments that are interesting but strictly weaker. The framework's name — *Theory of Universal Computation* — marks P5 as its center of gravity.

## P6 — Representation invariance

> **No signature is privileged. Every claim of the framework must be invariant under computable encodings between signatures (Definition 6.1 of [01-foundations.md](01-foundations.md)).**

*Load.* P6 is the framework's answer to "why *these* operators?" — the answer being that the choice is immaterial, in the precise sense that any two adequate signatures interconvert with linear size overhead (Prop. 6.2) and that quantities of interest are stable under encoding up to the corresponding constants. This is modeled on the invariance theorem of algorithmic information theory (Kolmogorov 1965; Li & Vitányi 2019), where description length is machine-independent up to an additive constant.

*Deniability.* P6 cannot be coherently denied *within* the framework without nominating a privileged signature, a move for which no non-arbitrary criterion is known. The genuine open question is different — whether invariance-up-to-a-constant is invariance *enough* for ontological purposes — and is discussed in [05-ontology.md §4](05-ontology.md).

---

## Immediate consequences

**Corollary A (Finite specifiability).** By P1 + P3, a system is completely specified by a pair (e₀, R): a finite initial expression and a finite rule-set. The framework's basic object of study is therefore the pair (e₀, R), called a *process specification*.

**Corollary B (Trajectory structure).** By P3, a system's history is a (finite or infinite) sequence e₀ → e₁ → e₂ → ⋯ of expressions, each obtained from its predecessor by one rule application. Nondeterminism enters only through *choice of rule and position*; [03-semantics.md](03-semantics.md) studies exactly this choice.

**Corollary C (Parallelism without a new primitive).** By P4 + Lemma 3.4, simultaneous application of rules at pairwise disjoint positions is well-defined and equal to any sequential ordering of the same applications. Concurrency is thus a derived notion, not an axiom.
