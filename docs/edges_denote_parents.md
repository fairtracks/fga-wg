

# Slot: edges_denote_parents 


_Whether the edges linking sequence features denote a parent-child relationship (all edges between sequence features denote parent-child relationships such as genes to exons, i.e. where the child is fully covered by the parent)._





URI: [https://w3id.org/fga-wg/schema/top_level/edges_denote_parents](https://w3id.org/fga-wg/schema/top_level/edges_denote_parents)
Alias: edges_denote_parents

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [TrackGeometry](TrackGeometry.md) | Overall geometric properties of the sequence features in the genomic annotati... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Boolean](Boolean.md) |
| Domain Of | [TrackGeometry](TrackGeometry.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fga-wg/schema/top_level




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/fga-wg/schema/top_level/edges_denote_parents |
| native | https://w3id.org/fga-wg/schema/top_level/edges_denote_parents |




## LinkML Source

<details>
```yaml
name: edges_denote_parents
description: Whether the edges linking sequence features denote a parent-child relationship
  (all edges between sequence features denote parent-child relationships such as genes
  to exons, i.e. where the child is fully covered by the parent).
from_schema: https://w3id.org/fga-wg/schema/top_level
rank: 1000
alias: edges_denote_parents
domain_of:
- TrackGeometry
range: boolean

```
</details>