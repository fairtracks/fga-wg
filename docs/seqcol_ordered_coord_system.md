---
search:
  boost: 5.0
---

# Slot: seqcol_ordered_coord_system 


_Content-derived digest that uniquely identifies the ordered coordinate system of the genome assembly. (Coordinate systems with the same sequence names and lengths, but where the sequences are ordered differently, will have different ordered digests.). Usage is the ordered coordinate system digest can be used to uniquely generate a chromSizes file, useful in a number of analysis tools. Definition is the ordered coordinate system digest is defined as the level 1 digest of the name_length_pairs attribute of the sequence collection generated from the genome assembly._



<div data-search-exclude markdown="1">



URI: [https://w3id.org/fga-wg/schema/top_level/seqcol_ordered_coord_system](https://w3id.org/fga-wg/schema/top_level/seqcol_ordered_coord_system)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [GenomeAssembly](GenomeAssembly.md) | Information about of the exact genome assembly used to generate the annotatio... |  no  |






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









## Examples

| Value |
| --- |
| ga4gh:SC.name_length_pairs.Yyz0Expaluj09xdDYg2Y6VOApvjg05Hf |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fga-wg/schema/top_level




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/fga-wg/schema/top_level/seqcol_ordered_coord_system |
| native | https://w3id.org/fga-wg/schema/top_level/seqcol_ordered_coord_system |




## LinkML Source

<details>
```yaml
name: seqcol_ordered_coord_system
description: Content-derived digest that uniquely identifies the ordered coordinate
  system of the genome assembly. (Coordinate systems with the same sequence names
  and lengths, but where the sequences are ordered differently, will have different
  ordered digests.). Usage is the ordered coordinate system digest can be used to
  uniquely generate a chromSizes file, useful in a number of analysis tools. Definition
  is the ordered coordinate system digest is defined as the level 1 digest of the
  name_length_pairs attribute of the sequence collection generated from the genome
  assembly.
examples:
- value: ga4gh:SC.name_length_pairs.Yyz0Expaluj09xdDYg2Y6VOApvjg05Hf
from_schema: https://w3id.org/fga-wg/schema/top_level
rank: 1000
domain_of:
- GenomeAssembly
range: curie
required: true

```
</details></div>