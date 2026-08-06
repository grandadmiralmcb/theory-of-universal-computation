# Toy Structural Sequential Simulator

Executable discrete calculus for the Expression-Tree Ontology (reduced primitives).

## What it implements

- Structural inertia \(m_{\rm struct}\) from share density
- Cost of velocity change: \(C(\delta v) = \frac12 m(\delta v)^2 + b(x)\,\delta v\)
- Preferential low-disruption sequentialization each tick
- **Constant bias** — recovers inverse-acceleration ratio
- **Position-dependent bias** (structural potential) — harmonic oscillator demo with energy tracking

## Continuum targets

| Bias | Continuum equation | Status |
|------|--------------------|--------|
| Constant \(b\) | \(m\ddot x = -b\) | Confirmed in simulator |
| Potential \(V(x)\) | \(m\ddot x = -V'(x)\) | Implemented (harmonic) |

## How to run

```bash
python sim/toy_simulator.py
```

## Next extensions

1. Replace integer share-density with an actual count of `share` nodes over a small expression tree.
2. Double-well / barrier potentials.
3. Two interacting clusters (mutual structural disruption).
4. Multi-path coherent sets + structural isolation-cost decoherence.
