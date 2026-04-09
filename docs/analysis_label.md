---
search:
  boost: 5.0
---

# Slot: analysis_label 


_A human-readable description of the analysis, short enough to be used for listings within software user interfaces, tables, illustration legends, etc._



<div data-search-exclude markdown="1">



URI: [https://w3id.org/fga-wg/schema/top_level/analysis_label](https://w3id.org/fga-wg/schema/top_level/analysis_label)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Analysis](Analysis.md) | Represents the computational processing applied to data from a sequencing exp... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Analysis](Analysis.md) |

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
| ENCODE3 ChIP-seq pipeline, GRCH38, replicated peak calling |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fga-wg/schema/top_level




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/fga-wg/schema/top_level/analysis_label |
| native | https://w3id.org/fga-wg/schema/top_level/analysis_label |




## LinkML Source

<details>
```yaml
name: analysis_label
description: A human-readable description of the analysis, short enough to be used
  for listings within software user interfaces, tables, illustration legends, etc.
examples:
- value: ENCODE3 ChIP-seq pipeline, GRCH38, replicated peak calling
from_schema: https://w3id.org/fga-wg/schema/top_level
rank: 1000
domain_of:
- Analysis
range: string
required: true
pattern: ^.{1,60}$

```
</details></div>