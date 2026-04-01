

# Slot: document_description 


_Human-readable description of the metadata document._





URI: [https://w3id.org/fga-wg/schema/top_level/document_description](https://w3id.org/fga-wg/schema/top_level/document_description)
Alias: document_description

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Document](Document.md) | Information about a document containing metadata about a set of genome annota... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md)&nbsp;or&nbsp;<br />[Uri](Uri.md)&nbsp;or&nbsp;<br />[Any](Any.md) |
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
alias: document_description
domain_of:
- Document
range: Any
any_of:
- range: string
- range: uri

```
</details>