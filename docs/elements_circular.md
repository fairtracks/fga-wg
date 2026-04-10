---
search:
  boost: 5.0
---

# Slot: elements_circular 


_Whether the sequence features have circular coordinates (at least one feature that cross a sequence border)._



<div data-search-exclude markdown="1">



URI: [https://w3id.org/fga-wg/schema/top_level/elements_circular](https://w3id.org/fga-wg/schema/top_level/elements_circular)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [TrackGeometry](TrackGeometry.md) | Overall geometric properties of the sequence features in the genomic annotati... |  no  |






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
| self | https://w3id.org/fga-wg/schema/top_level/elements_circular |
| native | https://w3id.org/fga-wg/schema/top_level/elements_circular |




## LinkML Source

<details>
```yaml
name: elements_circular
description: Whether the sequence features have circular coordinates (at least one
  feature that cross a sequence border).
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