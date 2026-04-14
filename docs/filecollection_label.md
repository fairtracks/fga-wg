---
search:
  boost: 5.0
---

# Slot: filecollection_label 


_A human-readable description of the file collection, short enough to be used for listings within software user interfaces, tables, illustration legends, etc._



<div data-search-exclude markdown="1">



URI: [https://w3id.org/fga-wg/schema/bundle/filecollection_label](https://w3id.org/fga-wg/schema/bundle/filecollection_label)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [FileCollection](FileCollection.md) | A collection of files, according to some selection criteria. In the context of the "FAIRification of Genomic Annotations" data model, we are mainly interested in "GenomicAnnotationFile" entities, but other types of files can also be contained in a collection, e.g. raw data files such as FASTQ files. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [FileCollection](FileCollection.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Value Constraints

| Property | Value |
| --- | --- |
| Regex Pattern | `^.{1,60}$` |











## Examples

| Value |
| --- |
| IHEC data portal: ENCODE dataset |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fga-wg/schema/bundle




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/fga-wg/schema/bundle/filecollection_label |
| native | https://w3id.org/fga-wg/schema/bundle/filecollection_label |




## LinkML Source

<details>
```yaml
name: filecollection_label
description: A human-readable description of the file collection, short enough to
  be used for listings within software user interfaces, tables, illustration legends,
  etc.
examples:
- value: 'IHEC data portal: ENCODE dataset'
from_schema: https://w3id.org/fga-wg/schema/bundle
rank: 1000
domain_of:
- FileCollection
range: string
required: true
pattern: ^.{1,60}$

```
</details></div>