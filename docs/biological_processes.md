---
search:
  boost: 5.0
---

# Slot: biological_processes 


_Biological processes illuminated by the experiment._



<div data-search-exclude markdown="1">



URI: [https://w3id.org/fga-wg/schema/bundle/biological_processes](https://w3id.org/fga-wg/schema/bundle/biological_processes)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Experiment](Experiment.md) | Represents a sequencing experiment that has been carried out within a study, based on biological samples, and providing data files as output. Subsequent analysis of output data is described by the Analysis entity. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Term](Term.md) |
| Domain Of | [Experiment](Experiment.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |









## Examples

| Value |
| --- |
| None |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fga-wg/schema/bundle




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/fga-wg/schema/bundle/biological_processes |
| native | https://w3id.org/fga-wg/schema/bundle/biological_processes |




## LinkML Source

<details>
```yaml
name: biological_processes
description: Biological processes illuminated by the experiment.
examples:
- object:
    id: GO:0140999
    label: histone H3K4 trimethyltransferase activity
from_schema: https://w3id.org/fga-wg/schema/bundle
rank: 1000
domain_of:
- Experiment
range: Term
multivalued: true

```
</details></div>