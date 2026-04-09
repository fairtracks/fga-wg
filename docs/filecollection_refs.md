---
search:
  boost: 5.0
---

# Slot: filecollection_refs 


_Internal references to the FileCollection objects (within the deposit) that contains the data file, if any._



<div data-search-exclude markdown="1">



URI: [https://w3id.org/fga-wg/schema/top_level/filecollection_refs](https://w3id.org/fga-wg/schema/top_level/filecollection_refs)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [File](File.md) | General information about a particular data file |  no  |
| [GenomicAnnotationFile](GenomicAnnotationFile.md) | Information about a genomic annotation / track file |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Curie](Curie.md) |
| Domain Of | [File](File.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
| Multivalued | Yes |









## Examples

| Value |
| --- |
| collection:ihec_encode |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fga-wg/schema/top_level




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/fga-wg/schema/top_level/filecollection_refs |
| native | https://w3id.org/fga-wg/schema/top_level/filecollection_refs |




## LinkML Source

<details>
```yaml
name: filecollection_refs
description: Internal references to the FileCollection objects (within the deposit)
  that contains the data file, if any.
examples:
- value: collection:ihec_encode
from_schema: https://w3id.org/fga-wg/schema/top_level
rank: 1000
domain_of:
- File
range: curie
required: true
multivalued: true

```
</details></div>