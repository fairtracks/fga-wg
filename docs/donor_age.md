---
search:
  boost: 5.0
---

# Slot: donor_age 


_Age of the donor/organism at the time of sampling_



<div data-search-exclude markdown="1">



URI: [https://w3id.org/fga-wg/schema/top_level/donor_age](https://w3id.org/fga-wg/schema/top_level/donor_age)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Sample](Sample.md) | Information about a biospecimen/sample used as raw material for lab experimen... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Sample](Sample.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |









## Examples

| Value |
| --- |
| W12 |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fga-wg/schema/top_level




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/fga-wg/schema/top_level/donor_age |
| native | https://w3id.org/fga-wg/schema/top_level/donor_age |




## LinkML Source

<details>
```yaml
name: donor_age
description: Age of the donor/organism at the time of sampling
examples:
- value: W12
from_schema: https://w3id.org/fga-wg/schema/top_level
rank: 1000
domain_of:
- Sample
range: string

```
</details></div>