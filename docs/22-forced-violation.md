# 22 — Forced-Violation States

*Status: development document for the open question inherited from contention 8's closure: are forced-violation states physically realized? Outcome: the question is reframed as a **progress-theorem question** about the conserving fragment; the phenomenology of minimal violation is derived; and all three Sakharov conditions acquire structural counterparts. Executable: `sim/forced_violation.py`.*

Authority: `docs/00-theory-charter.md` (ST1, CC′ adopted), `docs/21-stratified-variant.md` (TS4).

---

## 1. Definitions

Under ST1 + CC′, write \(V(e)\) for the top-stratum violation charge of a redex \(e\).

- **Conserving fragment:** the rewrite relation restricted to \(V=0\) redexes.
- **FV state:** a state that is **V=0-stuck** (no conserving redex exists) but **not fully normal** (violating redexes exist). Dynamics there proceeds by lex-min selection: minimal \(V\), then floor cost (TS4).
- **FV event:** the violating step selected at an FV state.

The two architectures separate exactly here: brute typing declares an FV state terminal (deadlock); ST1 continues through it by minimal violation.

## 2. FV1 — realization is a progress question

**Theorem FV1.** [ST1, CC′] If the conserving fragment satisfies **progress** (every reachable non-normal state has a \(V=0\) redex) and **preservation** (conserving steps stay in the reachable class) on a class of initial states, then no FV state is ever reached from that class, no violation is ever selected, and SM-B1′ reduces to absolute conservation (old SM-B1) on that class. Conversely, forced violations are realized from that class **iff progress fails** there. ∎

**Reading.** "Are forced-violation states physically realized?" is precisely the question type theory asks of a calculus: *does the well-typed (here: conserving) fragment enjoy progress?* Stuck-but-not-normal states are the familiar "stuck terms" of programming-language theory; ST1 gives them dynamics instead of undefinedness. The physical question becomes a structural analysis of the actual WM rule-set — a concrete, attackable target.

## 3. FV2 — the general question is undecidable; instances are not

**Theorem FV2.** [WM1 universality] For Turing-complete rule-sets, reachability of a V=0-stuck state from a given initial class is undecidable (reduce halting: encode a machine so that it reaches a clamp-like jam iff it halts). Hence there is no uniform decision procedure; FV-realization must be settled **per rule-set**, by progress proofs or counterexamples. ∎

The toy in `sim/forced_violation.py` shows both outcomes are structurally cheap: an *open* configuration class (vacuum slots available, no clamps) provably has progress — 200-tick runs select zero violations and conserve exactly; adding **packing + capacity structures** ("clamps": structures that must absorb a neighbor) breaks progress with a three-cell example, \([+1\;\#\;-1]\): no conserving redex, two violating ones.

## 4. Phenomenology of minimal violation (derived shapes)

At an FV state, lex-min selection entails:

1. **Minimal-step rule.** The violation channel with least \(V\) is selected: forced violations change conserved charge by the **minimal available group step** (demo: offered \(V=2\) and \(V=1\), selection takes \(V=1\)). Large-jump violations occur only when no smaller channel exists — a selection rule, derived, not imposed.
2. **Locality.** The violation occurs at the jam site (the redex that fires is one of the stuck state's own); charge non-conservation is a local event with a definite structural location.
3. **Out-of-equilibrium by construction.** An FV state is precisely one where the conserving flow is jammed — the framework's structural counterpart of departure from equilibrium. No separate non-equilibrium condition needs importing.

## 5. Sakharov counterparts

Baryogenesis requires (i) violation of the conserved number, (ii) C and CP violation, (iii) departure from equilibrium. All three now have structural counterparts:

| Sakharov condition | Structural counterpart | Where derived |
|---|---|---|
| Number violation | FV events (progress failure of the conserving fragment) | §§2–3 |
| C/CP violation | **Floor tie-breaking at V-ties**: when conjugate channels (+q vs −q destruction) tie in the top stratum, the Archimedean floor decides; a conjugation-asymmetric floor yields systematic drift | §5, demo 4 |
| Out of equilibrium | FV states are jammed conserving flow, by definition | §4.3 |

**FV3 (tie-breaking asymmetry).** [ST1, CC′] At V-ties between conjugate violation channels, selection is decided by floor costs. A conjugation-symmetric floor yields zero expected charge drift over an FV ensemble; any finite floor asymmetry yields systematic drift — in the toy, a +0.5 floor bias converts noise-level drift (−32/2000, ≈0.7σ) into deterministic drift (−2000/2000). ∎

**The notable structural fact:** the asymmetry needs **no top-stratum breaking** — the exact law (Γ-conjugation symmetry of the strata) remains exact; the bias lives entirely in the Archimedean floor, where finite asymmetries are cheap and Γ-invariance was never required to be exact (SB2 constrains the designated subgroup only). Matter excess as *floor-level tie-breaking of forced violations* is the framework's mechanism shape for baryogenesis.

**Hedge, prominently:** this is a mechanism *shape* with toy-level demonstration. No quantitative content — no rates, no abundances, no claim that the actual WM rule-set realizes FV states (that is §6's open target).

## 6. The concrete open target

**Progress analysis of the actual WM conserving fragment**: does the reduced primitive set (`app`, `abs`, `pair`/`proj`, `eq`, `reduce`, `share` with SB1 labels under ST1) admit reachable V=0-stuck states from well-formed initial configurations? The toy shows the answer is decided by structural features (packing, capacity, clamp-like obligations) that the real rule-set may or may not possess. A progress proof would make conservation absolute on-domain (FV1); a reachable counterexample would make forced violation a *prediction* of the working model.

**ANSWERED (docs/23-progress-analysis.md).** Progress **fails** for the unrestricted calculus — an explicit two-step term reaches an FV state from a purely conserving start (PA2) — and **holds** on the charge-relevant (λI-relativized) class (PA1, sketch level). Duplication is charge-safe by reference-sharing (PA0), so discards are the only violation channel; realization therefore relocates to the **initial class** (PA3): a boundary-condition question, with the SB3 ground configuration's charge-relevance as the successor probe.

## 7. Ledger

| Item | Status |
|---|---|
| FV state definition; typing-vs-ST1 separation | Definition + immediate |
| FV1 (progress ⇔ no realized violations) | Theorem |
| FV2 (general undecidability; per-system analysis) | Theorem (sketch) |
| Minimal-step, locality, out-of-equilibrium shapes | Derived from lex-min |
| FV3 (asymmetry from floor tie-breaking) | Theorem + executable |
| Sakharov mapping | Mechanism shape, toy-demonstrated, **no quantitative content** |
| Does the real WM rule-set realize FV states? | **Open** — the successor question, now well-posed (§6) |
