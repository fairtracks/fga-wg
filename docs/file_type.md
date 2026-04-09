---
search:
  boost: 5.0
---

# Slot: file_type 


_The file format of the data file._



<div data-search-exclude markdown="1">



URI: [https://w3id.org/fga-wg/schema/top_level/file_type](https://w3id.org/fga-wg/schema/top_level/file_type)
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
| Range | [Term](Term.md) |
| Domain Of | [File](File.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |









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
| self | https://w3id.org/fga-wg/schema/top_level/file_type |
| native | https://w3id.org/fga-wg/schema/top_level/file_type |




## LinkML Source

<details>
```yaml
name: file_type
description: The file format of the data file.
examples:
- object:
    id: edam:format_3004
    label: bigBed
from_schema: https://w3id.org/fga-wg/schema/top_level
rank: 1000
domain_of:
- File
range: Term
required: true

```
</details></div>