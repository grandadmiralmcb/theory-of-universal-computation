# 02 — Dynamics (Structural Sequential Calculus)

Every derivation below names the operation being performed. Operations are drawn from the reduced primitives (`app`, `abs`, `pair`/`proj`, `eq`, `reduce`, `share`) together with the derived structural counters and the preferential low-disruption selection principle.

---

## 1. Structural cost of a reduction step

**Operation: structural-cost evaluation**

Given a reduction step \(E \xrightarrow{s} E'\) performed by `reduce` under strategy \(s\):

| Counter | Definition | Primitive source |
|---------|------------|------------------|
| \(S\) | number of `share` nodes whose shared content is broken or duplicated | `share` |
| \(B\) | net change in open binding sites | `abs` / `app` |
| \(D\) | 1 if residual fails `eq`, else 0 | `eq` |

\[
C(E \xrightarrow{s} E') = \alpha S + \beta B + \gamma D \qquad (\alpha,\beta,\gamma > 0)
\]

**Operation name:** `structural_cost`

---

## 2. Velocity-form cost for a sequential cluster

**Operation: sequential-state abstraction**

A high-share-density cluster is abstracted to a sequential state \((x, v)\) maintained by a local evaluator. A proposed change of velocity \(\delta v\) is assigned cost by the same structural principle:

\[
C(\delta v) = \tfrac12 m_{\rm struct}\,(\delta v)^2 + b_{\rm struct}\,\delta v
\]

where

- **Operation `m_struct`:** \(m_{\rm struct} = \langle S(\delta x = 1)\rangle\) (average share disruption for unit sequential change; in the toy model proportional to share density).
- **Operation `b_struct`:** excess disruption imposed by a persistent bias context on steps against the preferred direction.

**Operation name:** `velocity_cost`

---

## 3. Preferential selection of the lowest-cost update

**Operation: preferential low-disruption sequentialization**

The evaluator selects the velocity change that minimizes structural cost:

\[
\delta v^* = \arg\min_{\delta v}\, C(\delta v) = -\frac{b_{\rm struct}}{m_{\rm struct}}
\]

(analytic minimum of the quadratic). This is the discrete embodiment of the dynamical axiom.

**Operation name:** `preferential_select` (equivalently `argmin_C`)

---

## 4. Discrete sequential update

**Operation: sequential tick**

At tick duration \(\tau\):

\[
\begin{align*}
v_{n+1} &= v_n + \delta v^*\,\tau = v_n - \frac{b_{\rm struct}}{m_{\rm struct}}\,\tau,\\
x_{n+1} &= x_n + v_{n+1}\,\tau
\end{align*}
\]

(the second line may use \(v_n\) or the updated velocity according to integrator convention; the simulator uses the updated velocity).

**Operation name:** `sequential_tick`

---

## 5. Continuum limit under constant bias

**Operation: continuum limit**

Take \(\tau \to 0\), \(n \to \infty\) with \(t = n\tau\) fixed:

\[
\frac{dv}{dt} = -\frac{b_{\rm struct}}{m_{\rm struct}}, \qquad \frac{dx}{dt} = v.
\]

Equivalently:

\[
\frac{d^2 x}{dt^2} = -\frac{b_{\rm struct}}{m_{\rm struct}} = -g_{\rm eff}.
\]

**Operation name:** `continuum_limit`

Constant acceleration is recovered solely from structural counts and preferential selection. No external numerical cost primitive is required.

---

## 6. Integration — elementary projectile motion

**Operation: analytic integration**

With initial data \(x(0)=h\), \(v(0)=v_0\) and constant \(g_{\rm eff}\):

\[
\begin{align*}
v(t) &= v_0 - g_{\rm eff}\,t,\\
x(t) &= h + v_0 t - \tfrac12 g_{\rm eff}\,t^2.
\end{align*}
\]

Landing time (positive root of \(x(t)=0\)):

\[
t_{\rm land} = \frac{v_0 + \sqrt{v_0^2 + 2 g_{\rm eff} h}}{g_{\rm eff}}.
\]

**Operation name:** `integrate_projectile`

---

## 7. Position-dependent bias (structural potential)

**Operation: bias-context evaluation**

Replace constant \(b_{\rm struct}\) by a function of sequential position:

\[
b_{\rm struct}(x) = \frac{\partial V_{\rm struct}}{\partial x}
\]

(or any tabulated excess disruption that varies with \(x\)). The continuum equation becomes

\[
m_{\rm struct}\,\ddot{x} = -b_{\rm struct}(x) = -\frac{\partial V_{\rm struct}}{\partial x}.
\]

**Operation name:** `position_dependent_bias` (or `evaluate_b_at`)

This is Newton’s second law for a conservative force. No new primitive is introduced; only the bias context is allowed to depend on the sequential parameter already maintained by the evaluator.

---

## 8. Harmonic case

**Operation: harmonic bias specialization**

Take \(V_{\rm struct}(x) = \tfrac12 k x^2\). Then

\[
b(x) = kx, \qquad \ddot{x} = -\frac{k}{m_{\rm struct}}x.
\]

Angular frequency and period:

\[
\omega = \sqrt{\frac{k}{m_{\rm struct}}}, \qquad T = \frac{2\pi}{\omega}.
\]

**Operation name:** `harmonic_potential`

---

## 9. Structural energy analogue

**Operation: energy accounting**

Define

\[
T = \tfrac12 m_{\rm struct}\,v^2, \qquad E = T + V_{\rm struct}(x).
\]

Under purely position-dependent bias (no explicit velocity dependence in the cost beyond the inertial term) and in the continuum limit, \(E\) is conserved. In the discrete simulator residual drift is an integrator artifact (semi-implicit Euler), not a structural dissipation.

**Operation name:** `structural_energy`

---

## 10. Executable confirmation

`sim/toy_simulator.py` implements:

- `structural_cost` / `velocity_cost`
- `preferential_select` (analytic `dv*`)
- `sequential_tick` with rate integration \(v \leftarrow v + \mathrm{dv}^*\cdot\mathrm{dt}\)
- `position_dependent_bias` via callable potential/force
- `structural_energy` tracking

Confirmed results:

| Experiment | Prediction | Observation |
|------------|------------|-------------|
| Constant bias, two share densities | \(a_1/a_2 = m_2/m_1\) | exact match |
| Harmonic oscillator, 3 periods | bounded oscillation, \(E\) conserved | relative energy drift \(\sim 6\times 10^{-3}\) |

---

## 11. Coherence

**Operation: coherence evaluation**

\[
\kappa \sim \frac{1}{1+\langle C\rangle_{\rm recent}}
\]

High \(\kappa\) = successful maintenance of low-disruption sequential projection. Classical regimes are high-\(\kappa\) regimes.

**Operation name:** `coherence_kappa`

---

## Status

**Closed**
- Constant-bias Newtonian regime (projectile motion).
- Position-dependent bias → conservative one-dimensional mechanics (harmonic verified).
- Inverse-acceleration relation under identical bias.

**Open extensions (same structural principle)**
- Multi-cluster mutual disruption (interaction forces).
- Velocity-dependent residual disruption (drag).
- Multi-dimensional sequential parameters.
- Continuum field limits of many weakly coupled excitations.
