---
search:
  boost: 5.0
---

# Slot: filecollection_external_id 


_External, globally unique identifier for the file collection (in most cases, this will not exist)._



<div data-search-exclude markdown="1">



URI: [https://w3id.org/fga-wg/schema/bundle/filecollection_external_id](https://w3id.org/fga-wg/schema/bundle/filecollection_external_id)
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










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fga-wg/schema/bundle




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/fga-wg/schema/bundle/filecollection_external_id |
| native | https://w3id.org/fga-wg/schema/bundle/filecollection_external_id |




## LinkML Source

<details>
```yaml
name: filecollection_external_id
description: External, globally unique identifier for the file collection (in most
  cases, this will not exist).
from_schema: https://w3id.org/fga-wg/schema/bundle
rank: 1000
domain_of:
- FileCollection
range: curie
required: false

```
</details></div>