---
search:
  boost: 5.0
---

# Slot: mime_type 


_A string providing the mime-type of the data file._



<div data-search-exclude markdown="1">



URI: [https://w3id.org/fga-wg/schema/bundle/mime_type](https://w3id.org/fga-wg/schema/bundle/mime_type)
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


* from schema: https://w3id.org/fga-wg/schema/bundle




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/fga-wg/schema/bundle/mime_type |
| native | https://w3id.org/fga-wg/schema/bundle/mime_type |




## LinkML Source

<details>
```yaml
name: mime_type
description: A string providing the mime-type of the data file.
examples:
- value: application/octet-stream
from_schema: https://w3id.org/fga-wg/schema/bundle
rank: 1000
domain_of:
- File
range: string

```
</details></div>