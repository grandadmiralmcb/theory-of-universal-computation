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
**T11** [T10] Rising maintain cost \(\Rightarrow\) singleton \(\Rightarrow\) classical sequentialization.  
**T12** [T10, free epoch] Foot fixed in free epoch.

---

## Continuum idealization (add CI1–CI3, WM3)

**T3** [WM2,WM3,CI1] \(\delta v^*=-b/m\).  
**T4** [T3] Discrete sequential updates.  
**T5** [T4,CI2] \(\ddot x=-b/m\) in continuum limit.  
**T6** [T5,WM3] \(a_A/a_B=m_B/m_A\) under same constant \(b\).  
**T7** [T5] Projectile kinematics.  
**T8** [T5,CI3] \(m\ddot x=-V'(x)\).

---

## Hosted quantum (add A4, D19, B_flow; Born = D12)

**T12+** [T12, A4, D19, O3] Support frozen in free epoch.  
**N★** [T12, D19, O3] Relative moduli frozen.  
**R★** [T12+, B_flow] Invertible free-epoch weight maps.  
**T13** [R★, N★, norm gauge] Unitarity on active subspace.  
**T14** [T13, T10] Sole non-unitary locus = structural projection.  
**D12** Born reading — **not a theorem**.

---

## Non-theorems

Amplitudes from O1–O4; unitarity from bare \(C\); Born derived; finite trees as ontology; continuum Newton without CI; monism; consciousness identity.

---

## Executable

T6: `sim/end_to_end_T6.py`  
T9–T12 pattern: `sim/expr_tree.py`  
HQ free epoch / projection: `sim/linear_reduce.py`
