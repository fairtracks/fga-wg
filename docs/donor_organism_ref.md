

# Slot: donor_organism_ref 


_Internal reference to the donor/organism from which the biospecimen/sample was taken._





URI: [https://w3id.org/fga-wg/schema/top_level/donor_organism_ref](https://w3id.org/fga-wg/schema/top_level/donor_organism_ref)
Alias: donor_organism_ref

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Sample](Sample.md) | Information about a biospecimen/sample used as raw material for lab experimen... |  no  |






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


* from schema: https://w3id.org/fga-wg/schema/top_level




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/fga-wg/schema/top_level/donor_organism_ref |
| native | https://w3id.org/fga-wg/schema/top_level/donor_organism_ref |




## LinkML Source

<details>
```yaml
name: donor_organism_ref
description: Internal reference to the donor/organism from which the biospecimen/sample
  was taken.
examples:
- value: donor:ENCDO001AAA
from_schema: https://w3id.org/fga-wg/schema/top_level
rank: 1000
alias: donor_organism_ref
domain_of:
- Sample
range: curie
required: true

```
</details>