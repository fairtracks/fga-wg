

# Slot: checksums 


_A list of checksums of the data file. At least one checksum must be provided. For blobs, the checksum is computed over the bytes in the blob._





URI: [https://w3id.org/fga-wg/schema/top_level/checksums](https://w3id.org/fga-wg/schema/top_level/checksums)
Alias: checksums

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
| Range | [Checksum](Checksum.md) |
| Domain Of | [File](File.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
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
| self | https://w3id.org/fga-wg/schema/top_level/checksums |
| native | https://w3id.org/fga-wg/schema/top_level/checksums |




## LinkML Source

<details>
```yaml
name: checksums
description: A list of checksums of the data file. At least one checksum must be provided.
  For blobs, the checksum is computed over the bytes in the blob.
examples:
- object:
    checksum: 535bc9628a1c5e5215226f9996e4eaca
    type: md5
from_schema: https://w3id.org/fga-wg/schema/top_level
rank: 1000
alias: checksums
domain_of:
- File
range: Checksum
required: true
multivalued: true

```
</details>