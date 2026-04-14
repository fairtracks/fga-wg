---
search:
  boost: 5.0
---

# Slot: experiment_samples 


_External or internal references to samples used in the experiment. Internal references should refer to Sample objects._



<div data-search-exclude markdown="1">



URI: [https://w3id.org/fga-wg/schema/top_level/experiment_samples](https://w3id.org/fga-wg/schema/top_level/experiment_samples)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Experiment](Experiment.md) | Represents a sequencing experiment that has been carried out within a study, based on biological samples, and providing data files as output. Subsequent analysis of output data is described by the Analysis entity. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [InputSource](InputSource.md) |
| Domain Of | [Experiment](Experiment.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
| Multivalued | Yes |









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
| self | https://w3id.org/fga-wg/schema/top_level/experiment_samples |
| native | https://w3id.org/fga-wg/schema/top_level/experiment_samples |




## LinkML Source

<details>
```yaml
name: experiment_samples
description: External or internal references to samples used in the experiment. Internal
  references should refer to Sample objects.
examples:
- object:
    inputsource_ref: sample:ENCBS004ENC
    qualified_relation: prov:used
    biological_replicate_labels:
    - '1'
    - '2'
    technical_replicate_labels:
    - '1_1'
    - '2_1'
from_schema: https://w3id.org/fga-wg/schema/top_level
rank: 1000
domain_of:
- Experiment
range: InputSource
required: true
multivalued: true

```
</details></div>