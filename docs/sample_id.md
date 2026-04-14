---
search:
  boost: 5.0
---

# Slot: sample_id 


_Internal identifier for the biospecimen/sample (unique within the metadata deposit)._



<div data-search-exclude markdown="1">



URI: [https://w3id.org/fga-wg/schema/top_level/sample_id](https://w3id.org/fga-wg/schema/top_level/sample_id)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Sample](Sample.md) | Information about a biospecimen/sample used as raw material for lab experiments. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Curie](Curie.md) |
| Domain Of | [Sample](Sample.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Identifier | Yes |











## Examples

| Value |
| --- |
| sample:ENCBS004ENC |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fga-wg/schema/top_level




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/fga-wg/schema/top_level/sample_id |
| native | https://w3id.org/fga-wg/schema/top_level/sample_id |




## LinkML Source

<details>
```yaml
name: sample_id
description: Internal identifier for the biospecimen/sample (unique within the metadata
  deposit).
examples:
- value: sample:ENCBS004ENC
from_schema: https://w3id.org/fga-wg/schema/top_level
rank: 1000
identifier: true
domain_of:
- Sample
range: curie
required: true

```
</details></div>