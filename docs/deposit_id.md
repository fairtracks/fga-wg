---
search:
  boost: 5.0
---

# Slot: deposit_id 


_A globally unique and persistent identifier for the public deposit of the metadata document. A DOI or other persistent identifier is recommended._



<div data-search-exclude markdown="1">



URI: [https://w3id.org/fga-wg/schema/top_level/deposit_id](https://w3id.org/fga-wg/schema/top_level/deposit_id)
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









## Examples

| Value |
| --- |
| doi:10.1234/zenodo.12345678 |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fga-wg/schema/top_level




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/fga-wg/schema/top_level/deposit_id |
| native | https://w3id.org/fga-wg/schema/top_level/deposit_id |




## LinkML Source

<details>
```yaml
name: deposit_id
description: A globally unique and persistent identifier for the public deposit of
  the metadata document. A DOI or other persistent identifier is recommended.
examples:
- value: doi:10.1234/zenodo.12345678
from_schema: https://w3id.org/fga-wg/schema/top_level
rank: 1000
domain_of:
- Deposit
range: curie

```
</details></div>