---
search:
  boost: 5.0
---

# Slot: studies 


_The scientific studies, i.e. units of research, within which experiments and/or analyses have been carried out._



<div data-search-exclude markdown="1">



URI: [https://w3id.org/fga-wg/schema/bundle/studies](https://w3id.org/fga-wg/schema/bundle/studies)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Bundle](Bundle.md) | A bundle representing a set of genome annotation files, organised in sub-collections. Metadata has been harmonised in line with the "FAIRification of Genomic Annotations" data model. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Study](Study.md) |
| Domain Of | [Bundle](Bundle.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fga-wg/schema/bundle




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/fga-wg/schema/bundle/studies |
| native | https://w3id.org/fga-wg/schema/bundle/studies |




## LinkML Source

<details>
```yaml
name: studies
description: The scientific studies, i.e. units of research, within which experiments
  and/or analyses have been carried out.
from_schema: https://w3id.org/fga-wg/schema/bundle
rank: 1000
domain_of:
- Bundle
range: Study
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>