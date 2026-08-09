# 21 — The Stratified Variant Developed (Contention 8)

*Status: development document for the ¬CC branch of RM2. Outcome: the stratified variant is not a rival theory to be eliminated — it is the natural home of the framework's **exact rules**, while observed phenomenology forces its **dynamical floor** to be one-currency. This yields a synthesis candidate **CC′** and a proposed unification of typing with cost (**ST1**). Executable: `sim/stratified_cost.py`.*

Authority: `docs/20-grounding-AD-axioms.md` (RM2 dichotomy), `docs/00-theory-charter.md`.

---

## 1. Lex selection is constraint-then-cost

A stratified cost is a vector in a lexicographic product (Hahn form, RM2); two strata \((C_{\rm hi}, C_{\rm lo})\) suffice for everything below. Lex-minimization factorizes:

> minimize \(C_{\rm hi}\); among its minimizers, minimize \(C_{\rm lo}\).

**Observation (the key structural fact).** The top stratum never *trades* against the floor at any finite rate — it acts as a **hard constraint** (an exact rule); the floor acts as ordinary cost (a force). Stratification is the cost-theoretic form of the distinction between *laws that are never violated* and *tendencies that are priced*. This single observation drives all four results.

## 2. TS1 — classical viability

**Theorem TS1.** Any stratification separating the terms of the velocity-form cost (CI4) degenerates classical dynamics: with the inertial term on top, \(\delta v = 0\) uniquely minimizes the top stratum and motion freezes; with the bias term on top, the top stratum is unbounded below and selection runs away. Newtonian dynamics (T3–T8) exists **iff** all CI4 ingredients share one stratum.

*Proof.* Lex-argmin case analysis; executable in `sim/stratified_cost.py` §2. ∎

## 3. TS2 — the decoherence freeze

**Theorem TS2.** If the observational-identity flag \(D\) sits strictly above the share/binding currency, and every isolation event charges the flag, then the isolation/maintain comparison is decided at the top stratum: \(C_{\rm iso} = (1, \cdot) >_{\rm lex} (0, \cdot) = C_{\rm maint}\) for **every** value of environmental share pressure. No structural projection is ever selected; T11 (classical limit of coherence) is lost; macroscopic superpositions persist indefinitely.

*Proof.* Immediate from §1's factorization; executable §3 (env = 0, 5, 50, 5000 — one-currency decoheres from env = 5, D-top never does). ∎

**Corollary (empirical adjudication, partial).** Observed classicality — the phenomenon T9–T11 were built to capture — **forces the counters that trade in realized isolation/maintain competitions into one stratum**. This is the first genuinely empirical constraint on contention 8: whatever else is stratified, the *dynamical floor is one-currency where we have looked*.

## 4. TS3 — observational reach of stratification

**Theorem TS3.** Lex selection depends only on (i) the top-stratum comparison and (ii) the floor comparison among top-minimizers. Hence: in any competition where all candidates carry **equal** top charge, the stratified theory is observationally identical to its floor; stratification is detectable **only** in competitions with unequal top charges — where it manifests as an exact selection rule, never as a graded tendency. ∎

**Reading.** Stratification cannot hide: it either does nothing (equal top charges) or shows up as an inviolable rule. Combined with TS1/TS2, the viable form of the stratified variant is fixed: **exact rules on top, one Archimedean dynamical currency below.**

## 5. TS4 + ST1 — typing recovered as a top stratum

The SB layer enforces conservation by *typing* (SB1-typing: label-violating rewrites are inadmissible), which docs/15 honestly flagged as "conservation by fiat, not Noether." The stratified variant offers something better:

**Postulate ST1 (typing as stratum).** Replace SB1-typing's admissibility rule with a top-stratum **violation charge** \(V\) (label-violation units), lexically above the dynamical floor.

**Theorem TS4.** Under ST1: (i) whenever a label-conserving alternative exists, lex selection chooses it — SM-B1's conservation behavior is reproduced *without any admissibility rule*; (ii) when **no** conserving alternative exists, selection degrades gracefully to the minimal violation — a situation brute typing cannot even express (it deadlocks).

*Proof.* §1 factorization; executable §4. ∎

**What ST1 buys conceptually:**
- **Unification.** "Constraints/typing" and "costs/forces" stop being two primitive kinds; they are strata of one ordered structure. The theory's exact laws (conservation) and its dynamical laws (Newtonian selection, decoherence) differ by *position in the Hahn order*, nothing else.
- **A discriminating prediction-shape.** Brute typing and top-stratum typing agree everywhere except **forced-violation situations** — states from which every admissible continuation violates the conservation law. Typing says such states halt; ST1 says they decay by minimal violation. Rare-event violation physics (Sakharov-condition-style processes needing baryon-number violation) is precisely where the two readings part company. *Carefully labeled speculation:* if the world realizes forced violations, ST1-style stratification is the natural host; nothing quantitative is claimed.

## 6. CC′ — the synthesis position on contention 8

The development yields a determinate proposal rather than a standing fork:

> **CC′ (refined common currency).** The **dynamical floor** is Archimedean — one currency, Hölder-represented, WM2-shaped (this is what TS1/TS2 show phenomenology demands). **Above** the floor sit finitely many exact strata — the theory's inviolable selection rules (label conservation via ST1; any future exact law). RM2's two branches are **both realized, in different roles.**

Under CC′: RM1/WM2 remain correct as statements about the floor; SM-B1 remains correct with its mechanism relocated from typing to stratification; contention 8's question "does the stratified variant deserve parallel development?" is answered — *it is not a parallel; it is the top of the same structure.*

## 7. Honest ledger

| Claim | Status |
|---|---|
| Lex = constraint-then-cost (§1) | Elementary, load-bearing |
| TS1, TS2, TS3, TS4 | Theorems (lex-argmin analysis; executable) |
| Empirical force of TS2's corollary | Real but conditional on the hypothesis that every isolation charges the flag; an identity-preserving isolation channel would reopen D-top stratification |
| ST1 | **Postulate** — an identification, not a derivation; it *replaces* SB1-typing rather than following from it |
| CC′ | **Synthesis proposal**, not a theorem: the "exact strata above, one floor below" architecture is consistent with everything proved and demanded by nothing beyond TS1/TS2's viability constraints plus ST1's elegance |
| Forced-violation phenomenology (§5) | Speculative hook, flagged; no quantitative content |

**Adjudication state for contention 8:** developed to a decision point. Adopting CC′ + ST1 closes the contention (both RM2 branches realized in role-separated form) at the price of one identification postulate; retaining brute typing + bare CC keeps the old architecture with typing as unexplained fiat.

**ADOPTED (2026-08-08, owner decision).** CC′ and ST1 are now charter postulates (docs/00 §3); contention 8 is closed. Consequences applied: SB1-typing is reclassified as the derived V=0 behavior of ST1 (docs/15); SM-B1's conservation is restated as conditional on non-forced states (docs/11); RM1's currency clause reads the floor of CC′. The forced-violation prediction-shape of §5 moves from speculation-about-a-variant to an open question *of the theory*.
