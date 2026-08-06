# 03 — Semantics

*Status: Stable*

This document defines the dynamical layer: rewrite rules, the rewrite relation, strategies, and the classical metatheory (confluence, normal forms, termination). All results here are standard (Baader & Nipkow 1998; Terese 2003); proofs are sketched or cited.

## 1. Rewrite rules and systems

**Definition 1.1 (Rewrite rule).** A *rewrite rule* over signature Σ is a pair of patterns, written l → r, such that l is not a bare variable and Var(r) ⊆ Var(l).

The two side-conditions are standard and load-bearing: a bare-variable left side would match everything everywhere; a fresh variable on the right would make a single step nondeterministic in its *output*, not merely in its site of application.

**Definition 1.2 (Rewrite system).** A *rewrite system* R is a finite set of rewrite rules over a common signature (finiteness per postulate P3).

**Definition 1.3 (One-step rewriting).** e →_R e′ iff there exist a rule (l → r) ∈ R, a position p ∈ Pos(e), and a substitution σ such that e|ₚ = lσ and e′ = e[rσ]ₚ. The subexpression e|ₚ is the *redex*; the surrounding context is preserved (postulate P4).

**Definition 1.4 (Derived relations).** →*_R is the reflexive-transitive closure (reduction); ↔*_R the equivalence closure (convertibility). An expression with no redex is a *normal form*. If e →*_R n with n a normal form, n is *a normal form of e*.

**Example 1.5 (SK reduction).** Over Σ₀ = {S, K}, Σ₂ = {·} (written infix, left-associative):

```
K·x·y     →  x
S·x·y·z   →  x·z·(y·z)
```

This two-rule system is computationally universal ([04-universality.md §3](04-universality.md)).

## 2. The shape of nondeterminism

A single expression may contain many redexes. The rewrite relation is therefore a *relation*, not a function, and the framework locates all nondeterminism in exactly two choices per step: which rule, and at which position (Corollary B of [02-axioms.md](02-axioms.md)). Two classical questions arise:

1. **Confluence** — does the choice ultimately matter?
2. **Termination** — does reduction always end?

Both are undecidable in general (reductions from the halting problem; Baader & Nipkow 1998, §4.1, §5.1), which the framework regards not as a defect but as the expected signature of universality (postulate P5).

## 3. Confluence

**Definition 3.1.** R is *confluent* if whenever e →* e₁ and e →* e₂, there exists e₃ with e₁ →* e₃ and e₂ →* e₃. R has the *Church–Rosser property* if e₁ ↔* e₂ implies a common reduct; the two properties are equivalent (Church & Rosser 1936 for λ; general form in Terese 2003, ch. 1).

**Theorem 3.2 (Uniqueness of normal forms).** In a confluent system, every expression has at most one normal form.

*Proof.* Two normal forms of e reduce to a common reduct; being normal, each reduces only to itself. ∎

**Theorem 3.3 (Newman's Lemma; Newman 1942).** A terminating system is confluent iff it is *locally* confluent (single-step divergences rejoin).

**Theorem 3.4 (Critical Pair Lemma; Knuth & Bendix 1970; Huet 1980).** A rewrite system is locally confluent iff all its critical pairs — the divergences arising from overlapping left-hand sides — are joinable. For terminating systems this yields, with Newman's Lemma, a *decision procedure* for confluence.

The critical-pair machinery matters to the framework because it makes a global property (confluence) checkable from finite, local data (rule overlaps) — a recurring pattern: the postulates P3/P4 keep the dynamics finitely and locally specified, and the metatheory rewards this with finite criteria.

**Remark 3.5 (Orthogonality).** A system whose rules are left-linear and non-overlapping (*orthogonal*) is confluent regardless of termination (Rosen 1973; Terese 2003, ch. 4). The SK system of Example 1.5 is orthogonal, hence confluent — this is the modern route to the Church–Rosser theorem for combinatory logic.

## 4. Strategies

**Definition 4.1 (Strategy).** A *strategy* for R is a sub-relation of →_R with the same normal forms — a policy for choosing among available redexes.

Canonical strategies, with their classical properties:

| Strategy | Choice | Key property |
|---|---|---|
| Leftmost-outermost ("normal order") | Outermost redex, leftmost first | *Normalizing* for orthogonal systems: reaches a normal form whenever one exists (O'Donnell 1977; standardization: Curry & Feys 1958) |
| Innermost ("applicative order") | A redex with no redex below it | Corresponds to call-by-value; may diverge where normal order halts |
| Parallel-outermost | All outermost redexes simultaneously | Normalizing for orthogonal systems; the well-definedness of the simultaneous step is Corollary C of [02-axioms.md](02-axioms.md) |

**Theorem 4.2 (Normalization, stated for orthogonal systems).** If e has a normal form n, then leftmost-outermost reduction from e reaches n.

*Significance for the framework.* Strategy theory is where ETO's determinism story lives: a *process specification* (e₀, R) plus a *strategy* is a deterministic system; without a strategy it is a space of possible histories. The framework deliberately keeps the two separate — postulates P1–P6 constrain the space; strategies select trajectories.

## 5. Termination

**Definition 5.1.** R is *terminating* (strongly normalizing) if no infinite reduction sequence exists.

**Theorem 5.2 (Undecidability; folklore via Turing 1936).** Termination of finite rewrite systems is undecidable; indeed it is Π⁰₂-complete in general.

**Remark 5.3 (Proof methods).** Reduction orders (Knuth–Bendix order, recursive path orders; Dershowitz 1982) prove termination for many concrete systems. Their existence for a given R is the standard technique, not a general decision procedure, consistent with Theorem 5.2.

**Remark 5.4 (Total fragments).** Rule-sets provably terminating in a fixed theory compute exactly that theory's provably total functions — strictly less than Turing-complete. This is the "downward denial" of P5 noted in [02-axioms.md](02-axioms.md): totality is bought with universality.

## 6. Equivalence of processes

When are two process specifications "the same process"? The framework adopts the standard ladder, from finest to coarsest:

1. **Syntactic identity** of (e₀, R) — too fine (renaming an operator changes nothing real; cf. P6).
2. **Bisimilarity** of their transition systems — respects branching structure; the right notion when the *choice structure* matters (Park 1981; Milner 1989).
3. **Convertibility / equal normal forms** — the right notion for confluent, terminating systems, where each expression denotes its unique normal form.
4. **Encoding-mediated simulation** — e ↦ ⟦e⟧ with steps mapped to bounded step sequences; the notion under which universality claims are made ([04-universality.md §1](04-universality.md)).

The framework fixes no single notion but requires every equivalence claim to name its rung. Most cross-formalism claims in these documents live on rung 4; most within-system claims on rung 3.
