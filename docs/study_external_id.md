---
search:
  boost: 5.0
---

# Slot: study_external_id 


_External, globally unique identifier for the study (preferably a BioStudies CURIE)._



<div data-search-exclude markdown="1">



URI: [https://w3id.org/fga-wg/schema/bundle/study_external_id](https://w3id.org/fga-wg/schema/bundle/study_external_id)
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









## Examples

| Value |
| --- |
| biostudies:S-EPMC7391744 |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fga-wg/schema/bundle




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/fga-wg/schema/bundle/study_external_id |
| native | https://w3id.org/fga-wg/schema/bundle/study_external_id |




## LinkML Source

<details>
```yaml
name: study_external_id
description: External, globally unique identifier for the study (preferably a BioStudies
  CURIE).
examples:
- value: biostudies:S-EPMC7391744
from_schema: https://w3id.org/fga-wg/schema/bundle
rank: 1000
domain_of:
- Study
range: curie

```
</details></div>