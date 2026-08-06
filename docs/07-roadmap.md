# 07 — Roadmap & Open Problems

## Open Questions

These are the central unresolved problems of the Expression-Tree Ontology. They are ordered roughly from more immediate and technical to deeper and foundational.

### Quantitative & Technical
1. What is the correct (or most predictive) concrete form of the cost function? Which expression features should it depend on, and how should the coefficients be fixed?
2. Can a discrete-tick simulation of the current cost function + sequential evaluation quantitatively recover Newtonian projectile motion and simple interference patterns?
3. How precisely does the continuum limit of amplitude-weighted multi-path reduction (`force_A`) produce Schrödinger- or Dirac-like evolution?
4. What is a workable numerical definition of the coherence measure \(\kappa\)?

### Structural & Emergent
5. How (if at all) do local gauge symmetries and the specific gauge group of the Standard Model emerge from labels, linear typing, and cost minimization?
6. Why are there three generations of fermions? Is this forced by the cost + label structure or must it be imposed?
7. What mechanism, if any, suppresses the residual cost of the vacuum expression \(V\) to the observed scale of dark energy?
8. How do multi-particle states, bound states, and continuum quantum fields arise as large-scale limits of expression clusters?

### Foundational
9. Is the amplitude structure \(\mathcal{A}\) (currently \(\mathbb{C}\)) itself derivable from more primitive considerations, or must it be added by hand?
10. Can sequential evaluation order + bounded signal fully generate classical spacetime geometry (including its Lorentzian signature and diffeomorphism invariance), or is additional structure required?
11. What is the precise relationship between the non-temporal fixed points (\(\mathcal{H}\) and \(\mathcal{L}\)) and cosmological or asymptotic boundary conditions?
12. How much of the observed physics can be shown to *emerge* purely from cost minimization and preferential sequentialization versus how much must be introduced via controlled enrichment (Route A style)?

### Meta-theoretic
13. Are the current primitives truly minimal, or can a still smaller generating set produce the same effective physics?
14. What would constitute a decisive empirical test (or falsification) of the framework at the present stage of development?

---

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
