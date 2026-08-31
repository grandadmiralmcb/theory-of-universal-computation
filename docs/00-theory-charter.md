# 00 — Theory Charter (derivation-first)

**Rule:** Claim only what is forced by stated ontological minima or by explicitly numbered postulates. Everything else is working model, idealization, or open.

Companion derivation spine: `docs/14-derivation-from-ontology.md`.

---

## 1. Ontological minima (O1–O4)

These are the only ontological commitments. They are **assumptions**, not theorems.

| ID | Statement |
|----|-----------|
| **O1** | There exists structured, evaluable information: patterns that admit composition, sharing of substructure, and reduction under strategies. |
| **O2** | Sequential order is not a global parameter of the structure; it is constructed locally by evaluators through successive reduction. |
| **O3** | When multiple admissible reductions are available, dynamics prefer those of lower structural disruption (disruption = change to sharing, binding, or observational identity). |
| **O4** | Structure not selected by a given sequentialization remains real; non-selection is not non-existence. |

**Preferred reading (not forced):** informational monism — unique non-idle reading of O1–O4. Not used as a premise in derivations.

---

## 2. What O1–O4 force (and what they do not)

### Forced (see `docs/14-derivation-from-ontology.md`)

- **F1** Local sequential trajectories exist as finite or transfinite chains of reductions (from O2).
- **F2** If the set of admissible one-step residuals is finite and non-empty and disruption is a total preorder, a minimal-disruption residual exists and is selectable (from O3).
- **F3** Unselected residuals persist as real structure alongside the selected trajectory (from O4).
- **F4** If co-dependence is realized by shared substructure, then breaking that sharing is a form of disruption; maintaining it is another; O3 compares them when both are admissible (from O1+O3).
- **F5** When breaking co-dependence is ranked no more disruptive than maintaining it, selection may isolate a residual (structural projection event) (from F4+O3).

### Not forced by O1–O4 alone

- Finite expression trees as the only carrier
- Integer cost formula \(C=\alpha S+\beta B+\gamma D\)
- Real sequential parameter \(x\), velocity, continuum ODEs
- \(m_{\rm struct} \propto\) share count (definitional in WM, not forced)
- Complex weights, linear residuals, unitarity, Born rule
- Consciousness, monism as theorem, spacetime, fields
- Metric geometry, area, curvature, the Einstein equation (TG2–TG5; docs/24)

---

## 3. Controlled extensions (explicit, not smuggled)

Each extension is a **postulate**, used only when stated in a theorem’s hypotheses.

| ID | Postulate | Role |
|----|-----------|------|
| **WM1** | Carrier is finite terms under `app`,`abs`,`pair`/`proj`,`eq`,`reduce`,`share` | Working model |
| **CP, CC′** | Disruption comparison is total (**CP**, ex-AD1). **CC′ (adopted 2026-08-08, owner decision — supersedes CC):** the cost structure is a Hahn form with finitely many **exact strata** above one **Archimedean dynamical floor**; RM1/WM2 describe the floor; TS1/TS2 (docs/21) show phenomenology demands exactly this shape. CP and the floor-Archimedean clause remain independent of O1–O4 (countermodels, docs/20 §§4–5); AD2 is derived (docs/20 §3) | The residual commitments of the classical quantitative chain (docs/20, docs/21) |
| **ST1** | **(Adopted 2026-08-08, owner decision.)** Conservation typing is a top stratum: label-violating rewrites carry a lexically dominant violation charge \(V\) rather than being inadmissible by fiat. Conservation behavior follows by TS4; in forced-violation states, selection degrades gracefully to minimal violation | Typing-as-stratum (docs/21 §5); supersedes SB1-typing's brute admissibility |
| **WM2** | Disruption measured by \(C=\alpha S+\beta B+\gamma D\) — **derivable via RM1** from AD1–AD3 + WM1 generation, unique up to positive scale (docs/19 §5) | Quantitative WM cost |
| **CI1** | Sequential labels include real \((x,v)\) | Continuum kinematics |
| **CI2** | Continuum limit of discrete ticks | ODE idealization |
| **CI3** | Smooth bias / potential \(b(x)\), \(V\) | Force law idealization |
| **WM3** | \(m_{\rm struct}=\alpha_m n_{\rm share}+\varepsilon\) (\(\alpha_m\) distinct from the WM2 counter weight \(\alpha\)) | Inertia proxy in WM |
| **WM4** | Environmental monitoring is charged to the maintain ledger only: environment-crossing shares raise \(C_{\rm maintain}\), not \(C_{\rm isolate}\) | Decoherence asymmetry (drives T11) |
| **CI4** | Sequential-state changes are charged the per-tick functional \(C_\tau(\delta v)=m_{\rm struct}(\delta v)^2/2\tau+b_{\rm struct}\,\delta v\); not an instance of WM2 (it is signed relative to the null change; the additive gauge \(b^2\tau/2m\) restores non-negativity without changing selection) | Velocity-form dynamics |
| **A4** | Share-linked residuals may form \(\sum a_i E_i\), \(a_i\in\mathbb{C}\) | Hosted linear layer |
| **D19** | Extended cost charges support collapse and relative-modulus change | Weight-sensitive cost |
| ~~**B_flow**~~ | ~~Free-epoch weight maps are invertible flows~~ **Demoted to derived** (docs/19 §2): T13′ obtains diagonal-unimodular free-epoch maps from A4 + D19 + norm gauge alone; invertibility is a consequence | Removed from the postulate roster |
| **D12** | Born reading \(P\propto\|a\|^2\) at projection | Probability reading |
| **D20** | Weight measures persisting structure: \(|a_i|^2\) is the measure of class \(i\)'s persisting residual structure. Supplies *meaning only* — the probability reading remains D12, non-derived | Weight semantics (postulate grade, same as A4; upgraded from explication per adversarial review — docs/18 §5) |
| **SB1** | Share nodes carry labels in a finitely generated abelian group \(G\); admissible reductions act by merge / split / pair-create / pair-annihilate (typing) | Charge structure (docs/15) |
| **SB2** | All cost functionals are invariant under a designated subgroup \(\Gamma \le \mathrm{Aut}(G)\); observables are \(\Gamma\)-invariants | Structural gauge principle |
| **SB3** | Particle = minimal-rest-cost stable excitation in its label class; ground configuration = minimal-cost \(Q=0\) | Spectrum definitions |
| **SB4** | Events = reduction steps, ordered by data dependence | Causal order (SM-B3) |
| **TG1** | Statistical coarse-graining: retaining only \(\Gamma\)-invariant macroscopic data induces the relative-entropy-minimizing (MaxEnt / Gibbs) measure \(p\propto\sigma e^{-C/\Theta}\) over compatible microstructures | Structural statistical mechanics (docs/24 §3). O3 gives an argmin, not an ensemble — TG1 is a genuine addition |
| **TG2** | Geometric limit: the SB4 event order coarse-grains to a Lorentzian \((M,g)\) in which the ground cut share count converges to \(\eta_N A\) | The entire geometric debt — the causal-set continuum problem, **imported unsolved**. Everything in docs/24 §§5–7 rests on it |
| **TG3** | Local modular flow: the accessible algebra's modular flow in the ground state is the boost generator, KMS-periodic at \(2\pi\) | Unruh relation \(T=\kappa/2\pi\); source of \(G\)'s normalization (docs/24 §3) |
| **TG4** | Modular energy is stress-energy: \(\delta\langle K\rangle = 2\pi\!\int T_{ab}\chi^a d\Sigma^b\), with \(\nabla^aT_{ab}=0\) | Source term for the field equation |
| **TG5** | Entanglement equilibrium: the ground configuration extremizes total entropy in a small ball at fixed volume | Route A only; Route B (Clausius) does not need it, and the two agreeing is the check on TG5 |

No theorem may treat these as forced by O1–O4.

---

## 4. Layers

1. **Ontology** — O1–O4 only.
2. **Forced corollaries** — F1–F5.
3. **Working model (WM)** — WM1–WM4; finite trees; executable tests.
4. **Continuum idealization (CI)** — CI1–CI4 on top of WM sequential calculus.
5. **Hosted quantum (HQ)** — A4, D19, B_flow, D12; structural projection (F5) as irreversible locus.
6. **Structural bridge (SB)** — SB1–SB4; SM-facing definitions and gap reexamination (docs/15, docs/05).
7. **Thermodynamics & gravity (TG)** — TG1–TG5 on top of WM+CI+HQ+SB; relative entropy as the only observable, the area law as WM2's own shape, and the Einstein equation as the resulting equation of state (docs/24).
8. **Time and the arrow (AT)** — no new postulates: order is forced (O2/F1/SM-B3), orientation is carried by F5 alone, and the entropy gradient is its readout (docs/25). Sits *below* the TG layer — the arrow does not depend on TG1–TG5.

---

## 5. Authority

`docs/14-derivation-from-ontology.md` is the derivation spine.  
`docs/11-theorems.md` must list hypotheses including every postulate used.  
Older text that claims amplitudes, unitarity, continuum Newton, or finite trees as forced by ontology alone is **void**.

---

## 6. Background assumptions (the B-ledger)

**Why this section exists.** §3 tracks the framework's *physics* postulates — WM, CI, HQ, SB, ST, TG. It has never tracked its *mathematical* ones. So sets, real numbers, infima, additivity along composition, choices of measure, and the logic of the metalanguage have all entered results without appearing in any hypothesis list. That is the reason a reader can follow every step of a derivation and still feel that more is being assumed than is being said: the ledger had no column for it.

These are not defects to be removed. Most are unavoidable. The requirement is only that they be **named and cited**, on the same terms as everything else.

| ID | Assumption | Where it bites |
|----|------------|----------------|
| **B1** | Structures form a set, or a class with well-defined hom-costs | Any claim about "the space of structures" — MG1, and the carrier question (docs/26 §7.1) |
| **B2** | The metalanguage is classical set theory | Every proof in the repository. Note the tension: docs/27 §2 suggests the *object* logic is naturally intuitionistic while every *proof about it* is classical |
| **B3** | **Admissibility is well defined.** O3 and F2 both quantify over "admissible reductions" and the notion is **used throughout and defined nowhere** | The selection principle itself. In WM1 it silently means "there is a redex", which is a carrier fact, not an ontological one |
| **B4** | **Identity of shared substructure.** What makes two holders hold *the same* thing rather than two alike things | O1's `share`, and therefore F4, F5, TH12 and the whole HQ layer. Currently supplied either by **SI**, which docs/20 §2 calls a reading, or by object identity in the carrier (docs/08 §1). **Neither is an axiom** |
| **B5** | Cost is additive along **sequential** composition | MG1. Distinct from AD2, which is additivity over **position-disjoint** events and does not imply it |
| **B6** | Infima over path sets exist | MG1 |
| **B7** | A choice of neighbourhood measure | MG2′ and any transport or curvature quantity. Ollivier curvature is defined only relative to such a choice; values are convention-dependent even where signs are not |
| **B8** | Reduction chains are countable | F1 permits transfinite chains; essentially every result assumes \(\omega\) |
| **B9** | **What an evaluator is.** O2 says order is constructed "by evaluators" and nothing says what one is. Two readings: an evaluator **is** a chain (deflationary), or it is a locus that *has* one (inflationary). The prose slides between them; F8 and TH3 are stated inflationally | O2 itself, and every result phrased in terms of an evaluator's access. **F13** says the ontology supplies no such locus, so the deflationary reading is the one the forced results need — and it is enough for all of them (`docs/28` §11) |
| **B10** | **Observational identity.** O3's own parenthetical defines disruption partly as change to "observational identity", which is undefined and, unlike sharing and binding, presupposes an observation | Inside the statement of the framework's only dynamical law. If it is chain-relative, the change-set is too and **F9 becomes conditional**; if absolute, it is a third ontological primitive with no charter line. Never chosen. **Contention 14** (`docs/28` §11) |

**Rule.** A theorem that uses a B-item names it in its hypothesis list, exactly as it names WM2 or TG2. Three are more than bookkeeping. An undefined admissibility relation sits underneath the only dynamical law (**B3**); an unaxiomatised identity criterion sits underneath the primitive that distinguishes this framework from a theory of bits (**B4**); and an undefined term sits inside O3's own parenthetical (**B10**). All three are recorded as contentions in `docs/07` — 12, 13 and 14. B10 was found last, by the second forced-layer pass, and where it was found is worth noting: this ledger was written to catch the framework's *mathematical* background, and the deepest gap it now holds is in the statement of an ontological minimum.

**What this does not fix.** Naming an assumption is not discharging it, and a long B-ledger is not a virtue. The list exists so that the honesty discipline of §§1–3 covers the mathematics as well as the physics, and so that "this feels less basic than it claims" becomes a checkable complaint rather than an impression.

