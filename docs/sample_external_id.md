

# Slot: sample_external_id 


_External, globally unique identifier for the biospecimen/sample._





URI: [https://w3id.org/fga-wg/schema/top_level/sample_external_id](https://w3id.org/fga-wg/schema/top_level/sample_external_id)
Alias: sample_external_id

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Sample](Sample.md) | Information about a biospecimen/sample used as raw material for lab experimen... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Curie](Curie.md) |
| Domain Of | [Sample](Sample.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |









## Examples

| Value |
| --- |
| encode:ENCBS004ENC |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fga-wg/schema/top_level




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/fga-wg/schema/top_level/sample_external_id |
| native | https://w3id.org/fga-wg/schema/top_level/sample_external_id |




## LinkML Source

<details>
```yaml
name: sample_external_id
description: External, globally unique identifier for the biospecimen/sample.
examples:
- value: encode:ENCBS004ENC
from_schema: https://w3id.org/fga-wg/schema/top_level
rank: 1000
alias: sample_external_id
domain_of:
- Sample
range: curie
required: true

```
</details>