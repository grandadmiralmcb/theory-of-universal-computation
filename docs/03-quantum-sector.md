# 03 — Quantum Sector

Structural multi-path coherence, isolation-cost decoherence, minimal amplitude enrichment, classical limit of coherence, and **velocity coupling** between coherent sets and the sequential calculus.

Every derivation names the operation performed.

---

## 0. Shared substrate

Reduced primitives and structural cost remain in force:

\[
C = \alpha S + \beta B + \gamma D
\]

Preferential low-disruption sequentialization (`preferential_select`) is the sole dynamical principle. Classical sequential calculus: `docs/02-dynamics.md`.

---

## 1. Purely structural multi-path regime

### 1.1 Share-linked residuals

**Operation: `share_link`**

Residuals are co-dependent when connected by `share` nodes.

**Operation: `coherent_set`**

\[
\mathcal{C} = \bigl\{ E_i \;\big|\; C_{\rm isolate}(E_i;\mathcal{C}) > C_{\rm maintain}(\mathcal{C}) \bigr\}.
\]

### 1.2 Isolation and maintain costs

**Operation: `isolation_cost`**

\[
C_{\rm isolate}(E_i;\mathcal{C})
  = \alpha\,\lvert\Sigma_i\rvert + \beta\, B_{\rm isolate}(E_i) + \gamma\, D_{\rm isolate}(E_i)
\]

**Operation: `maintain_cost`**

\[
C_{\rm maintain}(\mathcal{C})
  = \alpha\, S_{\rm maintain} + \beta\, B_{\rm maintain} + \gamma\, D_{\rm maintain}
\]

### 1.3 Structural decoherence

**Operation: `structural_decoherence`**

\[
\textbf{if } C_{\rm isolate}(E_i;\mathcal{C}) \le C_{\rm maintain}(\mathcal{C})
\quad\textbf{then}\quad
\mathcal{C} \leftarrow \mathcal{C}\setminus\{E_i\}.
\]

### 1.4 Structural visibility

**Operation: `visibility_structural`** — binary: 1 iff all active paths still satisfy isolation > maintain.

---

## 2. Minimal amplitude enrichment

### 2.1 Weights and reduction

**Operation: `amplitude_weight`** — \(a_i\in\mathbb{C}\) on each residual in \(\mathcal{C}\).

**Operation: `force_A`** — amplitude-valued reduction.

### 2.2 Recombination and interference

**Operation: `path_recombine`** — \(a_{\rm tot}=\sum_i a_i\).

**Operation: `intensity`** — \(I\propto\lvert a_{\rm tot}\rvert^2\).

**Operation: `visibility_amplitude`**

\[
\mathcal{V} = \frac{2\lvert a_1\rvert\lvert a_2\rvert}{\lvert a_1\rvert^2+\lvert a_2\rvert^2}
\]

when both paths active; else 0.

### 2.3 Born extraction

**Operation: `born_extract`**

\[
P(i) = \frac{\lvert a_i\rvert^2}{\sum_j\lvert a_j\rvert^2}.
\]

---

## 3. Velocity coupling

A coherent set is not only a collection of residuals and amplitudes; it can carry sequential parameters. This section derives how classical sequential dynamics and multi-path structure couple.

### 3.1 Sequential parameters on a coherent set

**Operation: `attach_sequential_state`**

Two consistent options:

| Mode | Sequential state | When natural |
|------|------------------|--------------|
| **Centre-of-mass (COM)** | single \((x,v)\) for the whole \(\mathcal{C}\) | paths not spatially distinguished; shared trajectory label |
| **Path-wise** | each \(E_i\) carries \((x_i,v_i)\) | paths diverge in sequential parameter (e.g. different arms of an interferometer) |

Both are permitted by the formalism. COM is the minimal coupling; path-wise is required for differential bias and which-path sequential distinction.

---

### 3.2 COM mode — collective sequential dynamics

**Operation: `com_velocity_cost`**

Treat \(\mathcal{C}\) as a single high-resistance object with structural inertia

\[
m_{\mathcal{C}} = m_{\rm struct}(\mathcal{C})
\]

(function of total share density of the set). Under bias \(b(x)\):

\[
C(\delta v) = \tfrac12 m_{\mathcal{C}}(\delta v)^2 + b(x)\,\delta v.
\]

**Operation: `preferential_select`** (unchanged)

\[
\delta v^* = -\frac{b(x)}{m_{\mathcal{C}}}.
\]

**Operation: `sequential_tick`** (on COM)

\[
v \leftarrow v + \delta v^*\,\tau, \qquad x \leftarrow x + v\,\tau.
\]

Amplitudes are passengers: they are not altered by COM sequential updates unless a separate free-evolution rule (phase accumulation) is active.

**Continuum limit**

\[
m_{\mathcal{C}}\,\ddot{x} = -b(x).
\]

A coherent set in COM mode behaves as one classical body of mass \(m_{\mathcal{C}}\) until `structural_decoherence` or `path_recombine` occurs.

---

### 3.3 Path-wise mode — differential sequential dynamics

**Operation: `pathwise_velocity_cost`**

Each active path \(E_i\) has its own sequential state \((x_i,v_i)\) and inertia \(m_i\). Local bias may differ:

\[
C_i(\delta v_i) = \tfrac12 m_i(\delta v_i)^2 + b_i(x_i)\,\delta v_i.
\]

**Operation: `preferential_select`** (per path)

\[
\delta v_i^* = -\frac{b_i(x_i)}{m_i}.
\]

**Operation: `sequential_tick`** (per path)

\[
v_i \leftarrow v_i + \delta v_i^*\,\tau, \qquad x_i \leftarrow x_i + v_i\,\tau.
\]

Paths can separate in sequential parameter space. Share links remain until isolation costs are paid. Differential bias is the structural origin of which-path information: if \(b_1\neq b_2\) strongly, sequential trajectories diverge and isolation often becomes cheap (decoherence).

---

### 3.4 Phase accumulation under path-wise motion (minimal enrichment)

**Operation: `phase_accumulate`**

While paths remain in \(\mathcal{C}\), each path may accumulate phase from its sequential history. Minimal rule (controlled enrichment):

\[
a_i(t+\tau) = a_i(t)\,\exp\bigl(-i\,\varphi_i\,\tau\bigr),
\qquad
\varphi_i = \varphi_i(x_i,v_i;\text{binding context}).
\]

A simple structural proxy: \(\varphi_i\) proportional to residual binding cost along the path (or to a potential evaluated on that path). Relative phase \(\Delta\phi\) then drives interference upon `path_recombine`.

This is the natural bridge between sequential motion and the interference cross term. It is still an enrichment (phase is not forced by \(S,B,D\) alone) but is tightly coupled to the sequential state already maintained by the evaluator.

---

### 3.5 Recombination with velocity

**Operation: `path_recombine_with_velocity`**

When paths are brought back into a single sequential context (share architecture forces or permits recombination):

1. **`path_recombine`** — amplitudes add: \(a_{\rm tot}=\sum a_i\).
2. Sequential parameters must be reconciled. Minimal rules:
   - **COM inheritance:** surviving sequential state is the amplitude-weighted mean
     \[
     x = \frac{\sum_i \lvert a_i\rvert^2 x_i}{\sum_j \lvert a_j\rvert^2}, \quad
     v = \frac{\sum_i \lvert a_i\rvert^2 v_i}{\sum_j \lvert a_j\rvert^2}.
     \]
   - **Selection inheritance:** if recombination coincides with `structural_decoherence` / `born_extract`, the chosen path’s \((x_i,v_i)\) becomes the sequential state of the singleton.

**Operation name for the weighted-mean rule:** `com_from_amplitudes`.

---

### 3.6 Decoherence with velocity

**Operation: `structural_decoherence`** (velocity-aware)

When a path is dropped:

- Its amplitude is removed from future recombinations.
- Its sequential state is discarded (or archived as a non-projected residual).
- The surviving set retains its own sequential parameters (COM or remaining path-wise states).

If environmental share density raises `maintain_cost` until only one path remains, the singleton continues under ordinary classical `sequential_tick` with that path’s \((x,v)\) — the classical limit of coherence with velocity intact.

---

### 3.7 Summary derivation — coupled two-path interferometer under bias

**Named pipeline**

1. `share_link` + `amplitude_weight` — prepare two-path coherent set.
2. `attach_sequential_state` (path-wise) — each arm has \((x_i,v_i)\).
3. Possibly different `evaluate_b_at` on each arm.
4. Repeated `preferential_select` + `sequential_tick` (path-wise) + optional `phase_accumulate`.
5. At the second beamsplitter region: `path_recombine_with_velocity` + `intensity` / `visibility_amplitude`.
6. If a detector binding raises isolation cost: `structural_decoherence` + `born_extract` + surviving path’s velocity continues classically.

This is a complete, named account of a biased two-path interferometer inside the expression ontology.

---

## 4. Classical limit of coherence (with velocity)

**Operation: `classical_limit_of_coherence`**

1. Microscopic \(\mathcal{C}\) share-links to a large environmental cluster.
2. `maintain_cost` rises → `structural_decoherence` → singleton.
3. Surviving \((x,v)\) evolves by classical `preferential_select` + `sequential_tick` under ambient bias.

Quantum multi-path and classical single-path motion remain two regimes of one dynamics, now including sequential velocity throughout.

---

## 5. Named operation register (full quantum + velocity)

| Operation | Role |
|-----------|------|
| `share_link` | co-dependence via `share` |
| `coherent_set` | multi-path set under isolation > maintain |
| `isolation_cost` / `maintain_cost` | structural scalars |
| `structural_decoherence` | drop paths |
| `visibility_structural` | binary coherence |
| `amplitude_weight` / `force_A` | complex weights |
| `path_recombine` / `intensity` / `visibility_amplitude` | interference |
| `born_extract` | \(\lvert a\rvert^2\) probabilities |
| `attach_sequential_state` | COM or path-wise \((x,v)\) |
| `com_velocity_cost` / `pathwise_velocity_cost` | cost of \(\delta v\) for set or path |
| `preferential_select` / `sequential_tick` | classical sequential update |
| `phase_accumulate` | path phase from sequential history |
| `path_recombine_with_velocity` | amplitudes + sequential reconciliation |
| `com_from_amplitudes` | weighted-mean sequential state |
| `classical_limit_of_coherence` | decoherence → classical trajectory |

---

## 6. Status

**Closed**
- Structural multi-path + decoherence.
- Amplitude interference + Born extraction.
- COM and path-wise velocity coupling.
- Phase accumulation as minimal enrichment linking motion to interference.
- Recombination and decoherence rules that carry sequential state forward.
- Named interferometer pipeline under bias.

**Open / next**
- Executable path-wise + phase simulator (extend `sim/two_path.py`).
- Whether \(\varphi_i\) can be forced from binding geometry alone.
- Multi-cluster interaction forces; continuum fields; spectra.
