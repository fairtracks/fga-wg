---
search:
  boost: 5.0
---

# Slot: run_provenance 


_Document detailing the provenance of the experiment or analysis run which produced the file as one of its outputs. The provenance info should include software versions, parameter settings, etc._



<div data-search-exclude markdown="1">



URI: [https://w3id.org/fga-wg/schema/top_level/run_provenance](https://w3id.org/fga-wg/schema/top_level/run_provenance)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [File](File.md) | General information about a particular data file |  no  |
| [GenomicAnnotationFile](GenomicAnnotationFile.md) | Information about a genomic annotation / track file |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Uriorcurie](Uriorcurie.md) |
| Domain Of | [File](File.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |









## Examples

| Value |
| --- |
| encode:ENCAN718KHT |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fga-wg/schema/top_level




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/fga-wg/schema/top_level/run_provenance |
| native | https://w3id.org/fga-wg/schema/top_level/run_provenance |




## LinkML Source

<details>
```yaml
name: run_provenance
description: Document detailing the provenance of the experiment or analysis run which
  produced the file as one of its outputs. The provenance info should include software
  versions, parameter settings, etc.
examples:
- value: encode:ENCAN718KHT
from_schema: https://w3id.org/fga-wg/schema/top_level
rank: 1000
domain_of:
- File
range: uriorcurie

```
</details></div>