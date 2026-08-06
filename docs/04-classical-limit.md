# 04 — Classical Limit

## Expression-theoretic mapping of macroscopic objects

- **Ball (or any macroscopic body)** — stable, high-rewrite-resistance expression cluster.
- **Mass** — quantitative rewrite resistance (minimal cost required to alter sequential trajectory by a unit amount).
- **Position / height / direction** — parameters of the local sequential trajectory and binding context relative to other stable clusters (especially the ground).
- **Throwing** — finite-duration, high-intensity constraint injection that alters the initial sequential trajectory.
- **Gravity / ambient bias** — persistent low-cost constraint field that systematically biases sequential trajectories of massive clusters.
- **Landing** — intersection of the ball-cluster trajectory with the ground-cluster trajectory.

## Prediction procedure (local evaluator)

1. Maintain a sequential model of the relevant clusters under a consistent binding context.
2. Record initial trajectory parameters after the throwing constraint.
3. Know the ambient bias strength and the rewrite resistance of the cluster (from prior high-\(\kappa\) experience).
4. Simulate (via repeated `force`) the lowest-cost sequential evolution until intersection with the ground cluster.
5. Because the region is high-stability and high-\(\kappa\), deviations are suppressed; the prediction is reliable within ordinary precision.

## Derivation status

The concrete cost function of document 02 together with the continuum-limit argument already yields the quantitative parabolic trajectory under constant bias. Variable bias, drag, spin, and multi-body effects remain to be developed as additional cost terms and secondary rewrite events.
