---
search:
  boost: 5.0
---

# Slot: sample_description 


_Human-readable description of the biospecimen/sample and the sampling process._



<div data-search-exclude markdown="1">



URI: [https://w3id.org/fga-wg/schema/top_level/sample_description](https://w3id.org/fga-wg/schema/top_level/sample_description)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Sample](Sample.md) | Information about a biospecimen/sample used as raw material for lab experimen... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Sample](Sample.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |









## Examples

| Value |
| --- |
| Homo sapiens AG04450 cell line |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fga-wg/schema/top_level




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/fga-wg/schema/top_level/sample_description |
| native | https://w3id.org/fga-wg/schema/top_level/sample_description |




## LinkML Source

<details>
```yaml
name: sample_description
description: Human-readable description of the biospecimen/sample and the sampling
  process.
examples:
- value: Homo sapiens AG04450 cell line
from_schema: https://w3id.org/fga-wg/schema/top_level
rank: 1000
domain_of:
- Sample
range: string

```
</details></div>