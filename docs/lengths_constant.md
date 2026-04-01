

# Slot: lengths_constant 


_Whether the sequence lengths are constant (all sequence features have the same length, excluding features at the very end of a sequence)._





URI: [https://w3id.org/fga-wg/schema/top_level/lengths_constant](https://w3id.org/fga-wg/schema/top_level/lengths_constant)
Alias: lengths_constant

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
| self | https://w3id.org/fga-wg/schema/top_level/lengths_constant |
| native | https://w3id.org/fga-wg/schema/top_level/lengths_constant |




## LinkML Source

<details>
```yaml
name: lengths_constant
description: Whether the sequence lengths are constant (all sequence features have
  the same length, excluding features at the very end of a sequence).
examples:
- object: false
from_schema: https://w3id.org/fga-wg/schema/top_level
rank: 1000
alias: lengths_constant
domain_of:
- TrackGeometry
range: boolean

```
</details>