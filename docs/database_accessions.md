---
search:
  boost: 5.0
---

# Slot: database_accessions 


_Accession numbers for database records used as input source. Used in connection with "inputsource_external_ref"._



<div data-search-exclude markdown="1">



URI: [https://w3id.org/fga-wg/schema/top_level/database_accessions](https://w3id.org/fga-wg/schema/top_level/database_accessions)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [InputSource](InputSource.md) | General object representing the source of data files, samples, or other entities used as input to a process or a result. An input source refering to a single file or sample object will represent that item only, while an input source referring to a container or process may represent a number of disctinct input items. InputSource also contains information about the type of relationship, replication labelling, versioning and retrieval date. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Any](Any.md)&nbsp;or&nbsp;<br />[String](String.md)&nbsp;or&nbsp;<br />[Curie](Curie.md) |
| Domain Of | [InputSource](InputSource.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
<details>
<summary>Expressions & Logic</summary>
#### Any Of

Value must satisfy at least one of:
- AnonymousSlotExpression({'range': 'string'})
- AnonymousSlotExpression({'range': 'curie'})

</details>











## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fga-wg/schema/top_level




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/fga-wg/schema/top_level/database_accessions |
| native | https://w3id.org/fga-wg/schema/top_level/database_accessions |




## LinkML Source

<details>
```yaml
name: database_accessions
description: Accession numbers for database records used as input source. Used in
  connection with "inputsource_external_ref".
from_schema: https://w3id.org/fga-wg/schema/top_level
rank: 1000
domain_of:
- InputSource
range: Any
multivalued: true
any_of:
- range: string
- range: curie

```
</details></div>