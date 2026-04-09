---
search:
  boost: 5.0
---

# Slot: contact_id 


_Globally unique identifier for a person (e.g. ORCID ID) or organisation (e.g. BioProject accession)._



<div data-search-exclude markdown="1">



URI: [https://w3id.org/fga-wg/schema/top_level/contact_id](https://w3id.org/fga-wg/schema/top_level/contact_id)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Contact](Contact.md) | Contact information for a person or an organisation |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Curie](Curie.md) |
| Domain Of | [Contact](Contact.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |









## Examples

| Value |
| --- |
| orcid:0000-0001-2345-6789 |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fga-wg/schema/top_level




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/fga-wg/schema/top_level/contact_id |
| native | https://w3id.org/fga-wg/schema/top_level/contact_id |




## LinkML Source

<details>
```yaml
name: contact_id
description: Globally unique identifier for a person (e.g. ORCID ID) or organisation
  (e.g. BioProject accession).
examples:
- value: orcid:0000-0001-2345-6789
from_schema: https://w3id.org/fga-wg/schema/top_level
rank: 1000
domain_of:
- Contact
range: curie

```
</details></div>