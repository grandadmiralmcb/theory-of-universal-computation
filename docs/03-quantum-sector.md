# 03 — Quantum Sector

Structural multi-path coherence, isolation-cost decoherence, **linear reduce on share-weighted residuals** (active direction), velocity coupling, and a toolbox of alternative complexifications.

Every derivation names the operation performed.

---

## 0. Shared substrate

Reduced primitives and structural cost remain in force:

\[
C = \alpha S + \beta B + \gamma D \qquad (\text{real, non-negative})
\]

Preferential low-disruption sequentialization remains the dynamical principle for *structural selection*. Classical sequential calculus: `docs/02-dynamics.md`.

---

## 1. Active direction — linear `reduce` + weighted `share`

This is the adopted upgrade. It is the smallest change to the existing axiom surface that makes QM-compatible expressions native to the share architecture rather than external labels.

### 1.1 Weighted share

**Operation: `share_weight`**

A `share` node may carry a complex weight \(a \in \mathbb{C}\) (or a pure U(1) phase). The weight is an attribute of the share link, not a new ontological kind of substance.

- Co-dependence remains identity of content via `share`.
- The weight rides on that co-dependence and is available at recombination.

### 1.2 Linear reduce

**Operation: `linear_reduce`**

Where share-linked residuals exist, reduction yields a **weighted sum** rather than a single preferred residual:

\[
\texttt{linear\_reduce}(E) = \sum_i a_i\, E_i, \qquad a_i \in \mathbb{C}.
\]

- Superposition is the *form* of the residual under linear reduction, not merely a set of residuals not yet isolated.
- Ordinary preferential `reduce` (single residual) remains available and is recovered when the coherent set has size 1, or when structural decoherence has already projected.

### 1.3 Structural multi-path (unchanged counts)

**Operation: `coherent_set`**

\[
\mathcal{C} = \bigl\{ E_i \;\big|\; C_{\rm isolate}(E_i;\mathcal{C}) > C_{\rm maintain}(\mathcal{C}) \bigr\}.
\]

**Operation: `isolation_cost`** / **`maintain_cost`** — still real structural counts from Share architecture (see `sim/expr_tree.py`).

**Operation: `structural_decoherence`**

\[
\textbf{if } C_{\rm isolate}(E_i) \le C_{\rm maintain}
\quad\textbf{then}\quad
\text{drop } E_i \text{ from the linear combination}.
\]

Isolation/maintain costs stay real. Linear combination is the free-evolution / multi-path form; structural preference still decides when the combination collapses to a singleton (or classical mixture).

### 1.4 Interference and intensity

**Operation: `path_recombine`** — addition of weighted residuals under `linear_reduce`:

\[
a_{\rm tot} = \sum_i a_i.
\]

**Operation: `intensity`**

\[
I \propto \lvert a_{\rm tot}\rvert^2
  = \sum_i \lvert a_i\rvert^2 + 2\sum_{i<j}\mathrm{Re}(a_i^* a_j).
\]

**Operation: `visibility_amplitude`**

\[
\mathcal{V} = \frac{2\lvert a_1\rvert\lvert a_2\rvert}{\lvert a_1\rvert^2+\lvert a_2\rvert^2}
\]

when both paths remain in \(\mathcal{C}\); else 0.

### 1.5 Phase accumulation

**Operation: `phase_accumulate`**

Weights on share-preserving trajectories may evolve:

\[
a_i(t+\tau) = a_i(t)\,\exp\bigl(-i\,\varphi_i\,\tau\bigr),
\qquad
\varphi_i = \varphi_i(x_i, v_i; \text{binding context}).
\]

\(\varphi_i\) is tied to sequential / binding history (controlled enrichment of the weight dynamics, not a new primitive).

### 1.6 Born extraction at structural selection

**Operation: `born_extract`**

When `structural_decoherence` (or an equivalent detection binding) forces a choice:

\[
P(i) = \frac{\lvert a_i\rvert^2}{\sum_j \lvert a_j\rvert^2}.
\]

This remains a *reading* of the weights at the moment of structural selection, not a theorem of real cost axioms alone.

### 1.7 Classical limit of coherence

**Operation: `classical_limit_of_coherence`**

Environmental share density raises `maintain_cost` → `structural_decoherence` → singleton → ordinary real `preferential_select` + `sequential_tick`. Quantum multi-path and classical single-path motion remain two regimes of one preference dynamics, distinguished by whether isolation of alternatives remains expensive.

### 1.8 Status of the active direction

| Recovered structurally (real counts) | Native after linear reduce + weighted share |
|--------------------------------------|---------------------------------------------|
| coherent sets, isolation/maintain | linear combination of residuals |
| structural decoherence | interference cross term |
| classical sequential calculus | continuous visibility |
| inverse share-count acceleration ratio | Born reading at selection |

Unitarity of free weight evolution and a derivation of Born from cost alone remain open.

---

## 2. Velocity coupling (unchanged in structure)

**Operation: `attach_sequential_state`** — COM or path-wise \((x,v)\).

**COM mode:** collective \(m_{\mathcal{C}}\), ordinary preferential sequentialization; weights are passengers unless `phase_accumulate` is active.

**Path-wise mode:** each arm has \((x_i,v_i)\); differential bias permitted (which-path sequential distinction).

**Operation: `path_recombine_with_velocity`** + **`com_from_amplitudes`** — reconcile sequential state on recombination via amplitude-weighted means, or inherit the selected path’s state on Born extraction.

Named interferometer pipeline under bias remains as before, with `linear_reduce` replacing ad-hoc external amplitude attachment.

---

## 3. Thought toolbox — alternative complexifications

Directions considered but not adopted as the primary upgrade. Kept as a refinement toolbox.

### Toolbox A — Complex / path-integral cost

**Idea:** Replace real structural cost \(C\) by a complex action \(S\), with path weight \(\propto e^{iS/\hbar_{\rm struct}}\). Preferential sequentialization becomes a discrete sum-over-paths (stationary phase recovers classical trajectories).

| Pros | Cons |
|------|------|
| Closest to standard path-integral intuition | Changes the *type* of the dynamical principle (argmin → sum of complex weights) |
| Classical limit via stationary phase matches high-\(\kappa\) regime | Requires a structural \(\hbar\) and a well-defined action on expression steps |
| Interference from path cancellation | Less continuous with existing real isolation/maintain counts |

**When to revisit:** if linear reduce + weighted share proves insufficient for continuous evolution between decoherence events, or if a natural structural action on reduction steps appears.

---

### Toolbox B — Complexify only `eq`

**Idea:** Observational equivalence becomes a continuous or complex similarity score rather than binary `eq`.

| Pros | Cons |
|------|------|
| Soft matching, graded distinguishability | Does not by itself give additive cancellation of path weights |
| Minimal change to one primitive | No native superposition algebra |

**When to revisit:** for approximate observation, noisy evaluators, or resource-bounded `eq` — not as a primary route to interference.

---

### Toolbox C — Complex sequential parameter only

**Idea:** Sequential state includes a phase coordinate \((x,\theta)\) without changing `reduce`.

| Pros | Cons |
|------|------|
| Phase clock tied to sequential motion | Without linear combination of residuals, no fringes |
| Simple to implement | Phase remains decorative |

**When to revisit:** as a lightweight add-on once linear reduce is in place (overlaps `phase_accumulate`).

---

### Toolbox D — External amplitude attribute (previous minimal enrichment)

**Idea:** Keep `reduce` preferential (single residual / coherent set of residuals) and attach \(a_i\in\mathbb{C}\) as an external label on each residual in \(\mathcal{C}\).

| Pros | Cons |
|------|------|
| Minimal formal surface; already partially implemented | Amplitudes are bolted on, not native to share/reduce |
| Clear boundary with pure structure | Weaker continuity with the compositional substrate |

**When to revisit:** if linear reduce proves technically awkward in the term language; as a fallback implementation style.

---

### Toolbox E — Full process / categorical package

**Idea:** Import dagger-compact or process-theory structure (as in categorical quantum mechanics) so that systems and processes already carry the linear package.

| Pros | Cons |
|------|------|
| Mature compositionality; interference native | Large departure from the reduced expression-tree core |
| Aligns with existing QI reconstructions | Risks replacing the theory rather than refining it |

**When to revisit:** only if the expression-tree program stalls and a full process-theoretic reformulation becomes the clearer route.

---

### Toolbox F — Information-principle reconstruction axioms

**Idea:** Add operational axioms (purification, no-broadcasting, reversibility, …) that force Hilbert-space kinematics, treating the expression forest as a substrate that must satisfy those constraints.

| Pros | Cons |
|------|------|
| Connects to Hardy / CDP / CBH-style reconstructions | Does not *derive* amplitudes from share/reduce; selects theories that already have them |
| Clear external benchmarks | Shifts the project from generative substrate to constraint satisfaction |

**When to revisit:** for comparative foundations work, or if the goal shifts from “generate QM from expressions” to “show the expression ontology can host a unique quantum information theory.”

---

## 4. Named operation register (active direction)

| Operation | Role |
|-----------|------|
| `share_weight` | complex / U(1) weight on a `share` link |
| `linear_reduce` | weighted sum of share-linked residuals |
| `coherent_set` | residuals with isolation > maintain |
| `isolation_cost` / `maintain_cost` | real structural scalars |
| `structural_decoherence` | drop terms from the linear combination |
| `path_recombine` / `intensity` / `visibility_amplitude` | interference |
| `phase_accumulate` | sequential evolution of share weights |
| `born_extract` | \(\lvert a\rvert^2\) reading at structural selection |
| `attach_sequential_state` | COM or path-wise \((x,v)\) |
| `preferential_select` / `sequential_tick` | classical sequential update |
| `path_recombine_with_velocity` / `com_from_amplitudes` | sequential reconciliation |
| `classical_limit_of_coherence` | decoherence → classical trajectory |

---

## 5. Status

**Active commitment**
- Linear `reduce` on share-weighted residuals.
- Real isolation/maintain costs and structural decoherence retained.
- Born rule as reading at selection; phase accumulation as weight dynamics on sequential history.

**Toolbox retained** for future refinement: complex action (A), soft `eq` (B), complex sequential parameter (C), external amplitudes (D), categorical process package (E), information-principle constraints (F).

**Still open**
- Executable implementation of `linear_reduce` over the term language in `sim/expr_tree.py`.
- Unitarity of weight evolution between decoherence events.
- Whether \(\varphi_i\) can be forced from binding geometry.
- Multi-cluster forces, fields, spectra.
