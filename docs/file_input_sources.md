

# Slot: file_input_sources 


_External or internal references to data sources for the file, typically a data collection or a process that has generated the file. Internal references should lead to FileCollection, File, Experiment, or Analysis objects._





URI: [https://w3id.org/fga-wg/schema/top_level/file_input_sources](https://w3id.org/fga-wg/schema/top_level/file_input_sources)
Alias: file_input_sources

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
| Range | [InputSource](InputSource.md) |
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
| self | https://w3id.org/fga-wg/schema/top_level/file_input_sources |
| native | https://w3id.org/fga-wg/schema/top_level/file_input_sources |




## LinkML Source

<details>
```yaml
name: file_input_sources
description: External or internal references to data sources for the file, typically
  a data collection or a process that has generated the file. Internal references
  should lead to FileCollection, File, Experiment, or Analysis objects.
examples:
- object:
    inputsource_ref: analysis:ENCAN718KHT
    qualified_relation: prov:wasGeneratedBy
    biological_replicate_labels:
    - '1'
    - '2'
    technical_replicate_labels:
    - '1_1'
    - '2_1'
from_schema: https://w3id.org/fga-wg/schema/top_level
rank: 1000
alias: file_input_sources
domain_of:
- File
range: InputSource
required: true
multivalued: true

```
</details>