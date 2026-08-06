# Toy Structural Sequential Simulator

First executable realization of the discrete sequential calculus for the Expression-Tree Ontology.

## What it implements

- Structural cost proxy \(C = \alpha S + \beta B + \gamma D\)
- Structural inertia \(m_{\rm struct}\) estimated by finite differences on share density
- Preferential low-disruption sequentialization (lowest-C move selected each tick)
- Constant-bias trajectories for idealized clusters
- Direct test of the inverse-acceleration prediction:
  two clusters that differ only in share density should obey
  \(a_1 / a_2 = m_2 / m_1\)

## How to run

```bash
python sim/toy_simulator.py
```

## Status

This is a deliberately minimal toy. Expression structure is collapsed to a single sequential parameter plus an integer share-density. Full `app`/`abs`/`share` term reduction is not yet present. The purpose is to make the structural continuum limit and the first relational prediction *executable* inside the pure theory so they can be inspected, falsified, or refined before any attempt to map laboratory systems onto the calculus.

## Next extensions

1. Replace the integer share-density with an actual `share`-node count over a small expression tree.
2. Enumerate genuine one-step residuals of a real `reduce` relation.
3. Add multi-path coherent sets and the structural isolation-cost decoherence criterion.
4. Calibrate or derive the relative weights \(\alpha,\beta,\gamma\).
