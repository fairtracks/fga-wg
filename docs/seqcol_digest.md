---
search:
  boost: 5.0
---

# Slot: seqcol_digest 


_Top-level sequence collection digest according to the GA4GH refget, Sequence Collections standard (v1.0). This a globally unique identifier for the genome assembly, algorithmically derivable from the genome assembly content. Usage is to uniquely identify the exact genome assembly used and allow detailed comparisons across genome assembly variants (say, variants of the GRCh38 assembly)._



<div data-search-exclude markdown="1">



URI: [https://w3id.org/fga-wg/schema/top_level/seqcol_digest](https://w3id.org/fga-wg/schema/top_level/seqcol_digest)
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
### Slot Characteristics

| Property | Value |
| --- | --- |
| Identifier | Yes |











## Examples

| Value |
| --- |
| ga4gh:SC.EiFob05aCWgVU_B_Ae0cypnQut3cxUP1 |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fga-wg/schema/top_level




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/fga-wg/schema/top_level/seqcol_digest |
| native | https://w3id.org/fga-wg/schema/top_level/seqcol_digest |




## LinkML Source

<details>
```yaml
name: seqcol_digest
description: Top-level sequence collection digest according to the GA4GH refget, Sequence
  Collections standard (v1.0). This a globally unique identifier for the genome assembly,
  algorithmically derivable from the genome assembly content. Usage is to uniquely
  identify the exact genome assembly used and allow detailed comparisons across genome
  assembly variants (say, variants of the GRCh38 assembly).
examples:
- value: ga4gh:SC.EiFob05aCWgVU_B_Ae0cypnQut3cxUP1
from_schema: https://w3id.org/fga-wg/schema/top_level
rank: 1000
identifier: true
domain_of:
- GenomeAssembly
range: curie
required: true

```
</details></div>