---
search:
  boost: 5.0
---

# Slot: file_size 


_For blobs, the blob size in bytes. _



<div data-search-exclude markdown="1">



URI: [https://w3id.org/fga-wg/schema/top_level/file_size](https://w3id.org/fga-wg/schema/top_level/file_size)
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
| Range | [Integer](Integer.md) |
| Domain Of | [File](File.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |









## Examples

| Value |
| --- |
| 5359719 |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fga-wg/schema/top_level




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/fga-wg/schema/top_level/file_size |
| native | https://w3id.org/fga-wg/schema/top_level/file_size |




## LinkML Source

<details>
```yaml
name: file_size
description: 'For blobs, the blob size in bytes. '
examples:
- value: '5359719'
from_schema: https://w3id.org/fga-wg/schema/top_level
rank: 1000
domain_of:
- File
range: integer
required: true

```
</details></div>