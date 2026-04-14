"""
Post-process generated documentation to inject example JSON for each class.

This script reads the generated markdown files and inserts example JSON
snippets after the class description and before the search-excluded content.
"""
import json
from pathlib import Path


def inject_examples(docs_dir: Path, examples_dir: Path) -> None:
    """Inject example JSON content into generated markdown files.

    For each class documentation file, if an example JSON exists,
    insert it as a collapsible section after the description.
    """
    if not examples_dir.exists():
        print(f"Examples directory not found: {examples_dir}")
        return

    for md_file in docs_dir.glob("*.md"):
        # Skip non-class files (those starting with lowercase)
        if md_file.stem[0].islower():
            continue

        # Check if example exists
        example_file = examples_dir / f"{md_file.stem}.json"
        if not example_file.exists():
            continue

        try:
            # Read the example
            with open(example_file) as f:
                example = json.load(f)
            example_json = json.dumps(example, indent=2)
        except (json.JSONDecodeError, IOError) as e:
            print(f"Error reading example {example_file}: {e}")
            continue

        # Read the markdown file
        try:
            content = md_file.read_text()
        except IOError as e:
            print(f"Error reading {md_file}: {e}")
            continue

        # Find insertion point: after the mermaid diagram closes (```\n\n\n)
        # Look for the pattern of closing ``` followed by blank lines
        insertion_marker = "```\n\n\n\n"

        if insertion_marker not in content:
            print(f"Warning: {md_file.name} has no mermaid block ending, skipping")
            continue

        # Create the example section
        example_section = f"""## Example

<details>
<summary>Example JSON</summary>

```json
{example_json}
```
</details>


"""

        # Insert after the mermaid block closes
        new_content = content.replace(
            insertion_marker,
            insertion_marker + example_section,
            1
        )

        # Write back
        try:
            md_file.write_text(new_content)
            print(f"✓ {md_file.name}: added example")
        except IOError as e:
            print(f"Error writing {md_file}: {e}")


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 2:
        docs_dir = Path(sys.argv[1])
        examples_dir = Path(sys.argv[2])
    else:
        # Default paths
        docs_dir = Path(__file__).parent.parent.parent / "docs"
        examples_dir = Path(__file__).parent.parent.parent / "generated" / "examples"

    inject_examples(docs_dir, examples_dir)

