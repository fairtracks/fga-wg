---
search:
  boost: 5.0
---

# Slot: bundle_description 


_Human-readable description of the bundle._



<div data-search-exclude markdown="1">



URI: [https://w3id.org/fga-wg/schema/bundle/bundle_description](https://w3id.org/fga-wg/schema/bundle/bundle_description)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [BundleMetadata](BundleMetadata.md) | Top-level metadata about a bundle representing a set of genome annotation files, harmonised according to the "FAIRification of Genomic Annotations" data model.  This includes self-referential identifiers and versioning of public deposits of the harmonized metadata. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Any](Any.md)&nbsp;or&nbsp;<br />[String](String.md)&nbsp;or&nbsp;<br />[Uri](Uri.md) |
| Domain Of | [BundleMetadata](BundleMetadata.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
<details>
<summary>Expressions & Logic</summary>
#### Any Of

Value must satisfy at least one of:
- AnonymousSlotExpression({'range': 'string'})
- AnonymousSlotExpression({'range': 'uri'})

</details>










## Examples

| Value |
| --- |
| The metadata contents of the International Human Epigenome Consortium (IHEC) data portal, harmonised to follow the metadata model developed by the "FAIRification of Genomic Annotations WG" in the Research Data Alliance (RDA), enhanced with metadata from original sources. |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fga-wg/schema/bundle




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/fga-wg/schema/bundle/bundle_description |
| native | https://w3id.org/fga-wg/schema/bundle/bundle_description |




## LinkML Source

<details>
```yaml
name: bundle_description
description: Human-readable description of the bundle.
examples:
- value: The metadata contents of the International Human Epigenome Consortium (IHEC)
    data portal, harmonised to follow the metadata model developed by the "FAIRification
    of Genomic Annotations WG" in the Research Data Alliance (RDA), enhanced with
    metadata from original sources.
from_schema: https://w3id.org/fga-wg/schema/bundle
rank: 1000
domain_of:
- BundleMetadata
range: Any
any_of:
- range: string
- range: uri

```
</details></div>