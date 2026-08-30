# 05 — Standard Model: Reexamination of the Classic Gaps

Authority: `docs/00-theory-charter.md`. Bridge formalism and postulates SB1–SB4: `docs/15-sm-bridge.md`. This document replaces the pre-rebuild version; its retracted claims are listed in §6.

## 1. Method and verdict vocabulary

Each gap gets a verdict from a fixed vocabulary, so no claim can hide in prose:

- **Native purchase** — existing machinery bears on the gap directly.
- **Reformulation** — the question changes shape here; no solution is claimed.
- **Research program** — a definable next step exists inside the framework.
- **Blocked (contention n)** — progress waits on a recorded contention (docs/07).
- **No purchase** — the framework currently has nothing to offer; saying so is required (charter §5).

## 2. Ontological contrast

| Aspect | Standard Model | This framework |
|---|---|---|
| Basic entities | Quantum fields on spacetime | Labeled expression structure under reduction (WM carrier) |
| Spacetime | Fundamental background | Causal order of reduction events (SB4, SM-B3); metric postulated in the TG layer (TG2), not derived |
| Particles | Field quanta | Minimal-rest-cost stable labeled excitations (SB3) |
| Forces | Local gauge interactions | Label-blind cost + label typing (SB1–SB2); continuous gauge home blocked (contention 1) |
| Measurement | Interpretation-dependent | Isolation/maintain cost criterion (T9–T11, F5) |

## 3. Gap-by-gap reexamination

### 3.1 Measurement problem — **native purchase + research program**

*The gap.* No dynamical account of outcome definiteness; the preferred-basis problem.

*Resources.* This is the framework's strongest suit, and it is genuinely structural:
- T9–T11 give a **criterion** for when definiteness occurs (isolation cost falls to or below maintain cost), and T14 locates all non-unitarity at that event.
- The **preferred basis** gets a structural answer: paths are share-linked residual classes, so the decomposition into alternatives is fixed by the tree, not chosen by an observer or a Hamiltonian's convenience.

*Caveats.* Born remains a reading (D12). The basis answer inherits the representation problem (why *this* tree decomposition of the world). Quantitative decoherence rates need tree-level environment modeling — currently an integer knob (docs/08 §1).

### 3.2 Quantum gravity / status of spacetime — **reformulation + research program**

*The gap.* Reconciling quantum dynamics with dynamical geometry; background independence.

*Resources.* Background independence is native (O2), and SM-B3 delivers causal-set structure by definition rather than postulate: events partially ordered by information flow. Qualitative causality (no influence outside the order) is free.

*Added since (docs/24, TG layer).* Given the geometric limit as a **postulate** (TG2), the Einstein equation follows by two independent routes (TH6), \(G\) is identified with the ground configuration's cut share density (TH7), and the inertia–geometry coupling — contention 2 — is **derived** (TH8). What the framework contributes on its own, without TG2, is sharper: the area law is the shape of WM2's own \(S\)-counter (TH2), horizon thermality's origin is F3 (TH3), and entropy monotonicity is the event trichotomy (TH4).

*Honesty.* The one thing that would make this a solution is exactly the thing still assumed. Dimension, metric and Lorentz invariance remain open; TG2 packages them into one postulate rather than solving any of them, and the reframed question ("which reduction statistics yield 3+1 locally-Lorentz order?") is still imported *unsolved* from causal-set theory (now docs/07 contention 9). Nothing here quantizes the metric. Verdict stays **reformulation + research program** — but the program is now specific: exhibit one order statistic with a finite share-per-area density, and a named block of results turns on.

### 3.3 Hierarchy / naturalness — **no purchase** *(previous claim retracted)*

*The gap.* The Higgs mass's quadratic sensitivity to UV scales in continuum QFT.

*Honesty.* The problem is a statement about QFT renormalization; the framework has no QFT limit, so the problem does not arise *here* — but that is dissolution-by-absence, which any non-QFT framework gets for free and which counts for nothing. Content would begin only if a continuum limit reproduced QFT and the light-scalar analogue provably stayed light. The pre-rebuild claim ("cost minimization dynamically disfavors high-cost fine-tunings") conflated parameter tuning with dynamical cost and is **retracted**.

### 3.4 Dark matter — **reformulation with a native mechanism**

*The gap.* Gravitating matter with no electromagnetic (and little other) coupling.

*Resources.* Under SB1/SB3, inertia-without-handle is *generic*, not exotic: stability requires only some conserved label; inertia (WM3) is label-blind; so any sector charged under a factor of \(G\) that mediates no interaction is stable, massive, and invisible to the interacting sectors. Executable demonstration: `sim/spectrum_toy.py` §3.

*Caveats.* "Gravitates but does not interact" is now *formalizable* (docs/24): gravitational coupling is to share count (TH8), which is label-blind, while interaction requires a label handle — so a dark sector gravitates with exactly the same universality as everything else, and this is a consequence rather than a stipulation. That is a coherence gain, not a prediction: still no abundance, distribution, or detection claims, and it inherits TG2. The mechanism explains why such sectors are *unsurprising*, nothing more.

### 3.5 Vacuum energy / cosmological constant — **reformulation** *(upgraded from no purchase; the 2026-08-08 retraction stands)*

*The gap.* Why vacuum energy does not gravitate at its naive QFT scale.

*Resources (docs/24).* Both routes to TH6 source curvature from **variations of relative entropy against the ground configuration**. The ground configuration's own cost is the reference and cancels identically, so "sum the vacuum modes' energy and gravitate it" is not a computation this framework performs — TH1 says so structurally (CI4's additive gauge: cost has no zero, so \(\langle K\rangle\) has no absolute value, only \(\Delta\langle K\rangle\)). \(\Lambda\) enters instead as a **constant of integration** in the Bianchi step.

*Honesty.* This dissolves the naive-scale question and answers nothing about the observed value: an integration constant is not a prediction, and no framework resource fixes it. "Why is \(\Lambda\) that size?" remains **no purchase**. The pre-rebuild phrase "opening room for dynamical suppression" stays **retracted** — what replaced it is a specific structural reason the naive computation is ill-posed, not a suppression mechanism.

### 3.6 Matter–antimatter asymmetry — **research program** *(unblocked by docs/17)*

*The gap.* Baryogenesis requires C and CP violation (Sakharov).

*Resources.* Charge conjugation \(q \to -q\) is native (SB1), and SB2's \(\Gamma\) makes the top-stratum law C-symmetric. With forced-violation states developed (docs/22), **all three Sakharov conditions have structural counterparts**: number violation ← FV events (progress failure of the conserving fragment); C/CP asymmetry ← conjugation-asymmetric *floor* tie-breaking at V-ties (the exact law stays exact — the bias lives in the Archimedean floor, where finite asymmetries are cheap); out-of-equilibrium ← FV states are jammed conserving flow by definition. Toy-demonstrated in `sim/forced_violation.py` (finite floor bias converts noise-level drift into deterministic drift). The weight-layer route via conjugation-asymmetric reconfiguration isometries (docs/17) remains a parallel locus.

*Verdict refinement:* mechanism **shape** with all three counterparts identified and toy-demonstrated; no rates or abundances. The realization question has been analyzed (docs/23): FV states are reachable in the raw calculus (PA2) and excluded exactly on the charge-relevant class (PA1) — so **whether baryogenesis-by-forced-violation occurs is a boundary-condition question** (is physical initial structure charge-relevant?), with the ground configuration's structure as the deciding probe.

### 3.7 Origin of gauge group and particle content — **research program** *(unblocked by docs/17)*

*Resources.* SB2 explains the *existence* of gauge redundancy — labels are description, invariants are physics — at the price of a postulate, and honestly locates where the *shape* of the group enters: the choice of the invariance subgroup \(\Gamma\) is data. Discrete symmetries live in WM. Continuous groups now have a definite home: the **isometries induced by reconfiguration events** (T15/T16, docs/17) — candidate gauge groups are stabilizers of the cost structure among induced maps, making gauge structure a property of *interactions*, as in physics.

*Honesty.* The specific group \(SU(3)\times SU(2)\times U(1)\) and its representation content: **no purchase**.

### 3.8 Three generations, masses, mixings — **no purchase; computational probe defined**

The one definable step: enumerate stable excitations of small labeled structures under families of cost landscapes and look for spectrum *multiplicities* (repeated states in one charge class at distinct rest costs — the generation-like signature). The method is demonstrated at toy scale in `sim/spectrum_toy.py`; nothing generation-like is claimed, and the two-phase toy result shows the answer is landscape-dependent, which is the difficulty in miniature.

### 3.9 Neutrino masses; strong CP — **no purchase**

Listed to keep the ledger complete (charter §5). No framework resource currently bears on either.

## 4. The success of Hilbert-space mathematics (relocated, restated)

Hilbert space is read as the effective description of the hosted linear layer (A4) in coherent regimes: superposition and interference are *hosted*; Born statistics enter as the D12 reading, not as consequences; entanglement corresponds to shared substructure. What the relocation buys is §3.1 — measurement gets a structural criterion — and, since docs/17, a clean event taxonomy: diagonal drift in free epochs, isometries at reconfigurations, non-isometry only at projection (T14′). The outstanding cost is constructive: exhibiting concrete rewrites whose induced maps realize the interactions of §§3.6–3.7.

## 5. Scorecard

| Gap | Verdict |
|---|---|
| Measurement problem | Native purchase + research program |
| Quantum gravity / spacetime | Reformulation + research program (TG layer, docs/24 — conditional on TG2) |
| Hierarchy / naturalness | No purchase (claim retracted) |
| Dark matter | Reformulation, native mechanism (gravitational universality now derived) |
| Vacuum energy | Reformulation: naive-scale question dissolved (docs/24 §5); observed value still no purchase |
| Matter–antimatter asymmetry | Research program (locus: reconfiguration isometries — docs/17) |
| Gauge group / particle content | Research program (locus: reconfiguration isometries — docs/17) |
| Three generations, masses, mixings | No purchase; probe defined |
| Neutrino masses; strong CP | No purchase |

## 6. Retractions from the pre-rebuild version

- "Superposition, interference, Born-rule statistics … arise naturally" → Born is the D12 reading (docs/11); interference is hosted, and its dynamical step is contended (docs/03 §3).
- "Cost minimization dynamically disfavors high-cost fine-tunings" → retracted (§3.3).
- "Vacuum energy … opening room for dynamical suppression" → retracted (§3.5).
- "Background independence is built-in" → kept, but downgraded to *order-only*: causal structure is native (SM-B3); geometry is not (§3.2).
- Vacuum \(V\), labels/charges, bounded signal \(c\) → reintroduced in charter-compliant form as SB3, SB1, and the qualitative causal bound of SB4 respectively (docs/15).
