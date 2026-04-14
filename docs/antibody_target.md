---
search:
  boost: 5.0
---

# Slot: antibody_target 


_The target of the antibody used in the experiment._



<div data-search-exclude markdown="1">



URI: [https://w3id.org/fga-wg/schema/bundle/antibody_target](https://w3id.org/fga-wg/schema/bundle/antibody_target)
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
| self | https://w3id.org/fga-wg/schema/bundle/antibody_target |
| native | https://w3id.org/fga-wg/schema/bundle/antibody_target |




## LinkML Source

<details>
```yaml
name: antibody_target
description: The target of the antibody used in the experiment.
examples:
- object:
    id: SO:0001707
    label: H3K9Me3
from_schema: https://w3id.org/fga-wg/schema/bundle
rank: 1000
domain_of:
- Experiment
range: Term

```
</details></div>