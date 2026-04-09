---
search:
  boost: 5.0
---

# Slot: filecollection_id 


_Internal identifier for the file collection (unique within the metadata deposit). _



<div data-search-exclude markdown="1">



URI: [https://w3id.org/fga-wg/schema/top_level/filecollection_id](https://w3id.org/fga-wg/schema/top_level/filecollection_id)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [FileCollection](FileCollection.md) | A collection of files, according to some selection criteria |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Curie](Curie.md) |
| Domain Of | [FileCollection](FileCollection.md) |

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
| filecollection:ihec_encode |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fga-wg/schema/top_level




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/fga-wg/schema/top_level/filecollection_id |
| native | https://w3id.org/fga-wg/schema/top_level/filecollection_id |




## LinkML Source

<details>
```yaml
name: filecollection_id
description: 'Internal identifier for the file collection (unique within the metadata
  deposit). '
examples:
- value: filecollection:ihec_encode
from_schema: https://w3id.org/fga-wg/schema/top_level
rank: 1000
identifier: true
domain_of:
- FileCollection
range: curie
required: true

```
</details></div>