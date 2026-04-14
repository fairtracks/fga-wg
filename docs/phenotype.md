---
search:
  boost: 5.0
---

# Slot: phenotype 


_Main phenotype (e.g. disease) connected to the biospecimen/sample._



<div data-search-exclude markdown="1">



URI: [https://w3id.org/fga-wg/schema/top_level/phenotype](https://w3id.org/fga-wg/schema/top_level/phenotype)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Sample](Sample.md) | Information about a biospecimen/sample used as raw material for lab experiments. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Term](Term.md) |
| Domain Of | [Sample](Sample.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |









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
| self | https://w3id.org/fga-wg/schema/top_level/phenotype |
| native | https://w3id.org/fga-wg/schema/top_level/phenotype |




## LinkML Source

<details>
```yaml
name: phenotype
description: Main phenotype (e.g. disease) connected to the biospecimen/sample.
examples:
- object:
    id: PATO:0000461
    label: normal
from_schema: https://w3id.org/fga-wg/schema/top_level
rank: 1000
domain_of:
- Sample
range: Term

```
</details></div>