---
search:
  boost: 5.0
---

# Slot: elements_overlapping 


_Whether the sequence features are overlapping (at least one base pair is simultaneously covered by two sequence features)._



<div data-search-exclude markdown="1">



URI: [https://w3id.org/fga-wg/schema/bundle/elements_overlapping](https://w3id.org/fga-wg/schema/bundle/elements_overlapping)
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


* from schema: https://w3id.org/fga-wg/schema/bundle




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/fga-wg/schema/bundle/elements_overlapping |
| native | https://w3id.org/fga-wg/schema/bundle/elements_overlapping |




## LinkML Source

<details>
```yaml
name: elements_overlapping
description: Whether the sequence features are overlapping (at least one base pair
  is simultaneously covered by two sequence features).
examples:
- value: 'False'
from_schema: https://w3id.org/fga-wg/schema/bundle
rank: 1000
domain_of:
- TrackGeometry
range: boolean
required: true

```
</details></div>