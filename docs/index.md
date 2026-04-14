# TopLevel



URI: https://w3id.org/fga-wg/schema/top_level

Name: TopLevel



## Classes

| Class | Description |
| --- | --- |
| [AccessMethod](AccessMethod.md) | Description of an access method (i.e. communication protocol) that can be used to fetch a File object (orig: DrsObject). Exact copy of the AccessMethod object of the GA4GH DRS data model (https://ga4gh.github.io/data-repository-service-schemas/preview/release/drs-1.4.0/docs/#tag/AccessMethodModel) |
| [AccessURL](AccessURL.md) | The URL and associated HTTP headers to access the File object (orig: DrsObject). Exact copy of AccessURL object of the GA4GH DRS data model (https://ga4gh.github.io/data-repository-service-schemas/preview/release/drs-1.4.0/docs/#tag/AccessURLModel). |
| [Analysis](Analysis.md) | Represents the computational processing applied to data from a sequencing experiment, or from another analysis. This can be described at the level of individual analysis steps in a workflow/pipeline, or more generally for the workflow/pipeline as a whole. |
| [Any](Any.md) | The Any allows the range of a slot to be any object (see https://linkml.io/linkml/schemas/advanced.html#linkml-any-type). |
| [AssessmentValue](AssessmentValue.md) | Key-value pair representing a specific value produced by a quality assessment. |
| [Checksum](Checksum.md) | A checksum of a File object (orig: DrsObject). Exact copy of the Checksum object of the GA4GH DRS data model (https://ga4gh.github.io/data-repository-service-schemas/preview/release/drs-1.4.0/docs/#tag/ChecksumModel). |
| [Contact](Contact.md) | Contact information for a person or an organisation. |
| [Deposit](Deposit.md) | Information about a public deposit of a document containing metadata about a set of genome annotation files. |
| [Document](Document.md) | Information about a document containing metadata about a set of genome annotation files, harmonised according to the "FAIRification of Genomic Annotations" data model.  This includes self-referential identifiers and versioning of public deposits of the document. |
| [Donor](Donor.md) | Information about the donor or complete organism from which the sample was taken. |
| [Experiment](Experiment.md) | Represents a sequencing experiment that has been carried out within a study, based on biological samples, and providing data files as output. Subsequent analysis of output data is described by the Analysis entity. |
| [File](File.md) | General information about a particular data file. Most fields (marked with an asterix*) are copied from the GA4GH DRS DrsObject model (https://ga4gh.github.io/data-repository-service-schemas/preview/release/drs-1.4.0/docs/#tag/DrsObjectModel), which is the top-level object returned from a DRS server in response to a successful lookup call (i.e. https://ga4gh.github.io/data-repository-service-schemas/preview/release/drs-1.4.0/docs/#tag/Objects). |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[GenomicAnnotationFile](GenomicAnnotationFile.md) | Information about a genomic annotation / track file. GenomicAnnotationFile is a specification of the File entity and inherits all the fields defined in File, in addition to the fields that are specific to GenomicAnnotationFile, as detailed here. |
| [FileCollection](FileCollection.md) | A collection of files, according to some selection criteria. In the context of the "FAIRification of Genomic Annotations" data model, we are mainly interested in "GenomicAnnotationFile" entities, but other types of files can also be contained in a collection, e.g. raw data files such as FASTQ files. |
| [GenomeAssembly](GenomeAssembly.md) | Information about of the exact genome assembly used to generate the annotation file, defining the genomic coordinate system for the sequence features. |
| [InputSource](InputSource.md) | General object representing the source of data files, samples, or other entities used as input to a process or a result. An input source refering to a single file or sample object will represent that item only, while an input source referring to a container or process may represent a number of disctinct input items. InputSource also contains information about the type of relationship, replication labelling, versioning and retrieval date. |
| [OntologyVersions](OntologyVersions.md) | Information about an ontology used in the metadata. |
| [QualityAssessment](QualityAssessment.md) | Represents the results of a quality assessment that has been carried out on a data file resulting from an experiment or analysis. |
| [Sample](Sample.md) | Information about a biospecimen/sample used as raw material for lab experiments. |
| [Study](Study.md) | A scientific study, i.e. a unit of research, within which experiments and/or analyses have been carried out. |
| [Term](Term.md) | Helper entity to represent an ontology term as a data value. |
| [TopLevel](TopLevel.md) | A document of harmonised metadata for a set of genome annotation files. Metadata has been harmonised in line with the "FAIRification of Genomic Annotations" data model. This is the top-level class to be used as root for the metadata document. |
| [TrackGeometry](TrackGeometry.md) | Overall geometric properties of the sequence features in the genomic annotation file if considered as an one-dimensional genome browser track, in line with the track type delineations from Gundersen et. al, 2011. While conceptually based on visual characteristics, these properties are also useful to e.g. select relevant annotation files for non-visual analyses. |



## Slots

| Slot | Description |
| --- | --- |
| [access_method](access_method.md) | Access method used to access the File object (orig: DrsObject). |
| [access_methods](access_methods.md) | The list of access methods that can be used to fetch the data file. |
| [access_url](access_url.md) | AccessURL object providing URL and associated HTTP headers to access the File object (orig: DrsObject). |
| [accessions](accessions.md) | Database accession numbers for the genome assembly, if available. Should precisely identify the genome assembly and be omitted if changes have been made to the assembly after retrieval, such as removing the alternate sequences. |
| [aliases](aliases.md) | Human-readable aliases of the genome assembly. Can be imprecise, as preciseness is enforced in the other fields. |
| [analyses](analyses.md) | Information about computational processing and analyses that have been carried out to generate the files. |
| [analysis_description](analysis_description.md) | Human-readable description of the analysis. |
| [analysis_external_id](analysis_external_id.md) | External, globally unique identifier for the experiment. |
| [analysis_id](analysis_id.md) | Internal identifier for the experiment (unique within the metadata deposit). |
| [analysis_input_sources](analysis_input_sources.md) | External or internal references to sources for the input data analyzed. Internal references should lead to FileCollection, File, Experiment, or Analysis objects. |
| [analysis_label](analysis_label.md) | A human-readable description of the analysis, short enough to be used for listings within software user interfaces, tables, illustration legends, etc. |
| [analysis_main_tool](analysis_main_tool.md) | Main software tool used for the analysis. |
| [analysis_main_tool_version](analysis_main_tool_version.md) | Version of the main software tool used for the analysis. |
| [analysis_protocol](analysis_protocol.md) | Document describing the analysis protocol that was followed. |
| [analysis_study_ref](analysis_study_ref.md) | Internal reference to the study within which the analysis has been carried out. |
| [analysis_type](analysis_type.md) | The type of analysis carried out. |
| [analysis_workflow](analysis_workflow.md) | External reference to the analysis workflow, with availability in at least one machine-operable form (e.g. CWL, Nextflow, ...). |
| [antibody_target](antibody_target.md) | The target of the antibody used in the experiment. |
| [assay_type](assay_type.md) | Sequencing technique intended for this library. |
| [assessment_details_url](assessment_details_url.md) | URL to a report containing the detailed output from the quality assessment. |
| [assessment_method](assessment_method.md) | Quality assessment method that has been carried out (e.g. BUSCO, OMArk, peak calling statistics, etc.) |
| [assessment_values](assessment_values.md) | Main values produced by the quality assessment. |
| [biological_processes](biological_processes.md) | Biological processes illuminated by the experiment. |
| [biological_replicate_labels](biological_replicate_labels.md) | Labels denoting the biological replicates within which the relation is defined, if any. |
| [biospecimen_classification](biospecimen_classification.md) | Main type of structural unit to be used for classification of the biospecimen/sample. |
| [cell_line](cell_line.md) | Cultured cell line used in the biospecimen/sample. |
| [cell_type](cell_type.md) | Cell type of isolated normal cells in the biospecimen/sample. |
| [checksum](checksum.md) | The hex-string encoded checksum for the data. |
| [checksum_type](checksum_type.md) | The digest method used to create the checksum. The value (e.g. `sha-256`) SHOULD be listed as `Hash Name String` in the https://www.iana.org/assignments/named-information/named-information.xhtml#hash-alg [IANA Named Information Hash Algorithm Registry]. Other values MAY be used, as long as implementors are aware of the issues discussed in https://tools.ietf.org/html/rfc6920#section-9.4 [RFC6920]. GA4GH may provide more explicit guidance for use of non-IANA-registered algorithms in the future. Until then, if implementors do choose such an algorithm (e.g. because it's implemented by their storage provider), they SHOULD use an existing standard `type` value such as `md5`, `etag`, `crc32c`, `trunc512`, or `sha1`. |
| [checksums](checksums.md) | A list of checksums of the data file. At least one checksum must be provided. For blobs, the checksum is computed over the bytes in the blob. |
| [contact_id](contact_id.md) | Globally unique identifier for a person (e.g. ORCID ID) or organisation (e.g. BioProject accession). |
| [created_time](created_time.md) | Timestamp of content creation in RFC3339. (This is the creation time of the underlying content, not of the JSON object.). |
| [data_content](data_content.md) | Classification describing the file's purpose or contents. |
| [database_accessions](database_accessions.md) | Accession numbers for database records used as input source. Used in connection with "inputsource_external_ref". |
| [date_of_retrieval](date_of_retrieval.md) | Date of retrieval from the input source, typically used to timestamp downloading data from a database or URL. |
| [deposit_first_created](deposit_first_created.md) | The date and time of the creation of the first deposited version of the metadata document. |
| [deposit_id](deposit_id.md) | A globally unique and persistent identifier for the public deposit of the metadata document. A DOI or other persistent identifier is recommended. |
| [deposit_last_changed](deposit_last_changed.md) | The date and time of the last deposited change of the current metadata document (corresponding to "deposit_versioned_id"). |
| [deposit_versioned_id](deposit_versioned_id.md) | A globally unique, persistent and versioned identifier for the public deposit of the metadata document. A versioned DOI to a deposited document is recommended. |
| [deposit_versioned_ref](deposit_versioned_ref.md) | Reference to versioned id of deposit containing this file collection. |
| [design_description](design_description.md) | The high-level experiment design including layout, protocol. |
| [document](document.md) | Information about this document containing harmonised metadata about a set of genome annotation files. This includes self-referential identifiers and versioning of public deposits of the document. |
| [document_deposit](document_deposit.md) | Information about the public deposit of the metadata document. |
| [document_description](document_description.md) | Human-readable description of the metadata document. |
| [document_input_sources](document_input_sources.md) | References to other input sources from which this entire metadata document was derived, or possibly including DOIs of other metadata documents used as source. |
| [document_label](document_label.md) | A human-readable description of the metadata document, short enough to be used for listings within software user interfaces, tables, illustration legends, etc. |
| [document_ontology_versions](document_ontology_versions.md) | Map from the version-agnostic URL to a versioned URL (e.g. "versionIRI" in owl) of each ontology used in the current metadata deposit (corresponding to deposit_versioned_id"). |
| [donor_age](donor_age.md) | Age of the donor/organism at the time of sampling |
| [donor_clinical_information](donor_clinical_information.md) | Clinical information of the donor/organism at the time of sampling. |
| [donor_development_stage](donor_development_stage.md) | Development stage of the donor at the time of sampling. |
| [donor_external_id](donor_external_id.md) | External, globally unique identifier for the donor/organism. |
| [donor_id](donor_id.md) | Internal identifier for the donor/organism (unique within the metadata deposit). |
| [donor_organism_ref](donor_organism_ref.md) | Internal reference to the donor/organism from which the biospecimen/sample was taken. |
| [donors](donors.md) | Information about the donors or complete organisms from which the samples were taken. |
| [drs_uri](drs_uri.md) | A drs:// hostname-based URI, as defined in the DRS documentation, that tells clients how to access this object. The intent of this field is to make DRS objects self-contained, and therefore easier for clients to store and pass around. For example, if you arrive at this DRS JSON by resolving a compact identifier-based DRS URI, the self_uri presents you with a hostname and properly encoded DRS ID for use in subsequent access endpoint calls. |
| [edge_weight_type](edge_weight_type.md) | The type of values associated with the edges. |
| [edges_are_directed](edges_are_directed.md) | Whether the edges linking sequence features are directed (at least one edge between sequence features is defined with a direction). |
| [edges_denote_parents](edges_denote_parents.md) | Whether the edges linking sequence features denote a parent-child relationship (all edges between sequence features denote parent-child relationships such as genes to exons, i.e. where the child is fully covered by the parent). |
| [edges_have_weights](edges_have_weights.md) | Whether the edges linking sequence features are weighted (at least one edge between sequence features has an associated weight). |
| [elements_circular](elements_circular.md) | Whether the sequence features have circular coordinates (at least one feature that cross a sequence border). |
| [elements_overlapping](elements_overlapping.md) | Whether the sequence features are overlapping (at least one base pair is simultaneously covered by two sequence features). |
| [email](email.md) | E-mail address of the person or organisation. |
| [experiment_external_id](experiment_external_id.md) | External, globally unique identifier for the experiment. |
| [experiment_id](experiment_id.md) | Internal identifier for the experiment (unique within the metadata deposit). |
| [experiment_label](experiment_label.md) | A human-readable description of the experiment, short enough to be used for listings within software user interfaces, tables, illustration legends, etc. |
| [experiment_samples](experiment_samples.md) | External or internal references to samples used in the experiment. Internal references should refer to Sample objects. |
| [experiment_study_ref](experiment_study_ref.md) | Internal reference to the study within which the experiment has been carried out. |
| [experiments](experiments.md) | Information about sequencing experiments that have been carried out to generate the files. |
| [file_collections](file_collections.md) | Information about collections of files contained in this dataset, each collection defined according to some selection criteria. |
| [file_description](file_description.md) | A human readable description of the data file. |
| [file_external_id](file_external_id.md) | External, globally unique identifier for the data file. |
| [file_id](file_id.md) | Internal identifier for the data file (unique within the metadata deposit). |
| [file_input_sources](file_input_sources.md) | External or internal references to data sources for the file, typically a data collection or a process that has generated the file. Internal references should lead to FileCollection, File, Experiment, or Analysis objects. |
| [file_label](file_label.md) | A human-readable description of the data file, short enough to be used for listings within software user interfaces, tables, illustration legends, etc. |
| [file_name](file_name.md) | A string that can be used to name a data file. This string is made up of uppercase and lowercase letters, decimal digits, hypen, period, and underscore [A-Za-z0-9.-_]. See http://pubs.opengroup.org/onlinepubs/9699919799/basedefs/V1_chap03.html#tag_03_282 [portable filenames]. |
| [file_size](file_size.md) | The file size in bytes. |
| [file_type](file_type.md) | The file format of the data file. |
| [file_version](file_version.md) | A string representing a version. (Some systems may use checksum, a RFC3339 timestamp, or an incrementing version number.). |
| [filecollection_contact](filecollection_contact.md) | Contact point to the creator and/or maintainer of the file collection. |
| [filecollection_description](filecollection_description.md) | Human-readable description of the file collection. |
| [filecollection_external_id](filecollection_external_id.md) | External, globally unique identifier for the file collection (in most cases, this will not exist). |
| [filecollection_id](filecollection_id.md) | Internal identifier for the file collection (unique within the metadata deposit). |
| [filecollection_input_sources](filecollection_input_sources.md) | References to other input sources from which this file collection was derived. |
| [filecollection_label](filecollection_label.md) | A human-readable description of the file collection, short enough to be used for listings within software user interfaces, tables, illustration legends, etc. |
| [filecollection_refs](filecollection_refs.md) | Internal references to the FileCollection objects (within the deposit) that contains the data file, if any. |
| [files](files.md) | Information about particular genome annotation (and other relevant) files. |
| [genome_assembly](genome_assembly.md) | Information about the genome assembly used to generate the genomic annotation file, consequently defining the genomic coordinate system for the annotation. |
| [genomic_annotation_digest](genomic_annotation_digest.md) | Content-derived digest for distributed identification of genomic annotation files. (This field is currently a placeholder, as an algorithm for generating such a digest is yet to be specified.). |
| [has_edges](has_edges.md) | Whether the sequence features are linked across positions (at least one edge between features exists). |
| [has_gaps](has_gaps.md) | Whether there are gaps between the sequence features (there exists at least one gap between two features on the same sequence). |
| [has_lengths](has_lengths.md) | Whether the sequence features have lengths (at least one feature spans more than 1 base pair). |
| [has_names](has_names.md) | Whether the sequence features are named (at least one feature has a name). |
| [has_strands](has_strands.md) | Whether the sequence features are stranded (at least one feature has strand information). |
| [has_values](has_values.md) | Whether the sequence features have associated values (at least one feature has an associated value). |
| [headers](headers.md) | An optional list of headers to include in the HTTP request to `url`. These headers can be used to provide auth tokens required to fetch the object bytes. |
| [id](id.md) | External, globally unique identifier for the ontology term (in CURIE form). |
| [inputsource_external_ref](inputsource_external_ref.md) | Reference to an external entity as the input source, using a globally unique identifier or an URL. External references will in most cases refer to a database, data record, data file, website or other data source. One of "inputsource_external_ref" or "inputsource_ref" must be specified. |
| [inputsource_ref](inputsource_ref.md) | Reference to an internal object as the input source using a local identifier. Entities to be used as an internal input source includes FileCollection, Sample, Experiment, Analysis or File as restricted by the description of the field where the input source is used. One of "inputsource_external_ref" or "inputsource_ref" must be specified. |
| [instrument](instrument.md) | Technology platform used to perform nucleic acid sequencing, including name and/or number associated with a specific sequencing instrument model. It is recommended to be as specific as possible for this property (e.g. if the model/revision are available, providing that instead of just the instrument maker). |
| [key](key.md) | Key/name of the assessment value. |
| [label](label.md) | Human-readable label associated to the term id in the current version of the ontology (as listed in the "ontology_versions" field of the Deposit object). |
| [lengths_constant](lengths_constant.md) | Whether the sequence lengths are constant (all sequence features have the same length, excluding features at the very end of a sequence). |
| [library_layout](library_layout.md) | Whether the library was built as paired-end, or single-end. |
| [mime_type](mime_type.md) | A string providing the mime-type of the data file. |
| [molecule_type](molecule_type.md) | Specifies the type of source material that is being sequenced. |
| [name](name.md) | Name of the person or organisation. |
| [namespace](namespace.md) | The CURIE namespace (prefix) an ontology (e.g. "GO" for Gene Ontology). |
| [ontology_url](ontology_url.md) | The version-agnostic URL of the ontology (e.g. the IRI of the ontology in OWL). |
| [organism_tissue](organism_tissue.md) | Part of organism (typically tissue or organ) from which the biospecimen/sample was taken, or cell line was derived from. |
| [other_biospecimen](other_biospecimen.md) | Other biospecimen-related terms that can be used to further classify the biospecimen/sample. |
| [phenotype](phenotype.md) | Main phenotype (e.g. disease) connected to the biospecimen/sample. |
| [project_external_ref](project_external_ref.md) | Reference to a project within which the study was carried out (preferably a BioProject CURIE). |
| [project_name](project_name.md) | Name of the project within which the study was carried out. |
| [publications](publications.md) | List of (relevant) publications containing the results of the study (in the form of DOI CURIEs). |
| [qualified_relation](qualified_relation.md) | A description of the relationship with the input source. |
| [quality_assessments](quality_assessments.md) | An array of QualityAssessment objects containing the main quality scores from assessment techniques applied to the data file. |
| [region](region.md) | Name of the region in the cloud service provider that the object belongs to. |
| [run_provenance](run_provenance.md) | Document detailing the provenance of the experiment or analysis run which produced the file as one of its outputs. The provenance info should include software versions, parameter settings, etc. |
| [sample_collection_date](sample_collection_date.md) | Date of sample collection. |
| [sample_collection_location](sample_collection_location.md) | Geographical location where the sample was collected. |
| [sample_description](sample_description.md) | Human-readable description of the biospecimen/sample and the sampling process. |
| [sample_external_id](sample_external_id.md) | External, globally unique identifier for the biospecimen/sample. |
| [sample_id](sample_id.md) | Internal identifier for the biospecimen/sample (unique within the metadata deposit). |
| [sample_label](sample_label.md) | A human-readable description of the sample, short enough to be used for listings within software user interfaces, tables, illustration legends, etc. |
| [samples](samples.md) | Information about the biospecimens/samples used as raw material for lab experiments. |
| [sampling_protocol](sampling_protocol.md) | Protocol detailing the collection and treatment of the biospecimen/sample. |
| [seqcol_digest](seqcol_digest.md) | Top-level sequence collection digest according to the GA4GH refget, Sequence Collections standard (v1.0). This a globally unique identifier for the genome assembly, algorithmically derivable from the genome assembly content. Usage is to uniquely identify the exact genome assembly used and allow detailed comparisons across genome assembly variants (say, variants of the GRCh38 assembly). |
| [seqcol_ordered_coord_system](seqcol_ordered_coord_system.md) | Content-derived digest that uniquely identifies the ordered coordinate system of the genome assembly. (Coordinate systems with the same sequence names and lengths, but where the sequences are ordered differently, will have different ordered digests.). Usage is the ordered coordinate system digest can be used to uniquely generate a chromSizes file, useful in a number of analysis tools. Definition is the ordered coordinate system digest is defined as the level 1 digest of the name_length_pairs attribute of the sequence collection generated from the genome assembly. |
| [seqcol_unordered_coord_system](seqcol_unordered_coord_system.md) | Content-derived digest that uniquely identifies the order-invariant coordinate system of the genome assembly. This digest will be shared across all coordinate systems with the same sequence names and lenghts, regardless of the order of the sequences. Usage is the order-invariant coordinate system digest can be used to uniquely describe the coordinate system of a particular genome browser instance and the annotation files that are compatible with it. Definition is the order-invariant coordinate system digest is defined as the level 1 digest of the sorted_name_length_pairs attribute of the sequence collection generated from the genome assembly. |
| [sequence_features](sequence_features.md) | List of sequence features described by the genomic annotation file. |
| [sequencing_protocol](sequencing_protocol.md) | Set of rules which guides how the sequencing protocol was followed. Change-tracking services such as Protocol.io or GitHub are encouraged instead of dumping free text in this field. |
| [sex](sex.md) | Biological sex of the donor/organism. |
| [species_taxon](species_taxon.md) | Taxonomical classification of the species of the donor/organism. |
| [studies](studies.md) | The scientific studies, i.e. units of research, within which experiments and/or analyses have been carried out. |
| [study_abstract](study_abstract.md) | Abstract of the study. |
| [study_contact](study_contact.md) | Contact point for the study. |
| [study_external_id](study_external_id.md) | External, globally unique identifier for the study (preferably a BioStudies CURIE). |
| [study_id](study_id.md) | Internal identifier for the study (unique within the metadata deposit). Namespace: "study". |
| [study_title](study_title.md) | Title of the study. |
| [technical_replicate_labels](technical_replicate_labels.md) | Labels denoting the technical replicates within which the relation is defined, if any. |
| [track_geometry](track_geometry.md) | Geometric properties of the sequence features in the genomic annotation file if considered as an one-dimensional genome browser track (also relevant for non-visual analyses). |
| [updated_time](updated_time.md) | Timestamp of content update in RFC3339, identical to created_time in systems that do not support updates. (This is the update time of the underlying content, not of the JSON object.). |
| [url](url.md) | A fully resolvable URL that can be used to fetch the actual object bytes. |
| [value](value.md) | Value corresponding to the assessment key. |
| [value_type](value_type.md) | The type of values associated with the sequence features, if any. |
| [version](version.md) | Version information for the retrieval from the input source. |
| [versioned_ontology_url](versioned_ontology_url.md) | The versioned URL of the ontology (e.g. the "versionIRI" in OWL). |


## Enumerations

| Enumeration | Description |
| --- | --- |
| [AccessMethods](AccessMethods.md) | Access methods (i.e. communication protocols), following the vocabulary defined in the GA4GH DRS specification (https://ga4gh.github.io/data-repository-service-schemas/preview/release/drs-1.4.0/docs/#tag/AccessMethodModel/operation/getAccessMethod). |
| [BiospecimenClassification](BiospecimenClassification.md) | Vocabulary from the ENCODE model describing the general category of boispecimen (see "Properties->classification" in https://www.encodeproject.org/profiles/biosample_type). |
| [DataTypes](DataTypes.md) | Types of data values associated with sequence features or edges. |
| [OutputType](OutputType.md) | Vocabulary from the ENCODE model describing the purpose or content of a file (see "Properties->output_type" in https://www.encodeproject.org/profiles/file). |


## Types

| Type | Description |
| --- | --- |
| [Boolean](Boolean.md) | A binary (true or false) value |
| [Curie](Curie.md) | a compact URI |
| [Date](Date.md) | a date (year, month and day) in an idealized calendar |
| [DateOrDatetime](DateOrDatetime.md) | Either a date or a datetime |
| [Datetime](Datetime.md) | The combination of a date and time |
| [Decimal](Decimal.md) | A real number with arbitrary precision that conforms to the xsd:decimal specification |
| [Double](Double.md) | A real number that conforms to the xsd:double specification |
| [Float](Float.md) | A real number that conforms to the xsd:float specification |
| [Integer](Integer.md) | An integer |
| [Jsonpath](Jsonpath.md) | A string encoding a JSON Path. The value of the string MUST conform to JSON Point syntax and SHOULD dereference to zero or more valid objects within the current instance document when encoded in tree form. |
| [Jsonpointer](Jsonpointer.md) | A string encoding a JSON Pointer. The value of the string MUST conform to JSON Point syntax and SHOULD dereference to a valid object within the current instance document when encoded in tree form. |
| [Ncname](Ncname.md) | Prefix part of CURIE |
| [Nodeidentifier](Nodeidentifier.md) | A URI, CURIE or BNODE that represents a node in a model. |
| [Objectidentifier](Objectidentifier.md) | A URI or CURIE that represents an object in the model. |
| [Sparqlpath](Sparqlpath.md) | A string encoding a SPARQL Property Path. The value of the string MUST conform to SPARQL syntax and SHOULD dereference to zero or more valid objects within the current instance document when encoded as RDF. |
| [String](String.md) | A character string |
| [Time](Time.md) | A time object represents a (local) time of day, independent of any particular day |
| [Uri](Uri.md) | a complete URI |
| [Uriorcurie](Uriorcurie.md) | a URI or a CURIE |


## Subsets

| Subset | Description |
| --- | --- |
