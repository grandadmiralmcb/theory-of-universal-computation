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
| Spacetime | Fundamental background | Causal order of reduction events (SB4, SM-B3); metric open |
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

*Honesty.* Everything geometric is open — dimension, metric, Lorentz invariance, the Einstein limit — and the inertia–geometry coupling is contention 2. The reframed question ("which reduction statistics yield 3+1 locally-Lorentz order?") is imported *unsolved* from causal-set theory. Reformulation, not progress, until one such statistic is exhibited.

### 3.3 Hierarchy / naturalness — **no purchase** *(previous claim retracted)*

*The gap.* The Higgs mass's quadratic sensitivity to UV scales in continuum QFT.

*Honesty.* The problem is a statement about QFT renormalization; the framework has no QFT limit, so the problem does not arise *here* — but that is dissolution-by-absence, which any non-QFT framework gets for free and which counts for nothing. Content would begin only if a continuum limit reproduced QFT and the light-scalar analogue provably stayed light. The pre-rebuild claim ("cost minimization dynamically disfavors high-cost fine-tunings") conflated parameter tuning with dynamical cost and is **retracted**.

### 3.4 Dark matter — **reformulation with a native mechanism**

*The gap.* Gravitating matter with no electromagnetic (and little other) coupling.

*Resources.* Under SB1/SB3, inertia-without-handle is *generic*, not exotic: stability requires only some conserved label; inertia (WM3) is label-blind; so any sector charged under a factor of \(G\) that mediates no interaction is stable, massive, and invisible to the interacting sectors. Executable demonstration: `sim/spectrum_toy.py` §3.

*Caveats.* "Gravitates but does not interact" cannot yet be formalized because gravitation itself is not (contention 2). No abundance, distribution, or detection predictions — the mechanism explains why such sectors are *unsurprising*, nothing more.

### 3.5 Vacuum energy / cosmological constant — **no purchase** *(previous claim retracted)*

*The gap.* Why vacuum energy does not gravitate at its naive QFT scale.

*Honesty.* Nothing gravitates in the framework yet. The ground configuration has a residual rest cost (SB3), but whether residual cost *sources* anything is a question for an unbuilt gravity sector. The pre-rebuild phrase "opening room for dynamical suppression" was content-free and is **retracted**.

### 3.6 Matter–antimatter asymmetry — **research program** *(unblocked by docs/17)*

*The gap.* Baryogenesis requires C and CP violation (Sakharov).

*Resources.* Charge conjugation \(q \to -q\) is native (SB1), and SB2's \(\Gamma\) makes the cost C-symmetric — so the framework states cleanly *what would have to break*: either drop conjugation from \(\Gamma\) (a conjugation-asymmetric cost term — a new postulate), or violate the CP-analogue in the weight layer. With contention 1 resolved (docs/17), the second option has a definite locus: the **induced isometries of reconfiguration events**. A CP-asymmetry is a conjugation-asymmetric rewrite whose induced map is not conjugation-covariant — a concrete structural object to look for, though none is exhibited.

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
| Quantum gravity / spacetime | Reformulation + research program |
| Hierarchy / naturalness | No purchase (claim retracted) |
| Dark matter | Reformulation, native mechanism |
| Vacuum energy | No purchase (claim retracted) |
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
