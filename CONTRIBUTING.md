# Contributing to FGA-WG

Thank you for your interest in contributing to the FAIRification of Genomic Annotations Working Group schema!

## Table of contents

- [Prerequisites](#prerequisites)
- [Setting up the development environment](#setting-up-the-development-environment)
- [Project structure](#project-structure)
- [Making schema changes](#making-schema-changes)
- [Available tasks](#available-tasks)
- [Previewing the documentation locally](#previewing-the-documentation-locally)
- [Submitting a pull request](#submitting-a-pull-request)
- [CI/CD overview](#cicd-overview)
- [Known issues and workarounds](#known-issues-and-workarounds)

---

## Prerequisites

| Tool | Purpose | Install |
|------|---------|---------|
| **Python ≥ 3.10** | Runtime | [python.org](https://www.python.org/downloads/) or your system package manager |
| **uv** | Dependency management & virtual env | `curl -LsSf https://astral.sh/uv/install.sh \| sh` |
| **git** | Version control | [git-scm.com](https://git-scm.com/) |

> **Note:** All Python tools (`linkml-lint`, `gen-doc`, `mkdocs`, `doit`, …) are managed by `uv`
> and installed automatically — you do not need to install them globally.

---

## Setting up the development environment

```bash
git clone git@github.com:fairtracks/fga-wg.git
cd fga-wg
uv sync          # installs all dependencies into .venv/
```

That is all.  Every command below is prefixed with `uv run`, which transparently
activates the virtual environment, so you never need to run `source .venv/bin/activate`.

---

## Project structure

```
fga-wg/
├── src/
│   ├── schema/                  # ← LinkML schema files (the source of truth)
│   │   ├── top_level.yaml       #   root schema — start here
│   │   └── *.yaml               #   one file per entity / concept
│   └── linkml_lint_config.yaml  # linter configuration
│
├── generated/                   # auto-generated artifacts — do not edit by hand
│   ├── schema.json              #   JSON Schema
│   ├── schema_summary.tsv       #   TSV class/slot summary
│   ├── schema_overview.md       #   Mermaid ER diagram (source)
│   └── schema_overview.puml     #   PlantUML class diagram (source)
│
├── docs/                        # auto-generated MkDocs pages — do not edit by hand
│
├── dodo.py                      # doit task definitions (build system)
├── mkdocs.yml                   # documentation site configuration
├── pyproject.toml               # Python dependencies (managed by uv)
└── uv.lock                      # pinned dependency versions — always commit this
```

> **Rule of thumb:** only edit files under `src/`.
> Everything in `generated/` and `docs/` is regenerated automatically.

---

## Making schema changes

1. **Edit** one or more `.yaml` files under `src/schema/`.
2. **Validate** the schema:
   ```bash
   uv run doit lint
   ```
3. **Regenerate** all derived artifacts:
   ```bash
   uv run doit
   ```
4. **Review** the generated outputs in `generated/` and preview the docs site (see below).
5. **Commit everything** — schema files, generated artifacts, and updated docs all belong in git.

---

## Available tasks

All tasks are defined in `dodo.py` and run via `uv run doit`.

```bash
uv run doit list              # show all tasks with descriptions
uv run doit                   # run all default tasks (lint + all generators)
uv run doit <task>            # run a single task
uv run doit -a                # force-run everything, ignoring up-to-date checks
uv run doit --continue        # keep going even if one task fails
```

| Task | What it does | Output |
|------|-------------|--------|
| `lint` | Validates schema with `linkml-lint` | — |
| `json_schema` | Generates JSON Schema | `generated/schema.json` |
| `summary` | Generates TSV class/slot summary | `generated/schema_summary.tsv` |
| `erdiagram` | Generates Mermaid ER diagram | `generated/schema_overview.md` |
| `plantuml` | Generates PlantUML class diagram | `generated/schema_overview.puml` |
| `docs` | Generates per-class Markdown pages | `docs/` |
| `overview` | Generates the schema overview page | `docs/overview.md` |
| `build_site` | Builds the full static HTML site | `site/` |
| `serve` | Serves the docs locally for preview | http://127.0.0.1:8000 |

**Doit only re-runs a task when its inputs have changed** (schema files or `uv.lock`),
so running `uv run doit` repeatedly is fast.
Use `uv run doit info <task>` to inspect the current up-to-date status of a specific task.

---

## Previewing the documentation locally

```bash
uv run doit serve
```

This generates the documentation and starts a live-reloading server at
<http://127.0.0.1:8000>.  The server does not watch the schema files for
changes — re-run `uv run doit` and then `uv run doit serve` after edits.

---

## Submitting a pull request

1. **Fork** the repository and create a feature branch:
   ```bash
   git checkout -b my-feature
   ```
2. Make your changes in `src/schema/`.
3. Run `uv run doit` to validate and regenerate all artifacts.
4. Commit schema files **and** generated artifacts together:
   ```bash
   git add src/ generated/ docs/
   git commit -m "feat: describe your change"
   ```
5. Push and open a pull request against `main`.

> The CI pipeline will re-run generation on your PR and upload the resulting
> `generated/` and `docs/` directories as downloadable artifacts so reviewers
> can inspect the exact outputs.

---

## CI/CD overview

| Workflow | Triggers | What it does |
|----------|----------|-------------|
| **Validate** (`.github/workflows/validate.yml`) | Every push, every PR | Runs `linkml-lint` — fast feedback |
| **Build & Deploy** (`.github/workflows/build.yml`) | Push to `main`, every PR | Generates all artifacts; on `main` commits them back and deploys to [GitHub Pages](https://fairtracks.github.io/fga-wg/) |

The `[skip ci]` tag is added to the auto-commit message on `main` to prevent
an infinite trigger loop.

---

## Known issues and workarounds

### `equals_number: true` lint error

`track_geometry.yaml` uses `equals_number: true` in a rule precondition.
This triggers a `valid-schema` lint error because the LinkML metamodel expects
an integer, not a boolean.  This is a known upstream bug
([linkml/linkml#1136](https://github.com/linkml/linkml/issues/1136));
`equals_number: true` is currently the only syntax that works correctly at
runtime.

The error is suppressed in `dodo.py` via the `LINT_KNOWN_ISSUES` list.
It is printed as a visible warning on every lint run so it is not silently
lost.  Once the upstream issue is resolved, remove the entry from
`LINT_KNOWN_ISSUES` and update `track_geometry.yaml` accordingly.

### Using a local linkml fork

If you need to work against a patched version of linkml, add the following
to `pyproject.toml` and run `uv sync`:

```toml
[tool.uv.sources]
linkml = { git = "https://github.com/<your-fork>/linkml.git", branch = "your-branch" }
```

