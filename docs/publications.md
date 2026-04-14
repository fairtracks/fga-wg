---
search:
  boost: 5.0
---

# Slot: publications 


_List of (relevant) publications containing the results of the study (in the form of DOI CURIEs)._



<div data-search-exclude markdown="1">



URI: [https://w3id.org/fga-wg/schema/bundle/publications](https://w3id.org/fga-wg/schema/bundle/publications)
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
| Multivalued | Yes |









## Examples

| Value |
| --- |
| https://doi.org/10.1038/s41467-020-14743-w |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fga-wg/schema/bundle




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/fga-wg/schema/bundle/publications |
| native | https://w3id.org/fga-wg/schema/bundle/publications |




## LinkML Source

<details>
```yaml
name: publications
description: List of (relevant) publications containing the results of the study (in
  the form of DOI CURIEs).
examples:
- value: https://doi.org/10.1038/s41467-020-14743-w
from_schema: https://w3id.org/fga-wg/schema/bundle
rank: 1000
domain_of:
- Study
range: curie
multivalued: true

```
</details></div>