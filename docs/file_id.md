

# Slot: file_id 


_Internal identifier for the data file (unique within the metadata deposit). _





URI: [https://w3id.org/fga-wg/schema/top_level/file_id](https://w3id.org/fga-wg/schema/top_level/file_id)
Alias: file_id

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
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Identifier | Yes |











## Examples

| Value |
| --- |
| file:ENCFF323LCS |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fga-wg/schema/top_level




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/fga-wg/schema/top_level/file_id |
| native | https://w3id.org/fga-wg/schema/top_level/file_id |




## LinkML Source

<details>
```yaml
name: file_id
description: 'Internal identifier for the data file (unique within the metadata deposit). '
examples:
- value: file:ENCFF323LCS
from_schema: https://w3id.org/fga-wg/schema/top_level
rank: 1000
identifier: true
alias: file_id
domain_of:
- File
range: curie
required: true

```
</details>