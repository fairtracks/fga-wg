# TopLevel



URI: https://w3id.org/fga-wg/schema/top_level

Name: TopLevel



## Classes

| Class | Description |
| --- | --- |
| [AccessMethod](AccessMethod.md) | Description of an access method (i |
| [AccessURL](AccessURL.md) | The URL and associated HTTP headers to access the File object (orig: DrsObjec... |
| [Analysis](Analysis.md) | Represents the computational processing applied to data from a sequencing exp... |
| [Any](Any.md) | The Any allows the range of a slot to be any object (see https://linkml |
| [AssessmentValue](AssessmentValue.md) | Key-value pair representing a specific value produced by a quality assessment |
| [Checksum](Checksum.md) | A checksum of a File object (orig: DrsObject) |
| [Contact](Contact.md) | Contact information for a person or an organisation |
| [Deposit](Deposit.md) | Information about a public deposit of a document containing metadata about a ... |
| [Document](Document.md) | Information about a document containing metadata about a set of genome annota... |
| [Donor](Donor.md) | Information about the donor or complete organism from which the sample was ta... |
| [Experiment](Experiment.md) | Represents a sequencing experiment that has been carried out within a study, ... |
| [File](File.md) | General information about a particular data file |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[GenomicAnnotationFile](GenomicAnnotationFile.md) | Information about a genomic annotation / track file |
| [FileCollection](FileCollection.md) | A collection of files, according to some selection criteria |
| [GenomeAssembly](GenomeAssembly.md) | Information about of the exact genome assembly used to generate the annotatio... |
| [InputSource](InputSource.md) | General object representing the source of data files, samples, or other entit... |
| [OntologyVersions](OntologyVersions.md) | Information about an ontology used in the metadata |
| [QualityAssessment](QualityAssessment.md) | Represents the results of a quality assessment that has been carried out on a... |
| [Sample](Sample.md) | Information about a biospecimen/sample used as raw material for lab experimen... |
| [Term](Term.md) | Helper entity to represent an ontology term as a data value |
| [TopLevel](TopLevel.md) | A document of harmonised metadata for a set of genome annotation files |
| [TrackGeometry](TrackGeometry.md) | Overall geometric properties of the sequence features in the genomic annotati... |



## Slots

| Slot | Description |
| --- | --- |
| [access_method](access_method.md) | Access method used to access the File object (orig: DrsObject) |
| [access_methods](access_methods.md) | The list of access methods that can be used to fetch the data file |
| [access_url](access_url.md) | AccessURL object providing URL and associated HTTP headers to access the File... |
| [accessions](accessions.md) | Database accession numbers for the genome assembly, if available |
| [aliases](aliases.md) | Human-readable aliases of the genome assembly |
| [analyses](analyses.md) | Information about computational processing and analyses that have been carrie... |
| [analysis_description](analysis_description.md) | Human-readable description of the analysis |
| [analysis_external_id](analysis_external_id.md) | External, globally unique identifier for the experiment |
| [analysis_id](analysis_id.md) | Internal identifier for the experiment (unique within the metadata deposit) |
| [analysis_input_sources](analysis_input_sources.md) | External or internal references to sources for the input data analyzed |
| [analysis_label](analysis_label.md) | A human-readable description of the analysis, short enough to be used for lis... |
| [analysis_main_tool](analysis_main_tool.md) | Main software tool used for the analysis |
| [analysis_main_tool_version](analysis_main_tool_version.md) | Version of the main software tool used for the analysis |
| [analysis_protocol](analysis_protocol.md) | Document describing the analysis protocol that was followed |
| [analysis_study_ref](analysis_study_ref.md) | Internal reference to the study within which the analysis has been carried ou... |
| [analysis_type](analysis_type.md) | The type of analysis carried out |
| [analysis_workflow](analysis_workflow.md) | External reference to the analysis workflow, with availability in at least on... |
| [antibody_target](antibody_target.md) | The target of the antibody used in the experiment |
| [assay_type](assay_type.md) | Sequencing technique intended for this library |
| [assessment_details_url](assessment_details_url.md) | URL to a report containing the detailed output from the quality assessment |
| [assessment_method](assessment_method.md) | Quality assessment method that has been carried out (e |
| [assessment_values](assessment_values.md) | Main values produced by the quality assessment |
| [biological_processes](biological_processes.md) | Biological processes illuminated by the experiment |
| [biological_replicate_labels](biological_replicate_labels.md) | Labels denoting the biological replicates within which the relation is define... |
| [biospecimen_classification](biospecimen_classification.md) | Main type of structural unit to be used for classification of the biospecimen... |
| [cell_line](cell_line.md) | Cultured cell line used in the biospecimen/sample |
| [cell_type](cell_type.md) | Cell type of isolated normal cells in the biospecimen/sample |
| [checksum](checksum.md) | The hex-string encoded checksum for the data |
| [checksum_type](checksum_type.md) | The digest method used to create the checksum |
| [checksums](checksums.md) | A list of checksums of the data file |
| [contact](contact.md) | Contact point to the creator and/or maintainer of the file collection |
| [contact_id](contact_id.md) | Globally unique identifier for a person (e |
| [created_time](created_time.md) | Timestamp of content creation in RFC3339 |
| [data_content](data_content.md) | Classification describing the file's purpose or contents |
| [database_accessions](database_accessions.md) | Accession numbers for database records used as input source |
| [date_of_retrieval](date_of_retrieval.md) | Date of retrieval from the input source, typically used to timestamp download... |
| [deposit_first_created](deposit_first_created.md) | The date and time of the creation of the first deposited version of the metad... |
| [deposit_id](deposit_id.md) | A globally unique and persistent identifier for the public deposit of the met... |
| [deposit_last_changed](deposit_last_changed.md) | The date and time of the last deposited change of the current metadata docume... |
| [deposit_versioned_id](deposit_versioned_id.md) | A globally unique, persistent and versioned identifier for the public deposit... |
| [deposit_versioned_ref](deposit_versioned_ref.md) | Reference to versioned id of deposit containing this file collection |
| [design_description](design_description.md) | The high-level experiment design including layout, protocol |
| [document](document.md) | Information about this document containing harmonised metadata about a set of... |
| [document_deposit](document_deposit.md) | Information about the public deposit of the metadata document |
| [document_description](document_description.md) | Human-readable description of the metadata document |
| [document_input_sources](document_input_sources.md) | References to other input sources from which this entire metadata document wa... |
| [document_label](document_label.md) | A human-readable description of the metadata document, short enough to be use... |
| [document_ontology_versions](document_ontology_versions.md) | Map from the version-agnostic URL to a versioned URL (e |
| [donor_age](donor_age.md) | Age of the donor/organism at the time of sampling |
| [donor_clinical_information](donor_clinical_information.md) | Clinical information of the donor/organism at the time of sampling |
| [donor_development_stage](donor_development_stage.md) | Development stage of the donor at the time of sampling |
| [donor_external_id](donor_external_id.md) | External, globally unique identifier for the donor/organism |
| [donor_id](donor_id.md) | Internal identifier for the donor/organism (unique within the metadata deposi... |
| [donor_organism_ref](donor_organism_ref.md) | Internal reference to the donor/organism from which the biospecimen/sample wa... |
| [donors](donors.md) | Information about the donors or complete organisms from which the samples wer... |
| [drs_uri](drs_uri.md) | A drs:// hostname-based URI, as defined in the DRS documentation, that tells ... |
| [edge_weight_type](edge_weight_type.md) | The type of values associated with the edges |
| [edges_are_directed](edges_are_directed.md) | Whether the edges linking sequence features are directed (at least one edge b... |
| [edges_denote_parents](edges_denote_parents.md) | Whether the edges linking sequence features denote a parent-child relationshi... |
| [edges_have_weights](edges_have_weights.md) | Whether the edges linking sequence features are weighted (at least one edge b... |
| [elements_circular](elements_circular.md) | Whether the sequence features have circular coordinates (at least one feature... |
| [elements_overlapping](elements_overlapping.md) | Whether the sequence features are overlapping (at least one base pair is simu... |
| [email](email.md) | E-mail address of the person or organisation |
| [experiment_external_id](experiment_external_id.md) | External, globally unique identifier for the experiment |
| [experiment_id](experiment_id.md) | Internal identifier for the experiment (unique within the metadata deposit) |
| [experiment_label](experiment_label.md) | A human-readable description of the experiment, short enough to be used for l... |
| [experiment_samples](experiment_samples.md) | External or internal references to samples used in the experiment |
| [experiment_study_ref](experiment_study_ref.md) | Internal reference to the study within which the experiment has been carried ... |
| [experiments](experiments.md) | Information about sequencing experiments that have been carried out to genera... |
| [file_collections](file_collections.md) | Information about collections of files contained in this dataset, each collec... |
| [file_description](file_description.md) | A human readable description of the data file |
| [file_external_id](file_external_id.md) | External, globally unique identifier for the data file |
| [file_id](file_id.md) | Internal identifier for the data file (unique within the metadata deposit) |
| [file_input_sources](file_input_sources.md) | External or internal references to data sources for the file, typically a dat... |
| [file_label](file_label.md) | A human-readable description of the data file, short enough to be used for li... |
| [file_name](file_name.md) | A string that can be used to name a data file |
| [file_size](file_size.md) | For blobs, the blob size in bytes |
| [file_type](file_type.md) | The file format of the data file |
| [file_version](file_version.md) | A string representing a version |
| [filecollection_description](filecollection_description.md) | Human-readable description of the file collection |
| [filecollection_external_id](filecollection_external_id.md) | External, globally unique identifier for the file collection (in most cases, ... |
| [filecollection_id](filecollection_id.md) | Internal identifier for the file collection (unique within the metadata depos... |
| [filecollection_input_sources](filecollection_input_sources.md) | References to other input sources from which this file collection was derived |
| [filecollection_label](filecollection_label.md) | A human-readable description of the file collection, short enough to be used ... |
| [filecollection_refs](filecollection_refs.md) | Internal references to the FileCollection objects (within the deposit) that c... |
| [files](files.md) | Information about particular genome annotation (and other relevant) files |
| [genome_assembly](genome_assembly.md) | Information about the genome assembly used to generate the genomic annotation... |
| [genomic_annotation_digest](genomic_annotation_digest.md) | Content-derived digest for distributed identification of genomic annotation f... |
| [has_edges](has_edges.md) | Whether the sequence features are linked across positions (at least one edge ... |
| [has_gaps](has_gaps.md) | Whether there are gaps between the sequence features (there exists at least o... |
| [has_lengths](has_lengths.md) | Whether the sequence features have lengths (at least one feature spans more t... |
| [has_names](has_names.md) | Whether the sequence features are named (at least one feature has a name) |
| [has_strands](has_strands.md) | Whether the sequence features are stranded (at least one feature has strand i... |
| [has_values](has_values.md) | Whether the sequence features have associated values (at least one feature ha... |
| [headers](headers.md) | An optional list of headers to include in the HTTP request to `url` |
| [id](id.md) | External, globally unique identifier for the ontology term (in CURIE form) |
| [inputsource_external_ref](inputsource_external_ref.md) | Reference to an external entity as the input source, using a globally unique ... |
| [inputsource_ref](inputsource_ref.md) | Reference to an internal object as the input source using a local identifier |
| [instrument](instrument.md) | Technology platform used to perform nucleic acid sequencing, including name a... |
| [key](key.md) | Key/name of the assessment value |
| [label](label.md) | Human-readable label associated to the term id in the current version of the ... |
| [lengths_constant](lengths_constant.md) | Whether the sequence lengths are constant (all sequence features have the sam... |
| [library_layout](library_layout.md) | Whether the library was built as paired-end, or single-end |
| [mime_type](mime_type.md) | A string providing the mime-type of the data file |
| [molecule_type](molecule_type.md) | Specifies the type of source material that is being sequenced |
| [name](name.md) | Name of the person or organisation |
| [namespace](namespace.md) | The CURIE namespace (prefix) an ontology (e |
| [ontology_url](ontology_url.md) | The version-agnostic URL of the ontology (e |
| [organism_tissue](organism_tissue.md) | Part of organism (typically tissue or organ) from which the biospecimen/sampl... |
| [other_biospecimen](other_biospecimen.md) | Other biospecimen-related terms that can be used to further classify the bios... |
| [phenotype](phenotype.md) | Main phenotype (e |
| [qualified_relation](qualified_relation.md) | A description of the relationship with the input source |
| [quality_assessments](quality_assessments.md) | An array of QualityAssessment objects containing the main quality scores from... |
| [region](region.md) | Name of the region in the cloud service provider that the object belongs to |
| [run_provenance](run_provenance.md) | Document detailing the provenance of the experiment or analysis run which pro... |
| [sample_collection_date](sample_collection_date.md) | Date of sample collection |
| [sample_collection_location](sample_collection_location.md) | Geographical location where the sample was collected |
| [sample_description](sample_description.md) | Human-readable description of the biospecimen/sample and the sampling process |
| [sample_external_id](sample_external_id.md) | External, globally unique identifier for the biospecimen/sample |
| [sample_id](sample_id.md) | Internal identifier for the biospecimen/sample (unique within the metadata de... |
| [sample_label](sample_label.md) | A human-readable description of the sample, short enough to be used for listi... |
| [samples](samples.md) | Information about the biospecimens/samples used as raw material for lab exper... |
| [sampling_protocol](sampling_protocol.md) | Protocol detailing the collection and treatment of the biospecimen/sample |
| [seqcol_digest](seqcol_digest.md) | Top-level sequence collection digest according to the GA4GH refget, Sequence ... |
| [seqcol_ordered_coord_system](seqcol_ordered_coord_system.md) | Content-derived digest that uniquely identifies the ordered coordinate system... |
| [seqcol_unordered_coord_system](seqcol_unordered_coord_system.md) | Content-derived digest that uniquely identifies the order-invariant coordinat... |
| [sequence_features](sequence_features.md) | List of sequence features described by the genomic annotation file |
| [sequencing_protocol](sequencing_protocol.md) | Set of rules which guides how the sequencing protocol was followed |
| [sex](sex.md) | Biological sex of the donor/organism |
| [species_taxon](species_taxon.md) | Taxonomical classification of the species of the donor/organism |
| [technical_replicate_labels](technical_replicate_labels.md) | Labels denoting the technical replicates within which the relation is defined... |
| [track_geometry](track_geometry.md) | Geometric properties of the sequence features in the genomic annotation file ... |
| [updated_time](updated_time.md) | Timestamp of content update in RFC3339, identical to created_time in systems ... |
| [url](url.md) | A fully resolvable URL that can be used to fetch the actual object bytes |
| [value](value.md) | Value corresponding to the assessment key |
| [value_type](value_type.md) | The type of values associated with the sequence features, if any |
| [version](version.md) | Version information for the retrieval from the input source |
| [versioned_ontology_url](versioned_ontology_url.md) | The versioned URL of the ontology (e |


## Enumerations

| Enumeration | Description |
| --- | --- |
| [AccessMethods](AccessMethods.md) | Access methods (i |
| [BiospecimenClassification](BiospecimenClassification.md) | Vocabulary from the ENCODE model describing the general category of boispecim... |
| [DataTypes](DataTypes.md) | Types of data values associated with sequence features or edges |
| [OutputType](OutputType.md) | Vocabulary from the ENCODE model describing the purpose or content of a file ... |


## Types

| Type | Description |
| --- | --- |
| [Boolean](Boolean.md) | A binary (true or false) value |
| [Curie](Curie.md) | a compact URI |
| [Date](Date.md) | a date (year, month and day) in an idealized calendar |
| [DateOrDatetime](DateOrDatetime.md) | Either a date or a datetime |
| [Datetime](Datetime.md) | The combination of a date and time |
| [Decimal](Decimal.md) | A real number with arbitrary precision that conforms to the xsd:decimal speci... |
| [Double](Double.md) | A real number that conforms to the xsd:double specification |
| [Float](Float.md) | A real number that conforms to the xsd:float specification |
| [Integer](Integer.md) | An integer |
| [Jsonpath](Jsonpath.md) | A string encoding a JSON Path |
| [Jsonpointer](Jsonpointer.md) | A string encoding a JSON Pointer |
| [Ncname](Ncname.md) | Prefix part of CURIE |
| [Nodeidentifier](Nodeidentifier.md) | A URI, CURIE or BNODE that represents a node in a model |
| [Objectidentifier](Objectidentifier.md) | A URI or CURIE that represents an object in the model |
| [Sparqlpath](Sparqlpath.md) | A string encoding a SPARQL Property Path |
| [String](String.md) | A character string |
| [Time](Time.md) | A time object represents a (local) time of day, independent of any particular... |
| [Uri](Uri.md) | a complete URI |
| [Uriorcurie](Uriorcurie.md) | a URI or a CURIE |


## Subsets

| Subset | Description |
| --- | --- |
