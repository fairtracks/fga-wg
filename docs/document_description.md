---
search:
  boost: 5.0
---

# Slot: document_description 


_Human-readable description of the metadata document._



<div data-search-exclude markdown="1">



URI: [https://w3id.org/fga-wg/schema/top_level/document_description](https://w3id.org/fga-wg/schema/top_level/document_description)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Document](Document.md) | Information about a document containing metadata about a set of genome annotation files, harmonised according to the "FAIRification of Genomic Annotations" data model.  This includes self-referential identifiers and versioning of public deposits of the document. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Any](Any.md)&nbsp;or&nbsp;<br />[String](String.md)&nbsp;or&nbsp;<br />[Uri](Uri.md) |
| Domain Of | [Document](Document.md) |

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


* from schema: https://w3id.org/fga-wg/schema/top_level




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/fga-wg/schema/top_level/document_description |
| native | https://w3id.org/fga-wg/schema/top_level/document_description |




## LinkML Source

<details>
```yaml
name: document_description
description: Human-readable description of the metadata document.
examples:
- value: The metadata contents of the International Human Epigenome Consortium (IHEC)
    data portal, harmonised to follow the metadata model developed by the "FAIRification
    of Genomic Annotations WG" in the Research Data Alliance (RDA), enhanced with
    metadata from original sources.
from_schema: https://w3id.org/fga-wg/schema/top_level
rank: 1000
domain_of:
- Document
range: Any
any_of:
- range: string
- range: uri

```
</details></div>