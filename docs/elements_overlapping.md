

# Slot: elements_overlapping 


_Whether the sequence features are overlapping (at least one base pair is simultaneously covered by two sequence features)._





URI: [https://w3id.org/fga-wg/schema/top_level/elements_overlapping](https://w3id.org/fga-wg/schema/top_level/elements_overlapping)
Alias: elements_overlapping

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
| None |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fga-wg/schema/top_level




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/fga-wg/schema/top_level/elements_overlapping |
| native | https://w3id.org/fga-wg/schema/top_level/elements_overlapping |




## LinkML Source

<details>
```yaml
name: elements_overlapping
description: Whether the sequence features are overlapping (at least one base pair
  is simultaneously covered by two sequence features).
examples:
- object: false
from_schema: https://w3id.org/fga-wg/schema/top_level
rank: 1000
alias: elements_overlapping
domain_of:
- TrackGeometry
range: boolean
required: true

```
</details>