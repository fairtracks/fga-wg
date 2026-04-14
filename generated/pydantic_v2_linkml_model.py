from __future__ import annotations

import re
import sys
from datetime import (
    date,
    datetime,
    time
)
from decimal import Decimal
from enum import Enum
from typing import (
    Any,
    ClassVar,
    Literal,
    Optional,
    Union
)

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    RootModel,
    SerializationInfo,
    SerializerFunctionWrapHandler,
    field_validator,
    model_serializer
)


metamodel_version = "1.7.0"
version = "None"


class ConfiguredBaseModel(BaseModel):
    model_config = ConfigDict(
        serialize_by_alias = True,
        validate_by_name = True,
        validate_assignment = True,
        validate_default = True,
        extra = "forbid",
        arbitrary_types_allowed = True,
        use_enum_values = True,
        strict = False,
    )





class LinkMLMeta(RootModel):
    root: dict[str, Any] = {}
    model_config = ConfigDict(frozen=True)

    def __getattr__(self, key:str):
        return getattr(self.root, key)

    def __getitem__(self, key:str):
        return self.root[key]

    def __setitem__(self, key:str, value):
        self.root[key] = value

    def __contains__(self, key:str) -> bool:
        return key in self.root


linkml_meta = LinkMLMeta({'default_prefix': 'https://w3id.org/fga-wg/schema/bundle/',
     'id': 'https://w3id.org/fga-wg/schema/bundle',
     'imports': ['linkml:types',
                 'BundleMetadata',
                 'Analysis',
                 'Donor',
                 'Experiment',
                 'File',
                 'FileCollection',
                 'GenomicAnnotationFile',
                 'Sample',
                 'Study'],
     'name': 'Bundle',
     'prefixes': {'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'}},
     'source_file': 'src/schema/Bundle.yaml'} )

class OutputType(str, Enum):
    """
    Vocabulary from the ENCODE model describing the purpose or content of a file (see "Properties->output_type" in https://www.encodeproject.org/profiles/file).
    """
    number_3D_structure = "3D structure"
    alignments = "alignments"
    alignments_with_modifications = "alignments with modifications"
    allele_specific_contact_matrix = "allele-specific contact matrix"
    allele_specific_variants = "allele-specific variants"
    archr_project = "archr project"
    bias_models = "bias models"
    bias_corrected_predicted_signal_profile = "bias-corrected predicted signal profile"
    bidirectional_peaks = "bidirectional peaks"
    candidate_Cis_Regulatory_Elements = "candidate Cis-Regulatory Elements"
    candidate_enhancers = "candidate enhancers"
    candidate_promoters = "candidate promoters"
    capture_targets = "capture targets"
    cell_coordinates = "cell coordinates"
    cell_topic_participation = "cell topic participation"
    cell_type_data = "cell type data"
    cell_type_annotations = "cell type annotations"
    chromatin_stripes = "chromatin stripes"
    chromosomes_reference = "chromosomes reference"
    chromosome_sizes = "chromosome sizes"
    contact_domains = "contact domains"
    contact_matrix = "contact matrix"
    consensus_DNase_hypersensitivity_sites = "consensus DNase hypersensitivity sites"
    curated_binding_sites = "curated binding sites"
    curated_SNVs = "curated SNVs"
    mapping_quality_thresholded_contact_matrix = "mapping quality thresholded contact matrix"
    conservative_IDR_thresholded_peaks = "conservative IDR thresholded peaks"
    control_normalized_signal = "control normalized signal"
    counts_sequence_contribution_scores = "counts sequence contribution scores"
    CpG_sites_coverage = "CpG sites coverage"
    depth_normalized_signals_matrix = "depth normalized signals matrix"
    fold_over_change_matrix = "fold over change matrix"
    DHS_peaks = "DHS peaks"
    DHS_regions_reference = "DHS regions reference"
    nuclease_cleavage_frequency = "nuclease cleavage frequency"
    differential_expression_quantifications = "differential expression quantifications"
    differential_splicing_quantifications = "differential splicing quantifications"
    diploid_personal_genome_alignments = "diploid personal genome alignments"
    divergent_peaks = "divergent peaks"
    DNN_MPRA_contribution_scores = "DNN-MPRA contribution scores"
    DNN_MPRA_predicted_signal = "DNN-MPRA predicted signal"
    dsQTLs = "dsQTLs"
    element_barcode_mapping = "element barcode mapping"
    elements_reference = "elements reference"
    element_gene_interactions_p_value = "element gene interactions p-value"
    element_gene_interactions_signal = "element gene interactions signal"
    element_gene_links = "element gene links"
    enhancer_gene_links = "enhancer-gene links"
    thresholded_links = "thresholded links"
    element_quantifications = "element quantifications"
    enhancer_prediction_model = "enhancer prediction model"
    enhancer_validation = "enhancer validation"
    enrichment = "enrichment"
    enhancers_reference = "enhancers reference"
    eQTLs = "eQTLs"
    exon_quantifications = "exon quantifications"
    exclusion_list_regions = "exclusion list regions"
    FDR_cut_rate = "FDR cut rate"
    female_genome_index = "female genome index"
    female_genome_reference = "female genome reference"
    filtered_indels = "filtered indels"
    filtered_peaks = "filtered peaks"
    filtered_reads = "filtered reads"
    filtered_regions = "filtered regions"
    filtered_SNPs = "filtered SNPs"
    fine_mapped_variants = "fine-mapped variants"
    fold_change_over_control = "fold change over control"
    footprints = "footprints"
    functional_conservation_mapping = "functional conservation mapping"
    functional_conservation_quantifications = "functional conservation quantifications"
    fragments = "fragments"
    gene_alignments = "gene alignments"
    gene_quantifications = "gene quantifications"
    gene_stabilities = "gene stabilities"
    genic_features_quantifications = "genic features quantifications"
    genic_regions_quantifications = "genic regions quantifications"
    genome_compartments = "genome compartments"
    genome_index = "genome index"
    genome_reference = "genome reference"
    genome_subcompartments = "genome subcompartments"
    gRNAs = "gRNAs"
    guide_locations = "guide locations"
    guide_quantifications = "guide quantifications"
    haplotype_specific_alignments = "haplotype-specific alignments"
    haplotype_specific_contact_matrix = "haplotype-specific contact matrix"
    haplotype_specific_nuclease_cleavage_frequency = "haplotype-specific nuclease cleavage frequency"
    haplotype_specific_nuclease_cleavage_corrected_frequency = "haplotype-specific nuclease cleavage corrected frequency"
    hotspots = "hotspots"
    hotspots1_reference = "hotspots1 reference"
    hotspots2_reference = "hotspots2 reference"
    idat_green_channel = "idat green channel"
    idat_red_channel = "idat red channel"
    inclusion_list = "inclusion list"
    index_reads = "index reads"
    intensity_values = "intensity values"
    IDR_ranked_peaks = "IDR ranked peaks"
    IDR_thresholded_peaks = "IDR thresholded peaks"
    kmer_weights = "kmer weights"
    library_fraction = "library fraction"
    loops = "loops"
    male_genome_index = "male genome index"
    male_genome_reference = "male genome reference"
    maternal_haplotype_mapping = "maternal haplotype mapping"
    maternal_variant_calls = "maternal variant calls"
    merged_transcription_segment_quantifications = "merged transcription segment quantifications"
    methylated_reads = "methylated reads"
    methylation_state_at_CHG = "methylation state at CHG"
    methylation_state_at_CHH = "methylation state at CHH"
    methylation_state_at_CpG = "methylation state at CpG"
    microRNA_quantifications = "microRNA quantifications"
    miRNA_annotations = "miRNA annotations"
    minus_strand_end_position_signal = "minus strand end position signal"
    minus_strand_inosine_methylation_state = "minus strand inosine methylation state"
    minus_strand_m5C_methylation_state = "minus strand m5C methylation state"
    minus_strand_m6A_methylation_state = "minus strand m6A methylation state"
    minus_strand_methylation_state_at_CpG = "minus strand methylation state at CpG"
    minus_strand_Nm_methylation_state = "minus strand Nm methylation state"
    minus_strand_normalized_end_position_signal = "minus strand normalized end position signal"
    minus_strand_pseudouridine_methylation_state = "minus strand pseudouridine methylation state"
    minus_strand_signal_of_all_reads = "minus strand signal of all reads"
    minus_strand_signal_of_unique_reads = "minus strand signal of unique reads"
    mitochondrial_exclusion_list_regions = "mitochondrial exclusion list regions"
    mitochondrial_genome_index = "mitochondrial genome index"
    mitochondrial_genome_reference = "mitochondrial genome reference"
    model_performance_metrics = "model performance metrics"
    models = "models"
    motif_clusters_reference = "motif clusters reference"
    motif_model = "motif model"
    mRNA_stabilities = "mRNA stabilities"
    nanopore_signal = "nanopore signal"
    negative_control_regions = "negative control regions"
    nested_contact_domains = "nested contact domains"
    non_targeting_gRNAs = "non-targeting gRNAs"
    normalized_bias_corrected_predicted_signal_profile = "normalized bias-corrected predicted signal profile"
    normalized_signal_of_all_reads = "normalized signal of all reads"
    normalized_observed_signal_profile = "normalized observed signal profile"
    normalized_observed_signal_profile_LEFT_PARENTHESISminus_strandRIGHT_PARENTHESIS = "normalized observed signal profile (minus strand)"
    normalized_observed_signal_profile_LEFT_PARENTHESISplus_strandRIGHT_PARENTHESIS = "normalized observed signal profile (plus strand)"
    normalized_predicted_bias_profile = "normalized predicted bias profile"
    normalized_predicted_signal_profile = "normalized predicted signal profile"
    normalized_predicted_signal_profile_LEFT_PARENTHESISminus_strandRIGHT_PARENTHESIS = "normalized predicted signal profile (minus strand)"
    normalized_predicted_signal_profile_LEFT_PARENTHESISplus_strandRIGHT_PARENTHESIS = "normalized predicted signal profile (plus strand)"
    novel_peptides = "novel peptides"
    observed_bias_profile = "observed bias profile"
    observed_control_profile_LEFT_PARENTHESISminus_strandRIGHT_PARENTHESIS = "observed control profile (minus strand)"
    observed_control_profile_LEFT_PARENTHESISplus_strandRIGHT_PARENTHESIS = "observed control profile (plus strand)"
    observed_signal_profile = "observed signal profile"
    observed_signal_profile_LEFT_PARENTHESISminus_strandRIGHT_PARENTHESIS = "observed signal profile (minus strand)"
    observed_signal_profile_LEFT_PARENTHESISplus_strandRIGHT_PARENTHESIS = "observed signal profile (plus strand)"
    open_chromatin_regions = "open chromatin regions"
    optimal_IDR_thresholded_peaks = "optimal IDR thresholded peaks"
    pairs = "pairs"
    paternal_haplotype_mapping = "paternal haplotype mapping"
    paternal_variant_calls = "paternal variant calls"
    peaks = "peaks"
    peaks_and_background_as_input_for_IDR = "peaks and background as input for IDR"
    peptide_quantifications = "peptide quantifications"
    personalized_genome_assembly = "personalized genome assembly"
    perturbation_signal = "perturbation signal"
    phastcons_score_reference = "phastcons score reference"
    phased_mapping = "phased mapping"
    phased_variant_calls = "phased variant calls"
    plus_strand_end_position_signal = "plus strand end position signal"
    plus_strand_inosine_methylation_state = "plus strand inosine methylation state"
    plus_strand_m5C_methylation_state = "plus strand m5C methylation state"
    plus_strand_m6A_methylation_state = "plus strand m6A methylation state"
    plus_strand_methylation_state_at_CpG = "plus strand methylation state at CpG"
    plus_strand_Nm_methylation_state = "plus strand Nm methylation state"
    plus_strand_normalized_end_position_signal = "plus strand normalized end position signal"
    plus_strand_pseudouridine_methylation_state = "plus strand pseudouridine methylation state"
    plus_strand_signal_of_all_reads = "plus strand signal of all reads"
    plus_strand_signal_of_unique_reads = "plus strand signal of unique reads"
    polyA_sites = "polyA sites"
    positive_control_regions = "positive control regions"
    predicted_bias_profile = "predicted bias profile"
    predicted_enhancers = "predicted enhancers"
    predicted_signal_profile = "predicted signal profile"
    predicted_signal_profile_LEFT_PARENTHESISminus_strandRIGHT_PARENTHESIS = "predicted signal profile (minus strand)"
    predicted_signal_profile_LEFT_PARENTHESISplus_strandRIGHT_PARENTHESIS = "predicted signal profile (plus strand)"
    predicted_3D_structural_ensembles = "predicted 3D structural ensembles"
    preprocessed_alignments = "preprocessed alignments"
    profile_sequence_contribution_scores = "profile sequence contribution scores"
    promoter_prediction_model = "promoter prediction model"
    promoters_reference = "promoters reference"
    protein_expression_quantifications = "protein expression quantifications"
    pseudoreplicated_peaks = "pseudoreplicated peaks"
    pseudoreplicated_IDR_thresholded_peaks = "pseudoreplicated IDR thresholded peaks"
    PWMs = "PWMs"
    R2C2_subreads = "R2C2 subreads"
    raw_imaging_signal = "raw imaging signal"
    raw_minus_strand_signal = "raw minus strand signal"
    raw_normalized_signal = "raw normalized signal"
    raw_plus_strand_signal = "raw plus strand signal"
    raw_signal = "raw signal"
    ranked_gRNAs = "ranked gRNAs"
    read_depth_normalized_signal = "read-depth normalized signal"
    read_annotations = "read annotations"
    reads = "reads"
    repeat_elements_annotation = "repeat elements annotation"
    repeats_reference = "repeats reference"
    reference_variants = "reference variants"
    regulatory_elements = "regulatory elements"
    relative_replication_signal = "relative replication signal"
    replicated_peaks = "replicated peaks"
    replication_timing_profile = "replication timing profile"
    reporter_code_counts = "reporter code counts"
    representative_DNase_hypersensitivity_sites = "representative DNase hypersensitivity sites"
    representative_IDR_thresholded_peaks = "representative IDR thresholded peaks"
    restriction_enzyme_site_locations = "restriction enzyme site locations"
    RNA_binding_protein_associated_mRNAs = "RNA-binding protein associated mRNAs"
    rRNA_reference = "rRNA reference"
    safe_targeting_gRNAs = "safe-targeting gRNAs"
    scaled_RNA_stability = "scaled RNA stability"
    selected_regions_for_bias_corrected_predicted_signal_profile = "selected regions for bias-corrected predicted signal profile"
    selected_regions_for_count_sequence_contribution_scores = "selected regions for count sequence contribution scores"
    selected_regions_for_predicted_bias_profile = "selected regions for predicted bias profile"
    selected_regions_for_predicted_signal_and_sequence_contribution_scores = "selected regions for predicted signal and sequence contribution scores"
    selected_regions_for_predicted_signal_profile = "selected regions for predicted signal profile"
    selected_regions_for_predicted_signal_profile_LEFT_PARENTHESISminus_strandRIGHT_PARENTHESIS = "selected regions for predicted signal profile (minus strand)"
    selected_regions_for_predicted_signal_profile_LEFT_PARENTHESISplus_strandRIGHT_PARENTHESIS = "selected regions for predicted signal profile (plus strand)"
    selected_regions_for_profile_sequence_contribution_scores = "selected regions for profile sequence contribution scores"
    semi_automated_genome_annotation = "semi-automated genome annotation"
    sequence_adapters = "sequence adapters"
    sequence_barcodes = "sequence barcodes"
    sequence_motifs_report = "sequence motifs report"
    sequence_motifs = "sequence motifs"
    sequence_motifs_instances = "sequence motifs instances"
    signal_of_all_reads = "signal of all reads"
    signal_of_unique_reads = "signal of unique reads"
    signal_p_value = "signal p-value"
    spike_ins = "spike-ins"
    smoothed_methylation_state_at_CpG = "smoothed methylation state at CpG"
    sparse_gene_count_matrix = "sparse gene count matrix"
    sparse_gene_count_matrix_of_all_reads = "sparse gene count matrix of all reads"
    sparse_gene_count_matrix_of_unique_reads = "sparse gene count matrix of unique reads"
    sparse_gRNA_count_matrix = "sparse gRNA count matrix"
    sparse_peak_count_matrix = "sparse peak count matrix"
    sparse_transcript_count_matrix = "sparse transcript count matrix"
    splice_junctions = "splice junctions"
    subreads = "subreads"
    TF_binding_prediction_model = "TF binding prediction model"
    TF_peaks_matrix = "TF peaks matrix"
    thresholded_element_gene_links = "thresholded element gene links"
    topic_gene_weights = "topic gene weights"
    training_and_test_regions = "training and test regions"
    training_set = "training set"
    transcribed_region_quantifications = "transcribed region quantifications"
    transcript_quantifications = "transcript quantifications"
    transcription_start_sites = "transcription start sites"
    transcription_segment_quantifications = "transcription segment quantifications"
    transcriptome_alignments = "transcriptome alignments"
    transcriptome_annotations = "transcriptome annotations"
    transcriptome_index = "transcriptome index"
    transcriptome_reference = "transcriptome reference"
    transposable_element_TF_ancestral_origin_percent_by_motif = "transposable element TF ancestral origin percent by motif"
    transposable_element_TF_ancestral_origin_percent_by_subfamily = "transposable element TF ancestral origin percent by subfamily"
    TSS_reference = "TSS reference"
    unfiltered_alignments = "unfiltered alignments"
    unfiltered_sparse_gene_count_matrix_of_all_reads = "unfiltered sparse gene count matrix of all reads"
    unfiltered_sparse_gene_count_matrix_of_unique_reads = "unfiltered sparse gene count matrix of unique reads"
    unfiltered_sparse_splice_junction_count_matrix_of_unique_reads = "unfiltered sparse splice junction count matrix of unique reads"
    unidirectional_peaks = "unidirectional peaks"
    UV_enriched_segment_quantifications = "UV enriched segment quantifications"
    variant_calls = "variant calls"
    variant_effect_quantifications = "variant effect quantifications"
    variant_reference = "variant reference"
    variants_contact_matrix = "variants contact matrix"
    variant_functional_prediction = "variant functional prediction"
    z_scores_matrix = "z scores matrix"


class AccessMethods(str, Enum):
    """
    Access methods (i.e. communication protocols), following the vocabulary defined in the GA4GH DRS specification (https://ga4gh.github.io/data-repository-service-schemas/preview/release/drs-1.4.0/docs/#tag/AccessMethodModel/operation/getAccessMethod).
    """
    s3 = "s3"
    """
    Amazon S3 and other S3-compatible bucket.
    """
    gs = "gs"
    """
    Google Cloud Storage (and compatible) bucket.
    """
    ftp = "ftp"
    """
    File Transfer Protocol.
    """
    gsiftp = "gsiftp"
    """
    GridFTP protocol (an extension of the File Transfer Protocol (FTP) for grid computing).
    """
    globus = "globus"
    """
    Data transfer via the Globus research cyberinfrastructure (https://www.globus.org/.)
    """
    htsget = "htsget"
    """
    GA4GH HTSget standard for retrieving subsections of genomic data (https://www.ga4gh.org/product/htsget/).
    """
    https = "https"
    """
    Hypertext Transfer Protocol Secure, the standard encrypted protocol used on the web.
    """
    file = "file"
    """
    For local files accessible via a file URI (e.g., file://path/to/file).
    """


class DataTypes(str, Enum):
    """
    Types of data values associated with sequence features or edges.
    """
    integer = "integer"
    """
    Integer numeric values.
    """
    decimal = "decimal"
    """
    Decimal numeric values.
    """
    boolean = "boolean"
    """
    Boolean values (true/false).
    """
    string = "string"
    """
    Text string values.
    """
    multiple = "multiple"
    """
    Multiple types of values are associated (e.g. both integer and string).
    """


class BiospecimenClassification(str, Enum):
    """
    Vocabulary from the ENCODE model describing the general category of boispecimen (see "Properties->classification" in https://www.encodeproject.org/profiles/biosample_type).
    """
    cell_line = "cell line"
    in_vitro_differentiated_cells = "in vitro differentiated cells"
    primary_cell = "primary cell"
    cell_free_sample = "cell-free sample"
    cloning_host = "cloning host"
    tissue = "tissue"
    whole_organisms = "whole organisms"
    organoid = "organoid"
    technical_sample = "technical sample"



class Deposit(ConfiguredBaseModel):
    """
    Information about a public deposit of a document containing metadata about a set of genome annotation files.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/fga-wg/schema/deposit'})

    deposit_id: Optional[str] = Field(default=None, description="""A globally unique and persistent identifier for the public deposit of the metadata document. A DOI or other persistent identifier is recommended.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Deposit'],
         'examples': [{'value': 'doi:10.1234/zenodo.12345678'}]} })
    deposit_versioned_id: str = Field(default=..., description="""A globally unique, persistent and versioned identifier for the public deposit of the metadata document. A versioned DOI to a deposited document is recommended.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Deposit'],
         'examples': [{'value': 'doi:10.1234/zenodo.12345679'}]} })
    deposit_first_created: datetime  = Field(default=..., description="""The date and time of the creation of the first deposited version of the metadata document.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Deposit'], 'examples': [{'value': '2025-07-01T12:36:00Z'}]} })
    deposit_last_changed: datetime  = Field(default=..., description="""The date and time of the last deposited change of the current metadata document (corresponding to \"deposit_versioned_id\").""", json_schema_extra = { "linkml_meta": {'domain_of': ['Deposit'], 'examples': [{'value': '2025-07-01T12:36:00Z'}]} })


class InputSource(ConfiguredBaseModel):
    """
    General object representing the source of data files, samples, or other entities used as input to a process or a result. An input source refering to a single file or sample object will represent that item only, while an input source referring to a container or process may represent a number of disctinct input items. InputSource also contains information about the type of relationship, replication labelling, versioning and retrieval date.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/fga-wg/schema/input-source',
         'rules': [{'postconditions': {'exactly_one_of': [{'slot_conditions': {'inputsource_external_ref': {'name': 'inputsource_external_ref',
                                                                                                            'required': True}}},
                                                          {'slot_conditions': {'inputsource_ref': {'name': 'inputsource_ref',
                                                                                                   'required': True}}}]},
                    'preconditions': {'slot_conditions': {'qualified_relation': {'name': 'qualified_relation',
                                                                                 'value_presence': 'PRESENT'}}}}]})

    inputsource_external_ref: Optional[str] = Field(default=None, description="""Reference to an external entity as the input source, using a globally unique identifier or an URL. External references will in most cases refer to a database, data record, data file, website or other data source. One of \"inputsource_external_ref\" or \"inputsource_ref\" must be specified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InputSource'],
         'examples': [{'value': 'https://www.encodeproject.org/files/GRCh38_no_alt_analysis_set_GCA_000001405.15'}]} })
    inputsource_ref: Optional[str] = Field(default=None, description="""Reference to an internal object as the input source using a local identifier. Entities to be used as an internal input source includes FileCollection, Sample, Experiment, Analysis or File as restricted by the description of the field where the input source is used. One of \"inputsource_external_ref\" or \"inputsource_ref\" must be specified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InputSource']} })
    database_accessions: Optional[list[str]] = Field(default=None, description="""Accession numbers for database records used as input source. Used in connection with \"inputsource_external_ref\".""", json_schema_extra = { "linkml_meta": {'any_of': [{'range': 'string'}, {'range': 'curie'}],
         'domain_of': ['InputSource']} })
    qualified_relation: str = Field(default=..., description="""A description of the relationship with the input source.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InputSource'],
         'examples': [{'value': 'bioschemas:FormalParameter'}]} })
    biological_replicate_labels: Optional[list[str]] = Field(default=None, description="""Labels denoting the biological replicates within which the relation is defined, if any.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InputSource'], 'examples': [{'value': '1'}, {'value': '2'}]} })
    technical_replicate_labels: Optional[list[str]] = Field(default=None, description="""Labels denoting the technical replicates within which the relation is defined, if any.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InputSource'], 'examples': [{'value': '1_1'}, {'value': '1_2'}]} })
    version: Optional[str] = Field(default=None, description="""Version information for the retrieval from the input source.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InputSource']} })
    date_of_retrieval: Optional[date] = Field(default=None, description="""Date of retrieval from the input source, typically used to timestamp downloading data from a database or URL.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InputSource'], 'examples': [{'value': '2016-04-19'}]} })


class BundleMetadata(ConfiguredBaseModel):
    """
    Top-level metadata about a bundle representing a set of genome annotation files, harmonised according to the \"FAIRification of Genomic Annotations\" data model.  This includes self-referential identifiers and versioning of public deposits of the harmonized metadata.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/fga-wg/schema/bundle_metadata'})

    bundle_label: str = Field(default=..., description="""A human-readable description of the bundle, short enough to be used for listings within software user interfaces, tables, illustration legends, etc.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BundleMetadata'],
         'examples': [{'value': 'IHEC data portal metadata, harmonised to the FGA-WG '
                                'model.'}]} })
    bundle_description: Optional[str] = Field(default=None, description="""Human-readable description of the bundle.""", json_schema_extra = { "linkml_meta": {'any_of': [{'range': 'string'}, {'range': 'uri'}],
         'domain_of': ['BundleMetadata'],
         'examples': [{'value': 'The metadata contents of the International Human '
                                'Epigenome Consortium (IHEC) data portal, harmonised '
                                'to follow the metadata model developed by the '
                                '"FAIRification of Genomic Annotations WG" in the '
                                'Research Data Alliance (RDA), enhanced with metadata '
                                'from original sources.'}]} })
    bundle_deposit: Optional[Deposit] = Field(default=None, description="""Information about the public deposit of the bundle.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BundleMetadata'],
         'examples': [{'object': {'deposit_first_created': '2025-07-01T12:36:00Z',
                                  'deposit_id': 'doi:10.1234/zenodo.12345678',
                                  'deposit_last_changed': '2025-07-01T12:36:00Z',
                                  'deposit_versioned_id': 'doi:10.1234/zenodo.12345679'}}]} })
    bundle_input_sources: Optional[list[InputSource]] = Field(default=None, description="""References to other input sources from which this entire bundle was derived, or possibly including DOIs of other bundles used as source.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BundleMetadata'],
         'examples': [{'object': {'inputsource_external_ref': 'https://epigenomesportal.ca/ihec/',
                                  'qualified_relation': 'prov:wasDerivedFrom'}}]} })
    bundle_ontology_versions: list[OntologyVersions] = Field(default=..., description="""Map from the version-agnostic URL to a versioned URL (e.g. \"versionIRI\" in owl) of each ontology used in the current metadata deposit (corresponding to deposit_versioned_id\").""", json_schema_extra = { "linkml_meta": {'domain_of': ['BundleMetadata'],
         'examples': [{'object': {'namespace': 'edam',
                                  'ontology_url': 'http://edamontology.org/EDAM.owl',
                                  'versioned_ontology_url': 'http://edamontology.org/EDAM_1.21.owl'}},
                      {'object': {'namespace': 'cl',
                                  'ontology_url': 'http://purl.obolibrary.org/obo/cl.owl',
                                  'versioned_ontology_url': 'http://purl.obolibrary.org/obo/cl/releases/2020-05-21/cl.owl'}},
                      {'object': {'namespace': 'efo',
                                  'ontology_url': 'http://www.ebi.ac.uk/efo/efo.owl',
                                  'versioned_ontology_url': 'http://www.ebi.ac.uk/efo/releases/v3.21.0/efo.owl'}},
                      {'object': {'namespace': 'ncit',
                                  'ontology_url': 'http://purl.obolibrary.org/obo/ncit.owl',
                                  'versioned_ontology_url': 'http://purl.obolibrary.org/obo/ncit/releases/2020-07-17/ncit.owl'}},
                      {'object': {'namespace': 'obi',
                                  'ontology_url': 'http://purl.obolibrary.org/obo/obi.owl',
                                  'versioned_ontology_url': 'http://purl.obolibrary.org/obo/obi/2020-04-23/obi.owl'}},
                      {'object': {'namespace': 'so',
                                  'ontology_url': 'http://purl.obolibrary.org/obo/so.owl',
                                  'versioned_ontology_url': 'http://purl.obolibrary.org/obo/so/2020-08-20/so.owl'}},
                      {'object': {'namespace': 'uberon',
                                  'ontology_url': 'http://purl.obolibrary.org/obo/uberon.owl',
                                  'versioned_ontology_url': 'http://purl.obolibrary.org/obo/uberon/releases/2020-06-30/uberon.owl'}}]} })

    @field_validator('bundle_label')
    def pattern_bundle_label(cls, v):
        pattern=re.compile(r"^.{1,60}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid bundle_label format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid bundle_label format: {v}"
            raise ValueError(err_msg)
        return v


class OntologyVersions(ConfiguredBaseModel):
    """
    Information about an ontology used for the bundle.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/fga-wg/schema/bundle_metadata'})

    namespace: str = Field(default=..., description="""The CURIE namespace (prefix) an ontology (e.g. \"GO\" for Gene Ontology).""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyVersions'], 'examples': [{'value': 'edam'}]} })
    ontology_url: str = Field(default=..., description="""The version-agnostic URL of the ontology (e.g. the IRI of the ontology in OWL).""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyVersions'],
         'examples': [{'value': 'http://edamontology.org/EDAM.owl'}]} })
    versioned_ontology_url: str = Field(default=..., description="""The versioned URL of the ontology (e.g. the \"versionIRI\" in OWL).""", json_schema_extra = { "linkml_meta": {'domain_of': ['OntologyVersions'],
         'examples': [{'value': 'http://edamontology.org/EDAM_1.21.owl'}]} })


class Term(ConfiguredBaseModel):
    """
    Helper entity to represent an ontology term as a data value. 
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/fga-wg/schema/term'})

    id: str = Field(default=..., description="""External, globally unique identifier for the ontology term (in CURIE form).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Term'], 'examples': [{'value': 'obi:OBI_0000716'}]} })
    label: Optional[str] = Field(default=None, description="""Human-readable label associated to the term id in the current version of the ontology (as listed in the \"ontology_versions\" field of the Deposit object).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Term'], 'examples': [{'value': 'ChIP-seq assay'}]} })


class Analysis(ConfiguredBaseModel):
    """
    Represents the computational processing applied to data from a sequencing experiment, or from another analysis. This can be described at the level of individual analysis steps in a workflow/pipeline, or more generally for the workflow/pipeline as a whole.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/fga-wg/schema/analysis'})

    analysis_external_id: Optional[str] = Field(default=None, description="""External, globally unique identifier for the experiment.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Analysis'], 'examples': [{'value': 'encode:ENCAN718KHT'}]} })
    analysis_id: str = Field(default=..., description="""Internal identifier for the experiment (unique within the metadata deposit). """, json_schema_extra = { "linkml_meta": {'domain_of': ['Analysis'], 'examples': [{'value': 'analysis:ENCAN718KHT'}]} })
    analysis_label: str = Field(default=..., description="""A human-readable description of the analysis, short enough to be used for listings within software user interfaces, tables, illustration legends, etc.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Analysis'],
         'examples': [{'value': 'ENCODE3 ChIP-seq pipeline, GRCH38, replicated peak '
                                'calling'}]} })
    analysis_description: Optional[str] = Field(default=None, description="""Human-readable description of the analysis.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Analysis'],
         'examples': [{'value': 'ENCODE3 ChIP-seq pipeline on GRCH38 with replicated '
                                'peak calling using MACS.'}]} })
    analysis_study_ref: Optional[str] = Field(default=None, description="""Internal reference to the study within which the analysis has been carried out.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Analysis'], 'examples': [{'value': 'study:S-EPMC7391744'}]} })
    analysis_input_sources: list[InputSource] = Field(default=..., description="""External or internal references to sources for the input data analyzed. Internal references should lead to FileCollection, File, Experiment, or Analysis objects.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Analysis'],
         'examples': [{'object': {'biological_replicate_labels': ['1', '2'],
                                  'inputsource_ref': 'experiment:ENCSR000DPJ',
                                  'qualified_relation': 'prov:wasInformedBy',
                                  'technical_replicate_labels': ['1_1', '2_1']}},
                      {'object': {'biological_replicate_labels': ['1', '2'],
                                  'date_of_retrieval': '2016-04-19',
                                  'inputsource_external_ref': 'https://www.encodeproject.org/files/GRCh38_no_alt_analysis_set_GCA_000001405.15',
                                  'qualified_relation': 'https://bioschemas.org/FormalParameter',
                                  'technical_replicate_labels': ['1_1', '2_1']}}]} })
    analysis_type: Term = Field(default=..., description="""The type of analysis carried out.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Analysis'],
         'examples': [{'object': {'id': 'edam:operation_3222',
                                  'label': 'Peak calling'}}]} })
    analysis_main_tool: Optional[str] = Field(default=None, description="""Main software tool used for the analysis.""", json_schema_extra = { "linkml_meta": {'any_of': [{'range': 'string'}, {'range': 'curie'}],
         'domain_of': ['Analysis'],
         'examples': [{'value': 'biotools:macs'}]} })
    analysis_main_tool_version: Optional[str] = Field(default=None, description="""Version of the main software tool used for the analysis.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Analysis'], 'examples': [{'value': '2.10'}]} })
    analysis_protocol: Optional[str] = Field(default=None, description="""Document describing the analysis protocol that was followed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Analysis'],
         'examples': [{'value': 'https://www.encodeproject.org/documents/7009beb8-340b-4e71-b9db-53bb020c7fe2/@@download/attachment/ChIP-seq_pipeline_overview.pdf'}]} })
    analysis_workflow: Optional[str] = Field(default=None, description="""External reference to the analysis workflow, with availability in at least one machine-operable form (e.g. CWL, Nextflow, ...).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Analysis'], 'examples': [{'value': 'encode:ENCPL272XAE'}]} })

    @field_validator('analysis_label')
    def pattern_analysis_label(cls, v):
        pattern=re.compile(r"^.{1,60}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid analysis_label format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid analysis_label format: {v}"
            raise ValueError(err_msg)
        return v


class Donor(ConfiguredBaseModel):
    """
    Information about the donor or complete organism from which the sample was taken.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/fga-wg/schema/donor'})

    donor_external_id: Optional[str] = Field(default=None, description="""External, globally unique identifier for the donor/organism.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Donor'], 'examples': [{'value': 'biosamples:SAMN04284578'}]} })
    donor_id: str = Field(default=..., description="""Internal identifier for the donor/organism (unique within the metadata deposit). """, json_schema_extra = { "linkml_meta": {'domain_of': ['Donor'], 'examples': [{'value': 'donor:ENCDO001AAA'}]} })
    species_taxon: Term = Field(default=..., description="""Taxonomical classification of the species of the donor/organism.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Donor'],
         'examples': [{'object': {'id': 'NCBITaxon:9606', 'label': 'Homo sapiens'}}]} })
    sex: Optional[Term] = Field(default=None, description="""Biological sex of the donor/organism.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Donor'],
         'examples': [{'object': {'id': 'CARO:0000027', 'label': 'male organism'}}]} })


class Experiment(ConfiguredBaseModel):
    """
    Represents a sequencing experiment that has been carried out within a study, based on biological samples, and providing data files as output. Subsequent analysis of output data is described by the Analysis entity.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/fga-wg/schema/experiment'})

    experiment_external_id: Optional[str] = Field(default=None, description="""External, globally unique identifier for the experiment.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Experiment'], 'examples': [{'value': 'encode:ENCSR000DPJ'}]} })
    experiment_id: str = Field(default=..., description="""Internal identifier for the experiment (unique within the metadata deposit).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Experiment'], 'examples': [{'value': 'experiment:ENCSR000DPJ'}]} })
    experiment_label: str = Field(default=..., description="""A human-readable description of the experiment, short enough to be used for listings within software user interfaces, tables, illustration legends, etc.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Experiment'],
         'examples': [{'value': 'H3K9me3 ChIP-seq on human AG04450'}]} })
    experiment_study_ref: str = Field(default=..., description="""Internal reference to the study within which the experiment has been carried out.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Experiment'], 'examples': [{'value': 'study:E-GEOD-35583'}]} })
    experiment_samples: list[InputSource] = Field(default=..., description="""External or internal references to samples used in the experiment. Internal references should refer to Sample objects.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Experiment'],
         'examples': [{'object': {'biological_replicate_labels': ['1', '2'],
                                  'inputsource_ref': 'sample:ENCBS004ENC',
                                  'qualified_relation': 'prov:used',
                                  'technical_replicate_labels': ['1_1', '2_1']}}]} })
    molecule_type: Term = Field(default=..., description="""Specifies the type of source material that is being sequenced.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Experiment'],
         'examples': [{'object': {'id': 'SO:0000991', 'label': 'genomic_DNA'}}]} })
    assay_type: Term = Field(default=..., description="""Sequencing technique intended for this library.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Experiment'],
         'examples': [{'object': {'id': 'obi:OBI_0000716', 'label': 'ChIP-seq assay'}}]} })
    design_description: Optional[str] = Field(default=None, description="""The high-level experiment design including layout, protocol.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Experiment'],
         'examples': [{'value': 'https://www.encodeproject.org/documents/92cd1386-ccad-450a-b5a6-ad49983e7e3f/@@download/attachment/wgEncodeUwHistone.release5.html.pdf'}]} })
    library_layout: Optional[Term] = Field(default=None, description="""Whether the library was built as paired-end, or single-end.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Experiment'],
         'examples': [{'object': {'id': 'obi:OBI_0000736',
                                  'label': 'single fragment library'}}]} })
    instrument: Optional[Term] = Field(default=None, description="""Technology platform used to perform nucleic acid sequencing, including name and/or number associated with a specific sequencing instrument model. It is recommended to be as specific as possible for this property (e.g. if the model/revision are available, providing that instead of just the instrument maker).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Experiment'],
         'examples': [{'object': {'id': 'obi:OBI_0002128',
                                  'label': 'Illumina Genome Analyzer'}}]} })
    sequencing_protocol: Optional[str] = Field(default=None, description="""Set of rules which guides how the sequencing protocol was followed. Change-tracking services such as Protocol.io or GitHub are encouraged instead of dumping free text in this field.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Experiment']} })
    antibody_target: Optional[Term] = Field(default=None, description="""The target of the antibody used in the experiment.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Experiment'],
         'examples': [{'object': {'id': 'SO:0001707', 'label': 'H3K9Me3'}}]} })
    biological_processes: Optional[list[Term]] = Field(default=None, description="""Biological processes illuminated by the experiment.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Experiment'],
         'examples': [{'object': {'id': 'GO:0140999',
                                  'label': 'histone H3K4 trimethyltransferase '
                                           'activity'}}]} })

    @field_validator('experiment_label')
    def pattern_experiment_label(cls, v):
        pattern=re.compile(r"^.{1,60}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid experiment_label format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid experiment_label format: {v}"
            raise ValueError(err_msg)
        return v


class File(ConfiguredBaseModel):
    """
    General information about a particular data file. Most fields (marked with an asterix*) are copied from the GA4GH DRS DrsObject model (https://ga4gh.github.io/data-repository-service-schemas/preview/release/drs-1.4.0/docs/#tag/DrsObjectModel), which is the top-level object returned from a DRS server in response to a successful lookup call (i.e. https://ga4gh.github.io/data-repository-service-schemas/preview/release/drs-1.4.0/docs/#tag/Objects).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/fga-wg/schema/file'})

    file_external_id: Optional[str] = Field(default=None, description="""External, globally unique identifier for the data file.""", json_schema_extra = { "linkml_meta": {'domain_of': ['File'], 'examples': [{'value': 'encode:ENCFF323LCS'}]} })
    file_id: str = Field(default=..., description="""Internal identifier for the data file (unique within the metadata deposit). """, json_schema_extra = { "linkml_meta": {'domain_of': ['File'], 'examples': [{'value': 'file:ENCFF323LCS'}]} })
    file_name: Optional[str] = Field(default=None, description="""A string that can be used to name a data file. This string is made up of uppercase and lowercase letters, decimal digits, hypen, period, and underscore [A-Za-z0-9.-_]. See http://pubs.opengroup.org/onlinepubs/9699919799/basedefs/V1_chap03.html#tag_03_282 [portable filenames].""", json_schema_extra = { "linkml_meta": {'domain_of': ['File'],
         'examples': [{'value': '87234.ENCODE.ENCBS004ENC.H3K9me3.peak_calls.bigBed'}]} })
    file_label: str = Field(default=..., description="""A human-readable description of the data file, short enough to be used for listings within software user interfaces, tables, illustration legends, etc.""", json_schema_extra = { "linkml_meta": {'domain_of': ['File'],
         'examples': [{'value': 'H3K9me3 ChIP-seq replicated peaks, GRCh38, AG04450'}]} })
    file_description: Optional[str] = Field(default=None, description="""A human readable description of the data file.""", json_schema_extra = { "linkml_meta": {'domain_of': ['File'],
         'examples': [{'value': 'H3K9me3 ChIP-seq replicated peaks on human (hg38) '
                                'AG04450 (Fibroblast derived cell line).'}]} })
    filecollection_refs: list[str] = Field(default=..., description="""Internal references to the FileCollection objects (within the deposit) that contains the data file, if any.""", json_schema_extra = { "linkml_meta": {'domain_of': ['File'], 'examples': [{'value': 'collection:ihec_encode'}]} })
    file_input_sources: list[InputSource] = Field(default=..., description="""External or internal references to data sources for the file, typically a data collection or a process that has generated the file. Internal references should lead to FileCollection, File, Experiment, or Analysis objects.""", json_schema_extra = { "linkml_meta": {'domain_of': ['File'],
         'examples': [{'object': {'biological_replicate_labels': ['1', '2'],
                                  'inputsource_ref': 'analysis:ENCAN718KHT',
                                  'qualified_relation': 'prov:wasGeneratedBy',
                                  'technical_replicate_labels': ['1_1', '2_1']}}]} })
    drs_uri: Optional[str] = Field(default=None, description="""A drs:// hostname-based URI, as defined in the DRS documentation, that tells clients how to access this object. The intent of this field is to make DRS objects self-contained, and therefore easier for clients to store and pass around. For example, if you arrive at this DRS JSON by resolving a compact identifier-based DRS URI, the self_uri presents you with a hostname and properly encoded DRS ID for use in subsequent access endpoint calls.""", json_schema_extra = { "linkml_meta": {'domain_of': ['File'],
         'examples': [{'value': 'drs://drs.example.org/ENCFF323LCS'}]} })
    access_methods: list[AccessMethod] = Field(default=..., description="""The list of access methods that can be used to fetch the data file. """, json_schema_extra = { "linkml_meta": {'domain_of': ['File'],
         'examples': [{'object': {'access_method': 'https',
                                  'access_url': {'url': 'https://epigenomesportal.ca/tracks/ENCODE/hg38/87234.ENCODE.ENCBS004ENC.H3K9me3.peak_calls.bigBed'}}},
                      {'object': {'access_method': 'https',
                                  'access_url': {'url': 'https://www.encodeproject.org/files/ENCFF323LCS/@@download/ENCFF323LCS.bigBed'}}},
                      {'object': {'access_method': 's3',
                                  'access_url': {'url': 's3://encode-public/2016/11/13/efd4e74e-7875-4d13-9630-0085bc834f18/ENCFF323LCS.bigBed'}}},
                      {'object': {'access_method': 'https',
                                  'access_url': {'url': 'https://encode-public.s3.amazonaws.com/2016/11/13/efd4e74e-7875-4d13-9630-0085bc834f18/ENCFF323LCS.bigBed'}}},
                      {'object': {'access_method': 'https',
                                  'access_url': {'url': 'https://datasetencode.blob.core.windows.net/dataset/2016/11/13/efd4e74e-7875-4d13-9630-0085bc834f18/ENCFF323LCS.bigBed?sv=2019-10-10&si=prod&sr=c&sig=9qSQZo4ggrCNpybBExU8SypuUZV33igI11xw0P7rB3c%3D'}}}]} })
    run_provenance: Optional[str] = Field(default=None, description="""Document detailing the provenance of the experiment or analysis run which produced the file as one of its outputs. The provenance info should include software versions, parameter settings, etc.""", json_schema_extra = { "linkml_meta": {'domain_of': ['File'], 'examples': [{'value': 'encode:ENCAN718KHT'}]} })
    quality_assessments: Optional[list[QualityAssessment]] = Field(default=None, description="""An array of QualityAssessment objects containing the main quality scores from assessment techniques applied to the data file.""", json_schema_extra = { "linkml_meta": {'domain_of': ['File'],
         'examples': [{'object': {'assessment_details_url': 'https://www.encodeproject.org/histone-chipseq-quality-metrics/70ae08dc-3edc-437f-a0a5-378c72e6269b/',
                                  'assessment_method': 'histone-chipseq-quality-metrics',
                                  'assessment_values': {'frip': 0.2931669095906483,
                                                        'nreads': 21018235,
                                                        'nreads_in_peaks': 6161851}}}]} })
    file_type: Term = Field(default=..., description="""The file format of the data file.""", json_schema_extra = { "linkml_meta": {'domain_of': ['File'],
         'examples': [{'object': {'id': 'edam:format_3004', 'label': 'bigBed'}}]} })
    mime_type: Optional[str] = Field(default=None, description="""A string providing the mime-type of the data file.""", json_schema_extra = { "linkml_meta": {'domain_of': ['File'], 'examples': [{'value': 'application/octet-stream'}]} })
    data_content: OutputType = Field(default=..., description="""Classification describing the file's purpose or contents.""", json_schema_extra = { "linkml_meta": {'domain_of': ['File'], 'examples': [{'value': 'replicated peaks'}]} })
    file_size: int = Field(default=..., description="""The file size in bytes.""", json_schema_extra = { "linkml_meta": {'domain_of': ['File'], 'examples': [{'value': '5359719'}]} })
    created_time: datetime  = Field(default=..., description="""Timestamp of content creation in RFC3339. (This is the creation time of the underlying content, not of the JSON object.).""", json_schema_extra = { "linkml_meta": {'domain_of': ['File'],
         'examples': [{'value': '2016-11-13T17:42:04.385801+00:00'}]} })
    updated_time: Optional[datetime ] = Field(default=None, description="""Timestamp of content update in RFC3339, identical to created_time in systems that do not support updates. (This is the update time of the underlying content, not of the JSON object.).""", json_schema_extra = { "linkml_meta": {'domain_of': ['File'],
         'examples': [{'value': '2016-11-13T17:42:04.385801+00:00'}]} })
    file_version: Optional[str] = Field(default=None, description="""A string representing a version. (Some systems may use checksum, a RFC3339 timestamp, or an incrementing version number.).""", json_schema_extra = { "linkml_meta": {'domain_of': ['File'],
         'examples': [{'value': 'efd4e74e-7875-4d13-9630-0085bc834f18'}]} })
    checksums: list[Checksum] = Field(default=..., description="""A list of checksums of the data file. At least one checksum must be provided. For blobs, the checksum is computed over the bytes in the blob.""", json_schema_extra = { "linkml_meta": {'domain_of': ['File'],
         'examples': [{'object': {'checksum': '535bc9628a1c5e5215226f9996e4eaca',
                                  'checksum_type': 'md5'}}]} })

    @field_validator('file_label')
    def pattern_file_label(cls, v):
        pattern=re.compile(r"^.{1,60}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid file_label format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid file_label format: {v}"
            raise ValueError(err_msg)
        return v


class Contact(ConfiguredBaseModel):
    """
    Contact information for a person or an organisation.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/fga-wg/schema/contact'})

    name: str = Field(default=..., description="""Name of the person or organisation.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Contact'], 'examples': [{'value': 'John Doe'}]} })
    contact_id: Optional[str] = Field(default=None, description="""Globally unique identifier for a person (e.g. ORCID ID) or organisation (e.g. BioProject accession).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Contact'], 'examples': [{'value': 'orcid:0000-0001-2345-6789'}]} })
    email: Optional[str] = Field(default=None, description="""E-mail address of the person or organisation.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Contact'], 'examples': [{'value': 'john@doe.com'}]} })

    @field_validator('email')
    def pattern_email(cls, v):
        pattern=re.compile(r"^\S+@\S+\.\S+$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid email format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid email format: {v}"
            raise ValueError(err_msg)
        return v


class FileCollection(ConfiguredBaseModel):
    """
    A collection of files, according to some selection criteria. In the context of the \"FAIRification of Genomic Annotations\" data model, we are mainly interested in \"GenomicAnnotationFile\" entities, but other types of files can also be contained in a collection, e.g. raw data files such as FASTQ files.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/fga-wg/schema/file-collection'})

    filecollection_external_id: Optional[str] = Field(default=None, description="""External, globally unique identifier for the file collection (in most cases, this will not exist).""", json_schema_extra = { "linkml_meta": {'domain_of': ['FileCollection']} })
    filecollection_id: str = Field(default=..., description="""Internal identifier for the file collection (unique within the metadata deposit). """, json_schema_extra = { "linkml_meta": {'domain_of': ['FileCollection'],
         'examples': [{'value': 'filecollection:ihec_encode'}]} })
    filecollection_label: str = Field(default=..., description="""A human-readable description of the file collection, short enough to be used for listings within software user interfaces, tables, illustration legends, etc.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FileCollection'],
         'examples': [{'value': 'IHEC data portal: ENCODE dataset'}]} })
    filecollection_description: Optional[str] = Field(default=None, description="""Human-readable description of the file collection.""", json_schema_extra = { "linkml_meta": {'any_of': [{'range': 'string'}, {'range': 'uri'}],
         'domain_of': ['FileCollection'],
         'examples': [{'value': 'ENCODE dataset in the International Human Epigenome '
                                'Consortium (IHEC) data portal, enhanced with metadata '
                                'from the ENCODE data portal.'}]} })
    filecollection_input_sources: Optional[list[InputSource]] = Field(default=None, description="""References to other input sources from which this file collection was derived.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FileCollection'],
         'examples': [{'object': {'inputsource_external_ref': 'https://epigenomesportal.ca/ihec/grid.html?build=2020-10&assembly=4&institutions=4',
                                  'qualified_relation': 'prov:wasDerivedFrom',
                                  'version': '2020-10'}},
                      {'object': {'inputsource_external_ref': 'https://www.encodeproject.org',
                                  'qualified_relation': 'prov:hadPrimarySource'}}]} })
    deposit_versioned_ref: str = Field(default=..., description="""Reference to versioned id of deposit containing this file collection.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FileCollection'],
         'examples': [{'value': 'doi:10.1234/zenodo.12345679'}]} })
    filecollection_contact: Optional[Contact] = Field(default=None, description="""Contact point to the creator and/or maintainer of the file collection.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FileCollection'],
         'examples': [{'object': {'contact_id': 'bioproject:PRJNA234466',
                                  'email': 'info@ihec-epigenomes.org',
                                  'name': 'International Human Epigenome Consortium'}}]} })

    @field_validator('filecollection_label')
    def pattern_filecollection_label(cls, v):
        pattern=re.compile(r"^.{1,60}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid filecollection_label format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid filecollection_label format: {v}"
            raise ValueError(err_msg)
        return v


class AccessURL(ConfiguredBaseModel):
    """
    The URL and associated HTTP headers to access the File object (orig: DrsObject). Exact copy of AccessURL object of the GA4GH DRS data model (https://ga4gh.github.io/data-repository-service-schemas/preview/release/drs-1.4.0/docs/#tag/AccessURLModel).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/fga-wg/schema/access-url'})

    url: str = Field(default=..., description="""A fully resolvable URL that can be used to fetch the actual object bytes.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AccessURL'],
         'examples': [{'value': 'https://epigenomesportal.ca/tracks/ENCODE/hg38/87234.ENCODE.ENCBS004ENC.H3K9me3.peak_calls.bigBed'}]} })
    headers: Optional[list[str]] = Field(default=None, description="""An optional list of headers to include in the HTTP request to `url`. These headers can be used to provide auth tokens required to fetch the object bytes.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AccessURL']} })


class AccessMethod(ConfiguredBaseModel):
    """
    Description of an access method (i.e. communication protocol) that can be used to fetch a File object (orig: DrsObject). Exact copy of the AccessMethod object of the GA4GH DRS data model (https://ga4gh.github.io/data-repository-service-schemas/preview/release/drs-1.4.0/docs/#tag/AccessMethodModel)
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/fga-wg/schema/access-method'})

    access_method: AccessMethods = Field(default=..., description="""Access method used to access the File object (orig: DrsObject).""", json_schema_extra = { "linkml_meta": {'domain_of': ['AccessMethod'], 'examples': [{'value': 'https'}]} })
    access_url: AccessURL = Field(default=..., description="""AccessURL object providing URL and associated HTTP headers to access the File object (orig: DrsObject).""", json_schema_extra = { "linkml_meta": {'domain_of': ['AccessMethod'],
         'examples': [{'object': {'url': 'https://epigenomesportal.ca/tracks/ENCODE/hg38/87234.ENCODE.ENCBS004ENC.H3K9me3.peak_calls.bigBed'}}]} })
    region: Optional[str] = Field(default=None, description="""Name of the region in the cloud service provider that the object belongs to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AccessMethod']} })


class Checksum(ConfiguredBaseModel):
    """
    A checksum of a File object (orig: DrsObject). Exact copy of the Checksum object of the GA4GH DRS data model (https://ga4gh.github.io/data-repository-service-schemas/preview/release/drs-1.4.0/docs/#tag/ChecksumModel).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/fga-wg/schema/checksum'})

    checksum: Optional[str] = Field(default=None, description="""The hex-string encoded checksum for the data.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Checksum'],
         'examples': [{'value': '535bc9628a1c5e5215226f9996e4eaca'}]} })
    checksum_type: str = Field(default=..., description="""The digest method used to create the checksum. The value (e.g. `sha-256`) SHOULD be listed as `Hash Name String` in the https://www.iana.org/assignments/named-information/named-information.xhtml#hash-alg [IANA Named Information Hash Algorithm Registry]. Other values MAY be used, as long as implementors are aware of the issues discussed in https://tools.ietf.org/html/rfc6920#section-9.4 [RFC6920]. GA4GH may provide more explicit guidance for use of non-IANA-registered algorithms in the future. Until then, if implementors do choose such an algorithm (e.g. because it's implemented by their storage provider), they SHOULD use an existing standard `type` value such as `md5`, `etag`, `crc32c`, `trunc512`, or `sha1`.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Checksum'], 'examples': [{'value': 'md5'}]} })


class QualityAssessment(ConfiguredBaseModel):
    """
    Represents the results of a quality assessment that has been carried out on a data file resulting from an experiment or analysis.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/fga-wg/schema/quality-assessment'})

    assessment_method: Union[Term, str] = Field(default=..., description="""Quality assessment method that has been carried out (e.g. BUSCO, OMArk, peak calling statistics, etc.)""", json_schema_extra = { "linkml_meta": {'any_of': [{'range': 'string'}, {'range': 'Term'}],
         'domain_of': ['QualityAssessment'],
         'examples': [{'value': 'histone-chipseq-quality-metrics'}]} })
    assessment_values: Union[dict[str, Union[Decimal, bool, int, str]], str] = Field(default=..., description="""Main values produced by the quality assessment.""", json_schema_extra = { "linkml_meta": {'any_of': [{'range': 'string'},
                    {'inlined': True,
                     'inlined_as_list': False,
                     'multivalued': True,
                     'range': 'AssessmentValue'}],
         'domain_of': ['QualityAssessment'],
         'examples': [{'object': {'frip': 0.2931669095906483,
                                  'nreads': 21018235,
                                  'nreads_in_peaks': 6161851}}]} })
    assessment_details_url: Optional[str] = Field(default=None, description="""URL to a report containing the detailed output from the quality assessment.""", json_schema_extra = { "linkml_meta": {'domain_of': ['QualityAssessment'],
         'examples': [{'value': 'https://www.encodeproject.org/histone-chipseq-quality-metrics/70ae08dc-3edc-437f-a0a5-378c72e6269b/'}]} })


class AssessmentValue(ConfiguredBaseModel):
    """
    Key-value pair representing a specific value produced by a quality assessment.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/fga-wg/schema/quality-assessment'})

    key: str = Field(default=..., description="""Key/name of the assessment value.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AssessmentValue']} })
    value: Union[Decimal, bool, int, str] = Field(default=..., description="""Value corresponding to the assessment key.""", json_schema_extra = { "linkml_meta": {'any_of': [{'range': 'decimal'},
                    {'range': 'boolean'},
                    {'range': 'integer'},
                    {'range': 'string'}],
         'domain_of': ['AssessmentValue']} })


class GenomeAssembly(ConfiguredBaseModel):
    """
    Information about of the exact genome assembly used to generate the annotation file, defining the genomic coordinate system for the sequence features.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/fga-wg/schema/genome-assembly'})

    seqcol_digest: str = Field(default=..., description="""Top-level sequence collection digest according to the GA4GH refget, Sequence Collections standard (v1.0). This a globally unique identifier for the genome assembly, algorithmically derivable from the genome assembly content. Usage is to uniquely identify the exact genome assembly used and allow detailed comparisons across genome assembly variants (say, variants of the GRCh38 assembly).""", json_schema_extra = { "linkml_meta": {'domain_of': ['GenomeAssembly'],
         'examples': [{'value': 'ga4gh:SC.EiFob05aCWgVU_B_Ae0cypnQut3cxUP1'}]} })
    seqcol_ordered_coord_system: str = Field(default=..., description="""Content-derived digest that uniquely identifies the ordered coordinate system of the genome assembly. (Coordinate systems with the same sequence names and lengths, but where the sequences are ordered differently, will have different ordered digests.). Usage is the ordered coordinate system digest can be used to uniquely generate a chromSizes file, useful in a number of analysis tools. Definition is the ordered coordinate system digest is defined as the level 1 digest of the name_length_pairs attribute of the sequence collection generated from the genome assembly.""", json_schema_extra = { "linkml_meta": {'domain_of': ['GenomeAssembly'],
         'examples': [{'value': 'ga4gh:SC.name_length_pairs.Yyz0Expaluj09xdDYg2Y6VOApvjg05Hf'}]} })
    seqcol_unordered_coord_system: str = Field(default=..., description="""Content-derived digest that uniquely identifies the order-invariant coordinate system of the genome assembly. This digest will be shared across all coordinate systems with the same sequence names and lenghts, regardless of the order of the sequences. Usage is the order-invariant coordinate system digest can be used to uniquely describe the coordinate system of a particular genome browser instance and the annotation files that are compatible with it. Definition is the order-invariant coordinate system digest is defined as the level 1 digest of the sorted_name_length_pairs attribute of the sequence collection generated from the genome assembly.""", json_schema_extra = { "linkml_meta": {'domain_of': ['GenomeAssembly'],
         'examples': [{'value': 'ga4gh:SC.sorted_name_length_pairs._dMQ5dPUNVx4OGQnDAPmGMkVRWWcYV99'}]} })
    accessions: Optional[list[str]] = Field(default=None, description="""Database accession numbers for the genome assembly, if available. Should precisely identify the genome assembly and be omitted if changes have been made to the assembly after retrieval, such as removing the alternate sequences.""", json_schema_extra = { "linkml_meta": {'domain_of': ['GenomeAssembly'], 'examples': [{'value': 'encode:ENCSR425FOI'}]} })
    aliases: list[str] = Field(default=..., description="""Human-readable aliases of the genome assembly. Can be imprecise, as preciseness is enforced in the other fields.""", json_schema_extra = { "linkml_meta": {'domain_of': ['GenomeAssembly'],
         'examples': [{'value': 'GRCh38_no_alt_analysis_set_GCA_000001405.15'},
                      {'value': 'GRCh38'},
                      {'value': 'hg38'}]} })


class TrackGeometry(ConfiguredBaseModel):
    """
    Overall geometric properties of the sequence features in the genomic annotation file if considered as an one-dimensional genome browser track, in line with the track type delineations from Gundersen et. al, 2011. While conceptually based on visual characteristics, these properties are also useful to e.g. select relevant annotation files for non-visual analyses.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/fga-wg/schema/track-geometry',
         'rules': [{'postconditions': {'slot_conditions': {'lengths_constant': {'name': 'lengths_constant',
                                                                                'required': True}}},
                    'preconditions': {'slot_conditions': {'has_lengths': {'equals_number': True,
                                                                          'name': 'has_lengths'}}}},
                   {'postconditions': {'slot_conditions': {'value_type': {'name': 'value_type',
                                                                          'required': True}}},
                    'preconditions': {'slot_conditions': {'has_values': {'equals_number': True,
                                                                         'name': 'has_values'}}}},
                   {'postconditions': {'all_of': [{'slot_conditions': {'edges_have_weights': {'name': 'edges_have_weights',
                                                                                              'required': True}}},
                                                  {'slot_conditions': {'edges_are_directed': {'name': 'edges_are_directed',
                                                                                              'required': True}}},
                                                  {'slot_conditions': {'edges_denote_parents': {'name': 'edges_denote_parents',
                                                                                                'required': True}}}]},
                    'preconditions': {'slot_conditions': {'has_edges': {'equals_number': True,
                                                                        'name': 'has_edges'}}}},
                   {'postconditions': {'slot_conditions': {'edge_weight_type': {'name': 'edge_weight_type',
                                                                                'required': True}}},
                    'preconditions': {'slot_conditions': {'edges_have_weights': {'equals_number': True,
                                                                                 'name': 'edges_have_weights'}}}}]})

    has_gaps: bool = Field(default=..., description="""Whether there are gaps between the sequence features (there exists at least one gap between two features on the same sequence).""", json_schema_extra = { "linkml_meta": {'domain_of': ['TrackGeometry'], 'examples': [{'value': 'True'}]} })
    has_lengths: bool = Field(default=..., description="""Whether the sequence features have lengths (at least one feature spans more than 1 base pair).""", json_schema_extra = { "linkml_meta": {'domain_of': ['TrackGeometry'], 'examples': [{'value': 'True'}]} })
    has_strands: bool = Field(default=..., description="""Whether the sequence features are stranded (at least one feature has strand information).""", json_schema_extra = { "linkml_meta": {'domain_of': ['TrackGeometry'], 'examples': [{'value': 'False'}]} })
    has_values: bool = Field(default=..., description="""Whether the sequence features have associated values (at least one feature has an associated value).""", json_schema_extra = { "linkml_meta": {'domain_of': ['TrackGeometry'], 'examples': [{'value': 'True'}]} })
    has_edges: bool = Field(default=..., description="""Whether the sequence features are linked across positions (at least one edge between features exists).""", json_schema_extra = { "linkml_meta": {'domain_of': ['TrackGeometry'], 'examples': [{'value': 'False'}]} })
    has_names: bool = Field(default=..., description="""Whether the sequence features are named (at least one feature has a name).""", json_schema_extra = { "linkml_meta": {'domain_of': ['TrackGeometry'], 'examples': [{'value': 'True'}]} })
    elements_overlapping: bool = Field(default=..., description="""Whether the sequence features are overlapping (at least one base pair is simultaneously covered by two sequence features).""", json_schema_extra = { "linkml_meta": {'domain_of': ['TrackGeometry'], 'examples': [{'value': 'False'}]} })
    elements_circular: bool = Field(default=..., description="""Whether the sequence features have circular coordinates (at least one feature that cross a sequence border).""", json_schema_extra = { "linkml_meta": {'domain_of': ['TrackGeometry'], 'examples': [{'value': 'False'}]} })
    lengths_constant: Optional[bool] = Field(default=None, description="""Whether the sequence lengths are constant (all sequence features have the same length, excluding features at the very end of a sequence).""", json_schema_extra = { "linkml_meta": {'domain_of': ['TrackGeometry'], 'examples': [{'value': 'False'}]} })
    value_type: Optional[DataTypes] = Field(default=None, description="""The type of values associated with the sequence features, if any.""", json_schema_extra = { "linkml_meta": {'domain_of': ['TrackGeometry'], 'examples': [{'value': 'multiple'}]} })
    edges_have_weights: Optional[bool] = Field(default=None, description="""Whether the edges linking sequence features are weighted (at least one edge between sequence features has an associated weight).""", json_schema_extra = { "linkml_meta": {'domain_of': ['TrackGeometry']} })
    edge_weight_type: Optional[DataTypes] = Field(default=None, description="""The type of values associated with the edges.""", json_schema_extra = { "linkml_meta": {'domain_of': ['TrackGeometry']} })
    edges_are_directed: Optional[bool] = Field(default=None, description="""Whether the edges linking sequence features are directed (at least one edge between sequence features is defined with a direction).""", json_schema_extra = { "linkml_meta": {'domain_of': ['TrackGeometry']} })
    edges_denote_parents: Optional[bool] = Field(default=None, description="""Whether the edges linking sequence features denote a parent-child relationship (all edges between sequence features denote parent-child relationships such as genes to exons, i.e. where the child is fully covered by the parent).""", json_schema_extra = { "linkml_meta": {'domain_of': ['TrackGeometry']} })


class GenomicAnnotationFile(File):
    """
    Information about a genomic annotation / track file. GenomicAnnotationFile is a specification of the File entity and inherits all the fields defined in File, in addition to the fields that are specific to GenomicAnnotationFile, as detailed here.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/fga-wg/schema/genomic-annotation-file'})

    genomic_annotation_digest: Optional[str] = Field(default=None, description="""Content-derived digest for distributed identification of genomic annotation files. (This field is currently a placeholder, as an algorithm for generating such a digest is yet to be specified.).""", json_schema_extra = { "linkml_meta": {'domain_of': ['GenomicAnnotationFile']} })
    genome_assembly: str = Field(default=..., description="""Information about the genome assembly used to generate the genomic annotation file, consequently defining the genomic coordinate system for the annotation.""", json_schema_extra = { "linkml_meta": {'domain_of': ['GenomicAnnotationFile'],
         'examples': [{'value': 'ga4gh:SC.EiFob05aCWgVU_B_Ae0cypnQut3cxUP1'}]} })
    track_geometry: TrackGeometry = Field(default=..., description="""Geometric properties of the sequence features in the genomic annotation file if considered as an one-dimensional genome browser track (also relevant for non-visual analyses).""", json_schema_extra = { "linkml_meta": {'domain_of': ['GenomicAnnotationFile'],
         'examples': [{'object': {'elements_circular': False,
                                  'elements_overlapping': False,
                                  'has_edges': False,
                                  'has_gaps': True,
                                  'has_lengths': True,
                                  'has_names': True,
                                  'has_strands': False,
                                  'has_values': True,
                                  'lengths_constant': False,
                                  'value_type': 'multiple'}}]} })
    sequence_features: list[Term] = Field(default=..., description="""List of sequence features described by the genomic annotation file.""", json_schema_extra = { "linkml_meta": {'domain_of': ['GenomicAnnotationFile'],
         'examples': [{'object': {'id': 'SO:0001707', 'label': 'H3K9Me3'}}]} })
    file_external_id: Optional[str] = Field(default=None, description="""External, globally unique identifier for the data file.""", json_schema_extra = { "linkml_meta": {'domain_of': ['File'], 'examples': [{'value': 'encode:ENCFF323LCS'}]} })
    file_id: str = Field(default=..., description="""Internal identifier for the data file (unique within the metadata deposit). """, json_schema_extra = { "linkml_meta": {'domain_of': ['File'], 'examples': [{'value': 'file:ENCFF323LCS'}]} })
    file_name: Optional[str] = Field(default=None, description="""A string that can be used to name a data file. This string is made up of uppercase and lowercase letters, decimal digits, hypen, period, and underscore [A-Za-z0-9.-_]. See http://pubs.opengroup.org/onlinepubs/9699919799/basedefs/V1_chap03.html#tag_03_282 [portable filenames].""", json_schema_extra = { "linkml_meta": {'domain_of': ['File'],
         'examples': [{'value': '87234.ENCODE.ENCBS004ENC.H3K9me3.peak_calls.bigBed'}]} })
    file_label: str = Field(default=..., description="""A human-readable description of the data file, short enough to be used for listings within software user interfaces, tables, illustration legends, etc.""", json_schema_extra = { "linkml_meta": {'domain_of': ['File'],
         'examples': [{'value': 'H3K9me3 ChIP-seq replicated peaks, GRCh38, AG04450'}]} })
    file_description: Optional[str] = Field(default=None, description="""A human readable description of the data file.""", json_schema_extra = { "linkml_meta": {'domain_of': ['File'],
         'examples': [{'value': 'H3K9me3 ChIP-seq replicated peaks on human (hg38) '
                                'AG04450 (Fibroblast derived cell line).'}]} })
    filecollection_refs: list[str] = Field(default=..., description="""Internal references to the FileCollection objects (within the deposit) that contains the data file, if any.""", json_schema_extra = { "linkml_meta": {'domain_of': ['File'], 'examples': [{'value': 'collection:ihec_encode'}]} })
    file_input_sources: list[InputSource] = Field(default=..., description="""External or internal references to data sources for the file, typically a data collection or a process that has generated the file. Internal references should lead to FileCollection, File, Experiment, or Analysis objects.""", json_schema_extra = { "linkml_meta": {'domain_of': ['File'],
         'examples': [{'object': {'biological_replicate_labels': ['1', '2'],
                                  'inputsource_ref': 'analysis:ENCAN718KHT',
                                  'qualified_relation': 'prov:wasGeneratedBy',
                                  'technical_replicate_labels': ['1_1', '2_1']}}]} })
    drs_uri: Optional[str] = Field(default=None, description="""A drs:// hostname-based URI, as defined in the DRS documentation, that tells clients how to access this object. The intent of this field is to make DRS objects self-contained, and therefore easier for clients to store and pass around. For example, if you arrive at this DRS JSON by resolving a compact identifier-based DRS URI, the self_uri presents you with a hostname and properly encoded DRS ID for use in subsequent access endpoint calls.""", json_schema_extra = { "linkml_meta": {'domain_of': ['File'],
         'examples': [{'value': 'drs://drs.example.org/ENCFF323LCS'}]} })
    access_methods: list[AccessMethod] = Field(default=..., description="""The list of access methods that can be used to fetch the data file. """, json_schema_extra = { "linkml_meta": {'domain_of': ['File'],
         'examples': [{'object': {'access_method': 'https',
                                  'access_url': {'url': 'https://epigenomesportal.ca/tracks/ENCODE/hg38/87234.ENCODE.ENCBS004ENC.H3K9me3.peak_calls.bigBed'}}},
                      {'object': {'access_method': 'https',
                                  'access_url': {'url': 'https://www.encodeproject.org/files/ENCFF323LCS/@@download/ENCFF323LCS.bigBed'}}},
                      {'object': {'access_method': 's3',
                                  'access_url': {'url': 's3://encode-public/2016/11/13/efd4e74e-7875-4d13-9630-0085bc834f18/ENCFF323LCS.bigBed'}}},
                      {'object': {'access_method': 'https',
                                  'access_url': {'url': 'https://encode-public.s3.amazonaws.com/2016/11/13/efd4e74e-7875-4d13-9630-0085bc834f18/ENCFF323LCS.bigBed'}}},
                      {'object': {'access_method': 'https',
                                  'access_url': {'url': 'https://datasetencode.blob.core.windows.net/dataset/2016/11/13/efd4e74e-7875-4d13-9630-0085bc834f18/ENCFF323LCS.bigBed?sv=2019-10-10&si=prod&sr=c&sig=9qSQZo4ggrCNpybBExU8SypuUZV33igI11xw0P7rB3c%3D'}}}]} })
    run_provenance: Optional[str] = Field(default=None, description="""Document detailing the provenance of the experiment or analysis run which produced the file as one of its outputs. The provenance info should include software versions, parameter settings, etc.""", json_schema_extra = { "linkml_meta": {'domain_of': ['File'], 'examples': [{'value': 'encode:ENCAN718KHT'}]} })
    quality_assessments: Optional[list[QualityAssessment]] = Field(default=None, description="""An array of QualityAssessment objects containing the main quality scores from assessment techniques applied to the data file.""", json_schema_extra = { "linkml_meta": {'domain_of': ['File'],
         'examples': [{'object': {'assessment_details_url': 'https://www.encodeproject.org/histone-chipseq-quality-metrics/70ae08dc-3edc-437f-a0a5-378c72e6269b/',
                                  'assessment_method': 'histone-chipseq-quality-metrics',
                                  'assessment_values': {'frip': 0.2931669095906483,
                                                        'nreads': 21018235,
                                                        'nreads_in_peaks': 6161851}}}]} })
    file_type: Term = Field(default=..., description="""The file format of the data file.""", json_schema_extra = { "linkml_meta": {'domain_of': ['File'],
         'examples': [{'object': {'id': 'edam:format_3004', 'label': 'bigBed'}}]} })
    mime_type: Optional[str] = Field(default=None, description="""A string providing the mime-type of the data file.""", json_schema_extra = { "linkml_meta": {'domain_of': ['File'], 'examples': [{'value': 'application/octet-stream'}]} })
    data_content: OutputType = Field(default=..., description="""Classification describing the file's purpose or contents.""", json_schema_extra = { "linkml_meta": {'domain_of': ['File'], 'examples': [{'value': 'replicated peaks'}]} })
    file_size: int = Field(default=..., description="""The file size in bytes.""", json_schema_extra = { "linkml_meta": {'domain_of': ['File'], 'examples': [{'value': '5359719'}]} })
    created_time: datetime  = Field(default=..., description="""Timestamp of content creation in RFC3339. (This is the creation time of the underlying content, not of the JSON object.).""", json_schema_extra = { "linkml_meta": {'domain_of': ['File'],
         'examples': [{'value': '2016-11-13T17:42:04.385801+00:00'}]} })
    updated_time: Optional[datetime ] = Field(default=None, description="""Timestamp of content update in RFC3339, identical to created_time in systems that do not support updates. (This is the update time of the underlying content, not of the JSON object.).""", json_schema_extra = { "linkml_meta": {'domain_of': ['File'],
         'examples': [{'value': '2016-11-13T17:42:04.385801+00:00'}]} })
    file_version: Optional[str] = Field(default=None, description="""A string representing a version. (Some systems may use checksum, a RFC3339 timestamp, or an incrementing version number.).""", json_schema_extra = { "linkml_meta": {'domain_of': ['File'],
         'examples': [{'value': 'efd4e74e-7875-4d13-9630-0085bc834f18'}]} })
    checksums: list[Checksum] = Field(default=..., description="""A list of checksums of the data file. At least one checksum must be provided. For blobs, the checksum is computed over the bytes in the blob.""", json_schema_extra = { "linkml_meta": {'domain_of': ['File'],
         'examples': [{'object': {'checksum': '535bc9628a1c5e5215226f9996e4eaca',
                                  'checksum_type': 'md5'}}]} })

    @field_validator('file_label')
    def pattern_file_label(cls, v):
        pattern=re.compile(r"^.{1,60}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid file_label format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid file_label format: {v}"
            raise ValueError(err_msg)
        return v


class Sample(ConfiguredBaseModel):
    """
    Information about a biospecimen/sample used as raw material for lab experiments.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/fga-wg/schema/sample',
         'rules': [{'postconditions': {'slot_conditions': {'cell_line': {'name': 'cell_line',
                                                                         'required': True}}},
                    'preconditions': {'slot_conditions': {'biospecimen_classification': {'equals_string': 'cell '
                                                                                                          'line',
                                                                                         'name': 'biospecimen_classification'}}}},
                   {'postconditions': {'slot_conditions': {'cell_type': {'name': 'cell_type',
                                                                         'required': True}}},
                    'preconditions': {'any_of': [{'slot_conditions': {'biospecimen_classification': {'equals_string': 'in '
                                                                                                                      'vitro '
                                                                                                                      'differentiated '
                                                                                                                      'cells',
                                                                                                     'name': 'biospecimen_classification'}}},
                                                 {'slot_conditions': {'biospecimen_classification': {'equals_string': 'primary '
                                                                                                                      'cell',
                                                                                                     'name': 'biospecimen_classification'}}}]}},
                   {'postconditions': {'slot_conditions': {'organism_tissue': {'name': 'organism_tissue',
                                                                               'required': True}}},
                    'preconditions': {'any_of': [{'slot_conditions': {'biospecimen_classification': {'equals_string': 'tissue',
                                                                                                     'name': 'biospecimen_classification'}}},
                                                 {'slot_conditions': {'biospecimen_classification': {'equals_string': 'organoid',
                                                                                                     'name': 'biospecimen_classification'}}}]}}]})

    sample_external_id: str = Field(default=..., description="""External, globally unique identifier for the biospecimen/sample.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sample'], 'examples': [{'value': 'encode:ENCBS004ENC'}]} })
    sample_id: str = Field(default=..., description="""Internal identifier for the biospecimen/sample (unique within the metadata deposit).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sample'], 'examples': [{'value': 'sample:ENCBS004ENC'}]} })
    sample_label: str = Field(default=..., description="""A human-readable description of the sample, short enough to be used for listings within software user interfaces, tables, illustration legends, etc.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sample'],
         'examples': [{'value': 'Homo sapiens AG04450 cell line'}]} })
    sample_description: Optional[str] = Field(default=None, description="""Human-readable description of the biospecimen/sample and the sampling process.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sample'],
         'examples': [{'value': 'Homo sapiens AG04450 cell line'}]} })
    donor_organism_ref: str = Field(default=..., description="""Internal reference to the donor/organism from which the biospecimen/sample was taken.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sample'], 'examples': [{'value': 'donor:ENCDO001AAA'}]} })
    biospecimen_classification: BiospecimenClassification = Field(default=..., description="""Main type of structural unit to be used for classification of the biospecimen/sample.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sample'], 'examples': [{'value': 'cell line'}]} })
    organism_tissue: Optional[Term] = Field(default=None, description="""Part of organism (typically tissue or organ) from which the biospecimen/sample was taken, or cell line was derived from.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sample'],
         'examples': [{'object': {'id': 'UBERON:0002048', 'label': 'lung'}}]} })
    cell_type: Optional[Term] = Field(default=None, description="""Cell type of isolated normal cells in the biospecimen/sample.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sample']} })
    cell_line: Optional[Term] = Field(default=None, description="""Cultured cell line used in the biospecimen/sample.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sample'],
         'examples': [{'object': {'id': 'CLO:0034832', 'label': 'AG04450 cell'}}]} })
    other_biospecimen: Optional[list[Term]] = Field(default=None, description="""Other biospecimen-related terms that can be used to further classify the biospecimen/sample.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sample'],
         'examples': [{'object': {'id': 'UBERON:0002384',
                                  'label': 'connective tissue'}},
                      {'object': {'id': 'CL:0002320',
                                  'label': 'connective tissue cell'}},
                      {'object': {'id': 'CL:0000057', 'label': 'fibroblast'}},
                      {'object': {'id': 'UBERON:0000925', 'label': 'endoterm'}},
                      {'object': {'id': 'UBERON:0001004',
                                  'label': 'respiratory system'}}]} })
    sampling_protocol: Optional[str] = Field(default=None, description="""Protocol detailing the collection and treatment of the biospecimen/sample.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sample'],
         'examples': [{'value': 'https://www.encodeproject.org/documents/3ed29dac-da67-47be-91b0-c9cad6a1b791/@@download/attachment/AG04450_Stam_protocol.pdf'}]} })
    sample_collection_location: Optional[str] = Field(default=None, description="""Geographical location where the sample was collected.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sample']} })
    sample_collection_date: Optional[datetime ] = Field(default=None, description="""Date of sample collection.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sample']} })
    phenotype: Optional[Term] = Field(default=None, description="""Main phenotype (e.g. disease) connected to the biospecimen/sample.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sample'],
         'examples': [{'object': {'id': 'PATO:0000461', 'label': 'normal'}}]} })
    donor_age: Optional[str] = Field(default=None, description="""Age of the donor/organism at the time of sampling""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sample'], 'examples': [{'value': 'W12'}]} })
    donor_development_stage: Optional[Term] = Field(default=None, description="""Development stage of the donor at the time of sampling.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sample'],
         'examples': [{'object': {'id': 'UBERON:0000323', 'label': 'late embryo'}}]} })
    donor_clinical_information: Optional[str] = Field(default=None, description="""Clinical information of the donor/organism at the time of sampling.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sample'], 'examples': [{'value': 'apparently healthy'}]} })

    @field_validator('sample_label')
    def pattern_sample_label(cls, v):
        pattern=re.compile(r"^.{1,60}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid sample_label format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid sample_label format: {v}"
            raise ValueError(err_msg)
        return v


class Study(ConfiguredBaseModel):
    """
    A scientific study, i.e. a unit of research, within which experiments and/or analyses have been carried out.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/fga-wg/schema/study'})

    study_external_id: Optional[str] = Field(default=None, description="""External, globally unique identifier for the study (preferably a BioStudies CURIE).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Study'], 'examples': [{'value': 'biostudies:S-EPMC7391744'}]} })
    study_id: str = Field(default=..., description="""Internal identifier for the study (unique within the metadata deposit). Namespace: \"study\".""", json_schema_extra = { "linkml_meta": {'domain_of': ['Study'], 'examples': [{'value': 'study:S-EPMC7391744'}]} })
    study_title: str = Field(default=..., description="""Title of the study.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Study'],
         'examples': [{'value': 'An integrative ENCODE resource for cancer genomics'}]} })
    study_abstract: Optional[str] = Field(default=None, description="""Abstract of the study.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Study'],
         'examples': [{'value': 'ENCODE comprises thousands of functional genomics '
                                'datasets, and the encyclopedia covers hundreds of '
                                'cell types, providing a universal annotation for '
                                'genome interpretation. However, for particular '
                                'applications, it may be advantageous to use a '
                                'customized annotation. Here, we develop such a custom '
                                'annotation by leveraging advanced assays, such as '
                                'eCLIP, Hi-C, and whole-genome STARR-seq on a number '
                                'of data-rich ENCODE cell types. A key aspect of this '
                                'annotation is comprehensive and experimentally '
                                'derived networks of both transcription factors and '
                                'RNA-binding proteins (TFs and RBPs). Cancer, a '
                                'disease of system-wide dysregulation, is an ideal '
                                'application for such a network-based annotation. '
                                'Specifically, for cancer-associated cell types, we '
                                'put regulators into hierarchies and measure their '
                                'network change (rewiring) during oncogenesis. We also '
                                'extensively survey TF-RBP crosstalk, highlighting how '
                                'SUB1, a previously uncharacterized RBP, drives '
                                'aberrant tumor expression and amplifies the effect of '
                                'MYC, a well-known oncogenic TF. Furthermore, we show '
                                'how our annotation allows us to place oncogenic '
                                'transformations in the context of a broad cell space; '
                                'here, many normal-to-tumor transitions move towards a '
                                'stem-like state, while oncogene knockdowns show an '
                                'opposing trend. Finally, we organize the resource '
                                'into a coherent workflow to prioritize key elements '
                                'and variants, in addition to regulators. We showcase '
                                'the application of this prioritization to somatic '
                                'burdening, cancer differential expression and GWAS. '
                                'Targeted validations of the prioritized regulators, '
                                'elements and variants using siRNA knockdowns, '
                                'CRISPR-based editing, and luciferase assays '
                                'demonstrate the value of the ENCODE resource.'}]} })
    project_external_ref: Optional[str] = Field(default=None, description="""Reference to a project within which the study was carried out (preferably a BioProject CURIE).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Study'], 'examples': [{'value': 'bioproject:PRJNA63441'}]} })
    project_name: Optional[str] = Field(default=None, description="""Name of the project within which the study was carried out.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Study']} })
    publications: Optional[list[str]] = Field(default=None, description="""List of (relevant) publications containing the results of the study (in the form of DOI CURIEs).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Study'],
         'examples': [{'value': 'https://doi.org/10.1038/s41467-020-14743-w'}]} })
    study_contact: Optional[Contact] = Field(default=None, description="""Contact point for the study.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Study'],
         'examples': [{'object': {'contact_id': 'orcid:0000-0002-9746-3719',
                                  'email': 'mark@gersteinlab.org',
                                  'name': 'Mark Gerstein'}}]} })


class Bundle(ConfiguredBaseModel):
    """
    A bundle representing a set of genome annotation files, organised in sub-collections. Metadata has been harmonised in line with the \"FAIRification of Genomic Annotations\" data model.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/fga-wg/schema/bundle'})

    bundle_metadata: BundleMetadata = Field(default=..., description="""Top-level metadata about the bundle of genomic annotation files.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Bundle']} })
    donors: Optional[list[Donor]] = Field(default=None, description="""Information about the donors or complete organisms from which the samples were taken.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Bundle']} })
    experiments: Optional[list[Experiment]] = Field(default=None, description="""Information about sequencing experiments that have been carried out to generate the files.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Bundle']} })
    files: Optional[list[Union[File,GenomicAnnotationFile]]] = Field(default=None, description="""Information about particular genome annotation (and other relevant) files.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Bundle']} })
    file_collections: Optional[list[FileCollection]] = Field(default=None, description="""Information about collections of files contained in this dataset, each collection defined according to some selection criteria.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Bundle']} })
    analyses: Optional[list[Analysis]] = Field(default=None, description="""Information about computational processing and analyses that have been carried out to generate the files.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Bundle']} })
    samples: Optional[list[Sample]] = Field(default=None, description="""Information about the biospecimens/samples used as raw material for lab experiments.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Bundle']} })
    studies: Optional[list[Study]] = Field(default=None, description="""The scientific studies, i.e. units of research, within which experiments and/or analyses have been carried out.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Bundle']} })


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
Deposit.model_rebuild()
InputSource.model_rebuild()
BundleMetadata.model_rebuild()
OntologyVersions.model_rebuild()
Term.model_rebuild()
Analysis.model_rebuild()
Donor.model_rebuild()
Experiment.model_rebuild()
File.model_rebuild()
Contact.model_rebuild()
FileCollection.model_rebuild()
AccessURL.model_rebuild()
AccessMethod.model_rebuild()
Checksum.model_rebuild()
QualityAssessment.model_rebuild()
AssessmentValue.model_rebuild()
GenomeAssembly.model_rebuild()
TrackGeometry.model_rebuild()
GenomicAnnotationFile.model_rebuild()
Sample.model_rebuild()
Study.model_rebuild()
Bundle.model_rebuild()
