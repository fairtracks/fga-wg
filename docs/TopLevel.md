---
search:
  boost: 10.0
---

# Class: TopLevel 


_A document of harmonised metadata for a set of genome annotation files. Metadata has been harmonised in line with the "FAIRification of Genomic Annotations" data model. This is the top-level class to be used as root for the metadata document._



<div data-search-exclude markdown="1">



URI: [https://w3id.org/fga-wg/schema/top_level/TopLevel](https://w3id.org/fga-wg/schema/top_level/TopLevel)





```mermaid
 classDiagram
    class TopLevel
    click TopLevel href "../TopLevel/"
      TopLevel : analyses
        
          
    
        
        
        TopLevel --> "*" Analysis : analyses
        click Analysis href "../Analysis/"
    

        
      TopLevel : document
        
          
    
        
        
        TopLevel --> "1" Document : document
        click Document href "../Document/"
    

        
      TopLevel : donors
        
          
    
        
        
        TopLevel --> "*" Donor : donors
        click Donor href "../Donor/"
    

        
      TopLevel : experiments
        
          
    
        
        
        TopLevel --> "*" Experiment : experiments
        click Experiment href "../Experiment/"
    

        
      TopLevel : file_collections
        
          
    
        
        
        TopLevel --> "*" FileCollection : file_collections
        click FileCollection href "../FileCollection/"
    

        
      TopLevel : files
        
          
    
        
        
        TopLevel --> "*" File : files
        click File href "../File/"
    

        
      TopLevel : samples
        
          
    
        
        
        TopLevel --> "*" Sample : samples
        click Sample href "../Sample/"
    

        
      TopLevel : studies
        
          
    
        
        
        TopLevel --> "*" Study : studies
        click Study href "../Study/"
    

        
      
```



## Example

<details>
<summary>Example JSON</summary>

```json
{
  "document": {
    "document_deposit": {
      "deposit_first_created": "2025-07-01T12:36:00Z",
      "deposit_id": "doi:10.1234/zenodo.12345678",
      "deposit_last_changed": "2025-07-01T12:36:00Z",
      "deposit_versioned_id": "doi:10.1234/zenodo.12345679"
    },
    "document_description": "The metadata contents of the International Human Epigenome Consortium (IHEC) data portal, harmonised to follow the metadata model developed by the \"FAIRification of Genomic Annotations WG\" in the Research Data Alliance (RDA), enhanced with metadata from original sources.",
    "document_input_sources": [
      {
        "inputsource_external_ref": "https://epigenomesportal.ca/ihec/",
        "qualified_relation": "prov:wasDerivedFrom"
      }
    ],
    "document_label": "IHEC data portal metadata, harmonised to the FGA-WG model.",
    "document_ontology_versions": [
      {
        "namespace": "edam",
        "ontology_url": "http://edamontology.org/EDAM.owl",
        "versioned_ontology_url": "http://edamontology.org/EDAM_1.21.owl"
      },
      {
        "namespace": "cl",
        "ontology_url": "http://purl.obolibrary.org/obo/cl.owl",
        "versioned_ontology_url": "http://purl.obolibrary.org/obo/cl/releases/2020-05-21/cl.owl"
      },
      {
        "namespace": "efo",
        "ontology_url": "http://www.ebi.ac.uk/efo/efo.owl",
        "versioned_ontology_url": "http://www.ebi.ac.uk/efo/releases/v3.21.0/efo.owl"
      },
      {
        "namespace": "ncit",
        "ontology_url": "http://purl.obolibrary.org/obo/ncit.owl",
        "versioned_ontology_url": "http://purl.obolibrary.org/obo/ncit/releases/2020-07-17/ncit.owl"
      },
      {
        "namespace": "obi",
        "ontology_url": "http://purl.obolibrary.org/obo/obi.owl",
        "versioned_ontology_url": "http://purl.obolibrary.org/obo/obi/2020-04-23/obi.owl"
      },
      {
        "namespace": "so",
        "ontology_url": "http://purl.obolibrary.org/obo/so.owl",
        "versioned_ontology_url": "http://purl.obolibrary.org/obo/so/2020-08-20/so.owl"
      },
      {
        "namespace": "uberon",
        "ontology_url": "http://purl.obolibrary.org/obo/uberon.owl",
        "versioned_ontology_url": "http://purl.obolibrary.org/obo/uberon/releases/2020-06-30/uberon.owl"
      }
    ]
  },
  "analyses": [
    {
      "analysis_description": "ENCODE3 ChIP-seq pipeline on GRCH38 with replicated peak calling using MACS.",
      "analysis_external_id": "encode:ENCAN718KHT",
      "analysis_id": "analysis:ENCAN718KHT",
      "analysis_input_sources": [
        {
          "biological_replicate_labels": [
            "1",
            "2"
          ],
          "inputsource_ref": "experiment:ENCSR000DPJ",
          "qualified_relation": "prov:wasInformedBy",
          "technical_replicate_labels": [
            "1_1",
            "2_1"
          ]
        },
        {
          "biological_replicate_labels": [
            "1",
            "2"
          ],
          "date_of_retrieval": "2016-04-19",
          "inputsource_external_ref": "https://www.encodeproject.org/files/GRCh38_no_alt_analysis_set_GCA_000001405.15",
          "qualified_relation": "https://bioschemas.org/FormalParameter",
          "technical_replicate_labels": [
            "1_1",
            "2_1"
          ]
        }
      ],
      "analysis_label": "ENCODE3 ChIP-seq pipeline, GRCH38, replicated peak calling",
      "analysis_main_tool": "biotools:macs",
      "analysis_main_tool_version": "2.10",
      "analysis_protocol": "https://www.encodeproject.org/documents/7009beb8-340b-4e71-b9db-53bb020c7fe2/@@download/attachment/ChIP-seq_pipeline_overview.pdf",
      "analysis_study_ref": "study:S-EPMC7391744",
      "analysis_type": {
        "id": "edam:operation_3222",
        "label": "Peak calling"
      },
      "analysis_workflow": "encode:ENCPL272XAE"
    }
  ],
  "donors": [
    {
      "donor_external_id": "biosamples:SAMN04284578",
      "donor_id": "donor:ENCDO001AAA",
      "sex": {
        "id": "CARO:0000027",
        "label": "male organism"
      },
      "species_taxon": {
        "id": "NCBITaxon:9606",
        "label": "Homo sapiens"
      }
    }
  ],
  "experiments": [
    {
      "antibody_target": {
        "id": "SO:0001707",
        "label": "H3K9Me3"
      },
      "assay_type": {
        "id": "obi:OBI_0000716",
        "label": "ChIP-seq assay"
      },
      "biological_processes": [
        {
          "id": "GO:0140999",
          "label": "histone H3K4 trimethyltransferase activity"
        }
      ],
      "design_description": "https://www.encodeproject.org/documents/92cd1386-ccad-450a-b5a6-ad49983e7e3f/@@download/attachment/wgEncodeUwHistone.release5.html.pdf",
      "experiment_external_id": "encode:ENCSR000DPJ",
      "experiment_id": "experiment:ENCSR000DPJ",
      "experiment_label": "H3K9me3 ChIP-seq on human AG04450",
      "experiment_samples": [
        {
          "biological_replicate_labels": [
            "1",
            "2"
          ],
          "inputsource_ref": "sample:ENCBS004ENC",
          "qualified_relation": "prov:used",
          "technical_replicate_labels": [
            "1_1",
            "2_1"
          ]
        }
      ],
      "experiment_study_ref": "study:E-GEOD-35583",
      "instrument": {
        "id": "obi:OBI_0002128",
        "label": "Illumina Genome Analyzer"
      },
      "library_layout": {
        "id": "obi:OBI_0000736",
        "label": "single fragment library"
      },
      "molecule_type": {
        "id": "SO:0000991",
        "label": "genomic_DNA"
      }
    }
  ],
  "file_collections": [
    {
      "deposit_versioned_ref": "doi:10.1234/zenodo.12345679",
      "filecollection_contact": {
        "contact_id": "bioproject:PRJNA234466",
        "email": "info@ihec-epigenomes.org",
        "name": "International Human Epigenome Consortium"
      },
      "filecollection_description": "ENCODE dataset in the International Human Epigenome Consortium (IHEC) data portal, enhanced with metadata from the ENCODE data portal.",
      "filecollection_id": "filecollection:ihec_encode",
      "filecollection_input_sources": [
        {
          "inputsource_external_ref": "https://epigenomesportal.ca/ihec/grid.html?build=2020-10&assembly=4&institutions=4",
          "qualified_relation": "prov:wasDerivedFrom",
          "version": "2020-10"
        },
        {
          "inputsource_external_ref": "https://www.encodeproject.org",
          "qualified_relation": "prov:hadPrimarySource"
        }
      ],
      "filecollection_label": "IHEC data portal: ENCODE dataset"
    }
  ],
  "files": [
    {
      "access_methods": [
        {
          "access_method": "https",
          "access_url": {
            "url": "https://epigenomesportal.ca/tracks/ENCODE/hg38/87234.ENCODE.ENCBS004ENC.H3K9me3.peak_calls.bigBed"
          }
        },
        {
          "access_method": "https",
          "access_url": {
            "url": "https://www.encodeproject.org/files/ENCFF323LCS/@@download/ENCFF323LCS.bigBed"
          }
        },
        {
          "access_method": "s3",
          "access_url": {
            "url": "s3://encode-public/2016/11/13/efd4e74e-7875-4d13-9630-0085bc834f18/ENCFF323LCS.bigBed"
          }
        },
        {
          "access_method": "https",
          "access_url": {
            "url": "https://encode-public.s3.amazonaws.com/2016/11/13/efd4e74e-7875-4d13-9630-0085bc834f18/ENCFF323LCS.bigBed"
          }
        },
        {
          "access_method": "https",
          "access_url": {
            "url": "https://datasetencode.blob.core.windows.net/dataset/2016/11/13/efd4e74e-7875-4d13-9630-0085bc834f18/ENCFF323LCS.bigBed?sv=2019-10-10&si=prod&sr=c&sig=9qSQZo4ggrCNpybBExU8SypuUZV33igI11xw0P7rB3c%3D"
          }
        }
      ],
      "checksums": [
        {
          "checksum": "535bc9628a1c5e5215226f9996e4eaca",
          "checksum_type": "md5"
        }
      ],
      "created_time": "2016-11-13T17:42:04.385801+00:00",
      "data_content": "replicated peaks",
      "drs_uri": "drs://drs.example.org/ENCFF323LCS",
      "file_description": "H3K9me3 ChIP-seq replicated peaks on human (hg38) AG04450 (Fibroblast derived cell line).",
      "file_external_id": "encode:ENCFF323LCS",
      "file_id": "file:ENCFF323LCS",
      "file_input_sources": [
        {
          "biological_replicate_labels": [
            "1",
            "2"
          ],
          "inputsource_ref": "analysis:ENCAN718KHT",
          "qualified_relation": "prov:wasGeneratedBy",
          "technical_replicate_labels": [
            "1_1",
            "2_1"
          ]
        }
      ],
      "file_label": "H3K9me3 ChIP-seq replicated peaks, GRCh38, AG04450",
      "file_name": "87234.ENCODE.ENCBS004ENC.H3K9me3.peak_calls.bigBed",
      "file_size": 5359719,
      "file_type": {
        "id": "edam:format_3004",
        "label": "bigBed"
      },
      "file_version": "efd4e74e-7875-4d13-9630-0085bc834f18",
      "filecollection_refs": [
        "collection:ihec_encode"
      ],
      "genome_assembly": "ga4gh:SC.EiFob05aCWgVU_B_Ae0cypnQut3cxUP1",
      "mime_type": "application/octet-stream",
      "quality_assessments": [
        {
          "assessment_details_url": "https://www.encodeproject.org/histone-chipseq-quality-metrics/70ae08dc-3edc-437f-a0a5-378c72e6269b/",
          "assessment_method": "histone-chipseq-quality-metrics",
          "assessment_values": {
            "frip": 0.2931669095906483,
            "nreads": 21018235,
            "nreads_in_peaks": 6161851
          }
        }
      ],
      "run_provenance": "encode:ENCAN718KHT",
      "sequence_features": [
        {
          "id": "SO:0001707",
          "label": "H3K9Me3"
        }
      ],
      "track_geometry": {
        "elements_circular": false,
        "elements_overlapping": false,
        "has_edges": false,
        "has_gaps": true,
        "has_lengths": true,
        "has_names": true,
        "has_strands": false,
        "has_values": true,
        "lengths_constant": false,
        "value_type": "multiple"
      },
      "updated_time": "2016-11-13T17:42:04.385801+00:00"
    }
  ],
  "samples": [
    {
      "biospecimen_classification": "cell line",
      "cell_line": {
        "id": "CLO:0034832",
        "label": "AG04450 cell"
      },
      "donor_age": "W12",
      "donor_clinical_information": "apparently healthy",
      "donor_development_stage": {
        "id": "UBERON:0000323",
        "label": "late embryo"
      },
      "donor_organism_ref": "donor:ENCDO001AAA",
      "organism_tissue": {
        "id": "UBERON:0002048",
        "label": "lung"
      },
      "other_biospecimen": [
        {
          "id": "UBERON:0002384",
          "label": "connective tissue"
        },
        {
          "id": "CL:0002320",
          "label": "connective tissue cell"
        },
        {
          "id": "CL:0000057",
          "label": "fibroblast"
        },
        {
          "id": "UBERON:0000925",
          "label": "endoterm"
        },
        {
          "id": "UBERON:0001004",
          "label": "respiratory system"
        }
      ],
      "phenotype": {
        "id": "PATO:0000461",
        "label": "normal"
      },
      "sample_description": "Homo sapiens AG04450 cell line",
      "sample_external_id": "encode:ENCBS004ENC",
      "sample_id": "sample:ENCBS004ENC",
      "sample_label": "Homo sapiens AG04450 cell line",
      "sampling_protocol": "https://www.encodeproject.org/documents/3ed29dac-da67-47be-91b0-c9cad6a1b791/@@download/attachment/AG04450_Stam_protocol.pdf"
    }
  ],
  "studies": [
    {
      "project_external_ref": "bioproject:PRJNA63441",
      "publications": [
        "https://doi.org/10.1038/s41467-020-14743-w"
      ],
      "study_abstract": "ENCODE comprises thousands of functional genomics datasets, and the encyclopedia covers hundreds of cell types, providing a universal annotation for genome interpretation. However, for particular applications, it may be advantageous to use a customized annotation. Here, we develop such a custom annotation by leveraging advanced assays, such as eCLIP, Hi-C, and whole-genome STARR-seq on a number of data-rich ENCODE cell types. A key aspect of this annotation is comprehensive and experimentally derived networks of both transcription factors and RNA-binding proteins (TFs and RBPs). Cancer, a disease of system-wide dysregulation, is an ideal application for such a network-based annotation. Specifically, for cancer-associated cell types, we put regulators into hierarchies and measure their network change (rewiring) during oncogenesis. We also extensively survey TF-RBP crosstalk, highlighting how SUB1, a previously uncharacterized RBP, drives aberrant tumor expression and amplifies the effect of MYC, a well-known oncogenic TF. Furthermore, we show how our annotation allows us to place oncogenic transformations in the context of a broad cell space; here, many normal-to-tumor transitions move towards a stem-like state, while oncogene knockdowns show an opposing trend. Finally, we organize the resource into a coherent workflow to prioritize key elements and variants, in addition to regulators. We showcase the application of this prioritization to somatic burdening, cancer differential expression and GWAS. Targeted validations of the prioritized regulators, elements and variants using siRNA knockdowns, CRISPR-based editing, and luciferase assays demonstrate the value of the ENCODE resource.",
      "study_contact": {
        "contact_id": "orcid:0000-0002-9746-3719",
        "email": "mark@gersteinlab.org",
        "name": "Mark Gerstein"
      },
      "study_external_id": "biostudies:S-EPMC7391744",
      "study_id": "study:S-EPMC7391744",
      "study_title": "An integrative ENCODE resource for cancer genomics"
    }
  ]
}
```
</details>



<!-- no inheritance hierarchy -->

## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [document](document.md) | 1 <br/> [Document](Document.md) | Information about this document containing harmonised metadata about a set of... | direct |
| [donors](donors.md) | * <br/> [Donor](Donor.md) | Information about the donors or complete organisms from which the samples wer... | direct |
| [experiments](experiments.md) | * <br/> [Experiment](Experiment.md) | Information about sequencing experiments that have been carried out to genera... | direct |
| [files](files.md) | * <br/> [File](File.md) | Information about particular genome annotation (and other relevant) files | direct |
| [file_collections](file_collections.md) | * <br/> [FileCollection](FileCollection.md) | Information about collections of files contained in this dataset, each collec... | direct |
| [analyses](analyses.md) | * <br/> [Analysis](Analysis.md) | Information about computational processing and analyses that have been carrie... | direct |
| [samples](samples.md) | * <br/> [Sample](Sample.md) | Information about the biospecimens/samples used as raw material for lab exper... | direct |
| [studies](studies.md) | * <br/> [Study](Study.md) | The scientific studies, i | direct |















## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fga-wg/schema/top_level




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/fga-wg/schema/top_level/TopLevel |
| native | https://w3id.org/fga-wg/schema/top_level/TopLevel |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: TopLevel
description: A document of harmonised metadata for a set of genome annotation files.
  Metadata has been harmonised in line with the "FAIRification of Genomic Annotations"
  data model. This is the top-level class to be used as root for the metadata document.
from_schema: https://w3id.org/fga-wg/schema/top_level
slots:
- document
- donors
- experiments
- files
- file_collections
- analyses
- samples
- studies

```
</details>

### Induced

<details>
```yaml
name: TopLevel
description: A document of harmonised metadata for a set of genome annotation files.
  Metadata has been harmonised in line with the "FAIRification of Genomic Annotations"
  data model. This is the top-level class to be used as root for the metadata document.
from_schema: https://w3id.org/fga-wg/schema/top_level
attributes:
  document:
    name: document
    description: Information about this document containing harmonised metadata about
      a set of genome annotation files. This includes self-referential identifiers
      and versioning of public deposits of the document.
    from_schema: https://w3id.org/fga-wg/schema/top_level
    rank: 1000
    owner: TopLevel
    domain_of:
    - TopLevel
    range: Document
    required: true
    inlined: true
  donors:
    name: donors
    description: Information about the donors or complete organisms from which the
      samples were taken.
    from_schema: https://w3id.org/fga-wg/schema/top_level
    rank: 1000
    owner: TopLevel
    domain_of:
    - TopLevel
    range: Donor
    multivalued: true
    inlined: true
    inlined_as_list: true
  experiments:
    name: experiments
    description: Information about sequencing experiments that have been carried out
      to generate the files.
    from_schema: https://w3id.org/fga-wg/schema/top_level
    rank: 1000
    owner: TopLevel
    domain_of:
    - TopLevel
    range: Experiment
    multivalued: true
    inlined: true
    inlined_as_list: true
  files:
    name: files
    description: Information about particular genome annotation (and other relevant)
      files.
    from_schema: https://w3id.org/fga-wg/schema/top_level
    rank: 1000
    owner: TopLevel
    domain_of:
    - TopLevel
    range: File
    multivalued: true
    inlined: true
    inlined_as_list: true
  file_collections:
    name: file_collections
    description: Information about collections of files contained in this dataset,
      each collection defined according to some selection criteria.
    from_schema: https://w3id.org/fga-wg/schema/top_level
    rank: 1000
    owner: TopLevel
    domain_of:
    - TopLevel
    range: FileCollection
    multivalued: true
    inlined: true
    inlined_as_list: true
  analyses:
    name: analyses
    description: Information about computational processing and analyses that have
      been carried out to generate the files.
    from_schema: https://w3id.org/fga-wg/schema/top_level
    rank: 1000
    owner: TopLevel
    domain_of:
    - TopLevel
    range: Analysis
    multivalued: true
    inlined: true
    inlined_as_list: true
  samples:
    name: samples
    description: Information about the biospecimens/samples used as raw material for
      lab experiments.
    from_schema: https://w3id.org/fga-wg/schema/top_level
    rank: 1000
    owner: TopLevel
    domain_of:
    - TopLevel
    range: Sample
    multivalued: true
    inlined: true
    inlined_as_list: true
  studies:
    name: studies
    description: The scientific studies, i.e. units of research, within which experiments
      and/or analyses have been carried out.
    from_schema: https://w3id.org/fga-wg/schema/top_level
    rank: 1000
    owner: TopLevel
    domain_of:
    - TopLevel
    range: Study
    multivalued: true
    inlined: true
    inlined_as_list: true

```
</details></div>