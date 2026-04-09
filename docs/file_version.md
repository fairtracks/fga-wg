

# Slot: file_version 


_A string representing a version. (Some systems may use checksum, a RFC3339 timestamp, or an incrementing version number.)._





URI: [https://w3id.org/fga-wg/schema/top_level/file_version](https://w3id.org/fga-wg/schema/top_level/file_version)
Alias: file_version

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
| efd4e74e-7875-4d13-9630-0085bc834f18 |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fga-wg/schema/top_level




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/fga-wg/schema/top_level/file_version |
| native | https://w3id.org/fga-wg/schema/top_level/file_version |




## LinkML Source

<details>
```yaml
name: file_version
description: A string representing a version. (Some systems may use checksum, a RFC3339
  timestamp, or an incrementing version number.).
examples:
- value: efd4e74e-7875-4d13-9630-0085bc834f18
from_schema: https://w3id.org/fga-wg/schema/top_level
rank: 1000
alias: file_version
domain_of:
- File
range: string

```
</details>