---
search:
  boost: 5.0
---

# Slot: analysis_protocol 


_Document describing the analysis protocol that was followed._



<div data-search-exclude markdown="1">



URI: [https://w3id.org/fga-wg/schema/bundle/analysis_protocol](https://w3id.org/fga-wg/schema/bundle/analysis_protocol)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Analysis](Analysis.md) | Represents the computational processing applied to data from a sequencing experiment, or from another analysis. This can be described at the level of individual analysis steps in a workflow/pipeline, or more generally for the workflow/pipeline as a whole. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Uriorcurie](Uriorcurie.md) |
| Domain Of | [Analysis](Analysis.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |









## Examples

| Value |
| --- |
| https://www.encodeproject.org/documents/7009beb8-340b-4e71-b9db-53bb020c7fe2/@@download/attachment/ChIP-seq_pipeline_overview.pdf |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fga-wg/schema/bundle




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/fga-wg/schema/bundle/analysis_protocol |
| native | https://w3id.org/fga-wg/schema/bundle/analysis_protocol |




## LinkML Source

<details>
```yaml
name: analysis_protocol
description: Document describing the analysis protocol that was followed.
examples:
- value: https://www.encodeproject.org/documents/7009beb8-340b-4e71-b9db-53bb020c7fe2/@@download/attachment/ChIP-seq_pipeline_overview.pdf
from_schema: https://w3id.org/fga-wg/schema/bundle
rank: 1000
domain_of:
- Analysis
range: uriorcurie

```
</details></div>