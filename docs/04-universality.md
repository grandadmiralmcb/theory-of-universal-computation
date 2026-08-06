# 04 — Universality

*Status: Stable*

This document establishes the framework's central mathematical claim: expression rewriting is computationally universal — it simulates, and is simulated by, the canonical models of computation. Every result here is classical; the contribution is the uniform packaging under the simulation notion of [03-semantics.md §6](03-semantics.md).

## 1. The simulation notion

**Definition 1.1 (Simulation).** Model A *simulates* model B if there is a computable encoding ⟦·⟧ of B-states as A-states and a constant k such that: (i) each B-step from s to s′ is matched by between 1 and k A-steps from ⟦s⟧ to ⟦s′⟧; (ii) halting/normal-form states correspond under the encoding; (iii) results decode computably.

**Definition 1.2 (Universality).** A model is *universal* if it simulates some (equivalently, by composition of simulations, every) Turing-complete model.

Simulations compose, and each direction below is stated with its overhead. All overheads are polynomial — universality here is robust down to complexity-theoretic granularity, not merely computability-theoretic.

## 2. Expression rewriting simulates Turing machines

**Theorem 2.1.** For every Turing machine M there is a signature Σ_M and finite rewrite system R_M simulating M with constant overhead per step.

*Construction sketch.* Represent a configuration — tape, head position, control state — as the expression

```
conf(revList(leftTape), q, list(headSymbol : rightTape))
```

with tapes as cons-lists of symbol atoms (left tape reversed, so both cells adjacent to the head are at list heads). Each transition δ(q, a) = (q′, b, direction) becomes one rewrite rule; e.g. a right-move:

```
conf(L, q, cons(a, R))  →  conf(cons(b, L), q′, R)
```

Blank-extension at the tape ends adds two rules per state. The rule left sides are left-linear and pairwise non-overlapping, so R_M is orthogonal, hence confluent — and in fact each configuration contains exactly one redex, so the simulation is deterministic. One machine step = one rewrite step. ∎

*Reference.* The construction is folklore; its ancestor is the string-rewriting simulation in Post 1947 and Markov's normal algorithms (Markov 1954), and the term-rewriting form appears in Baader & Nipkow 1998, §4.1 (there used to prove undecidability results, which is the same construction read in the other direction).

**Corollary 2.2.** All undecidability phenomena of Turing machines transfer: reachability (e →* e′?), normalizability, and termination of expression rewriting are undecidable.

## 3. Minimal universal systems: SK combinators

Universality needs remarkably little signature. Over Σ₀ = {S, K}, Σ₂ = {·}:

```
K·x·y    →  x
S·x·y·z  →  x·z·(y·z)
```

**Theorem 3.1 (Combinatory completeness; Schönfinkel 1924, Curry 1930).** Every λ-definable function is representable by an SK expression; hence (with Theorem 4.1's converse) the two-rule SK system is universal.

*Proof route.* The bracket-abstraction translation compiles any λ-term to an applicative SK term, with the fundamental combinators satisfying Kxy = x and Sxyz = xz(yz) exactly as rewrite steps. Details in Barendregt 1984, ch. 7; Hindley & Seldin 2008. ∎

The SK system is the framework's preferred *minimal witness*: two atoms, one binary operator, two rules — a complete basis for computation. By Proposition 6.2 of [01-foundations.md](01-foundations.md), no generality is lost by working over richer signatures, and by P6 nothing is *meant* by the choice.

## 4. The λ-calculus

**Theorem 4.1 (Church 1936; Turing 1937).** The λ-calculus computes exactly the Turing-computable functions.

The λ-calculus is *almost* a first-class citizen of the framework, with one honest caveat: β-reduction, (λx.M)N → M[x := N], involves capture-avoiding substitution, which is not a single ETO rewrite (it acts at unboundedly many positions and requires α-renaming). Two standard repairs, both fully inside the framework:

1. **Compile it away**: bracket abstraction into SK (§3), where substitution never occurs.
2. **Make substitution explicit**: calculi of explicit substitutions (λσ; Abadi, Cardelli, Curien & Lévy 1991) or de Bruijn-indexed presentations turn β into a finite set of genuine local rewrite rules, at the cost of a larger signature.

The framework's reading: λ's substitution is a *macro-step*, and ETO is the assembly language in which such macro-steps expand. This is not a weakness of λ but a confirmation of the framework's altitude — it sits at the level where every step is finite, local, and mechanical.

## 5. Simulations *of* expression rewriting

**Theorem 5.1.** Every finite rewrite system R is simulated by a Turing machine with polynomial overhead.

*Sketch.* Serialize expressions (unambiguously, by Prop. 2.3 of [01-foundations.md](01-foundations.md)); a TM scans for a redex under a fixed strategy, checks matching (linear time for linear rules; with subterm-equality checks otherwise), and splices the instantiated right side. Each rewrite step costs time polynomial in the current expression size. ∎

Together, §2 and §5 place expression rewriting in the Church–Turing equivalence class *with polynomial interconvertibility* — the class where the invariance thesis of complexity theory (van Emde Boas 1990) locates all reasonable sequential models.

**Remark 5.2 (Neighboring formalisms).** String rewriting (Post 1943; semi-Thue systems), graph rewriting (Ehrig et al. 2006), cellular automata (universal instances: Cook 2004 for rule 110), tag systems, and interaction nets (Lafont 1990) all interconvert with expression rewriting by standard encodings. The framework's preference for trees is argued on grounds of perspicuity in [00-overview.md §2](00-overview.md), never of power.

## 6. What universality does and does not license

**It licenses:**
- Treating (e₀, R) as a fully general model of discrete effective process (postulate P5's mathematical half).
- Transferring every computability and complexity result into the expression vocabulary.
- The *substrate-independence* observation: any universal system can host the dynamics of any other, so no universal formalism can be distinguished from another by its computational behavior alone.

**It does not license:**
- **Hypercomputation.** Nothing here exceeds Turing computability, and the framework declines infinite rule-sets and oracles by P3/P5.
- **The ontological reading.** That physical processes *are* expression rewriting does not follow from the fact that they can be *modeled* by it — universality makes the modeling claim cheap, and therefore makes the ontological claim require *more* than universality, not less. This gap is the entire subject of [05-ontology.md](05-ontology.md), and conflating the two claims is, in the framework's view, the characteristic error of naive pancomputationalism.
