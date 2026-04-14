---
search:
  boost: 5.0
---

# Slot: checksums 


_A list of checksums of the data file. At least one checksum must be provided. For blobs, the checksum is computed over the bytes in the blob._



<div data-search-exclude markdown="1">



URI: [https://w3id.org/fga-wg/schema/top_level/checksums](https://w3id.org/fga-wg/schema/top_level/checksums)
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
| Range | [Checksum](Checksum.md) |
| Domain Of | [File](File.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
| Multivalued | Yes |









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
| self | https://w3id.org/fga-wg/schema/top_level/checksums |
| native | https://w3id.org/fga-wg/schema/top_level/checksums |




## LinkML Source

<details>
```yaml
name: checksums
description: A list of checksums of the data file. At least one checksum must be provided.
  For blobs, the checksum is computed over the bytes in the blob.
examples:
- object:
    checksum: 535bc9628a1c5e5215226f9996e4eaca
    checksum_type: md5
from_schema: https://w3id.org/fga-wg/schema/top_level
rank: 1000
domain_of:
- File
range: Checksum
required: true
multivalued: true

```
</details></div>