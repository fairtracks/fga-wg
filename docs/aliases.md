

# Slot: aliases 


_Human-readable aliases of the genome assembly. Can be imprecise, as preciseness is enforced in the other fields._





URI: [https://w3id.org/fga-wg/schema/top_level/aliases](https://w3id.org/fga-wg/schema/top_level/aliases)
Alias: aliases

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [GenomeAssembly](GenomeAssembly.md) | Information about of the exact genome assembly used to generate the annotatio... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Curie](Curie.md) |
| Domain Of | [GenomeAssembly](GenomeAssembly.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
| Multivalued | Yes |









## Examples

| Value |
| --- |
| GRCh38_no_alt_analysis_set_GCA_000001405.15 |
| GRCh38 |
| hg38 |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fga-wg/schema/top_level




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/fga-wg/schema/top_level/aliases |
| native | https://w3id.org/fga-wg/schema/top_level/aliases |




## LinkML Source

<details>
```yaml
name: aliases
description: Human-readable aliases of the genome assembly. Can be imprecise, as preciseness
  is enforced in the other fields.
examples:
- value: GRCh38_no_alt_analysis_set_GCA_000001405.15
- value: GRCh38
- value: hg38
from_schema: https://w3id.org/fga-wg/schema/top_level
rank: 1000
alias: aliases
domain_of:
- GenomeAssembly
range: curie
required: true
multivalued: true

```
</details>