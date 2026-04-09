---
search:
  boost: 5.0
---

# Slot: email 


_E-mail address of the person or organisation._



<div data-search-exclude markdown="1">



URI: [https://w3id.org/fga-wg/schema/top_level/email](https://w3id.org/fga-wg/schema/top_level/email)
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
### Value Constraints

| Property | Value |
| --- | --- |
| Regex Pattern | `^\S+@\S+\.\S+$` |











## Examples

| Value |
| --- |
| john@doe.com |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fga-wg/schema/top_level




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/fga-wg/schema/top_level/email |
| native | https://w3id.org/fga-wg/schema/top_level/email |




## LinkML Source

<details>
```yaml
name: email
description: E-mail address of the person or organisation.
examples:
- value: john@doe.com
from_schema: https://w3id.org/fga-wg/schema/top_level
rank: 1000
domain_of:
- Contact
range: string
pattern: ^\S+@\S+\.\S+$

```
</details></div>