# 12 — Formalization of Assumptions R and N in the Term Language

Elevate R and N from interpretive principles to term-language constraints with checkable predicates.

---

## Assumption R — Reversibility of share-preserving linear reduce

### Informal statement
If a share-preserving linear reduction step is admissible, there exists a share-preserving step that undoes it.

### Term-language formalization

**D13 (Share footprint).**  
For a residual form \(R = \sum_i a_i E_i\) over coherent set \(\mathcal{C}\),
\[
\mathrm{Foot}(R) = \bigcup_{E_i\in\mathcal{C}} \{\text{Share nodes of }E_i\}
\]
(by object identity).

**D14 (Share-preserving map).**  
A weight update \(U: (a_i)\mapsto(a_i')\) is *share-preserving* iff it does not remove any element of \(\mathrm{Foot}(R)\) and does not break any share in that footprint (no change to share topology).

**D15 (Linear reduce step on weights).**  
A free-epoch step is a linear invertible map on the weight vector of active paths, leaving Foot fixed:
\[
\mathbf{a}' = M\mathbf{a}, \qquad M\in \mathrm{GL}(|\mathcal{C}|,\mathbb{C}), \quad \mathrm{Foot}\text{ unchanged}.
\]

**R (formal).**  
Every free-epoch weight update is of the form D15. Consequently \(M^{-1}\) exists and is itself a free-epoch (share-preserving) update. Operational reversibility is the existence of \(M^{-1}\) in \(\mathrm{GL}(n,\mathbb{C})\).

**Checkable predicate (`is_share_preserving`).**  
Given before/after Foot sets: Foot_after = Foot_before (same Share object identities). Given weight map matrix \(M\): \(\det M \neq 0\).

**Theorem R★.**  
If a free-epoch step satisfies D14 and is linear and invertible on weights (D15), then it is reversible by a free-epoch step.  
*Proof.* \(M^{-1}\) exists in \(\mathrm{GL}(n,\mathbb{C})\); applying it restores weights; Foot unchanged by construction of D14. ☐

R is now: free-epoch dynamics are restricted to D15. That restriction is a term-language typing constraint, not an external metaphysical reading.

---

## Principle N — No cost-free relative-modulus change

### Informal statement
Relative moduli \(|a_i|/|a_j|\) cannot change unless structural cost is charged.

### Term-language formalization

**D16 (Relative modulus vector).**  
For active weights \(\mathbf{a}\) with \(\|\mathbf{a}\|_2 > 0\),
\[
\mu_i = \frac{|a_i|}{\|\mathbf{a}\|_2}, \qquad \boldsymbol{\mu}\in S^{n-1}_{+}.
\]

**D17 (Modulus-changing step).**  
A weight update changes relative moduli if \(\boldsymbol{\mu}' \neq \boldsymbol{\mu}\).

**D18 (Structural charge for modulus change).**  
Any step with \(\boldsymbol{\mu}' \neq \boldsymbol{\mu}\) must either:
1. break at least one share in Foot (\(S \ge 1\)), or
2. alter open bindings (\(B \neq 0\)), or
3. fail observational equivalence (\(D = 1\)),
so that \(C = \alpha S + \beta B + \gamma D > 0\).

**N (formal).**  
In a free epoch (Foot fixed, no share break, maintain cheaper than isolate), D18 implies no admissible step may change \(\boldsymbol{\mu}\). Therefore free-epoch maps preserve relative moduli: they lie in the unitary group times global rescaling, and by ray-gauge (Born reading) we fix norm 1 and obtain unitary maps.

**Checkable predicate (`modulus_change_requires_cost`).**  
If \(\|\boldsymbol{\mu}' - \boldsymbol{\mu}\| > \epsilon\) then computed \(C\) of the step must be \(> 0\). In free-epoch simulation, any proposed non-unitary-modulus-changing update is rejected.

**Theorem N★.**  
Under N (formal) and free-epoch conditions, free-epoch weight maps preserve \(\boldsymbol{\mu}\). Combined with R★ (invertibility) and norm gauge, they are unitary.  
*Proof.* Relative moduli fixed \(\Rightarrow\) map is diagonal phase times global scale, or more generally an element of U(n) after norm fix, once invertibility and linearity are given (T13). ☐

---

## Combined consequence

**T13★ (unitarity, upgraded).**  
Free-epoch dynamics typed as D15 + N-constraint are unitary on the active subspace. Structural decoherence remains the only operation that may change relative moduli (by deleting coordinates) and is therefore the only non-unitary locus.

---

## Implementation hooks

| Predicate | Module |
|-----------|--------|
| `is_share_preserving(foot_before, foot_after)` | `sim/linear_reduce.py` |
| `is_invertible(M)` | `sim/linear_reduce.py` |
| `relative_moduli(a)` / `moduli_equal` | `sim/linear_reduce.py` |
| Free-epoch unitary step (phase / general U(n)) | `sim/linear_reduce.py` |
| Reject modulus change at zero cost | enforced in free-epoch API |
