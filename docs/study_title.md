---
search:
  boost: 5.0
---

# Slot: study_title 


_Title of the study._



<div data-search-exclude markdown="1">



URI: [https://w3id.org/fga-wg/schema/top_level/study_title](https://w3id.org/fga-wg/schema/top_level/study_title)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Study](Study.md) | A scientific study, i |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Study](Study.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |









## Examples

| Value |
| --- |
| An integrative ENCODE resource for cancer genomics |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fga-wg/schema/top_level




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/fga-wg/schema/top_level/study_title |
| native | https://w3id.org/fga-wg/schema/top_level/study_title |




## LinkML Source

<details>
```yaml
name: study_title
description: Title of the study.
examples:
- value: An integrative ENCODE resource for cancer genomics
from_schema: https://w3id.org/fga-wg/schema/top_level
rank: 1000
domain_of:
- Study
range: string
required: true

```
</details></div>