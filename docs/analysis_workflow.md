---
search:
  boost: 5.0
---

# Slot: analysis_workflow 


_External reference to the analysis workflow, with availability in at least one machine-operable form (e.g. CWL, Nextflow, ...)._



<div data-search-exclude markdown="1">



URI: [https://w3id.org/fga-wg/schema/bundle/analysis_workflow](https://w3id.org/fga-wg/schema/bundle/analysis_workflow)
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
| encode:ENCPL272XAE |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fga-wg/schema/bundle




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/fga-wg/schema/bundle/analysis_workflow |
| native | https://w3id.org/fga-wg/schema/bundle/analysis_workflow |




## LinkML Source

<details>
```yaml
name: analysis_workflow
description: External reference to the analysis workflow, with availability in at
  least one machine-operable form (e.g. CWL, Nextflow, ...).
examples:
- value: encode:ENCPL272XAE
from_schema: https://w3id.org/fga-wg/schema/bundle
rank: 1000
domain_of:
- Analysis
range: uriorcurie

```
</details></div>