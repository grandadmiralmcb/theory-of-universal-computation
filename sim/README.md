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
| `cut_shares` / `isolation_cost` | cut share count and the area-law reading of \(C_{\rm isolate}\) (TH2) |
| `rel_entropy` / `rel_entropy_q` | relative information against the ground configuration (TH1, TH4) |
| `kerr_area` / `bh_entropy` / `hawking_T` | horizon thermodynamics; the merger inequality (TH10) |
| `cost_metric` / `ollivier` | the Lawvere metric from the cost structure, and curvature with no manifold (MG1, MG2) |

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
python sim/thermo_gravity.py
python sim/arrow_of_time.py
python sim/metric_from_cost.py
python sim/forced_layer.py
```

Every file must execute cleanly; a sim that does not run must not be cited
as an executable confirmation in the docs.

## Formalism reference

Full named-operation derivations: `docs/02-dynamics.md`, `docs/04-classical-limit.md`.
Thermodynamics and gravity: `docs/24-thermodynamics-gravity.md`.
Time and the arrow: `docs/25-time-and-the-arrow.md`.
Mathematics from the minima: `docs/27-mathematics-from-the-minima.md`.
The forced layer, audited (both passes, F6–F17): `docs/28-forced-layer-audit.md`.
