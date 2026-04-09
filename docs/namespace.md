---
search:
  boost: 5.0
---

# Slot: namespace 


_The CURIE namespace (prefix) an ontology (e.g. "GO" for Gene Ontology)._



<div data-search-exclude markdown="1">



URI: [https://w3id.org/fga-wg/schema/top_level/namespace](https://w3id.org/fga-wg/schema/top_level/namespace)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [OntologyVersions](OntologyVersions.md) | Information about an ontology used in the metadata |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [OntologyVersions](OntologyVersions.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |









## Examples

| Value |
| --- |
| edam |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fga-wg/schema/top_level




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/fga-wg/schema/top_level/namespace |
| native | https://w3id.org/fga-wg/schema/top_level/namespace |




## LinkML Source

<details>
```yaml
name: namespace
description: The CURIE namespace (prefix) an ontology (e.g. "GO" for Gene Ontology).
examples:
- value: edam
from_schema: https://w3id.org/fga-wg/schema/top_level
rank: 1000
domain_of:
- OntologyVersions
range: string
required: true

```
</details></div>