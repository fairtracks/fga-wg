---
search:
  boost: 5.0
---

# Slot: analysis_main_tool 


_Main software tool used for the analysis._



<div data-search-exclude markdown="1">



URI: [https://w3id.org/fga-wg/schema/top_level/analysis_main_tool](https://w3id.org/fga-wg/schema/top_level/analysis_main_tool)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Analysis](Analysis.md) | Represents the computational processing applied to data from a sequencing exp... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Any](Any.md)&nbsp;or&nbsp;<br />[String](String.md)&nbsp;or&nbsp;<br />[Curie](Curie.md) |
| Domain Of | [Analysis](Analysis.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
<details>
<summary>Expressions & Logic</summary>
#### Any Of

Value must satisfy at least one of:
- AnonymousSlotExpression({'range': 'string'})
- AnonymousSlotExpression({'range': 'curie'})

</details>










## Examples

| Value |
| --- |
| biotools:macs |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fga-wg/schema/top_level




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/fga-wg/schema/top_level/analysis_main_tool |
| native | https://w3id.org/fga-wg/schema/top_level/analysis_main_tool |




## LinkML Source

<details>
```yaml
name: analysis_main_tool
description: Main software tool used for the analysis.
examples:
- value: biotools:macs
from_schema: https://w3id.org/fga-wg/schema/top_level
rank: 1000
domain_of:
- Analysis
range: Any
any_of:
- range: string
- range: curie

```
</details></div>