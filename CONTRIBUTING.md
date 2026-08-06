# Contributing

This repository is a **living document**. Its value grows with corrections, sharpened objections, counterexamples, and progress on the [open problems](docs/06-open-problems.md) — in roughly that order of preciousness.

## What to contribute

**Most wanted:**
- **Errors in the Stable documents** (01–04, notation, glossary, bibliography): a wrong statement, a misattributed theorem, a proof sketch that doesn't survive expansion, a broken cross-reference. Open an issue with the document, section, and the problem; a one-line issue beats silence.
- **Objections to the Speculative document** (05): the document aims to state the strongest objections to its own thesis. If you know a stronger form of Objections I–III, or a fourth, that is a contribution to the thesis's statement, not an attack to be defended against.
- **Progress on open problems** (06): partial results, relevant literature the problem statements miss, or arguments that a problem is ill-posed (dissolving a problem counts as progress and moves it to the solved list with that status noted).
- **Bibliography accuracy**: wrong years, venues, or attributions.

**Also welcome:**
- Clarity improvements that preserve meaning (shorter sentences, better examples).
- New worked examples in 01–04.
- The reference implementation (OP-8) — coordinate via an issue first.

## How to contribute

1. **Issues** for errors, objections, and discussion. Include document + section. For objections to 05, state the objection in its strongest form you can manage.
2. **Pull requests** for concrete text changes. Keep PRs single-topic: one correction, one clarification, or one problem-entry per PR. Reference the issue if one exists.

## Editorial conventions

These keep the documents coherent; PRs that fight them will be asked to conform.

- **Status labels are honest.** Every document carries Stable / Draft / Speculative ([README](README.md#document-status-labels)). Moving material *up* the ladder (e.g., Speculative → Stable) requires that the material actually be established, with citations — not merely that it has been around a while.
- **Established vs. original is always marked.** Classical results are cited (author year, resolvable in [docs/bibliography.md](docs/bibliography.md)). Framework-original claims are labeled as postulates, framework claims, or conjectures. The reader must never have to guess which kind of sentence they are reading.
- **The Speculative document keeps its objections.** Edits to [05-ontology.md](docs/05-ontology.md) that strengthen the thesis must not weaken the statement of the objections. Deleting an objection requires refuting it, in the document, with the refutation labeled by its own epistemic status.
- **Open problem numbers are stable.** OP-n is never renumbered or reused. Solved problems move to the solved section; new problems take fresh numbers.
- **Notation goes through the notation page.** New symbols must be added to [docs/notation.md](docs/notation.md) in the same PR that introduces them.
- **GitHub-flavored Markdown only.** Unicode math in prose, code blocks for concrete rules and expressions, no LaTeX extensions — documents must render on github.com as-is.
- **Cross-references are relative links** (`[04-universality.md §3](04-universality.md)`), so they work in any clone.

## Commit and history conventions

- Commit messages: an imperative summary line scoped to the document touched, e.g. `docs/03: fix statement of Newman's Lemma`, with body text explaining *why* when the change is substantive.
- History stays linear on `main`; PRs are squash-merged unless the commit sequence itself is informative.

## Scope guardrails

To keep the project coherent, some things are out of scope regardless of quality:

- Claims of hypercomputation or of physical predictions derived from the framework (both explicitly disclaimed in [00-overview.md §4](docs/00-overview.md)).
- Promotion of the interpretive thesis from Speculative status without the epistemic goods (see editorial conventions).
- Content unrelated to the framework (general philosophy-of-mind or physics essays that do not engage the postulates).
