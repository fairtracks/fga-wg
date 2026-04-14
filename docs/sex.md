---
search:
  boost: 5.0
---

# Slot: sex 


_Biological sex of the donor/organism._



<div data-search-exclude markdown="1">



URI: [https://w3id.org/fga-wg/schema/bundle/sex](https://w3id.org/fga-wg/schema/bundle/sex)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Donor](Donor.md) | Information about the donor or complete organism from which the sample was taken. |  no  |






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


* from schema: https://w3id.org/fga-wg/schema/bundle




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/fga-wg/schema/bundle/sex |
| native | https://w3id.org/fga-wg/schema/bundle/sex |




## LinkML Source

<details>
```yaml
name: sex
description: Biological sex of the donor/organism.
examples:
- object:
    id: CARO:0000027
    label: male organism
from_schema: https://w3id.org/fga-wg/schema/bundle
rank: 1000
domain_of:
- Donor
range: Term

```
</details></div>