# 15 — Structural Bridge to Standard-Model Physics (SB layer)

Authority: `docs/00-theory-charter.md`. Everything here is postulational (the **SB** family) or definitional; **nothing in this document is forced by O1–O4**. Companion reexamination of the SM's open problems: `docs/05-standard-model.md`. Theorems with hypotheses: `docs/11-theorems.md`. Executable demonstrations: `sim/spectrum_toy.py`.

**Method rule.** For each SM-facing structure: (i) name the postulate that buys it, (ii) prove what is provable in WM, (iii) mark continuum/HQ dependence, (iv) say plainly where a bridge element sits behind a recorded contention (docs/07).

---

## 0. Information-theoretic reading (orientation, not derivation)

The bridge treats three SM-facing structures as three faces of information:

| Physics face | Information face | Where it lives below |
|---|---|---|
| Conserved charges | Typed information that admissible dynamics cannot delete | SB1 + SM-B1 |
| Gauge symmetry | Redundancy of description: labels are coordinates, invariants are physics | SB2 |
| Causal structure | The partial order of information flow between reduction events | SB4 + SM-B3 |

These readings motivate the postulates; they do not prove them.

---

## 1. SB1 — Labels (charge structure)

**Postulate SB1.** Each `Share` node carries a label \(q\) in a finitely generated abelian group \(G = \mathbb{Z}^k \times F\) (\(F\) finite). The **cluster charge** is \(Q(E) = \sum q_i\) over distinct Share nodes. Independent charge sectors are factors of \(G\).

**SB1-typing (admissible label dynamics).** Reductions act on labeled shares only by:
- **merge**: \((q_1), (q_2) \to (q_1+q_2)\)
- **split**: \((q) \to (q_1), (q_2)\) with \(q_1+q_2=q\)
- **pair creation**: \(\varnothing \to (q), (-q)\)
- **pair annihilation**: \((q), (-q) \to \varnothing\)

Unlabeled structure is unrestricted. Deletion of a share with \(q \neq 0\) is inadmissible; shares with \(q=0\) in every sector may be created or removed freely.

**Theorem SM-B1 (conservation by typing).** [WM1, SB1, SB1-typing] \(Q(E)\) is invariant under every admissible reduction sequence.
*Proof.* Each typing clause preserves the label sum; induction on the sequence. ∎

**Honesty.** Conservation here is *enforced* (a typing discipline, in the linear-logic tradition), not *derived* from a symmetry. A Noether-style route — obtaining SM-B1 from SB2 invariance plus the selection principle A3 — is **open**, and its existence is not obvious: SB2 constrains description, A3 constrains selection, and neither obviously yields additivity along histories. Do not cite SM-B1 as "Noether recovered."

**Status note.** SB1 reintroduces the pre-rebuild "labels/charges" in charter-compliant form. Non-abelian labels / representation categories are a strict extension (Toolbox E territory, docs/09), not assumed.

---

## 2. SB2 — Structural gauge principle

**Postulate SB2.** Fix a designated subgroup \(\Gamma \le \mathrm{Aut}(G)\). Every cost functional of the theory (\(C\), \(C^+\), isolation/maintain, CI4, and any SB3 rest-cost terms) is invariant under uniform relabeling by any \(\varphi \in \Gamma\). Observables are \(\Gamma\)-invariants.

**Why \(\Gamma\), not all of \(\mathrm{Aut}(G)\).** Full \(\mathrm{Aut}(\mathbb{Z}^k)=\mathrm{GL}(k,\mathbb{Z})\) does not preserve quadratic label terms (a shear changes \(\sum q_i^2\)), so a cost with label tension cannot be invariant under all automorphisms. The invariance subgroup \(\Gamma\) is **data** — this is exactly where the *shape* of a gauge group enters the framework, and it is chosen, not derived. In the toy of §4, \(\Gamma = \{\pm 1\} \times \{\pm 1\}\): charge conjugation per sector.

**What SB2 buys and what it does not:**
- It gives gauge redundancy a natural home: "why is there gauge symmetry?" reframes as "why is dynamics label-blind?" — which SB2 answers *by postulate*, no better.
- Conjugation \(q \to -q\) in \(\Gamma\) makes cost C-symmetric; a matter–antimatter asymmetry would require breaking exactly this (docs/05 §3.6).
- In WM, available symmetry groups are **discrete**. Continuous gauge groups have exactly one candidate home: the A4 weight layer — the stabilizer of the extended cost structure inside \(U(n)\) acting on share-linked residuals. That construction is **blocked behind contention 1** (which free-epoch maps exist at all is the contended question). \(SU(3)\times SU(2)\times U(1)\) is *not derived*; at best the framework locates where it would have to live.
- **Local** gauge transformations (per-region relabeling) require a locality notion on the structure (SB4 adjacency) plus a compatibility condition along shares — the connection analogue. Formulating it is open.

---

## 3. SB3 — Particles, vacuum, spectrum

**Definitions.** [WM1–WM3, SB1]
- **Ground configuration** (sector vacuum): a minimal-rest-cost configuration with \(Q = 0\). (Charter-compliant reintroduction of the pre-rebuild "vacuum \(V\).")
- **Rest cost**: \(m_{\rm struct}\) extended by label terms, e.g. \(\alpha_m n_{\rm share} + \lambda \sum_i \lVert q_i \rVert^2 + \varepsilon\) (the specific tension form is toy data, not theory).
- **Stable**: no admissible reduction lowers rest cost (charge preservation is automatic by SM-B1).
- **Particle**: a minimal-rest-cost stable excitation in its charge class. Its rest cost is the mass proxy.

**Theorem SM-B2 (WM spectrum discreteness).** [WM1–WM3, SB1, SB3] The set of particle rest costs is discrete.
*Proof.* Rational-coefficient counters on finite terms take values in a discrete set. ∎

**Honesty.** Discreteness is an **artifact of integer counters** — any counting cost is trivially discrete. The physically relevant question is whether a continuum idealization preserves gaps; that is open.

**Two-phase toy landscape** (executable, `sim/spectrum_toy.py`): with per-share cost \(\alpha_m\) and tension \(\lambda q^2\), the minimal excitation of charge \(Q\) is \(Q\) unit shares when \(\lambda > \alpha_m/2\), giving the exact linear spectrum \(m(Q) = (\alpha_m+\lambda)Q + \varepsilon\). When \(\lambda < \alpha_m/2\) the optimum *clumps*: shares carry a characteristic charge \(\approx \sqrt{\alpha_m/\lambda}\) (balancing per-unit-charge share cost against tension), with a single merged share only at small \(Q\) and an asymptotically linear spectrum of slope \(2\sqrt{\alpha_m\lambda}\). The spectrum's shape — including an emergent preferred charge quantum — is a property of the cost landscape. This demonstrates the *mechanism* (discrete stable excitations selected by cost within charge classes) and predicts no SM value.

**Dark sectors are generic.** A cluster neutral in every "interacting" factor of \(G\) but charged in another conserved factor is stable (SM-B1 protects it) and has inertia (WM3 is label-blind), with no label-mediated handle. What this does and does not buy: docs/05 §3.4.

---

## 4. SB4 — Causal order from reduction dependence

**Postulate SB4 (with a built-in definition).** Physical events are reduction steps. For events \(e, e'\): \(e \prec_1 e'\) iff the redex of \(e'\) contains a node created by \(e\); \(\prec\) is the transitive closure. The physically meaningful "spacetime substitute" of the working model is the event set with \(\prec\) — nothing finer.

**Theorem SM-B3 (causal-set structure).** [WM1, F1] \(\prec\) is a strict partial order on events, and each evaluator's F1 chain is a total suborder (its proper-time analogue).
*Proof sketch.* Fix any interleaving realizing the history; creation precedes consumption in it, so \(\prec_1\) is acyclic; and \(\prec\) depends only on the local chains and share links, not on the interleaving (trace-equivalence of independent steps, per Lemma-3.4-style commutation). ∎

**What this buys:**
- Background independence is native (O2: order constructed, not assumed) and lands the framework in causal-set territory (Bombelli–Lee–Meyer–Sorkin) by *definition*, not extra machinery.
- Qualitative causality is native: a reduction can be influenced only by structure it consumes, so no influence propagates outside \(\prec\). This partially rehabilitates the orphaned pre-rebuild "bounded signal \(c\)": the *existence* of a causal bound is structural; a *quantitative* maximum speed needs a metric, which does not exist yet.

**What it does not buy:** dimension, metric, Lorentz invariance, Einstein-equation limit, and the coupling of inertia to geometry (contention 2). The hard problem imported unsolved from causal-set theory — which order statistics yield 3+1-dimensional, locally Lorentz-invariant behavior — is inherited intact.

---

## 5. Non-purchases (fixed ledger)

The bridge, as it stands, has **no resources** for: the specific group \(SU(3)\times SU(2)\times U(1)\) or its representations; three generations; Yukawa/mixing textures; neutrino masses; strong CP; coupling-constant values. Listing these as open is mandatory; claiming resources for them without new postulates is void under charter §5.

---

## 6. Dependency map

```
SB1 (labels) ──> SM-B1 conservation (with SB1-typing)     [proved, WM]
SB1+SB3      ──> SM-B2 discrete WM spectrum               [proved, flagged artifact]
SB2 (Γ-invariance) ──> gauge redundancy; C-symmetry       [postulate]
SB2 + A4     ──> continuous gauge candidate (U(n) stabilizer)  [BLOCKED: contention 1]
SB4 + F1     ──> SM-B3 causal order                       [proved, WM]
SB4 + metric(?) ──> spacetime, Lorentz, gravity           [open; contention 2 adjacent]
```
