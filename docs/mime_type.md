---
search:
  boost: 5.0
---

# Slot: mime_type 


_A string providing the mime-type of the data file._



<div data-search-exclude markdown="1">



URI: [https://w3id.org/fga-wg/schema/top_level/mime_type](https://w3id.org/fga-wg/schema/top_level/mime_type)
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
| Range | [String](String.md) |
| Domain Of | [File](File.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |









## Examples

| Value |
| --- |
| application/octet-stream |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fga-wg/schema/top_level




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/fga-wg/schema/top_level/mime_type |
| native | https://w3id.org/fga-wg/schema/top_level/mime_type |




## LinkML Source

<details>
```yaml
name: mime_type
description: A string providing the mime-type of the data file.
examples:
- value: application/octet-stream
from_schema: https://w3id.org/fga-wg/schema/top_level
rank: 1000
domain_of:
- File
range: string

```
</details></div>