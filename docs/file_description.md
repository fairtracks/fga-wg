---
search:
  boost: 5.0
---

# Slot: file_description 


_A human readable description of the data file._



<div data-search-exclude markdown="1">



URI: [https://w3id.org/fga-wg/schema/top_level/file_description](https://w3id.org/fga-wg/schema/top_level/file_description)
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
| H3K9me3 ChIP-seq replicated peaks on human (hg38) AG04450 (Fibroblast derived cell line). |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fga-wg/schema/top_level




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/fga-wg/schema/top_level/file_description |
| native | https://w3id.org/fga-wg/schema/top_level/file_description |




## LinkML Source

<details>
```yaml
name: file_description
description: A human readable description of the data file.
examples:
- value: H3K9me3 ChIP-seq replicated peaks on human (hg38) AG04450 (Fibroblast derived
    cell line).
from_schema: https://w3id.org/fga-wg/schema/top_level
rank: 1000
domain_of:
- File
range: string

```
</details></div>