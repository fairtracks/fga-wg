---
search:
  boost: 5.0
---

# Slot: checksum 


_The hex-string encoded checksum for the data._



<div data-search-exclude markdown="1">



URI: [https://w3id.org/fga-wg/schema/top_level/checksum](https://w3id.org/fga-wg/schema/top_level/checksum)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Checksum](Checksum.md) | A checksum of a File object (orig: DrsObject). Exact copy of the Checksum object of the GA4GH DRS data model (https://ga4gh.github.io/data-repository-service-schemas/preview/release/drs-1.4.0/docs/#tag/ChecksumModel). |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Checksum](Checksum.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |









## Examples

| Value |
| --- |
| 535bc9628a1c5e5215226f9996e4eaca |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fga-wg/schema/top_level




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/fga-wg/schema/top_level/checksum |
| native | https://w3id.org/fga-wg/schema/top_level/checksum |




## LinkML Source

<details>
```yaml
name: checksum
description: The hex-string encoded checksum for the data.
examples:
- value: 535bc9628a1c5e5215226f9996e4eaca
from_schema: https://w3id.org/fga-wg/schema/top_level
rank: 1000
domain_of:
- Checksum
range: string

```
</details></div>