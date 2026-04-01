

# Slot: library_layout 


_Whether the library was built as paired-end, or single-end._





URI: [https://w3id.org/fga-wg/schema/top_level/library_layout](https://w3id.org/fga-wg/schema/top_level/library_layout)
Alias: library_layout

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Experiment](Experiment.md) | Represents a sequencing experiment that has been carried out within a study, ... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Term](Term.md) |
| Domain Of | [Experiment](Experiment.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |









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
| self | https://w3id.org/fga-wg/schema/top_level/library_layout |
| native | https://w3id.org/fga-wg/schema/top_level/library_layout |




## LinkML Source

<details>
```yaml
name: library_layout
description: Whether the library was built as paired-end, or single-end.
examples:
- object:
    id: obi:OBI_0000736
    label: single fragment library
from_schema: https://w3id.org/fga-wg/schema/top_level
rank: 1000
alias: library_layout
domain_of:
- Experiment
range: Term

```
</details>