# FAIR Genomic Annotation Schema

This repository contains the LinkML schema for the RDA FAIR Genomic Annotation Working Group (FGA-WG).

## Overview

The FAIR Genomic Annotation schema provides a standardized way to describe genomic annotations and their associated biological samples. This schema enables interoperability between different genomic annotation resources and supports the FAIR (Findable, Accessible, Interoperable, and Reusable) principles for scientific data.

## Schema Structure

The schema is organized into several modules:

- **core.yaml**: The main schema that imports all other components
- **annotation.yaml**: Defines the GenomicAnnotation class and related slots
- **sample.yaml**: Defines the Sample class and related biological entities
- **enums.yaml**: Contains enumerated types for controlled vocabularies

## Key Classes

The schema includes the following key classes:

### GenomicAnnotation

Represents genomic features or measurements aligned to a reference genome assembly, such as:
- ChIP-seq peaks
- RNA-seq expression data
- Variant calls
- Genome segmentations

### Sample

Describes the biological material used for the genomic annotation, including:
- Biospecimen classification (cell line, tissue, etc.)
- Cell types
- Phenotype information
- Donor information
- Replicate details

## Usage

### Installation

```bash
pip install fga-schema
```

### Working with the Schema

Using Python:

```python
from fga_schema.datamodel import GenomicAnnotation, Sample

# Create a sample
sample = Sample(
    global_id="https://identifiers.org/biosample:SAMN12345678",
    local_id="ENCBS456DEF",
    biospecimen_classification="cell_line"
)

# Create an annotation
annotation = GenomicAnnotation(
    global_id="https://identifiers.org/geo:GSM1234567",
    local_id="ENCSR123ABC",
    desc_short_label="H3K4me3 ChIP-seq K562",
    genome_assembly_alias="GRCh38",
    sample=sample
)
```

## Examples

See the `examples/` directory for example data.

## Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for details.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

This schema is developed by the RDA FAIR Genomic Annotation Working Group.
