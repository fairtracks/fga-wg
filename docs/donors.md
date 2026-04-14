---
search:
  boost: 5.0
---

# Slot: donors 


_Information about the donors or complete organisms from which the samples were taken._



<div data-search-exclude markdown="1">



URI: [https://w3id.org/fga-wg/schema/bundle/donors](https://w3id.org/fga-wg/schema/bundle/donors)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Bundle](Bundle.md) | A bundle representing a set of genome annotation files, organised in sub-collections. Metadata has been harmonised in line with the "FAIRification of Genomic Annotations" data model. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Donor](Donor.md) |
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
| self | https://w3id.org/fga-wg/schema/bundle/donors |
| native | https://w3id.org/fga-wg/schema/bundle/donors |




## LinkML Source

<details>
```yaml
name: donors
description: Information about the donors or complete organisms from which the samples
  were taken.
from_schema: https://w3id.org/fga-wg/schema/bundle
rank: 1000
domain_of:
- Bundle
range: Donor
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>