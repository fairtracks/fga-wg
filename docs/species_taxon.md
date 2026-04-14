---
search:
  boost: 5.0
---

# Slot: species_taxon 


_Taxonomical classification of the species of the donor/organism._



<div data-search-exclude markdown="1">



URI: [https://w3id.org/fga-wg/schema/top_level/species_taxon](https://w3id.org/fga-wg/schema/top_level/species_taxon)
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
| self | https://w3id.org/fga-wg/schema/top_level/species_taxon |
| native | https://w3id.org/fga-wg/schema/top_level/species_taxon |




## LinkML Source

<details>
```yaml
name: species_taxon
description: Taxonomical classification of the species of the donor/organism.
examples:
- object:
    id: NCBITaxon:9606
    label: Homo sapiens
from_schema: https://w3id.org/fga-wg/schema/top_level
rank: 1000
domain_of:
- Donor
range: Term
required: true

```
</details></div>