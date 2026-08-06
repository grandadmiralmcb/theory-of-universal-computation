# Toy Structural Sequential Simulator

Executable discrete calculus for the Expression-Tree Ontology.

## Named operations implemented

| Operation | Role |
|-----------|------|
| `m_struct` | structural inertia from share density |
| `evaluate_b_at` / `b_struct` | bias strength (constant or \(V'(x)\)) |
| `velocity_cost` | \(C(\delta v) = \frac12 m(\delta v)^2 + b\,\delta v\) |
| `preferential_select` | \(\delta v^* = -b/m\) |
| `sequential_tick` | integrate rate: \(v \leftarrow v + \delta v^*\cdot dt\), advance \(x\) |
| `structural_energy` | \(T + V\) tracking |
| `harmonic_potential` | specialized \(V = \frac12 kx^2\) |

## Continuum targets recovered

| Bias | Equation | Status |
|------|----------|--------|
| Constant \(b\) | \(m\ddot x = -b\) | exact inverse-acceleration ratio |
| Potential \(V(x)\) | \(m\ddot x = -V'(x)\) | harmonic verified, energy ~conserved |

## How to run

```bash
python sim/toy_simulator.py
```

## Formalism reference

Full named-operation derivations: `docs/02-dynamics.md`, `docs/04-classical-limit.md`.
