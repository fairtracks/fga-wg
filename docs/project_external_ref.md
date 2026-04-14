---
search:
  boost: 5.0
---

# Slot: project_external_ref 


_Reference to a project within which the study was carried out (preferably a BioProject CURIE)._



<div data-search-exclude markdown="1">



URI: [https://w3id.org/fga-wg/schema/top_level/project_external_ref](https://w3id.org/fga-wg/schema/top_level/project_external_ref)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Study](Study.md) | A scientific study, i.e. a unit of research, within which experiments and/or analyses have been carried out. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Uriorcurie](Uriorcurie.md) |
| Domain Of | [Study](Study.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |









## Examples

| Value |
| --- |
| bioproject:PRJNA63441 |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fga-wg/schema/top_level




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/fga-wg/schema/top_level/project_external_ref |
| native | https://w3id.org/fga-wg/schema/top_level/project_external_ref |




## LinkML Source

<details>
```yaml
name: project_external_ref
description: Reference to a project within which the study was carried out (preferably
  a BioProject CURIE).
examples:
- value: bioproject:PRJNA63441
from_schema: https://w3id.org/fga-wg/schema/top_level
rank: 1000
domain_of:
- Study
range: uriorcurie

```
</details></div>