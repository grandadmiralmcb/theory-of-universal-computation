# Changelog

All notable developments of the Expression-Tree Ontology are recorded here.

## [2026-08-06] (R/N formalization + T6 end-to-end + linear_reduce sim)

### 1. R and N in the term language (`docs/12-RN-formalization.md`)
- **R★:** free-epoch maps typed as share-preserving invertible linear maps on weights (D13–D15); inverse is free-epoch.
- **N★:** relative-modulus change requires structural cost (D16–D18); free epochs freeze \(\boldsymbol{\mu}\).
- **T13★:** unitarity follows from R★ + N★ + T12.

### 2. End-to-end T6 (`sim/end_to_end_T6.py`)
- Expression tree → `m_struct_from_tree` → velocity integrator → measured acceleration ratio.
- No integer knobs; relative error at machine precision for constant bias.

### 3. Linear reduce simulator (`sim/linear_reduce.py`)
- Free-epoch diagonal unitary (`phase_accumulate`) with R/N asserts.
- General free-epoch unitary matrix step.
- Structural projection (non-unitary locus) + Born extract + intensity.

### Theorems doc updated
- `docs/11-theorems.md` includes R★, N★, T13★ and executable links.

## [2026-08-06] (earlier)

- Theorem chain T1–T14; unitarity from projection; linear reduce adoption; toolbox; tree costs; classical formalisms.
