---
search:
  boost: 5.0
---

# Slot: instrument 


_Technology platform used to perform nucleic acid sequencing, including name and/or number associated with a specific sequencing instrument model. It is recommended to be as specific as possible for this property (e.g. if the model/revision are available, providing that instead of just the instrument maker)._



<div data-search-exclude markdown="1">



URI: [https://w3id.org/fga-wg/schema/top_level/instrument](https://w3id.org/fga-wg/schema/top_level/instrument)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Experiment](Experiment.md) | Represents a sequencing experiment that has been carried out within a study, ... |  no  |






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


* from schema: https://w3id.org/fga-wg/schema/top_level




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/fga-wg/schema/top_level/instrument |
| native | https://w3id.org/fga-wg/schema/top_level/instrument |




## LinkML Source

<details>
```yaml
name: instrument
description: Technology platform used to perform nucleic acid sequencing, including
  name and/or number associated with a specific sequencing instrument model. It is
  recommended to be as specific as possible for this property (e.g. if the model/revision
  are available, providing that instead of just the instrument maker).
examples:
- object:
    id: obi:OBI_0002128
    label: Illumina Genome Analyzer
from_schema: https://w3id.org/fga-wg/schema/top_level
rank: 1000
domain_of:
- Experiment
range: Term

```
</details></div>