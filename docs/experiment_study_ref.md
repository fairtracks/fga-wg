

# Slot: experiment_study_ref 


_Internal reference to the study within which the experiment has been carried out._





URI: [https://w3id.org/fga-wg/schema/top_level/experiment_study_ref](https://w3id.org/fga-wg/schema/top_level/experiment_study_ref)
Alias: experiment_study_ref

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Experiment](Experiment.md) | Represents a sequencing experiment that has been carried out within a study, ... |  no  |






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









## Examples

| Value |
| --- |
| study:E-GEOD-35583 |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fga-wg/schema/top_level




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/fga-wg/schema/top_level/experiment_study_ref |
| native | https://w3id.org/fga-wg/schema/top_level/experiment_study_ref |




## LinkML Source

<details>
```yaml
name: experiment_study_ref
description: Internal reference to the study within which the experiment has been
  carried out.
examples:
- value: study:E-GEOD-35583
from_schema: https://w3id.org/fga-wg/schema/top_level
rank: 1000
alias: experiment_study_ref
domain_of:
- Experiment
range: curie
required: true

```
</details>