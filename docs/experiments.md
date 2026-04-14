---
search:
  boost: 5.0
---

# Slot: experiments 


_Information about sequencing experiments that have been carried out to generate the files._



<div data-search-exclude markdown="1">



URI: [https://w3id.org/fga-wg/schema/bundle/experiments](https://w3id.org/fga-wg/schema/bundle/experiments)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Bundle](Bundle.md) | A bundle representing a set of genome annotation files, organised in sub-collections. Metadata has been harmonised in line with the "FAIRification of Genomic Annotations" data model. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Experiment](Experiment.md) |
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
| self | https://w3id.org/fga-wg/schema/bundle/experiments |
| native | https://w3id.org/fga-wg/schema/bundle/experiments |




## LinkML Source

<details>
```yaml
name: experiments
description: Information about sequencing experiments that have been carried out to
  generate the files.
from_schema: https://w3id.org/fga-wg/schema/bundle
rank: 1000
domain_of:
- Bundle
range: Experiment
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>