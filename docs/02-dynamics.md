# 02 — Dynamics

## Concrete Cost Function (minimal working version)

For a single high-resistance expression cluster characterized by inertia parameter \(m > 0\) and sequential trajectory parameter \(x\), a change \(\delta x\) is assigned cost

\[
C(\delta x) = \frac12 m\, (\delta x)^2 + b\, x\, \delta x
\]

(or, in velocity form, \(C(\delta v) = \frac12 m\, (\delta v)^2 + b\, \delta v\)).

- \(\frac12 m (\delta x)^2\) — inertial cost of changing sequential state.
- Linear bias term — constant ambient constraint of strength \(b\).

Cost is zero only for the null change and increases with both inertia and magnitude of change.

## Discrete Lowest-Cost Dynamics

Treating the state as the pair \((x_n, v_n)\) and minimizing cost at each tick of duration \(\tau\) yields the updates

\[
\begin{align*}
v_{n+1} &= v_n - \frac{b}{m}\,\tau,\\
x_{n+1} &= x_n + v_n\,\tau.
\end{align*}
\]

## Continuum Limit

In the limit \(\tau \to 0\), \(n\to\infty\) with \(t = n\tau\) fixed, the discrete system converges to

\[
\frac{dv}{dt} = -\frac{b}{m}, \qquad \frac{dx}{dt} = v,
\]

or equivalently the second-order equation

\[
\frac{d^2 x}{dt^2} = -\frac{b}{m} = -g_{\rm eff}.
\]

This is constant acceleration. The effective gravitational acceleration is the positive constant \(g_{\rm eff} = b/m\) (sign conventional).

## Integration — Parabolic Trajectory

With initial conditions \(x(0) = h\), \(v(0) = v_0\):

\[
\begin{align*}
v(t) &= v_0 - g_{\rm eff}\, t,\\
x(t) &= h + v_0 t - \frac12 g_{\rm eff}\, t^2.
\end{align*}
\]

Landing time (positive root of \(x(t)=0\)) is

\[
t_{\rm land} = \frac{v_0 + \sqrt{v_0^2 + 2 g_{\rm eff} h}}{g_{\rm eff}}.
\]

This recovers elementary projectile motion as the continuum limit of lowest-cost sequential evaluation under constant bias.

## Coherence Measure \(\kappa\)

\(\kappa\) quantifies the predictive consistency and narrative continuity of a local sequential model. High \(\kappa\) is dynamically favored. Concrete numerical realizations (inverse error accumulation, mutual information between successive states, residual amplitude dispersion, etc.) remain to be fixed and calibrated.
