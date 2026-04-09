

# Slot: data_content 


_Classification describing the file's purpose or contents._





URI: [https://w3id.org/fga-wg/schema/top_level/data_content](https://w3id.org/fga-wg/schema/top_level/data_content)
Alias: data_content

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
alias: data_content
domain_of:
- File
range: OutputType
required: true

```
</details>