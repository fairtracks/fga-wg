---
search:
  boost: 5.0
---

# Slot: document_label 


_A human-readable description of the metadata document, short enough to be used for listings within software user interfaces, tables, illustration legends, etc._



<div data-search-exclude markdown="1">



URI: [https://w3id.org/fga-wg/schema/top_level/document_label](https://w3id.org/fga-wg/schema/top_level/document_label)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Document](Document.md) | Information about a document containing metadata about a set of genome annota... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Document](Document.md) |

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


* from schema: https://w3id.org/fga-wg/schema/top_level




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/fga-wg/schema/top_level/document_label |
| native | https://w3id.org/fga-wg/schema/top_level/document_label |




## LinkML Source

<details>
```yaml
name: document_label
description: A human-readable description of the metadata document, short enough to
  be used for listings within software user interfaces, tables, illustration legends,
  etc.
examples:
- value: IHEC data portal metadata, harmonised to the FGA-WG model.
from_schema: https://w3id.org/fga-wg/schema/top_level
rank: 1000
domain_of:
- Document
range: string
required: true
pattern: ^.{1,60}$

```
</details></div>