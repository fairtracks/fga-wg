"""Generate the schema overview page (docs/overview.md).

Combines the Mermaid ER diagram and the PlantUML class diagram source into a
single MkDocs page.  The PlantUML block is rendered at build time via the
mkdocs-kroki-plugin (```kroki-plantuml fences).
"""
from pathlib import Path


def create_overview(erdiagram_src: Path, plantuml_src: Path, target: Path) -> None:
    """Combine the ER diagram and PlantUML source into docs/overview.md."""
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

