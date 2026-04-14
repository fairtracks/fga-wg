---
search:
  boost: 10.0
---

# Class: File 


_General information about a particular data file. Most fields (marked with an asterix*) are copied from the GA4GH DRS DrsObject model (https://ga4gh.github.io/data-repository-service-schemas/preview/release/drs-1.4.0/docs/#tag/DrsObjectModel), which is the top-level object returned from a DRS server in response to a successful lookup call (i.e. https://ga4gh.github.io/data-repository-service-schemas/preview/release/drs-1.4.0/docs/#tag/Objects)._



<div data-search-exclude markdown="1">



URI: [https://w3id.org/fga-wg/schema/bundle/File](https://w3id.org/fga-wg/schema/bundle/File)





```mermaid
 classDiagram
    class File
    click File href "../File/"
      File <|-- GenomicAnnotationFile
        click GenomicAnnotationFile href "../GenomicAnnotationFile/"
      
      File : access_methods
        
          
    
        
        
        File --> "1..*" AccessMethod : access_methods
        click AccessMethod href "../AccessMethod/"
    

        
      File : checksums
        
          
    
        
        
        File --> "1..*" Checksum : checksums
        click Checksum href "../Checksum/"
    

        
      File : created_time
        
      File : data_content
        
          
    
        
        
        File --> "1" OutputType : data_content
        click OutputType href "../OutputType/"
    

        
      File : drs_uri
        
      File : file_description
        
      File : file_external_id
        
      File : file_id
        
      File : file_input_sources
        
          
    
        
        
        File --> "1..*" InputSource : file_input_sources
        click InputSource href "../InputSource/"
    

        
      File : file_label
        
      File : file_name
        
      File : file_size
        
      File : file_type
        
          
    
        
        
        File --> "1" Term : file_type
        click Term href "../Term/"
    

        
      File : file_version
        
      File : filecollection_refs
        
      File : mime_type
        
      File : quality_assessments
        
          
    
        
        
        File --> "*" QualityAssessment : quality_assessments
        click QualityAssessment href "../QualityAssessment/"
    

        
      File : run_provenance
        
      File : updated_time
        
      
```



## Example

<details>
<summary>Example JSON</summary>

```json
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
  "updated_time": "2016-11-13T17:42:04.385801+00:00"
}
```
</details>




## Inheritance
* **File**
    * [GenomicAnnotationFile](GenomicAnnotationFile.md)


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [file_external_id](file_external_id.md) | 0..1 <br/> [Curie](Curie.md) | External, globally unique identifier for the data file. | direct |
| [file_id](file_id.md) | 1 <br/> [Curie](Curie.md) | Internal identifier for the data file (unique within the metadata deposit). | direct |
| [file_name](file_name.md) | 0..1 <br/> [String](String.md) | A string that can be used to name a data file. This string is made up of uppercase and lowercase letters, decimal digits, hypen, period, and underscore [A-Za-z0-9.-_]. See http://pubs.opengroup.org/onlinepubs/9699919799/basedefs/V1_chap03.html#tag_03_282 [portable filenames]. | direct |
| [file_label](file_label.md) | 1 <br/> [String](String.md) | A human-readable description of the data file, short enough to be used for listings within software user interfaces, tables, illustration legends, etc. | direct |
| [file_description](file_description.md) | 0..1 <br/> [String](String.md) | A human readable description of the data file. | direct |
| [filecollection_refs](filecollection_refs.md) | 1..* <br/> [Curie](Curie.md) | Internal references to the FileCollection objects (within the deposit) that contains the data file, if any. | direct |
| [file_input_sources](file_input_sources.md) | 1..* <br/> [InputSource](InputSource.md) | External or internal references to data sources for the file, typically a data collection or a process that has generated the file. Internal references should lead to FileCollection, File, Experiment, or Analysis objects. | direct |
| [drs_uri](drs_uri.md) | 0..1 <br/> [Uri](Uri.md) | A drs:// hostname-based URI, as defined in the DRS documentation, that tells clients how to access this object. The intent of this field is to make DRS objects self-contained, and therefore easier for clients to store and pass around. For example, if you arrive at this DRS JSON by resolving a compact identifier-based DRS URI, the self_uri presents you with a hostname and properly encoded DRS ID for use in subsequent access endpoint calls. | direct |
| [access_methods](access_methods.md) | 1..* <br/> [AccessMethod](AccessMethod.md) | The list of access methods that can be used to fetch the data file. | direct |
| [run_provenance](run_provenance.md) | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | Document detailing the provenance of the experiment or analysis run which produced the file as one of its outputs. The provenance info should include software versions, parameter settings, etc. | direct |
| [quality_assessments](quality_assessments.md) | * <br/> [QualityAssessment](QualityAssessment.md) | An array of QualityAssessment objects containing the main quality scores from assessment techniques applied to the data file. | direct |
| [file_type](file_type.md) | 1 <br/> [Term](Term.md) | The file format of the data file. | direct |
| [mime_type](mime_type.md) | 0..1 <br/> [String](String.md) | A string providing the mime-type of the data file. | direct |
| [data_content](data_content.md) | 1 <br/> [OutputType](OutputType.md) | Classification describing the file's purpose or contents. | direct |
| [file_size](file_size.md) | 1 <br/> [Integer](Integer.md) | The file size in bytes. | direct |
| [created_time](created_time.md) | 1 <br/> [Datetime](Datetime.md) | Timestamp of content creation in RFC3339. (This is the creation time of the underlying content, not of the JSON object.). | direct |
| [updated_time](updated_time.md) | 0..1 <br/> [Datetime](Datetime.md) | Timestamp of content update in RFC3339, identical to created_time in systems that do not support updates. (This is the update time of the underlying content, not of the JSON object.). | direct |
| [file_version](file_version.md) | 0..1 <br/> [String](String.md) | A string representing a version. (Some systems may use checksum, a RFC3339 timestamp, or an incrementing version number.). | direct |
| [checksums](checksums.md) | 1..* <br/> [Checksum](Checksum.md) | A list of checksums of the data file. At least one checksum must be provided. For blobs, the checksum is computed over the bytes in the blob. | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Bundle](Bundle.md) | [files](files.md) | range | [File](File.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fga-wg/schema/bundle




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://w3id.org/fga-wg/schema/bundle/File |
| native | https://w3id.org/fga-wg/schema/bundle/File |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: File
description: General information about a particular data file. Most fields (marked
  with an asterix*) are copied from the GA4GH DRS DrsObject model (https://ga4gh.github.io/data-repository-service-schemas/preview/release/drs-1.4.0/docs/#tag/DrsObjectModel),
  which is the top-level object returned from a DRS server in response to a successful
  lookup call (i.e. https://ga4gh.github.io/data-repository-service-schemas/preview/release/drs-1.4.0/docs/#tag/Objects).
from_schema: https://w3id.org/fga-wg/schema/bundle
slots:
- file_external_id
- file_id
- file_name
- file_label
- file_description
- filecollection_refs
- file_input_sources
- drs_uri
- access_methods
- run_provenance
- quality_assessments
- file_type
- mime_type
- data_content
- file_size
- created_time
- updated_time
- file_version
- checksums

```
</details>

### Induced

<details>
```yaml
name: File
description: General information about a particular data file. Most fields (marked
  with an asterix*) are copied from the GA4GH DRS DrsObject model (https://ga4gh.github.io/data-repository-service-schemas/preview/release/drs-1.4.0/docs/#tag/DrsObjectModel),
  which is the top-level object returned from a DRS server in response to a successful
  lookup call (i.e. https://ga4gh.github.io/data-repository-service-schemas/preview/release/drs-1.4.0/docs/#tag/Objects).
from_schema: https://w3id.org/fga-wg/schema/bundle
attributes:
  file_external_id:
    name: file_external_id
    description: External, globally unique identifier for the data file.
    examples:
    - value: encode:ENCFF323LCS
    from_schema: https://w3id.org/fga-wg/schema/bundle
    rank: 1000
    owner: File
    domain_of:
    - File
    range: curie
  file_id:
    name: file_id
    description: 'Internal identifier for the data file (unique within the metadata
      deposit). '
    examples:
    - value: file:ENCFF323LCS
    from_schema: https://w3id.org/fga-wg/schema/bundle
    rank: 1000
    identifier: true
    owner: File
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
    from_schema: https://w3id.org/fga-wg/schema/bundle
    rank: 1000
    owner: File
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
    from_schema: https://w3id.org/fga-wg/schema/bundle
    rank: 1000
    owner: File
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
    from_schema: https://w3id.org/fga-wg/schema/bundle
    rank: 1000
    owner: File
    domain_of:
    - File
    range: string
  filecollection_refs:
    name: filecollection_refs
    description: Internal references to the FileCollection objects (within the deposit)
      that contains the data file, if any.
    examples:
    - value: collection:ihec_encode
    from_schema: https://w3id.org/fga-wg/schema/bundle
    rank: 1000
    owner: File
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
    from_schema: https://w3id.org/fga-wg/schema/bundle
    rank: 1000
    owner: File
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
    from_schema: https://w3id.org/fga-wg/schema/bundle
    rank: 1000
    owner: File
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
    from_schema: https://w3id.org/fga-wg/schema/bundle
    rank: 1000
    owner: File
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
    from_schema: https://w3id.org/fga-wg/schema/bundle
    rank: 1000
    owner: File
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
    from_schema: https://w3id.org/fga-wg/schema/bundle
    rank: 1000
    owner: File
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
    from_schema: https://w3id.org/fga-wg/schema/bundle
    rank: 1000
    owner: File
    domain_of:
    - File
    range: Term
    required: true
  mime_type:
    name: mime_type
    description: A string providing the mime-type of the data file.
    examples:
    - value: application/octet-stream
    from_schema: https://w3id.org/fga-wg/schema/bundle
    rank: 1000
    owner: File
    domain_of:
    - File
    range: string
  data_content:
    name: data_content
    description: Classification describing the file's purpose or contents.
    examples:
    - value: replicated peaks
    from_schema: https://w3id.org/fga-wg/schema/bundle
    rank: 1000
    owner: File
    domain_of:
    - File
    range: OutputType
    required: true
  file_size:
    name: file_size
    description: The file size in bytes.
    examples:
    - value: '5359719'
    from_schema: https://w3id.org/fga-wg/schema/bundle
    rank: 1000
    owner: File
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
    from_schema: https://w3id.org/fga-wg/schema/bundle
    rank: 1000
    owner: File
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
    from_schema: https://w3id.org/fga-wg/schema/bundle
    rank: 1000
    owner: File
    domain_of:
    - File
    range: datetime
  file_version:
    name: file_version
    description: A string representing a version. (Some systems may use checksum,
      a RFC3339 timestamp, or an incrementing version number.).
    examples:
    - value: efd4e74e-7875-4d13-9630-0085bc834f18
    from_schema: https://w3id.org/fga-wg/schema/bundle
    rank: 1000
    owner: File
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
    from_schema: https://w3id.org/fga-wg/schema/bundle
    rank: 1000
    owner: File
    domain_of:
    - File
    range: Checksum
    required: true
    multivalued: true

```
</details></div>