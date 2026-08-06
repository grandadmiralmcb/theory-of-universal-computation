# 10 — Unitarity from Structural Projection

Attempt to derive constraints on free weight evolution from share-preserving dynamics and isolation-cost projection. Every step is named. Forced results are separated from remaining stipulations.

---

## 0. Setup

Active direction (`docs/03-quantum-sector.md`):

- Coherent set \(\mathcal{C} = \{E_i\}\) with share weights \(a_i \in \mathbb{C}\).
- **`linear_reduce`:** residual form \(\sum_i a_i E_i\) while isolation remains expensive.
- **`structural_decoherence`:** when \(C_{\rm isolate}(E_i) \le C_{\rm maintain}\), drop \(E_i\) from the combination.
- Real structural cost \(C = \alpha S + \beta B + \gamma D\).

**Definition (free epoch)**  
A time interval during which no path is dropped: isolation > maintain for all members of \(\mathcal{C}\). All share links in \(\mathcal{C}\) remain intact.

**Goal**  
Constrain the map

\[
U_\tau : (a_i) \mapsto (a_i')
\]

that updates weights over a free epoch of duration \(\tau\).

---

## 1. Share preservation forbids weight destruction

**Operation: `share_preserve`**

During a free epoch, by definition, no `share` node that participates in \(\mathcal{C}\) is broken. Structural cost of weight evolution cannot charge \(S\) for those links (they are not broken).

**Lemma 1 (no structural license for norm decrease via share-breaking)**  
Any update that reduces total weight mass by *breaking* share structure would incur positive \(S\) and therefore positive \(C\). Preferential sequentialization forbids such a step while cheaper share-preserving alternatives exist. In a free epoch those alternatives exist by definition (maintain is still cheaper than isolate). Therefore weight updates in a free epoch cannot be realized by share-breaking.

**What this forces:** free evolution is a **share-preserving** map on the weight vector. It does not act by discarding paths.

**What this does not force:** that the map preserves \(\sum |a_i|^2\). Share preservation alone allows rescaling, relative phase changes, or non-invertible linear maps that never break a share node.

---

## 2. Reversibility from undoing share-preserving reduce

**Operation: `linear_reduce_inverse_candidate`**

Suppose over a free epoch the only operations applied to the coherent set are share-preserving instances of `linear_reduce` (rearrangement of the weighted sum without breaking shares).

**Assumption R (reversibility of share-preserving linear reduce)**  
If a share-preserving linear reduction step is admissible, there exists a share-preserving step that undoes it (restores the prior weighted residual), because no structural information was destroyed — every share link and binding that existed before still exists.

**Lemma 2 (invertibility on the weight space of \(\mathcal{C}\))**  
Under Assumption R, the free-epoch map \(U_\tau\) is invertible on the span of active path weights. Non-invertible updates would amount to irreversible loss of weight configuration without share-breaking, contradicting the claim that share-preserving reduce destroys no structural content.

**Status of Assumption R:**  
It is a natural reading of “share-preserving = no structural loss,” but it is not a theorem of the real cost counts alone. It is the weakest extra principle needed to upgrade share preservation into invertibility. Marked as **semi-forced** (forced once “no structural loss” is read as operational reversibility).

---

## 3. Norm preservation from Born reading consistency

**Operation: `born_extract`** (at a later structural selection)

At the first post-epoch decoherence event,

\[
P(i) = \frac{|a_i|^2}{\sum_j |a_j|^2}.
\]

**Lemma 3 (norm is a pure gauge for Born reading)**  
Born probabilities depend only on the ray of the weight vector. Global rescaling \((a_i) \mapsto \lambda(a_i)\) does not change any \(P(i)\). Therefore structural selection does not by itself demand \(\|a\|=1\) during free evolution.

**However:** if free evolution could *differentially* rescale path weights (change relative moduli) without share-breaking, isolation costs would still be unchanged (isolation is about share topology, not weight moduli), while Born probabilities at later selection would be altered by a process that incurred no structural cost.

**Principle N (no free relative-modulus change)**  
A change in relative moduli \(|a_i|/|a_j|\) that is not accompanied by structural disruption (share break, binding change, or observational inequivalence) is an untethered alteration of future selection probabilities. Preferential sequentialization has no license for cost-free modification of quantities that control later `born_extract` outcomes, because that would be dynamical content without structural currency.

**Lemma 4 (relative moduli frozen in free epochs)**  
Under Principle N, free evolution may not change relative \(|a_i|\). Combined with global-rescaling gauge freedom for Born reading, one may fix

\[
\sum_i |a_i|^2 = \mathrm{const}
\]

throughout each free epoch (e.g. normalize once at the start of the epoch).

**Status of Principle N:**  
Interpretive but tightly tied to the theory’s own claim that structural cost is the sole dynamical currency. If weight moduli affected later selection yet could change at zero cost, the cost axiom would be incomplete. Marked as **semi-forced**.

---

## 4. Phase dynamics and inner-product preservation

**Operation: `phase_accumulate`**

With relative moduli fixed, free evolution reduces to relative phase motion:

\[
a_i(t+\tau) = a_i(t)\, e^{-i\varphi_i\tau}
\]

(or a joint unitary mixing of paths if share architecture permits coherent redistribution without isolation).

**Lemma 5 (norm-preserving phase maps are unitary on the active subspace)**  
Any invertible linear map on a finite-dimensional complex weight space that preserves \(\sum |a_i|^2\) is unitary (with respect to the standard Hermitian inner product). Therefore, under Lemmas 2 and 4, free-epoch evolution is unitary on the span of active paths.

**What forces full unitarity (not only diagonal phase):**  
If share architecture allows coherent redistribution among paths without breaking isolation (e.g. local linear_reduce rearrangements inside \(\mathcal{C}\)), the admissible maps are the full unitary group on that subspace, not only diagonal phase gates. If the architecture only permits path-local phase accumulation, evolution is unitary but diagonal in the path basis.

---

## 5. Structural projection as the non-unitary locus

**Operation: `structural_decoherence`**

When isolation ≤ maintain for some path, that path is dropped. The map on weight space is a (normalized) projection onto the surviving subspace — **not** unitary.

**Lemma 6 (unitarity holds only in free epochs)**  
Unitarity is the dynamics of share-preserving free evolution. Structural projection is the dynamics of isolation-cost selection. The theory therefore has the same bipartition as textbook QM: unitary free evolution punctuated by non-unitary selection events — with selection identified with structural decoherence rather than an extra collapse postulate.

---

## 6. Derivation summary (named pipeline)

1. **`share_preserve`** — free epoch ⇒ no share-breaking (Lemma 1).
2. **Assumption R** — share-preserving linear reduce is reversible ⇒ \(U_\tau\) invertible (Lemma 2).
3. **Principle N** — no cost-free change of relative moduli ⇒ relative \(|a_i|\) frozen; norm fixable (Lemmas 3–4).
4. Invertible + norm-preserving linear maps on \(\mathbb{C}^{|\mathcal{C}|}\) ⇒ **unitary** on the active subspace (Lemma 5).
5. **`structural_decoherence`** — non-unitary projection when isolation fails (Lemma 6).

---

## 7. Forced vs stipulated

| Result | Status |
|--------|--------|
| Free evolution does not act by share-breaking | **Forced** (definition of free epoch + cost preference) |
| Free evolution invertible on active weights | **Semi-forced** (Assumption R: no structural loss ⇒ reversible) |
| Relative moduli frozen in free epochs | **Semi-forced** (Principle N: cost is sole currency for selection-relevant quantities) |
| Free evolution unitary on active subspace | **Follows** from invertibility + norm preservation |
| Global phase / overall norm gauge | **Free** (Born reading is ray-dependent) |
| Diagonal vs full unitary mixing | **Architecture-dependent** (share connectivity) |
| Born rule \(P\propto\|a\|^2\) | **Still stipulated** as reading at selection |
| Concrete generator \(H\) or values of \(\varphi_i\) | **Open** (needs binding-geometry or action rule) |

---

## 8. Adversarial residual

The derivation does **not** obtain unitarity from real \(S,B,D\) alone. It obtains unitarity from:

- real structural projection (when unitarity *fails*), plus
- two semi-forced principles (R and N) that read “share-preserving / zero structural cost” as “reversible and selection-neutral on relative moduli.”

An adversary can reject R or N without rejecting isolation-cost decoherence. The gain is that unitarity is no longer an arbitrary external law: it is the unique linear weight dynamics compatible with share preservation, reversibility of non-destructive reduce, and cost as the sole currency of selection-relevant change. Structural projection remains the sole non-unitary mechanism.

---

## 9. Next pressures

1. Replace Assumption R with a formal invertibility theorem inside the term language.
2. Tie Principle N to an explicit prohibition in the cost calculus (relative-modulus change must charge \(C\)).
3. Derive a generator for \(\varphi_i\) (or a structural Hamiltonian) from binding / sequential history.
4. Executable free-epoch unitary evolution + structural projection in `sim/`.
