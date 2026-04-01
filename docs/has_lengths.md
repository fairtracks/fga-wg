

# Slot: has_lengths 


_Whether the sequence features have lengths (at least one feature spans more than 1 base pair)._





URI: [https://w3id.org/fga-wg/schema/top_level/has_lengths](https://w3id.org/fga-wg/schema/top_level/has_lengths)
Alias: has_lengths

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
| self | https://w3id.org/fga-wg/schema/top_level/has_lengths |
| native | https://w3id.org/fga-wg/schema/top_level/has_lengths |




## LinkML Source

<details>
```yaml
name: has_lengths
description: Whether the sequence features have lengths (at least one feature spans
  more than 1 base pair).
examples:
- object: true
from_schema: https://w3id.org/fga-wg/schema/top_level
rank: 1000
alias: has_lengths
domain_of:
- TrackGeometry
range: boolean
required: true

```
</details>