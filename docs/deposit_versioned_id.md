---
search:
  boost: 5.0
---

# Slot: deposit_versioned_id 


_A globally unique, persistent and versioned identifier for the public deposit of the metadata document. A versioned DOI to a deposited document is recommended._



<div data-search-exclude markdown="1">



URI: [https://w3id.org/fga-wg/schema/top_level/deposit_versioned_id](https://w3id.org/fga-wg/schema/top_level/deposit_versioned_id)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Deposit](Deposit.md) | Information about a public deposit of a document containing metadata about a set of genome annotation files. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Curie](Curie.md) |
| Domain Of | [Deposit](Deposit.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Identifier | Yes |











## Examples

| Value |
| --- |
| doi:10.1234/zenodo.12345679 |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fga-wg/schema/top_level




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/fga-wg/schema/top_level/deposit_versioned_id |
| native | https://w3id.org/fga-wg/schema/top_level/deposit_versioned_id |




## LinkML Source

<details>
```yaml
name: deposit_versioned_id
description: A globally unique, persistent and versioned identifier for the public
  deposit of the metadata document. A versioned DOI to a deposited document is recommended.
examples:
- value: doi:10.1234/zenodo.12345679
from_schema: https://w3id.org/fga-wg/schema/top_level
rank: 1000
identifier: true
domain_of:
- Deposit
range: curie
required: true

```
</details></div>