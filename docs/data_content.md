---
search:
  boost: 5.0
---

# Slot: data_content 


_Classification describing the file's purpose or contents._



<div data-search-exclude markdown="1">



URI: [https://w3id.org/fga-wg/schema/top_level/data_content](https://w3id.org/fga-wg/schema/top_level/data_content)
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
| Range | [OutputType](OutputType.md) |
| Domain Of | [File](File.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |









## Examples

| Value |
| --- |
| replicated peaks |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fga-wg/schema/top_level




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/fga-wg/schema/top_level/data_content |
| native | https://w3id.org/fga-wg/schema/top_level/data_content |




## LinkML Source

<details>
```yaml
name: data_content
description: Classification describing the file's purpose or contents.
examples:
- value: replicated peaks
from_schema: https://w3id.org/fga-wg/schema/top_level
rank: 1000
domain_of:
- File
range: OutputType
required: true

```
</details></div>