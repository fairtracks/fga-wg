---
search:
  boost: 5.0
---

# Slot: technical_replicate_labels 


_Labels denoting the technical replicates within which the relation is defined, if any._



<div data-search-exclude markdown="1">



URI: [https://w3id.org/fga-wg/schema/bundle/technical_replicate_labels](https://w3id.org/fga-wg/schema/bundle/technical_replicate_labels)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [InputSource](InputSource.md) | General object representing the source of data files, samples, or other entities used as input to a process or a result. An input source refering to a single file or sample object will represent that item only, while an input source referring to a container or process may represent a number of disctinct input items. InputSource also contains information about the type of relationship, replication labelling, versioning and retrieval date. |  no  |






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
| 1_1 |
| 1_2 |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fga-wg/schema/bundle




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/fga-wg/schema/bundle/technical_replicate_labels |
| native | https://w3id.org/fga-wg/schema/bundle/technical_replicate_labels |




## LinkML Source

<details>
```yaml
name: technical_replicate_labels
description: Labels denoting the technical replicates within which the relation is
  defined, if any.
examples:
- value: '1_1'
- value: '1_2'
from_schema: https://w3id.org/fga-wg/schema/bundle
rank: 1000
domain_of:
- InputSource
range: string
multivalued: true

```
</details></div>