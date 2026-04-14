---
search:
  boost: 5.0
---

# Slot: genome_assembly 


_Information about the genome assembly used to generate the genomic annotation file, consequently defining the genomic coordinate system for the annotation._



<div data-search-exclude markdown="1">



URI: [https://w3id.org/fga-wg/schema/top_level/genome_assembly](https://w3id.org/fga-wg/schema/top_level/genome_assembly)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [GenomicAnnotationFile](GenomicAnnotationFile.md) | Information about a genomic annotation / track file. GenomicAnnotationFile is a specification of the File entity and inherits all the fields defined in File, in addition to the fields that are specific to GenomicAnnotationFile, as detailed here. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [GenomeAssembly](GenomeAssembly.md) |
| Domain Of | [GenomicAnnotationFile](GenomicAnnotationFile.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |









## Examples

| Value |
| --- |
| ga4gh:SC.EiFob05aCWgVU_B_Ae0cypnQut3cxUP1 |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fga-wg/schema/top_level




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/fga-wg/schema/top_level/genome_assembly |
| native | https://w3id.org/fga-wg/schema/top_level/genome_assembly |




## LinkML Source

<details>
```yaml
name: genome_assembly
description: Information about the genome assembly used to generate the genomic annotation
  file, consequently defining the genomic coordinate system for the annotation.
examples:
- value: ga4gh:SC.EiFob05aCWgVU_B_Ae0cypnQut3cxUP1
from_schema: https://w3id.org/fga-wg/schema/top_level
rank: 1000
domain_of:
- GenomicAnnotationFile
range: GenomeAssembly
required: true

```
</details></div>