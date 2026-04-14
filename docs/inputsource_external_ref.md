---
search:
  boost: 5.0
---

# Slot: inputsource_external_ref 


_Reference to an external entity as the input source, using a globally unique identifier or an URL. External references will in most cases refer to a database, data record, data file, website or other data source. One of "inputsource_external_ref" or "inputsource_ref" must be specified._



<div data-search-exclude markdown="1">



URI: [https://w3id.org/fga-wg/schema/bundle/inputsource_external_ref](https://w3id.org/fga-wg/schema/bundle/inputsource_external_ref)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [InputSource](InputSource.md) | General object representing the source of data files, samples, or other entities used as input to a process or a result. An input source refering to a single file or sample object will represent that item only, while an input source referring to a container or process may represent a number of disctinct input items. InputSource also contains information about the type of relationship, replication labelling, versioning and retrieval date. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Uriorcurie](Uriorcurie.md) |
| Domain Of | [InputSource](InputSource.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |









## Examples

| Value |
| --- |
| https://www.encodeproject.org/files/GRCh38_no_alt_analysis_set_GCA_000001405.15 |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fga-wg/schema/bundle




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/fga-wg/schema/bundle/inputsource_external_ref |
| native | https://w3id.org/fga-wg/schema/bundle/inputsource_external_ref |




## LinkML Source

<details>
```yaml
name: inputsource_external_ref
description: Reference to an external entity as the input source, using a globally
  unique identifier or an URL. External references will in most cases refer to a database,
  data record, data file, website or other data source. One of "inputsource_external_ref"
  or "inputsource_ref" must be specified.
examples:
- value: https://www.encodeproject.org/files/GRCh38_no_alt_analysis_set_GCA_000001405.15
from_schema: https://w3id.org/fga-wg/schema/bundle
rank: 1000
domain_of:
- InputSource
range: uriorcurie

```
</details></div>