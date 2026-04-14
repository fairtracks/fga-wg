---
search:
  boost: 5.0
---

# Slot: id 


_External, globally unique identifier for the ontology term (in CURIE form)._



<div data-search-exclude markdown="1">



URI: [https://w3id.org/fga-wg/schema/bundle/id](https://w3id.org/fga-wg/schema/bundle/id)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Term](Term.md) | Helper entity to represent an ontology term as a data value. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Curie](Curie.md) |
| Domain Of | [Term](Term.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |









## Examples

| Value |
| --- |
| obi:OBI_0000716 |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fga-wg/schema/bundle




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/fga-wg/schema/bundle/id |
| native | https://w3id.org/fga-wg/schema/bundle/id |




## LinkML Source

<details>
```yaml
name: id
description: External, globally unique identifier for the ontology term (in CURIE
  form).
examples:
- value: obi:OBI_0000716
from_schema: https://w3id.org/fga-wg/schema/bundle
rank: 1000
domain_of:
- Term
range: curie
required: true

```
</details></div>