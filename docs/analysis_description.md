---
search:
  boost: 5.0
---

# Slot: analysis_description 


_Human-readable description of the analysis._



<div data-search-exclude markdown="1">



URI: [https://w3id.org/fga-wg/schema/bundle/analysis_description](https://w3id.org/fga-wg/schema/bundle/analysis_description)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Analysis](Analysis.md) | Represents the computational processing applied to data from a sequencing experiment, or from another analysis. This can be described at the level of individual analysis steps in a workflow/pipeline, or more generally for the workflow/pipeline as a whole. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Analysis](Analysis.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |









## Examples

| Value |
| --- |
| ENCODE3 ChIP-seq pipeline on GRCH38 with replicated peak calling using MACS. |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fga-wg/schema/bundle




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/fga-wg/schema/bundle/analysis_description |
| native | https://w3id.org/fga-wg/schema/bundle/analysis_description |




## LinkML Source

<details>
```yaml
name: analysis_description
description: Human-readable description of the analysis.
examples:
- value: ENCODE3 ChIP-seq pipeline on GRCH38 with replicated peak calling using MACS.
from_schema: https://w3id.org/fga-wg/schema/bundle
rank: 1000
domain_of:
- Analysis
range: string

```
</details></div>