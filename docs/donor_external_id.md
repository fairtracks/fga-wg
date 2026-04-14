---
search:
  boost: 5.0
---

# Slot: donor_external_id 


_External, globally unique identifier for the donor/organism._



<div data-search-exclude markdown="1">



URI: [https://w3id.org/fga-wg/schema/top_level/donor_external_id](https://w3id.org/fga-wg/schema/top_level/donor_external_id)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Donor](Donor.md) | Information about the donor or complete organism from which the sample was taken. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Curie](Curie.md) |
| Domain Of | [Donor](Donor.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |









## Examples

| Value |
| --- |
| biosamples:SAMN04284578 |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fga-wg/schema/top_level




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/fga-wg/schema/top_level/donor_external_id |
| native | https://w3id.org/fga-wg/schema/top_level/donor_external_id |




## LinkML Source

<details>
```yaml
name: donor_external_id
description: External, globally unique identifier for the donor/organism.
examples:
- value: biosamples:SAMN04284578
from_schema: https://w3id.org/fga-wg/schema/top_level
rank: 1000
domain_of:
- Donor
range: curie

```
</details></div>