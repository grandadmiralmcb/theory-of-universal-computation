# 11 — Theorems (derivation-first hypotheses)

Authority: `docs/00-theory-charter.md`, `docs/14-derivation-from-ontology.md`.

Every theorem lists **full hypotheses**. Nothing is derived from O1–O4 alone beyond F1–F5 (see doc 14).

---

## Forced from ontology (Part I of doc 14)

| ID | Claim | Hypotheses |
|----|--------|------------|
| **F1** | Local sequential chains exist | O2 |
| **F2** | Minimal-disruption residual exists | O3 + finite non-empty admissible set + total preorder |
| **F3** | Unselected remains real | O4 |
| **F4** | Co-dependence admits disruption comparison | O1, O3 |
| **F5** | Structural projection when break ≤ maintain | F4, O3 |

---

## Working model (hypotheses always include WM1–WM2 as needed)

**T1** [WM1,WM2] Cost \(C\) well-defined on finite terms.  
**T2** [O3, F2, WM2] Preferential select attains min \(C\).  
**T9** [WM1,WM2] Isolation/maintain costs well-defined.  
**T10** [O3, T2, T9] If \(C_{\rm isolate}\le C_{\rm maintain}\), isolate. (Numeric form of F5.)  
**T11** [T10, WM4] Rising maintain cost \(\Rightarrow\) singleton \(\Rightarrow\) classical sequentialization. (WM4 supplies the environment→maintain-ledger asymmetry; without it, environmental shares could equally be charged to isolation, inverting the conclusion.)  
**T12** [T10, free epoch] Foot fixed in free epoch.

---

## Continuum idealization (add CI1–CI4, WM3)

**T3** [WM3,CI1,CI4] \(\delta v^*=-(b/m)\,\tau\) per tick. (WM2 does not supply the velocity-form cost; CI4 does — see docs/02 §2.)  
**T4** [T3] Discrete sequential updates \(v_{n+1}=v_n+\delta v^*\).  
**T5** [T4,CI2] \(\ddot x=-b/m\) in continuum limit.  
**T6** [T5,WM3] \(a_A/a_B=m_B/m_A\) under same constant \(b\).  
**T7** [T5] Projectile kinematics.  
**T8** [T5,CI3] \(m\ddot x=-V'(x)\).

---

## Hosted quantum (add A4, D19, B_flow; Born = D12)

**Q1** [WM2, D19-typing, A4] Operator totality: admissibility and cost are weight-blind, so epoch/event maps are single state-independent linear operators on the hosted span. (docs/19 §1)  
**T12+** [T12, A4, D19, O3] Support frozen in free epoch.  
**N★** [T12, A4, D19, O3] Relative moduli frozen — on D19's stated domain (Foot fixed); across reconfigurations (T15) the \(M_w\) comparison is undefined, so N★ constrains nothing there (docs/17 §3).  
**T13′** [A4, N★, norm gauge, Q1] Free-epoch maps are **diagonal unimodular** (phase drift); invertibility follows. **B_flow is not needed and is demoted to derived; R★ is a corollary, not a premise.** (docs/19 §2)  
**T15** [WM1, A4, O4, F5] Event trichotomy: free-epoch map | reconfiguration (decomposition changes, nothing dropped) | structural projection; mixed events factor. (docs/17 §2) *Scope: a classification of outcomes, not a dynamical theorem — it does not entail that type-2 rewrites occur or are preferred; occurrence is governed by structural cost and device structure (contention 7).*  
**T16′** [A4, D20, O4, T15, Q1] Reconfiguration maps are isometries (unitary at constant class count); injectivity — hence "no irreversible weight loss outside projection" — is a **corollary**, so the R-principle is demoted from hypothesis to consequence (docs/19 §3). "Determined by the rewrite" is concrete via the functor F on its domain (docs/18 §1; tags remain device data outside the symmetric case). Supersedes the T16a/T16b split.  
**L2–L5** [WM1, A4, D20, T16b] Splitter functor results: moduli forced by routing fractions; the symmetric 2→2 isometry filter pins the Hadamard up to diagonal gauge; Mach-Zehnder fringes \(\cos^2(\varphi/2)\) end to end; merges are never pure reconfigurations (no \(\mathbb{C}^2\to\mathbb{C}^1\) isometry). (docs/18 §2)  
**T14′** [T13′, T15, T16′, T10] Non-isometric weight change ⇔ structural projection. (Supersedes T14's earlier caveated form.)  
**T17** [T13′, T16′, Q1, WM2] Cost-decoupling: no admissible dynamics biases Born statistics toward structurally cheap outcomes — both weight-map types are functions of structure alone. Discharges docs/16 criterion C4; see contention 7 for its architectural bearing. (docs/19 §7)  
**L6** [A4, T15, CI1] Spreading lemma: an interaction-free cluster is a single class with a single weight — no internal position-weights exist to spread. Discharges docs/16 criterion C3. (docs/19 §6)  
**RM1** [M1/M2, PC, IND, CP, CC′ (floor clause), WM1] Hölder representation of the **dynamical floor**: the floor's disruption order embeds in \((\mathbb{R}_{\ge0},+)\) uniquely up to scale; with counter generation, \(C=\alpha S+\beta B+\gamma D\). WM2's form is derived, not stipulated. (Hypotheses restated per docs/20; currency clause reads CC′'s Archimedean floor since adoption.)  
**RM2** [CP, AD2-grounded] Dichotomy: the disruption order is Archimedean (⇒ \(\mathbb{R}\), Hölder, WM2 form) or stratified (⇒ Hahn lexicographic product; priority-ranked cost). CC selects the first branch; ¬CC is coherent. (docs/20 §5)  
**Q2** [O1–O4, M1/M2, PC, IND] Separation: the entire qualitative theory (F-layer with F2′, T2, T9–T12, T15, T13′/T16′/T14′/T17 given the weight postulates) needs neither CP nor CC; those two bits are needed exactly for RM1 and the quantitative classical chain T3–T8. (docs/20 §6)  
**F2′** [O3, well-foundedness] Minimal-disruption residuals exist under a well-founded (partial) preorder — F2's finiteness and totality hypotheses both weakened. (docs/19 §4)  
**TS1–TS4** [lex-argmin analysis; TS4 also ST1] Stratified-architecture results: CI4 ingredients must be co-stratal or classical dynamics degenerates (TS1); identity-flag-on-top freezes decoherence, losing T11 — observed classicality forces a one-currency dynamical floor (TS2); stratification is observable only as exact rules (TS3); conservation typing is the derived V=0 behavior of a top-stratum charge (TS4). **CC′ and ST1 adopted 2026-08-08 (owner decision)** — these are now theorems *of the theory's architecture*, not of a variant. (docs/21)  
**FV1** [ST1, CC′] Forced violations are realized from an initial class **iff** the conserving fragment fails progress there; under progress + preservation, SM-B1′ reduces to absolute conservation on-domain. (docs/22 §2)  
**FV2** [WM1 universality] Reachable V=0-stuckness is undecidable in general; FV-realization must be settled per rule-set. (docs/22 §3)  
**FV3** [ST1, CC′] At V-ties between conjugate violation channels the Archimedean floor decides; any finite conjugation-asymmetric floor bias yields systematic charge drift over FV ensembles, with the top-stratum law exactly symmetric. (docs/22 §5)  
**PA0** [WM1, SB1] Duplication is charge-safe: sharing is by reference, so contraction copies references, never shares — discards are the calculus's only violation channel. (docs/23 §1)  
**PA1** [WM1, SB1, ST1] Progress + preservation on the charge-relevant (λI-relativized) class: conservation absolute there. *Sketch level; mechanization open.* (docs/23 §3)  
**PA2** [WM1, SB1, ST1] FV states are **reachable** in the unrestricted calculus: \((\lambda f. f S)(\lambda x. c)\) reaches a state whose only redex discards the charged share, in one conserving step. Fully rigorous. (docs/23 §2)  
**PA3** [FV1, PA1, PA2] Relocation: forced-violation realization is a property of the **initial class** (boundary conditions), not of the dynamics. (docs/23 §4)  
**D12** Born reading — **not a theorem**.

---

## Structural bridge (add SB1–SB4; docs/15)

**SM-B1′** [WM1, SB1, ST1, CC′] Label sums are invariant along every selected reduction through states admitting a conserving continuation; in forced-violation states selection degrades to minimal violation (TS4). Conservation by *stratification* (ST1 adopted — charter §3), not typing fiat and still not Noether; the symmetry route from SB2 remains open. Supersedes SM-B1.  
**SM-B2** [WM1–WM3, SB1, SB3] The WM rest-cost spectrum per label class is discrete. (Artifact of integer counters; continuum-limit discreteness is open and is the physical question.)  
**SM-B3** [WM1, F1] Reduction-event dependence is a strict partial order (causal-set structure); each F1 chain is a total suborder. Metric, dimension, Lorentz: open.

---

## Non-theorems

Amplitudes from O1–O4; unitarity from bare \(C\); Born derived; finite trees as ontology; continuum Newton without CI; monism; consciousness identity; \(SU(3)\times SU(2)\times U(1)\) or generation structure from the bridge postulates SB1–SB4.

---

## Executable

T6: `sim/end_to_end_T6.py` — consistency check only: measured and predicted ratios derive from the same \(m\) (docs/08 §3)  
T9–T12 pattern: `sim/expr_tree.py`  
HQ free epoch / projection: `sim/linear_reduce.py` — unrunnable (SyntaxError) until 2026-08-08; "executable" claims for this file predating that date preceded any successful run  
SM-B1 / SM-B2 pattern: `sim/spectrum_toy.py` (conservation property test; two-phase toy spectrum; dark-sector stability)  
L2–L5 / T16b filter: `sim/splitter_rewrite.py` (induced map computed from routing; Hadamard pinned by the isometry filter; Mach-Zehnder fringes; negative cases)  
TS1–TS4: `sim/stratified_cost.py` (constraint-then-cost; classical degeneracy; decoherence freeze; typing as stratum with forced-violation degradation)  
FV1–FV3: `sim/forced_violation.py` (progress in open configurations; FV reachability under packing+clamps; minimal-step rule; asymmetry from floor tie-breaking)  
PA0–PA2: `sim/progress_analysis.py` (mini sharing calculus; charge-safe duplication; the reachable FV term; projection discards; reference subtlety; conservative relevance checker vs dynamic audit)
