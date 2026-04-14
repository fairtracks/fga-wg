---
search:
  boost: 5.0
---

# Slot: assessment_method 


_Quality assessment method that has been carried out (e.g. BUSCO, OMArk, peak calling statistics, etc.)_



<div data-search-exclude markdown="1">



URI: [https://w3id.org/fga-wg/schema/bundle/assessment_method](https://w3id.org/fga-wg/schema/bundle/assessment_method)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [QualityAssessment](QualityAssessment.md) | Represents the results of a quality assessment that has been carried out on a data file resulting from an experiment or analysis. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Any](Any.md)&nbsp;or&nbsp;<br />[String](String.md)&nbsp;or&nbsp;<br />[Term](Term.md) |
| Domain Of | [QualityAssessment](QualityAssessment.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
<details>
<summary>Expressions & Logic</summary>
#### Any Of

Value must satisfy at least one of:
- AnonymousSlotExpression({'range': 'string'})
- AnonymousSlotExpression({'range': 'Term'})

</details>










## Examples

| Value |
| --- |
| histone-chipseq-quality-metrics |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fga-wg/schema/bundle




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/fga-wg/schema/bundle/assessment_method |
| native | https://w3id.org/fga-wg/schema/bundle/assessment_method |




## LinkML Source

<details>
```yaml
name: assessment_method
description: Quality assessment method that has been carried out (e.g. BUSCO, OMArk,
  peak calling statistics, etc.)
examples:
- value: histone-chipseq-quality-metrics
from_schema: https://w3id.org/fga-wg/schema/bundle
rank: 1000
domain_of:
- QualityAssessment
range: Any
required: true
any_of:
- range: string
- range: Term

```
</details></div>