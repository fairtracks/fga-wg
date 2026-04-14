---
search:
  boost: 5.0
---

# Slot: document_ontology_versions 


_Map from the version-agnostic URL to a versioned URL (e.g. "versionIRI" in owl) of each ontology used in the current metadata deposit (corresponding to deposit_versioned_id")._



<div data-search-exclude markdown="1">



URI: [https://w3id.org/fga-wg/schema/top_level/document_ontology_versions](https://w3id.org/fga-wg/schema/top_level/document_ontology_versions)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Document](Document.md) | Information about a document containing metadata about a set of genome annotation files, harmonised according to the "FAIRification of Genomic Annotations" data model.  This includes self-referential identifiers and versioning of public deposits of the document. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [OntologyVersions](OntologyVersions.md) |
| Domain Of | [Document](Document.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
| Multivalued | Yes |









## Examples

| Value |
| --- |
| None |
| None |
| None |
| None |
| None |
| None |
| None |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fga-wg/schema/top_level




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/fga-wg/schema/top_level/document_ontology_versions |
| native | https://w3id.org/fga-wg/schema/top_level/document_ontology_versions |




## LinkML Source

<details>
```yaml
name: document_ontology_versions
description: Map from the version-agnostic URL to a versioned URL (e.g. "versionIRI"
  in owl) of each ontology used in the current metadata deposit (corresponding to
  deposit_versioned_id").
examples:
- object:
    namespace: edam
    ontology_url: http://edamontology.org/EDAM.owl
    versioned_ontology_url: http://edamontology.org/EDAM_1.21.owl
- object:
    namespace: cl
    ontology_url: http://purl.obolibrary.org/obo/cl.owl
    versioned_ontology_url: http://purl.obolibrary.org/obo/cl/releases/2020-05-21/cl.owl
- object:
    namespace: efo
    ontology_url: http://www.ebi.ac.uk/efo/efo.owl
    versioned_ontology_url: http://www.ebi.ac.uk/efo/releases/v3.21.0/efo.owl
- object:
    namespace: ncit
    ontology_url: http://purl.obolibrary.org/obo/ncit.owl
    versioned_ontology_url: http://purl.obolibrary.org/obo/ncit/releases/2020-07-17/ncit.owl
- object:
    namespace: obi
    ontology_url: http://purl.obolibrary.org/obo/obi.owl
    versioned_ontology_url: http://purl.obolibrary.org/obo/obi/2020-04-23/obi.owl
- object:
    namespace: so
    ontology_url: http://purl.obolibrary.org/obo/so.owl
    versioned_ontology_url: http://purl.obolibrary.org/obo/so/2020-08-20/so.owl
- object:
    namespace: uberon
    ontology_url: http://purl.obolibrary.org/obo/uberon.owl
    versioned_ontology_url: http://purl.obolibrary.org/obo/uberon/releases/2020-06-30/uberon.owl
from_schema: https://w3id.org/fga-wg/schema/top_level
rank: 1000
domain_of:
- Document
range: OntologyVersions
required: true
multivalued: true

```
</details></div>