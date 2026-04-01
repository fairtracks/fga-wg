

# Slot: ontology_url 


_The version-agnostic URL of the ontology (e.g. the IRI of the ontology in OWL)._





URI: [https://w3id.org/fga-wg/schema/top_level/ontology_url](https://w3id.org/fga-wg/schema/top_level/ontology_url)
Alias: ontology_url

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [OntologyVersions](OntologyVersions.md) | Information about an ontology used in the metadata |  no  |






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
| http://edamontology.org/EDAM.owl |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fga-wg/schema/top_level




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/fga-wg/schema/top_level/ontology_url |
| native | https://w3id.org/fga-wg/schema/top_level/ontology_url |




## LinkML Source

<details>
```yaml
name: ontology_url
description: The version-agnostic URL of the ontology (e.g. the IRI of the ontology
  in OWL).
examples:
- value: http://edamontology.org/EDAM.owl
from_schema: https://w3id.org/fga-wg/schema/top_level
rank: 1000
alias: ontology_url
domain_of:
- OntologyVersions
range: uri
required: true

```
</details>