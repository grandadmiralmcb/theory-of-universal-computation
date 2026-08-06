# The Expression-Tree Ontology

**A Theory of Universal Computation**

> *Status: living document — actively developed. See [CHANGELOG.md](CHANGELOG.md) for revision history and [CONTRIBUTING.md](CONTRIBUTING.md) for how to propose changes.*

---

## Abstract

The **Expression-Tree Ontology** (ETO) is a formal framework built on a single structural commitment: that the state of any discrete computational system can be represented, without loss, as a **finite expression tree** — a finite, ordered, rooted tree whose nodes are labeled by operators drawn from a signature — and that all change in such a system is the application of **rewrite rules** to such trees.

From this commitment the framework develops three layers:

1. **A mathematical core** (foundations, axioms, semantics): expression trees as the free term algebra over a signature, rewriting as the sole dynamical primitive, and the standard metatheory of reduction — confluence, normal forms, and evaluation strategies.
2. **A universality layer**: the demonstration, via standard encodings, that expression rewriting is computationally universal — it simulates the λ-calculus, combinatory logic, and Turing machines, and is simulated by them in turn. This places ETO squarely within the equivalence class identified by the Church–Turing thesis.
3. **An interpretive layer** (the *ontology* proper): a carefully hedged philosophical proposal that expression trees and rewriting are not merely a convenient formalism but a candidate description of what discrete physical processes *are*. This layer is explicitly speculative and is developed alongside its strongest known objections.

The mathematical core and universality layer consist of established results, restated in a uniform vocabulary with citations. The interpretive layer is original synthesis and is labeled as such throughout.

## Reading guide

| Document | Contents | Status |
|---|---|---|
| [docs/00-overview.md](docs/00-overview.md) | Motivation, scope, and a map of the framework | Stable |
| [docs/01-foundations.md](docs/01-foundations.md) | Signatures, expressions, positions, contexts, substitution | Stable |
| [docs/02-axioms.md](docs/02-axioms.md) | The six postulates of the framework | Stable |
| [docs/03-semantics.md](docs/03-semantics.md) | Rewrite relations, strategies, confluence, normal forms | Stable |
| [docs/04-universality.md](docs/04-universality.md) | Encodings of λ-calculus, SK combinators, Turing machines | Stable |
| [docs/05-ontology.md](docs/05-ontology.md) | The interpretive thesis, objections, and replies | Speculative |
| [docs/06-open-problems.md](docs/06-open-problems.md) | Open problems and conjectures | Draft |
| [docs/notation.md](docs/notation.md) | Notation reference | Stable |
| [docs/glossary.md](docs/glossary.md) | Definitions of all technical terms | Stable |
| [docs/bibliography.md](docs/bibliography.md) | Annotated bibliography | Stable |

Readers comfortable with term rewriting can skim documents 01–03 and start at [04-universality.md](docs/04-universality.md). Readers primarily interested in the philosophical thesis should still read [02-axioms.md](docs/02-axioms.md) first, since the interpretive layer leans on the exact wording of the postulates.

## Document status labels

Every document carries one of three labels:

- **Stable** — established mathematics or settled framework vocabulary; changes require strong justification.
- **Draft** — under active development; structure may change.
- **Speculative** — interpretive or conjectural material; presented with objections and explicitly *not* claimed as established.

## How to cite

> *The Expression-Tree Ontology: A Theory of Universal Computation.* Living document, https://github.com/grandadmiralmcb/theory-of-universal-computation. Cite a specific commit hash for stable reference.

## Contributing

Corrections, objections, and counterexamples are the most valuable contributions this project can receive. See [CONTRIBUTING.md](CONTRIBUTING.md).
