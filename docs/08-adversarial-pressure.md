# 08 — Adversarial Pressure Points

Response to the three pressures from the adversarial review.

---

## Pressure 1 — Compute structural inertia and isolation costs from actual expression trees

### Status: discharged at the formal and toy-executable level

**Operation: `m_struct_from_tree`**

Given a term built from `Var`, `Abs`, `App`, `Pair`, `Share`:

\[
m_{\rm struct}(E) = \alpha\,\lvert\{\text{distinct Share nodes in }E\}\rvert + \varepsilon
\]

with \(\varepsilon>0\) a floor. Share nodes are counted by object identity (true sharing, not syntactic duplication).

**Operation: `isolation_cost_from_tree`**

For path residual \(E_i\) against other members of a coherent set:

\[
\Sigma_i = \{\text{Share nodes of }E_i\text{ that also appear in some other member}\}
\]

\[
C_{\rm isolate}(E_i) = \alpha\,\lvert\Sigma_i\rvert + \beta\, B(\Sigma_i) + \gamma\, [\lvert\Sigma_i\rvert>0]
\]

where \(B(\Sigma_i)\) counts binding sites inside the contents of shares to be broken.

**Operation: `maintain_cost_from_tree`**

\[
C_{\rm maintain} = \alpha\,(\lvert\text{cross-member shares}\rvert + N_{\rm env}) + \beta\, B_{\rm cross}
\]

Executable realization: `sim/expr_tree.py`.

**Remaining gap**  
The sequential parameter \(x\) is still attached externally; a full derivation would obtain sequential labels from evaluator strategy over the tree, not only inertia from Share counts. That is the next structural debt.

---

## Pressure 2 — Derive phase / amplitudes from the reduced basis

### Status: not discharged — permanently marked as controlled enrichment

**Honest finding**

No derivation from `app`, `abs`, `pair`/`proj`, `eq`, `reduce`, `share` and structural counts \(S,B,D\) alone yields:

- a complex (or U(1)) phase on residuals, or
- additive amplitudes with a modulus-squared probability rule.

What pure structure supplies:

- which residuals remain co-dependent (`share_link`, `coherent_set`),
- when co-dependence is broken (`structural_decoherence`),
- binary structural visibility.

What it does not supply:

- continuous fringe visibility,
- relative phase accumulation,
- Born-rule weights.

**Decision**

`amplitude_weight`, `force_A`, `phase_accumulate`, and `born_extract` remain **controlled enrichments**. They are not claimed as theorems of the reduced core. The theory’s structural contribution stops at multi-path coexistence and isolation-cost decoherence. Interference phenomenology is hosted, not generated, until a future derivation appears.

**Operation boundary**

| Recovered from reduced core | Requires enrichment |
|-----------------------------|---------------------|
| `coherent_set`, `isolation_cost`, `maintain_cost` | `amplitude_weight` |
| `structural_decoherence` | `phase_accumulate` |
| `visibility_structural` (binary) | `visibility_amplitude`, `born_extract` |
| classical sequential calculus | |

---

## Pressure 3 — One quantitative prediction that can fail independently of tuning

### Prediction (parameter-free ratio)

**Statement**

Let \(E_A\) and \(E_B\) be two expression clusters that differ only in the number of distinct `Share` nodes (\(n_A\), \(n_B\)). Under identical constant structural bias \(b\), the continuum sequential calculus requires

\[
\frac{a_A}{a_B} = \frac{m_B}{m_A} = \frac{\alpha n_B + \varepsilon}{\alpha n_A + \varepsilon}.
\]

When \(\varepsilon \ll \alpha n_A, \alpha n_B\) (or when the same \(\alpha,\varepsilon\) apply to both),

\[
\frac{a_A}{a_B} \to \frac{n_B}{n_A}.
\]

**Why this is not tunable away**

- \(n_A\), \(n_B\) are read from the trees by `count_shares` / `m_struct_from_tree`.
- \(\alpha\) and \(\varepsilon\) cancel in the leading ratio (or affect both sides equally).
- The prediction fails if, once share counts are fixed by real term structure, measured sequential accelerations under a common bias do not track the inverse share-count ratio.

**Executable check**

`sim/expr_tree.py` builds clusters with prescribed Share counts and reports the required ratio. Coupling those trees to the velocity integrator of `sim/toy_simulator.py` (replacing the integer `share_density` knob with `m_struct_from_tree`) makes the prediction an end-to-end test inside pure theory.

**Empirical counterpart (future)**

Any laboratory or simulated system for which an independent estimate of “share density” (complexity / entanglement / shared-subexpression count) exists can confront the same inverse-acceleration relation. Failure of that relation, with share structure held fixed, falsifies the identification of structural inertia with share count under preferential sequentialization.

---

## Summary

| Pressure | Outcome |
|----------|---------|
| (1) Costs from real trees | Formal ops + executable `sim/expr_tree.py` |
| (2) Derive phase/amplitudes | **Cannot** from current core; marked enrichment |
| (3) Untunable quantitative prediction | Inverse share-count acceleration ratio |
