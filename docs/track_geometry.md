---
search:
  boost: 5.0
---

# Slot: track_geometry 


_Geometric properties of the sequence features in the genomic annotation file if considered as an one-dimensional genome browser track (also relevant for non-visual analyses)._



<div data-search-exclude markdown="1">



URI: [https://w3id.org/fga-wg/schema/bundle/track_geometry](https://w3id.org/fga-wg/schema/bundle/track_geometry)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [GenomicAnnotationFile](GenomicAnnotationFile.md) | Information about a genomic annotation / track file. GenomicAnnotationFile is a specification of the File entity and inherits all the fields defined in File, in addition to the fields that are specific to GenomicAnnotationFile, as detailed here. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [TrackGeometry](TrackGeometry.md) |
| Domain Of | [GenomicAnnotationFile](GenomicAnnotationFile.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |









## Examples

| Value |
| --- |
| None |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fga-wg/schema/bundle




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/fga-wg/schema/bundle/track_geometry |
| native | https://w3id.org/fga-wg/schema/bundle/track_geometry |




## LinkML Source

<details>
```yaml
name: track_geometry
description: Geometric properties of the sequence features in the genomic annotation
  file if considered as an one-dimensional genome browser track (also relevant for
  non-visual analyses).
examples:
- object:
    elements_circular: false
    elements_overlapping: false
    has_edges: false
    has_gaps: true
    has_lengths: true
    has_names: true
    has_strands: false
    has_values: true
    lengths_constant: false
    value_type: multiple
from_schema: https://w3id.org/fga-wg/schema/bundle
rank: 1000
domain_of:
- GenomicAnnotationFile
range: TrackGeometry
required: true

```
</details></div>