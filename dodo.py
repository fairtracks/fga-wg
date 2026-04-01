"""
dodo.py — doit task definitions for the FGA-WG LinkML schema project.

All commands run inside the uv-managed virtual environment via `uv run`.

Usage:
    uv run doit                       # run all default tasks
    uv run doit <task>                # run a specific task, e.g. `uv run doit lint`
    uv run doit list                  # list all available tasks with descriptions
    uv run doit --continue            # keep going even if one task fails
    uv run doit -a                    # force-run all tasks, ignoring up-to-date checks

Diagnostic commands:
    uv run doit info <task>           # show task status, file deps, and targets
    uv run doit list --status         # show up-to-date status for all tasks
    uv run doit -r executed-only      # show only tasks that actually ran (hides skipped)

Understanding the run output:
    .  task_name   task ran (either a schema file changed, or a target was missing/small)
    -- task_name   task skipped (all up-to-date checks passed)

    When a target file triggers a re-run (missing or suspiciously small), the reason
    is printed explicitly.  For file_dep-triggered re-runs, use `doit info <task>` to
    inspect which dependencies are newer than the target.

Default tasks (run by `uv run doit`):
    lint, json_schema, summary, erdiagram, plantuml, docs, overview
"""
from pathlib import Path

from doit.reporter import ConsoleReporter
from doit.tools import title_with_actions

# ── Constants ──────────────────────────────────────────────────────────────────

SCHEMA_DIR = Path("src/schema")
TOP_LEVEL  = SCHEMA_DIR / "top_level.yaml"
LINT_CFG   = Path("src/linkml_lint_config.yaml")
GEN_DIR    = Path("generated")
DOCS_DIR   = Path("docs")

# Every .yaml in the schema dir — any change triggers dependent tasks
SCHEMA_FILES = list(SCHEMA_DIR.glob("*.yaml"))

# uv.lock changes whenever a dependency is updated (e.g. a new linkml release).
# Adding it to file_dep ensures all generation tasks re-run after any dep change.
TOOL_DEPS = [Path("uv.lock")]

# Upper file size threshold for empty files. If target files are smaller
# than this, they are considered empty and tasks execution is not skipped.
EMPTY_FILE_THRESHOLD = 10

# ── Helpers ─────────────────────────────────────────────────────────────────

def uv(cmd: str) -> str:
    """Prefix a command with `uv run` so it uses the project virtual env."""
    return f"uv run {cmd}"


class CommandOnRunReporter(ConsoleReporter):
    """Doit reporter that shows task commands only when a task actually runs.

    Doit's default ConsoleReporter calls task.title() for both executed and
    skipped tasks, so title_with_actions shows the command list even for
    skipped (--) tasks — which is confusing.  This reporter overrides
    skip_uptodate to show just the task name instead.
    """


    def skip_uptodate(self, task):
        self.write(f"-- {task.name}\n")


# ── Global doit configuration ───────────────────────────────────────────────

DOIT_CONFIG = {
    "default_tasks": ["lint", "json_schema", "summary", "erdiagram", "plantuml", "docs", "overview", "nav"],
    "verbosity": 1,
    "reporter": CommandOnRunReporter,
}


def non_empty_targets(*targets: Path):
    """Return an uptodate callable that fails if any target is missing or suspiciously small.

    Doit's default up-to-date check only compares modification times, so a
    task whose target was overwritten with an empty or near-empty file would be
    incorrectly skipped.  Adding this to a task's `uptodate` list catches that
    case and forces a re-run.

    The 10-byte threshold catches both 0-byte files and near-empty outputs
    (e.g. a stray newline written by a failed command), while staying well
    below the minimum meaningful size of any generated file in this project.

    When a target triggers a re-run, the reason is printed to stdout so it
    appears alongside the task output in the doit run log.

    Usage:
        "uptodate": non_empty_targets(target),
    """
    def check() -> bool:
        for t in targets:
            p = Path(t)
            if not p.exists():
                print(f"↻ {p.name}: target does not exist")
                return False
            size = p.stat().st_size
            if size <= EMPTY_FILE_THRESHOLD:
                print(f"↻ {p.name}: target too small ({size}B ≤ {EMPTY_FILE_THRESHOLD}B)")
                return False
        return True
    return [check]


# ── Known linkml-lint false positives ──────────────────────────────────────
# Errors that fail lint due to bugs or missing features in LinkML itself.
# Each entry documents the reason and a link to the upstream issue.
# Suppressed issues are still printed as visible warnings — they are NOT silently ignored.

LINT_KNOWN_ISSUES = [
    {
        # equals_number: true uses a boolean where the metamodel expects integer/null.
        # This is the only syntax that works to check for boolean true in rule preconditions.
        # Upstream issue: https://github.com/linkml/linkml/issues/1136
        "message_pattern": "equals_number: True is not of type 'integer', 'null'",
        "reason": (
            "equals_number: true is the only working syntax to check for boolean true "
            "in LinkML rule preconditions. See https://github.com/linkml/linkml/issues/1136"
        ),
    },
]


def _run_lint() -> bool:
    """Run linkml-lint with JSON output, filtering documented known false positives.

    Suppressed issues are still printed visibly so they are not silently lost.
    Returns False (task failure) if any non-suppressed errors are found.
    """
    import json
    import subprocess

    lint_command = [
        "linkml-lint",
        "--config", str(LINT_CFG),
        "--validate",
        "--format", "json",
        str(SCHEMA_DIR),
    ]
    print(f"        Cmd: {' '.join(lint_command)}")
    result = subprocess.run(
        lint_command,
        capture_output=True,
        text=True,
    )

    # Parse JSON output — linkml-lint exits non-zero on errors so we ignore returncode
    # and inspect the structured output ourselves.
    try:
        problems = json.loads(result.stdout) if result.stdout.strip() else []
    except json.JSONDecodeError:
        # Unexpected / unparseable output — print raw and fail
        print(result.stdout)
        if result.stderr:
            print(result.stderr)
        return False

    # Partition into known false positives vs real problems
    real_problems: list = []
    suppressed: list = []
    for problem in problems:
        matched = next(
            (ki for ki in LINT_KNOWN_ISSUES if ki["message_pattern"] in problem["message"]),
            None,
        )
        if matched:
            suppressed.append((problem, matched))
        else:
            real_problems.append(problem)

    # Always print suppressed issues — they are known but should remain visible
    if suppressed:
        print(f"\n  ⚠  {len(suppressed)} known issue(s) suppressed (upstream LinkML bugs):")
        for problem, known_issue in suppressed:
            print(f"     [{problem['level']}] {problem['message']}")
            print(f"     → {known_issue['reason']}")

    # Print and fail on real problems
    if real_problems:
        print(f"\n  ✖  {len(real_problems)} problem(s) found:")
        for p in real_problems:
            print(f"     [{p['level']}] {p['message']}")
        return False

    suffix = f" ({len(suppressed)} suppressed)" if suppressed else ""
    print(f"✓ No problems found{suffix}")
    return True


# ── Tasks ────────────────────────────────────────────────────────────────────

def task_lint():
    """Validate the schema with linkml-lint, filtering documented known false positives."""
    return {
        "actions":  [_run_lint],
        "uptodate": [False],   # always run — lint is a check, not a build step
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
        "file_dep": SCHEMA_FILES + TOOL_DEPS,
        "targets":  [target],
        "uptodate": non_empty_targets(target),
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
        "file_dep": SCHEMA_FILES + TOOL_DEPS,
        "targets":  [target],
        "uptodate": non_empty_targets(target),
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
        "file_dep": SCHEMA_FILES + TOOL_DEPS,
        "targets":  [target],
        "uptodate": non_empty_targets(target),
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
        "file_dep": SCHEMA_FILES + TOOL_DEPS,
        "targets":  [target],
        "uptodate": non_empty_targets(target),
    }


def task_docs():
    """Generate per-class Markdown documentation → docs/"""
    # TopLevel.md is used as the representative target for up-to-date checks
    target = DOCS_DIR / "TopLevel.md"

    return {
        "actions": [
            f"mkdir -p {DOCS_DIR}",
            uv(f"gen-doc -d {DOCS_DIR} {TOP_LEVEL}"),
        ],
        "title":    title_with_actions,
        "file_dep": SCHEMA_FILES + TOOL_DEPS,
        "targets":  [target],
        "uptodate": non_empty_targets(target),
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
        "file_dep": [erdiagram_src, plantuml_src] + TOOL_DEPS,
        "targets":  [target],
        "uptodate": non_empty_targets(target),
        "task_dep": ["erdiagram", "plantuml"],
    }


def task_nav():
    """Categorise generated docs pages and write the literate-nav file → docs/nav.md

    Reads the schema via SchemaView to determine which pages are classes, slots,
    types, or enums, then writes docs/nav.md which mkdocs-literate-nav uses to
    build a tabbed navigation (Introduction | Classes | Slots | Types & Enums).
    """
    target = DOCS_DIR / "nav.md"

    def generate_nav():
        from linkml_runtime.utils.schemaview import SchemaView

        sv = SchemaView(str(TOP_LEVEL))

        class_names = set(sv.all_classes().keys())
        slot_names  = set(sv.all_slots().keys())
        type_names  = set(sv.all_types().keys())
        enum_names  = set(sv.all_enums().keys())

        # Pages with fixed positions at the top — excluded from category scan
        skip = {"index.md", "overview.md", "nav.md"}

        classes, slots, types_enums, other = [], [], [], []

        for p in sorted(DOCS_DIR.iterdir()):
            if not p.name.endswith(".md") or p.name in skip or p.name.startswith("."):
                continue
            stem = p.stem
            if stem in class_names:
                classes.append(stem)
            elif stem in slot_names:
                slots.append(stem)
            elif stem in type_names or stem in enum_names:
                types_enums.append(stem)
            else:
                other.append(stem)

        def entry(name):
            return f"    * [{name}]({name}.md)"

        lines = [
            "* Introduction",
            "    * [Home](index.md)",
            "    * [Schema Overview](overview.md)",
            "* Classes",
            *[entry(n) for n in classes],
            "* Slots",
            *[entry(n) for n in slots],
            "* Types & Enums",
            *[entry(n) for n in types_enums],
        ]
        if other:
            lines += ["* Other", *[entry(n) for n in other]]

        target.write_text("\n".join(lines) + "\n")

    return {
        "actions":  [generate_nav],
        "file_dep": SCHEMA_FILES + TOOL_DEPS,
        "targets":  [target],
        "task_dep": ["docs", "overview"],
        "uptodate": non_empty_targets(target),
    }


def task_build_site():
    """Build the full MkDocs HTML site → site/  (run after nav)"""
    return {
        "actions":   [uv("mkdocs build")],
        "title":     title_with_actions,
        "task_dep":  ["nav"],   # nav implies docs + overview
        "verbosity": 2,
    }


def task_serve():
    """Serve the docs site locally for live preview  (mkdocs serve)"""
    return {
        "actions":   [uv("mkdocs serve")],
        "title":     title_with_actions,
        "task_dep":  ["nav"],   # nav implies docs + overview
        "uptodate":  [False],
        "verbosity": 2,
    }
