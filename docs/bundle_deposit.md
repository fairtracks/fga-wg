---
search:
  boost: 5.0
---

# Slot: bundle_deposit 


_Information about the public deposit of the bundle._



<div data-search-exclude markdown="1">



URI: [https://w3id.org/fga-wg/schema/bundle/bundle_deposit](https://w3id.org/fga-wg/schema/bundle/bundle_deposit)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [BundleMetadata](BundleMetadata.md) | Top-level metadata about a bundle representing a set of genome annotation files, harmonised according to the "FAIRification of Genomic Annotations" data model.  This includes self-referential identifiers and versioning of public deposits of the harmonized metadata. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Deposit](Deposit.md) |
| Domain Of | [BundleMetadata](BundleMetadata.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |









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
| self | https://w3id.org/fga-wg/schema/bundle/bundle_deposit |
| native | https://w3id.org/fga-wg/schema/bundle/bundle_deposit |




## LinkML Source

<details>
```yaml
name: bundle_deposit
description: Information about the public deposit of the bundle.
examples:
- object:
    deposit_id: doi:10.1234/zenodo.12345678
    deposit_versioned_id: doi:10.1234/zenodo.12345679
    deposit_first_created: '2025-07-01T12:36:00Z'
    deposit_last_changed: '2025-07-01T12:36:00Z'
from_schema: https://w3id.org/fga-wg/schema/bundle
rank: 1000
domain_of:
- BundleMetadata
range: Deposit
inlined: true

```
</details></div>