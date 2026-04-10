---
search:
  boost: 5.0
---

# Slot: sequence_features 


_List of sequence features described by the genomic annotation file._



<div data-search-exclude markdown="1">



URI: [https://w3id.org/fga-wg/schema/top_level/sequence_features](https://w3id.org/fga-wg/schema/top_level/sequence_features)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [GenomicAnnotationFile](GenomicAnnotationFile.md) | Information about a genomic annotation / track file |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Term](Term.md) |
| Domain Of | [GenomicAnnotationFile](GenomicAnnotationFile.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
| Multivalued | Yes |









## Examples

| Value |
| --- |
| None |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fga-wg/schema/top_level




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/fga-wg/schema/top_level/sequence_features |
| native | https://w3id.org/fga-wg/schema/top_level/sequence_features |




## LinkML Source

<details>
```yaml
name: sequence_features
description: List of sequence features described by the genomic annotation file.
examples:
- object:
    id: SO:0001707
    label: H3K9Me3
from_schema: https://w3id.org/fga-wg/schema/top_level
rank: 1000
domain_of:
- GenomicAnnotationFile
range: Term
required: true
multivalued: true

```
</details></div>