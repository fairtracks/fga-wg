

# Slot: inputsource_ref 


_Reference to an internal object as the input source using a local identifier. Entities to be used as an internal input source includes FileCollection, Sample, Experiment, Analysis or File as restricted by the description of the field where the input source is used. One of "inputsource_external_ref" or "inputsource_ref" must be specified._





URI: [https://w3id.org/fga-wg/schema/top_level/inputsource_ref](https://w3id.org/fga-wg/schema/top_level/inputsource_ref)
Alias: inputsource_ref

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [InputSource](InputSource.md) | General object representing the source of data files, samples, or other entit... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Curie](Curie.md) |
| Domain Of | [InputSource](InputSource.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fga-wg/schema/top_level




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/fga-wg/schema/top_level/inputsource_ref |
| native | https://w3id.org/fga-wg/schema/top_level/inputsource_ref |




## LinkML Source

<details>
```yaml
name: inputsource_ref
description: Reference to an internal object as the input source using a local identifier.
  Entities to be used as an internal input source includes FileCollection, Sample,
  Experiment, Analysis or File as restricted by the description of the field where
  the input source is used. One of "inputsource_external_ref" or "inputsource_ref"
  must be specified.
from_schema: https://w3id.org/fga-wg/schema/top_level
rank: 1000
alias: inputsource_ref
domain_of:
- InputSource
range: curie

```
</details>