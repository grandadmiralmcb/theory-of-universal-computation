# AGENTS.md

## Project Mission

This repository is the canonical living source for the **Expression-Tree Ontology** (Theory of Universal Computation).

Keep the theory coherent, precise, and extensible. Prefer formal clarity, consistent terminology, and incremental quantitative progress over speculative expansion.

## Core Principles

- Reality is modeled as evaluation of syntactically bound expression trees under cost minimization and preferential sequentialization.
- Maintain a small, stable set of primitive functions.
- Classical and quantum-like regimes should emerge cleanly from the same primitives.
- Record major conceptual advances in `CHANGELOG.md`.

## Repository Structure

| Path | Purpose |
|------|---------|
| `README.md` | Front page + reading guide |
| `docs/` | Numbered core theory documents (01–07) |
| `CHANGELOG.md` | Chronological record of advances |
| `notes/` (optional) | Experimental or speculative ideas |

## Working Style

- Prefer precise, compositional language.
- Keep mathematical notation consistent with existing docs (cost functions, amplitudes, linear typing, vacuum, etc.).
- When adding new content, update the reading guide table in `README.md` if needed.
- Label open problems and speculative sections clearly.
- Prefer short, self-contained sections over long narrative.

## Conventions for Edits

1. Major conceptual or formal advances → update `CHANGELOG.md` first.
2. Keep document numbering and cross-references stable.
3. Prefer rewriting for clarity over accumulating contradictory notes.
4. Do not introduce new primitives without explicit justification and update to the core set.

## Safety & Scope

- This is a pure theory / documentation repository.
- Do not add executable code, secrets, or personal data.
- Do not claim endorsement by any organization.

## Useful First Prompts for Grok

- Explain the current core ontology and list the primitive functions.
- Summarize the continuum-limit derivation and the effective classical trajectory.
- Identify the highest-priority open problems from `docs/07-roadmap.md`.
- Propose the next quantitative step that would most strengthen the framework.
