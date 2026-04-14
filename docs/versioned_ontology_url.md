---
search:
  boost: 5.0
---

# Slot: versioned_ontology_url 


_The versioned URL of the ontology (e.g. the "versionIRI" in OWL)._



<div data-search-exclude markdown="1">



URI: [https://w3id.org/fga-wg/schema/top_level/versioned_ontology_url](https://w3id.org/fga-wg/schema/top_level/versioned_ontology_url)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [OntologyVersions](OntologyVersions.md) | Information about an ontology used in the metadata. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Uri](Uri.md) |
| Domain Of | [OntologyVersions](OntologyVersions.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |









## Examples

| Value |
| --- |
| http://edamontology.org/EDAM_1.21.owl |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fga-wg/schema/top_level




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/fga-wg/schema/top_level/versioned_ontology_url |
| native | https://w3id.org/fga-wg/schema/top_level/versioned_ontology_url |




## LinkML Source

<details>
```yaml
name: versioned_ontology_url
description: The versioned URL of the ontology (e.g. the "versionIRI" in OWL).
examples:
- value: http://edamontology.org/EDAM_1.21.owl
from_schema: https://w3id.org/fga-wg/schema/top_level
rank: 1000
domain_of:
- OntologyVersions
range: uri
required: true

```
</details></div>