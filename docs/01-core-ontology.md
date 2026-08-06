# 01 — Core Ontology

## Ontological Status (current)

**Forced by the formalism**
- Structured, shareable, reducible informational patterns exist.
- Sequential order is not global; it is constructed locally by repeated reduction under strategies that favor low structural disruption.
- The experienced / measured world of any local evaluator is a high-coherence sequential projection (systematic selection of low-disruption residuals).
- Un-selected residuals remain real parts of the expression forest; they are simply not currently on a high-\(\kappa\) trajectory.

**Preferred reading (unique non-idle interpretation)**
Informational monism: the expression forest *is* what fundamentally exists. Any non-informational substrate either (a) duplicates the same capacities and is therefore informational under another name, (b) introduces a regress of isomorphic dynamical levels, or (c) requires an unexplained contact relation with informational evaluators. The monist reading is the unique reading that avoids idle structure, regress, and unexplained contact. It is not a formal theorem, but the space of coherent alternatives is now severely restricted.

**Holographic character**
Local sequential evaluation already implements projection: at each step alternative residuals are not selected (or, under linear reduce, not yet projected by structural decoherence). The ordinary sensory and instrumental world is a veiled sequential interface to a larger informational structure.

### Matter and Energy
Matter and energy are dual sequential presentations of the same class of informational excitations.
- High internal sharing density → high structural inertia → matter-like behavior.
- Configurations that release or redistribute residual structure at lower net disruption → energy-like behavior.
Both are measured by the same structural disruption counts.

## Reduced Primitive Set

### Syntactic / compositional
- `app` — application
- `abs` — abstraction
- `pair` / `proj` — products
- `eq` — observational equivalence

### Dynamical
- `reduce` — evaluation / reduction
  - **Preferential form:** selects a single low-disruption residual (classical sequentialization).
  - **Linear form (`linear_reduce`):** on share-linked residuals, yields a weighted sum \(\sum a_i E_i\) (quantum-compatible multi-path form). See `docs/03-quantum-sector.md`.
- `share` — explicit sharing
  - May carry a complex weight \(a\in\mathbb{C}\) (or U(1) phase): **`share_weight`**.

### Dynamical principle
Preferential low-disruption sequentialization for structural selection and classical trajectories. Linear reduce supplies multi-path residual algebra while isolation remains expensive; structural decoherence restores preferential single-path dynamics when isolation becomes cheap.

## Structural Cost Proxy

For a reduction step (preferential or as the real cost underlying isolation/maintain):

- \(S\) = shares broken/duplicated
- \(B\) = net open-binding change
- \(D\) = observational inequivalence

\[
C = \alpha S + \beta B + \gamma D \qquad (\alpha,\beta,\gamma > 0)
\]

**Structural inertia:** \(m_{\rm struct} = \langle S(\delta x=1)\rangle\) (computable from expression trees; `sim/expr_tree.py`).

**Continuum limit (constant bias):** \(\ddot{x} = -b_{\rm struct}/m_{\rm struct}\).

## Coherence

\[
\kappa \sim \frac{1}{1 + \langle C\rangle_{\rm recent}}
\]

High \(\kappa\) = successful low-disruption sequential projection (classical regime).

## Core Axioms (current)

1. Structured, evaluable information under the reduced primitives is the operative substrate.
2. Sequential order is a local construction.
3. Dynamics favor minimal structural disruption (\(S,B,D\)) for selection and classical trajectories.
4. On share-linked residuals, reduction may be linear (weighted sum); weights live on `share`.
5. Local evaluators are informational patterns that generate sequential projections.
6. Un-selected / not-yet-projected residuals remain real forest structure.
7. Matter and energy are dual presentations of informational excitations indexed by the same disruption measures.

## Bounded claims
- Consciousness: high-\(\kappa\) sequential evaluation is the formal counterpart of coherent experience; exhaustiveness left open.
- Informational monism: preferred unique non-idle reading, not formal theorem.
- Complex weights and linear reduce: controlled upgrade of existing primitives, not theorems of real cost counts alone; Born rule is a reading at structural selection.
