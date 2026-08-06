# 02 — Dynamics (Structural Sequential Calculus)

## Structural Cost Proxy

Numerical cost is not primitive. For a reduction step \(E \xrightarrow{s} E'\) the structural disruption counts are:

- \(S\) = number of `share` nodes whose shared content is broken or duplicated
- \(B\) = net change in open binding sites
- \(D\) = 1 if the residual fails `eq` under the current strategy, else 0

\[
C = \alpha S + \beta B + \gamma D \qquad (\alpha,\beta,\gamma > 0)
\]

All three quantities are readable from the reduced primitives alone.

## Velocity-form cost for sequential clusters

For a high-resistance cluster whose sequential state is tracked by parameter \(x\) and velocity \(v\), a change of velocity \(\delta v\) is assigned structural cost

\[
C(\delta v) = \frac12 m_{\rm struct}\,(\delta v)^2 + b_{\rm struct}\,\delta v
\]

where

- \(m_{\rm struct} = \langle S(\delta x=1)\rangle\) (or a direct function of share density in the toy model),
- \(b_{\rm struct}\) = excess disruption imposed by a persistent bias context on steps against the preferred direction.

Minimizing \(C\) with respect to \(\delta v\) immediately yields the optimal update

\[
\delta v^* = -\frac{b_{\rm struct}}{m_{\rm struct}}.
\]

## Discrete sequential dynamics

At each tick of duration \(\tau\):

\[
\begin{align*}
v_{n+1} &= v_n + \delta v^* = v_n - \frac{b_{\rm struct}}{m_{\rm struct}}\,\tau,\\
x_{n+1} &= x_n + v_n\,\tau.
\end{align*}
\]

## Continuum limit (classical Newtonian regime)

In the joint limit \(\tau\to 0\), \(n\to\infty\) with \(t=n\tau\) fixed:

\[
\frac{dv}{dt} = -\frac{b_{\rm struct}}{m_{\rm struct}}, \qquad \frac{dx}{dt} = v,
\]

or

\[
\frac{d^2 x}{dt^2} = -\frac{b_{\rm struct}}{m_{\rm struct}} = -g_{\rm eff}.
\]

Constant acceleration is recovered purely from structural counts. No external numerical cost function is required.

## Integration — elementary projectile motion

With initial conditions \(x(0)=h\), \(v(0)=v_0\):

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

This is ordinary projectile motion, now derived as the continuum limit of lowest-structural-disruption sequential evaluation under constant bias.

## Executable confirmation (toy simulator)

`sim/toy_simulator.py` implements the discrete velocity-update dynamics. For two idealized clusters that differ only in share density the measured acceleration ratio satisfies

\[
\frac{a_1}{a_2} \approx \frac{m_2}{m_1}
\]
to within discretization error, confirming the inverse-acceleration prediction inside pure theory.

## Coherence

\[
\kappa \sim \frac{1}{1+\langle C\rangle_{\rm recent}}
\]

High \(\kappa\) = successful maintenance of low-disruption sequential projection. Classical regimes are high-\(\kappa\) regimes.

## Status toward richer classical limits

The constant-bias, single-cluster Newtonian regime is closed. Open extensions required for broader classical coverage:

- variable / position-dependent bias (effective potentials),
- multiple interacting clusters,
- angular / multi-dimensional sequential parameters,
- drag-like terms arising from residual share disruption that depends on velocity,
- continuum field limits of large numbers of weakly coupled excitations.
