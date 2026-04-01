

# Slot: checksum_type 


_The digest method used to create the checksum. The value (e.g. `sha-256`) SHOULD be listed as `Hash Name String` in the https://www.iana.org/assignments/named-information/named-information.xhtml#hash-alg [IANA Named Information Hash Algorithm Registry]. Other values MAY be used, as long as implementors are aware of the issues discussed in https://tools.ietf.org/html/rfc6920#section-9.4 [RFC6920]. GA4GH may provide more explicit guidance for use of non-IANA-registered algorithms in the future. Until then, if implementors do choose such an algorithm (e.g. because it's implemented by their storage provider), they SHOULD use an existing standard `type` value such as `md5`, `etag`, `crc32c`, `trunc512`, or `sha1`._





URI: [https://w3id.org/fga-wg/schema/top_level/checksum_type](https://w3id.org/fga-wg/schema/top_level/checksum_type)
Alias: checksum_type

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Checksum](Checksum.md) | A checksum of a File object (orig: DrsObject) |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Checksum](Checksum.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |









## Examples

| Value |
| --- |
| md5 |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fga-wg/schema/top_level




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/fga-wg/schema/top_level/checksum_type |
| native | https://w3id.org/fga-wg/schema/top_level/checksum_type |




## LinkML Source

<details>
```yaml
name: checksum_type
description: The digest method used to create the checksum. The value (e.g. `sha-256`)
  SHOULD be listed as `Hash Name String` in the https://www.iana.org/assignments/named-information/named-information.xhtml#hash-alg
  [IANA Named Information Hash Algorithm Registry]. Other values MAY be used, as long
  as implementors are aware of the issues discussed in https://tools.ietf.org/html/rfc6920#section-9.4
  [RFC6920]. GA4GH may provide more explicit guidance for use of non-IANA-registered
  algorithms in the future. Until then, if implementors do choose such an algorithm
  (e.g. because it's implemented by their storage provider), they SHOULD use an existing
  standard `type` value such as `md5`, `etag`, `crc32c`, `trunc512`, or `sha1`.
examples:
- value: md5
from_schema: https://w3id.org/fga-wg/schema/top_level
rank: 1000
alias: checksum_type
domain_of:
- Checksum
range: string
required: true

```
</details>