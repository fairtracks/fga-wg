---
search:
  boost: 2.0
---# Enum: DataTypes 




_Types of data values associated with sequence features or edges._



<div data-search-exclude markdown="1">

URI: [https://w3id.org/fga-wg/schema/top_level/DataTypes](https://w3id.org/fga-wg/schema/top_level/DataTypes)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| integer | None | Integer numeric values |
| decimal | None | Decimal numeric values |
| boolean | None | Boolean values (true/false) |
| string | None | Text string values |
| multiple | None | Multiple types of values are associated (e |




## Slots

| Name | Description |
| ---  | --- |
| [value_type](value_type.md) | The type of values associated with the sequence features, if any |
| [edge_weight_type](edge_weight_type.md) | The type of values associated with the edges |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fga-wg/schema/top_level






## LinkML Source

<details>
```yaml
name: DataTypes
description: Types of data values associated with sequence features or edges.
from_schema: https://w3id.org/fga-wg/schema/top_level
rank: 1000
permissible_values:
  integer:
    text: integer
    description: Integer numeric values.
  decimal:
    text: decimal
    description: Decimal numeric values.
  boolean:
    text: boolean
    description: Boolean values (true/false).
  string:
    text: string
    description: Text string values.
  multiple:
    text: multiple
    description: Multiple types of values are associated (e.g. both integer and string).

```
</details>

</div>