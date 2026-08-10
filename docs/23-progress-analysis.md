# 23 — Progress Analysis of the WM Conserving Fragment

*Status: analysis with executable results — the successor target of docs/22 §6, answered. **Result: forced-violation states are reachable in the unrestricted working-model calculus** (a one-conserving-step example exists); progress holds exactly on the charge-relevant (λI-style) class; and the physical realization question therefore relocates from the dynamics to the **initial class** — a boundary-condition question. Executable: `sim/progress_analysis.py`.*

Authority: `docs/00-theory-charter.md` (ST1, CC′), `docs/22-forced-violation.md` (FV1–FV3).

---

## 1. The violation channels of the actual calculus

In the working-model term language (`app`, `abs`, `pair`/`proj` over labeled shares), where can charge be destroyed or created?

**Theorem PA0 (duplication is charge-safe).** [WM1, SB1] Substitution copies term structure but reuses Share objects — sharing is by reference. Duplicating a bound variable duplicates *references*, never shares; cluster charge counts distinct shares once, so contraction conserves charge identically. ∎ (Demo 1: \((\lambda x.\langle x,x\rangle)\,S \to \langle S,S\rangle\) with \(Q = 1\) throughout.)

This is worth savoring: **the `share` primitive is exactly what makes contraction conserving.** Linear logic must *restrict* duplication to protect resources; the sharing calculus gets the protection for free, because charge lives on the shared object, not on its references.

**Consequently the only violation channels are discards:**
- **K-redexes**: \((\lambda x.M)\,N\) with \(x \notin FV(M)\) — the argument is dropped;
- **projections**: \(\mathrm{proj}_i\,\langle A,B\rangle\) — the unprojected component is dropped.

A discard destroys charge only when it drops the **last reference** (Demo 4: dropping one reference to a still-shared share is \(V=0\)). The toy "clamp" of docs/22 is precisely a discarding context of the real calculus.

## 2. PA2 — progress fails, non-trivially

**Theorem PA2.** The unrestricted calculus reaches forced-violation states from initial terms whose every redex is conserving:
\[
(\lambda f.\, f\,S)\,(\lambda x.\, c) \;\xrightarrow{\beta,\ V=0}\; (\lambda x.\, c)\,S \;\xrightarrow{\text{only redex: K-discard},\ V=1}\; c
\]
The initial term's only redex is an ordinary β-step; its reduct's only redex discards the charged share. Hence FV states are **reachable**, not merely constructible, and progress fails for the conserving fragment of the raw working model. ∎ (Demo 2, fully rigorous — an explicit two-line term.)

## 3. PA1 — progress on the charge-relevant class

**Definition (charge relevance).** A configuration is *charge-relevant* if no charged share can flow to a discard position: no K-redex argument and no unprojected pair component contains (or can come to contain) the last reference to a charged share. This is Church's λI discipline relativized to charge: vacuous binding and unprojected positions are forbidden **for charged flows only** — neutral structure may be discarded freely (matching SB1's free \(q=0\) removal).

**Theorem PA1 (progress + preservation, sketch).** [WM1, SB1, ST1] On charge-relevant configurations: (preservation) β and projection steps preserve charge relevance — substitution places arguments precisely at their occurrence sites, so a charged share's references land in relevant positions; (progress) every non-normal charge-relevant configuration has a \(V=0\) redex, since any redex present either involves no charged discard or is excluded by relevance. Hence by FV1, **conservation is absolute on the charge-relevant class.** *Proof status: sketch — the standard λI induction relativized; mechanization is the remaining debt.* The dynamic audit (Demo 5) confirms the pattern: checker-accepted terms run violation-free.

**Checker.** `charge_relevant` in the sim is a conservative static approximation (it also rejects a safe higher-order term — Demo 5's last case — exactly the incompleteness every type system has). Ground truth for the examples is the dynamic audit.

## 4. PA3 — the relocation result

Combining FV1 + PA1 + PA2:

> **The dynamics is the same either way; whether forced violations occur is a property of the initial class.** If physical initial configurations (the SB3 ground configuration and its excitations) are charge-relevant, conservation is absolute and the Sakharov door of docs/22 closes structurally. If physical structure contains charge-discarding contexts — real "clamps" — forced violations occur with the derived docs/22 phenomenology (minimal step, locality, out-of-equilibrium, floor-tie asymmetry).

Three readings of significance:

1. **Baryon-number violation becomes a boundary-condition question.** Not "does the law permit it" (it does, gracefully, via ST1) nor "does the dynamics drive it" (the dynamics is violation-averse by construction) — but "does the world's structure include discarding contexts for charged flows?" A cosmological-initial-data question, sharply posed.
2. **The consistency check closes.** `spectrum_toy`'s and `expr_tree`'s move sets contain no charged-discard channel — they are charge-relevant by construction, which is *why* their conservation was absolute. The corpus's own executable history is explained by PA1.
3. **The next structural probe is the vacuum.** Whether the SB3 ground configuration is charge-relevant is now the concrete question standing between the framework and a verdict on forced violation — connecting the FV thread to the vacuum/spectrum sector.

## 5. Ledger

| Item | Status |
|---|---|
| PA0 (duplication charge-safe via sharing) | Theorem; executable |
| PA2 (reachable FV state in the raw calculus) | **Theorem, fully rigorous** (explicit term); executable |
| PA1 (progress + preservation on charge-relevant class) | Theorem at sketch level; mechanization open; dynamic audit consistent |
| Conservative checker | Tool; incomplete by design (demonstrated honestly) |
| PA3 (relocation to the initial class) | Reading of FV1+PA1+PA2 — the framework's answer to "are FV states realized?": **decided by boundary conditions, not by dynamics** |
| Successor question | Is the SB3 ground configuration charge-relevant? |
