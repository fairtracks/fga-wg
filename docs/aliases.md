---
search:
  boost: 5.0
---

# Slot: aliases 


_Human-readable aliases of the genome assembly. Can be imprecise, as preciseness is enforced in the other fields._



<div data-search-exclude markdown="1">



URI: [https://w3id.org/fga-wg/schema/bundle/aliases](https://w3id.org/fga-wg/schema/bundle/aliases)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [GenomeAssembly](GenomeAssembly.md) | Information about of the exact genome assembly used to generate the annotation file, defining the genomic coordinate system for the sequence features. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Curie](Curie.md) |
| Domain Of | [GenomeAssembly](GenomeAssembly.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
| Multivalued | Yes |









## Examples

| Value |
| --- |
| GRCh38_no_alt_analysis_set_GCA_000001405.15 |
| GRCh38 |
| hg38 |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fga-wg/schema/bundle




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/fga-wg/schema/bundle/aliases |
| native | https://w3id.org/fga-wg/schema/bundle/aliases |




## LinkML Source

<details>
```yaml
name: aliases
description: Human-readable aliases of the genome assembly. Can be imprecise, as preciseness
  is enforced in the other fields.
examples:
- value: GRCh38_no_alt_analysis_set_GCA_000001405.15
- value: GRCh38
- value: hg38
from_schema: https://w3id.org/fga-wg/schema/bundle
rank: 1000
domain_of:
- GenomeAssembly
range: curie
required: true
multivalued: true

```
</details></div>