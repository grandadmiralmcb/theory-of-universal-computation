# 04 — Classical Limit

Formal derivations name every operation. See also `docs/02-dynamics.md` for the full sequential calculus.

---

## Expression-theoretic mapping

| Classical notion | Structural counterpart | Operation / source |
|------------------|------------------------|--------------------|
| Body / ball | high-share-density expression cluster | `share` density |
| Mass | structural inertia \(m_{\rm struct}\) | `m_struct` |
| Position / velocity | sequential parameters of a local evaluator | sequential state |
| Force / bias | persistent disruption context | `b_struct` / `evaluate_b_at` |
| Potential | position-dependent bias integrated | \(V_{\rm struct}\) |
| Trajectory | high-\(\kappa\) path of lowest-disruption residuals | `preferential_select` + `sequential_tick` |

---

## Derivation 1 — Constant bias → constant acceleration

1. **`velocity_cost`**  
   \(C(\delta v) = \tfrac12 m_{\rm struct}(\delta v)^2 + b_{\rm struct}\,\delta v\)

2. **`preferential_select`**  
   \(\delta v^* = \arg\min C = -b_{\rm struct}/m_{\rm struct}\)

3. **`sequential_tick`**  
   \(v \leftarrow v + \delta v^*\,\tau\), \(x \leftarrow x + v\,\tau\)

4. **`continuum_limit`** (\(\tau\to 0\))  
   \(\ddot{x} = -b_{\rm struct}/m_{\rm struct} = -g_{\rm eff}\)

5. **`integrate_projectile`**  
   recovers ordinary parabolic trajectories and landing times.

**Executable check:** inverse-acceleration ratio for two share densities is exact in the toy simulator.

---

## Derivation 2 — Position-dependent bias → Newton’s second law

1. **`position_dependent_bias`**  
   Let \(b_{\rm struct}(x) = \partial V_{\rm struct}/\partial x\).

2. **`preferential_select`** at each location  
   \(\delta v^*(x) = -b_{\rm struct}(x)/m_{\rm struct}\)

3. **`continuum_limit`**  
   \(m_{\rm struct}\,\ddot{x} = -\partial V_{\rm struct}/\partial x\)

This is the conservative form of Newton’s second law. No new ontological primitive is required.

---

## Derivation 3 — Harmonic oscillator

1. **`harmonic_potential`**  
   \(V_{\rm struct}(x) = \tfrac12 k x^2\) \(\Rightarrow\) \(b(x) = kx\)

2. **`continuum_limit`**  
   \(\ddot{x} + (k/m_{\rm struct})x = 0\)

3. **`structural_energy`**  
   \(E = \tfrac12 m_{\rm struct}v^2 + \tfrac12 k x^2\) is conserved in the continuum; discrete residual drift is integrator artifact only.

**Executable check:** three periods of oscillation with relative energy drift \(\sim 6\times 10^{-3}\) under semi-implicit Euler.

---

## Prediction procedure (local evaluator)

1. Maintain sequential model of relevant high-share clusters (`sequential_state`).
2. Estimate relative structural inertias (`m_struct` from share architecture).
3. Identify bias context — constant or position-dependent (`evaluate_b_at`).
4. Evolve by repeated `preferential_select` + `sequential_tick` (or continuum integration).
5. High-\(\kappa\) regime suppresses deviations; projection remains reliable within ordinary precision.

---

## Current reach

**Closed**
- Single cluster, constant bias → constant acceleration + projectile motion.
- Inverse relation \(a \propto 1/m_{\rm struct}\) under identical bias.
- Position-dependent bias → one-dimensional conservative mechanics (harmonic verified).
- Structural energy accounting under potential bias.

**Still open (same structural principle, no new primitives)**
- Multi-cluster mutual disruption → interaction forces.
- Velocity-dependent residual disruption → drag / dissipation.
- Multi-dimensional sequential parameters → vectors, angular analogues.
- Many weakly coupled excitations → continuum fields.
