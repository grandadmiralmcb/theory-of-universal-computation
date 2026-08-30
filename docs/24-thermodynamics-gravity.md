# 24 — Thermodynamics and Gravity (TG layer)

*Status: derivation document. Thesis: **the relevant entropy is relative information**, and gravity is what that entropy does. Given five named postulates (TG1–TG5) on top of the existing WM/CI/HQ/SB stack, the Einstein equation follows by two independent routes, Newton's constant is **identified** (not fitted) with the ground configuration's share density across a cut, the equivalence principle becomes a **theorem** (closing contention 2), and the black-hole area theorem — including "two merging holes make a bigger hole" — falls out of a monotonicity theorem that the framework already owned. Executable: `sim/thermo_gravity.py`.*

Authority: `docs/00-theory-charter.md`. Companion bridge: `docs/15-sm-bridge.md` (SB1–SB4). Theorems with hypotheses: `docs/11-theorems.md`.

**Method rule, restated for this layer.** Everything geometric enters through one postulate (TG2) that is the causal-set continuum-limit problem, imported **unsolved**. If TG2 fails, §§5–7 fall with it. What the framework contributes is not the continuum machinery — that is standard and cited — but four things it supplies from its own primitives: *which* entropy is physical (§1), *why* it obeys an area law (§2), *why* it is monotone (§4), and *why* gravity couples to inertia (§6).

---

## 0. The three claims in one view

| Claim | Framework resource | Status |
|---|---|---|
| Only **relative** entropy is an observable | RM1 scale gauge + CI4 additive gauge + WM1 granularity | **TH1**, from existing gauges (RM1/CI4/WM1) |
| Entropy of a region is an **area** (cut share count) | WM2's \(S\) counter is a boundary quantity | **TH2**, forced given WM1+WM2 |
| Entropy is **monotone**; all production sits at projection | T13′/T16′/T14′ event trichotomy | **TH4**, forced given A4/D20 |
| Einstein equation | TH1–TH5 + TG1–TG5 | **TH6**, postulational |
| \(G\) = reciprocal ground cut density | TH6 + TG2 | **TH7**, identification |
| Weak equivalence principle | WM3 + TH2 (one counter, two roles) | **TH8**, closes contention 2 |
| Merged hole is bigger | TH4 + SM-B3 | **TH9/TH10** |

---

## 1. TH1 — Only relative entropy is an observable

The framework has three gauge freedoms, all already on the record. Each removes a different absolute:

1. **Scale (RM1).** The Hölder representation fixes the floor cost \(C\) only **up to positive scale** (docs/19 §5, docs/20). Any Gibbs weight built on it depends on \(C\) only through \(C/\Theta\), and \(\Theta\) — the structural temperature — is itself measured in cost units. So \(\Theta\) is **not an independent constant of the theory**: it is the unit choice RM1 leaves open, and the invariant \(C/\Theta\) is a pure number. *Consequence:* entropy in this framework is a **count**, never a cost.
2. **Additive gauge (CI4).** docs/02 §2 records that the constant \(b^2\tau/2m\) may be added to the per-tick cost "without changing which \(\delta v\) is selected." So cost has no zero, hence neither does the modular energy \(\langle K\rangle = \langle C_{\rm maintain}\rangle/\Theta\). *Consequence:* only **differences** \(\Delta\langle K\rangle\) against a reference are defined — which is why the first law (TH5) is a statement about \(\delta\), and why "sum the vacuum's cost and gravitate it" is not a computation this framework performs (§5, \(\Lambda\)).
3. **Granularity (WM1).** The number of `share` nodes crossing a boundary depends on how finely the carrier decomposes structure: refining each share into \(k\) sub-shares multiplies every count by \(k\). docs/15 §3 already flags the same dependence for the spectrum ("discreteness is an artifact of integer counters"). *Consequence:* absolute entropy has **no carrier-independent value**.

**Theorem TH1 (relativity of entropy).** [RM1, CI4, WM1] Under a \(k\)-fold granularity refinement of a region carrying \(N\) shares, the von Neumann entropy of any state diverges as \(S \to S + N\log k\), while for any fixed reference \(\sigma\)
\[
S_{\rm rel}(\rho\Vert\sigma) \;=\; \operatorname{Tr}\rho(\log\rho - \log\sigma) \;\ge\; 0
\]
is exactly invariant. Together with (1) and (2): **every thermodynamic quantity that does physical work in this layer is a difference against the SB3 ground configuration**, never an absolute.

*Proof.* Refinement tensors both \(\rho\) and \(\sigma\) with the same maximally mixed factor \(\mathbb{1}_k/k\) per share. \(S\) is additive under tensoring, picking up \(N\log k\); \(S_{\rm rel}\) is additive too, but the common factor contributes \(S_{\rm rel}(\mathbb{1}_k/k\Vert\mathbb{1}_k/k)=0\). Positivity is Klein's inequality. ∎ (Executable: `sim/thermo_gravity.py` §2.)

**Reference state.** The reference is not a free choice: \(\sigma\) is the **SB3 ground configuration** restricted to the region — the minimal-rest-cost \(Q=0\) state. "Relative to what" is answered by machinery the framework already had.

**Consequence for the divergence problem.** The UV divergence of entanglement entropy in QFT is, read here, exactly item (3): carrier-granularity dependence, not a physical infinity. This is the framework's version of Susskind–Uglum (the divergence renormalizes \(G\)); §5 makes it an identity rather than a renormalization.

> **This is the document's organizing thesis: relevant entropy is tied to relative information.** Every quantity below that does work — modular energy, generalized entropy, horizon entropy change, the Einstein equation's source — is a difference against the ground configuration. Absolute entropies appear only as bookkeeping.

---

## 2. TH2 — The area law is what the \(S\)-counter counts

**Definitions.** A **cut** \(\chi=(\mathrm{In},\mathrm{Out})\) is a partition of a term's nodes. The **cut share count** \(N(\chi)\) is the number of distinct `share` nodes whose content is reachable from both sides.

**Theorem TH2 (structural area law).** [WM1, WM2] The cost of isolating \(\mathrm{In}\) from \(\mathrm{Out}\) is
\[
C_{\rm isolate}(\chi) \;=\; \alpha\,N(\chi) \;+\; \beta\,B(\chi) \;+\; \gamma\,[N(\chi)>0],
\]
a function of the **cut alone**. It is independent of the number of nodes interior to either side.

*Proof.* This is `isolation_cost_from_tree` (docs/08 §1) with \(\Sigma\) the cross-cut share set: \(\Sigma\) is determined by which shares are severed, and \(B(\Sigma)\) counts binding sites inside those shares' contents. Interior structure enters neither. ∎ (Executable: `sim/thermo_gravity.py` §1 — interior grown by two orders of magnitude at fixed boundary; \(C_{\rm isolate}\) constant.)

**Corollary TH2′ (entropy per cut).** [TH2, TG1, D20] Under TG1 the reduced state on \(\mathrm{In}\) is mixed exactly to the extent that shares are severed; with \(d\) the effective content-dimension per share, the ground cut entropy is
\[
S(\chi) \;=\; s_0\,N(\chi), \qquad s_0 \equiv \log d .
\]

**Reading.** The framework did not *add* holography; docs/01 already listed "holographic character" as an ontological reading. TH2 says why: the theory's disruption currency is a **severed-sharing count**, and severed sharing is a boundary relation. A volume-extensive cost would require charging structure that is not disturbed. The area law is not a discovery about gravity here — it is the shape of WM2.

---

## 3. Postulates TG1–TG5

Each is charged explicitly and appears in every theorem hypothesis that uses it.

| ID | Postulate | What it buys | Honest cost |
|----|-----------|--------------|-------------|
| **TG1** | **Statistical coarse-graining.** When only \(\Gamma\)-invariant (SB2) macroscopic data about a region is retained, the induced measure over compatible microstructures minimizes relative entropy to the ground measure subject to that data — giving Gibbs form \(p \propto \sigma\,e^{-C/\Theta}\), with \(\Theta\) the **structural temperature** (the scale RM1 leaves free) | statistical mechanics on the floor | O3 gives an **argmin**, not an ensemble. TG1 is a genuine addition: it says selection under retained-information constraints is MaxEnt, i.e. adds no information beyond the constraints |
| **TG2** | **Geometric limit.** There is a coarse-graining of the SB4 event order to a Lorentzian manifold \((M,g)\) in which (i) \(\prec\) approximates the metric causal order, and (ii) the ground cut count of a codimension-2 surface converges to \(N_{\rm gnd} = \eta_N\,A\) with finite \(\eta_N\) (shares per unit area) | area, curvature, null generators | **The whole geometric debt.** This is the causal-set continuum-limit problem (dimension, local Lorentz invariance), imported **unsolved** — docs/15 §4, docs/05 §3.2. Nothing below is safer than TG2 |
| **TG3** | **Local modular flow (KMS).** For a local causal horizon, the modular flow of the accessible algebra in the ground state is the boost generator, KMS-periodic with period \(2\pi\) | Unruh relation \(T=\kappa/2\pi\) | Bisognano–Wichmann is a **theorem for wedges in Minkowski QFT**; asserting it for the emergent structure is an assumption, and it is where the factor \(2\pi\) — hence \(G\)'s normalization — comes from |
| **TG4** | **Modular energy is stress-energy.** The continuum limit's \(T_{ab}\) represents the flux of modular (maintain-ledger) cost: \(\delta\langle K\rangle = 2\pi\!\int T_{ab}\chi^a d\Sigma^b\) | a source term | Identification, not derivation. Also imports \(\nabla^a T_{ab}=0\) |
| **TG5** | **Entanglement equilibrium.** The ground configuration extremizes total entropy in a small ball at fixed volume | Route A (§5) | Route B (§5) does **not** need TG5; the two routes agreeing is the check on it |

**Layer position (charter §4).** TG sits above SB and CI: it consumes WM1–WM4, CI1–CI3, A4/D19/D20, SB1–SB4, CC′.

---

## 4. TH3–TH5 — Horizons, monotonicity, the first law

### TH3 — Horizons are already in the theory

**Theorem TH3 (horizon reduction).** [F1, F3/O4, SB4, SM-B3, A4] Let \(\gamma\) be an evaluator's F1 chain and \(\mathrm{Acc}(\gamma)=\bigcup_n J^-(\gamma_n)\) its accessible past under \(\prec\). If \(\mathrm{Acc}(\gamma)\) is a proper subset of the event set, the evaluator's algebra is a proper subalgebra, its state is the restriction of the global state, and that restriction is generically **mixed**, with entropy given by TH2′ on the horizon cut \(\partial\mathrm{Acc}(\gamma)\).

*Proof.* \(\prec\) is a strict partial order (SM-B3), so causal exclusion is stable: an event outside \(\mathrm{Acc}(\gamma)\) is outside it at every later stage. O4/F3 makes the excluded structure **real but unselectable** — precisely the condition for the accessible description to be a proper restriction. Restriction of a state entangled across the cut is mixed. ∎

**Why this matters.** The origin of horizon thermality is not an extra hypothesis here: F3 ("the unselected persists") plus SB4's order *is* the statement that a horizon leaves behind real, inaccessible structure. What TG3 adds is only that the resulting mixed state is **KMS at \(2\pi\)** — the quantitative part.

### TH4 — Structural monotonicity (the framework's data-processing inequality)

**Theorem TH4.** [A4, D20, T15, T13′, T16′, T14′] For any admissible event map \(\Phi\) and any states \(\rho,\sigma\),
\[
S_{\rm rel}(\Phi\rho\Vert\Phi\sigma) \;\le\; S_{\rm rel}(\rho\Vert\sigma),
\]
with **equality** on free epochs and reconfigurations, and strict decrease possible only at structural projection.

*Proof.* T15's trichotomy exhausts the event types. (i) Free-epoch maps are diagonal unimodular (T13′), hence unitary; \(S_{\rm rel}\) is unitarily invariant. (ii) Reconfiguration maps are isometries (T16′); \(S_{\rm rel}(V\rho V^\dagger\Vert V\sigma V^\dagger)=S_{\rm rel}(\rho\Vert\sigma)\) for \(V^\dagger V=\mathbb{1}\). (iii) A structural projection acts on the accessible description as class-dephasing followed by restriction to the surviving class algebra; both are CPTP, and \(S_{\rm rel}\) is monotone under CPTP maps (Uhlmann). ∎

**Reading — the load-bearing sentence of this document.** The framework already located *all* irreversibility at one event type (T14′: non-isometric weight change ⇔ structural projection). TH4 says the **second law has the same locus**. Entropy production and the measurement problem are not two mysteries: they are one event, seen through two ledgers.

### TH5 — First law of structural entanglement

**Theorem TH5.** [TG1, A4] With \(K \equiv -\log\sigma\) the modular Hamiltonian of the ground state on a region,
\[
S_{\rm rel}(\rho\Vert\sigma) = \Delta\langle K\rangle - \Delta S \;\ge\; 0,
\]
and since \(S_{\rm rel}\) is minimized (at \(0\)) when \(\rho=\sigma\), its first variation about \(\sigma\) vanishes:
\[
\boxed{\;\delta S = \delta\langle K\rangle\;}
\]

*Proof.* Expand the definition; positivity with equality at \(\rho=\sigma\) forces the linear term to vanish. ∎

**Framework identification.** Under TG1, \(\sigma \propto e^{-C_{\rm maintain}/\Theta}\) on the region, so
\[
K = C_{\rm maintain}/\Theta + \text{const}.
\]
The modular Hamiltonian **is the maintain ledger in temperature units** — and WM4 already says which shares are charged to that ledger: the environment-crossing ones, i.e. exactly the cut. The two structures were built for different purposes and coincide.

---

## 5. TH6–TH7 — The Einstein equation, twice

Both routes assume TG2 (so that "area", "null generator", "\(R_{ab}\)" exist) and set \(c=\hbar=k_B=1\). Write \(\eta \equiv s_0\,\eta_N\) for entropy per unit area — the only free constant.

### Route B (non-equilibrium: Clausius on local causal horizons)

Hypotheses: TG1–TG4 (**not** TG5), TH2′, TH3.

For each point \(p\) and each null \(k^a\), take the local Rindler horizon with approximate boost Killing field \(\chi^a=-\kappa\lambda k^a\), and impose the Clausius relation \(\delta Q = T\,\delta S\) for the heat flux across it:

\[
\delta Q = \int T_{ab}\chi^a\,d\Sigma^b = -\kappa\!\int\!\lambda\,T_{ab}k^ak^b\,d\lambda\,dA \quad \text{(TG4)}
\]
\[
\frac{d\theta}{d\lambda} = -R_{ab}k^ak^b \;\Rightarrow\; \delta A = \int\theta\,d\lambda\,dA = -\!\int\!\lambda\,R_{ab}k^ak^b\,d\lambda\,dA \quad \text{(Raychaudhuri, } \theta=\sigma=0 \text{ at } p)
\]
\[
T\,\delta S = \frac{\kappa}{2\pi}\,\eta\,\delta A \quad \text{(TG3 + TH2′)}
\]

Equating for all null \(k^a\) gives \(T_{ab}k^ak^b = \frac{\eta}{2\pi}R_{ab}k^ak^b\), hence \(\frac{\eta}{2\pi}R_{ab} - T_{ab} = f\,g_{ab}\). Imposing \(\nabla^aT_{ab}=0\) (TG4) and the contracted Bianchi identity fixes \(f = \frac{\eta}{4\pi}R + \text{const}\):

\[
\boxed{\;G_{ab} + \Lambda g_{ab} = \frac{2\pi}{\eta}\,T_{ab}\;}
\]

### Route A (equilibrium: relative entropy in a small ball)

Hypotheses: TG1–TG5, TH5. This is the route that wears the thesis of §1 on its face — the whole derivation is a statement about \(S_{\rm rel}\).

Take a geodesic ball of radius \(\ell\) about \(p\) in the local free-fall frame. TG5: \(\eta\,\delta A|_V + \delta S_{\rm matter} = 0\).

*Geometry side.* For a 3-dimensional geodesic ball, \(A(\ell)=4\pi\ell^2\!\left(1-\tfrac{R^{(3)}\ell^2}{18}\right)\), \(V(\ell)=\tfrac{4\pi}{3}\ell^3\!\left(1-\tfrac{R^{(3)}\ell^2}{30}\right)\). Comparing at **fixed volume** (so \(\ell_{\rm flat}=\ell(1-R^{(3)}\ell^2/90)\)):
\[
\delta A|_V = -\tfrac{2\pi}{15}\,\ell^4 R^{(3)} = -\tfrac{4\pi}{15}\,\ell^4\,G_{ab}u^au^b,
\]
using the Hamiltonian constraint \(R^{(3)} = 2G_{ab}u^au^b\) on the maximal slice through \(p\).

*Matter side.* By TH5, \(\delta S_{\rm matter}=\delta\langle K\rangle\), and the ball's modular Hamiltonian (TG3/TG4, CHM form) \(K = 2\pi\!\int_\Sigma \frac{\ell^2-r^2}{2\ell}T_{ab}u^au^b\,d^3x\) gives, for slowly varying \(T\),
\[
\delta\langle K\rangle = \tfrac{8\pi^2}{15}\,\ell^4\,\delta T_{ab}u^au^b .
\]

Equating: \(\eta\,\tfrac{4\pi}{15}G_{ab}u^au^b = \tfrac{8\pi^2}{15}\,T_{ab}u^au^b\), i.e. \(G_{ab}u^au^b = \frac{2\pi}{\eta}T_{ab}u^au^b\) for every local frame \(u\) — hence, by local Lorentz invariance, the same tensor equation as Route B. ∎

*(The \(\ell^4\) coefficients \(-2\pi/15\) and \(8\pi^2/15\) are verified numerically against exact geodesic balls on \(S^3\) and exact quadrature in `sim/thermo_gravity.py` §4.)*

### TH6 and TH7

**Theorem TH6 (Einstein equation).** [TG1–TG4 (+TG5 for Route A), TH2′, TH3, TH5] Under the hypotheses above, the continuum limit satisfies \(G_{ab}+\Lambda g_{ab} = (2\pi/\eta)\,T_{ab}\), with \(\Lambda\) an **integration constant** of the Bianchi step.

**Theorem TH7 (identification of \(G\)).** [TH6] Matching to \(G_{ab}+\Lambda g_{ab}=8\pi G\,T_{ab}\) forces \(\eta = 1/4G\), i.e. \(S = A/4G\), and therefore
\[
\boxed{\;G \;=\; \frac{1}{4\,s_0\,\eta_N}\;}
\]
**Newton's constant is the reciprocal of the ground configuration's share density across a cut**, weighted by the entropy per severed share. Gravity is weak exactly to the extent that the vacuum shares densely.

**What TH7 does and does not buy.** It converts \(G\) from a free constant into a **property of the ground configuration** — a genuine structural relocation, and the sharpest thing this layer says. It does **not compute** \(\eta_N\): that needs the continuum limit TG2 actually solved, not assumed. Listing it as computed would be void under charter §5.

**Where \(\Lambda\) went (docs/05 §3.5 revisited).** Both routes source curvature from *variations* of relative entropy. The ground configuration's own cost is the reference and cancels identically — so the naive "sum the vacuum modes' energy and gravitate it" computation is not a computation this framework performs. \(\Lambda\) appears instead as a constant of integration. That upgrades §3.5 from **no purchase** to **reformulation**: the question "why doesn't vacuum energy gravitate at its naive scale?" is dissolved (only relative quantities source), while "why is \(\Lambda\) the observed size?" remains **no purchase** — an integration constant is not a prediction.

---

## 6. TH8 — The equivalence principle, derived (contention 2 closed)

Contention 2 has stood as: free-fall universality *forces* \(b_{\rm grav}=m_{\rm struct}\,g\), and "nothing in the working model derives it; it is a consistency requirement imposed by observation" (docs/02 §6). The TG layer derives it.

**Setup.** Under TG1, selection on the floor minimizes the free cost \(F = \langle C\rangle - \Theta S\), so the effective bias splits:
\[
b_{\rm eff} = \frac{\partial F}{\partial x} = \underbrace{\frac{\partial\langle C\rangle}{\partial x}}_{\text{ordinary bias}} \;-\; \underbrace{\Theta\,\frac{\partial S}{\partial x}}_{\displaystyle \;\equiv\; -\,b_{\rm grav}} .
\]

**Theorem TH8 (weak equivalence principle).** [WM3, TH2, TH2′, TG1, TG2] Displacing a cluster by \(\delta x\) toward a horizon converts a fraction of its own shares into cut-crossing shares, at a rate proportional to its total share count: \(\delta N_{\rm cross} = (n_{\rm share}/\lambda)\,\delta x\) with \(\lambda\) the ground share separation. Hence
\[
b_{\rm grav} = \Theta\,s_0\,\frac{n_{\rm share}}{\lambda} = m_{\rm struct}\,g, \qquad g \equiv \frac{\Theta\,s_0}{\alpha_m \lambda},
\]
and therefore \(g_{\rm eff}=b_{\rm grav}/m_{\rm struct}=g\) is **cluster-independent** in the limit \(\varepsilon\ll\alpha_m n_{\rm share}\) (exactly, if \(\varepsilon=0\); see TH8-ε). ∎

**Why it works — one counter, two roles.** WM3 says inertia is a share count. TH2 says horizon entropy is a share count. They are the *same counter*. The equivalence principle is the statement that the quantity resisting sequential change and the quantity measuring severed sharing cannot differ, because there is only one of them. No coincidence remains to explain.

**Corollary TH8-ε (the floor predicts a residual violation).** WM3's inertia is \(m_{\rm struct}=\alpha_m n_{\rm share}+\varepsilon\), but the entropic bias of TH8 is proportional to \(n_{\rm share}\) with **no floor** — a shareless structure severs nothing. Hence
\[
g_{\rm eff}(n) = g\,\frac{\alpha_m n}{\alpha_m n + \varepsilon}, \qquad
\eta_E(n_1,n_2) \simeq \frac{\varepsilon}{\alpha_m}\left|\frac{1}{n_1}-\frac{1}{n_2}\right| .
\]
TH8 is therefore **exact only in the limit \(\varepsilon \ll \alpha_m n\)**: the framework predicts a WEP violation suppressed by inverse share count — i.e. by inverse mass, *larger for lighter bodies*. This is a genuine prediction-shape and a genuine caveat, and it is checked numerically (`sim/thermo_gravity.py` §6c: measured \(\eta_E\) matches \(\varepsilon\alpha_m^{-1}|1/n_1-1/n_2|\) to three digits; with \(\varepsilon=0\) the spread is exactly zero, so the floor is the *only* source of non-universality). Its empirical force depends entirely on whether \(\varepsilon\) is a real floor or a regularization convenience — the framework does not currently say which, and \(\varepsilon\) has never been independently operationalized (docs/08 §3's standing debt).

**Corollary TH8′ (Eötvös experiments test CC′).** If the dynamical floor were stratified (¬CC′), structure classes charged differently on a higher stratum would contribute to \(m_{\rm struct}\) and to \(\partial S/\partial x\) in different proportions, and would fall at different rates. The measured Eötvös parameter \(\eta_E \lesssim 10^{-15}\) (MICROSCOPE) is therefore a direct bound on floor stratification — a second empirical constraint on contention 8, independent of TS2's decoherence argument, and much sharper.

**Corollary TH8″ (why gravity is attractive and universal).** Attractive: the entropic term always points toward larger \(S\), and by TH9 that is toward larger horizon area. Universal: every structure has shares (WM3's \(\varepsilon\) floor is the only shareless case), so nothing is uncoupled — the universality of gravitational coupling is the macroscopic face of CC′'s one-currency floor.

**Newtonian cross-check (not load-bearing).** With a holographic screen of area \(A=4\pi r^2\), \(N=A/G\) (TH7), equipartition \(E=\tfrac12 N\Theta\) with \(E=M\), and \(\delta S = 2\pi m\,\delta x\) (TH8's rate in Compton units), the entropic force is \(F=\Theta\,\partial S/\partial x = GMm/r^2\). This reproduces Verlinde's argument inside the framework. It is a **consistency check only**: §5 already delivered the full Einstein equation, whose Newtonian limit is the inverse-square law by standard means, and the screen/equipartition ansatz is considerably weaker than TG1–TG4. TH8 itself does **not** depend on it — it needs only "entropy gradient \(\propto\) share count."

**Contention 2 disposition.** *Resolved conditionally.* \(b_{\rm grav}\propto m_{\rm struct}\) is derived from TG1–TG2 + WM3 + TH2, not imposed. The residue is that TG2 is assumed, not solved. The scope note on T6 is unchanged and now explained rather than stipulated: T6's inverse-ratio applies to cluster-*independent* bias precisely because a gravitational bias is *not* cluster-independent — it is proportional to the very counter T6 divides by.

---

## 7. TH9–TH11 — The second law, the area theorem, and merging black holes

### TH9 — Generalized second law

**Theorem TH9.** [TH4, TH3, TG3, TG4] For cuts \(\chi_1 \prec \chi_2\) on the same horizon, the generalized entropy \(S_{\rm gen}(\chi) = \eta A(\chi) + S_{\rm out}(\chi)\) satisfies \(S_{\rm gen}(\chi_2) \ge S_{\rm gen}(\chi_1)\).

*Proof.* As the cut advances up the horizon, the exterior algebra shrinks: \(\mathcal{A}_2 \subset \mathcal{A}_1\) (SM-B3 again — causal exclusion is stable). Writing \(S_{\rm gen}(\chi_i) = \text{const} - S_{\rm rel}(\rho_i\Vert\sigma_i)\) (Casini's identification of generalized entropy with relative entropy against the boost-thermal reference — the area term is the \(\Delta\langle K\rangle\) piece, TH5), monotonicity of \(S_{\rm rel}\) under the inclusion \(\mathcal{A}_2\subset\mathcal{A}_1\) — which is TH4 — gives the result. ∎

**Reading.** The second law here is *not* an extra postulate and *not* a coarse-graining story about ignorance. It is TH4, which is the event trichotomy, which is O4 plus the HQ layer. **Thermodynamic irreversibility and structural projection are the same fact.**

### TH10 — Area theorem and the merger inequality

**Corollary TH10a (area theorem).** [TH9] With quiescent exteriors (\(S_{\rm out}\) bounded), \(\eta\,\Delta A \ge 0\): horizon area is non-decreasing.

The positivity driving the focusing — the null energy condition in the continuum statement — is, in this layer, the non-negativity of the WM2 counters transported through TG4: \(S_{\rm rel}\ge 0\) and its monotonicity are what the averaged null energy condition expresses in the geometric limit. There is no separate energy-condition postulate.

**Corollary TH10b (merging black holes).** [TH10a, SM-B3] Let two holes with horizon areas \(A_1, A_2\) merge. Trace the *final* event horizon back to a cut early enough that it has two disjoint components; its area is \(A_1+A_2\). Monotonicity along the horizon then gives
\[
\boxed{\;A_f \;\ge\; A_1 + A_2 \quad\Longleftrightarrow\quad S_f \;\ge\; S_1 + S_2\;}
\]
The merged hole is necessarily bigger, and the reverse process — one hole fissioning into two — is **thermodynamically forbidden**, not merely unlikely.

**Quantitative content.** For Schwarzschild holes, \(A = 16\pi G^2M^2\), so \(A_f \ge A_1+A_2\) reads \(M_f \ge \sqrt{m_1^2+m_2^2}\), bounding the radiated fraction:
\[
f_{\rm rad} \;=\; 1 - \frac{M_f}{m_1+m_2} \;\le\; 1 - \frac{\sqrt{m_1^2+m_2^2}}{m_1+m_2} \;\xrightarrow[\;m_1=m_2\;]{}\; 1-\tfrac{1}{\sqrt2} \approx 29.3\%.
\]
Checked against four observed mergers in `sim/thermo_gravity.py` §5 (GW150914, GW151226, GW170814, GW190521): horizon area rises by 42–56\% while the radiated fraction is 4–6\%, an order of magnitude inside the ceiling. GW150914 radiates \(\approx4.7\%\) with area up \(\approx56\%\). The spin-corrected Kerr constraint \(2M_f^2(1+\sqrt{1-\chi_f^2}) \ge 4(m_1^2+m_2^2)\) is also checked and also satisfied.

**Corollary TH10c (black-hole first law).** [TG3, TH7] With \(T=\kappa/2\pi\) and \(S=A/4G\), \(dM = T\,dS\) holds identically for Schwarzschild (\(T=1/8\pi GM\), \(S=4\pi GM^2\)); \(T_H\) is the Unruh temperature of the horizon's own modular flow. Verified numerically in §5 of the sim.

**The subadditivity objection, answered.** Entanglement entropy is *sub*additive (\(S(AB)\le S(A)+S(B)\)) while TH10b is *super*additive — a real tension worth stating plainly. The resolution is that the two statements are about different objects. Subadditivity compares two regions of **one state at one time**; TH10b compares **two cuts of one horizon at two times**. Interior–interior shares between the pre-merger holes genuinely drop out of the final cut — that is the subadditive effect, and it is real — but it is over-compensated by focusing driven by the infalling modular energy. TH10b is not a counting identity; it is a dynamical consequence of positivity (TH4/TH9). Anyone reading TH2 as "entropy is literally the pairwise share count, so the second law is combinatorics" has the argument wrong.

### TH11 — Bekenstein bound

**Corollary TH11.** [TH5] \(S_{\rm rel}\ge0\) is exactly \(\Delta S \le \Delta\langle K\rangle\); for a region of size \(R\) with TG3/TG4's modular Hamiltonian this is the Bekenstein bound \(S - S_{\rm gnd} \le 2\pi E R\). ∎ (Casini's argument, imported; what the framework supplies is that the *relevant* entropy in it was relative all along — §1.)

---

## 8. The entropy of quantum fields, manifesting

The user-facing form of the thesis: *where does the entropy of quantum fields show up?*

**Answer: as the geometry.** There are not two entropies — a divergent field-theoretic one across a surface, plus a separate gravitational \(A/4G\). There is one cut share count. Splitting it into "\(A/4G\) plus matter entropy" is a **choice of reference**: which shares are called ground and which are called excitation. The invariant is \(S_{\rm gen}\), and the framework's three statements about it are:

1. Its **divergence is not physical** — it is WM1 granularity (TH1, item 3). QFT's cutoff-dependent area-law divergence and the cutoff-dependence of \(G\) are one dependence, seen twice; here they cancel by construction because \(G\) *is* \(1/4s_0\eta_N\) (TH7).
2. Its **area law is structural** (TH2), not an accident of the vacuum's short-distance behavior.
3. Its **monotonicity is the event trichotomy** (TH4), so entropy production is located exactly where the theory already located non-unitarity.

**Research program (not a claim): the quantum extremal surface.** The framework's own selection principle T10 chooses a cut by minimizing structural cost; the modern holographic prescription chooses a surface by extremizing \(S_{\rm gen}\). Under TH2′ these are the same *shape* of variational problem over the same object (cuts of a term). Whether T10's argmin reproduces the QES prescription — and with it the Page curve — is a definable next step, and nothing here claims it does.

---

## 9. Adversarial pressure

| Pressure | Response |
|---|---|
| **Entropic gravity destroys interference** (Kobakhidze: a thermal origin for gravity should decohere neutrons in COW/qBounce; it does not) | The gravitational bias here is a **floor** bias, and by Q1/T17 admissible maps are functions of structure alone. A bias that does not resolve the branches' share structure acts identically on every class of a coherent set — a common factor, no which-path record, no decoherence. Decoherence in this framework needs WM4's environment-crossing shares raising the maintain ledger, which a uniform field does not supply. **Prediction shape:** gravitationally induced decoherence requires gradients that structurally distinguish the branches; uniform fields give none. Shape only — no rate |
| **Subadditive vs superadditive** | §7, TH10b's note. Real tension, standard resolution, stated rather than hidden |
| **"An equation of state is not a theory of gravity"** (the standard critique of Jacobson) | Conceded in full. TH6 says the Einstein equation is the equation of state of the structural degrees of freedom. It does not quantize the metric, does not fix higher-curvature corrections (which change \(\eta\)), and Route B's local-equilibrium assumption is known to need care in genuinely non-equilibrium settings |
| **Circularity** (TG3 presupposes QFT-on-curved-spacetime results) | Partly conceded. TG3 and TG4 are postulates precisely because they are the imported content; the derivation exhibits **mutual determination**, not construction from nothing. What is not circular: TH1, TH2, TH3, TH4, TH8 — these use only framework-internal resources |
| **TG2 does everything** | Yes. Stated in the method rule and repeated here: geometry is assumed, not derived, and the causal-set continuum problem (dimension, local Lorentz) is inherited unsolved (docs/15 §4). If TG2 fails, §§5–7 fail |

---

## 10. Non-purchases (fixed ledger, charter §5)

The TG layer has **no resources** for: the value of \(\eta_N\) (hence of \(G\)); the value of \(\Lambda\); spacetime dimension; local Lorentz invariance; a quantum theory of the metric or a graviton; singularity resolution; the black-hole information paradox or the Page curve (§8 defines a probe, claims nothing); Hawking radiation's spectrum beyond \(T=\kappa/2\pi\); dark energy dynamics; MOND-like phenomenology. Claiming any of these without new postulates is void.

---

## 11. Dependency map

```
WM1,WM2 ──> TH2 area law (forced in WM: the S-counter is a boundary quantity)
RM1,CI4,WM1 ──> TH1 only relative entropy is observable
F3/O4,SB4,SM-B3 ──> TH3 horizons leave real inaccessible structure
T15,T13',T16',T14' ──> TH4 monotonicity (= data processing; all production at projection)
TG1 + TH2 ──> TH2' entropy per severed share; K = C_maintain/Θ
TH2',TG1 ──> TH5 first law  δS = δ⟨K⟩

TH2',TH3,TH5 + TG1,TG2,TG3,TG4        ──> TH6 Einstein eq (Route B, Clausius)
TH2',TH3,TH5 + TG1,TG2,TG3,TG4,TG5    ──> TH6 Einstein eq (Route A, relative entropy)
TH6 ──> TH7  G = 1/(4 s0 ηN)

WM3 + TH2 + TG1,TG2 ──> TH8 weak equivalence principle  [closes contention 2]
                     └─> TH8' Eötvös bounds floor stratification (contention 8)

TH4 ──> TH9 generalized second law
     └─> TH10a area theorem ──> TH10b  A_f ≥ A_1 + A_2  (mergers; fission forbidden)
     └─> TH10c dM = T dS
TH5 ──> TH11 Bekenstein bound
```

## 12. Executable

`sim/thermo_gravity.py` — every section below runs and prints its check:

1. **TH2**: `C_isolate` on real expression trees; interior grown 100×, boundary fixed, cost constant.
2. **TH1**: \(S_{\rm rel}\) invariant under cost rescaling, cost offset, and \(k\)-fold granularity refinement; \(S\) invariant under none.
3. **TH4**: monotonicity under a unitary (free epoch), an isometry (reconfiguration), and dephasing+restriction (projection) — classical and qubit versions.
4. **TH6**: the \(\ell^4\) coefficients \(-2\pi/15\) (exact geodesic balls on \(S^3\)) and \(8\pi^2/15\) (quadrature); both routes agree on \(\eta = 1/4G\).
5. **TH10**: \(dM=T\,dS\); area theorem and the merger inequality on GW150914 / GW151226 / GW170814 / GW190521, Schwarzschild and Kerr forms, plus the radiated-fraction bound and the forbidden fission.
6. **TH8**: entropic bias \(\propto\) share count ⇒ identical accelerations for clusters of different inertia, contrasted with T6's cluster-independent-bias regime; Verlinde cross-check recovering \(GMm/r^2\).
