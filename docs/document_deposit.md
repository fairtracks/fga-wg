---
search:
  boost: 5.0
---

# Slot: document_deposit 


_Information about the public deposit of the metadata document._



<div data-search-exclude markdown="1">



URI: [https://w3id.org/fga-wg/schema/top_level/document_deposit](https://w3id.org/fga-wg/schema/top_level/document_deposit)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Document](Document.md) | Information about a document containing metadata about a set of genome annota... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Deposit](Deposit.md) |
| Domain Of | [Document](Document.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |









## Examples

| Value |
| --- |
| None |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fga-wg/schema/top_level




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/fga-wg/schema/top_level/document_deposit |
| native | https://w3id.org/fga-wg/schema/top_level/document_deposit |




## LinkML Source

<details>
```yaml
name: document_deposit
description: Information about the public deposit of the metadata document.
examples:
- object:
    deposit_id: doi:10.1234/zenodo.12345678
    deposit_versioned_id: doi:10.1234/zenodo.12345679
    deposit_first_created: '2025-07-01T12:36:00Z'
    deposit_last_changed: '2025-07-01T12:36:00Z'
from_schema: https://w3id.org/fga-wg/schema/top_level
rank: 1000
domain_of:
- Document
range: Deposit
inlined: true

```
</details></div>