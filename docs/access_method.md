---
search:
  boost: 5.0
---

# Slot: access_method 


_Access method used to access the File object (orig: DrsObject)._



<div data-search-exclude markdown="1">



URI: [https://w3id.org/fga-wg/schema/top_level/access_method](https://w3id.org/fga-wg/schema/top_level/access_method)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AccessMethod](AccessMethod.md) | Description of an access method (i.e. communication protocol) that can be used to fetch a File object (orig: DrsObject). Exact copy of the AccessMethod object of the GA4GH DRS data model (https://ga4gh.github.io/data-repository-service-schemas/preview/release/drs-1.4.0/docs/#tag/AccessMethodModel) |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [AccessMethods](AccessMethods.md) |
| Domain Of | [AccessMethod](AccessMethod.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |









## Examples

| Value |
| --- |
| https |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fga-wg/schema/top_level




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/fga-wg/schema/top_level/access_method |
| native | https://w3id.org/fga-wg/schema/top_level/access_method |




## LinkML Source

<details>
```yaml
name: access_method
description: 'Access method used to access the File object (orig: DrsObject).'
examples:
- value: https
from_schema: https://w3id.org/fga-wg/schema/top_level
rank: 1000
domain_of:
- AccessMethod
range: AccessMethods
required: true

```
</details></div>