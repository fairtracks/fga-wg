---
search:
  boost: 5.0
---

# Slot: quality_assessments 


_An array of QualityAssessment objects containing the main quality scores from assessment techniques applied to the data file._



<div data-search-exclude markdown="1">



URI: [https://w3id.org/fga-wg/schema/top_level/quality_assessments](https://w3id.org/fga-wg/schema/top_level/quality_assessments)
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


* from schema: https://w3id.org/fga-wg/schema/top_level




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/fga-wg/schema/top_level/quality_assessments |
| native | https://w3id.org/fga-wg/schema/top_level/quality_assessments |




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
from_schema: https://w3id.org/fga-wg/schema/top_level
rank: 1000
domain_of:
- File
range: QualityAssessment
multivalued: true

```
</details></div>