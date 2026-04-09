---
search:
  boost: 5.0
---

# Slot: headers 


_An optional list of headers to include in the HTTP request to `url`. These headers can be used to provide auth tokens required to fetch the object bytes._



<div data-search-exclude markdown="1">



URI: [https://w3id.org/fga-wg/schema/top_level/headers](https://w3id.org/fga-wg/schema/top_level/headers)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AccessURL](AccessURL.md) | The URL and associated HTTP headers to access the File object (orig: DrsObjec... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [AccessURL](AccessURL.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fga-wg/schema/top_level




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/fga-wg/schema/top_level/headers |
| native | https://w3id.org/fga-wg/schema/top_level/headers |




## LinkML Source

<details>
```yaml
name: headers
description: An optional list of headers to include in the HTTP request to `url`.
  These headers can be used to provide auth tokens required to fetch the object bytes.
from_schema: https://w3id.org/fga-wg/schema/top_level
rank: 1000
domain_of:
- AccessURL
range: string
multivalued: true

```
</details></div>