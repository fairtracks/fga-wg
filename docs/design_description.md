---
search:
  boost: 5.0
---

# Slot: design_description 


_The high-level experiment design including layout, protocol._



<div data-search-exclude markdown="1">



URI: [https://w3id.org/fga-wg/schema/bundle/design_description](https://w3id.org/fga-wg/schema/bundle/design_description)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Experiment](Experiment.md) | Represents a sequencing experiment that has been carried out within a study, based on biological samples, and providing data files as output. Subsequent analysis of output data is described by the Analysis entity. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Experiment](Experiment.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |









## Examples

| Value |
| --- |
| https://www.encodeproject.org/documents/92cd1386-ccad-450a-b5a6-ad49983e7e3f/@@download/attachment/wgEncodeUwHistone.release5.html.pdf |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fga-wg/schema/bundle




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/fga-wg/schema/bundle/design_description |
| native | https://w3id.org/fga-wg/schema/bundle/design_description |




## LinkML Source

<details>
```yaml
name: design_description
description: The high-level experiment design including layout, protocol.
examples:
- value: https://www.encodeproject.org/documents/92cd1386-ccad-450a-b5a6-ad49983e7e3f/@@download/attachment/wgEncodeUwHistone.release5.html.pdf
from_schema: https://w3id.org/fga-wg/schema/bundle
rank: 1000
domain_of:
- Experiment
range: string

```
</details></div>