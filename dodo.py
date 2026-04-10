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
from collections.abc import Callable
from pathlib import Path
from typing import override, TypedDict, NotRequired, Literal

from doit.task import Task
from doit.reporter import ConsoleReporter
from doit.tools import title_with_actions

# ── Types ─────────────────────────────────────────────────────────────────

_FilePath = str | Path  # str or pathlib.Path, as accepted by doit for file_dep / targets

# Tuple form of a Python action / uptodate callable: doit unpacks it as
#   item[0]   → the callable
#   item[1]   → positional args list  (optional)
#   item[2]   → keyword args dict     (optional)
_CallableTuple = (
    tuple[Callable[..., object]]
    | tuple[Callable[..., object], list[object]]
    | tuple[Callable[..., object], list[object], dict[str, object]]
)

# A single action item accepted by doit:
#   str                   → shell command (shell=True)
#   list[str | Path]      → shell command + args (shell=False)
#   _CallableTuple        → (callable,), (callable, args), or (callable, args, kwargs)
#   Callable[..., object] → Python callable (PythonAction)
_ActionItem = str | list[str | Path] | _CallableTuple | Callable[..., object]

# A single uptodate item accepted by doit:
#   bool / None           → fixed up-to-date status
#   str                   → result dependency by task name
#   Callable[..., object] → computed check (called at task evaluation time)
#   _CallableTuple        → callable with explicit positional / keyword args
_UpToDateItem = bool | None | str | Callable[..., object] | _CallableTuple


class CmdParamDict(TypedDict):
    """Dict format for a single task parameter (passed to doit's CmdOption)."""
    name: str                                    # required
    default: object                              # required; any Python value
    section: NotRequired[str]
    type: NotRequired[type]
    short: NotRequired[str]                      # single-char short flag
    long: NotRequired[str]                       # long flag name
    inverse: NotRequired[str]                    # boolean inverse flag name
    choices: NotRequired[list[tuple[str, str]]]  # [(value, description), ...]
    help: NotRequired[str]
    metavar: NotRequired[str]
    env_var: NotRequired[str | None]


class TaskDict(TypedDict):
    """Dict format returned by doit task-creator functions.

    Only ``actions`` is required (doit raises InvalidTask if it is absent).
    All other keys are optional; omitted keys use doit's own defaults.

    See ``doit.task.Task.valid_attr`` for the authoritative list of accepted
    fields and their valid types.
    """
    actions: list[_ActionItem] | tuple[_ActionItem, ...] | None  # required key; None → no-op task
    basename: NotRequired[str]             # used when a generator yields sub-tasks
    name: NotRequired[str]                 # sub-task name (normally set by loader)
    file_dep: NotRequired[list[_FilePath] | tuple[_FilePath, ...]]
    task_dep: NotRequired[list[str] | tuple[str, ...]]
    uptodate: NotRequired[list[_UpToDateItem] | tuple[_UpToDateItem, ...]]
    calc_dep: NotRequired[list[str] | tuple[str, ...]]
    targets: NotRequired[list[_FilePath] | tuple[_FilePath, ...]]
    setup: NotRequired[list[str] | tuple[str, ...]]                              # task names to run as setup
    clean: NotRequired[list[_ActionItem] | tuple[_ActionItem, ...] | Literal[True]]  # True → delete targets
    teardown: NotRequired[list[_ActionItem] | tuple[_ActionItem, ...]]
    doc: NotRequired[str]
    params: NotRequired[list[CmdParamDict] | tuple[CmdParamDict, ...]]
    pos_arg: NotRequired[str]
    verbosity: NotRequired[Literal[0, 1, 2] | None]
    io: NotRequired[dict[str, object]]                             # e.g. {"capture": True}
    getargs: NotRequired[dict[str, tuple[str, str]]]               # {arg_name: (task_id, key)}
    title: NotRequired[Callable[[Task], str]]
    watch: NotRequired[list[object] | tuple[object, ...]]
    meta: NotRequired[dict[str, object]]


class LinterProblem(TypedDict):
    message: str
    level: str | None
    schema_name: str | None
    schema_source: str | None
    rule_name: str | None

class KnownIssue(TypedDict):
    message_pattern: str
    reason: str

# ── Constants ──────────────────────────────────────────────────────────────────

SCHEMA_DIR = Path("src/schema")
TOP_LEVEL = SCHEMA_DIR / "TopLevel.yaml"
TOP_LEVEL_CLASS = 'TopLevel'
LINT_CFG = Path("src/linkml_lint_config.yaml")
GEN_DIR = Path("generated")
JSON_SCHEMA = GEN_DIR / "schema.json"
PYDANTIC_V1_MODEL = GEN_DIR / "pydantic_v1_model.py"
PYDANTIC_V2_MODEL = GEN_DIR / "pydantic_v2_model.py"
PYDANTIC_MODELS = (PYDANTIC_V1_MODEL, PYDANTIC_V2_MODEL)
EXAMPLES_DIR = GEN_DIR / "examples"
DOCS_DIR   = Path("docs")
SCRIPTS_DIR = Path("src/scripts")

EXTRACT_EXAMPLES_SCRIPT = SCRIPTS_DIR / "extract_examples.py"

# Every .yaml in the schema dir — any change triggers dependent tasks
SCRIPT_FILES = tuple(SCRIPTS_DIR.glob("*.py"))
SCHEMA_FILES = tuple(SCHEMA_DIR.glob("*.yaml"))
EXAMPLE_FILES = tuple(EXAMPLES_DIR / f"{model.with_suffix('.json').name}"
                 for model in SCHEMA_FILES
                 if model.stem != "Any") # skip Any since it is a special case with no examples

# uv.lock changes whenever a dependency is updated (e.g. a new linkml release).
# Adding it to file_dep ensures all generation tasks re-run after any dep change.
TOOL_DEPS = (Path("uv.lock"), 'dodo.py') + SCRIPT_FILES

# Upper file size threshold for empty files. If target files are smaller
# than this, they are considered empty and tasks execution is not skipped.
EMPTY_FILE_THRESHOLD = 10


# ── Helpers ─────────────────────────────────────────────────────────────────

def uv(cmd: str | list[str]) -> str:
    """Prefix a command with `uv run` so it uses the project virtual env."""
    if isinstance(cmd, list):
        cmd = ' '.join(cmd)

    return f"uv run {cmd}"


class CommandOnRunReporter(ConsoleReporter):
    """Doit reporter that shows task commands only when a task actually runs.

    Doit's default ConsoleReporter calls task.title() for both executed and
    skipped tasks, so title_with_actions shows the command list even for
    skipped (--) tasks — which is confusing.  This reporter overrides
    skip_uptodate to show just the task name instead.
    """

    @override
    def skip_uptodate(self, task: Task):
        self.write(f"-- {task.name}\n")  # pyright: ignore[reportUnknownMemberType]


# ── Global doit configuration ───────────────────────────────────────────────

DOIT_CONFIG = {
    "default_tasks": ["lint", "json_schema", "pydantic", "examples", "summary", "erdiagram", "plantuml", "docs", "overview", "nav"],
    "verbosity": 1,
    "reporter": CommandOnRunReporter,
}


def non_empty_targets(*targets: _FilePath) -> list[_UpToDateItem]:
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

LINT_KNOWN_ISSUES : list[KnownIssue] = [
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
        problems: list[LinterProblem] = json.loads(result.stdout) if result.stdout.strip() else []
    except json.JSONDecodeError:
        # Unexpected / unparseable output — print raw and fail
        print(result.stdout)
        if result.stderr:
            print(result.stderr)
        return False

    # Partition into known false positives vs real problems
    real_problems: list[LinterProblem] = []
    suppressed: list[tuple[LinterProblem, KnownIssue]] = []
    for problem in problems:
        matched: KnownIssue | None = next(
            (ki for ki in LINT_KNOWN_ISSUES if ki["message_pattern"] in problem["message"]),
            None,
        )
        if matched is not None:
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

def task_lint() -> TaskDict:
    """Validate the schema with linkml-lint, filtering documented known false positives."""
    return {
        "actions":  [_run_lint],
        "uptodate": [False],   # always run — lint is a check, not a build step
        "verbosity": 2,
    }


def task_json_schema() -> TaskDict:
    """Generate JSON Schema → generated/schema.json"""
    target = JSON_SCHEMA
    return {
        "actions": [
            f"mkdir -p {GEN_DIR}",
            uv(f"gen-json-schema {TOP_LEVEL} -t {TOP_LEVEL_CLASS} > {target}"),
        ],
        'title': title_with_actions,
        "file_dep": SCHEMA_FILES + TOOL_DEPS,
        "targets":  [target],
        "uptodate": non_empty_targets(target),
    }


def task_pydantic() -> TaskDict:
    """Generate Pydantic models → generated/pydantic_v1_schema.py and generated/pydantic_v2_schema.py"""
    targets = PYDANTIC_MODELS

    def replace_import_line_for_embedded_pydantic_v1():
        content = PYDANTIC_V1_MODEL.read_text()
        new_content = content.replace("from pydantic import", "from pydantic.v1 import")
        PYDANTIC_V1_MODEL.write_text(new_content)

    def get_common_cmd(target: Path) -> list[str]:
        return [
            'datamodel-codegen',
            '--formatters ruff-format',
            f'--input {JSON_SCHEMA}',
            f'--input-file-type jsonschema',
            f'--output {target}',
        ]

    return {
        "actions": [
            f"mkdir -p {GEN_DIR}",
            uv(get_common_cmd(PYDANTIC_V1_MODEL) + ['--output-model-type pydantic.BaseModel']),
            replace_import_line_for_embedded_pydantic_v1,
            uv(get_common_cmd(PYDANTIC_V2_MODEL) + ['--output-model-type pydantic_v2.BaseModel']),
        ],
        'title': title_with_actions,
        "file_dep": TOOL_DEPS + (JSON_SCHEMA,),
        "targets":  targets,
        "uptodate": non_empty_targets(*targets),
    }


def task_examples() -> TaskDict:
    """Generate JSON examples from Pydantic models → generated/examples/*.json"""
    targets = EXAMPLE_FILES

    def _module_string_from_path(file_path: Path) -> str:
        return ".".join(file_path.with_suffix("").parts)

    return {
        "actions": [
            f"mkdir -p {GEN_DIR}",
            uv(['python',
                '-m',
                _module_string_from_path(EXTRACT_EXAMPLES_SCRIPT)]
               + [_file.stem for _file in EXAMPLE_FILES]),
        ],
        'title': title_with_actions,
        "file_dep": TOOL_DEPS + PYDANTIC_MODELS,
        "targets":  targets,
        "uptodate": non_empty_targets(*targets),
    }

def task_summary() -> TaskDict:
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


def task_erdiagram() -> TaskDict:
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


def task_plantuml() -> TaskDict:
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


def task_docs() -> TaskDict:
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


def task_overview() -> TaskDict:
    """Create schema overview page → docs/overview.md (erdiagram + PlantUML UML)"""
    erdiagram_src = GEN_DIR / "schema_overview.md"
    plantuml_src  = GEN_DIR / "schema_overview.puml"
    target        = DOCS_DIR / "overview.md"

    def run():
        from src.docs.overview import create_overview
        create_overview(erdiagram_src, plantuml_src, target)

    return {
        "actions":  [run],
        "file_dep": (erdiagram_src, plantuml_src) + TOOL_DEPS,
        "targets":  [target],
        "uptodate": non_empty_targets(target),
        "task_dep": ["erdiagram", "plantuml"],
    }


def task_nav() -> TaskDict:
    """Categorise generated docs pages and write the literate-nav file → docs/nav.md

    Delegates to src/docs/nav.py which uses SchemaView to group pages into
    Introduction | Classes | Slots | Types & Enums tabs.
    """
    target = DOCS_DIR / "nav.md"

    def run():
        from src.docs.nav import generate_nav
        generate_nav(TOP_LEVEL, DOCS_DIR, target)

    return {
        "actions":  [run],
        "file_dep": SCHEMA_FILES + TOOL_DEPS,
        "targets":  [target],
        "task_dep": ["docs", "overview"],
        "uptodate": non_empty_targets(target),
    }


def task_build_site() -> TaskDict:
    """Build the full MkDocs HTML site → site/  (run after nav)"""
    return {
        "actions":   [uv("mkdocs build")],
        "title":     title_with_actions,
        "task_dep":  ["nav"],   # nav implies docs + overview
        "verbosity": 2,
    }


def task_serve() -> TaskDict:
    """Serve the docs site locally for live preview  (mkdocs serve)"""
    return {
        "actions":   [uv("mkdocs serve")],
        "title":     title_with_actions,
        "task_dep":  ["nav"],   # nav implies docs + overview
        "uptodate":  [False],
        "verbosity": 2,
    }
