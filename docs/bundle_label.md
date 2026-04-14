---
search:
  boost: 5.0
---

# Slot: bundle_label 


_A human-readable description of the bundle, short enough to be used for listings within software user interfaces, tables, illustration legends, etc._



<div data-search-exclude markdown="1">



URI: [https://w3id.org/fga-wg/schema/bundle/bundle_label](https://w3id.org/fga-wg/schema/bundle/bundle_label)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [BundleMetadata](BundleMetadata.md) | Top-level metadata about a bundle representing a set of genome annotation files, harmonised according to the "FAIRification of Genomic Annotations" data model.  This includes self-referential identifiers and versioning of public deposits of the harmonized metadata. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [BundleMetadata](BundleMetadata.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Value Constraints

| Property | Value |
| --- | --- |
| Regex Pattern | `^.{1,60}$` |











## Examples

| Value |
| --- |
| IHEC data portal metadata, harmonised to the FGA-WG model. |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fga-wg/schema/bundle




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/fga-wg/schema/bundle/bundle_label |
| native | https://w3id.org/fga-wg/schema/bundle/bundle_label |




## LinkML Source

<details>
```yaml
name: bundle_label
description: A human-readable description of the bundle, short enough to be used for
  listings within software user interfaces, tables, illustration legends, etc.
examples:
- value: IHEC data portal metadata, harmonised to the FGA-WG model.
from_schema: https://w3id.org/fga-wg/schema/bundle
rank: 1000
domain_of:
- BundleMetadata
range: string
required: true
pattern: ^.{1,60}$

```
</details></div>