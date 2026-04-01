

# Slot: samples 


_Information about the biospecimens/samples used as raw material for lab experiments._





URI: [https://w3id.org/fga-wg/schema/top_level/samples](https://w3id.org/fga-wg/schema/top_level/samples)
Alias: samples

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [TopLevel](TopLevel.md) | A document of harmonised metadata for a set of genome annotation files |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Sample](Sample.md) |
| Domain Of | [TopLevel](TopLevel.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fga-wg/schema/top_level




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/fga-wg/schema/top_level/samples |
| native | https://w3id.org/fga-wg/schema/top_level/samples |




## LinkML Source

<details>
```yaml
name: samples
description: Information about the biospecimens/samples used as raw material for lab
  experiments.
from_schema: https://w3id.org/fga-wg/schema/top_level
rank: 1000
alias: samples
domain_of:
- TopLevel
range: Sample
multivalued: true
inlined: true
inlined_as_list: true

```
</details>