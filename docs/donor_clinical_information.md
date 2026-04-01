

# Slot: donor_clinical_information 


_Clinical information of the donor/organism at the time of sampling._





URI: [https://w3id.org/fga-wg/schema/top_level/donor_clinical_information](https://w3id.org/fga-wg/schema/top_level/donor_clinical_information)
Alias: donor_clinical_information

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Sample](Sample.md) | Information about a biospecimen/sample used as raw material for lab experimen... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Sample](Sample.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |









## Examples

| Value |
| --- |
| apparently healthy |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fga-wg/schema/top_level




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/fga-wg/schema/top_level/donor_clinical_information |
| native | https://w3id.org/fga-wg/schema/top_level/donor_clinical_information |




## LinkML Source

<details>
```yaml
name: donor_clinical_information
description: Clinical information of the donor/organism at the time of sampling.
examples:
- value: apparently healthy
from_schema: https://w3id.org/fga-wg/schema/top_level
rank: 1000
alias: donor_clinical_information
domain_of:
- Sample
range: string

```
</details>