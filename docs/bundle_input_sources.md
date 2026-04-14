---
search:
  boost: 5.0
---

# Slot: bundle_input_sources 


_References to other input sources from which this entire bundle was derived, or possibly including DOIs of other bundles used as source._



<div data-search-exclude markdown="1">



URI: [https://w3id.org/fga-wg/schema/bundle/bundle_input_sources](https://w3id.org/fga-wg/schema/bundle/bundle_input_sources)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [BundleMetadata](BundleMetadata.md) | Top-level metadata about a bundle representing a set of genome annotation files, harmonised according to the "FAIRification of Genomic Annotations" data model.  This includes self-referential identifiers and versioning of public deposits of the harmonized metadata. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [InputSource](InputSource.md) |
| Domain Of | [BundleMetadata](BundleMetadata.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |









## Examples

| Value |
| --- |
| None |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fga-wg/schema/bundle




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/fga-wg/schema/bundle/bundle_input_sources |
| native | https://w3id.org/fga-wg/schema/bundle/bundle_input_sources |




## LinkML Source

<details>
```yaml
name: bundle_input_sources
description: References to other input sources from which this entire bundle was derived,
  or possibly including DOIs of other bundles used as source.
examples:
- object:
    inputsource_external_ref: https://epigenomesportal.ca/ihec/
    qualified_relation: prov:wasDerivedFrom
from_schema: https://w3id.org/fga-wg/schema/bundle
rank: 1000
domain_of:
- BundleMetadata
range: InputSource
multivalued: true

```
</details></div>