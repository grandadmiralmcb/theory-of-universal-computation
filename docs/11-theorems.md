# 11 — Theorems from Axioms

Formal chain from stated axioms to the results the theory relies on. Each theorem lists hypotheses, claim, and proof sketch with named operations.

**Convention.** Axioms (A1–A7) are taken as given. Definitions (D1–D12) introduce derived notions. Theorems (T1–T14) are proved. Lemmas internal to a proof are numbered locally. Semi-forced principles (R, N) from `docs/10-unitarity-from-projection.md` are flagged where used.

---

## Part 0 — Axioms and definitions

### Axioms

| ID | Statement |
|----|-----------|
| **A1** | The operative substrate is structured, evaluable information under the reduced primitives `app`, `abs`, `pair`/`proj`, `eq`, `reduce`, `share`. |
| **A2** | Sequential order is a local construction of evaluators, not a global parameter of the forest. |
| **A3** | Dynamics favor minimal structural disruption: among admissible reduction steps, those of least structural cost are selected (`preferential_select`). |
| **A4** | On share-linked residuals, reduction may be linear: `linear_reduce` yields \(\sum_i a_i E_i\) with weights on `share` (`share_weight`). |
| **A5** | Local evaluators are themselves informational patterns that generate sequential projections. |
| **A6** | Residuals not selected (or not yet projected by structural decoherence) remain real parts of the expression forest. |
| **A7** | Matter- and energy-like behaviour are dual sequential presentations of the same class of informational excitations, indexed by structural disruption measures. |

### Definitions

**D1 (Structural counters).** For a reduction step \(E \xrightarrow{s} E'\):
- \(S\) = number of distinct `share` nodes whose shared content is broken or duplicated;
- \(B\) = net change in open binding sites (`abs`/`app` structure);
- \(D\) = 1 if the residual fails `eq` under the current strategy, else 0.

**D2 (Structural cost).** \(C = \alpha S + \beta B + \gamma D\) with \(\alpha,\beta,\gamma > 0\).

**D3 (Structural inertia).** For a cluster with sequential parameter \(x\),
\(m_{\rm struct} = \langle S(\delta x = 1)\rangle\) (average share disruption for unit sequential change). In the tree model, \(m_{\rm struct}(E) = \alpha\,n_{\rm share}(E) + \varepsilon\) with \(\varepsilon > 0\).

**D4 (Structural bias).** \(b_{\rm struct}\) = excess disruption imposed by a persistent context on steps against a preferred sequential direction. May depend on \(x\): \(b(x)\).

**D5 (Velocity cost).** \(C(\delta v) = \tfrac12 m_{\rm struct}(\delta v)^2 + b_{\rm struct}\,\delta v\).

**D6 (Coherent set).** \(\mathcal{C} = \{E_i \mid C_{\rm isolate}(E_i;\mathcal{C}) > C_{\rm maintain}(\mathcal{C})\}\).

**D7 (Isolation cost).** \(C_{\rm isolate}(E_i;\mathcal{C}) = \alpha|\Sigma_i| + \beta B(\Sigma_i) + \gamma[|\Sigma_i|>0]\), where \(\Sigma_i\) is the set of Share nodes of \(E_i\) shared with other members of \(\mathcal{C}\).

**D8 (Maintain cost).** \(C_{\rm maintain}(\mathcal{C}) = \alpha(|\text{cross-member shares}| + N_{\rm env}) + \beta B_{\rm cross}\).

**D9 (Free epoch).** Interval during which \(C_{\rm isolate}(E_i) > C_{\rm maintain}\) for all \(E_i\in\mathcal{C}\).

**D10 (Share weight).** Each relevant `share` may carry \(a\in\mathbb{C}\) (or U(1)).

**D11 (Linear residual).** Under A4, a multi-path residual has the form \(\sum_i a_i E_i\).

**D12 (Born reading).** At structural selection, \(P(i) = |a_i|^2 / \sum_j |a_j|^2\).

---

## Part I — Structural cost and classical sequential dynamics

### T1 — Structural cost is well-defined from the primitives

**Hypotheses.** A1; D1–D2.

**Claim.** For any reduction step expressible with the reduced primitives, \(S\), \(B\), and \(D\) are uniquely determined, and \(C\in\mathbb{R}_{\ge 0}\).

**Proof.**  
(1) Distinct `share` nodes are identifiable by object identity in the term graph (A1, `share`). Breaking or duplicating one increments \(S\) by 1.  
(2) Open binding sites are the residual `abs` nodes not discharged by `app` (A1). Net change under the step is \(B\in\mathbb{Z}\); in cost we use a non-negative measure of disruption (e.g. \(|B|\) or positive part as fixed by convention in D1).  
(3) `eq` returns a binary observational verdict (A1); failure contributes \(D=1\).  
(4) With \(\alpha,\beta,\gamma>0\) and non-negative counters, \(C\ge 0\). Uniqueness follows from uniqueness of the term graph and the strategy’s residual. ☐

---

### T2 — Preferential sequentialization selects a minimal-cost residual

**Hypotheses.** A3; D2; finite set of admissible one-step residuals.

**Claim.** `preferential_select` returns a residual of minimal \(C\). If several achieve the minimum, the set of minimizers is the admissible coherent outcome set at that step.

**Proof.** Immediate from A3 and finiteness: the argmin of a real function on a finite non-empty set exists and is attained on a non-empty subset. ☐

---

### T3 — Optimal velocity update under quadratic cost

**Hypotheses.** D3–D5; \(m_{\rm struct}>0\).

**Claim.** \(\arg\min_{\delta v} C(\delta v) = -b_{\rm struct}/m_{\rm struct}\).

**Proof.** \(C(\delta v) = \tfrac12 m(\delta v)^2 + b\,\delta v\) is a strictly convex quadratic in \(\delta v\). Derivative: \(m\,\delta v + b = 0\) \(\Rightarrow\) \(\delta v^* = -b/m\). Second derivative \(m>0\) confirms minimum. ☐

---

### T4 — Discrete sequential dynamics

**Hypotheses.** T3; tick duration \(\tau>0\); sequential state \((x_n,v_n)\).

**Claim.** The updates
\[
v_{n+1} = v_n + \delta v^*\,\tau = v_n - \frac{b}{m}\tau, \qquad
x_{n+1} = x_n + v_{n+1}\tau
\]
(with the integrator convention that position uses the updated velocity) realize one step of preferential sequentialization on the sequential parameters.

**Proof.** By T3 the preferred velocity change rate is \(\delta v^*\). Integrating the rate over duration \(\tau\) yields the velocity update. The position update is the definition of sequential advance under the maintained velocity (A2, sequential parameter as evaluator construct). ☐

---

### T5 — Continuum limit under constant bias (Newtonian regime)

**Hypotheses.** T4; \(b_{\rm struct}=b\) constant; \(\tau\to 0\), \(n\to\infty\), \(t=n\tau\) fixed.

**Claim.** \(\dfrac{dv}{dt} = -\dfrac{b}{m_{\rm struct}}\), \(\dfrac{dx}{dt} = v\), hence \(\ddot{x} = -\dfrac{b}{m_{\rm struct}}\).

**Proof.** From T4, \(\Delta v / \tau = -b/m\) and \(\Delta x / \tau = v\) (to first order). Taking the continuum limit of the difference quotients yields the ODEs. Eliminating \(v\) gives the second-order equation. ☐

---

### T6 — Inverse share-count acceleration ratio (parameter-free)

**Hypotheses.** T5; two clusters \(E_A,E_B\) with share counts \(n_A,n_B\); same constant bias \(b\); tree inertia \(m = \alpha n + \varepsilon\) (D3).

**Claim.**
\[
\frac{a_A}{a_B} = \frac{m_B}{m_A} = \frac{\alpha n_B + \varepsilon}{\alpha n_A + \varepsilon}.
\]
In particular, if \(\varepsilon \ll \alpha n_A,\alpha n_B\) or the ratio is taken with identical \((\alpha,\varepsilon)\),
\[
\frac{a_A}{a_B} \to \frac{n_B}{n_A}.
\]

**Proof.** By T5, \(a = -b/m\) under constant \(b\). Ratio of accelerations is the inverse ratio of inertias. Substitute D3. The constants \(\alpha,\varepsilon\) appear in both numerator and denominator and cancel in the leading large-share limit. ☐

**Remark.** This is the theory’s sharpest parameter-free quantitative prediction. It fails if measured sequential accelerations under common bias do not track the inverse share-count ratio once trees (hence \(n_A,n_B\)) are fixed.

---

### T7 — Projectile motion under constant bias

**Hypotheses.** T5; initial data \(x(0)=h\), \(v(0)=v_0\); \(g_{\rm eff} = b/m_{\rm struct}\).

**Claim.** \(v(t)=v_0-g_{\rm eff}t\), \(x(t)=h+v_0 t-\tfrac12 g_{\rm eff}t^2\), and the positive landing time is
\[
t_{\rm land} = \frac{v_0 + \sqrt{v_0^2 + 2 g_{\rm eff} h}}{g_{\rm eff}}
\]
(when defined).

**Proof.** Direct integration of T5 with constant \(g_{\rm eff}\). Landing root of \(x(t)=0\). ☐

---

### T8 — Position-dependent bias yields Newton’s second law

**Hypotheses.** T3–T5 with \(b = b(x) = V'(x)\).

**Claim.** \(m_{\rm struct}\,\ddot{x} = -V'(x)\).

**Proof.** T3 gives \(\delta v^* = -b(x)/m\). Continuum limit as in T5 with \(b\) evaluated at the current \(x\) yields \(\ddot{x} = -V'(x)/m\). ☐

---

## Part II — Multi-path structure and decoherence

### T9 — Isolation and maintain costs are well-defined from trees

**Hypotheses.** A1; D7–D8; finite term graphs.

**Claim.** For any finite coherent-set candidate, \(C_{\rm isolate}\) and \(C_{\rm maintain}\) are uniquely determined non-negative reals.

**Proof.** Share nodes are finite and identifiable by identity. \(\Sigma_i\) is the intersection of the path’s share-set with the union of other members’ share-sets — a finite set. Cross-member shares are those appearing in at least two members. Environmental share count \(N_{\rm env}\) is an external non-negative integer parameter. Counters and cost form match T1. ☐

---

### T10 — Structural decoherence criterion

**Hypotheses.** A3; D6–D8; T2; T9.

**Claim.** If \(C_{\rm isolate}(E_i;\mathcal{C}) \le C_{\rm maintain}(\mathcal{C})\), preferential sequentialization selects breaking the shares in \(\Sigma_i\) over maintaining them, and \(E_i\) leaves \(\mathcal{C}\).

**Proof.** The two alternatives at the relevant step are (a) maintain all cross-links (cost \(C_{\rm maintain}\)) and (b) break \(\Sigma_i\) (cost \(C_{\rm isolate}\)). By A3/T2 the lower-cost alternative is selected. When (b) is cheaper or equal, isolation occurs and \(E_i\notin\mathcal{C}\) thereafter (D6). ☐

---

### T11 — Classical limit of coherence

**Hypotheses.** T10; environmental share density increases \(N_{\rm env}\) so that \(C_{\rm maintain}\) eventually meets or exceeds isolation costs of all but one path.

**Claim.** \(\mathcal{C}\) reduces to a singleton; subsequent dynamics are ordinary preferential sequentialization on that path’s sequential state (Part I).

**Proof.** Apply T10 repeatedly as \(C_{\rm maintain}\) rises. When only one path remains, D6 gives a singleton. Free multi-path form ceases; T2–T5 apply to the survivor. ☐

---

## Part III — Linear weights and unitarity constraints

### T12 — Free evolution does not act by share-breaking

**Hypotheses.** D9; A3; T10.

**Claim.** During a free epoch, weight updates cannot be realized by breaking shares that define \(\mathcal{C}\).

**Proof.** Breaking such a share would be an isolation step. By D9, isolation cost still exceeds maintain cost, so A3/T10 forbid isolation. Therefore free-epoch dynamics are share-preserving. ☐

---

### T13 — Unitarity on the active subspace (conditional)

**Hypotheses.** T12; A4; D10–D11;
- **Assumption R:** share-preserving linear reduce is operationally reversible (no structural loss \(\Rightarrow\) invertible weight map);
- **Principle N:** relative moduli \(|a_i|/|a_j|\) cannot change at zero structural cost (cost is sole currency for selection-relevant quantities).

**Claim.** Free-epoch weight evolution is unitary on the span of active path weights.

**Proof.**  
(1) By T12, evolution is share-preserving.  
(2) By R, the induced map \(U_\tau\) on weight space is invertible.  
(3) By N, relative moduli are frozen; combined with ray-gauge freedom of D12, fix \(\sum_i |a_i|^2 = \mathrm{const}\).  
(4) An invertible linear map on a finite-dimensional complex inner-product space that preserves the Euclidean norm is unitary.  
(5) If share architecture permits coherent redistribution inside \(\mathcal{C}\), the unitary group is full on that subspace; if only path-local phase is admitted, evolution is diagonal unitary in the path basis. ☐

**Status.** Conditional on R and N (semi-forced; see `docs/10-unitarity-from-projection.md`). Not a theorem of A1–A3 + real counters alone.

---

### T14 — Structural decoherence is the sole non-unitary locus

**Hypotheses.** T13 (under R, N); T10.

**Claim.** Within the active direction, weight dynamics are unitary in free epochs and non-unitary precisely when structural decoherence drops paths (projection onto the surviving subspace, up to Born reading normalization).

**Proof.** T13 gives unitarity in free epochs. When T10 fires, the map on weight space deletes coordinates of dropped paths — a projection, not a unitary. No other non-unitary mechanism is present in the active direction. ☐

---

## Part IV — Dependency graph

```
A1–A3, D1–D2  →  T1 (cost well-defined)
A3, T1         →  T2 (preferential select)
D3–D5          →  T3 (optimal δv)
T3, A2         →  T4 (discrete dynamics)
T4             →  T5 (continuum Newton)
T5, D3         →  T6 (inverse share-count ratio)
T5             →  T7 (projectile)
T5, b=V'       →  T8 (conservative force)
A1, D7–D8      →  T9 (isolation/maintain well-defined)
A3, T2, T9     →  T10 (decoherence criterion)
T10            →  T11 (classical limit of coherence)
D9, A3, T10    →  T12 (free epoch share-preserving)
T12, A4, R, N  →  T13 (unitarity conditional)
T13, T10       →  T14 (non-unitary locus = projection)
```

---

## Part V — Gaps (theorems not yet obtained)

| Desired result | Blocker |
|----------------|---------|
| R as theorem (not assumption) | Need formal invertibility of share-preserving linear reduce in the term language |
| N as theorem | Need cost calculus to charge any relative-modulus change |
| Born rule as theorem | Still a reading (D12), not derived from A1–A3 |
| Generator of \(\varphi_i\) | No structural Hamiltonian from binding geometry yet |
| Sequential parameter \(x\) from syntax alone | Still attached by evaluator convention |
| Multi-body forces, fields, spectra | Outside current axiom reach |

---

## Part VI — Status

**Proved from A1–A3 + definitions:** T1–T12, T14 (non-unitary locus relative to T13).

**Conditional (R, N):** T13 unitarity.

**Executable support:** T3–T8 (toy simulator); T6/T9 (expr_tree); T10 structural pattern (two_path).

**Next dogfooding:** formalize R and N inside the term language; end-to-end tree → \(m_{\rm struct}\) → measured acceleration ratio; implement `linear_reduce` with free-epoch unitary updates.
