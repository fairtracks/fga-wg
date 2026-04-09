---
search:
  boost: 5.0
---

# Slot: other_biospecimen 


_Other biospecimen-related terms that can be used to further classify the biospecimen/sample._



<div data-search-exclude markdown="1">



URI: [https://w3id.org/fga-wg/schema/top_level/other_biospecimen](https://w3id.org/fga-wg/schema/top_level/other_biospecimen)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Sample](Sample.md) | Information about a biospecimen/sample used as raw material for lab experimen... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Term](Term.md) |
| Domain Of | [Sample](Sample.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |









## Examples

| Value |
| --- |
| None |
| None |
| None |
| None |
| None |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fga-wg/schema/top_level




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/fga-wg/schema/top_level/other_biospecimen |
| native | https://w3id.org/fga-wg/schema/top_level/other_biospecimen |




## LinkML Source

<details>
```yaml
name: other_biospecimen
description: Other biospecimen-related terms that can be used to further classify
  the biospecimen/sample.
examples:
- object:
    id: UBERON:0002384
    label: connective tissue
- object:
    id: CL:0002320
    label: connective tissue cell
- object:
    id: CL:0000057
    label: fibroblast
- object:
    id: UBERON:0000925
    label: endoterm
- object:
    id: UBERON:0001004
    label: respiratory system
from_schema: https://w3id.org/fga-wg/schema/top_level
rank: 1000
domain_of:
- Sample
range: Term
multivalued: true

```
</details></div>