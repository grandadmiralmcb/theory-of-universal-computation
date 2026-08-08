# 14 — Derivation from Ontological Minima

Build outward from O1–O4 only. Every step is either forced or explicitly postulational.

---

## 0. Ontological minima (assumptions)

**O1.** Structured, evaluable information exists (composition, sharing, reduction under strategies).

**O2.** Sequential order is constructed locally by successive reduction; it is not a global parameter of the structure.

**O3.** Among admissible reductions, dynamics prefer lower structural disruption (disruption = change to sharing, binding, or observational identity).

**O4.** Non-selected structure remains real.

No other ontological assumptions enter Part I.

---

## Part I — Forced consequences (F1–F5)

### F1 — Local sequential trajectories [from O2]

**Claim.** For any evaluator, the record of successive reductions is a (possibly finite) chain
\[
E_0 \xrightarrow{s_1} E_1 \xrightarrow{s_2} \cdots
\]
that chain *is* sequential order for that evaluator.

**Derivation.** O2: sequential order is constructed by successive reduction. The construction yields a chain ordered by reduction steps. No global time parameter is required. ☐

---

### F2 — Existence of a minimal-disruption residual [from O3 + finiteness]

**Additional hypothesis (local, not ontological):** the set \(\mathcal{R}\) of admissible one-step residuals from a given state is finite and non-empty, and disruption induces a total preorder \(\preceq\) on \(\mathcal{R}\).

**Claim.** There exists \(r^*\in\mathcal{R}\) minimal with respect to \(\preceq\), and O3 licenses selection of such an \(r^*\).

**Derivation.** Finite non-empty set + total preorder \(\Rightarrow\) non-empty set of minima. O3: dynamics prefer lower disruption \(\Rightarrow\) selection among minima. ☐

**Note.** Finiteness of \(\mathcal{R}\) is a regularity hypothesis for this lemma, not part of O1–O4. Without it, one needs existence of minima by other means (e.g. well-foundedness).

---

### F3 — Persistence of the unselected [from O4]

**Claim.** If \(r^*\) is selected and \(r\in\mathcal{R}\setminus\{r^*\}\), then \(r\) (and structure supporting it) remains real.

**Derivation.** Immediate from O4. ☐

---

### F4 — Co-dependence has a disruption comparison [from O1 + O3]

**Claim.** If two residuals share substructure (co-dependence via sharing, from O1), then:
- maintaining the sharing is one admissible disposition;
- breaking the sharing is another;
- both dispositions have disruption ranks under O3’s comparison when both are admissible.

**Derivation.** O1 admits sharing of substructure. Breaking shared substructure changes sharing (hence is disruption). Maintaining it is the alternative disposition. O3 applies to any pair of admissible reductions/dispositions that differ in disruption. ☐

---

### F5 — Structural projection event [from F4 + O3]

**Claim.** When the disruption of breaking co-dependence is ranked ≤ the disruption of maintaining it, O3 permits selection of the break: a residual may be isolated from the co-dependent set. Call this a **structural projection event**.

**Derivation.** F4 supplies the comparison. O3 selects lower (or equal, if policy allows) disruption. Isolation is the selected disposition. ☐

**What F5 does not force:** probabilities over which residual survives; complex weights; continuum of outcomes.

---

## Part II — What cannot be derived from O1–O4

| Target | Why not forced |
|--------|----------------|
| Finite expression trees only | O1 allows any evaluable structure; finiteness is WM1 |
| Numeric cost \(C=\alpha S+\beta B+\gamma D\) | O3 is ordinal preference; cardinal cost is WM2 |
| \(m \propto\) share count | Proxy definition WM3; O3 does not fix cardinal inertia |
| Real \(x\), \(\ddot x=-b/m\) | Requires CI1–CI3 + WM sequential calculus |
| Complex amplitudes | Requires A4 (type change) |
| Unitarity of free evolution | Requires A4 + D19 + B_flow |
| Born rule | Requires D12 reading or a future derivation |
| Monism as theorem | Preferred reading only |
| Consciousness = high coherence sequentialization | Open interpretive link |

**Fixed negative results**

- **N1:** Bare ordinal disruption preference does not determine a unique cardinal cost.
- **N2:** Disruption counts that ignore weights cannot constrain weight moduli or support (hence cannot force N★/R★ without D19/B_flow).
- **N3:** O1–O4 do not force continuum sequential parameters.

---

## Part III — Working model as optional sharpening

Postulates **WM1–WM3** (finite terms; cardinal \(C\); \(m=\alpha n+\varepsilon\)) turn F1–F5 into quantitative WM theorems (T1, T2, T9–T12 in `docs/11-theorems.md`).

**Derivation pattern (example: isolation criterion)**

1. O1+O3 \(\Rightarrow\) F4 (comparison exists).
2. WM1+WM2 \(\Rightarrow\) comparison is numeric \(C_{\rm isolate}\) vs \(C_{\rm maintain}\).
3. O3+F2 \(\Rightarrow\) select cheaper alternative.
4. **T10 [WM]:** if \(C_{\rm isolate}\le C_{\rm maintain}\), isolate.

Every use of WM1–WM3 must appear in the hypothesis list.

---

## Part IV — Continuum idealization as optional limit

Postulates **CI1–CI4** + WM sequential updates (T3–T4 under WM3, CI1, CI4) yield:

- **T5 [CI]:** \(\ddot x = -b/m\) in the tick continuum limit.
- **T6 [WM+CI]:** acceleration ratio = inverse inertia ratio for two clusters under same \(b\).

T6 is the strongest quantitative claim: forced given WM1–WM3 + CI1–CI2 + constant bias — not forced by O1–O4 alone.

---

## Part V — Hosted linear layer as optional extension

To speak of interference and unitary free evolution one must adopt:

- **A4** linear weighted residuals,
- **D19** weight-sensitive cost,
- **B_flow** invertible free-epoch flows,
- **D12** Born reading (unless replaced by a derivation).

Then T12+ , N★, R★, T13, T14 follow as in `docs/11-theorems.md` under those hypotheses.

**Derivation-first rule:** do not say “O3 implies unitarity.” Say “O3 + D19 + B_flow + A4 imply unitarity on the active subspace.”

---

## Part VI — Build-out map (only forced arrows)

```
O1, O2, O3, O4
    │
    ├─ F1 sequential chains
    ├─ F2 minimal residual (needs finite ℜ or well-foundedness)
    ├─ F3 unselected persists
    ├─ F4 co-dependence comparable
    └─ F5 structural projection when break ≤ maintain

F1–F5  +  WM1,WM2,WM3  →  quantitative WM theorems (cost, isolation, T10–T12)
WM theorems  +  CI1,CI2,CI3,CI4  →  continuum sequential calculus (T5–T8), T6 ratio
F5  +  A4,D19,B_flow  →  unitary free epoch, projection as non-unitary locus
(+ D12)  →  Born statistics at projection (reading)
```

No arrow from O1–O4 alone to continuum, amplitudes, or Born.

---

## Part VII — Immediate research discipline

1. **New claims** must cite O1–O4 and every postulate used.
2. **WM results** stay valuable as exact theorems under WM1–WM3; they do not upgrade ontology.
3. **Next derivation targets** (in order of loyalty to derivation-first):
   - Weaken finiteness in F2 (well-founded disruption or compact residual spaces).
   - Derive a cardinal disruption measure from representation theorems (if any) rather than stipulating WM2.
   - Internalize sequential labels in structure (reduce dependence on CI1 as external).
   - Born: either derive from extended preference at F5 or permanently mark D12 non-derived.
4. **Do not** re-ontologize finite trees or treat A4 as forced by O3.
