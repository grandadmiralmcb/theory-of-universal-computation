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
| **F6** | No global order: events on no common chain are unordered — no global now, no privileged global state | O2, F1 |
| **F7** | Selection is non-destructive | O4 |
| **F8** | Accessibility is proper — no chain holds all real structure | F1, F2, O4 |
| **F9** | Preference is structurally determined (weak form; PC is stronger and needs SI) | O3, analytic |
| **F10** | Selection need not be unique; determinism is not forced | F2′ |
| **F11** | Order carries no orientation (was AT2) | O2 |
| **F12** | O3 is **silent** where residuals are incomparable — which is not the same as indifferent, and only a tie licenses a symmetry argument | O3, F2′, B3 |
| **F13** | Projection has no agent: sharing is symmetric, so system/observer is a chain-relative labelling and not an ontological fact | O1, F5, B4 |
| **F14** | Projection destroys its own precondition — F4's antecedent fails after F5, so O3 does not rank the inverse *as an inverse*. Permanent exclusion (AT4) is **not** thereby forced | F4, F5 |
| **F15** | Composition is not free — *or* parts are individuated by more than their own content and **B4** encodes the sharing. Either horn puts non-separability at O1; what is unavailable on both is self-contained parts | O1, B4 |
| **F16** | The disruption order ranks **transitions** and need not come from a function on states — **no state-valued quantity is forced** | O3 |
| **F17** | No forced termination and no forced monotone progress; F2′'s well-foundedness is per-step | O1–O4, F2′ |

*F6–F11 added by the audit's first pass, F12–F17 by its second (`docs/28`). Three of the first relocate load off postulates carrying it unnecessarily: F8 under TH3, F9 under T17, F11 out of the AT layer. One standing claim was **rejected** — "structure cannot cease" is forced given WM1 only (`docs/28` §8) — and one **corrected**: AT4's layer, below TG rather than forced (§10.3).*

*The second pass is mostly silences, and each one names the postulate standing in it: F12 → CP or a measure postulate (contention 4); F16 → WM2 and RM1, whose job it now is to **manufacture** the state functional O1–O4 do not supply; F17 → nothing, which is why the arrow had to come from F5's structure rather than from monotone descent. One recorded non-consequence: **O4 does not entail branching histories**, in either direction.*

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

## Thermodynamics & gravity (add TG1–TG5; docs/24)

**TH1** [RM1, CI4, WM1] Relativity of entropy: under \(k\)-fold granularity refinement the von Neumann entropy diverges as \(N\log k\) while \(S_{\rm rel}(\rho\Vert\sigma)\) against the SB3 ground configuration is exactly invariant; with RM1's scale gauge (entropy is a count, not a cost) and CI4's additive gauge (modular energy has no zero), **every thermodynamic quantity that does work in this layer is a difference against the ground configuration**. (docs/24 §1)  
**TH2** [WM1, WM2] Structural area law: \(C_{\rm isolate}\) is a function of the cut alone — \(\alpha N(\chi)+\beta B(\chi)+\gamma[N>0]\) — independent of interior structure. Holography is not added; it is the shape of the \(S\)-counter. **TH2′** [+TG1, D20] \(S(\chi)=s_0N(\chi)\).  
**TH3** [F1, F3/O4, SB4, SM-B3, A4] Horizon reduction: an evaluator whose accessible past is proper has a proper subalgebra and a generically mixed restricted state, with entropy TH2′ on the horizon cut. Thermality's *origin* is F3 (the unselected persists); only the KMS normalization is postulated (TG3).  
**TH4** [A4, D20, T15, T13′, T16′, T14′] Structural monotonicity: \(S_{\rm rel}(\Phi\rho\Vert\Phi\sigma)\le S_{\rm rel}(\rho\Vert\sigma)\), with equality on free epochs and reconfigurations and strict decrease possible only at structural projection. The framework's data-processing inequality; **entropy production and the measurement problem have one locus.**  
**TH5** [TG1, A4] First law of structural entanglement: \(S_{\rm rel}=\Delta\langle K\rangle-\Delta S\ge0\) with vanishing first variation, so \(\delta S=\delta\langle K\rangle\); under TG1, \(K=C_{\rm maintain}/\Theta+\)const — the modular Hamiltonian **is** the WM4 maintain ledger.  
**TH6** [TG1–TG4 (+TG5 for Route A), TH2′, TH3, TH5] Einstein equation \(G_{ab}+\Lambda g_{ab}=(2\pi/\eta)T_{ab}\), by two independent routes (Clausius flux; small-ball relative-entropy equilibrium) that agree. \(\Lambda\) is an integration constant, not a vacuum-energy sum.  
**TH7** [TH6] \(\eta=1/4G\), i.e. \(G=1/(4s_0\eta_N)\): Newton's constant is the reciprocal ground-configuration share density across a cut. Identification, **not** a computation of \(G\) — that needs TG2 solved.  
**TH8** [WM3, TH2, TH2′, TG1, TG2] Weak equivalence principle: the entropic bias is \(b_{\rm grav}=m_{\rm struct}\,g\), so \(g_{\rm eff}\) is cluster-independent — because inertia (WM3) and horizon entropy (TH2) count the **same shares**. **Closes contention 2** (previously an observational consistency requirement, docs/02 §6). **TH8-ε**: exact only to \(O(\varepsilon/\alpha_m n)\); WM3's floor predicts \(\eta_E\simeq(\varepsilon/\alpha_m)\,|n_1^{-1}-n_2^{-1}|\), a WEP violation growing for lighter bodies. **TH8′**: Eötvös bounds therefore constrain floor stratification (contention 8) independently of TS2.  
**TH9** [TH4, TH3, TG3, TG4] Generalized second law: \(S_{\rm gen}=\eta A+S_{\rm out}\) is non-decreasing along a horizon, by monotonicity under the shrinking exterior algebra. Not a postulate and not an ignorance story — it is TH4.  
**TH10** [TH9, SM-B3] **a**: area theorem \(\Delta A\ge0\). **b**: merger inequality \(A_f\ge A_1+A_2\), so a merged hole is necessarily bigger and fission is thermodynamically **forbidden**; for Schwarzschild, \(M_f\ge\sqrt{m_1^2+m_2^2}\) and \(f_{\rm rad}\le1-1/\sqrt2\approx29.3\%\) at equal masses. **c**: \(dM=T\,dS\) with \(T=\kappa/2\pi\), \(S=A/4G\).  
**TH12** [WM1, WM2, AD2] Additivity and its defect. **a**: for regions sharing nothing, cut counts and entropies add — this is **AD2**, already grounded (docs/20 §3), and is exactly what RM1's Hölder representation needs to make the cost cardinal rather than ordinal. **b**: otherwise the defect is the mutual information, \(I(A{:}B)=S_A+S_B-S_{AB}\le 2s_0N(A\!\leftrightarrow\!B)\), saturated at maximal correlation — a cross share is severed by two cuts and by no third, which is the whole source of the factor 2. **c**: universal additivity would force \(I\equiv0\), deleting co-dependence, F4, F5, coherent sets and the entire HQ layer — the framework *needs* additivity to fail exactly where sharing exists. **d**: area law and bulk extensivity are the two terms of \(S_{\rm gen}=\eta A+S_{\rm out}\), not rivals. **e**: TH10b = TH12a on disjoint components + TH9 monotonicity, so no counting identity crosses the merger. (docs/24 §2.1)
**TH11** [TH5] Bekenstein bound \(S-S_{\rm gnd}\le2\pi ER\), as the content of \(S_{\rm rel}\ge0\).

*Non-theorems of this layer:* the value of \(\eta_N\) (hence \(G\)); the value of \(\Lambda\); spacetime dimension; local Lorentz invariance; a quantum theory of the metric; the Page curve (docs/24 §8 defines a probe only).

---

## Time and the arrow (docs/25)

**AT1** [O2, F1, SM-B3] Sequential order is forced by O2 alone — no cost, no entropy, no state functional. **AT1′**: deriving *order* from an entropy gradient would therefore be circular here, since entropy is a functional of states and states are indexed by the chain. Order is prior and not emergent.  
**AT2** [SM-B3] A strict partial order's converse is a strict partial order and F1 is reversal-invariant, so order fixes **no orientation**. The gap is real and something must fill it.  
**AT3** [TH4, T13′, T16′, T14′, TH9] Orientation is carried by structural projection and by no other event type: isometric events preserve \(S_{\rm rel}\) and have admissible inverses (no orientation); projection is non-isometric and **non-injective**, so no admissible map runs it backwards. **The arrow of time, entropy production and structural projection are one event.**  
**AT4** [F5, O4/F3, SM-B3] The gradient *measures* the arrow; F5 **is** the arrow. Projection breaks the co-dependence linking unselected residuals to the chain, and causal exclusion is stable, so re-inclusion has no data-dependence path. \(\Delta S_{\rm gen}\ge0\) is the readout of a **sub-TG** ratchet — which puts the arrow **below** the TG stack, so it survives even if TG2 (contention 9) fails, and explains why the gradient never changes sign. **Corrected 2026-08-31 (`docs/28` §10.3):** this row said *forced-layer* ratchet. AT4 carries SM-B3, hence SB4's dependence relation and WM1's vocabulary, so it is sub-TG and not forced. The forced part is **F14**.  
**AT5** [T10, T11, WM4, AT3] The arrow's density equals decoherence density: sweeping environmental share pressure moves the oriented-tick fraction from ~0 (isolated, near-reversible) to ~1 (classical, saturated). Why the arrow is macroscopically ubiquitous and microscopically absent — T11 read in the temporal ledger.  
**AT6** [AT3, TH4, TH5] Flow and duration: the generator of time's flow is the maintain ledger (\(K=C_{\rm maintain}/\Theta\), the thermal-time reading); and since a record undoable by an admissible inverse certifies nothing, **measurable duration is counted by projection events**. An isometric clock's readings recur and certify no duration.

*Non-theorems of this layer:* the past hypothesis (relocated to the initial class exactly as PA3 relocated FV realization — a boundary-condition question); duration in physical units (needs decoherence rates, still the docs/08 §1 knob); global time (barred by O2); time dilation and simultaneity (need TG2); CPT as a derived symmetry.

---

## Mathematics from the minima (docs/27)

**MG1** [O1, O3, WM2, B5, B6] The cost structure is a metric. With \(d(A,B)\) the least total cost of a reduction path, \(d(A,A)=0\), \(d\ge0\) and the triangle inequality hold. These are exactly Lawvere's axioms for a metric space as a category enriched over \(([0,\infty],\ge,+)\); symmetry and separation are extra conditions rather than part of the definition, and symmetry fails precisely where reduction is one-way. **The framework has had a metric since O3 — on configuration space, not on physical space.**
**MG2′** [MG1, B7, symmetry] Curvature is definable **wherever the cost metric is symmetric**, with no manifold, chart or dimension, via Ollivier's coarse Ricci, relative to a chosen neighbourhood measure (B7), and agrees with the classical value wherever one exists (trees \(-1/3\) and \(-1/2\), flat lattices \(0\) in 2-D and 3-D, \(K_8\) at \(4/7\), all exact for \(\alpha=1/2\)). **The unrestricted MG2 was false**: where the metric is asymmetric the same edge returns two different values. Since the metric is symmetric exactly on the reversible sector (T13′, T16′) and asymmetric exactly at projection (AT3), **curvature is definable precisely where time has no direction**, and extending it across projection events is open.
**Consequence for contention 9.** Topology comes with the order, the metric with the cost and curvature with both. The geometric debt is therefore **manifoldlikeness** alone — locally Euclidean, with a dimension and a Lorentzian signature — and its precise form is whether the structure is a *Lorentzian length space*. Curvature does not fix dimension: flat 2-D and 3-D lattices both return exactly zero.

*Non-theorems of this layer:* that any generated structure is manifoldlike; that dimension is well defined away from hand-built lattices; that the signature is Lorentzian; that physical space appears inside configuration-space geometry.

---

## Non-theorems

Geometry, area, curvature or the Einstein equation without TG2–TG5; sequential order as emergent from entropy (AT1′); the past hypothesis; amplitudes from O1–O4; unitarity from bare \(C\); Born derived; finite trees as ontology; continuum Newton without CI; monism; consciousness identity; \(SU(3)\times SU(2)\times U(1)\) or generation structure from the bridge postulates SB1–SB4.

---

## Executable

T6: `sim/end_to_end_T6.py` — consistency check only: measured and predicted ratios derive from the same \(m\) (docs/08 §3)  
T9–T12 pattern: `sim/expr_tree.py`  
HQ free epoch / projection: `sim/linear_reduce.py` — unrunnable (SyntaxError) until 2026-08-08; "executable" claims for this file predating that date preceded any successful run  
SM-B1 / SM-B2 pattern: `sim/spectrum_toy.py` (conservation property test; two-phase toy spectrum; dark-sector stability)  
L2–L5 / T16b filter: `sim/splitter_rewrite.py` (induced map computed from routing; Hadamard pinned by the isometry filter; Mach-Zehnder fringes; negative cases)  
TS1–TS4: `sim/stratified_cost.py` (constraint-then-cost; classical degeneracy; decoherence freeze; typing as stratum with forced-violation degradation)  
FV1–FV3: `sim/forced_violation.py` (progress in open configurations; FV reachability under packing+clamps; minimal-step rule; asymmetry from floor tie-breaking)  
F6–F11 and the rejection: `sim/forced_layer.py` §§1–7 (all linearisations enumerated; the proper-subset count; the change-set identity; two minimal residuals and no minimum; an order and its converse both strict partial orders; and the countermodel reaching the empty structure)  
F12–F17 and the non-consequence: `sim/forced_layer.py` §§8–14 (a minimal set partitioned into one tied pair and five incomparable ones; the share link as an unordered pair; F4's antecedent before and after the projection, then re-established; the same two parts composed with and without sharing; the three-cycle whose potential constraints contain a cycle, so no state functional exists; twelve steps of a chain that is periodic; and two models of O1–O4 differing only in whether a chain runs along the unselected residual)  
MG1–MG2: `sim/metric_from_cost.py` (metric axioms verified, asymmetry exhibited on a one-way chain; Ollivier curvature by exact min-cost flow reproducing the analytic values; the two flat lattices returning zero, which is the numerical form of curvature not knowing its dimension)  
AT1–AT6: `sim/arrow_of_time.py` (isometric chains reversed exactly; projection's non-injectivity exhibited; exclusion stable over 200 steps; arrow density swept 0→99.8%; recurrent isometric clock vs monotone projection counter)  
TH1–TH12: `sim/thermo_gravity.py` (area law at fixed cut; relative-entropy gauge invariance against divergent \(S\); monotonicity across the event trichotomy; both small-ball coefficients verified against exact \(S^3\) balls and quadrature; \(dM=T\,dS\); the merger inequality on observed binary black holes; WEP universality and its \(\varepsilon\)-floor residue; additivity exact at zero cross-shares and off by exactly \(2n_{\rm cross}\) otherwise)  
PA0–PA2: `sim/progress_analysis.py` (mini sharing calculus; charge-safe duplication; the reachable FV term; projection discards; reference subtlety; conservative relevance checker vs dynamic audit)
