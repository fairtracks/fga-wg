---
search:
  boost: 5.0
---

# Slot: study_abstract 


_Abstract of the study._



<div data-search-exclude markdown="1">



URI: [https://w3id.org/fga-wg/schema/top_level/study_abstract](https://w3id.org/fga-wg/schema/top_level/study_abstract)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Study](Study.md) | A scientific study, i |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Study](Study.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |









## Examples

| Value |
| --- |
| ENCODE comprises thousands of functional genomics datasets, and the encyclopedia covers hundreds of cell types, providing a universal annotation for genome interpretation. However, for particular applications, it may be advantageous to use a customized annotation. Here, we develop such a custom annotation by leveraging advanced assays, such as eCLIP, Hi-C, and whole-genome STARR-seq on a number of data-rich ENCODE cell types. A key aspect of this annotation is comprehensive and experimentally derived networks of both transcription factors and RNA-binding proteins (TFs and RBPs). Cancer, a disease of system-wide dysregulation, is an ideal application for such a network-based annotation. Specifically, for cancer-associated cell types, we put regulators into hierarchies and measure their network change (rewiring) during oncogenesis. We also extensively survey TF-RBP crosstalk, highlighting how SUB1, a previously uncharacterized RBP, drives aberrant tumor expression and amplifies the effect of MYC, a well-known oncogenic TF. Furthermore, we show how our annotation allows us to place oncogenic transformations in the context of a broad cell space; here, many normal-to-tumor transitions move towards a stem-like state, while oncogene knockdowns show an opposing trend. Finally, we organize the resource into a coherent workflow to prioritize key elements and variants, in addition to regulators. We showcase the application of this prioritization to somatic burdening, cancer differential expression and GWAS. Targeted validations of the prioritized regulators, elements and variants using siRNA knockdowns, CRISPR-based editing, and luciferase assays demonstrate the value of the ENCODE resource. |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fga-wg/schema/top_level




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/fga-wg/schema/top_level/study_abstract |
| native | https://w3id.org/fga-wg/schema/top_level/study_abstract |




## LinkML Source

<details>
```yaml
name: study_abstract
description: Abstract of the study.
examples:
- value: ENCODE comprises thousands of functional genomics datasets, and the encyclopedia
    covers hundreds of cell types, providing a universal annotation for genome interpretation.
    However, for particular applications, it may be advantageous to use a customized
    annotation. Here, we develop such a custom annotation by leveraging advanced assays,
    such as eCLIP, Hi-C, and whole-genome STARR-seq on a number of data-rich ENCODE
    cell types. A key aspect of this annotation is comprehensive and experimentally
    derived networks of both transcription factors and RNA-binding proteins (TFs and
    RBPs). Cancer, a disease of system-wide dysregulation, is an ideal application
    for such a network-based annotation. Specifically, for cancer-associated cell
    types, we put regulators into hierarchies and measure their network change (rewiring)
    during oncogenesis. We also extensively survey TF-RBP crosstalk, highlighting
    how SUB1, a previously uncharacterized RBP, drives aberrant tumor expression and
    amplifies the effect of MYC, a well-known oncogenic TF. Furthermore, we show how
    our annotation allows us to place oncogenic transformations in the context of
    a broad cell space; here, many normal-to-tumor transitions move towards a stem-like
    state, while oncogene knockdowns show an opposing trend. Finally, we organize
    the resource into a coherent workflow to prioritize key elements and variants,
    in addition to regulators. We showcase the application of this prioritization
    to somatic burdening, cancer differential expression and GWAS. Targeted validations
    of the prioritized regulators, elements and variants using siRNA knockdowns, CRISPR-based
    editing, and luciferase assays demonstrate the value of the ENCODE resource.
from_schema: https://w3id.org/fga-wg/schema/top_level
rank: 1000
domain_of:
- Study
range: string

```
</details></div>