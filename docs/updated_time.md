

# Slot: updated_time 


_Timestamp of content update in RFC3339, identical to created_time in systems that do not support updates. (This is the update time of the underlying content, not of the JSON object.)._





URI: [https://w3id.org/fga-wg/schema/top_level/updated_time](https://w3id.org/fga-wg/schema/top_level/updated_time)
Alias: updated_time

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
| Range | [Datetime](Datetime.md) |
| Domain Of | [File](File.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |









## Examples

| Value |
| --- |
| 2016-11-13T17:42:04.385801+00:00 |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fga-wg/schema/top_level




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/fga-wg/schema/top_level/updated_time |
| native | https://w3id.org/fga-wg/schema/top_level/updated_time |




## LinkML Source

<details>
```yaml
name: updated_time
description: Timestamp of content update in RFC3339, identical to created_time in
  systems that do not support updates. (This is the update time of the underlying
  content, not of the JSON object.).
examples:
- value: '2016-11-13T17:42:04.385801+00:00'
from_schema: https://w3id.org/fga-wg/schema/top_level
rank: 1000
alias: updated_time
domain_of:
- File
range: datetime

```
</details>