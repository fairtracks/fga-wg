---
search:
  boost: 5.0
---

# Slot: assessment_values 


_Main values produced by the quality assessment._



<div data-search-exclude markdown="1">



URI: [https://w3id.org/fga-wg/schema/bundle/assessment_values](https://w3id.org/fga-wg/schema/bundle/assessment_values)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [QualityAssessment](QualityAssessment.md) | Represents the results of a quality assessment that has been carried out on a data file resulting from an experiment or analysis. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Any](Any.md)&nbsp;or&nbsp;<br />[String](String.md)&nbsp;or&nbsp;<br />[AssessmentValue](AssessmentValue.md) |
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
- AnonymousSlotExpression({
  'range': 'AssessmentValue',
  'multivalued': True,
  'inlined': True,
  'inlined_as_list': False
})

</details>










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
| self | https://w3id.org/fga-wg/schema/bundle/assessment_values |
| native | https://w3id.org/fga-wg/schema/bundle/assessment_values |




## LinkML Source

<details>
```yaml
name: assessment_values
description: Main values produced by the quality assessment.
examples:
- object:
    nreads: 21018235
    nreads_in_peaks: 6161851
    frip: 0.2931669095906483
from_schema: https://w3id.org/fga-wg/schema/bundle
rank: 1000
domain_of:
- QualityAssessment
range: Any
required: true
any_of:
- range: string
- range: AssessmentValue
  multivalued: true
  inlined: true
  inlined_as_list: false

```
</details></div>