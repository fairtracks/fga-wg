---
search:
  boost: 5.0
---

# Slot: filecollection_refs 


_Internal references to the FileCollection objects (within the deposit) that contains the data file, if any._



<div data-search-exclude markdown="1">



URI: [https://w3id.org/fga-wg/schema/bundle/filecollection_refs](https://w3id.org/fga-wg/schema/bundle/filecollection_refs)
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
| Range | [Curie](Curie.md) |
| Domain Of | [File](File.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
| Multivalued | Yes |









## Examples

| Value |
| --- |
| collection:ihec_encode |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fga-wg/schema/bundle




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/fga-wg/schema/bundle/filecollection_refs |
| native | https://w3id.org/fga-wg/schema/bundle/filecollection_refs |




## LinkML Source

<details>
```yaml
name: filecollection_refs
description: Internal references to the FileCollection objects (within the deposit)
  that contains the data file, if any.
examples:
- value: collection:ihec_encode
from_schema: https://w3id.org/fga-wg/schema/bundle
rank: 1000
domain_of:
- File
range: curie
required: true
multivalued: true

```
</details></div>