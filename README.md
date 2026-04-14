# FAIRification of Genomic Annotations WG (FGA-WG)

Main repository for the FAIRification of Genomic Annotations WG in the
[Research Data Alliance (RDA)](https://www.rd-alliance.org/).

📖 **[Schema documentation](https://fairtracks.github.io/fga-wg/)**

## Overview

This repository hosts the FGA-WG [LinkML](https://linkml.io/) schema — a data model
for harmonised metadata describing genomic annotation files.  From the schema, the
following artifacts are generated automatically:

| Artifact | Location |
|----------|----------|
| JSON Schema | `generated/schema.json` |
| TSV class/slot summary | `generated/schema_summary.tsv` |
| HTML documentation site | [fairtracks.github.io/fga-wg](https://fairtracks.github.io/fga-wg/) |

## Conceptual illustration of the infrastructure to be defined by the FGA-WG

![Initial vision of the FGA-WG core infrastructure](material/images/fga_wg_overview.png)

## Quick start

```bash
git clone git@github.com:fairtracks/fga-wg.git
cd fga-wg
uv sync           # install all dependencies
uv run doit       # validate schema and regenerate all artifacts
uv run doit serve # preview the documentation at http://127.0.0.1:8000
```

See [CONTRIBUTING.md](CONTRIBUTING.md) for a full guide to the development workflow.
