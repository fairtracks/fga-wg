---
search:
  boost: 5.0
---

# Slot: analysis_study_ref 


_Internal reference to the study within which the analysis has been carried out._



<div data-search-exclude markdown="1">



URI: [https://w3id.org/fga-wg/schema/top_level/analysis_study_ref](https://w3id.org/fga-wg/schema/top_level/analysis_study_ref)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Analysis](Analysis.md) | Represents the computational processing applied to data from a sequencing experiment, or from another analysis. This can be described at the level of individual analysis steps in a workflow/pipeline, or more generally for the workflow/pipeline as a whole. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Curie](Curie.md) |
| Domain Of | [Analysis](Analysis.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |









## Examples

| Value |
| --- |
| study:S-EPMC7391744 |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fga-wg/schema/top_level




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/fga-wg/schema/top_level/analysis_study_ref |
| native | https://w3id.org/fga-wg/schema/top_level/analysis_study_ref |




## LinkML Source

<details>
```yaml
name: analysis_study_ref
description: Internal reference to the study within which the analysis has been carried
  out.
examples:
- value: study:S-EPMC7391744
from_schema: https://w3id.org/fga-wg/schema/top_level
rank: 1000
domain_of:
- Analysis
range: curie

```
</details></div>