---
search:
  boost: 5.0
---

# Slot: bundle_metadata 


_Top-level metadata about the bundle of genomic annotation files._



<div data-search-exclude markdown="1">



URI: [https://w3id.org/fga-wg/schema/bundle/bundle_metadata](https://w3id.org/fga-wg/schema/bundle/bundle_metadata)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Bundle](Bundle.md) | A bundle representing a set of genome annotation files, organised in sub-collections. Metadata has been harmonised in line with the "FAIRification of Genomic Annotations" data model. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [BundleMetadata](BundleMetadata.md) |
| Domain Of | [Bundle](Bundle.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fga-wg/schema/bundle




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/fga-wg/schema/bundle/bundle_metadata |
| native | https://w3id.org/fga-wg/schema/bundle/bundle_metadata |




## LinkML Source

<details>
```yaml
name: bundle_metadata
description: Top-level metadata about the bundle of genomic annotation files.
from_schema: https://w3id.org/fga-wg/schema/bundle
rank: 1000
domain_of:
- Bundle
range: BundleMetadata
required: true
inlined: true

```
</details></div>