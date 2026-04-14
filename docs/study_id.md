---
search:
  boost: 5.0
---

# Slot: study_id 


_Internal identifier for the study (unique within the metadata deposit). Namespace: "study"._



<div data-search-exclude markdown="1">



URI: [https://w3id.org/fga-wg/schema/top_level/study_id](https://w3id.org/fga-wg/schema/top_level/study_id)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Study](Study.md) | A scientific study, i.e. a unit of research, within which experiments and/or analyses have been carried out. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Curie](Curie.md) |
| Domain Of | [Study](Study.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Identifier | Yes |











## Examples

| Value |
| --- |
| study:S-EPMC7391744 |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fga-wg/schema/top_level




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/fga-wg/schema/top_level/study_id |
| native | https://w3id.org/fga-wg/schema/top_level/study_id |




## LinkML Source

<details>
```yaml
name: study_id
description: 'Internal identifier for the study (unique within the metadata deposit).
  Namespace: "study".'
examples:
- value: study:S-EPMC7391744
from_schema: https://w3id.org/fga-wg/schema/top_level
rank: 1000
identifier: true
domain_of:
- Study
range: curie
required: true

```
</details></div>