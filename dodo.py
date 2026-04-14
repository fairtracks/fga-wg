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
import json
import jsonschema

from collections.abc import Callable, Iterator
from pathlib import Path
import sys
from typing import override, TypedDict, NotRequired, Literal

from doit.task import Task
from doit.reporter import ConsoleReporter
from doit.tools import title_with_actions

# Add src/ to sys.path so project-local modules are importable without the
# 'src.' prefix (e.g. ``from scripts.helpers import …`` instead of
# ``from src.scripts.helpers import …``).  This is needed because the project
# is declared non-installable (``package = false`` in pyproject.toml).
sys.path.insert(0, str(Path(__file__).parent / "src"))

from scripts.helpers import import_from_path  # noqa: E402

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
PYDANTIC_V2_LINKML_MODEL = GEN_DIR / "pydantic_v2_linkml_model.py"
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
    """Doit reporter that shows task commands only when a task actually runs,
    and prints a pass/fail summary at the end of the run.

    Doit's default ConsoleReporter calls task.title() for both executed and
    skipped tasks, so title_with_actions shows the command list even for
    skipped (--) tasks — which is confusing.  This reporter overrides
    skip_uptodate to show just the task name instead.

    Failed task names are collected during the run and printed in a summary
    block by complete_run(), making it easy to spot which subtasks need
    attention after a --continue run.
    """

    def __init__(self, outstream: object, options: dict[str, object]) -> None:
        super().__init__(outstream, options)  # type: ignore[arg-type]
        self._failed_tasks: list[str] = []
        self._succeeded_tasks: list[str] = []

    @override
    def skip_uptodate(self, task: Task) -> None:
        self.write(f"-- {task.name}\n")  # pyright: ignore[reportUnknownMemberType]

    @override
    def add_success(self, task: Task) -> None:
        super().add_success(task)  # type: ignore[arg-type]
        self._succeeded_tasks.append(task.name)

    @override
    def add_failure(self, task: Task, fail: object) -> None:
        super().add_failure(task, fail)  # type: ignore[arg-type]
        self._failed_tasks.append(task.name)

    @override
    def complete_run(self) -> None:
        super().complete_run()
        n_ok   = len(self._succeeded_tasks)
        n_fail = len(self._failed_tasks)
        total  = n_ok + n_fail
        if total == 0:
            return
        self.write(f"\n{'─' * 60}\n")  # pyright: ignore[reportUnknownMemberType]
        if n_fail == 0:
            self.write(f"  ✓  All {total} task(s) passed\n")  # pyright: ignore[reportUnknownMemberType]
        else:
            self.write(  # pyright: ignore[reportUnknownMemberType]
                f"  ✖  {n_fail} of {total} task(s) failed"
                f" ({n_ok} passed):\n"
            )
            for name in self._failed_tasks:
                self.write(f"       • {name}\n")  # pyright: ignore[reportUnknownMemberType]
        self.write(f"{'─' * 60}\n")  # pyright: ignore[reportUnknownMemberType]


# ── Global doit configuration ───────────────────────────────────────────────

DOIT_CONFIG = {
    "default_tasks": [
        "lint",
        "json_schema", "pydantic", "pydantic_linkml", "examples",
        "validate_linkml", "validate_json_schema", "validate_pydantic_v1", "validate_pydantic_v2", "validate_pydantic_v2_linkml",
        "summary", "erdiagram", "plantuml", "docs", "overview", "nav",
    ],
    "verbosity": 1,
    "reporter": CommandOnRunReporter,
    "continue": True,   # keep running independent tasks even when one validation subtask fails
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
    {
        "message_pattern": "is not of type 'string', 'null'",
        "reason": (
            "LinkML's metamodel for Example.value only supports strings, while Example.object"
            "supports only objects/dicts. Integers, boolean, floats and lists are not supported."
            "See https://github.com/linkml/linkml/issues/3018"
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
        "file_dep": (*SCHEMA_FILES, *TOOL_DEPS),
        "verbosity": 2,
    }


def task_json_schema() -> TaskDict:
    """Generate JSON Schema → generated/schema.json

    --include-range-class-descendants makes slots whose range has subclasses emit
    ``anyOf: [{$ref: Parent}, {$ref: Child}, …]`` instead of just ``{$ref: Parent}``.
    This is necessary for the ``files`` slot to accept both ``File`` and
    ``GenomicAnnotationFile`` objects, because ``File`` is closed
    (``additionalProperties: false``) and a plain ``{$ref: "#/$defs/File"}`` would
    reject the extra fields on ``GenomicAnnotationFile``.
    """
    target = JSON_SCHEMA
    return {
        "actions": [
            f"mkdir -p {GEN_DIR}",
            uv([
                'gen-json-schema',
                f'{TOP_LEVEL}',
                f'-t {TOP_LEVEL_CLASS}',
               '--include-range-class-descendants',
                f'> {target}'
            ]),
        ],
        'title': title_with_actions,
        "file_dep": (*SCHEMA_FILES, *TOOL_DEPS),
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
            '--disable-timestamp',
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
        "file_dep": (JSON_SCHEMA, *TOOL_DEPS),
        "targets":  targets,
        "uptodate": non_empty_targets(*targets),
    }


def task_pydantic_linkml() -> TaskDict:
    """Generate a LinkML-native Pydantic v2 model → generated/pydantic_v2_linkml_model.py

    Unlike the ``pydantic`` task (which uses datamodel-codegen from the JSON Schema),
    this task uses LinkML's own ``gen-pydantic`` generator, which reads ``is_a``
    relationships directly and therefore preserves Python class inheritance:

        class GenomicAnnotationFile(File): ...   # ← is_a: File preserved

    With ``datamodel-codegen``, the JSON Schema is flattened (all inherited properties
    are inlined into each class definition without ``allOf``), so the generator has no
    signal to reconstruct the hierarchy and emits ``class GenomicAnnotationFile(BaseModel)``
    instead.

    Trade-off: the ``files`` slot is typed as ``list[File]`` in this model (following
    the ``range: File`` declaration).  Because ``GenomicAnnotationFile`` truly inherits
    from ``File``, Python's type system and most validators accept subclass instances.

    As in task_json_schema, ``--include-range-class-descendants`` is required for the
    ``files`` slot to accept both ``File`` and ``GenomicAnnotationFile`` objects.
    """
    target = PYDANTIC_V2_LINKML_MODEL
    return {
        "actions": [
            f"mkdir -p {GEN_DIR}",
            uv([
                'gen-pydantic',
                f'{TOP_LEVEL}',
               '--include-range-class-descendants',
                f'> {target}',
            ]),
        ],
        'title': title_with_actions,
        "file_dep": (*SCHEMA_FILES, *TOOL_DEPS),
        "targets":  [target],
        "uptodate": non_empty_targets(target),
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
        "file_dep": (*PYDANTIC_MODELS, *TOOL_DEPS),
        "targets":  targets,
        "uptodate": non_empty_targets(*targets),
    }

def task_validate_linkml() -> Iterator[TaskDict]:
    """Validate each generated example against its LinkML class — one subtask per file.

    Subtasks are named ``validate_linkml:<ClassName>`` so individual examples can be
    targeted with ``uv run doit validate_linkml:Assessment`` and failed subtasks are
    identified by name in the run output.  Because each subtask has its own file_dep,
    only examples whose source file (or any schema file) changed are re-validated.
    """
    for example_file in EXAMPLE_FILES:
        class_name = example_file.stem

        # Default-argument capture avoids the closure-over-loop-variable pitfall
        def run(cls: str = class_name, fp: Path = example_file) -> bool:
            import subprocess
            result = subprocess.run(
                [
                    "linkml-validate",
                    "--schema", str(TOP_LEVEL),
                    "--target-class", cls,
                    str(fp),
                ],
                capture_output=True,
                text=True,
            )
            if result.returncode != 0:
                print((result.stderr or result.stdout).strip())
                return False
            return True

        task: TaskDict = {
            "name":     class_name,
            "actions":  [run],
            "file_dep": (example_file, *SCHEMA_FILES, *TOOL_DEPS),
            "task_dep": ["examples"],
            "verbosity": 2,
        }
        yield task


def task_validate_json_schema() -> Iterator[TaskDict]:
    """Validate each generated example against its class definition in the JSON Schema.

    Each subtask loads the full schema once, then validates one example file so that
    only changed example files (or a changed JSON Schema) are re-checked.
    """
    for example_file in EXAMPLE_FILES:
        class_name = example_file.stem

        def run(cls: str = class_name, fp: Path = example_file) -> bool:
            full_schema = json.loads(JSON_SCHEMA.read_text())
            defs = full_schema.get("$defs", {})

            if cls not in defs:
                print(f"no '$defs.{cls}' entry found in JSON Schema")
                return False

            instance = json.loads(fp.read_text())
            ref_schema = {"$ref": f"#/$defs/{cls}", "$defs": defs}

            try:
                jsonschema.validate(instance, ref_schema)
            except jsonschema.ValidationError as exc:
                print(exc.message)
                return False
            return True

        task: TaskDict = {
            "name":     class_name,
            "actions":  [run],
            "file_dep": (example_file, JSON_SCHEMA, *TOOL_DEPS),
            "task_dep": ["examples", "json_schema"],
            "verbosity": 2,
        }
        yield task


def _pydantic_subtasks(
    model_file: Path,
    version: Literal["v1", "v2"],
    generation_task: str = "pydantic",
) -> Iterator[TaskDict]:
    """Yield one per-example validation subtask for the given Pydantic model version.

    ``generation_task`` is the doit task that produces ``model_file`` and is listed
    as a ``task_dep`` so doit runs generation before validation.
    """
    module_name = f"_doit_{model_file.stem}"

    for example_file in EXAMPLE_FILES:
        class_name = Path(example_file).stem

        # `model_file`, `version`, and `generation_task` are captured from the
        # enclosing function scope (stable across the loop), so only the per-iteration
        # `cls` and `fp` need default-argument capture.
        def run(cls: str = class_name, fp: Path = example_file) -> bool:
            import json
            import sys

            if module_name not in sys.modules:
                import_from_path(module_name, model_file)

            model_class = getattr(sys.modules[module_name], cls, None)
            if model_class is None:
                print(f"class '{cls}' not found in Pydantic {version} module")
                return False

            try:
                if version == "v2":
                    model_class.model_validate(json.loads(fp.read_text()))
                else:
                    model_class.parse_obj(json.loads(fp.read_text()))
            except Exception as exc:  # noqa: BLE001
                print(str(exc))
                return False

            return True

        task: TaskDict = {
            "name":     class_name,
            "actions":  [run],
            "file_dep": (example_file, model_file, *TOOL_DEPS),
            "task_dep": ["examples", generation_task],
            "verbosity": 2,
        }
        yield task


def task_validate_pydantic_v1() -> Iterator[TaskDict]:
    """Validate each generated example against the Pydantic v1 models."""
    yield from _pydantic_subtasks(PYDANTIC_V1_MODEL, "v1")


def task_validate_pydantic_v2() -> Iterator[TaskDict]:
    """Validate each generated example against the Pydantic v2 models."""
    yield from _pydantic_subtasks(PYDANTIC_V2_MODEL, "v2")


def task_validate_pydantic_v2_linkml() -> Iterator[TaskDict]:
    """Validate each generated example against the LinkML-native Pydantic v2 models."""
    yield from _pydantic_subtasks(PYDANTIC_V2_LINKML_MODEL, "v2", generation_task="pydantic_linkml")


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
            # --preserve-names keeps original LinkML names rather than normalizing them
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

    def inject_examples_after_generation():
        from src.docs.inject_examples import inject_examples
        inject_examples(DOCS_DIR, EXAMPLES_DIR)

    return {
        "actions": [
            f"mkdir -p {DOCS_DIR}",
            uv(f"gen-doc -d {DOCS_DIR} {TOP_LEVEL}"),
            inject_examples_after_generation,
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
    """Categorize generated docs pages and write the literate-nav file → docs/nav.md

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
