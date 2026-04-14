---
search:
  boost: 5.0
---

# Slot: organism_tissue 


_Part of organism (typically tissue or organ) from which the biospecimen/sample was taken, or cell line was derived from._



<div data-search-exclude markdown="1">



URI: [https://w3id.org/fga-wg/schema/bundle/organism_tissue](https://w3id.org/fga-wg/schema/bundle/organism_tissue)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Sample](Sample.md) | Information about a biospecimen/sample used as raw material for lab experiments. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Term](Term.md) |
| Domain Of | [Sample](Sample.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |









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
| self | https://w3id.org/fga-wg/schema/bundle/organism_tissue |
| native | https://w3id.org/fga-wg/schema/bundle/organism_tissue |




## LinkML Source

<details>
```yaml
name: organism_tissue
description: Part of organism (typically tissue or organ) from which the biospecimen/sample
  was taken, or cell line was derived from.
examples:
- object:
    id: UBERON:0002048
    label: lung
from_schema: https://w3id.org/fga-wg/schema/bundle
rank: 1000
domain_of:
- Sample
range: Term

```
</details></div>