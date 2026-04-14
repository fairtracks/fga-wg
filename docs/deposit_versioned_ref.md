---
search:
  boost: 5.0
---

# Slot: deposit_versioned_ref 


_Reference to versioned id of deposit containing this file collection._



<div data-search-exclude markdown="1">



URI: [https://w3id.org/fga-wg/schema/bundle/deposit_versioned_ref](https://w3id.org/fga-wg/schema/bundle/deposit_versioned_ref)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [FileCollection](FileCollection.md) | A collection of files, according to some selection criteria. In the context of the "FAIRification of Genomic Annotations" data model, we are mainly interested in "GenomicAnnotationFile" entities, but other types of files can also be contained in a collection, e.g. raw data files such as FASTQ files. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Curie](Curie.md) |
| Domain Of | [FileCollection](FileCollection.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |









## Examples

| Value |
| --- |
| doi:10.1234/zenodo.12345679 |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fga-wg/schema/bundle




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/fga-wg/schema/bundle/deposit_versioned_ref |
| native | https://w3id.org/fga-wg/schema/bundle/deposit_versioned_ref |




## LinkML Source

<details>
```yaml
name: deposit_versioned_ref
description: Reference to versioned id of deposit containing this file collection.
examples:
- value: doi:10.1234/zenodo.12345679
from_schema: https://w3id.org/fga-wg/schema/bundle
rank: 1000
domain_of:
- FileCollection
range: curie
required: true

```
</details></div>