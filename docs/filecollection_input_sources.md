

# Slot: filecollection_input_sources 


_References to other input sources from which this file collection was derived._





URI: [https://w3id.org/fga-wg/schema/top_level/filecollection_input_sources](https://w3id.org/fga-wg/schema/top_level/filecollection_input_sources)
Alias: filecollection_input_sources

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [FileCollection](FileCollection.md) | A collection of files, according to some selection criteria |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [InputSource](InputSource.md) |
| Domain Of | [FileCollection](FileCollection.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |









## Examples

| Value |
| --- |
| None |
| None |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fga-wg/schema/top_level




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/fga-wg/schema/top_level/filecollection_input_sources |
| native | https://w3id.org/fga-wg/schema/top_level/filecollection_input_sources |




## LinkML Source

<details>
```yaml
name: filecollection_input_sources
description: References to other input sources from which this file collection was
  derived.
examples:
- object:
    inputsource_external_ref: https://epigenomesportal.ca/ihec/grid.html?build=2020-10&assembly=4&institutions=4
    qualified_relation: prov:wasDerivedFrom
    version: 2020-10
- object:
    inputsource_external_ref: https://www.encodeproject.org
    qualified_relation: prov:hadPrimarySource
from_schema: https://w3id.org/fga-wg/schema/top_level
rank: 1000
alias: filecollection_input_sources
domain_of:
- FileCollection
range: InputSource
multivalued: true

```
</details>