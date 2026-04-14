---
search:
  boost: 5.0
---

# Slot: donor_organism_ref 


_Internal reference to the donor/organism from which the biospecimen/sample was taken._



<div data-search-exclude markdown="1">



URI: [https://w3id.org/fga-wg/schema/bundle/donor_organism_ref](https://w3id.org/fga-wg/schema/bundle/donor_organism_ref)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Sample](Sample.md) | Information about a biospecimen/sample used as raw material for lab experiments. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Curie](Curie.md) |
| Domain Of | [Sample](Sample.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |









## Examples

| Value |
| --- |
| donor:ENCDO001AAA |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fga-wg/schema/bundle




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/fga-wg/schema/bundle/donor_organism_ref |
| native | https://w3id.org/fga-wg/schema/bundle/donor_organism_ref |




## LinkML Source

<details>
```yaml
name: donor_organism_ref
description: Internal reference to the donor/organism from which the biospecimen/sample
  was taken.
examples:
- value: donor:ENCDO001AAA
from_schema: https://w3id.org/fga-wg/schema/bundle
rank: 1000
domain_of:
- Sample
range: curie
required: true

```
</details></div>