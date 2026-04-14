---
search:
  boost: 5.0
---

# Slot: url 


_A fully resolvable URL that can be used to fetch the actual object bytes._



<div data-search-exclude markdown="1">



URI: [https://w3id.org/fga-wg/schema/bundle/url](https://w3id.org/fga-wg/schema/bundle/url)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AccessURL](AccessURL.md) | The URL and associated HTTP headers to access the File object (orig: DrsObject). Exact copy of AccessURL object of the GA4GH DRS data model (https://ga4gh.github.io/data-repository-service-schemas/preview/release/drs-1.4.0/docs/#tag/AccessURLModel). |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Uri](Uri.md) |
| Domain Of | [AccessURL](AccessURL.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |









## Examples

| Value |
| --- |
| https://epigenomesportal.ca/tracks/ENCODE/hg38/87234.ENCODE.ENCBS004ENC.H3K9me3.peak_calls.bigBed |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fga-wg/schema/bundle




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/fga-wg/schema/bundle/url |
| native | https://w3id.org/fga-wg/schema/bundle/url |




## LinkML Source

<details>
```yaml
name: url
description: A fully resolvable URL that can be used to fetch the actual object bytes.
examples:
- value: https://epigenomesportal.ca/tracks/ENCODE/hg38/87234.ENCODE.ENCBS004ENC.H3K9me3.peak_calls.bigBed
from_schema: https://w3id.org/fga-wg/schema/bundle
rank: 1000
domain_of:
- AccessURL
range: uri
required: true

```
</details></div>