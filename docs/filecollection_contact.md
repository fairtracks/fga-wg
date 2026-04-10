---
search:
  boost: 5.0
---

# Slot: filecollection_contact 


_Contact point to the creator and/or maintainer of the file collection._



<div data-search-exclude markdown="1">



URI: [https://w3id.org/fga-wg/schema/top_level/filecollection_contact](https://w3id.org/fga-wg/schema/top_level/filecollection_contact)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [FileCollection](FileCollection.md) | A collection of files, according to some selection criteria |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Contact](Contact.md) |
| Domain Of | [FileCollection](FileCollection.md) |

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
| self | https://w3id.org/fga-wg/schema/top_level/filecollection_contact |
| native | https://w3id.org/fga-wg/schema/top_level/filecollection_contact |




## LinkML Source

<details>
```yaml
name: filecollection_contact
description: Contact point to the creator and/or maintainer of the file collection.
examples:
- object:
    name: International Human Epigenome Consortium
    contact_id: bioproject:PRJNA234466
    email: info@ihec-epigenomes.org
from_schema: https://w3id.org/fga-wg/schema/top_level
rank: 1000
domain_of:
- FileCollection
range: Contact

```
</details></div>