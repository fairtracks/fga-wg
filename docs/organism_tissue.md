

# Slot: organism_tissue 


_Part of organism (typically tissue or organ) from which the biospecimen/sample was taken, or cell line was derived from._





URI: [https://w3id.org/fga-wg/schema/top_level/organism_tissue](https://w3id.org/fga-wg/schema/top_level/organism_tissue)
Alias: organism_tissue

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Sample](Sample.md) | Information about a biospecimen/sample used as raw material for lab experimen... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Term](Term.md) |
| Domain Of | [Sample](Sample.md) |

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
| self | https://w3id.org/fga-wg/schema/top_level/organism_tissue |
| native | https://w3id.org/fga-wg/schema/top_level/organism_tissue |




## LinkML Source

<details>
```yaml
name: organism_tissue
description: Part of organism (typically tissue or organ) from which the biospecimen/sample
  was taken, or cell line was derived from.
examples:
- object:
    id: UBERON:0002048
    label: lung
from_schema: https://w3id.org/fga-wg/schema/top_level
rank: 1000
alias: organism_tissue
domain_of:
- Sample
range: Term

```
</details>