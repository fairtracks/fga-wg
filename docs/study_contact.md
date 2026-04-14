---
search:
  boost: 5.0
---

# Slot: study_contact 


_Contact point for the study._



<div data-search-exclude markdown="1">



URI: [https://w3id.org/fga-wg/schema/bundle/study_contact](https://w3id.org/fga-wg/schema/bundle/study_contact)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Study](Study.md) | A scientific study, i.e. a unit of research, within which experiments and/or analyses have been carried out. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Contact](Contact.md) |
| Domain Of | [Study](Study.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |









## Examples

| Value |
| --- |
| None |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fga-wg/schema/bundle




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/fga-wg/schema/bundle/study_contact |
| native | https://w3id.org/fga-wg/schema/bundle/study_contact |




## LinkML Source

<details>
```yaml
name: study_contact
description: Contact point for the study.
examples:
- object:
    name: Mark Gerstein
    contact_id: orcid:0000-0002-9746-3719
    email: mark@gersteinlab.org
from_schema: https://w3id.org/fga-wg/schema/bundle
rank: 1000
domain_of:
- Study
range: Contact

```
</details></div>