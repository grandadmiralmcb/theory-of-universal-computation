# 25 — Time and the Arrow (AT results)

*Status: derivation document. Claim under examination: **time is emergent from the entropy gradient**. Verdict: **half right, and the half that is right is a theorem the framework already owned.** Sequential order is forced by O2 with no entropy anywhere (AT1) — deriving it from an entropy gradient would be circular. What order does not supply is **orientation**: a strict partial order and its converse are both strict partial orders (AT2). The entropy gradient supplies exactly that missing half, and by TH4 it is carried by structural projection events and by nothing else (AT3). Sharper still: the gradient **measures** the arrow rather than creating it — the ratchet is F5 plus stable causal exclusion, one layer below the postulational TG stack (AT4). Executable: `sim/arrow_of_time.py`.*

Authority: `docs/00-theory-charter.md`. Thermodynamic layer: `docs/24-thermodynamics-gravity.md`. Theorems with hypotheses: `docs/11-theorems.md`.

---

## 0. Three things called "time"

The claim is ambiguous until these are separated, and once separated it resolves cleanly.

| Notion | What it is | Status here |
|---|---|---|
| **Order** | which events precede which | **Forced** from O2 (F1 chains, SM-B3 partial order). Prior to entropy. **Not emergent** |
| **Orientation** | which end of the chain is the past | **Not** fixed by order. Supplied by the entropy gradient — **emergent, exactly as claimed** (AT3), with its root in F5 (AT4) |
| **Flow / duration** | rate, elapsed amount, what a clock reads | Modular flow of the state (TG3); measurable duration counted by projection events — **emergent and state-dependent** (AT6) |

The one-sentence version: **the framework builds time's *order* from reduction and time's *direction* from entropy, and it needs both because neither gives the other.**

---

## 1. AT1 — Order is prior, and could not be otherwise

**Theorem AT1.** [O2, F1, SM-B3] The reduction-event partial order \(\prec\) and each evaluator's F1 chain exist given O2 alone — no cost, no cardinal structure, no entropy, no postulate beyond the ontological minima.

*Proof.* F1 (docs/14): O2 says sequential order is constructed by successive reduction; the construction yields a chain. SM-B3: dependence is a strict partial order on events. Neither derivation mentions WM2, TG1 or any state functional. ∎

**Corollary AT1′ (the circularity bar).** Entropy in this framework is a functional of states (TH1: \(S_{\rm rel}(\rho\Vert\sigma)\)), and states are indexed by position along a chain. So an account deriving *order* from an entropy gradient would define the gradient using the order it purports to construct. **Order cannot be emergent from entropy here.** Any reading of "time is emergent from the entropy gradient" that targets order is barred — not by preference, but by the dependency structure.

This is not a limitation; it is the framework's distinctive position. O2 already refused a global time parameter, and background independence (docs/05 §3.2) is native precisely because order is *constructed*, not derived from a state functional.

---

## 2. AT2 — But order carries no orientation

**Theorem AT2.** [SM-B3] The converse relation \(\succ\) of a strict partial order is a strict partial order, and F1's chain condition is invariant under reversal. Hence \(\prec\) alone does not determine which end of a chain is the past.

*Proof.* Irreflexivity and transitivity are preserved under converse; a total suborder reversed is a total suborder. ∎

So the framework's temporal primitive fixes *adjacency and precedence structure* while leaving *direction* completely open. Something else must orient it. **This is the gap the claim correctly identifies.**

Executable (`sim/arrow_of_time.py` §1): a chain of four free-epoch and reconfiguration events leaves \(S_{\rm rel}\) invariant to ten decimals at every step, every step has an admissible inverse (its adjoint), and running the whole chain backwards returns the initial state to \(3\times10^{-16}\). Nothing in such a segment distinguishes forward from backward.

---

## 3. AT3 — The entropy gradient is the orientation

**Theorem AT3.** [TH4, T13′, T16′, T14′, TH9] Orientation is carried by structural projection events and by no other event type.

*Proof.* By T15's trichotomy the event types are exhaustive.
- **Free epochs** (T13′: diagonal unimodular) and **reconfigurations** (T16′: isometries) preserve \(S_{\rm rel}\) exactly (TH4), and each has an admissible inverse of the same type (the adjoint). A segment built from them is traversable in either direction, with identical entropy at every step. *No orientation.*
- **Structural projection** is non-isometric (T14′). \(S_{\rm rel}\) strictly decreases and \(S_{\rm gen}\) strictly increases (TH9), and the map is **not injective** — distinct pre-states share a post-state — so no admissible map runs it backwards. *Orientation.* ∎

Executable (§2): dephasing takes \(S_{\rm rel}\) from \(0.2028\) to \(0.0472\) and selection to \(0\); two states differing in weight by \(0.70\) vs \(0.40\) are exhibited with bit-identical outputs, so the inverse does not exist.

**The three-way identification.** docs/24 already noted that entropy production and the measurement problem share a locus (TH4). AT3 adds the third:

> **The arrow of time, entropy production, and structural projection are one event.**

The framework does not have three mysteries about irreversibility. It has one event type, F5, seen through three ledgers.

---

## 4. AT4 — The gradient measures the arrow; F5 *is* the arrow

This is where the framework can do better than "time emerges from the entropy gradient," and the improvement matters because it moves the arrow **out of the postulational TG layer and into the forced layer**.

**Theorem AT4.** [F5, O4/F3, SM-B3] The asymmetry of AT3 does not originate in the entropy functional. Its source is structural: a projection breaks the co-dependence linking the unselected residuals to the chain, and causal exclusion is stable — \(\prec\) is a strict partial order, so re-inclusion would require a data-dependence path that the projection is precisely what removed. The unselected remains **real** (O4/F3) and permanently **off that chain**.

*Proof sketch.* After the break, the chain's reachable share set and the dropped residual's are disjoint. Any later chain event's redex is built from chain-reachable structure (SB4), so no later event can depend on the dropped residual. Induction along the chain. ∎ (Executable §3: 200 further chain steps, co-dependence never returns.)

**Consequence.** \(\Delta S_{\rm gen}\ge0\) is the **quantitative readout** of a ratchet that exists at the F-layer, not the thing that makes it turn. This is strictly better for the theory:

- the arrow no longer depends on TG1–TG5, so it survives even if the geometric limit (contention 9) fails;
- it is not circular — the asymmetry is "this map has no inverse," which needs no prior notion of direction;
- and it explains *why* the gradient never changes sign, which "time emerges from the gradient" would have to assume.

**Correct statement of the claim, then:** *the arrow of time is entropic in content — every measurable manifestation of temporal direction is an entropy gradient — and structural in origin.*

---

## 5. AT5 — The arrow is exactly as dense as decoherence

**Theorem AT5.** [T10, T11, WM4, AT3] The frequency of oriented events along a chain is set by the isolation/maintain competition. Where environment-crossing shares are plentiful (WM4 charges them to the maintain ledger), \(C_{\rm isolate}\le C_{\rm maintain}\) holds continually and projection occurs at essentially every tick; where the cluster is isolated, projection is rare and the chain is nearly orientation-free.

Executable (§4): sweeping environmental pressure moves the fraction of oriented ticks from \(0\%\) through \(13\%\), \(37\%\), \(67\%\) to \(98\text{--}99.8\%\).

**What this buys.** It answers, without a new hypothesis, why the arrow is *macroscopically ubiquitous and microscopically absent*: those are the two ends of one sweep. It is T11 (rising maintain cost \(\Rightarrow\) classical sequentialization) read in the temporal ledger rather than the coherence ledger. The classical regime is not merely "where things decohere" — it is **where time has a direction**, and the same inequality decides both.

**Connection to \(\kappa\).** docs/02 §11's coherence \(\kappa\sim1/(1+\langle C\rangle)\) marks high-\(\kappa\) regimes as classical. AT5 says those are also the densely-oriented regimes. A deeply isolated coherent system has order without much arrow.

---

## 6. AT6 — Flow and duration

Two distinct things are meant by "the passage" of time, and the framework separates them.

**(a) Modular flow (state-dependent time).** Under TG1, \(K=-\log\sigma = C_{\rm maintain}/\Theta\) (TH5) generates a flow. On a horizon TG3 identifies it with the boost; in general this is the Connes–Rovelli thermal-time reading, and its framework content is sharp: **the generator of time's flow is the maintain ledger.** Time's flow is a property of the *state*, not of a background — which is what O2 demanded anyway.

**(b) Measurable duration.** **Theorem AT6.** [AT3, TH4] A clock must leave a record that later stages can read; a record that can be undone by an admissible inverse certifies nothing. By AT3 the only event without an admissible inverse is structural projection. Hence **measurable duration is counted by projection events** — equivalently by accumulated \(\Delta S_{\rm gen}\).

Executable (§5): an isometric clock's reading oscillates \(1.0, 0.5, 0.0, 0.5, 1.0,\dots\) — it revisits every value with period 4 and cannot distinguish \(t\) from \(t+4\), so it certifies no elapsed duration. Only the projection count is monotone.

This is the framework's version of the standard result that memory requires dissipation (Landauer–Bennett), obtained here from the event trichotomy rather than assumed.

---

## 7. Non-purchases (fixed ledger, charter §5)

- **The past hypothesis.** Nothing here explains why the initial class had low entropy. The framework says the gradient has a sign along chains; it does not say why the starting point was far from equilibrium. This relocates exactly as PA3 relocated forced-violation realization (docs/23 §4): **it is a property of the initial class — a boundary-condition question, not a dynamical one.** The parallel is structural, not rhetorical: in both cases the dynamics are settled and the initial class is not.
- **A metric on time.** Duration counted in projection events is not duration in seconds. Converting requires decoherence *rates*, which are still the integer environment knob of docs/08 §1, and any relativistic notion requires TG2 (contention 9).
- **Global time.** O2 forbids it, so the arrow is per-chain. Different evaluators accumulate different oriented duration; nothing here privileges one.
- **Time dilation, relativistic simultaneity, closed timelike curves.** All require the geometric limit; none is claimed.
- **CPT or microscopic reversibility as a derived symmetry.** The framework *has* micro-reversibility (free epochs are unitary, T13′) with macro-irreversibility localised at F5, which is the right shape — but no CPT theorem is proved.

---

## 8. Dependency map

```
O2 ──> F1 chains ──> SM-B3 partial order        [AT1: order, forced, no entropy]
                          │
                          └─ AT2: converse is also a partial order
                                  => order fixes NO orientation

T15 trichotomy
  ├─ T13' free epochs   (isometric) ──┐
  ├─ T16' reconfigurations (isometric)─┼─> S_rel invariant, inverse exists
  │                                    │   => no orientation
  └─ T14' structural projection ───────┴─> S_rel drops, NOT injective
                                           => AT3: orientation lives here alone

F5 + O4/F3 + SM-B3 ──> AT4 the ratchet (stable causal exclusion)
                        └─> dS_gen >= 0 is its readout, not its source
T10/T11 + WM4      ──> AT5 arrow density = decoherence density
AT3 + TH5          ──> AT6 duration counted by projection; flow = modular flow of C_maintain
```

## 9. Executable

`sim/arrow_of_time.py`:

1. **AT2**: four isometric events, \(S_{\rm rel}\) invariant to \(10^{-10}\), every step invertible, whole chain reversed to \(3\times10^{-16}\).
2. **AT3**: \(S_{\rm rel}\) drops at dephasing and again at selection; two distinct pre-states with bit-identical post-states, so no inverse.
3. **AT4**: co-dependence broken by projection never returns across 200 further chain steps.
4. **AT5**: oriented-tick fraction swept from 0% to 99.8% with environmental pressure.
5. **AT6**: isometric clock readings periodic (period 4) against a monotone projection counter.
