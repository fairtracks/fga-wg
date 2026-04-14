---
search:
  boost: 5.0
---

# Slot: updated_time 


_Timestamp of content update in RFC3339, identical to created_time in systems that do not support updates. (This is the update time of the underlying content, not of the JSON object.)._



<div data-search-exclude markdown="1">



URI: [https://w3id.org/fga-wg/schema/top_level/updated_time](https://w3id.org/fga-wg/schema/top_level/updated_time)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [File](File.md) | General information about a particular data file. Most fields (marked with an asterix*) are copied from the GA4GH DRS DrsObject model (https://ga4gh.github.io/data-repository-service-schemas/preview/release/drs-1.4.0/docs/#tag/DrsObjectModel), which is the top-level object returned from a DRS server in response to a successful lookup call (i.e. https://ga4gh.github.io/data-repository-service-schemas/preview/release/drs-1.4.0/docs/#tag/Objects). |  no  |
| [GenomicAnnotationFile](GenomicAnnotationFile.md) | Information about a genomic annotation / track file. GenomicAnnotationFile is a specification of the File entity and inherits all the fields defined in File, in addition to the fields that are specific to GenomicAnnotationFile, as detailed here. |  no  |






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
domain_of:
- File
range: datetime

```
</details></div>