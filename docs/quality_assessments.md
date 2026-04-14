---
search:
  boost: 5.0
---

# Slot: quality_assessments 


_An array of QualityAssessment objects containing the main quality scores from assessment techniques applied to the data file._



<div data-search-exclude markdown="1">



URI: [https://w3id.org/fga-wg/schema/bundle/quality_assessments](https://w3id.org/fga-wg/schema/bundle/quality_assessments)
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
| Range | [QualityAssessment](QualityAssessment.md) |
| Domain Of | [File](File.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |









## Examples

| Value |
| --- |
| None |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fga-wg/schema/bundle




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/fga-wg/schema/bundle/quality_assessments |
| native | https://w3id.org/fga-wg/schema/bundle/quality_assessments |




## LinkML Source

<details>
```yaml
name: quality_assessments
description: An array of QualityAssessment objects containing the main quality scores
  from assessment techniques applied to the data file.
examples:
- object:
    assessment_method: histone-chipseq-quality-metrics
    assessment_values:
      nreads: 21018235
      nreads_in_peaks: 6161851
      frip: 0.2931669095906483
    assessment_details_url: https://www.encodeproject.org/histone-chipseq-quality-metrics/70ae08dc-3edc-437f-a0a5-378c72e6269b/
from_schema: https://w3id.org/fga-wg/schema/bundle
rank: 1000
domain_of:
- File
range: QualityAssessment
multivalued: true

```
</details></div>