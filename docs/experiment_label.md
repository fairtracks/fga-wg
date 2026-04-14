---
search:
  boost: 5.0
---

# Slot: experiment_label 


_A human-readable description of the experiment, short enough to be used for listings within software user interfaces, tables, illustration legends, etc._



<div data-search-exclude markdown="1">



URI: [https://w3id.org/fga-wg/schema/top_level/experiment_label](https://w3id.org/fga-wg/schema/top_level/experiment_label)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Experiment](Experiment.md) | Represents a sequencing experiment that has been carried out within a study, based on biological samples, and providing data files as output. Subsequent analysis of output data is described by the Analysis entity. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Experiment](Experiment.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Value Constraints

| Property | Value |
| --- | --- |
| Regex Pattern | `^.{1,60}$` |











## Examples

| Value |
| --- |
| H3K9me3 ChIP-seq on human AG04450 |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fga-wg/schema/top_level




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/fga-wg/schema/top_level/experiment_label |
| native | https://w3id.org/fga-wg/schema/top_level/experiment_label |




## LinkML Source

<details>
```yaml
name: experiment_label
description: A human-readable description of the experiment, short enough to be used
  for listings within software user interfaces, tables, illustration legends, etc.
examples:
- value: H3K9me3 ChIP-seq on human AG04450
from_schema: https://w3id.org/fga-wg/schema/top_level
rank: 1000
domain_of:
- Experiment
range: string
required: true
pattern: ^.{1,60}$

```
</details></div>