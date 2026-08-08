# Changelog

## [2026-08-08] (adversarial review fixes)

- `sim/linear_reduce.py`: fixed the SyntaxError that had made the file unrunnable since it was committed — every earlier "executable HQ confirmation" citing it predated any successful run. The general-matrix step now rejects norm-changing proposals and warns on modulus-changing ones instead of silently rescaling; the demo exercises a Hadamard to display contention 1.
- Classical chain repaired: per-tick velocity cost **CI4** \(C_\tau(\delta v)=m(\delta v)^2/2\tau+b\,\delta v\) added as an explicit postulate (charter §3); T3 restated as \(\delta v^*=-(b/m)\tau\); the silent increment→rate reinterpretation in docs/02 §3–4 and the sims removed; T3–T8 hypothesis lists corrected.
- **WM4** (environment charged to the maintain ledger only) named as the postulate driving T11.
- N★ scope corrected: the D19+A3 argument confines free epochs to diagonal phase drift; T13 restated (diagonal unitary; general unitarity contended); beam-splitter/recombination cost locus recorded as contention 1 in docs/07.
- Equivalence-principle scope added: gravitational bias must satisfy \(b_{\rm grav}=m_{\rm struct}\,g\); the T6 ratio applies to cluster-independent (applied-force) biases only (docs/02 §6, docs/08 §3).
- T6 executable relabeled a consistency check (prediction and measurement derive from the same \(m\)); independent test requires an external share-count operationalization.
- D13–D17 written out in docs/12 (previously referenced but never defined).
- \(\alpha_m\) (WM3 inertia coefficient) disambiguated from the WM2 counter weight \(\alpha\); dead `gamma` parameter removed from `maintain_cost_from_tree`.
- docs/05 and docs/06 marked pre-rebuild/superseded with void-content banners; AGENTS.md synced with the actual repository (docs 00–14, `sim/` exists and must stay runnable).

## [2026-08-06] (derivation-first ontology rebuild)

### Foundation
- Ontological minima **O1–O4** only as assumptions.
- **F1–F5** derived from O1–O4 (with finiteness regularity for F2).
- Explicit **non-forced** ledger and negative results N1–N3.
- All further structure via numbered postulates (WM, CI, HQ).
- `docs/14-derivation-from-ontology.md` is the derivation spine.
- Charter and theorems rescoped: no claim of amplitudes/unitarity/continuum/Born from ontology alone.

## [2026-08-06] (earlier)

- Charter (trees demoted); theorems WM/CI/HQ tags; D19; T6 end-to-end; linear_reduce; etc.
