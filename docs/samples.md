---
search:
  boost: 5.0
---

# Slot: samples 


_Information about the biospecimens/samples used as raw material for lab experiments._



<div data-search-exclude markdown="1">



URI: [https://w3id.org/fga-wg/schema/top_level/samples](https://w3id.org/fga-wg/schema/top_level/samples)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [TopLevel](TopLevel.md) | A document of harmonised metadata for a set of genome annotation files. Metadata has been harmonised in line with the "FAIRification of Genomic Annotations" data model. This is the top-level class to be used as root for the metadata document. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Sample](Sample.md) |
| Domain Of | [TopLevel](TopLevel.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fga-wg/schema/top_level




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/fga-wg/schema/top_level/samples |
| native | https://w3id.org/fga-wg/schema/top_level/samples |




## LinkML Source

<details>
```yaml
name: samples
description: Information about the biospecimens/samples used as raw material for lab
  experiments.
from_schema: https://w3id.org/fga-wg/schema/top_level
rank: 1000
domain_of:
- TopLevel
range: Sample
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>