

# Slot: biological_processes 


_Biological processes illuminated by the experiment._





URI: [https://w3id.org/fga-wg/schema/top_level/biological_processes](https://w3id.org/fga-wg/schema/top_level/biological_processes)
Alias: biological_processes

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
| self | https://w3id.org/fga-wg/schema/top_level/biological_processes |
| native | https://w3id.org/fga-wg/schema/top_level/biological_processes |




## LinkML Source

<details>
```yaml
name: biological_processes
description: Biological processes illuminated by the experiment.
examples:
- object:
    id: GO:0140999
    label: histone H3K4 trimethyltransferase activity
from_schema: https://w3id.org/fga-wg/schema/top_level
rank: 1000
alias: biological_processes
domain_of:
- Experiment
range: Term
multivalued: true

```
</details>