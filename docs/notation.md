# Notation

*Status: Stable*

Symbol reference for all documents. Definitions live in the documents cited; this page is a lookup table only.

## Signatures and expressions

| Notation | Meaning | Defined in |
|---|---|---|
| Σ | A signature (countable operator set with arities) | [01 §1](01-foundations.md) |
| Σₙ | Operators of Σ with arity n | [01 §1](01-foundations.md) |
| Expr(Σ) | Expressions (ground terms) over Σ; carrier of T(Σ) | [01 §2](01-foundations.md) |
| Expr(Σ, X) | Patterns: expressions possibly containing variables from X | [01 §4](01-foundations.md) |
| f(e₁, …, eₙ) | The expression with root operator f and children e₁ … eₙ | [01 §2](01-foundations.md) |
| \|e\| | Size of e (number of nodes) | [01 §2](01-foundations.md) |
| depth(e) | Depth of e (longest root-to-leaf path) | [01 §2](01-foundations.md) |

## Positions and contexts

| Notation | Meaning | Defined in |
|---|---|---|
| ε | The root position (empty sequence) | [01 §3](01-foundations.md) |
| i·p | Position: step to child i, then follow p | [01 §3](01-foundations.md) |
| Pos(e) | The set of positions of e | [01 §3](01-foundations.md) |
| e\|ₚ | Subexpression of e at position p | [01 §3](01-foundations.md) |
| e[e′]ₚ | e with the subexpression at p replaced by e′ | [01 §3](01-foundations.md) |
| p ∥ q | p and q are disjoint (neither prefixes the other) | [01 §3](01-foundations.md) |
| C, □, C[e] | Context, hole, and hole-filling | [01 §5](01-foundations.md) |

## Variables and substitution

| Notation | Meaning | Defined in |
|---|---|---|
| X | A fixed countably infinite set of variables | [01 §4](01-foundations.md) |
| Var(t) | Variables occurring in pattern t | [01 §4](01-foundations.md) |
| σ, tσ | A substitution; its application to t | [01 §4](01-foundations.md) |

## Rewriting

| Notation | Meaning | Defined in |
|---|---|---|
| l → r | A rewrite rule (left side l, right side r) | [03 §1](03-semantics.md) |
| R | A rewrite system (finite set of rules) | [03 §1](03-semantics.md) |
| e →_R e′ | One-step rewriting (subscript dropped when clear) | [03 §1](03-semantics.md) |
| →* | Reflexive-transitive closure of → (reduction) | [03 §1](03-semantics.md) |
| ↔* | Equivalence closure of → (convertibility) | [03 §1](03-semantics.md) |
| (e₀, R) | A process specification: initial expression + rule-set | [02, Cor. A](02-axioms.md) |

## Encodings and simulation

| Notation | Meaning | Defined in |
|---|---|---|
| ⟦·⟧ | A computable encoding between expression sets | [01 §6](01-foundations.md) |
| "A simulates B" | Encoding + bounded step correspondence + computable decoding | [04 §1](04-universality.md) |

## Postulates

P1 Discreteness · P2 Compositionality · P3 Dynamics-as-rewriting · P4 Locality · P5 Universality · P6 Representation invariance — all in [02-axioms.md](02-axioms.md). Open problems are cited as OP-n per [06-open-problems.md](06-open-problems.md).

## Typographical conventions

- Concrete rules and expressions are set in code blocks; the application operator `·` is written infix and associates left (`S·x·y·z` = `((S·x)·y)·z`).
- Named results are cited as "document §section" or by their number within a document, e.g. "Prop. 2.3 of [01-foundations.md](01-foundations.md)".
- Unicode math (→, Σ, λ, ⟦⟧) is used directly in prose; documents avoid LaTeX so they render on GitHub without extensions.
