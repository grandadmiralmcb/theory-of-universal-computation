# 13 — Derive R★ and N★ from Structural Cost

Attempt to obtain free-epoch reversibility and frozen relative moduli from A1–A3 and real structural cost alone. Forced lemmas are separated from residual bridge principles.

---

## 0. What cost actually sees

Structural cost of a step is determined only by:

\[
C = \alpha S + \beta B + \gamma D
\]

- \(S\): share nodes broken or duplicated
- \(B\): change in open bindings
- \(D\): observational inequivalence under `eq`

**Critical observation.**  
Complex weights \(a_i\) on shares are **not** arguments of \(S\), \(B\), or \(D\) as currently defined. Cost is blind to the numerical values of weights. Preferential sequentialization (A3) therefore cannot, by itself, prefer one weight configuration over another unless those configurations differ in share topology, bindings, or observational equivalence.

Any derivation of R★/N★ from cost must either:
1. show that non-R or non-N maps necessarily alter \(S\), \(B\), or \(D\), or
2. extend the cost functional so that weight changes that matter for later selection are charged.

Route (1) is the pure derivation. Route (2) is an enrichment of cost. Both are examined.

---

## 1. Forced from cost: free epoch forbids share-breaking

**Lemma C1 (already T12).**  
In a free epoch, \(C_{\rm isolate}(E_i) > C_{\rm maintain}\) for all active paths. Any step that breaks a defining share of \(\mathcal{C}\) realizes isolation and incurs at least the isolation cost. By A3 that step is not selected while maintain remains cheaper.

**Corollary C1.1.**  
Free-epoch dynamics are share-topology-preserving: Foot is fixed. This is **forced** by A3 + D6–D9.

This is the only purely cost-forced half of R: maps that break Foot are forbidden in free epochs. It does **not** yet force invertibility or linearity of weight updates.

---

## 2. Gap for R: invertibility is not a cost fact

**Problem.**  
A map that sends \((a_1,a_2)\mapsto(a_1,0)\) without breaking any share has \(S=B=D=0\) under current definitions. Cost is zero; A3 does not forbid it. Yet the map is non-invertible and destroys the second path’s weight.

**Why cost is silent.**  
Weights are attributes of shares, not share identity. Zeroing a weight leaves the Share node in the term graph; Foot is unchanged; `eq` need not fail if the strategy does not inspect weights.

**Bridge principle B_R (weight support is structural content).**  
The support of the weight vector (which paths carry non-zero weight) is part of the residual’s structural identity. Changing support without removing Share nodes is observationally equivalent to isolation of zero-weight paths and must be charged as isolation (or as \(D=1\) under weight-sensitive `eq`).

**Lemma R1 (under B_R).**  
Free-epoch maps cannot send any active weight to zero (or change support). Combined with finite dimensionality and linearity (A4), admissible free-epoch linear maps have full support preservation. Among linear maps, support-preserving maps on \(\mathbb{C}^n\) that are continuous in a neighbourhood of the current weight (or defined as global linear maps on the active subspace) are invertible only if we further require surjectivity / non-collapse of dimension.

**Stronger B_R⁺.**  
Share-preserving linear reduce is a bijection on residual forms that leave Foot fixed: every such reduce has an inverse reduce that is also share-preserving. (Operational reading of “no structural loss.”)

**Lemma R2 (under B_R⁺).**  
Free-epoch linear weight maps lie in \(\mathrm{GL}(n,\mathbb{C})\). This is R★.

**Status.**  
C1 is forced. R★ requires B_R or B_R⁺ — a bridge that couples weight support (or residual bijectivity) to structural identity. Without B_R, cost alone does not forbid non-invertible weight maps.

---

## 3. Gap for N: relative moduli are invisible to cost

**Problem.**  
The map \((a_1,a_2)\mapsto(2a_1,\tfrac12 a_2)\) (after normalization, relative moduli change) can leave Foot, bindings, and binary `eq` unchanged. Then \(C=0\). A3 does not forbid it. Later Born reading changes, so selection-relevant content changed at zero cost.

**Why cost is silent.**  
\(S,B,D\) do not depend on \(|a_i|\).

**Bridge principle B_N (selection-relevant quantities are cost-bearing).**  
Any quantity that affects future `preferential_select` or `born_extract` outcomes is a dynamical degree of freedom that may only change when structural cost is charged. Relative moduli determine Born probabilities at later structural selection; therefore relative-modulus change requires \(C>0\).

**Alternative B_N′ (weight-extended cost).**  
Extend cost:
\[
C_{\rm ext} = \alpha S + \beta B + \gamma D + \delta\,\Delta\boldsymbol{\mu}
\]
with \(\delta>0\) and \(\Delta\boldsymbol{\mu}\) a measure of relative-modulus change (e.g. total variation on the simplex). Then A3 applied to \(C_{\rm ext}\) directly forbids free relative-modulus change in free epochs (where \(S=B=D=0\) still implies \(C_{\rm ext}=\delta\Delta\boldsymbol{\mu}\), minimized at \(\Delta\boldsymbol{\mu}=0\)).

**Lemma N1 (under B_N or B_N′).**  
Free-epoch maps preserve relative moduli. This is N★.

**Status.**  
N★ is **not** forced by bare \(S,B,D\). It is forced once selection-relevance of moduli is admitted into the cost currency (B_N) or cost is extended (B_N′).

---

## 4. What a pure-cost derivation would need

To derive R★ and N★ with no bridge principles, one would need theorems of the form:

1. Every change of weight support alters Foot, bindings, or `eq` (false under current definitions).
2. Every change of relative moduli alters Foot, bindings, or `eq` (false under current definitions).

Both are false because weights are orthogonal to the three counters. **Conclusion:** pure derivation from existing cost is impossible. The counters must be extended or weights must be declared structural in a way that makes support/moduli changes charge \(S\), \(B\), or \(D\).

---

## 5. Minimal cost extension that forces N★ (and aids R★)

**Definition D19 (weight-sensitive disruption).**  
For a step that updates weights from \(\mathbf{a}\) to \(\mathbf{a}'\) with Foot fixed:

- \(S_w = 0\) if support(\(\mathbf{a}'\)) = support(\(\mathbf{a}\)), else \(S_w \ge 1\) (treat support loss as share-equivalent isolation).
- \(M_w = \|\boldsymbol{\mu}'-\boldsymbol{\mu}\|_1\) (relative-modulus variation).

**Extended cost:**
\[
C^+ = \alpha S + \beta B + \gamma D + \alpha_w S_w + \delta M_w
\]
with \(\alpha_w,\delta > 0\).

**Theorem N from cost (under D19).**  
In a free epoch, Foot is fixed and isolation is not selected, so ordinary \(S=0\). Preferential select on \(C^+\) forces \(S_w=0\) and \(M_w=0\) whenever those terms can be avoided. Hence support and relative moduli are frozen. ☐

**Theorem R fragment from cost (under D19).**  
Support-freezing (\(S_w=0\)) rules out the simplest non-invertible maps (those that zero a coordinate). Full \(\mathrm{GL}(n)\) still needs linearity (A4) plus absence of non-surjective full-support linear maps as dynamical steps — e.g. require steps to be generated by flows (continuous invertible one-parameter groups), which yields invertible maps automatically.

**Flow completion B_flow.**  
Free-epoch weight updates are finite compositions of steps drawn from a continuous one-parameter group of Foot-preserving maps. Then invertibility is automatic (group property), and with N-from-cost one obtains unitaries after norm gauge.

---

## 6. Derivation scorecard

| Claim | From bare \(S,B,D\)? | From D19 extended cost? | Needs extra bridge? |
|-------|---------------------|-------------------------|---------------------|
| Free epoch preserves Foot | **Yes** (C1/T12) | Yes | No |
| Support of weights frozen | No | **Yes** (\(S_w\)) | or B_R |
| Relative moduli frozen (N★) | No | **Yes** (\(M_w\)) | or B_N |
| Invertibility (R★) | No | Partial (no zeroing) | B_R⁺ or B_flow |
| Unitarity (T13) | No | With D19 + B_flow + norm gauge | Yes |

---

## 7. Recommended commitment

**Adopt D19 (weight-sensitive disruption) as part of structural cost** when weights are present (A4 active).

Rationale:
- Keeps a single dynamical currency (cost).
- Makes N★ a theorem of preferential sequentialization under extended cost.
- Makes support-collapse cost-forbidden (partial R).
- Remaining gap to full R★ is only “free-epoch maps are invertible flows / group-like,” which is a mild dynamical regularity principle (B_flow), not an independent quantum axiom.

**Do not claim** R★/N★ from bare three-counter cost. That claim is false.

---

## 8. Updated status line

- **Forced from bare cost:** Foot preservation in free epochs (T12).
- **Forced from extended cost D19:** N★; support preservation.
- **Residual for full R★:** B_flow (or B_R⁺) — free-epoch maps invertible by construction as flows/group actions.
- **Unitarity:** free-epoch + D19 + B_flow + norm gauge → unitary on active subspace; structural projection remains sole non-unitary locus.

---

## 9. Next formal steps

1. Rewrite cost definitions in core ontology / theorems to include D19 when A4 is active.
2. Re-prove N★ and support preservation as corollaries of A3 + D19.
3. State B_flow explicitly as the remaining regularity axiom for full R★.
4. Update `sim/linear_reduce.py` cost accounting to charge \(M_w\) and \(S_w\) if non-unitary modulus/support changes are ever proposed outside free-epoch API.
