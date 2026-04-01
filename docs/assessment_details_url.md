

# Slot: assessment_details_url 


_URL to a report containing the detailed output from the quality assessment._





URI: [https://w3id.org/fga-wg/schema/top_level/assessment_details_url](https://w3id.org/fga-wg/schema/top_level/assessment_details_url)
Alias: assessment_details_url

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [QualityAssessment](QualityAssessment.md) | Represents the results of a quality assessment that has been carried out on a... |  no  |






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


* from schema: https://w3id.org/fga-wg/schema/top_level




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/fga-wg/schema/top_level/assessment_details_url |
| native | https://w3id.org/fga-wg/schema/top_level/assessment_details_url |




## LinkML Source

<details>
```yaml
name: assessment_details_url
description: URL to a report containing the detailed output from the quality assessment.
examples:
- value: https://www.encodeproject.org/histone-chipseq-quality-metrics/70ae08dc-3edc-437f-a0a5-378c72e6269b/
from_schema: https://w3id.org/fga-wg/schema/top_level
rank: 1000
alias: assessment_details_url
domain_of:
- QualityAssessment
range: uri

```
</details>