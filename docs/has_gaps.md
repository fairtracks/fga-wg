

# Slot: has_gaps 


_Whether there are gaps between the sequence features (there exists at least one gap between two features on the same sequence)._





URI: [https://w3id.org/fga-wg/schema/top_level/has_gaps](https://w3id.org/fga-wg/schema/top_level/has_gaps)
Alias: has_gaps

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
| self | https://w3id.org/fga-wg/schema/top_level/has_gaps |
| native | https://w3id.org/fga-wg/schema/top_level/has_gaps |




## LinkML Source

<details>
```yaml
name: has_gaps
description: Whether there are gaps between the sequence features (there exists at
  least one gap between two features on the same sequence).
examples:
- object: true
from_schema: https://w3id.org/fga-wg/schema/top_level
rank: 1000
alias: has_gaps
domain_of:
- TrackGeometry
range: boolean
required: true

```
</details>