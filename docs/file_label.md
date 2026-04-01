

# Slot: file_label 


_A human-readable description of the data file, short enough to be used for listings within software user interfaces, tables, illustration legends, etc._





URI: [https://w3id.org/fga-wg/schema/top_level/file_label](https://w3id.org/fga-wg/schema/top_level/file_label)
Alias: file_label

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
| Required | Yes |
### Value Constraints

| Property | Value |
| --- | --- |
| Regex Pattern | `^.{1,60}$` |











## Examples

| Value |
| --- |
| H3K9me3 ChIP-seq replicated peaks, GRCh38, AG04450 |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fga-wg/schema/top_level




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/fga-wg/schema/top_level/file_label |
| native | https://w3id.org/fga-wg/schema/top_level/file_label |




## LinkML Source

<details>
```yaml
name: file_label
description: A human-readable description of the data file, short enough to be used
  for listings within software user interfaces, tables, illustration legends, etc.
examples:
- value: H3K9me3 ChIP-seq replicated peaks, GRCh38, AG04450
from_schema: https://w3id.org/fga-wg/schema/top_level
rank: 1000
alias: file_label
domain_of:
- File
range: string
required: true
pattern: ^.{1,60}$

```
</details>