---
search:
  boost: 5.0
---

# Slot: drs_uri 


_A drs:// hostname-based URI, as defined in the DRS documentation, that tells clients how to access this object. The intent of this field is to make DRS objects self-contained, and therefore easier for clients to store and pass around. For example, if you arrive at this DRS JSON by resolving a compact identifier-based DRS URI, the self_uri presents you with a hostname and properly encoded DRS ID for use in subsequent access endpoint calls._



<div data-search-exclude markdown="1">



URI: [https://w3id.org/fga-wg/schema/top_level/drs_uri](https://w3id.org/fga-wg/schema/top_level/drs_uri)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [File](File.md) | General information about a particular data file. Most fields (marked with an asterix*) are copied from the GA4GH DRS DrsObject model (https://ga4gh.github.io/data-repository-service-schemas/preview/release/drs-1.4.0/docs/#tag/DrsObjectModel), which is the top-level object returned from a DRS server in response to a successful lookup call (i.e. https://ga4gh.github.io/data-repository-service-schemas/preview/release/drs-1.4.0/docs/#tag/Objects). |  no  |
| [GenomicAnnotationFile](GenomicAnnotationFile.md) | Information about a genomic annotation / track file. GenomicAnnotationFile is a specification of the File entity and inherits all the fields defined in File, in addition to the fields that are specific to GenomicAnnotationFile, as detailed here. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Uri](Uri.md) |
| Domain Of | [File](File.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |









## Examples

| Value |
| --- |
| drs://drs.example.org/ENCFF323LCS |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fga-wg/schema/top_level




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/fga-wg/schema/top_level/drs_uri |
| native | https://w3id.org/fga-wg/schema/top_level/drs_uri |




## LinkML Source

<details>
```yaml
name: drs_uri
description: A drs:// hostname-based URI, as defined in the DRS documentation, that
  tells clients how to access this object. The intent of this field is to make DRS
  objects self-contained, and therefore easier for clients to store and pass around.
  For example, if you arrive at this DRS JSON by resolving a compact identifier-based
  DRS URI, the self_uri presents you with a hostname and properly encoded DRS ID for
  use in subsequent access endpoint calls.
examples:
- value: drs://drs.example.org/ENCFF323LCS
from_schema: https://w3id.org/fga-wg/schema/top_level
rank: 1000
domain_of:
- File
range: uri

```
</details></div>