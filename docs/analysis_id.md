---
search:
  boost: 5.0
---

# Slot: analysis_id 


_Internal identifier for the experiment (unique within the metadata deposit). _



<div data-search-exclude markdown="1">



URI: [https://w3id.org/fga-wg/schema/top_level/analysis_id](https://w3id.org/fga-wg/schema/top_level/analysis_id)
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
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Identifier | Yes |











## Examples

| Value |
| --- |
| analysis:ENCAN718KHT |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fga-wg/schema/top_level




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/fga-wg/schema/top_level/analysis_id |
| native | https://w3id.org/fga-wg/schema/top_level/analysis_id |




## LinkML Source

<details>
```yaml
name: analysis_id
description: 'Internal identifier for the experiment (unique within the metadata deposit). '
examples:
- value: analysis:ENCAN718KHT
from_schema: https://w3id.org/fga-wg/schema/top_level
rank: 1000
identifier: true
domain_of:
- Analysis
range: curie
required: true

```
</details></div>