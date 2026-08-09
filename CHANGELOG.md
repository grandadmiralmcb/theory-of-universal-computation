# Changelog

## [2026-08-08] (forced-violation states developed)

- `docs/22-forced-violation.md` + `sim/forced_violation.py`: the question inherited from contention 8's closure — are forced-violation states physically realized? — pulled to its structure.
  - **Reframing (FV1):** FV realization is a **progress-theorem question** about the conserving (V=0) fragment — the exact question type theory asks of a calculus. Progress + preservation ⇒ absolute conservation on-domain; violations realized ⇔ progress fails. FV states are the "stuck terms" of the conserving calculus, and ST1 gives them dynamics instead of undefinedness.
  - **FV2:** the general question is undecidable (halting reduction); per-rule-set analysis required. The toy shows both outcomes are structurally cheap: open configurations provably have progress (200-tick runs, zero violations); packing + capacity clamps break it with a 3-cell example.
  - **Derived phenomenology:** minimal-step selection rule (forced violations take the smallest available charge step), locality of the violation event, and out-of-equilibrium **by construction** (an FV state is jammed conserving flow).
  - **FV3 + Sakharov counterparts:** all three baryogenesis conditions map structurally — number violation ← FV events; C/CP ← conjugation-asymmetric **floor** tie-breaking at V-ties (top-stratum law stays exactly symmetric; demo: +0.5 floor bias converts −32/2000 noise into −2000/2000 deterministic drift); out-of-equilibrium ← FV definition. Mechanism shape only; no rates.
  - docs/05 §3.6 verdict refined; successor open target recorded: progress analysis of the actual WM conserving fragment (docs/22 §6).

## [2026-08-08] (CC′ + ST1 adopted; contention 8 closed)

- **Owner decision:** CC′ (exact strata above one Archimedean dynamical floor) and ST1 (conservation typing as a lexically dominant violation charge) are adopted as charter postulates; CC is superseded; contention 8 is closed.
- Consequences applied:
  - **SM-B1 → SM-B1′** (docs/15, docs/11): conservation is *stratification-derived* and **conditional** — exact wherever a conserving continuation exists (which includes the entire working-model domain exhibited to date); in forced-violation states, selection degrades to minimal violation (TS4). Honesty note updated: better mechanism than typing fiat, still not Noether.
  - **RM1** reads CC′'s floor clause; the Hölder representation is a statement about the dynamical floor.
  - TS1–TS4 reclassified from variant results to theorems of the theory's architecture.
  - New open question inherited by the theory proper (docs/07 contention 8 closure note): are forced-violation states physically realized? The minimal-violation decay shape is the discriminating prediction.
  - `sim/spectrum_toy.py` docstring reframed (V=0 stratum, not typing fiat); README read-order extended with the docs/17–21 resolution chain.

## [2026-08-08] (stratified variant developed; contention 8 at a decision point)

- `docs/21-stratified-variant.md` + `sim/stratified_cost.py`: the ¬CC branch of RM2 built out.
  - Core observation: lexicographic cost factorizes selection into **constraint-then-cost** — a top stratum is an exact rule, the floor is a force.
  - **TS1**: splitting CI4's terms across strata degenerates classical dynamics (frozen or runaway) — Newton requires co-stratal ingredients.
  - **TS2**: identity-flag-on-top freezes decoherence at any environmental pressure — T11 lost; observed classicality **forces the dynamical floor to be one-currency** (first empirical constraint on contention 8).
  - **TS3**: stratification is observationally reachable only as exact rules — it cannot masquerade as a graded tendency.
  - **TS4 + ST1**: SB1-typing recovered as a top-stratum violation charge — conservation without admissibility fiat, plus graceful minimal-violation behavior in forced-violation situations that brute typing cannot express (a discriminating prediction-shape; speculative hook to Sakharov-style violation physics flagged as such).
  - Synthesis candidate **CC′**: exact strata above one Archimedean floor — both RM2 branches realized in different roles. Adoption of CC′+ST1 (which would close contention 8 at the price of one identification postulate) left to owner adjudication.
- Charter CC row, docs/07 contention 8, docs/11 (TS1–TS4 + executable), docs/15 (alternative conservation mechanism note) updated.

## [2026-08-08] (AD1–AD3 grounded to their floor)

- `docs/20-grounding-AD-axioms.md`: the order axioms beneath the classical chain are taken as deep as derivation permits.
  - **AD2 derived**: decomposed into M1/M2 (analytic to O3's "disruption = change"), PC (position covariance from O2 + structural individuation SI), and IND (independence of disjoint context, from O2's local selection + selection coherence SC) — with a counterexample showing the translation-invariance clause genuinely needed IND (rank \(x+y+xy\) is monotone but not additive).
  - **AD1 and AD3 proven independent of O1–O4** by countermodels (componentwise order on \(\mathbb{N}^k\); lexicographic order on \(\mathbb{N}^2\)) and sharpened to **CP** (universal comparability) and **CC** (common currency — tying down docs/01's own phrase).
  - **RM2 (dichotomy)**: under CP + grounded AD2, disruption is either Archimedean (Hölder ⇒ \(\mathbb{R}\), WM2's form) or stratified (Hahn ⇒ lexicographic product; priority-ranked cost) — there is no third shape; ¬CC is a coherent theory variant, recorded as contention 8.
  - **Q2 (separation)**: the entire qualitative theory needs neither CP nor CC; they are needed exactly for the cardinal representation and the quantitative classical chain. The classical sector's stipulation content is now **two bits**.
- Charter postulate table updated (AD row → CP/CC with grounding status); RM1 hypotheses restated; roadmap priority 5 discharged to its floor; contention 8 added.

## [2026-08-08] (tightening pass: fewer postulates, deeper roots)

- `docs/19-tightening-derivations.md`: seven results shrinking the postulate base and pushing stipulations down to more primitive axioms.
  - **Q1** (operator totality) named as the shared lemma licensing every "for all states" step — exposing exactly where weight-blindness is load-bearing.
  - **T13′**: free-epoch maps diagonal-unimodular from A4 + D19 + norm gauge alone — **B_flow demoted from postulate to derived** (HQ roster shrinks to A4, D19, D12, D20); R★ becomes a corollary.
  - **T16′**: the T16a/b split unified; isometry from [A4, D20, O4, T15, Q1]; injectivity a corollary — **the R-principle is no longer a hypothesis anywhere**. Contention 3 (R and N) resolved.
  - **F2′**: F2's finiteness *and* totality hypotheses weakened to a well-founded partial preorder at the ontological root.
  - **RM1**: WM2's linear cost form derived via Hölder representation from new order axioms **AD1–AD3** (total, disjoint-additive/cancellative, Archimedean) — the stipulation moves from a formula down to arguable order axioms, unique up to scale; N1 refined, not overturned.
  - **L6** (spreading lemma): an interaction-free cluster is one class with one weight — no internal position-weights exist to spread. docs/16 criterion C3 discharged.
  - **T17** (cost-decoupling): no admissible dynamics can bias Born statistics toward cheap outcomes — both weight-map types are functions of structure alone. docs/16 criterion C4 discharged, and contention 7 gains a standing "feature" argument.
- All four docs/16 criteria now discharged (C1 docs/17, C2 docs/18, C3/C4 docs/19). Charter, docs/07/10/11/12/14/16 updated accordingly.

## [2026-08-08] (splitter functor built; adversarial review of T15/T16 applied)

- `sim/splitter_rewrite.py` + `docs/18-splitter-functor.md`: the induced-map functor F exhibited at unit-share granularity. Moduli are **computed** from routing fractions (D20); enumerating all ±1 orientation tags for the symmetric 2→2 recombiner, exactly the odd-sign-flip half passes the T16b isometry filter and **every survivor is the Hadamard up to diagonal gauge** — the beam splitter is derived, not stipulated. Mach-Zehnder end to end: \(P(C)=\cos^2(\varphi/2)\), visibility 1, Monte Carlo agreement. Negative cases: merges admit no isometric map (always contain a projection component); non-channel-disjoint routings violate D20 and fall outside F's domain.
- Adversarial-review dispositions (docs/18 §5): **D20 upgraded to a named postulate** (charter §3, same grade as A4; supplies meaning, not probability — Born remains D12); **T15 rescoped** as a classification of outcomes, not a dynamical entailment; the **weight-blind selection seam** recorded as contention 7 (O3 never sees weights outside projection; device structure is external data); docs/17's "no new postulate" headline amended via addendum.
- docs/07: functor priority discharged at toy level; remaining debts stated (F on full WM terms; φ from binding geometry; spreading lemma).

## [2026-08-08] (contention 1 resolved by derivation)

- `docs/17-forced-resolution-contention-1.md`: the fork is resolved by entailment from prior commitments, not by preference. Decomposition co-motion is definitional (O1, O4, WM1); the **event trichotomy T15** (free-epoch map / reconfiguration / projection) is a theorem of case exhaustion; N★ never applied across reconfigurations because D19's \(M_w\) is typed on a fixed decomposition — its own stated hypothesis; reconfiguration maps are injective (**T16a**, forced) and isometric (**T16b**, forced given the **D20** explication — the one added sentence, flagged); **T14′**: non-isometry ⇔ projection. Horn (b) barred as unforced revision of an unrefuted commitment; Toolbox-A license lapsed with its named trigger discharged. Readout rules reconciled (interference sum = matrix element of the screen isometry, then Born).
- Applied across docs/01, 03, 05, 07, 11, 12, 13, 15, 16 and `sim/linear_reduce.py`: T13 no longer contended; contention 1 marked resolved; baryogenesis and continuous-gauge verdicts in docs/05 upgraded from "blocked" to "research program" with the concrete locus (reconfiguration isometries).
- Residue is construction, not choice: the induced-map functor / concrete splitter rewrite in `sim/` (docs/17 §7).

## [2026-08-08] (contention 1 fork review)

- `docs/16-contention-1-review.md`: full analysis of the N★/interference fork. Key reframing: QM itself is phases-only in the co-rotating eigenbasis, so the contention is about **basis rigidity**, not phase-onlyness. Horn taxonomy extended beyond the recorded (a)/(b) with (c1) co-moving decomposition (folds into (a)), (c2) Toolbox-A path integral (now formally licensed by the Toolbox usage rule, since contention 1 is its named trigger), and (c3) instrumentalist retreat (rejected — fails the two-slit test). Partial formal results stated: induced-map isometry target (L0) and swap-symmetry one-parameter family (L1, with the balanced-splitter \(\theta\)-pinning residue). Wave-packet spreading objection assessed as likely dissolving under (a) (one class, no position-weights, absent environmental shares). Recommendation: pursue (a), fallback (c2), (b) dominated; decision criteria C1–C4 recorded. Analysis only — no theory content changed.

## [2026-08-08] (Standard-Model bridge)

- New postulate family **SB1–SB4** (labels + typing, structural gauge principle with designated invariance subgroup \(\Gamma\), particle/vacuum definitions, causal order from reduction dependence) — `docs/15-sm-bridge.md`; charter table and layer list updated.
- Theorems **SM-B1** (conservation by typing — explicitly *not* Noether), **SM-B2** (WM spectrum discreteness, flagged as an integer-counter artifact), **SM-B3** (causal-set structure of reduction events) added to `docs/11-theorems.md` with full hypotheses.
- `docs/05-standard-model.md` rewritten charter-aligned: gap-by-gap reexamination with a fixed verdict vocabulary (native purchase / reformulation / research program / blocked / no purchase). Measurement identified as the strongest native purchase (structural definiteness criterion + structural preferred basis); dark matter as a native mechanism (conserved label + label-blind inertia); baryogenesis and continuous gauge groups recorded as blocked behind contention 1; hierarchy and vacuum-energy claims from the pre-rebuild version explicitly retracted.
- Pre-rebuild orphans rehabilitated in charter-compliant form: vacuum \(V\) → SB3 ground configuration; labels/charges → SB1; bounded signal \(c\) → qualitative causal bound of SB4 (quantitative speed needs a metric, open).
- `sim/spectrum_toy.py`: SM-B1 conservation property test (admissible moves conserve charge; an inadmissible deletion breaks it), two-phase toy spectrum (unit-share phase vs clumped phase with emergent charge quantum \(\approx\sqrt{\alpha_m/\lambda}\)), dark-sector stability demonstration.

## [2026-08-08] (adversarial review fixes)

- `sim/linear_reduce.py`: fixed the SyntaxError that had made the file unrunnable since it was committed — every earlier "executable HQ confirmation" citing it predated any successful run. The general-matrix step now rejects norm-changing proposals and warns on modulus-changing ones instead of silently rescaling; the demo exercises a Hadamard to display contention 1.
- Classical chain repaired: per-tick velocity cost **CI4** \(C_\tau(\delta v)=m(\delta v)^2/2\tau+b\,\delta v\) added as an explicit postulate (charter §3); T3 restated as \(\delta v^*=-(b/m)\tau\); the silent increment→rate reinterpretation in docs/02 §3–4 and the sims removed; T3–T8 hypothesis lists corrected.
- **WM4** (environment charged to the maintain ledger only) named as the postulate driving T11.
- N★ scope corrected: the D19+A3 argument confines free epochs to diagonal phase drift; T13 restated (diagonal unitary; general unitarity contended); beam-splitter/recombination cost locus recorded as contention 1 in docs/07.
- Equivalence-principle scope added: gravitational bias must satisfy \(b_{\rm grav}=m_{\rm struct}\,g\); the T6 ratio applies to cluster-independent (applied-force) biases only (docs/02 §6, docs/08 §3).
- T6 executable relabeled a consistency check (prediction and measurement derive from the same \(m\)); independent test requires an external share-count operationalization.
- D13–D17 written out in docs/12 (previously referenced but never defined).
- \(\alpha_m\) (WM3 inertia coefficient) disambiguated from the WM2 counter weight \(\alpha\); dead `gamma` parameter removed from `maintain_cost_from_tree`.
- docs/05 and docs/06 marked pre-rebuild/superseded with void-content banners; AGENTS.md synced with the actual repository (docs 00–14, `sim/` exists and must stay runnable).

## [2026-08-06] (derivation-first ontology rebuild)

### Foundation
- Ontological minima **O1–O4** only as assumptions.
- **F1–F5** derived from O1–O4 (with finiteness regularity for F2).
- Explicit **non-forced** ledger and negative results N1–N3.
- All further structure via numbered postulates (WM, CI, HQ).
- `docs/14-derivation-from-ontology.md` is the derivation spine.
- Charter and theorems rescoped: no claim of amplitudes/unitarity/continuum/Born from ontology alone.

## [2026-08-06] (earlier)

- Charter (trees demoted); theorems WM/CI/HQ tags; D19; T6 end-to-end; linear_reduce; etc.
