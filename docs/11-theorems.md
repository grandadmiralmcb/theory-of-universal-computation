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

**T12+** [T12, A4, D19, O3] Support frozen in free epoch.  
**N★** [T12, A4, D19, O3] Relative moduli frozen — on D19's stated domain (Foot fixed); across reconfigurations (T15) the \(M_w\) comparison is undefined, so N★ constrains nothing there (docs/17 §3).  
**R★** [T12+, B_flow] Invertible free-epoch weight maps.  
**T13** [R★, N★, norm gauge] Free-epoch maps are **diagonal** unitary on the active subspace (phase drift). No longer contended: general (non-diagonal) unitaries live at reconfiguration events (T16), matching QM's own architecture (free evolution diagonal in the co-rotating eigenbasis; mixing at interactions).  
**T15** [WM1, A4, O4, F5] Event trichotomy: free-epoch map | reconfiguration (decomposition changes, nothing dropped) | structural projection; mixed events factor. (docs/17 §2)  
**T16a** [A4, R-principle, T15] Reconfiguration maps are injective linear, determined by the rewrite.  
**T16b** [A4, T15, T16a, D20, O4] Reconfiguration maps are isometries; unitary at constant class count. (D20 is an explication, flagged in docs/17 §4.)  
**T14′** [T13, T15, T16b, T10] Non-isometric weight change ⇔ structural projection. (Supersedes T14's earlier caveated form.)  
**D12** Born reading — **not a theorem**.

---

## Structural bridge (add SB1–SB4; docs/15)

**SM-B1** [WM1, SB1, SB1-typing] Label sums are invariant under every admissible reduction. Conservation by *typing*, not Noether; a derivation from SB2 invariance is open.  
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
