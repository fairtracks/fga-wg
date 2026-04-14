---
search:
  boost: 5.0
---

# Slot: assessment_details_url 


_URL to a report containing the detailed output from the quality assessment._



<div data-search-exclude markdown="1">



URI: [https://w3id.org/fga-wg/schema/bundle/assessment_details_url](https://w3id.org/fga-wg/schema/bundle/assessment_details_url)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [QualityAssessment](QualityAssessment.md) | Represents the results of a quality assessment that has been carried out on a data file resulting from an experiment or analysis. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Uri](Uri.md) |
| Domain Of | [QualityAssessment](QualityAssessment.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |









## Examples

| Value |
| --- |
| https://www.encodeproject.org/histone-chipseq-quality-metrics/70ae08dc-3edc-437f-a0a5-378c72e6269b/ |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fga-wg/schema/bundle




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/fga-wg/schema/bundle/assessment_details_url |
| native | https://w3id.org/fga-wg/schema/bundle/assessment_details_url |




## LinkML Source

<details>
```yaml
name: assessment_details_url
description: URL to a report containing the detailed output from the quality assessment.
examples:
- value: https://www.encodeproject.org/histone-chipseq-quality-metrics/70ae08dc-3edc-437f-a0a5-378c72e6269b/
from_schema: https://w3id.org/fga-wg/schema/bundle
rank: 1000
domain_of:
- QualityAssessment
range: uri

```
</details></div>