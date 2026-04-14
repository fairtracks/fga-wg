---
search:
  boost: 5.0
---

# Slot: has_gaps 


_Whether there are gaps between the sequence features (there exists at least one gap between two features on the same sequence)._



<div data-search-exclude markdown="1">



URI: [https://w3id.org/fga-wg/schema/top_level/has_gaps](https://w3id.org/fga-wg/schema/top_level/has_gaps)
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
| True |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fga-wg/schema/top_level




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/fga-wg/schema/top_level/has_gaps |
| native | https://w3id.org/fga-wg/schema/top_level/has_gaps |




## LinkML Source

<details>
```yaml
name: has_gaps
description: Whether there are gaps between the sequence features (there exists at
  least one gap between two features on the same sequence).
examples:
- value: 'True'
from_schema: https://w3id.org/fga-wg/schema/top_level
rank: 1000
domain_of:
- TrackGeometry
range: boolean
required: true

```
</details></div>