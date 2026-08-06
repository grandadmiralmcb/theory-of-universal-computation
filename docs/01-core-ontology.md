# 01 — Core Ontology

## Primitive Functions (working set)

### Compositional core
- `id` : \(\alpha \to \alpha\)
- `comp` : \((\beta \to \gamma) \to (\alpha \to \beta) \to (\alpha \to \gamma)\)
- `app` : \((\alpha \to \beta) \to \alpha \to \beta\)
- `abs` : binder forming function values
- `pair` / `proj₁`, `proj₂`

### Binding, information flow, observation
- `bind` : \(\texttt{Bind} \to \texttt{Expr} \to \texttt{Expr}\)
- `copy` : \(\alpha \to (\alpha \times \alpha)\)
- `discard` : \(\alpha \to \mathbf{1}\)
- `eq` : observational equivalence

### Dynamics
- `rewrite` (cost-valued) : \(\texttt{Expr} \to \texttt{Expr} \to (\texttt{Expr} \times \mathbb{R}_{\geq 0})\)
- `force` / `force_A` : evaluation (amplitude-valued in Route A)
- `fix` : fixed-point combinator

### Enrichments (Route A)
- Linear composition (`lcomp`, `lapp`)
- Additive labels / charges on expressions
- Distinguished vacuum expression \(V\)
- Bounded sequential signal speed \(c\)

## Core Axioms (summary)

1. **Functional Composition Ontology** — Reality is the total system of syntactically bound composable functions and their evaluation.
2. **Events as Expression Transformations** — An event is the evaluation or rewriting of expression trees; every event remains inspectable as an AST.
3. **Native Nonlinearity of Evaluation** — No global privileged evaluation order; cycles, sharing, lazy/non-strict strategies, and rewriting of prior reductions are permitted.
4. **Preferential Sequentialization** — Regions admitting stable, low-cost sequential evaluation are dynamically favored. Ordinary physical law is the macroscopic expression of this preference.
5. **Costed Rewriting** — Every genuine change carries a non-negative dynamical cost. High-cost rewrites are rare.
6. **Local Consciousness as Sequential Evaluator** — A local consciousness maintains a sequential predictive model of a limited region and monitors it via a coherence measure \(\kappa\).
7. **Emergence of Non-Temporal Fixed Points** — Maximal-coherence and maximal-anti-coherence fixed points arise naturally and correspond to the non-temporal domains traditionally associated with heaven- and hell-like phenomenology.
8. **Constraint Injection & Portals** — Precise, stable mental configurations can inject soft constraints and, when they also relax sequential forcing, function as portals.

## Metaphysical Glossary (condensed)

**Primitive functions** are the elementary *capacities* of reality (the verbs).  
**Input parameters** are the elementary *relata* (the nouns) that those capacities act upon.

Selected readings:
- `rewrite` + cost — genuine change together with its dynamical price.
- `force_A` — actualization of potential into amplitude-weighted outcomes.
- `bind` — imposition of a local interpretive or dynamical context.
- Labels — intrinsic conserved attributes (precursors of charge, spin, etc.).
- Vacuum \(V\) — lowest-cost baseline relative to which excitations are defined.
- Bounded signal — finite speed of ordered sequential information propagation.
