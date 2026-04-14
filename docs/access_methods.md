---
search:
  boost: 5.0
---

# Slot: access_methods 


_The list of access methods that can be used to fetch the data file. _



<div data-search-exclude markdown="1">



URI: [https://w3id.org/fga-wg/schema/top_level/access_methods](https://w3id.org/fga-wg/schema/top_level/access_methods)
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
| Range | [AccessMethod](AccessMethod.md) |
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
| None |
| None |
| None |
| None |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fga-wg/schema/top_level




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/fga-wg/schema/top_level/access_methods |
| native | https://w3id.org/fga-wg/schema/top_level/access_methods |




## LinkML Source

<details>
```yaml
name: access_methods
description: 'The list of access methods that can be used to fetch the data file. '
examples:
- object:
    access_method: https
    access_url:
      url: https://epigenomesportal.ca/tracks/ENCODE/hg38/87234.ENCODE.ENCBS004ENC.H3K9me3.peak_calls.bigBed
- object:
    access_method: https
    access_url:
      url: https://www.encodeproject.org/files/ENCFF323LCS/@@download/ENCFF323LCS.bigBed
- object:
    access_method: s3
    access_url:
      url: s3://encode-public/2016/11/13/efd4e74e-7875-4d13-9630-0085bc834f18/ENCFF323LCS.bigBed
- object:
    access_method: https
    access_url:
      url: https://encode-public.s3.amazonaws.com/2016/11/13/efd4e74e-7875-4d13-9630-0085bc834f18/ENCFF323LCS.bigBed
- object:
    access_method: https
    access_url:
      url: https://datasetencode.blob.core.windows.net/dataset/2016/11/13/efd4e74e-7875-4d13-9630-0085bc834f18/ENCFF323LCS.bigBed?sv=2019-10-10&si=prod&sr=c&sig=9qSQZo4ggrCNpybBExU8SypuUZV33igI11xw0P7rB3c%3D
from_schema: https://w3id.org/fga-wg/schema/top_level
rank: 1000
domain_of:
- File
range: AccessMethod
required: true
multivalued: true

```
</details></div>