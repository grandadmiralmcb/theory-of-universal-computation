# 06 — Open Problems

*Status: Draft — this list is expected to grow and to be revised as problems are sharpened, solved, or dissolved. Proposals for new problems, and progress on existing ones, are welcome via issues and pull requests.*

Problems are numbered stably for citation (OP-1, OP-2, …); numbers are never reused. Each entry states the problem, its motivation within the framework, and what a solution would look like.

---

## OP-1 — Canonical signatures

**Problem.** P6 makes all adequate signatures interconvertible with linear overhead, but the constants differ. Is there a principled *canonical* choice — e.g., a signature minimizing a natural complexity measure over a natural distribution of processes — or a proof that no non-arbitrary selection criterion exists?

**Motivation.** Sharpens P6 from "no privileged signature is known" to a theorem in either direction. Analogous to the (open) search for natural reference machines in algorithmic information theory (Müller 2010 studied machine-invariance limits).

**Solution shape.** Either a selection theorem with a defensible optimality criterion, or an impossibility/relativity theorem showing every criterion smuggles in an arbitrary choice.

## OP-2 — Quantitative locality

**Problem.** Define and study a *locality measure* for rewrite systems: how far information propagates per step as a function of rule shape (depth of left sides, variable spread). Is there a Lieb–Robinson-style bound for expression rewriting — a provable maximum speed at which a disturbance at one position can influence a distant position?

**Motivation.** P4 gives qualitative locality; physics-flavored applications of the interpretive layer need a quantitative version.

**Solution shape.** A theorem bounding, for any rule-set R with stated shape parameters, the tree-distance influence cone after k steps, with tightness examples.

## OP-3 — Strategy-independence of physical content

**Problem.** [03-semantics.md §4](03-semantics.md) separates the rule space from the strategy. For confluent R, normal forms are strategy-independent, but *trajectories* are not. Which trajectory properties (step counts, intermediate-size bounds, causal orderings of disjoint events) are invariant across normalizing strategies?

**Motivation.** If the interpretive thesis attributes (e₀, R) to a physical system, the physically meaningful quantities should be exactly the strategy-invariant ones — an analogue of gauge invariance.

**Solution shape.** A classification of strategy-invariant observables for orthogonal systems, starting from standardization theorems (Curry & Feys 1958; Lévy 1978 on optimal reduction and redex families).

## OP-4 — Cost realism

**Problem.** The framework's step (one rewrite) is not obviously a fair unit of cost: matching a deep left side or copying a large substituted subtree does unbounded work in one "step." Formulate a cost model for expression rewriting that is (a) invariant under P6-encodings up to polynomial factors and (b) honest about copying, and relate it to established models (van Emde Boas 1990's invariance thesis; Accattoli & Dal Lago 2016 on the λ-calculus's unitary cost model).

**Motivation.** Without cost realism, complexity-theoretic claims made in the expression vocabulary are not securely meaningful.

**Solution shape.** A cost semantics with simulation theorems to/from RAM within polynomial (ideally quasi-linear) overhead.

## OP-5 — The honest-attribution equivalence class

**Problem.** ([05-ontology.md §4](05-ontology.md)) Make precise the notion of an *honest attribution* of a process specification (e₀, R) to a physical system — counterfactual-supporting, projectible, fixed-in-advance — and characterize when two honest attributions to the same system must be equivalent up to computable encoding. Putnam-style triviality should be provably excluded; residual relativity should be provably characterized.

**Motivation.** This is the framework's response-in-progress to the strongest objection against the interpretive thesis. Prior art: Chalmers 1996; Copeland 1996; Piccinini 2015.

**Solution shape.** A definition plus two theorems: (i) trivializing mappings fail the definition; (ii) any two attributions satisfying it are related by an encoding of a stated class — or a counterexample showing irreducible attribution pluralism.

## OP-6 — Quantum states as expressions

**Problem.** Find a signature and rule-set discipline in which quantum states and dynamics are represented *natively* — candidates include tree-structured tensor-network states with rewriting as circuit application — such that the simulation overhead relative to the quantum circuit model is understood, and the representation respects P6.

**Motivation.** Objection II ([05-ontology.md §5](05-ontology.md)) stands until the framework can at least *express* quantum dynamics without loss. Constraint: classical simulation of general quantum circuits is believed exponentially costly (Bernstein & Vazirani 1997), so "native" cannot mean "efficiently classical" — the interesting question is what structure survives.

**Solution shape.** Either a representation theorem with characterized overhead, or a no-go result identifying exactly which postulate (P1? P3's single-position locality?) quantum dynamics violates.

## OP-7 — Nondeterminism as physical branching

**Problem.** [03-semantics.md §2](03-semantics.md) locates all nondeterminism in choice of rule and position. Develop, or refute, a reading in which this branching structure does physical work — e.g., a many-histories interpretation where the reduction graph of (e₀, R) is the object, not any single trajectory — and determine whether interference-like phenomena can be modeled by identifications between branches.

**Motivation.** Speculative end of the quantum question; separated from OP-6 because it revises the framework's semantics rather than encoding into it.

**Solution shape.** At minimum, a mathematically precise "reduction-graph realism" semantics with a worked toy example; ideally, a correspondence or a clean impossibility argument.

## OP-8 — Reference implementation

**Problem.** Build a small, verified reference implementation: a parser for a fixed concrete syntax, a rewrite engine parameterized by strategy, and executable versions of the encodings in [04-universality.md](04-universality.md) (SK, Turing machine simulation), with the metatheoretic checks (critical pairs, orthogonality) mechanized.

**Motivation.** A living document about computation should compute. Mechanization also guards the Stable documents against error.

**Solution shape.** A `src/` tree in this repository with CI running the encodings end-to-end; mechanized statements of Theorems 2.1/3.1 of document 04 would exceed the bar.

---

## Solved problems

*(None yet. Solved entries move here with a pointer to the resolving document or commit.)*
