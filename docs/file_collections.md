

# Slot: file_collections 


_Information about collections of files contained in this dataset, each collection defined according to some selection criteria._





URI: [https://w3id.org/fga-wg/schema/top_level/file_collections](https://w3id.org/fga-wg/schema/top_level/file_collections)
Alias: file_collections

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [TopLevel](TopLevel.md) | A document of harmonised metadata for a set of genome annotation files |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [FileCollection](FileCollection.md) |
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
| self | https://w3id.org/fga-wg/schema/top_level/file_collections |
| native | https://w3id.org/fga-wg/schema/top_level/file_collections |




## LinkML Source

<details>
```yaml
name: file_collections
description: Information about collections of files contained in this dataset, each
  collection defined according to some selection criteria.
from_schema: https://w3id.org/fga-wg/schema/top_level
rank: 1000
alias: file_collections
domain_of:
- TopLevel
range: FileCollection
multivalued: true
inlined: true
inlined_as_list: true

```
</details>