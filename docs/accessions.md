---
search:
  boost: 5.0
---

# Slot: accessions 


_Database accession numbers for the genome assembly, if available. Should precisely identify the genome assembly and be omitted if changes have been made to the assembly after retrieval, such as removing the alternate sequences._



<div data-search-exclude markdown="1">



URI: [https://w3id.org/fga-wg/schema/bundle/accessions](https://w3id.org/fga-wg/schema/bundle/accessions)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [GenomeAssembly](GenomeAssembly.md) | Information about of the exact genome assembly used to generate the annotation file, defining the genomic coordinate system for the sequence features. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [GenomeAssembly](GenomeAssembly.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |









## Examples

| Value |
| --- |
| encode:ENCSR425FOI |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fga-wg/schema/bundle




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/fga-wg/schema/bundle/accessions |
| native | https://w3id.org/fga-wg/schema/bundle/accessions |




## LinkML Source

<details>
```yaml
name: accessions
description: Database accession numbers for the genome assembly, if available. Should
  precisely identify the genome assembly and be omitted if changes have been made
  to the assembly after retrieval, such as removing the alternate sequences.
examples:
- value: encode:ENCSR425FOI
from_schema: https://w3id.org/fga-wg/schema/bundle
rank: 1000
domain_of:
- GenomeAssembly
range: string
multivalued: true

```
</details></div>