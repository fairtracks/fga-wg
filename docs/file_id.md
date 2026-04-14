---
search:
  boost: 5.0
---

# Slot: file_id 


_Internal identifier for the data file (unique within the metadata deposit). _



<div data-search-exclude markdown="1">



URI: [https://w3id.org/fga-wg/schema/bundle/file_id](https://w3id.org/fga-wg/schema/bundle/file_id)
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


* from schema: https://w3id.org/fga-wg/schema/bundle




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/fga-wg/schema/bundle/file_id |
| native | https://w3id.org/fga-wg/schema/bundle/file_id |




## LinkML Source

<details>
```yaml
name: file_id
description: 'Internal identifier for the data file (unique within the metadata deposit). '
examples:
- value: file:ENCFF323LCS
from_schema: https://w3id.org/fga-wg/schema/bundle
rank: 1000
identifier: true
domain_of:
- File
range: curie
required: true

```
</details></div>