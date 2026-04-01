

# Class: AssessmentValue 


_Key-value pair representing a specific value produced by a quality assessment._





URI: [https://w3id.org/fga-wg/schema/top_level/AssessmentValue](https://w3id.org/fga-wg/schema/top_level/AssessmentValue)





```mermaid
 classDiagram
    class AssessmentValue
    click AssessmentValue href "../AssessmentValue/"
      AssessmentValue : key
        
      AssessmentValue : value
        
          
    
        
        
        AssessmentValue --> "1" Any : value
        click Any href "../Any/"
    

        
      
```




<!-- no inheritance hierarchy -->

## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [key](key.md) | 1 <br/> [String](String.md) | Key/name of the assessment value | direct |
| [value](value.md) | 1 <br/> [Any](Any.md)&nbsp;or&nbsp;<br />[String](String.md)&nbsp;or&nbsp;<br />[Integer](Integer.md)&nbsp;or&nbsp;<br />[Decimal](Decimal.md)&nbsp;or&nbsp;<br />[Boolean](Boolean.md) | Value corresponding to the assessment key | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [QualityAssessment](QualityAssessment.md) | [assessment_values](assessment_values.md) | any_of[range] | [AssessmentValue](AssessmentValue.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fga-wg/schema/top_level




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/fga-wg/schema/top_level/AssessmentValue |
| native | https://w3id.org/fga-wg/schema/top_level/AssessmentValue |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: AssessmentValue
description: Key-value pair representing a specific value produced by a quality assessment.
from_schema: https://w3id.org/fga-wg/schema/top_level
slots:
- key
- value

```
</details>

### Induced

<details>
```yaml
name: AssessmentValue
description: Key-value pair representing a specific value produced by a quality assessment.
from_schema: https://w3id.org/fga-wg/schema/top_level
attributes:
  key:
    name: key
    description: Key/name of the assessment value.
    examples:
    - value: nreads
    - value: nreads_in_peaks
    - value: frip
    from_schema: https://w3id.org/fga-wg/schema/top_level
    rank: 1000
    alias: key
    owner: AssessmentValue
    domain_of:
    - AssessmentValue
    range: string
    required: true
  value:
    name: value
    description: Value corresponding to the assessment key.
    examples:
    - object: 21018235
    - object: 6161851
    - object: 0.2931669095906483
    from_schema: https://w3id.org/fga-wg/schema/top_level
    rank: 1000
    alias: value
    owner: AssessmentValue
    domain_of:
    - AssessmentValue
    range: Any
    required: true
    any_of:
    - range: decimal
    - range: boolean
    - range: integer
    - range: string

```
</details>