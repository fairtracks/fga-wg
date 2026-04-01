"""Generate the MkDocs literate-nav file (docs/nav.md).

Uses SchemaView to categorise all generated documentation pages by type and
writes a nav.md that mkdocs-literate-nav uses to build a tabbed navigation:

    Introduction | Classes | Slots | Types & Enums
"""
from pathlib import Path


# Pages that have fixed positions at the top of the nav — excluded from the
# category scan below.
_FIXED_PAGES = {"index.md", "overview.md", "nav.md"}


def generate_nav(schema_path: Path, docs_dir: Path, target: Path) -> None:
    """Categorise generated docs pages and write the literate-nav file.

    Args:
        schema_path: Path to the top-level LinkML schema YAML file.
        docs_dir:    Directory containing the generated Markdown pages.
        target:      Output path for the nav.md file (typically docs/nav.md).
    """
    from linkml_runtime.utils.schemaview import SchemaView

    sv = SchemaView(str(schema_path))

    class_names = set(sv.all_classes().keys())
    slot_names  = set(sv.all_slots().keys())
    type_names  = set(sv.all_types().keys())
    enum_names  = set(sv.all_enums().keys())

    classes: list[str] = []
    slots: list[str]   = []
    types_enums: list[str] = []
    other: list[str]   = []

    for p in sorted(docs_dir.iterdir()):
        if not p.name.endswith(".md") or p.name in _FIXED_PAGES or p.name.startswith("."):
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

    def entry(name: str) -> str:
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

