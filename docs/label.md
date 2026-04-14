---
search:
  boost: 5.0
---

# Slot: label 


_Human-readable label associated to the term id in the current version of the ontology (as listed in the "ontology_versions" field of the Deposit object)._



<div data-search-exclude markdown="1">



URI: [https://w3id.org/fga-wg/schema/bundle/label](https://w3id.org/fga-wg/schema/bundle/label)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Term](Term.md) | Helper entity to represent an ontology term as a data value. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Term](Term.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |









## Examples

| Value |
| --- |
| ChIP-seq assay |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fga-wg/schema/bundle




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/fga-wg/schema/bundle/label |
| native | https://w3id.org/fga-wg/schema/bundle/label |




## LinkML Source

<details>
```yaml
name: label
description: Human-readable label associated to the term id in the current version
  of the ontology (as listed in the "ontology_versions" field of the Deposit object).
examples:
- value: ChIP-seq assay
from_schema: https://w3id.org/fga-wg/schema/bundle
rank: 1000
domain_of:
- Term
range: string

```
</details></div>