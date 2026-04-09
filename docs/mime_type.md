

# Slot: mime_type 


_A string providing the mime-type of the data file._





URI: [https://w3id.org/fga-wg/schema/top_level/mime_type](https://w3id.org/fga-wg/schema/top_level/mime_type)
Alias: mime_type

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [GenomicAnnotationFile](GenomicAnnotationFile.md) | Information about a genomic annotation / track file |  no  |
| [File](File.md) | General information about a particular data file |  no  |






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
alias: mime_type
domain_of:
- File
range: string

```
</details>