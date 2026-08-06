# Glossary

*Status: Stable*

Alphabetical. Each entry gives a one-paragraph working definition and points to the defining document. The [notation reference](notation.md) covers symbols; this page covers terms.

**Atom.** An operator of arity 0; a leaf of an expression tree. ([01 §1](01-foundations.md))

**Church–Rosser property.** The property that convertible expressions (e₁ ↔* e₂) share a common reduct; equivalent to confluence. ([03 §3](03-semantics.md))

**Church–Turing thesis.** The (unprovable, universally held) thesis that Turing computability captures all effective calculation. Imported into the framework as the thesis half of postulate P5. ([02](02-axioms.md), [04](04-universality.md))

**Confluence.** The property of a rewrite system that any two reductions from a common expression can be extended to a common reduct; guarantees uniqueness (not existence) of normal forms. ([03 §3](03-semantics.md))

**Context.** An expression with exactly one hole (□); the formal device for "everything except the subexpression at one position." ([01 §5](01-foundations.md))

**Critical pair.** The local divergence arising from two rule left-sides overlapping at compatible positions; joinability of all critical pairs characterizes local confluence (Critical Pair Lemma). ([03 §3](03-semantics.md))

**Encoding.** An injective, computable, computably invertible, linear-size-overhead map between expression sets over different signatures; the sense in which no signature is privileged (P6). ([01 §6](01-foundations.md))

**Expression.** A finite, ordered, rooted tree with operator-labeled nodes respecting arities; equivalently an element of the free term algebra T(Σ). The framework's structural primitive. ([01 §2](01-foundations.md))

**Expression-Tree Ontology (ETO).** (i) The mathematical framework of documents 01–04; (ii) the interpretive thesis of document 05 that the expression/rewrite description is a candidate for what discrete physical processes are. Context disambiguates; these documents say "the framework" for (i) and "the (interpretive) thesis" for (ii).

**Ground.** Containing no variables. Ground patterns are exactly expressions. ([01 §4](01-foundations.md))

**Honest attribution.** (Proposed, not yet formalized — OP-5.) An attribution of a process specification to a physical system that supports counterfactuals, is fixed in advance, and is projectible; the framework's intended exclusion of Putnam-style trivializing mappings. ([05 §4](05-ontology.md))

**Linear (pattern).** Containing no repeated variable. Left-linearity is one half of orthogonality. ([01 §4](01-foundations.md))

**Locality.** The property, guaranteed by construction, that a rewrite at position p preserves the surrounding context identically (postulate P4); quantitative refinement is OP-2. ([02](02-axioms.md))

**Matching.** The decidable relation "pattern l matches expression e via substitution σ" (lσ = e); the mechanical trigger condition of a rewrite rule. ([01 §4](01-foundations.md))

**Normal form.** An expression containing no redex. In confluent systems, an expression has at most one normal form and may be identified with it as its "value." ([03 §1, §3](03-semantics.md))

**Orthogonal (system).** Left-linear with no overlapping left sides. Orthogonal systems are confluent regardless of termination; SK is the standard example. ([03 §3](03-semantics.md))

**Pattern.** An expression possibly containing variables; the schematic objects rules are made of. ([01 §4](01-foundations.md))

**Position.** A finite sequence of child indices addressing a node of a tree (Dewey notation); the framework's notion of "place." ([01 §3](01-foundations.md))

**Process specification.** A pair (e₀, R) of initial expression and finite rule-set; by Corollary A of the axioms, the framework's complete description of a discrete system. ([02](02-axioms.md))

**Redex.** A subexpression matched by some rule's left side — a site where a rewrite can occur. ([03 §1](03-semantics.md))

**Rewrite rule / rewrite system.** A pattern pair l → r (l not a variable, Var(r) ⊆ Var(l)); a finite set of such rules. The framework's dynamical primitive (postulate P3). ([03 §1](03-semantics.md))

**Signature.** A countable set of operators with fixed arities; the framework's "alphabet of structure." ([01 §1](01-foundations.md))

**Simulation.** Model A simulates model B when B-states encode into A-states, B-steps map to bounded A-step sequences, and results decode computably; the rung-4 equivalence on which universality claims stand. ([04 §1](04-universality.md), [03 §6](03-semantics.md))

**SK combinators.** The two-atom, two-rule universal system (Kxy → x; Sxyz → xz(yz)); the framework's minimal witness of universality. ([04 §3](04-universality.md))

**Strategy.** A policy selecting among available redexes; a sub-relation of → with the same normal forms. Separates the framework's space of possible histories from deterministic trajectories. ([03 §4](03-semantics.md))

**Substitution.** A finitely-supported map from variables to patterns, extended homomorphically; the engine of rule instantiation. ([01 §4](01-foundations.md))

**Termination (strong normalization).** Absence of infinite reductions. Undecidable in general; provable per-system by reduction orders. ([03 §5](03-semantics.md))

**Universality.** The property of simulating some (hence every) Turing-complete model. Held by expression rewriting with polynomial overhead in both directions. ([04](04-universality.md))
