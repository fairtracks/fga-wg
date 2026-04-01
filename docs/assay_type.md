

# Slot: assay_type 


_Sequencing technique intended for this library._





URI: [https://w3id.org/fga-wg/schema/top_level/assay_type](https://w3id.org/fga-wg/schema/top_level/assay_type)
Alias: assay_type

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
| Required | Yes |









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
| self | https://w3id.org/fga-wg/schema/top_level/assay_type |
| native | https://w3id.org/fga-wg/schema/top_level/assay_type |




## LinkML Source

<details>
```yaml
name: assay_type
description: Sequencing technique intended for this library.
examples:
- object:
    id: obi:OBI_0000716
    label: ChIP-seq assay
from_schema: https://w3id.org/fga-wg/schema/top_level
rank: 1000
alias: assay_type
domain_of:
- Experiment
range: Term
required: true

```
</details>