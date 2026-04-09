---
search:
  boost: 5.0
---

# Slot: created_time 


_Timestamp of content creation in RFC3339. (This is the creation time of the underlying content, not of the JSON object.)._



<div data-search-exclude markdown="1">



URI: [https://w3id.org/fga-wg/schema/top_level/created_time](https://w3id.org/fga-wg/schema/top_level/created_time)
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
| Range | [Datetime](Datetime.md) |
| Domain Of | [File](File.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |









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
| self | https://w3id.org/fga-wg/schema/top_level/created_time |
| native | https://w3id.org/fga-wg/schema/top_level/created_time |




## LinkML Source

<details>
```yaml
name: created_time
description: Timestamp of content creation in RFC3339. (This is the creation time
  of the underlying content, not of the JSON object.).
examples:
- value: '2016-11-13T17:42:04.385801+00:00'
from_schema: https://w3id.org/fga-wg/schema/top_level
rank: 1000
domain_of:
- File
range: datetime
required: true

```
</details></div>