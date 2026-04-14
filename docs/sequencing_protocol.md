---
search:
  boost: 5.0
---

# Slot: sequencing_protocol 


_Set of rules which guides how the sequencing protocol was followed. Change-tracking services such as Protocol.io or GitHub are encouraged instead of dumping free text in this field._



<div data-search-exclude markdown="1">



URI: [https://w3id.org/fga-wg/schema/bundle/sequencing_protocol](https://w3id.org/fga-wg/schema/bundle/sequencing_protocol)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Experiment](Experiment.md) | Represents a sequencing experiment that has been carried out within a study, based on biological samples, and providing data files as output. Subsequent analysis of output data is described by the Analysis entity. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Uriorcurie](Uriorcurie.md) |
| Domain Of | [Experiment](Experiment.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fga-wg/schema/bundle




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/fga-wg/schema/bundle/sequencing_protocol |
| native | https://w3id.org/fga-wg/schema/bundle/sequencing_protocol |




## LinkML Source

<details>
```yaml
name: sequencing_protocol
description: Set of rules which guides how the sequencing protocol was followed. Change-tracking
  services such as Protocol.io or GitHub are encouraged instead of dumping free text
  in this field.
from_schema: https://w3id.org/fga-wg/schema/bundle
rank: 1000
domain_of:
- Experiment
range: uriorcurie

```
</details></div>