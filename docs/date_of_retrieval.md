---
search:
  boost: 5.0
---

# Slot: date_of_retrieval 


_Date of retrieval from the input source, typically used to timestamp downloading data from a database or URL._



<div data-search-exclude markdown="1">



URI: [https://w3id.org/fga-wg/schema/top_level/date_of_retrieval](https://w3id.org/fga-wg/schema/top_level/date_of_retrieval)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [InputSource](InputSource.md) | General object representing the source of data files, samples, or other entities used as input to a process or a result. An input source refering to a single file or sample object will represent that item only, while an input source referring to a container or process may represent a number of disctinct input items. InputSource also contains information about the type of relationship, replication labelling, versioning and retrieval date. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Date](Date.md) |
| Domain Of | [InputSource](InputSource.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |









## Examples

| Value |
| --- |
| 2016-04-19 |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fga-wg/schema/top_level




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/fga-wg/schema/top_level/date_of_retrieval |
| native | https://w3id.org/fga-wg/schema/top_level/date_of_retrieval |




## LinkML Source

<details>
```yaml
name: date_of_retrieval
description: Date of retrieval from the input source, typically used to timestamp
  downloading data from a database or URL.
examples:
- value: '2016-04-19'
from_schema: https://w3id.org/fga-wg/schema/top_level
rank: 1000
domain_of:
- InputSource
range: date

```
</details></div>