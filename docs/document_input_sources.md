---
search:
  boost: 5.0
---

# Slot: document_input_sources 


_References to other input sources from which this entire metadata document was derived, or possibly including DOIs of other metadata documents used as source._



<div data-search-exclude markdown="1">



URI: [https://w3id.org/fga-wg/schema/top_level/document_input_sources](https://w3id.org/fga-wg/schema/top_level/document_input_sources)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Document](Document.md) | Information about a document containing metadata about a set of genome annota... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [InputSource](InputSource.md) |
| Domain Of | [Document](Document.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |









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
| self | https://w3id.org/fga-wg/schema/top_level/document_input_sources |
| native | https://w3id.org/fga-wg/schema/top_level/document_input_sources |




## LinkML Source

<details>
```yaml
name: document_input_sources
description: References to other input sources from which this entire metadata document
  was derived, or possibly including DOIs of other metadata documents used as source.
examples:
- object:
    inputsource_external_ref: https://epigenomesportal.ca/ihec/
    qualified_relation: prov:wasDerivedFrom
from_schema: https://w3id.org/fga-wg/schema/top_level
rank: 1000
domain_of:
- Document
range: InputSource
multivalued: true

```
</details></div>