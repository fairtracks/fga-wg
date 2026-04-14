---
search:
  boost: 5.0
---

# Slot: sampling_protocol 


_Protocol detailing the collection and treatment of the biospecimen/sample._



<div data-search-exclude markdown="1">



URI: [https://w3id.org/fga-wg/schema/bundle/sampling_protocol](https://w3id.org/fga-wg/schema/bundle/sampling_protocol)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Sample](Sample.md) | Information about a biospecimen/sample used as raw material for lab experiments. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Uri](Uri.md) |
| Domain Of | [Sample](Sample.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |









## Examples

| Value |
| --- |
| https://www.encodeproject.org/documents/3ed29dac-da67-47be-91b0-c9cad6a1b791/@@download/attachment/AG04450_Stam_protocol.pdf |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fga-wg/schema/bundle




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/fga-wg/schema/bundle/sampling_protocol |
| native | https://w3id.org/fga-wg/schema/bundle/sampling_protocol |




## LinkML Source

<details>
```yaml
name: sampling_protocol
description: Protocol detailing the collection and treatment of the biospecimen/sample.
examples:
- value: https://www.encodeproject.org/documents/3ed29dac-da67-47be-91b0-c9cad6a1b791/@@download/attachment/AG04450_Stam_protocol.pdf
from_schema: https://w3id.org/fga-wg/schema/bundle
rank: 1000
domain_of:
- Sample
range: uri

```
</details></div>