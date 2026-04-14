---
search:
  boost: 5.0
---

# Slot: molecule_type 


_Specifies the type of source material that is being sequenced._



<div data-search-exclude markdown="1">



URI: [https://w3id.org/fga-wg/schema/bundle/molecule_type](https://w3id.org/fga-wg/schema/bundle/molecule_type)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Experiment](Experiment.md) | Represents a sequencing experiment that has been carried out within a study, based on biological samples, and providing data files as output. Subsequent analysis of output data is described by the Analysis entity. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Term](Term.md) |
| Domain Of | [Experiment](Experiment.md) |

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


* from schema: https://w3id.org/fga-wg/schema/bundle




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/fga-wg/schema/bundle/molecule_type |
| native | https://w3id.org/fga-wg/schema/bundle/molecule_type |




## LinkML Source

<details>
```yaml
name: molecule_type
description: Specifies the type of source material that is being sequenced.
examples:
- object:
    id: SO:0000991
    label: genomic_DNA
from_schema: https://w3id.org/fga-wg/schema/bundle
rank: 1000
domain_of:
- Experiment
range: Term
required: true

```
</details></div>