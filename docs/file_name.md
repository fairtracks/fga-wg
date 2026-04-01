

# Slot: file_name 


_A string that can be used to name a data file. This string is made up of uppercase and lowercase letters, decimal digits, hypen, period, and underscore [A-Za-z0-9.-_]. See http://pubs.opengroup.org/onlinepubs/9699919799/basedefs/V1_chap03.html#tag_03_282 [portable filenames]._





URI: [https://w3id.org/fga-wg/schema/top_level/file_name](https://w3id.org/fga-wg/schema/top_level/file_name)
Alias: file_name

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
| 87234.ENCODE.ENCBS004ENC.H3K9me3.peak_calls.bigBed |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fga-wg/schema/top_level




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/fga-wg/schema/top_level/file_name |
| native | https://w3id.org/fga-wg/schema/top_level/file_name |




## LinkML Source

<details>
```yaml
name: file_name
description: A string that can be used to name a data file. This string is made up
  of uppercase and lowercase letters, decimal digits, hypen, period, and underscore
  [A-Za-z0-9.-_]. See http://pubs.opengroup.org/onlinepubs/9699919799/basedefs/V1_chap03.html#tag_03_282
  [portable filenames].
examples:
- value: 87234.ENCODE.ENCBS004ENC.H3K9me3.peak_calls.bigBed
from_schema: https://w3id.org/fga-wg/schema/top_level
rank: 1000
alias: file_name
domain_of:
- File
range: string

```
</details>