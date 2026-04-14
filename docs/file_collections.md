---
search:
  boost: 5.0
---

# Slot: file_collections 


_Information about collections of files contained in this dataset, each collection defined according to some selection criteria._



<div data-search-exclude markdown="1">



URI: [https://w3id.org/fga-wg/schema/bundle/file_collections](https://w3id.org/fga-wg/schema/bundle/file_collections)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Bundle](Bundle.md) | A bundle representing a set of genome annotation files, organised in sub-collections. Metadata has been harmonised in line with the "FAIRification of Genomic Annotations" data model. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [FileCollection](FileCollection.md) |
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
| self | https://w3id.org/fga-wg/schema/bundle/file_collections |
| native | https://w3id.org/fga-wg/schema/bundle/file_collections |




## LinkML Source

<details>
```yaml
name: file_collections
description: Information about collections of files contained in this dataset, each
  collection defined according to some selection criteria.
from_schema: https://w3id.org/fga-wg/schema/bundle
rank: 1000
domain_of:
- Bundle
range: FileCollection
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>