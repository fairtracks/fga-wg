---
search:
  boost: 5.0
---

# Slot: has_edges 


_Whether the sequence features are linked across positions (at least one edge between features exists)._



<div data-search-exclude markdown="1">



URI: [https://w3id.org/fga-wg/schema/top_level/has_edges](https://w3id.org/fga-wg/schema/top_level/has_edges)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [TrackGeometry](TrackGeometry.md) | Overall geometric properties of the sequence features in the genomic annotation file if considered as an one-dimensional genome browser track, in line with the track type delineations from Gundersen et. al, 2011. While conceptually based on visual characteristics, these properties are also useful to e.g. select relevant annotation files for non-visual analyses. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Boolean](Boolean.md) |
| Domain Of | [TrackGeometry](TrackGeometry.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |









## Examples

| Value |
| --- |
| False |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fga-wg/schema/top_level




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/fga-wg/schema/top_level/has_edges |
| native | https://w3id.org/fga-wg/schema/top_level/has_edges |




## LinkML Source

<details>
```yaml
name: has_edges
description: Whether the sequence features are linked across positions (at least one
  edge between features exists).
examples:
- value: 'False'
from_schema: https://w3id.org/fga-wg/schema/top_level
rank: 1000
domain_of:
- TrackGeometry
range: boolean
required: true

```
</details></div>