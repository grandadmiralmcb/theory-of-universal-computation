# 03 — Quantum Sector (Structural Recovery + Minimal Enrichment)

Goal: recover quantum-like multi-path coherence, interference, and measurement from the reduced sequential calculus, adding new structure only where the purely structural counts are provably insufficient.

Every step is labeled with an operation name.

---

## Part A — Purely structural multi-path regime

### A1. Coherent multi-path set

**Operation: `share_link`**

When two (or more) residuals \(E_1, E_2\) remain connected by one or more `share` nodes, a local evaluator that has not yet paid the isolation cost continues to track both. The coherent set is

\[
\mathcal{C} = \{E_i \mid C_{\rm isolate}(E_i) > C_{\rm maintain}\}.
\]

**Operation: `coherent_set`**

As long as the inequality holds, sequential projection does not force a single residual. This is the structural substrate of superposition: simultaneous dependence on multiple residuals linked by sharing.

---

### A2. Isolation cost and structural decoherence

**Operation: `isolation_cost`**

\(C_{\rm isolate}(E_i)\) = structural disruption (in \(S\), \(B\), \(D\)) required to eliminate all `share` links connecting \(E_i\) to the rest of \(\mathcal{C}\).

**Operation: `maintain_cost`**

\(C_{\rm maintain}\) = ongoing disruption cost of keeping the share links intact under the current sequential strategy.

**Operation: `structural_decoherence`**

When

\[
C_{\rm isolate}(E_i) \le C_{\rm maintain}
\]

the preference for low disruption forces the break. Path \(E_i\) is dropped from \(\mathcal{C}\). Multi-path coherence is lost. This is measurement-like selection without an extra collapse postulate: it is ordinary preferential sequentialization applied to share architecture.

---

### A3. Limits of pure structure

Structural counts supply:
- which paths remain coherent,
- when coherence is lost,
- a qualitative visibility (coherence persists while isolation is expensive).

They do **not** by themselves supply:
- continuous interference fringes,
- relative phases,
- Born-rule probabilities.

Those require a weight on each path that can add (and cancel) upon recombination. The next section introduces the minimal enrichment that supplies path weights while remaining inside the expression ontology.

---

## Part B — Minimal amplitude enrichment (Route A, tightened)

### B1. Amplitude-valued residuals

**Operation: `amplitude_weight`**

Each residual in a coherent set carries a weight \(a_i \in \mathcal{A}\). Working choice: \(\mathcal{A} = \mathbb{C}\).

The weight is not a new ontological kind of substance; it is an attribute of the residual under the current share architecture, analogous to how \(S\), \(B\), \(D\) are attributes of a reduction step.

**Operation: `force_A`** (amplitude-valued reduction)

\[
\texttt{force}_A : \texttt{Expr} \to \mathcal{A}(\texttt{Val})
\]

Multiple reduction paths receive weights; when paths recombine, weights add.

---

### B2. Interference on recombination

**Operation: `path_recombine`**

When two share-linked paths that have acquired relative phase structure are brought back into a single sequential context, their amplitudes add:

\[
a_{\rm total} = a_1 + a_2.
\]

Intensity / detection weight:

\[
I \propto |a_{\rm total}|^2 = |a_1|^2 + |a_2|^2 + 2\,\mathrm{Re}(a_1^* a_2).
\]

The cross term is interference. Constructive or destructive outcomes depend on relative phase — a structural attribute of how the paths diverged and recombined under sharing and binding.

---

### B3. Born-rule extraction

**Operation: `born_extract`**

When structural decoherence forces selection of a single residual from a coherent set, the probability that residual \(i\) is the one retained is

\[
P(i) = \frac{|a_i|^2}{\sum_j |a_j|^2}.
\]

This is the Born rule as the natural normalized weight under amplitude-valued residuals once isolation cost has forced a choice. It is still an enrichment rule, not derived from \(S,B,D\) alone; it is the minimal probabilistic reading of amplitude weights consistent with the structural selection dynamics.

---

### B4. Compatibility with the classical regime

**Operation: `classical_limit_of_coherence`**

When an excitation becomes large, high-share-density, and strongly linked to a macroscopic sequential evaluator:

1. Isolation costs of alternative paths fall (or maintain costs rise) rapidly.
2. **`structural_decoherence`** eliminates all but one residual.
3. Surviving dynamics reduce to ordinary lowest-cost sequential trajectories (Part A of the classical limit).

Thus the same preferential sequentialization that produces Newtonian motion under constant bias also suppresses multi-path coherence in the macroscopic regime. Quantum and classical regimes are two limits of one dynamics, distinguished by whether share isolation remains expensive.

---

## Part C — Named operation summary (quantum)

| Operation | Role |
|-----------|------|
| `share_link` | keep residuals co-dependent via `share` |
| `coherent_set` | collection of residuals with isolation cost still high |
| `isolation_cost` | disruption required to break a path out of the set |
| `maintain_cost` | cost of preserving share links |
| `structural_decoherence` | drop path when isolation ≤ maintain |
| `amplitude_weight` | complex weight on a residual |
| `force_A` | amplitude-valued reduction |
| `path_recombine` | amplitude addition on shared recombination |
| `born_extract` | \(|a_i|^2\) normalized probabilities on selection |
| `classical_limit_of_coherence` | decoherence → single high-\(\kappa\) trajectory |

---

## Part D — Status and open contentions

**Recovered structurally (no amplitude needed)**
- Multi-path coherence as share-linked residual sets.
- Decoherence as isolation-cost vs maintain-cost inequality.
- Classical limit as forced single-path sequentialization.

**Recovered with minimal enrichment**
- Interference fringes via amplitude addition.
- Born-rule probabilities on structural selection.

**Still open**
- Can relative phase / amplitude structure itself be derived from deeper share and binding geometry, or must \(\mathcal{A}=\mathbb{C}\) remain a controlled enrichment?
- Quantitative two-path visibility curve from a fully specified isolation-cost + amplitude model.
- Discrete spectra and particle species from vacuum + labels (requires the label enrichment of Route A).
- Relation to Hilbert-space kinematics and unitary evolution between decoherence events.

---

## Relation to earlier Route A document

The previous Route A list (linear typing, labels, vacuum \(V\), bounded signal) remains available as further controlled enrichment when particle spectra and conservation laws are required. The present document prioritizes the multi-path / interference / measurement sector that can be reached with only sharing + structural cost + minimal amplitude weights, keeping the adversarial surface as small as possible.
