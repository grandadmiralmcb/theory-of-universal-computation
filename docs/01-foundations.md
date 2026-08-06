# 01 — Foundations

*Status: Stable*

This document fixes the basic objects of the framework: signatures, expressions, positions, contexts, and substitution. Everything here is standard universal algebra and term-rewriting vocabulary (Baader & Nipkow 1998, ch. 3; Terese 2003, ch. 2), restated in the framework's uniform notation. See [notation.md](notation.md) for a symbol reference.

## 1. Signatures

**Definition 1.1 (Signature).** A *signature* Σ is a countable set of *operators*, each with a fixed *arity* in ℕ. We write Σₙ for the set of operators of arity *n*. Operators of arity 0 are called *atoms* (or *constants*).

**Convention.** Σ is assumed nonempty and to contain at least one atom; otherwise no finite expression exists.

**Example 1.2.** The signature of combinatory logic: Σ₀ = {S, K}, Σ₂ = {·} (application). The signature of Peano arithmetic terms: Σ₀ = {0}, Σ₁ = {succ}, Σ₂ = {+, ×}.

## 2. Expressions

**Definition 2.1 (Expression).** The set **Expr(Σ)** of *expressions over Σ* is the least set such that: if f ∈ Σₙ and e₁, …, eₙ ∈ Expr(Σ), then f(e₁, …, eₙ) ∈ Expr(Σ). In particular every atom a ∈ Σ₀ is an expression (the case n = 0).

Equivalently, an expression is a finite, ordered, rooted tree whose nodes are labeled by operators of Σ such that a node labeled by f ∈ Σₙ has exactly n children, in order. The two presentations — inductive and tree-theoretic — are used interchangeably; **Expr(Σ)** is exactly the carrier of the free term algebra over Σ (with no generators), also written T(Σ).

**Definition 2.2 (Size and depth).** |e|, the *size* of e, is its number of nodes; depth(e) is the length of its longest root-to-leaf path. Both are defined by the evident structural recursion.

**Proposition 2.3 (Unique decomposition).** Every expression e is *either* an atom *or* equal to f(e₁, …, eₙ) for exactly one f ∈ Σₙ (n ≥ 1) and exactly one tuple (e₁, …, eₙ).

*Proof sketch.* Immediate from the freeness of T(Σ): the term algebra satisfies no equations, so the top-level constructor and its arguments are uniquely determined. ∎

Unique decomposition is the technical content of the compositionality postulate P2 in [02-axioms.md](02-axioms.md); it is what strings lack (a string factors as a concatenation in many ways) and what makes structural induction over expressions unambiguous.

## 3. Positions and subexpressions

**Definition 3.1 (Position).** A *position* is a finite sequence of positive integers. The set Pos(e) of positions *of* e is defined by: ε ∈ Pos(e); and if e = f(e₁, …, eₙ) and p ∈ Pos(eᵢ), then i·p ∈ Pos(e). The *subexpression of e at p*, written e|ₚ, is defined by e|_ε = e and f(e₁, …, eₙ)|_{i·p} = eᵢ|ₚ.

This is Dewey decimal notation: position 2·1 names the first child of the second child of the root.

**Definition 3.2 (Replacement).** e[e′]ₚ denotes the expression obtained from e by replacing the subexpression at position p with e′. It is defined by structural recursion on p.

**Definition 3.3 (Disjoint positions).** Positions p, q are *disjoint* (p ∥ q) if neither is a prefix of the other.

**Lemma 3.4 (Commutation of disjoint replacements).** If p ∥ q then e[e₁]ₚ[e₂]_q = e[e₂]_q[e₁]ₚ.

*Proof sketch.* Induction on the length of the shared prefix of p and q; disjointness means the replacements occur in different immediate subtrees at the point of divergence. ∎

Lemma 3.4 is the seed of every locality and parallelism result in the framework: changes at disjoint positions do not interact.

## 4. Variables, patterns, and substitution

Rewrite rules are stated schematically, which requires extending expressions with variables.

**Definition 4.1 (Patterns).** Fix a countably infinite set X of *variables*, disjoint from Σ. The set **Expr(Σ, X)** of *patterns* is defined like Expr(Σ) but additionally admitting every x ∈ X as a pattern. Var(t) denotes the set of variables occurring in pattern t. A pattern t with Var(t) = ∅ is *ground* — i.e., an expression proper. A pattern is *linear* if no variable occurs in it twice.

**Definition 4.2 (Substitution).** A *substitution* σ is a function X → Expr(Σ, X) that is the identity on all but finitely many variables. Its action extends homomorphically: σ(f(t₁, …, tₙ)) = f(σ(t₁), …, σ(tₙ)). We write tσ for the result.

**Definition 4.3 (Matching).** Pattern l *matches* expression e if there is a substitution σ with lσ = e. When it exists for given l and e, the restriction of σ to Var(l) is unique (again by freeness), so we may speak of *the* matching substitution.

**Remark 4.4 (Decidability and cost).** Whether l matches e is decidable in time O(|l| + |e|) for linear l by a single simultaneous traversal; nonlinear patterns additionally require equality checks between matched subexpressions. Nothing in the framework depends on matching being anything other than a cheap, local, mechanical operation — a point the interpretive layer ([05-ontology.md](05-ontology.md)) leans on.

## 5. Contexts

**Definition 5.1 (Context).** A *context* C is a pattern over Σ ∪ {□} containing exactly one occurrence of the distinguished atom □ ("hole"). C[e] denotes the expression obtained by replacing □ with e.

Contexts package "the rest of the tree" around a position: for every e and p ∈ Pos(e) there is a unique context C with C[e|ₚ] = e. They are the standard device for stating locality: a rewrite at p leaves the surrounding context literally identical.

## 6. Encodings between signatures

The framework must not depend on a privileged signature (postulate P6). The relevant notion:

**Definition 6.1 (Computable encoding).** For signatures Σ, Σ′, an *encoding* is an injective function ⟦·⟧ : Expr(Σ) → Expr(Σ′) such that ⟦·⟧ and the partial inverse ⟦·⟧⁻¹ are computable, and |⟦e⟧| ≤ c·|e| + c for some constant c depending only on the encoding.

**Proposition 6.2 (Binary sufficiency).** For every finite signature Σ there is an encoding of Expr(Σ) into Expr(Σ_pair) where Σ_pair has one atom and one binary operator.

*Proof sketch.* Standard: enumerate Σ, encode each operator as a comb-shaped spine of the binary operator over the atom (unary numeral), and encode f(e₁, …, eₙ) as the right comb ⟨code(f), ⟨⟦e₁⟧, ⟨…, ⟦eₙ⟧⟩⟩⟩. Injectivity follows from unique decomposition (Prop. 2.3); linear size overhead is direct, with the constant depending on |Σ| and its maximum arity. ∎

Proposition 6.2 is why the framework can, without loss of generality, conduct universality arguments over a fixed minimal signature ([04-universality.md](04-universality.md)) while claiming signature-independence.
