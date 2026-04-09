

# Slot: filecollection_description 


_Human-readable description of the file collection._





URI: [https://w3id.org/fga-wg/schema/top_level/filecollection_description](https://w3id.org/fga-wg/schema/top_level/filecollection_description)
Alias: filecollection_description

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [FileCollection](FileCollection.md) | A collection of files, according to some selection criteria |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Uri](Uri.md)&nbsp;or&nbsp;<br />[Any](Any.md)&nbsp;or&nbsp;<br />[String](String.md) |
| Domain Of | [FileCollection](FileCollection.md) |

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
| ENCODE dataset in the International Human Epigenome Consortium (IHEC) data portal, enhanced with metadata from the ENCODE data portal. |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fga-wg/schema/top_level




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/fga-wg/schema/top_level/filecollection_description |
| native | https://w3id.org/fga-wg/schema/top_level/filecollection_description |




## LinkML Source

<details>
```yaml
name: filecollection_description
description: Human-readable description of the file collection.
examples:
- value: ENCODE dataset in the International Human Epigenome Consortium (IHEC) data
    portal, enhanced with metadata from the ENCODE data portal.
from_schema: https://w3id.org/fga-wg/schema/top_level
rank: 1000
alias: filecollection_description
domain_of:
- FileCollection
range: Any
any_of:
- range: string
- range: uri

```
</details>