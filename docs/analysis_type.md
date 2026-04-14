---
search:
  boost: 5.0
---

# Slot: analysis_type 


_The type of analysis carried out._



<div data-search-exclude markdown="1">



URI: [https://w3id.org/fga-wg/schema/top_level/analysis_type](https://w3id.org/fga-wg/schema/top_level/analysis_type)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Analysis](Analysis.md) | Represents the computational processing applied to data from a sequencing experiment, or from another analysis. This can be described at the level of individual analysis steps in a workflow/pipeline, or more generally for the workflow/pipeline as a whole. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Term](Term.md) |
| Domain Of | [Analysis](Analysis.md) |

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


* from schema: https://w3id.org/fga-wg/schema/top_level




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/fga-wg/schema/top_level/analysis_type |
| native | https://w3id.org/fga-wg/schema/top_level/analysis_type |




## LinkML Source

<details>
```yaml
name: analysis_type
description: The type of analysis carried out.
examples:
- object:
    id: edam:operation_3222
    label: Peak calling
from_schema: https://w3id.org/fga-wg/schema/top_level
rank: 1000
domain_of:
- Analysis
range: Term
required: true

```
</details></div>