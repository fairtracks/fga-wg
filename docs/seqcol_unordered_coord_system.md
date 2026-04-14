---
search:
  boost: 5.0
---

# Slot: seqcol_unordered_coord_system 


_Content-derived digest that uniquely identifies the order-invariant coordinate system of the genome assembly. This digest will be shared across all coordinate systems with the same sequence names and lenghts, regardless of the order of the sequences. Usage is the order-invariant coordinate system digest can be used to uniquely describe the coordinate system of a particular genome browser instance and the annotation files that are compatible with it. Definition is the order-invariant coordinate system digest is defined as the level 1 digest of the sorted_name_length_pairs attribute of the sequence collection generated from the genome assembly._



<div data-search-exclude markdown="1">



URI: [https://w3id.org/fga-wg/schema/bundle/seqcol_unordered_coord_system](https://w3id.org/fga-wg/schema/bundle/seqcol_unordered_coord_system)
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









## Examples

| Value |
| --- |
| ga4gh:SC.sorted_name_length_pairs._dMQ5dPUNVx4OGQnDAPmGMkVRWWcYV99 |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fga-wg/schema/bundle




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/fga-wg/schema/bundle/seqcol_unordered_coord_system |
| native | https://w3id.org/fga-wg/schema/bundle/seqcol_unordered_coord_system |




## LinkML Source

<details>
```yaml
name: seqcol_unordered_coord_system
description: Content-derived digest that uniquely identifies the order-invariant coordinate
  system of the genome assembly. This digest will be shared across all coordinate
  systems with the same sequence names and lenghts, regardless of the order of the
  sequences. Usage is the order-invariant coordinate system digest can be used to
  uniquely describe the coordinate system of a particular genome browser instance
  and the annotation files that are compatible with it. Definition is the order-invariant
  coordinate system digest is defined as the level 1 digest of the sorted_name_length_pairs
  attribute of the sequence collection generated from the genome assembly.
examples:
- value: ga4gh:SC.sorted_name_length_pairs._dMQ5dPUNVx4OGQnDAPmGMkVRWWcYV99
from_schema: https://w3id.org/fga-wg/schema/bundle
rank: 1000
domain_of:
- GenomeAssembly
range: curie
required: true

```
</details></div>