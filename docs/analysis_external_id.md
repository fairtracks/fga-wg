---
search:
  boost: 5.0
---

# Slot: analysis_external_id 


_External, globally unique identifier for the experiment._



<div data-search-exclude markdown="1">



URI: [https://w3id.org/fga-wg/schema/top_level/analysis_external_id](https://w3id.org/fga-wg/schema/top_level/analysis_external_id)
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
| encode:ENCAN718KHT |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fga-wg/schema/top_level




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/fga-wg/schema/top_level/analysis_external_id |
| native | https://w3id.org/fga-wg/schema/top_level/analysis_external_id |




## LinkML Source

<details>
```yaml
name: analysis_external_id
description: External, globally unique identifier for the experiment.
examples:
- value: encode:ENCAN718KHT
from_schema: https://w3id.org/fga-wg/schema/top_level
rank: 1000
domain_of:
- Analysis
range: curie

```
</details></div>