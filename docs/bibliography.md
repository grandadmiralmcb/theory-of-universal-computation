# Annotated Bibliography

*Status: Stable*

Grouped by the tradition each source anchors ([00-overview.md §5](00-overview.md)). Annotations state what the framework takes from each source. Citation style: author year, as used inline throughout the documents.

## Term rewriting and its metatheory

- **Baader, F. & Nipkow, T. (1998).** *Term Rewriting and All That.* Cambridge University Press. — The framework's default reference for foundations ([01](01-foundations.md)) and semantics ([03](03-semantics.md)): term algebra, positions, critical pairs, undecidability results.
- **Terese (2003).** *Term Rewriting Systems.* Cambridge Tracts in Theoretical Computer Science 55. — Encyclopedic treatment; source for abstract rewriting, orthogonality, and strategy theory.
- **Newman, M. H. A. (1942).** "On theories with a combinatorial definition of 'equivalence'." *Annals of Mathematics* 43(2). — Newman's Lemma (Theorem 3.3 of [03](03-semantics.md)).
- **Knuth, D. E. & Bendix, P. B. (1970).** "Simple word problems in universal algebras." In *Computational Problems in Abstract Algebra.* Pergamon. — Critical pairs and completion.
- **Huet, G. (1980).** "Confluent reductions: abstract properties and applications to term rewriting systems." *JACM* 27(4). — The Critical Pair Lemma in its modern form.
- **Rosen, B. K. (1973).** "Tree-manipulating systems and Church–Rosser theorems." *JACM* 20(1). — Confluence of orthogonal systems (Remark 3.5 of [03](03-semantics.md)).
- **Dershowitz, N. (1982).** "Orderings for term-rewriting systems." *Theoretical Computer Science* 17(3). — Reduction orders for termination proofs.
- **Post, E. L. (1943).** "Formal reductions of the general combinatorial decision problem." *American Journal of Mathematics* 65(2). — Production systems; the dynamical claim's earliest general form.
- **Post, E. L. (1947).** "Recursive unsolvability of a problem of Thue." *Journal of Symbolic Logic* 12(1). — String-rewriting simulation of machines, ancestor of Theorem 2.1 of [04](04-universality.md).
- **Markov, A. A. (1954).** *Theory of Algorithms.* Academy of Sciences of the USSR. — Normal algorithms; rewriting as a complete model of computation.

## λ-calculus and combinatory logic

- **Schönfinkel, M. (1924).** "Über die Bausteine der mathematischen Logik." *Mathematische Annalen* 92. — The S and K combinators; minimality of the universal basis ([04 §3](04-universality.md)).
- **Church, A. (1936).** "An unsolvable problem of elementary number theory." *American Journal of Mathematics* 58(2). — λ-definability and undecidability; one pillar of P5.
- **Church, A. & Rosser, J. B. (1936).** "Some properties of conversion." *Transactions of the AMS* 39. — The original confluence theorem.
- **Turing, A. M. (1936).** "On computable numbers, with an application to the Entscheidungsproblem." *Proc. LMS* s2-42. — The machine model; undecidability of the halting problem.
- **Turing, A. M. (1937).** "Computability and λ-definability." *Journal of Symbolic Logic* 2(4). — Equivalence of the models (Theorem 4.1 of [04](04-universality.md)).
- **Curry, H. B. (1930).** "Grundlagen der kombinatorischen Logik." *American Journal of Mathematics* 52. — Combinatory completeness.
- **Curry, H. B. & Feys, R. (1958).** *Combinatory Logic, Vol. I.* North-Holland. — Standardization; bracket abstraction.
- **Barendregt, H. P. (1984).** *The Lambda Calculus: Its Syntax and Semantics.* Revised ed., North-Holland. — The framework's reference for λ and its translation to combinators.
- **Hindley, J. R. & Seldin, J. P. (2008).** *Lambda-Calculus and Combinators: An Introduction.* Cambridge University Press. — Accessible treatment of [04 §§3–4](04-universality.md).
- **Abadi, M., Cardelli, L., Curien, P.-L. & Lévy, J.-J. (1991).** "Explicit substitutions." *Journal of Functional Programming* 1(4). — Making β locally finite ([04 §4](04-universality.md)).
- **Lévy, J.-J. (1978).** *Réductions correctes et optimales dans le lambda-calcul.* Thèse d'État, Paris VII. — Redex families; background for OP-3.
- **O'Donnell, M. J. (1977).** *Computing in Systems Described by Equations.* LNCS 58, Springer. — Normalizing strategies for orthogonal systems.

## Computability, complexity, and information

- **Kleene, S. C. (1952).** *Introduction to Metamathematics.* North-Holland. — General recursion theory background.
- **Solomonoff, R. J. (1964).** "A formal theory of inductive inference, Parts I–II." *Information and Control* 7. — Universal priors; representation invariance's first appearance.
- **Kolmogorov, A. N. (1965).** "Three approaches to the quantitative definition of information." *Problems of Information Transmission* 1(1). — The invariance theorem behind P6's modeling.
- **Li, M. & Vitányi, P. (2019).** *An Introduction to Kolmogorov Complexity and Its Applications.* 4th ed., Springer. — Standard AIT reference.
- **van Emde Boas, P. (1990).** "Machine models and simulations." In *Handbook of Theoretical Computer Science, Vol. A.* Elsevier. — The invariance thesis; polynomial interconvertibility of reasonable models ([04 §5](04-universality.md), OP-4).
- **Accattoli, B. & Dal Lago, U. (2016).** "(Leftmost-outermost) beta reduction is invariant, indeed." *Logical Methods in Computer Science* 12(1). — Cost realism for λ; the model for OP-4.
- **Bernstein, E. & Vazirani, U. (1997).** "Quantum complexity theory." *SIAM Journal on Computing* 26(5). — Quantum universality and the cost of classical simulation (OP-6).
- **Cook, M. (2004).** "Universality in elementary cellular automata." *Complex Systems* 15(1). — Rule 110; universality of minimal CA ([04 §5](04-universality.md)).
- **Lafont, Y. (1990).** "Interaction nets." *POPL '90.* — A neighboring graph-based universal formalism.
- **Ehrig, H., Ehrig, K., Prange, U. & Taentzer, G. (2006).** *Fundamentals of Algebraic Graph Transformation.* Springer. — Graph rewriting, the P2-denying neighbor.
- **Milner, R. (1989).** *Communication and Concurrency.* Prentice Hall. — Bisimulation (rung 2 of [03 §6](03-semantics.md)).
- **Park, D. (1981).** "Concurrency and automata on infinite sequences." *Theoretical Computer Science* (5th GI-Conference). — Origin of bisimilarity.
- **Birkhoff, G. (1935).** "On the structure of abstract algebras." *Proc. Cambridge Phil. Soc.* 31. — Free algebras; the structural claim's algebraic root.

## Digital physics, pancomputationalism, and critics

- **Zuse, K. (1969).** *Rechnender Raum.* Vieweg. (English: *Calculating Space*, MIT translation.) — The first developed universe-as-computation proposal.
- **Fredkin, E. (1990).** "Digital mechanics." *Physica D* 45. — Reversible CA as fundamental physics; compared in [05 §3](05-ontology.md).
- **Wheeler, J. A. (1990).** "Information, physics, quantum: the search for links." In *Complexity, Entropy, and the Physics of Information.* Addison-Wesley. — "It from bit."
- **Wolfram, S. (2002).** *A New Kind of Science.* Wolfram Media. — Simple-programs methodology; discussed and partially declined in [05 §3](05-ontology.md).
- **Deutsch, D. (1985).** "Quantum theory, the Church–Turing principle and the universal quantum computer." *Proc. Royal Society A* 400. — The Church–Turing–Deutsch principle ([05 §3, §5](05-ontology.md)).
- **Putnam, H. (1988).** *Representation and Reality.* MIT Press. — The triviality theorem; Objection I of [05 §4](05-ontology.md).
- **Searle, J. R. (1992).** *The Rediscovery of the Mind.* MIT Press. — "The wall implements WordStar"; companion to Putnam's objection.
- **Chalmers, D. J. (1996).** "Does a rock implement every finite-state automaton?" *Synthese* 108. — The counterfactual reply the framework builds on ([05 §4](05-ontology.md), OP-5).
- **Copeland, B. J. (1996).** "What is computation?" *Synthese* 108. — Honest-labeling constraints on implementation claims.
- **Piccinini, G. (2015).** *Physical Computation: A Mechanistic Account.* Oxford University Press. — The mechanistic account; principal modern interlocutor for [05](05-ontology.md).
- **Ladyman, J. & Ross, D. (2007).** *Every Thing Must Go: Metaphysics Naturalized.* Oxford University Press. — Ontic structural realism, the interpretive thesis's philosophical home ([05 §1, §6](05-ontology.md)).
- **Bekenstein, J. D. (1981).** "Universal upper bound on the entropy-to-energy ratio for bounded systems." *Physical Review D* 23. — Finite entropy of bounded regions ([05 §5](05-ontology.md)).
- **'t Hooft, G. (1993).** "Dimensional reduction in quantum gravity." arXiv:gr-qc/9310026. — Holographic principle, original form.
- **Susskind, L. (1995).** "The world as a hologram." *Journal of Mathematical Physics* 36. — Holographic principle, developed.
- **Bombelli, L., Lee, J., Meyer, D. & Sorkin, R. D. (1987).** "Space-time as a causal set." *Physical Review Letters* 59. — Discrete spacetime program cited in [05 §5](05-ontology.md).
- **Müller, M. (2010).** "Stationary algorithmic probability." *Theoretical Computer Science* 411. — Limits of machine-invariance; prior art for OP-1.
