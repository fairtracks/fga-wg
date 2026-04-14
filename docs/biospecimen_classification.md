---
search:
  boost: 5.0
---

# Slot: biospecimen_classification 


_Main type of structural unit to be used for classification of the biospecimen/sample._



<div data-search-exclude markdown="1">



URI: [https://w3id.org/fga-wg/schema/bundle/biospecimen_classification](https://w3id.org/fga-wg/schema/bundle/biospecimen_classification)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Sample](Sample.md) | Information about a biospecimen/sample used as raw material for lab experiments. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [BiospecimenClassification](BiospecimenClassification.md) |
| Domain Of | [Sample](Sample.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |









## Examples

| Value |
| --- |
| cell line |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fga-wg/schema/bundle




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/fga-wg/schema/bundle/biospecimen_classification |
| native | https://w3id.org/fga-wg/schema/bundle/biospecimen_classification |




## LinkML Source

<details>
```yaml
name: biospecimen_classification
description: Main type of structural unit to be used for classification of the biospecimen/sample.
examples:
- value: cell line
from_schema: https://w3id.org/fga-wg/schema/bundle
rank: 1000
domain_of:
- Sample
range: BiospecimenClassification
required: true

```
</details></div>