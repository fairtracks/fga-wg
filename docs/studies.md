---
search:
  boost: 5.0
---

# Slot: studies 


_The scientific studies, i.e. units of research, within which experiments and/or analyses have been carried out._



<div data-search-exclude markdown="1">



URI: [https://w3id.org/fga-wg/schema/top_level/studies](https://w3id.org/fga-wg/schema/top_level/studies)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [TopLevel](TopLevel.md) | A document of harmonised metadata for a set of genome annotation files. Metadata has been harmonised in line with the "FAIRification of Genomic Annotations" data model. This is the top-level class to be used as root for the metadata document. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Study](Study.md) |
| Domain Of | [TopLevel](TopLevel.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fga-wg/schema/top_level




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/fga-wg/schema/top_level/studies |
| native | https://w3id.org/fga-wg/schema/top_level/studies |




## LinkML Source

<details>
```yaml
name: studies
description: The scientific studies, i.e. units of research, within which experiments
  and/or analyses have been carried out.
from_schema: https://w3id.org/fga-wg/schema/top_level
rank: 1000
domain_of:
- TopLevel
range: Study
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>