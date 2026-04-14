---
search:
  boost: 5.0
---

# Slot: edges_denote_parents 


_Whether the edges linking sequence features denote a parent-child relationship (all edges between sequence features denote parent-child relationships such as genes to exons, i.e. where the child is fully covered by the parent)._



<div data-search-exclude markdown="1">



URI: [https://w3id.org/fga-wg/schema/bundle/edges_denote_parents](https://w3id.org/fga-wg/schema/bundle/edges_denote_parents)
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










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fga-wg/schema/bundle




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/fga-wg/schema/bundle/edges_denote_parents |
| native | https://w3id.org/fga-wg/schema/bundle/edges_denote_parents |




## LinkML Source

<details>
```yaml
name: edges_denote_parents
description: Whether the edges linking sequence features denote a parent-child relationship
  (all edges between sequence features denote parent-child relationships such as genes
  to exons, i.e. where the child is fully covered by the parent).
from_schema: https://w3id.org/fga-wg/schema/bundle
rank: 1000
domain_of:
- TrackGeometry
range: boolean

```
</details></div>