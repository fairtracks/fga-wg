

# Slot: genome_assembly 


_Information about the genome assembly used to generate the genomic annotation file, consequently defining the genomic coordinate system for the annotation._





URI: [https://w3id.org/fga-wg/schema/top_level/genome_assembly](https://w3id.org/fga-wg/schema/top_level/genome_assembly)
Alias: genome_assembly

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [GenomicAnnotationFile](GenomicAnnotationFile.md) | Information about a genomic annotation / track file |  no  |






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
alias: genome_assembly
domain_of:
- GenomicAnnotationFile
range: GenomeAssembly
required: true

```
</details>