---
search:
  boost: 5.0
---

# Slot: file_input_sources 


_External or internal references to data sources for the file, typically a data collection or a process that has generated the file. Internal references should lead to FileCollection, File, Experiment, or Analysis objects._



<div data-search-exclude markdown="1">



URI: [https://w3id.org/fga-wg/schema/top_level/file_input_sources](https://w3id.org/fga-wg/schema/top_level/file_input_sources)
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
| Range | [InputSource](InputSource.md) |
| Domain Of | [File](File.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
| Multivalued | Yes |









## Examples

| Value |
| --- |
| None |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fga-wg/schema/top_level




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/fga-wg/schema/top_level/file_input_sources |
| native | https://w3id.org/fga-wg/schema/top_level/file_input_sources |




## LinkML Source

<details>
```yaml
name: file_input_sources
description: External or internal references to data sources for the file, typically
  a data collection or a process that has generated the file. Internal references
  should lead to FileCollection, File, Experiment, or Analysis objects.
examples:
- object:
    inputsource_ref: analysis:ENCAN718KHT
    qualified_relation: prov:wasGeneratedBy
    biological_replicate_labels:
    - '1'
    - '2'
    technical_replicate_labels:
    - '1_1'
    - '2_1'
from_schema: https://w3id.org/fga-wg/schema/top_level
rank: 1000
domain_of:
- File
range: InputSource
required: true
multivalued: true

```
</details></div>