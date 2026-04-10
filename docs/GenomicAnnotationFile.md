---
search:
  boost: 10.0
---

# Class: GenomicAnnotationFile 


_Information about a genomic annotation / track file. GenomicAnnotationFile is a specification of the File entity and inherits all the fields defined in File, in addition to the fields that are specific to GenomicAnnotationFile, as detailed here._



<div data-search-exclude markdown="1">



URI: [https://w3id.org/fga-wg/schema/top_level/GenomicAnnotationFile](https://w3id.org/fga-wg/schema/top_level/GenomicAnnotationFile)





```mermaid
 classDiagram
    class GenomicAnnotationFile
    click GenomicAnnotationFile href "../GenomicAnnotationFile/"
      File <|-- GenomicAnnotationFile
        click File href "../File/"
      
      GenomicAnnotationFile : access_methods
        
          
    
        
        
        GenomicAnnotationFile --> "1..*" AccessMethod : access_methods
        click AccessMethod href "../AccessMethod/"
    

        
      GenomicAnnotationFile : checksums
        
          
    
        
        
        GenomicAnnotationFile --> "1..*" Checksum : checksums
        click Checksum href "../Checksum/"
    

        
      GenomicAnnotationFile : created_time
        
      GenomicAnnotationFile : data_content
        
          
    
        
        
        GenomicAnnotationFile --> "1" OutputType : data_content
        click OutputType href "../OutputType/"
    

        
      GenomicAnnotationFile : drs_uri
        
      GenomicAnnotationFile : file_description
        
      GenomicAnnotationFile : file_external_id
        
      GenomicAnnotationFile : file_id
        
      GenomicAnnotationFile : file_input_sources
        
          
    
        
        
        GenomicAnnotationFile --> "1..*" InputSource : file_input_sources
        click InputSource href "../InputSource/"
    

        
      GenomicAnnotationFile : file_label
        
      GenomicAnnotationFile : file_name
        
      GenomicAnnotationFile : file_size
        
      GenomicAnnotationFile : file_type
        
          
    
        
        
        GenomicAnnotationFile --> "1" Term : file_type
        click Term href "../Term/"
    

        
      GenomicAnnotationFile : file_version
        
      GenomicAnnotationFile : filecollection_refs
        
      GenomicAnnotationFile : genome_assembly
        
          
    
        
        
        GenomicAnnotationFile --> "1" GenomeAssembly : genome_assembly
        click GenomeAssembly href "../GenomeAssembly/"
    

        
      GenomicAnnotationFile : genomic_annotation_digest
        
      GenomicAnnotationFile : mime_type
        
      GenomicAnnotationFile : quality_assessments
        
          
    
        
        
        GenomicAnnotationFile --> "*" QualityAssessment : quality_assessments
        click QualityAssessment href "../QualityAssessment/"
    

        
      GenomicAnnotationFile : run_provenance
        
      GenomicAnnotationFile : sequence_features
        
          
    
        
        
        GenomicAnnotationFile --> "1..*" Term : sequence_features
        click Term href "../Term/"
    

        
      GenomicAnnotationFile : track_geometry
        
          
    
        
        
        GenomicAnnotationFile --> "1" TrackGeometry : track_geometry
        click TrackGeometry href "../TrackGeometry/"
    

        
      GenomicAnnotationFile : updated_time
        
      
```





## Inheritance
* [File](File.md)
    * **GenomicAnnotationFile**


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [genomic_annotation_digest](genomic_annotation_digest.md) | 0..1 <br/> [Curie](Curie.md) | Content-derived digest for distributed identification of genomic annotation f... | direct |
| [genome_assembly](genome_assembly.md) | 1 <br/> [GenomeAssembly](GenomeAssembly.md) | Information about the genome assembly used to generate the genomic annotation... | direct |
| [track_geometry](track_geometry.md) | 1 <br/> [TrackGeometry](TrackGeometry.md) | Geometric properties of the sequence features in the genomic annotation file ... | direct |
| [sequence_features](sequence_features.md) | 1..* <br/> [Term](Term.md) | List of sequence features described by the genomic annotation file | direct |
| [file_external_id](file_external_id.md) | 0..1 <br/> [Curie](Curie.md) | External, globally unique identifier for the data file | [File](File.md) |
| [file_id](file_id.md) | 1 <br/> [Curie](Curie.md) | Internal identifier for the data file (unique within the metadata deposit) | [File](File.md) |
| [file_name](file_name.md) | 0..1 <br/> [String](String.md) | A string that can be used to name a data file | [File](File.md) |
| [file_label](file_label.md) | 1 <br/> [String](String.md) | A human-readable description of the data file, short enough to be used for li... | [File](File.md) |
| [file_description](file_description.md) | 0..1 <br/> [String](String.md) | A human readable description of the data file | [File](File.md) |
| [filecollection_refs](filecollection_refs.md) | 1..* <br/> [Curie](Curie.md) | Internal references to the FileCollection objects (within the deposit) that c... | [File](File.md) |
| [file_input_sources](file_input_sources.md) | 1..* <br/> [InputSource](InputSource.md) | External or internal references to data sources for the file, typically a dat... | [File](File.md) |
| [drs_uri](drs_uri.md) | 0..1 <br/> [Uri](Uri.md) | A drs:// hostname-based URI, as defined in the DRS documentation, that tells ... | [File](File.md) |
| [access_methods](access_methods.md) | 1..* <br/> [AccessMethod](AccessMethod.md) | The list of access methods that can be used to fetch the data file | [File](File.md) |
| [run_provenance](run_provenance.md) | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | Document detailing the provenance of the experiment or analysis run which pro... | [File](File.md) |
| [quality_assessments](quality_assessments.md) | * <br/> [QualityAssessment](QualityAssessment.md) | An array of QualityAssessment objects containing the main quality scores from... | [File](File.md) |
| [file_type](file_type.md) | 1 <br/> [Term](Term.md) | The file format of the data file | [File](File.md) |
| [mime_type](mime_type.md) | 0..1 <br/> [String](String.md) | A string providing the mime-type of the data file | [File](File.md) |
| [data_content](data_content.md) | 1 <br/> [OutputType](OutputType.md) | Classification describing the file's purpose or contents | [File](File.md) |
| [file_size](file_size.md) | 1 <br/> [Integer](Integer.md) | The file size in bytes | [File](File.md) |
| [created_time](created_time.md) | 1 <br/> [Datetime](Datetime.md) | Timestamp of content creation in RFC3339 | [File](File.md) |
| [updated_time](updated_time.md) | 0..1 <br/> [Datetime](Datetime.md) | Timestamp of content update in RFC3339, identical to created_time in systems ... | [File](File.md) |
| [file_version](file_version.md) | 0..1 <br/> [String](String.md) | A string representing a version | [File](File.md) |
| [checksums](checksums.md) | 1..* <br/> [Checksum](Checksum.md) | A list of checksums of the data file | [File](File.md) |















## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fga-wg/schema/top_level




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/fga-wg/schema/top_level/GenomicAnnotationFile |
| native | https://w3id.org/fga-wg/schema/top_level/GenomicAnnotationFile |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: GenomicAnnotationFile
description: Information about a genomic annotation / track file. GenomicAnnotationFile
  is a specification of the File entity and inherits all the fields defined in File,
  in addition to the fields that are specific to GenomicAnnotationFile, as detailed
  here.
from_schema: https://w3id.org/fga-wg/schema/top_level
is_a: File
slots:
- genomic_annotation_digest
- genome_assembly
- track_geometry
- sequence_features

```
</details>

### Induced

<details>
```yaml
name: GenomicAnnotationFile
description: Information about a genomic annotation / track file. GenomicAnnotationFile
  is a specification of the File entity and inherits all the fields defined in File,
  in addition to the fields that are specific to GenomicAnnotationFile, as detailed
  here.
from_schema: https://w3id.org/fga-wg/schema/top_level
is_a: File
attributes:
  genomic_annotation_digest:
    name: genomic_annotation_digest
    description: Content-derived digest for distributed identification of genomic
      annotation files. (This field is currently a placeholder, as an algorithm for
      generating such a digest is yet to be specified.).
    from_schema: https://w3id.org/fga-wg/schema/top_level
    rank: 1000
    owner: GenomicAnnotationFile
    domain_of:
    - GenomicAnnotationFile
    range: curie
  genome_assembly:
    name: genome_assembly
    description: Information about the genome assembly used to generate the genomic
      annotation file, consequently defining the genomic coordinate system for the
      annotation.
    examples:
    - value: ga4gh:SC.EiFob05aCWgVU_B_Ae0cypnQut3cxUP1
    from_schema: https://w3id.org/fga-wg/schema/top_level
    rank: 1000
    owner: GenomicAnnotationFile
    domain_of:
    - GenomicAnnotationFile
    range: GenomeAssembly
    required: true
  track_geometry:
    name: track_geometry
    description: Geometric properties of the sequence features in the genomic annotation
      file if considered as an one-dimensional genome browser track (also relevant
      for non-visual analyses).
    examples:
    - object:
        elements_circular: false
        elements_overlapping: false
        has_edges: false
        has_gaps: true
        has_lengths: true
        has_names: true
        has_strands: false
        has_values: true
        lengths_constant: false
        value_type: multiple
    from_schema: https://w3id.org/fga-wg/schema/top_level
    rank: 1000
    owner: GenomicAnnotationFile
    domain_of:
    - GenomicAnnotationFile
    range: TrackGeometry
    required: true
  sequence_features:
    name: sequence_features
    description: List of sequence features described by the genomic annotation file.
    examples:
    - object:
        id: SO:0001707
        label: H3K9Me3
    from_schema: https://w3id.org/fga-wg/schema/top_level
    rank: 1000
    owner: GenomicAnnotationFile
    domain_of:
    - GenomicAnnotationFile
    range: Term
    required: true
    multivalued: true
  file_external_id:
    name: file_external_id
    description: External, globally unique identifier for the data file.
    examples:
    - value: encode:ENCFF323LCS
    from_schema: https://w3id.org/fga-wg/schema/top_level
    rank: 1000
    owner: GenomicAnnotationFile
    domain_of:
    - File
    range: curie
  file_id:
    name: file_id
    description: 'Internal identifier for the data file (unique within the metadata
      deposit). '
    examples:
    - value: file:ENCFF323LCS
    from_schema: https://w3id.org/fga-wg/schema/top_level
    rank: 1000
    identifier: true
    owner: GenomicAnnotationFile
    domain_of:
    - File
    range: curie
    required: true
  file_name:
    name: file_name
    description: A string that can be used to name a data file. This string is made
      up of uppercase and lowercase letters, decimal digits, hypen, period, and underscore
      [A-Za-z0-9.-_]. See http://pubs.opengroup.org/onlinepubs/9699919799/basedefs/V1_chap03.html#tag_03_282
      [portable filenames].
    examples:
    - value: 87234.ENCODE.ENCBS004ENC.H3K9me3.peak_calls.bigBed
    from_schema: https://w3id.org/fga-wg/schema/top_level
    rank: 1000
    owner: GenomicAnnotationFile
    domain_of:
    - File
    range: string
  file_label:
    name: file_label
    description: A human-readable description of the data file, short enough to be
      used for listings within software user interfaces, tables, illustration legends,
      etc.
    examples:
    - value: H3K9me3 ChIP-seq replicated peaks, GRCh38, AG04450
    from_schema: https://w3id.org/fga-wg/schema/top_level
    rank: 1000
    owner: GenomicAnnotationFile
    domain_of:
    - File
    range: string
    required: true
    pattern: ^.{1,60}$
  file_description:
    name: file_description
    description: A human readable description of the data file.
    examples:
    - value: H3K9me3 ChIP-seq replicated peaks on human (hg38) AG04450 (Fibroblast
        derived cell line).
    from_schema: https://w3id.org/fga-wg/schema/top_level
    rank: 1000
    owner: GenomicAnnotationFile
    domain_of:
    - File
    range: string
  filecollection_refs:
    name: filecollection_refs
    description: Internal references to the FileCollection objects (within the deposit)
      that contains the data file, if any.
    examples:
    - value: collection:ihec_encode
    from_schema: https://w3id.org/fga-wg/schema/top_level
    rank: 1000
    owner: GenomicAnnotationFile
    domain_of:
    - File
    range: curie
    required: true
    multivalued: true
  file_input_sources:
    name: file_input_sources
    description: External or internal references to data sources for the file, typically
      a data collection or a process that has generated the file. Internal references
      should lead to FileCollection, File, Experiment, or Analysis objects.
    examples:
    - object:
        inputsource_ref: analysis:ENCAN718KHT
        qualified_relation: prov:wasGeneratedBy
        biological_replicate_labels:
        - '1'
        - '2'
        technical_replicate_labels:
        - '1_1'
        - '2_1'
    from_schema: https://w3id.org/fga-wg/schema/top_level
    rank: 1000
    owner: GenomicAnnotationFile
    domain_of:
    - File
    range: InputSource
    required: true
    multivalued: true
  drs_uri:
    name: drs_uri
    description: A drs:// hostname-based URI, as defined in the DRS documentation,
      that tells clients how to access this object. The intent of this field is to
      make DRS objects self-contained, and therefore easier for clients to store and
      pass around. For example, if you arrive at this DRS JSON by resolving a compact
      identifier-based DRS URI, the self_uri presents you with a hostname and properly
      encoded DRS ID for use in subsequent access endpoint calls.
    examples:
    - value: drs://drs.example.org/ENCFF323LCS
    from_schema: https://w3id.org/fga-wg/schema/top_level
    rank: 1000
    owner: GenomicAnnotationFile
    domain_of:
    - File
    range: uri
  access_methods:
    name: access_methods
    description: 'The list of access methods that can be used to fetch the data file. '
    examples:
    - object:
        access_method: https
        access_url:
          url: https://epigenomesportal.ca/tracks/ENCODE/hg38/87234.ENCODE.ENCBS004ENC.H3K9me3.peak_calls.bigBed
    - object:
        access_method: https
        access_url:
          url: https://www.encodeproject.org/files/ENCFF323LCS/@@download/ENCFF323LCS.bigBed
    - object:
        access_method: s3
        access_url:
          url: s3://encode-public/2016/11/13/efd4e74e-7875-4d13-9630-0085bc834f18/ENCFF323LCS.bigBed
    - object:
        access_method: https
        access_url:
          url: https://encode-public.s3.amazonaws.com/2016/11/13/efd4e74e-7875-4d13-9630-0085bc834f18/ENCFF323LCS.bigBed
    - object:
        access_method: https
        access_url:
          url: https://datasetencode.blob.core.windows.net/dataset/2016/11/13/efd4e74e-7875-4d13-9630-0085bc834f18/ENCFF323LCS.bigBed?sv=2019-10-10&si=prod&sr=c&sig=9qSQZo4ggrCNpybBExU8SypuUZV33igI11xw0P7rB3c%3D
    from_schema: https://w3id.org/fga-wg/schema/top_level
    rank: 1000
    owner: GenomicAnnotationFile
    domain_of:
    - File
    range: AccessMethod
    required: true
    multivalued: true
  run_provenance:
    name: run_provenance
    description: Document detailing the provenance of the experiment or analysis run
      which produced the file as one of its outputs. The provenance info should include
      software versions, parameter settings, etc.
    examples:
    - value: encode:ENCAN718KHT
    from_schema: https://w3id.org/fga-wg/schema/top_level
    rank: 1000
    owner: GenomicAnnotationFile
    domain_of:
    - File
    range: uriorcurie
  quality_assessments:
    name: quality_assessments
    description: An array of QualityAssessment objects containing the main quality
      scores from assessment techniques applied to the data file.
    examples:
    - object:
        assessment_method: histone-chipseq-quality-metrics
        assessment_values:
          nreads: 21018235
          nreads_in_peaks: 6161851
          frip: 0.2931669095906483
        assessment_details_url: https://www.encodeproject.org/histone-chipseq-quality-metrics/70ae08dc-3edc-437f-a0a5-378c72e6269b/
    from_schema: https://w3id.org/fga-wg/schema/top_level
    rank: 1000
    owner: GenomicAnnotationFile
    domain_of:
    - File
    range: QualityAssessment
    multivalued: true
  file_type:
    name: file_type
    description: The file format of the data file.
    examples:
    - object:
        id: edam:format_3004
        label: bigBed
    from_schema: https://w3id.org/fga-wg/schema/top_level
    rank: 1000
    owner: GenomicAnnotationFile
    domain_of:
    - File
    range: Term
    required: true
  mime_type:
    name: mime_type
    description: A string providing the mime-type of the data file.
    examples:
    - value: application/octet-stream
    from_schema: https://w3id.org/fga-wg/schema/top_level
    rank: 1000
    owner: GenomicAnnotationFile
    domain_of:
    - File
    range: string
  data_content:
    name: data_content
    description: Classification describing the file's purpose or contents.
    examples:
    - value: replicated peaks
    from_schema: https://w3id.org/fga-wg/schema/top_level
    rank: 1000
    owner: GenomicAnnotationFile
    domain_of:
    - File
    range: OutputType
    required: true
  file_size:
    name: file_size
    description: The file size in bytes.
    examples:
    - value: '5359719'
    from_schema: https://w3id.org/fga-wg/schema/top_level
    rank: 1000
    owner: GenomicAnnotationFile
    domain_of:
    - File
    range: integer
    required: true
  created_time:
    name: created_time
    description: Timestamp of content creation in RFC3339. (This is the creation time
      of the underlying content, not of the JSON object.).
    examples:
    - value: '2016-11-13T17:42:04.385801+00:00'
    from_schema: https://w3id.org/fga-wg/schema/top_level
    rank: 1000
    owner: GenomicAnnotationFile
    domain_of:
    - File
    range: datetime
    required: true
  updated_time:
    name: updated_time
    description: Timestamp of content update in RFC3339, identical to created_time
      in systems that do not support updates. (This is the update time of the underlying
      content, not of the JSON object.).
    examples:
    - value: '2016-11-13T17:42:04.385801+00:00'
    from_schema: https://w3id.org/fga-wg/schema/top_level
    rank: 1000
    owner: GenomicAnnotationFile
    domain_of:
    - File
    range: datetime
  file_version:
    name: file_version
    description: A string representing a version. (Some systems may use checksum,
      a RFC3339 timestamp, or an incrementing version number.).
    examples:
    - value: efd4e74e-7875-4d13-9630-0085bc834f18
    from_schema: https://w3id.org/fga-wg/schema/top_level
    rank: 1000
    owner: GenomicAnnotationFile
    domain_of:
    - File
    range: string
  checksums:
    name: checksums
    description: A list of checksums of the data file. At least one checksum must
      be provided. For blobs, the checksum is computed over the bytes in the blob.
    examples:
    - object:
        checksum: 535bc9628a1c5e5215226f9996e4eaca
        checksum_type: md5
    from_schema: https://w3id.org/fga-wg/schema/top_level
    rank: 1000
    owner: GenomicAnnotationFile
    domain_of:
    - File
    range: Checksum
    required: true
    multivalued: true

```
</details></div>