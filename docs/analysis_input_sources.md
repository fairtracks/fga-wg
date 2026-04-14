---
search:
  boost: 5.0
---

# Slot: analysis_input_sources 


_External or internal references to sources for the input data analyzed. Internal references should lead to FileCollection, File, Experiment, or Analysis objects._



<div data-search-exclude markdown="1">



URI: [https://w3id.org/fga-wg/schema/top_level/analysis_input_sources](https://w3id.org/fga-wg/schema/top_level/analysis_input_sources)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Analysis](Analysis.md) | Represents the computational processing applied to data from a sequencing experiment, or from another analysis. This can be described at the level of individual analysis steps in a workflow/pipeline, or more generally for the workflow/pipeline as a whole. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [InputSource](InputSource.md) |
| Domain Of | [Analysis](Analysis.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
| Multivalued | Yes |









## Examples

| Value |
| --- |
| None |
| None |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fga-wg/schema/top_level




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/fga-wg/schema/top_level/analysis_input_sources |
| native | https://w3id.org/fga-wg/schema/top_level/analysis_input_sources |




## LinkML Source

<details>
```yaml
name: analysis_input_sources
description: External or internal references to sources for the input data analyzed.
  Internal references should lead to FileCollection, File, Experiment, or Analysis
  objects.
examples:
- object:
    inputsource_ref: experiment:ENCSR000DPJ
    qualified_relation: prov:wasInformedBy
    biological_replicate_labels:
    - '1'
    - '2'
    technical_replicate_labels:
    - '1_1'
    - '2_1'
- object:
    inputsource_external_ref: https://www.encodeproject.org/files/GRCh38_no_alt_analysis_set_GCA_000001405.15
    qualified_relation: https://bioschemas.org/FormalParameter
    biological_replicate_labels:
    - '1'
    - '2'
    technical_replicate_labels:
    - '1_1'
    - '2_1'
    date_of_retrieval: '2016-04-19'
from_schema: https://w3id.org/fga-wg/schema/top_level
rank: 1000
domain_of:
- Analysis
range: InputSource
required: true
multivalued: true

```
</details></div>