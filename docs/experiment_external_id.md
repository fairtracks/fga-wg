---
search:
  boost: 5.0
---

# Slot: experiment_external_id 


_External, globally unique identifier for the experiment._



<div data-search-exclude markdown="1">



URI: [https://w3id.org/fga-wg/schema/bundle/experiment_external_id](https://w3id.org/fga-wg/schema/bundle/experiment_external_id)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Experiment](Experiment.md) | Represents a sequencing experiment that has been carried out within a study, based on biological samples, and providing data files as output. Subsequent analysis of output data is described by the Analysis entity. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Curie](Curie.md) |
| Domain Of | [Experiment](Experiment.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |









## Examples

| Value |
| --- |
| encode:ENCSR000DPJ |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fga-wg/schema/bundle




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/fga-wg/schema/bundle/experiment_external_id |
| native | https://w3id.org/fga-wg/schema/bundle/experiment_external_id |




## LinkML Source

<details>
```yaml
name: experiment_external_id
description: External, globally unique identifier for the experiment.
examples:
- value: encode:ENCSR000DPJ
from_schema: https://w3id.org/fga-wg/schema/bundle
rank: 1000
domain_of:
- Experiment
range: curie

```
</details></div>