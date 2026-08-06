# 07 — Roadmap & Open Problems

## Immediate quantitative priorities

1. **Refine and calibrate the cost function**  
   Explore alternative feature sets (depth, binding density, shared-subexpression count, residual complexity, information-theoretic measures). Fix coefficients against one or two empirical scales.

2. **Concrete amplitude arithmetic**  
   Lock \(\mathcal{A} = \mathbb{C}\), write explicit reduction and recombination rules, implement Born extraction, demonstrate a simple two-path interference calculation.

3. **Discrete-tick simulations**  
   Implement a minimal expression language + cost-weighted reduction engine capable of:
   - single-cluster continuum limit under constant bias,
   - few-path interference,
   - basic decoherence when a microscopic expression binds to a larger high-resistance cluster.

4. **Continuum limit for amplitude-weighted excitations**  
   Derive effective Schrödinger- or Dirac-like equations from multi-path `force_A` + cost minimization in the sequential continuum.

## Medium-term structural questions

- Emergence (or controlled imposition) of gauge-like interaction patterns.
- Realistic particle spectrum and three-generation structure.
- Variable bias, multi-body forces, and continuum field limits.
- Quantitative treatment of vacuum residual cost and possible suppression mechanisms for vacuum energy.
- Sharper definition and numerical realization of coherence \(\kappa\).

## Longer-term / foundational

- Full background-independent treatment of sequential geometry and its relation to classical spacetime.
- Derivation or principled selection of the amplitude structure itself.
- Relation between non-temporal fixed points and cosmological or asymptotic regimes.
- Controlled enrichment versus pure emergence: how much structure must be added versus how much can be shown to arise from cost + sequentialization alone.

## Simulation architecture (first target)

A practical early simulator needs only:
- finite term representation of expressions,
- explicit numerical cost,
- amplitude tracking for a small number of paths,
- sequential evaluator objects with binding contexts,
- truncation / approximation scheme.

Once that exists, the classical projectile limit and elementary interference become executable tests of the framework.
