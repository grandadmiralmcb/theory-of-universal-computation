# Toy Structural Sequential Simulator

Executable discrete calculus for the Expression-Tree Ontology.

## Named operations implemented

| Operation | Role |
|-----------|------|
| `m_struct` | structural inertia from share density |
| `evaluate_b_at` / `b_struct` | bias strength (constant or \(V'(x)\)) |
| `velocity_cost` | per-tick \(C_{dt}(\delta v) = m(\delta v)^2/2dt + b\,\delta v\) (postulate CI4) |
| `preferential_select` | \(\delta v^* = -(b/m)\,dt\) (a per-tick increment, not a rate) |
| `sequential_tick` | \(v \leftarrow v + \delta v^*\), advance \(x\) |
| `structural_energy` | \(T + V\) tracking |
| `harmonic_potential` | specialized \(V = \frac12 kx^2\) |

## Continuum targets recovered

| Bias | Equation | Status |
|------|----------|--------|
| Constant \(b\) | \(m\ddot x = -b\) | exact inverse-acceleration ratio (consistency check — docs/08 §3) |
| Potential \(V(x)\) | \(m\ddot x = -V'(x)\) | harmonic verified, energy ~conserved |

## How to run

```bash
python sim/toy_simulator.py
python sim/end_to_end_T6.py
python sim/expr_tree.py
python sim/two_path.py
python sim/linear_reduce.py
python sim/spectrum_toy.py
python sim/splitter_rewrite.py
python sim/stratified_cost.py
python sim/forced_violation.py
python sim/progress_analysis.py
```

Every file must execute cleanly; a sim that does not run must not be cited
as an executable confirmation in the docs.

## Formalism reference

Full named-operation derivations: `docs/02-dynamics.md`, `docs/04-classical-limit.md`.
