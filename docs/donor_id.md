

# Slot: donor_id 


_Internal identifier for the donor/organism (unique within the metadata deposit). _





URI: [https://w3id.org/fga-wg/schema/top_level/donor_id](https://w3id.org/fga-wg/schema/top_level/donor_id)
Alias: donor_id

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Donor](Donor.md) | Information about the donor or complete organism from which the sample was ta... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Curie](Curie.md) |
| Domain Of | [Donor](Donor.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Identifier | Yes |











## Examples

| Value |
| --- |
| donor:ENCDO001AAA |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fga-wg/schema/top_level




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/fga-wg/schema/top_level/donor_id |
| native | https://w3id.org/fga-wg/schema/top_level/donor_id |




## LinkML Source

<details>
```yaml
name: donor_id
description: 'Internal identifier for the donor/organism (unique within the metadata
  deposit). '
examples:
- value: donor:ENCDO001AAA
from_schema: https://w3id.org/fga-wg/schema/top_level
rank: 1000
identifier: true
alias: donor_id
domain_of:
- Donor
range: curie
required: true

```
</details>