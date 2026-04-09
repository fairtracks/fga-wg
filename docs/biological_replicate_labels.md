---
search:
  boost: 5.0
---

# Slot: biological_replicate_labels 


_Labels denoting the biological replicates within which the relation is defined, if any._



<div data-search-exclude markdown="1">



URI: [https://w3id.org/fga-wg/schema/top_level/biological_replicate_labels](https://w3id.org/fga-wg/schema/top_level/biological_replicate_labels)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [InputSource](InputSource.md) | General object representing the source of data files, samples, or other entit... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [InputSource](InputSource.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |









## Examples

| Value |
| --- |
| 1 |
| 2 |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fga-wg/schema/top_level




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/fga-wg/schema/top_level/biological_replicate_labels |
| native | https://w3id.org/fga-wg/schema/top_level/biological_replicate_labels |




## LinkML Source

<details>
```yaml
name: biological_replicate_labels
description: Labels denoting the biological replicates within which the relation is
  defined, if any.
examples:
- value: '1'
- value: '2'
from_schema: https://w3id.org/fga-wg/schema/top_level
rank: 1000
domain_of:
- InputSource
range: string
multivalued: true

```
</details></div>