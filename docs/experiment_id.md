---
search:
  boost: 5.0
---

# Slot: experiment_id 


_Internal identifier for the experiment (unique within the metadata deposit)._



<div data-search-exclude markdown="1">



URI: [https://w3id.org/fga-wg/schema/top_level/experiment_id](https://w3id.org/fga-wg/schema/top_level/experiment_id)
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
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Identifier | Yes |











## Examples

| Value |
| --- |
| experiment:ENCSR000DPJ |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fga-wg/schema/top_level




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/fga-wg/schema/top_level/experiment_id |
| native | https://w3id.org/fga-wg/schema/top_level/experiment_id |




## LinkML Source

<details>
```yaml
name: experiment_id
description: Internal identifier for the experiment (unique within the metadata deposit).
examples:
- value: experiment:ENCSR000DPJ
from_schema: https://w3id.org/fga-wg/schema/top_level
rank: 1000
identifier: true
domain_of:
- Experiment
range: curie
required: true

```
</details></div>