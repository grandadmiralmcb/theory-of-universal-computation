# AGENTS.md

## Project Mission

This repository is the canonical living source for the **Expression-Tree Ontology** (Theory of Universal Computation).

Keep the theory coherent, precise, and extensible. Prefer formal clarity, consistent terminology, and incremental quantitative progress over speculative expansion.

## Core Principles

- Claims follow the derivation-first charter (`docs/00-theory-charter.md`): only O1–O4 are ontology; everything further is a numbered postulate (WM, CI, HQ) that must appear in theorem hypotheses.
- Maintain a small, stable set of primitive functions.
- Classical and quantum-like regimes should emerge cleanly from the same primitives; where they currently do not, record the gap as a named contention in `docs/07-roadmap.md` rather than papering over it.
- Record major conceptual advances in `CHANGELOG.md`.

## Repository Structure

| Path | Purpose |
|------|---------|
| `README.md` | Front page + reading order |
| `docs/` | Numbered theory documents (00–14); `docs/00-theory-charter.md` and `docs/14-derivation-from-ontology.md` are authoritative |
| `sim/` | Executable toy simulators instantiating the working model |
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

- This is a theory / documentation repository with a small executable `sim/` suite.
- Executable code is limited to `sim/`. Every sim must run (`python3 sim/<file>.py`) — run it before citing it as an executable confirmation in any doc. A sim that does not execute must not be cited as evidence.
- Do not add secrets or personal data.
- Do not claim endorsement by any organization.

## Useful First Prompts for Grok

- Explain the current core ontology and list the primitive functions.
- Summarize the continuum-limit derivation and the effective classical trajectory.
- Identify the highest-priority open problems from `docs/07-roadmap.md`.
- Propose the next quantitative step that would most strengthen the framework.
