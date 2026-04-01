

# Slot: drs_uri 


_A drs:// hostname-based URI, as defined in the DRS documentation, that tells clients how to access this object. The intent of this field is to make DRS objects self-contained, and therefore easier for clients to store and pass around. For example, if you arrive at this DRS JSON by resolving a compact identifier-based DRS URI, the self_uri presents you with a hostname and properly encoded DRS ID for use in subsequent access endpoint calls._





URI: [https://w3id.org/fga-wg/schema/top_level/drs_uri](https://w3id.org/fga-wg/schema/top_level/drs_uri)
Alias: drs_uri

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [File](File.md) | General information about a particular data file |  no  |
| [GenomicAnnotationFile](GenomicAnnotationFile.md) | Information about a genomic annotation / track file |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Uri](Uri.md) |
| Domain Of | [File](File.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |









## Examples

| Value |
| --- |
| drs://drs.example.org/ENCFF323LCS |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fga-wg/schema/top_level




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/fga-wg/schema/top_level/drs_uri |
| native | https://w3id.org/fga-wg/schema/top_level/drs_uri |




## LinkML Source

<details>
```yaml
name: drs_uri
description: A drs:// hostname-based URI, as defined in the DRS documentation, that
  tells clients how to access this object. The intent of this field is to make DRS
  objects self-contained, and therefore easier for clients to store and pass around.
  For example, if you arrive at this DRS JSON by resolving a compact identifier-based
  DRS URI, the self_uri presents you with a hostname and properly encoded DRS ID for
  use in subsequent access endpoint calls.
examples:
- value: drs://drs.example.org/ENCFF323LCS
from_schema: https://w3id.org/fga-wg/schema/top_level
rank: 1000
alias: drs_uri
domain_of:
- File
range: uri

```
</details>