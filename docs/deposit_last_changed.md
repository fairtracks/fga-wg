---
search:
  boost: 5.0
---

# Slot: deposit_last_changed 


_The date and time of the last deposited change of the current metadata document (corresponding to "deposit_versioned_id")._



<div data-search-exclude markdown="1">



URI: [https://w3id.org/fga-wg/schema/top_level/deposit_last_changed](https://w3id.org/fga-wg/schema/top_level/deposit_last_changed)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Deposit](Deposit.md) | Information about a public deposit of a document containing metadata about a set of genome annotation files. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Datetime](Datetime.md) |
| Domain Of | [Deposit](Deposit.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |









## Examples

| Value |
| --- |
| 2025-07-01T12:36:00Z |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fga-wg/schema/top_level




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/fga-wg/schema/top_level/deposit_last_changed |
| native | https://w3id.org/fga-wg/schema/top_level/deposit_last_changed |




## LinkML Source

<details>
```yaml
name: deposit_last_changed
description: The date and time of the last deposited change of the current metadata
  document (corresponding to "deposit_versioned_id").
examples:
- value: '2025-07-01T12:36:00Z'
from_schema: https://w3id.org/fga-wg/schema/top_level
rank: 1000
domain_of:
- Deposit
range: datetime
required: true

```
</details></div>