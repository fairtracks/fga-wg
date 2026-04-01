

# Slot: has_names 


_Whether the sequence features are named (at least one feature has a name)._





URI: [https://w3id.org/fga-wg/schema/top_level/has_names](https://w3id.org/fga-wg/schema/top_level/has_names)
Alias: has_names

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
| self | https://w3id.org/fga-wg/schema/top_level/has_names |
| native | https://w3id.org/fga-wg/schema/top_level/has_names |




## LinkML Source

<details>
```yaml
name: has_names
description: Whether the sequence features are named (at least one feature has a name).
examples:
- object: true
from_schema: https://w3id.org/fga-wg/schema/top_level
rank: 1000
alias: has_names
domain_of:
- TrackGeometry
range: boolean
required: true

```
</details>