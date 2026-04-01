

# Slot: value 


_Value corresponding to the assessment key._





URI: [https://w3id.org/fga-wg/schema/top_level/value](https://w3id.org/fga-wg/schema/top_level/value)
Alias: value

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AssessmentValue](AssessmentValue.md) | Key-value pair representing a specific value produced by a quality assessment |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Any](Any.md)&nbsp;or&nbsp;<br />[String](String.md)&nbsp;or&nbsp;<br />[Integer](Integer.md)&nbsp;or&nbsp;<br />[Decimal](Decimal.md)&nbsp;or&nbsp;<br />[Boolean](Boolean.md) |
| Domain Of | [AssessmentValue](AssessmentValue.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
<details>
<summary>Expressions & Logic</summary>
#### Any Of

Value must satisfy at least one of:
- AnonymousSlotExpression({'range': 'decimal'})
- AnonymousSlotExpression({'range': 'boolean'})
- AnonymousSlotExpression({'range': 'integer'})
- AnonymousSlotExpression({'range': 'string'})

</details>










## Examples

| Value |
| --- |
| None |
| None |
| None |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fga-wg/schema/top_level




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/fga-wg/schema/top_level/value |
| native | https://w3id.org/fga-wg/schema/top_level/value |




## LinkML Source

<details>
```yaml
name: value
description: Value corresponding to the assessment key.
examples:
- object: 21018235
- object: 6161851
- object: 0.2931669095906483
from_schema: https://w3id.org/fga-wg/schema/top_level
rank: 1000
alias: value
domain_of:
- AssessmentValue
range: Any
required: true
any_of:
- range: decimal
- range: boolean
- range: integer
- range: string

```
</details>