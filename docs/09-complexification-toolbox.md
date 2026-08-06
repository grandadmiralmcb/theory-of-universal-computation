# 09 — Complexification Thought Toolbox

Alternatives to the active direction (linear `reduce` + weighted `share`). Use when refining the quantum sector or if the active direction stalls.

---

## Active direction (reference)

- `share` carries \(a\in\mathbb{C}\) (or U(1)).
- `reduce` is linear on share-linked residuals: \(\sum a_i E_i\).
- Isolation/maintain costs stay real; structural decoherence projects the linear combination.
- Born reading at selection; optional `phase_accumulate` on sequential history.

Documented in `docs/03-quantum-sector.md` §1.

---

## Toolbox entries

### A. Complex / path-integral cost

Upgrade the dynamical principle: path weight \(\propto e^{iS/\hbar_{\rm struct}}\) with structural action \(S\) on reduction steps. Classical limit = stationary phase / large \(m_{\rm struct}}\).

**Revisit if:** free evolution between decoherence events needs a sum-over-paths semantics more than a linear residual algebra.

### B. Soft / complex `eq`

Observational equivalence becomes graded or complex similarity.

**Revisit if:** approximate observation, noise, or resource-bounded evaluators matter more than interference.

### C. Complex sequential parameter

Sequential state includes phase \((x,\theta)\) without changing `reduce`.

**Revisit if:** a lightweight phase clock is needed on top of an already linear residual algebra (overlaps `phase_accumulate`).

### D. External amplitude attribute

Keep preferential `reduce`; attach \(a_i\) as labels on coherent-set members.

**Revisit if:** implementing linear reduce in the term language is awkward; use as fallback hosting style.

### E. Process / categorical package

Import dagger-compact or process-theory structure so composition already includes the linear package.

**Revisit if:** the expression-tree generative program is abandoned in favor of a process-theoretic reformulation.

### F. Information-principle reconstruction axioms

Add operational constraints (purification, no-broadcasting, …) that select quantum kinematics.

**Revisit if:** the project shifts from generating QM from expressions to showing the ontology can host a unique quantum information theory.

---

## Usage rule

Do not activate a toolbox entry without an explicit adversarial reason that the active direction fails a named requirement. Prefer the smallest upgrade that restores the missing capacity.
