"""
dodo.py — doit task definitions for the FGA-WG LinkML schema project.

All commands run inside the uv-managed virtual environment via `uv run`.

Usage:
    uv run doit              # run all default tasks
    uv run doit <task>       # run a specific task, e.g. `uv run doit lint`
    uv run doit list         # list all available tasks with descriptions
    uv run doit --continue   # keep going even if one task fails

Default tasks (run by `uv run doit`):
    lint, json_schema, summary, erdiagram, plantuml, docs
"""
from pathlib import Path

from doit.tools import title_with_actions

# ── Paths ──────────────────────────────────────────────────────────────────

SCHEMA_DIR = Path("src/schema")
TOP_LEVEL  = SCHEMA_DIR / "top_level.yaml"
LINT_CFG   = Path("src/linkml_lint_config.yaml")
GEN_DIR    = Path("generated")
DOCS_DIR   = Path("docs")

# Every .yaml in the schema dir — any change triggers dependent tasks
SCHEMA_FILES = list(SCHEMA_DIR.glob("*.yaml"))

# ── Global doit configuration ───────────────────────────────────────────────

DOIT_CONFIG = {
    "default_tasks": ["lint", "json_schema", "summary", "erdiagram", "plantuml", "docs", "overview"],
    "verbosity": 1,
}


# ── Helper ──────────────────────────────────────────────────────────────────

def uv(cmd: str) -> str:
    """Prefix a command with `uv run` so it uses the project virtual env."""
    return f"uv run {cmd}"


# ── Tasks ────────────────────────────────────────────────────────────────────

def task_lint():
    """Validate the schema with linkml-lint."""
    return {
        "actions":  [uv(f"linkml-lint --config {LINT_CFG} --validate {SCHEMA_DIR}")],
        "title":    title_with_actions,
        "uptodate": [False],  # always run — lint is a check, not a build step
        "verbosity": 2,
    }


def task_json_schema():
    """Generate JSON Schema → generated/schema.json"""
    target = GEN_DIR / "schema.json"
    return {
        "actions": [
            f"mkdir -p {GEN_DIR}",
            uv(f"gen-json-schema {TOP_LEVEL} > {target}"),
        ],
        'title': title_with_actions,
        "file_dep": SCHEMA_FILES,
        "targets":  [target],
    }


def task_summary():
    """Generate TSV class/slot summary → generated/schema_summary.tsv"""
    target = GEN_DIR / "schema_summary.tsv"
    return {
        "actions": [
            f"mkdir -p {GEN_DIR}",
            uv(f"gen-summary {TOP_LEVEL} > {target}"),
        ],
        'title': title_with_actions,
        "file_dep": SCHEMA_FILES,
        "targets":  [target],
    }


def task_erdiagram():
    """Generate full-schema Mermaid ER diagram → generated/schema_overview.md"""
    target = GEN_DIR / "schema_overview.md"
    return {
        "actions": [
            f"mkdir -p {GEN_DIR}",
            uv(f"gen-erdiagram {TOP_LEVEL} > {target}"),
        ],
        'title': title_with_actions,
        "file_dep": SCHEMA_FILES,
        "targets":  [target],
    }


def task_plantuml():
    """Generate PlantUML class diagram source → generated/schema_overview.puml"""
    target = GEN_DIR / "schema_overview.puml"
    return {
        "actions": [
            f"mkdir -p {GEN_DIR}",
            # --preserve-names keeps original LinkML names rather than normalising them
            uv(f"gen-plantuml --format puml --preserve-names {TOP_LEVEL} > {target}"),
        ],
        'title': title_with_actions,
        "file_dep": SCHEMA_FILES,
        "targets":  [target],
    }


def task_docs():
    """Generate per-class Markdown documentation → docs/"""
    # TopLevel.md is used as the representative target for up-to-date checks
    target     = DOCS_DIR / "TopLevel.md"
    pages_file = DOCS_DIR / ".pages"

    def write_pages_file():
        """Pin the nav order: index first, overview second, then everything else."""
        pages_file.write_text(
            "nav:\n"
            "  - index.md\n"
            "  - overview.md\n"
            "  - ...\n"
        )

    return {
        "actions": [
            f"mkdir -p {DOCS_DIR}",
            uv(f"gen-doc -d {DOCS_DIR} {TOP_LEVEL}"),
            write_pages_file,
        ],
        'title': title_with_actions,
        "file_dep": SCHEMA_FILES,
        "targets":  [target, pages_file],
    }


def task_overview():
    """Create schema overview page → docs/overview.md (erdiagram + PlantUML UML)"""
    erdiagram_src = GEN_DIR / "schema_overview.md"
    plantuml_src  = GEN_DIR / "schema_overview.puml"
    target        = DOCS_DIR / "overview.md"

    def create_overview():
        erdiagram = erdiagram_src.read_text().strip()
        plantuml  = plantuml_src.read_text().strip()
        content = (
            "# Schema Overview\n\n"
            "## Entity–Relationship Diagram\n\n"
            "The diagram below shows all classes in the FGA-WG schema "
            "and their relationships.\n\n"
            f"{erdiagram}\n\n"
            "## UML Class Diagram\n\n"
            "The PlantUML diagram below provides a UML class view of the schema, "
            "showing field types and inheritance relationships.\n\n"
            "```kroki-plantuml\n"
            f"{plantuml}\n"
            "```\n"
        )
        target.write_text(content)

    return {
        "actions":  [create_overview],
        "file_dep": [erdiagram_src, plantuml_src],
        "targets":  [target],
        "task_dep": ["erdiagram", "plantuml"],
    }


def task_build_site():
    """Build the full MkDocs HTML site → site/  (run after docs)"""
    return {
        "actions":   [uv("mkdocs build")],
        'title': title_with_actions,
        "task_dep":  ["docs", "overview"],
        "verbosity": 2,
    }


def task_serve():
    """Serve the docs site locally for live preview  (mkdocs serve)"""
    return {
        "actions":   [uv("mkdocs serve")],
        'title': title_with_actions,
        "task_dep":  ["docs", "overview"],
        "uptodate":  [False],   # always run when explicitly requested
        "verbosity": 2,
    }
