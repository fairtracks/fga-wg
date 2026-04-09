

# Slot: file_external_id 


_External, globally unique identifier for the data file._





URI: [https://w3id.org/fga-wg/schema/top_level/file_external_id](https://w3id.org/fga-wg/schema/top_level/file_external_id)
Alias: file_external_id

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
| Range | [Curie](Curie.md) |
| Domain Of | [File](File.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |









## Examples

| Value |
| --- |
| encode:ENCFF323LCS |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fga-wg/schema/top_level




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/fga-wg/schema/top_level/file_external_id |
| native | https://w3id.org/fga-wg/schema/top_level/file_external_id |




## LinkML Source

<details>
```yaml
name: file_external_id
description: External, globally unique identifier for the data file.
examples:
- value: encode:ENCFF323LCS
from_schema: https://w3id.org/fga-wg/schema/top_level
rank: 1000
alias: file_external_id
domain_of:
- File
range: curie

```
</details>