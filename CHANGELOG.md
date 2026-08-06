# Changelog

All notable developments of the Expression-Tree Ontology are recorded here.

## [2026-08-06] (position-dependent bias + named formalisms)

### Position-dependent bias implemented and formalized
- Bias context may depend on sequential position: \(b(x) = \partial V/\partial x\).
- Continuum limit recovers \(m\ddot{x} = -V'(x)\) (Newton’s second law, conservative form).
- Harmonic oscillator specialized, integrated, and verified in the toy simulator.
- Structural energy analogue tracked; relative drift over three periods \(\sim 6\times 10^{-3}\).

### Named operations in all classical derivations
Every step in `docs/02-dynamics.md` and `docs/04-classical-limit.md` is labeled with an operation name:
- `structural_cost`, `m_struct`, `b_struct` / `evaluate_b_at`
- `velocity_cost`, `preferential_select` (`argmin_C`)
- `sequential_tick`, `continuum_limit`
- `integrate_projectile`, `position_dependent_bias`
- `harmonic_potential`, `structural_energy`, `coherence_kappa`

### Simulator
- Integrator corrected: \(\mathrm{dv}^*\) applied as a rate (\(v \leftarrow v + \mathrm{dv}^*\cdot\mathrm{dt}\)).
- Constant-bias inverse-acceleration ratio exact.
- Harmonic energy approximately conserved.

## [2026-08-06] (classical-limit dogfooding)

### Dynamics rewritten in structural terms
- Velocity-form cost, discrete updates, continuum limit, projectile integration with \(m_{\rm struct}\), \(b_{\rm struct}\).

### Executable confirmation
- Toy simulator demonstrates inverse-acceleration ratio under constant bias.

## [2026-08-06] (simulator)

### First executable calculus
- `sim/toy_simulator.py` — discrete sequential evaluator, structural cost proxy.

## [2026-08-06] (dogfooding series)

### Structural cost and continuum limit
- Numerical cost demoted; structural proxy from \(S\), \(B\), \(D\).
- Ontological tightening (monism as unique non-idle reading, etc.).

## [2026-08-06] (earlier)
### Ontological commitment and radical reduction
- Informational monism + holographic projection; reduced primitive set.

## [2026-08-06] (initial)
- Repository structure, first continuum limit, Route A outline, SM comparison, proto-axiology.
