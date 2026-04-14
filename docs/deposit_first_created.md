---
search:
  boost: 5.0
---

# Slot: deposit_first_created 


_The date and time of the creation of the first deposited version of the metadata document._



<div data-search-exclude markdown="1">



URI: [https://w3id.org/fga-wg/schema/bundle/deposit_first_created](https://w3id.org/fga-wg/schema/bundle/deposit_first_created)
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


* from schema: https://w3id.org/fga-wg/schema/bundle




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/fga-wg/schema/bundle/deposit_first_created |
| native | https://w3id.org/fga-wg/schema/bundle/deposit_first_created |




## LinkML Source

<details>
```yaml
name: deposit_first_created
description: The date and time of the creation of the first deposited version of the
  metadata document.
examples:
- value: '2025-07-01T12:36:00Z'
from_schema: https://w3id.org/fga-wg/schema/bundle
rank: 1000
domain_of:
- Deposit
range: datetime
required: true

```
</details></div>