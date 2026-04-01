

# Slot: sample_label 


_A human-readable description of the sample, short enough to be used for listings within software user interfaces, tables, illustration legends, etc._





URI: [https://w3id.org/fga-wg/schema/top_level/sample_label](https://w3id.org/fga-wg/schema/top_level/sample_label)
Alias: sample_label

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
| Required | Yes |
### Value Constraints

| Property | Value |
| --- | --- |
| Regex Pattern | `^.{1,60}$` |











## Examples

| Value |
| --- |
| Homo sapiens AG04450 cell line |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fga-wg/schema/top_level




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/fga-wg/schema/top_level/sample_label |
| native | https://w3id.org/fga-wg/schema/top_level/sample_label |




## LinkML Source

<details>
```yaml
name: sample_label
description: A human-readable description of the sample, short enough to be used for
  listings within software user interfaces, tables, illustration legends, etc.
examples:
- value: Homo sapiens AG04450 cell line
from_schema: https://w3id.org/fga-wg/schema/top_level
rank: 1000
alias: sample_label
domain_of:
- Sample
range: string
required: true
pattern: ^.{1,60}$

```
</details>