---
search:
  boost: 5.0
---

# Slot: name 


_Name of the person or organisation._



<div data-search-exclude markdown="1">



URI: [https://w3id.org/fga-wg/schema/top_level/name](https://w3id.org/fga-wg/schema/top_level/name)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Contact](Contact.md) | Contact information for a person or an organisation |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Contact](Contact.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |









## Examples

| Value |
| --- |
| John Doe |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fga-wg/schema/top_level




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/fga-wg/schema/top_level/name |
| native | https://w3id.org/fga-wg/schema/top_level/name |




## LinkML Source

<details>
```yaml
name: name
description: Name of the person or organisation.
examples:
- value: John Doe
from_schema: https://w3id.org/fga-wg/schema/top_level
rank: 1000
domain_of:
- Contact
range: string
required: true

```
</details></div>