# 03 — Quantum Sector

Structural multi-path coherence, isolation-cost decoherence, minimal amplitude enrichment, and the classical limit of coherence.

Every derivation names the operation performed. Operations compose with the structural sequential calculus of `docs/02-dynamics.md`.

---

## 0. Shared substrate

The reduced primitives and structural cost remain in force:

\[
C = \alpha S + \beta B + \gamma D
\]

with \(S\) from `share`, \(B\) from `abs`/`app`, \(D\) from `eq`. Preferential low-disruption sequentialization (`preferential_select`) is the sole dynamical principle.

---

## 1. Purely structural multi-path regime

### 1.1 Share-linked residuals

**Operation: `share_link`**

Two residuals \(E_1, E_2\) are share-linked when there exists at least one `share` node whose content is required by both. An evaluator that has not broken those nodes remains dependent on both residuals simultaneously.

**Operation: `coherent_set`**

\[
\mathcal{C} = \bigl\{ E_i \;\big|\; C_{\rm isolate}(E_i;\mathcal{C}) > C_{\rm maintain}(\mathcal{C}) \bigr\}.
\]

While \(\lvert\mathcal{C}\rvert > 1\), sequential projection has not forced a unique residual. This is the structural substrate of superposition.

---

### 1.2 Isolation and maintain costs (explicit)

**Operation: `isolation_cost`**

To isolate residual \(E_i\) from \(\mathcal{C}\) is to break every `share` node that connects \(E_i\) to any other member of \(\mathcal{C}\). Let \(\Sigma_i\) be that set of share nodes. Then

\[
C_{\rm isolate}(E_i;\mathcal{C})
  = \alpha\,\lvert\Sigma_i\rvert
  + \beta\, B_{\rm isolate}(E_i)
  + \gamma\, D_{\rm isolate}(E_i)
\]

where \(B_{\rm isolate}\) counts binding residuals opened by the break and \(D_{\rm isolate}\) is 1 if the post-break residual fails `eq` with the pre-break sequential model.

**Operation: `maintain_cost`**

\[
C_{\rm maintain}(\mathcal{C})
  = \alpha\, S_{\rm maintain}
  + \beta\, B_{\rm maintain}
  + \gamma\, D_{\rm maintain}
\]

counts the ongoing disruption of keeping all current share links of \(\mathcal{C}\) intact under the evaluator’s sequential strategy (including any environmental shares).

---

### 1.3 Structural decoherence

**Operation: `structural_decoherence`**

At each sequential tick, for every \(E_i\in\mathcal{C}\):

\[
\textbf{if }\; C_{\rm isolate}(E_i;\mathcal{C}) \le C_{\rm maintain}(\mathcal{C})
\quad\textbf{then}\quad
\mathcal{C} \leftarrow \mathcal{C}\setminus\{E_i\}.
\]

**Derivation (named steps)**

1. `isolation_cost` / `maintain_cost` — evaluate structural counts.
2. `preferential_select` — among “keep share” vs “break share”, choose the lower \(C\).
3. When break wins, `share` nodes in \(\Sigma_i\) are reduced away; residual leaves \(\mathcal{C}\).

No collapse postulate is added. Selection is ordinary lowest-disruption sequentialization applied to share architecture.

---

### 1.4 Qualitative visibility

**Operation: `visibility_structural`**

Define a coarse visibility for a two-path set:

\[
\mathcal{V}_{\rm struct}
  = \begin{cases}
      1 & \text{if }\min_i C_{\rm isolate}(E_i) > C_{\rm maintain},\\
      0 & \text{otherwise.}
    \end{cases}
\]

Coherence is binary at the pure-structural level: either isolation remains expensive for all paths, or at least one path has already been forced out. Continuous fringe visibility requires path weights (Section 2).

---

## 2. Minimal amplitude enrichment

Pure structure does not supply continuous interference or Born-rule probabilities. The following enrichment is the smallest addition that does, while remaining an attribute of residuals under sharing rather than a new ontological substance.

### 2.1 Amplitude weights

**Operation: `amplitude_weight`**

Each residual \(E_i\in\mathcal{C}\) carries \(a_i\in\mathcal{A}\). Working choice: \(\mathcal{A}=\mathbb{C}\).

**Operation: `force_A`**

\[
\texttt{force}_A : \texttt{Expr} \to \mathcal{A}(\texttt{Val}).
\]

Reduction paths are weighted; recombination adds weights.

---

### 2.2 Path recombination and interference

**Operation: `path_recombine`**

When share-linked paths that have acquired relative phase are brought into a single sequential context:

\[
a_{\rm tot} = \sum_{i\in\mathcal{C}} a_i.
\]

**Operation: `intensity`**

\[
I \propto \lvert a_{\rm tot}\rvert^2
  = \sum_i \lvert a_i\rvert^2
  + 2\sum_{i<j}\mathrm{Re}(a_i^* a_j).
\]

**Two-path specialization**

Let \(a_1 = \lvert a_1\rvert e^{i\phi_1}\), \(a_2 = \lvert a_2\rvert e^{i\phi_2}\), \(\Delta\phi=\phi_1-\phi_2\). Then

\[
I \propto \lvert a_1\rvert^2 + \lvert a_2\rvert^2 + 2\lvert a_1\rvert\lvert a_2\rvert\cos\Delta\phi.
\]

**Operation: `visibility_amplitude`**

\[
\mathcal{V}
  = \frac{I_{\rm max}-I_{\rm min}}{I_{\rm max}+I_{\rm min}}
  = \frac{2\lvert a_1\rvert\lvert a_2\rvert}{\lvert a_1\rvert^2+\lvert a_2\rvert^2}
\]

when both paths remain in \(\mathcal{C}\) (\(\mathcal{V}_{\rm struct}=1\)). If structural decoherence has already dropped a path, \(\mathcal{V}=0\).

---

### 2.3 Born-rule extraction on structural selection

**Operation: `born_extract`**

When `structural_decoherence` reduces \(\mathcal{C}\) to a singleton, or when a detection context forces selection of one residual, the probability that residual \(i\) is retained is

\[
P(i) = \frac{\lvert a_i\rvert^2}{\sum_{j\in\mathcal{C}}\lvert a_j\rvert^2}.
\]

**Derivation (named steps)**

1. `coherent_set` holds with amplitude weights attached.
2. `structural_decoherence` (or an equivalent detection binding) forces a choice.
3. `born_extract` reads normalized modulus-squared weights as selection probabilities.

This is the minimal probabilistic reading of amplitude weights consistent with structural selection. It is an enrichment rule, not a consequence of \(S,B,D\) alone.

---

## 3. Classical limit of coherence

**Operation: `classical_limit_of_coherence`**

**Derivation**

1. A microscopic coherent set \(\mathcal{C}\) becomes share-linked to a large high-resistance environmental cluster (many additional `share` nodes).
2. `maintain_cost` rises with environmental share density; alternatively, isolation of environmental alternatives becomes cheap relative to maintaining global multi-path structure.
3. `structural_decoherence` fires: all but one residual leave \(\mathcal{C}\).
4. Surviving dynamics are ordinary `preferential_select` + `sequential_tick` on a single high-\(\kappa\) trajectory (classical sequential calculus of `docs/02-dynamics.md`).

**Statement**

Quantum multi-path behavior and classical single-path motion are two regimes of the same preferential low-disruption dynamics, distinguished by whether isolation of alternative residuals remains expensive.

---

## 4. Composition with the classical sequential calculus

Between decoherence events, a coherent set may still carry sequential parameters (e.g. centre-of-mass labels). Then:

1. `preferential_select` acts on the sequential parameters of the set as a whole (or on each path’s parameters if they differ).
2. Amplitude weights evolve by whatever enrichment rule is adopted for free evolution (minimal choice: constant weights between recombinations; richer choice: path-dependent phase accumulation from structural binding history).
3. Upon `path_recombine` or `structural_decoherence`, amplitudes and structural costs interact as above.

No conflict arises: classical cost minimization governs sequential labels; amplitude enrichment governs multi-path weights until structure forces selection.

---

## 5. Named operation register (quantum)

| Operation | Input | Output / effect |
|-----------|-------|------------------|
| `share_link` | residuals, `share` nodes | co-dependence |
| `coherent_set` | isolation vs maintain costs | multi-path set \(\mathcal{C}\) |
| `isolation_cost` | residual + \(\mathcal{C}\) | scalar \(C_{\rm isolate}\) |
| `maintain_cost` | \(\mathcal{C}\) + strategy | scalar \(C_{\rm maintain}\) |
| `structural_decoherence` | \(\mathcal{C}\) | possibly smaller \(\mathcal{C}\) |
| `visibility_structural` | costs | binary coherence flag |
| `amplitude_weight` | residual | \(a_i\in\mathbb{C}\) |
| `force_A` | expression | amplitude-valued residual |
| `path_recombine` | weighted paths | \(a_{\rm tot}=\sum a_i\) |
| `intensity` | \(a_{\rm tot}\) | \(\lvert a_{\rm tot}\rvert^2\) |
| `visibility_amplitude` | two-path amplitudes | fringe visibility \(\mathcal{V}\) |
| `born_extract` | weighted \(\mathcal{C}\) on selection | probabilities \(P(i)\) |
| `classical_limit_of_coherence` | environmental share density | single-path classical trajectory |

---

## 6. Status after dogfooding

**Closed formally**
- Explicit \(C_{\rm isolate}\), \(C_{\rm maintain}\) in terms of \(S,B,D\).
- Binary structural visibility and continuous amplitude visibility.
- Interference intensity and two-path fringe formula.
- Born extraction on structural selection.
- Classical limit of coherence as structural decoherence under environmental sharing.
- Clean composition with the classical sequential calculus.

**Still open / next dogfooding targets**
- Executable two-path simulator (coherent set, isolation threshold, amplitude recombination, Born sampling).
- Whether relative phase can be forced from binding geometry rather than assigned.
- Unitary-like free evolution rule between decoherence events derived from structural cost, if possible.
- Labels, vacuum, discrete spectra (further Route A enrichment).
