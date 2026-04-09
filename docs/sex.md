---
search:
  boost: 5.0
---

# Slot: sex 


_Biological sex of the donor/organism._



<div data-search-exclude markdown="1">



URI: [https://w3id.org/fga-wg/schema/top_level/sex](https://w3id.org/fga-wg/schema/top_level/sex)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Donor](Donor.md) | Information about the donor or complete organism from which the sample was ta... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Term](Term.md) |
| Domain Of | [Donor](Donor.md) |

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
| self | https://w3id.org/fga-wg/schema/top_level/sex |
| native | https://w3id.org/fga-wg/schema/top_level/sex |




## LinkML Source

<details>
```yaml
name: sex
description: Biological sex of the donor/organism.
examples:
- object:
    id: CARO:0000027
    label: male organism
from_schema: https://w3id.org/fga-wg/schema/top_level
rank: 1000
domain_of:
- Donor
range: Term

```
</details></div>