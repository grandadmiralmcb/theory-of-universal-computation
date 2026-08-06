# 04 — Classical Limit

Formal derivations name every operation. See also `docs/02-dynamics.md` and `docs/03-quantum-sector.md`.

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

1. **`velocity_cost`** — \(C(\delta v)=\tfrac12 m(\delta v)^2+b\,\delta v\)
2. **`preferential_select`** — \(\delta v^*=-b/m\)
3. **`sequential_tick`** — integrate rate, advance position
4. **`continuum_limit`** — \(\ddot x=-b/m=-g_{\rm eff}\)
5. **`integrate_projectile`** — parabolic trajectories

**Executable check:** inverse-acceleration ratio exact in toy simulator.

---

## Derivation 2 — Position-dependent bias → Newton’s second law

1. **`position_dependent_bias`** — \(b(x)=\partial V/\partial x\)
2. **`preferential_select`** at each \(x\)
3. **`continuum_limit`** — \(m\ddot x=-V'(x)\)

---

## Derivation 3 — Harmonic oscillator

1. **`harmonic_potential`** — \(V=\tfrac12 kx^2\)
2. **`continuum_limit`** — \(\ddot x+(k/m)x=0\)
3. **`structural_energy`** — \(E=T+V\) approximately conserved (integrator drift only)

**Executable check:** three periods, relative energy drift \(\sim 6\times 10^{-3}\).

---

## Derivation 4 — Classical limit of quantum coherence

1. **`coherent_set`** of share-linked residuals exists while isolation costs remain high.
2. Macroscopic environment raises maintain cost or lowers isolation cost of alternatives.
3. **`structural_decoherence`** drops all but one residual.
4. Surviving dynamics reduce to **`preferential_select`** + **`sequential_tick`** on a single high-\(\kappa\) trajectory (Derivations 1–3).

Quantum and classical regimes are two limits of one preferential sequentialization dynamics, distinguished by whether share isolation remains expensive.

---

## Prediction procedure (local evaluator)

1. Maintain sequential model of relevant clusters.
2. Estimate structural inertias (`m_struct`).
3. Identify bias context (`evaluate_b_at`).
4. Evolve by `preferential_select` + `sequential_tick` (or continuum integration).
5. High-\(\kappa\) regime suppresses deviations.

---

## Current reach

**Closed**
- Constant-bias Newtonian regime + projectile motion.
- Position-dependent bias → 1-D conservative mechanics (harmonic verified).
- Structural energy accounting.
- Structural decoherence criterion linking quantum multi-path regime to classical single-path regime.

**Still open**
- Multi-cluster interaction forces, drag, multi-dimensional sequential parameters, continuum fields.
- Quantitative two-path interference simulation.
