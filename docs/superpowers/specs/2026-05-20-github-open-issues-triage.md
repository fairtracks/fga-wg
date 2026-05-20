# Open GitHub Issues Triage Plan

This triage snapshot covers the 22 currently open GitHub issues for `fairtracks/fga-wg`, prioritized by the newest visible comment first and using the issue `updatedAt` timestamp when no comments exist. The list is intended to help the working group focus first on active discussions, unresolved schema design questions, and deliverable-tracking items.

1. **Issue #23 — FGA Schema Class Inventory: core vs ancillary attributes**
   - Created: 2026-03-11T20:48:08Z
   - Updated: 2026-03-27T02:07:48Z
   - Latest comment timestamp: 2026-03-27T02:07:48Z
   - Labels: None
   - Assignees: None
   - Body:

     This document inventories all 23 classes and 4 enums in the FGA (FAIRification of Genomic Annotations) schema, classifying each as **core** (novel to genomic annotations) or **ancillary** (modeling concepts already defined by external standards). The goal is to identify which classes should be defined by FGA and which should reference existing standards, reducing duplication and improving interoperability.


     Browse the schema interactively: [FGA Schema Viewer](https://databio.org/fga-schema-viewer/)


     ## Definitions


     - **Core**: Classes that represent the schema's novel contribution — concepts unique to genomic annotations that no existing standard models. These are what FGA adds to the world.

     - **Ancillary**: Classes that model concepts already defined by external standards (GA4GH DRS, W3C PROV-O, EBI BioSamples, etc.). These are necessary context for genomic annotations but are not themselves about genomic annotations.


     Of 23 classes, only **2 are core**. The other 21 are ancillary.


     ## Proposal


     Here's my radical proposal: **all 21 ancillary objects should be references to external models, not defined by us**.


     The FGA schema's value is GenomicAnnotationFile and TrackGeometry. Everything else — files, checksums, samples, experiments, provenance — is someone else's problem, already solved. We should reference their solutions, not redefine them.


     So then the question just becomes: to what extent can we reference external models, and how?


     ## Linking vs. Embedding


     The FGA schema currently **embeds** external definitions — copying them into the schema with a description noting the origin (e.g., *"Exact copy of the AccessMethod object of the GA4GH DRS data model"*). The alternative is **linking** — referencing the external definition in place so that tooling can validate against the upstream source and updates propagate naturally. LinkML supports structural linking via `imports`, but only to other LinkML schemas; none of the 14 external standards surveyed publish LinkML schemas, so true structural linking is not currently possible. JSON Schema fares better — `$ref` can link to any JSON Schema or OpenAPI spec, covering DRS, Seqcol, Phenopackets, DataCite, and ISA-JSON. For ontologies (EDAM, PROV-O, DCAT), both languages reference terms by URI as values. For archives (BioSamples, ENA/SRA), the connection is a string accession field.


     ## Classes


     | Name | File | Role | Current External Link | Suggested External Link |

     |---|---|---|---|---|

     | **GenomicAnnotationFile** | genomic_annotation_file.yaml | **core** | — | — |

     | **TrackGeometry** | track_geometry.yaml | **core** | — | — |

     | File | file.yaml | ancillary | GA4GH DRS 1.4 DrsObject | GA4GH DRS — add `class_uri`/`conforms_to` |

     | AccessMethod | access_method.yaml | ancillary | GA4GH DRS 1.4 AccessMethod | GA4GH DRS — add `class_uri`/`conforms_to` |

     | AccessURL | access_url.yaml | ancillary | GA4GH DRS 1.4 AccessURL | GA4GH DRS — add `class_uri`/`conforms_to` |

     | Checksum | checksum.yaml | ancillary | GA4GH DRS 1.4 Checksum | GA4GH DRS — add `class_uri`/`conforms_to` |

     | GenomeAssembly | genome_assembly.yaml | ancillary | GA4GH Refget/Seqcol | GA4GH Refget/Seqcol — add `implements`/`conforms_to` |

     | InputSource | input_source.yaml | ancillary | — | W3C PROV-O — declare as `prov:Influence` subclass |

     | Sample | sample.yaml | ancillary | — | EBI BioSamples; ISA Sample |

     | Donor | donor.yaml | ancillary | — | GA4GH Phenopackets Individual; EBI BioSamples |

     | Experiment | experiment.yaml | ancillary | — | ENA/SRA Experiment; ISA Assay |

     | Analysis | analysis.yaml | ancillary | — | W3C PROV-O Activity; RO-Crate |

     | Study | study.yaml | ancillary | — | EBI BioStudies; DataCite |

     | Contact | contact.yaml | ancillary | — | DataCite Creator; Schema.org Person |

     | TopLevel | top_level.yaml | ancillary | — | — |

     | Document | document.yaml | ancillary | — | DCAT Catalog; DataCite |

     | FileCollection | file_collection.yaml | ancillary | — | DCAT Dataset |

     | Deposit | deposit.yaml | ancillary | — | DataCite; Zenodo deposit model |

     | OntologyVersions | document.yaml | ancillary | — | OWL versionIRI |

     | Term | term.yaml | ancillary | — | SKOS Concept |

     | QualityAssessment | quality_assessment.yaml | ancillary | — | — |

     | AssessmentValue | quality_assessment.yaml | ancillary | — | — |

     | Any | util.yaml | ancillary | linkml:Any | linkml:Any |


     ## Enums


     | Name | File | Role | Current External Link | Suggested External Link |

     |---|---|---|---|---|

     | **DataTypes** | track_geometry.yaml | **core** | — | — |

     | OutputType | file.yaml | ancillary | ENCODE output_type | EDAM Ontology; replace with `Term` |

     | AccessMethods | access_method.yaml | ancillary | GA4GH DRS | GA4GH DRS — already aligned |

     | BiospecimenClassification | sample.yaml | ancillary | ENCODE biosample_type | EBI BioSamples; OBI |


     ## Summary


     - **Core:** 2 classes + 1 enum (GenomicAnnotationFile, TrackGeometry, DataTypes)

     - **Ancillary:** 21 classes + 3 enums

       - Already documented as external (in descriptions): 6 classes (File, AccessMethod, AccessURL, Checksum, GenomeAssembly, Any)

       - Should link to external standard: 12 classes (InputSource, Sample, Donor, Experiment, Analysis, Study, Contact, Document, FileCollection, Deposit, OntologyVersions, Term)

       - Generic helpers (no obvious single external): 3 classes (TopLevel, QualityAssessment, AssessmentValue)

   - Latest comment text:

     @nsheff:


     Here is another resource, with clinical focus:

     - https://www.hl7.org/fhir/genomicstudy-definitions.html

     - https://www.hl7.org/fhir/genomicstudy-example.json.html

2. **Issue #26 — Questions about Sample and Donor entities**
   - Created: 2026-03-11T21:11:14Z
   - Updated: 2026-03-11T21:11:14Z
   - Latest comment timestamp: 2026-03-11T21:11:14Z
   - Labels: None
   - Assignees: None
   - Body:

     # Questions About Sample and Donor


     **FGA schema files:** `src/schema/sample.yaml`, `src/schema/donor.yaml`


     ## Summary


     The FGA schema defines a 17-field `Sample` and a 4-field `Donor` to capture biological sample metadata. These model experimental biology — organism, tissue, cell type, cell line, phenotype, clinical information — not genomic annotations. At least four external standards already model this space (Phenopackets, BioSamples, ENA/SRA, ISA-JSON), though none match FGA's field structure exactly. I have four suggestions:


     1. **If Sample is kept, link it to Phenopackets.** FGA Donor is a strict subset of Phenopackets Individual. FGA Sample overlaps ~10/17 fields with Phenopackets Biosample. At minimum, declare `implements` and use Phenopackets field names where they overlap.

     2. **Consider a BioSamples checklist instead.** No checklist exists for genomic annotation samples. FGA's Sample fields could become a community-contributed checklist validated by EBI's existing infrastructure, rather than a standalone class.

     3. **Use thin references.** BEDbase already uses `global_sample_id` to point to GEO/ENCODE records. FGA could formalize this as a CURIE reference instead of defining a 17-field class.

     4. **Replace the BiospecimenClassification enum.** Same pattern as OutputType — a hardcoded ENCODE vocabulary with no ontology backing.


     ## Background


     ### The scope question


     Should a genomic annotation schema define what a biological sample looks like?


     Sample and Donor are context that a genomic annotation *references*, not *defines* (see [class inventory](class-inventory.md)). On the other hand, no existing standard provides a typed, genomics-focused sample profile — Phenopackets is clinical; BioSamples/ENA/ISA use untyped attribute bags. Maybe the genomics community needs typed fields for `cell_type`, `organism_tissue`, `cell_line`, and FGA is filling that gap.


     ### How BEDbase handles this today


     BEDbase stores sample metadata as flat free-text strings on the BED file record:


     ```python

     class BedPEPHub(BaseModel):

         cell_type: str = ""          # free text, not ontology-typed

         cell_line: str = ""

         tissue: str = ""

         global_sample_id: str = ""   # ← thin reference (e.g. "GSM1234")

         global_experiment_id: str = ""

     ```


     There are no separate Sample or Donor tables. The `global_sample_id` is already a thin reference to GEO/ENCODE; the free-text fields are a search cache populated from those external sources.


     Would FGA's typed fields improve this? Possibly — if the right fields are chosen and ontology constraints add real value. But adopting the full 17-field Sample means either building a normalized sample database (duplicating BioSamples/ENCODE) or populating many typed fields per BED file. The cost-benefit depends on whether FGA's field selection is the right one.


     ### What Phenopackets already covers


     I compared every FGA field against four external standards. The short version: Donor adds nothing over Phenopackets, and Sample partially overlaps.


     #### Donor (4 fields) vs Phenopackets Individual (9 fields)


     | FGA Donor | Phenopackets Individual | Match |

     |---|---|---|

     | `donor_id` | `id` | Direct |

     | `donor_external_id` | `alternate_ids` | Direct |

     | `species_taxon` (Term) | `taxonomy` (OntologyClass) | Direct |

     | `sex` (Term) | `sex` + `karyotypic_sex` + `gender` | Direct (richer) |

     | — | `date_of_birth`, `vital_status`, etc. | FGA lacks these |


     **FGA Donor is a strict subset of Phenopackets Individual. It adds nothing.**


     #### Sample (17 fields) vs external standards


     | FGA Sample field | Phenopackets Biosample | BioSamples | ENA/SRA | ISA |

     |---|---|---|---|---|

     | `sample_id` | `id` | `accession` | `accession` | `@id` |

     | `sample_external_id` | — | — | `alias` | — |

     | `sample_label` | — | `name` | `TITLE` | `name` |

     | `sample_description` | `description` | (bag) | `DESCRIPTION` | — |

     | `donor_organism_ref` | `individual_id` | (via relationships) | — | `derivesFrom` |

     | `biospecimen_classification` | `sample_type` | (bag) | (bag) | (bag) |

     | `organism_tissue` | `sampled_tissue` | (bag) | (bag) | (bag) |

     | `cell_type` | — | (bag) | (bag) | (bag) |

     | `cell_line` | — | (bag) | (bag) | (bag) |

     | `other_biospecimen` | `material_sample` | (bag) | (bag) | (bag) |

     | `sampling_protocol` | `procedure` | — | — | — |

     | `sample_collection_location` | — | (bag) | (bag) | — |

     | `sample_collection_date` | `time_of_collection` | — | (bag) | — |

     | `phenotype` | `phenotypic_features` | (bag) | (bag) | (bag) |

     | `donor_age` | (on Individual) | (bag) | (bag) | (bag) |

     | `donor_development_stage` | — | (bag) | (bag) | (bag) |

     | `donor_clinical_information` | histological_diagnosis + tumor_* | (bag) | (bag) | (bag) |


     "(bag)" = stored as an untyped key-value pair in an open attributes bag.


     No single standard matches FGA's 17 fields exactly. This cuts both ways — it could mean FGA is filling a real gap, or it could mean FGA is inventing a standalone model with no interoperability path. Phenopackets Biosample is closest (~10/17 overlap) but clinically focused, missing `cell_type`, `cell_line`, and `biospecimen_classification`. The other standards use open bags with no typed fields at all.


     ## Suggestions


     ### 1. If Sample is kept, link it to Phenopackets


     If a typed sample profile is needed, FGA should at minimum declare its relationship to Phenopackets Biosample — use their field names where they overlap and add only what's missing:


     ```yaml

     classes:

       Sample:

         implements:

           - phenopackets:Biosample

         conforms_to: "GA4GH Phenopackets v2"

         slots:

           # From Phenopackets (use their names)

           - id                    # was: sample_id

           - individual_id         # was: donor_organism_ref

           - sampled_tissue        # was: organism_tissue

           - sample_type           # was: biospecimen_classification

           - description           # was: sample_description

           - time_of_collection    # was: sample_collection_date

           # FGA additions (not in Phenopackets)

           - cell_type             # Term (CL ontology)

           - cell_line             # Term (CLO ontology)

     ```


     This makes the relationship honest: "we're profiling Phenopackets Biosample, keeping their names for the ~10 overlapping fields, and adding 2-3 that they don't cover."


     ### 2. Contribute a BioSamples checklist instead


     Another option avoids defining Sample in FGA at all. EBI BioSamples uses an open attribute bag with validation from **checklists** — community-defined JSON Schemas that specify which attributes are required or recommended for a particular type of sample. There are ~50 existing checklists covering environmental, clinical, metagenomic, and agricultural samples, but **none for genomic annotation samples**.


     This is exactly the gap FGA's Sample class tries to fill: "for a genomic annotation file, which sample properties matter?" A BioSamples checklist would answer that question within an existing, governed system:


     - FGA's Sample fields become required/recommended attributes in a checklist JSON Schema

     - Validation uses BioSamples' infrastructure ([EBIBioSamples/json-schema-store](https://github.com/EBIBioSamples/json-schema-store))

     - The checklist is maintained by the genomic annotation community, hosted and tooled by EBI

     - FGA says "samples should conform to checklist BSDCXXXXX" instead of defining Sample internally

     - Consumers point to BioSamples accessions knowing the upstream record has the right fields


     This is the most practical external path because it uses BioSamples' intended extension mechanism. Other possibilities — extending Phenopackets or creating a new GA4GH standard — are heavier lifts, since Phenopackets is clinically governed and new GA4GH standards require Driver Projects.


     ### 3. Use thin references


     Regardless of where sample metadata is defined, FGA could replace its Sample and Donor classes with simple references to where the authoritative record lives:


     ```yaml

     slots:

       sample_ref:

         range: uriorcurie

         examples:

           - value: 'biosamples:SAMEA104371999'

           - value: 'encode:ENCBS004ENC'

           - value: 'geo:GSM1234567'

       donor_ref:

         range: uriorcurie

         examples:

           - value: 'biosamples:SAMN04284578'

           - value: 'encode:ENCDO001AAA'

     ```


     This formalizes what BEDbase already does with `global_sample_id`. A minimal `SampleSummary` cache could provide queryable fields without round-tripping to an external API.


     ### 4. Replace the BiospecimenClassification enum


     The `BiospecimenClassification` enum (9 values: "cell line", "tissue", "primary cell", etc.) is a hardcoded copy from ENCODE's `biosample_type` vocabulary with no ontology backing — the same pattern as OutputType (see [replace-outputtype-enum.md](replace-outputtype-enum.md)).

   - Latest comment text:

     No comments

3. **Issue #25 — Questions About InputSource**
   - Created: 2026-03-11T20:58:27Z
   - Updated: 2026-03-11T20:58:27Z
   - Latest comment timestamp: 2026-03-11T20:58:27Z
   - Labels: None
   - Assignees: None
   - Body:

     # Questions About InputSource


     FGA schema file: `src/schema/input_source.yaml`


     ## Background


     The FGA schema defines an `InputSource` class — an intermediary object that every inter-entity reference must go through. It carries 8 fields: a reference (internal or external), a relationship type, biological and technical replicate labels, database accessions, version, and date of retrieval. It's used on File, Experiment, Analysis, Document, and FileCollection. On the first three, it's **required**.


     I have some questions about this design, coming from the perspective of a potential adopter (BEDbase).


     ## The scope question


     InputSource exists to model the provenance chain of bioinformatics analysis — how samples become experiments, experiments feed analyses, and analyses produce files, with replicate tracking at each step. That's a formal model of *how bioinformatics works*, which is a much bigger problem than describing genomic annotation files.


     Existing standards have been working on this for years: W3C PROV-O for general provenance, ISA for experimental metadata, CWL/Nextflow for workflow provenance, and ENCODE's own data model for replicate tracking. Is it in scope for FGA to define its own approach to this? If analysis provenance is needed, could the schema defer to one of these existing standards rather than defining InputSource?


     ## The adopter problem


     BEDbase stores genomic annotation files (BED files). Our data model is flat: a BED file has an ID, genome, format, stats, and annotation metadata (cell type, assay, antibody target, tissue, etc.). We don't have Experiment, Analysis, or Sample entities. The metadata that FGA puts on those entities, we put directly on the file as flat fields — because our users want to search and filter by those properties, not navigate a provenance graph.


     Since `file_input_sources` is required on File, adopting the FGA schema means we'd have to construct InputSource objects for provenance relationships that don't exist in our data. We'd be manufacturing structure to satisfy a schema requirement, not describing something real.


     I think InputSource (or at least its required status) assumes that every adopter has a full provenance chain from sample through experiment through analysis to file. Many don't. Making it optional would let adopters describe what they have without forcing them to invent what they don't.


     ## Replicate labels on every relationship


     InputSource carries `biological_replicate_labels` and `technical_replicate_labels` on every instance. These fields appear on every file-analysis link, every experiment-sample link, and every analysis-experiment link. Looking at the examples in the schema, the same replicate values are repeated at each level of the provenance chain — they're not subsets or derivations, just the same list copied through.


     Replicates are fundamentally a property of experimental design — they describe how an experiment organized its samples. ENCODE models this directly: Replicate is an object on Experiment that links a sample to a replicate number. File-level replicate associations are derived by tracing provenance. This keeps the information in one place.


     In the current FGA design, every adopter encounters replicate fields on every relationship, even if they have no replicate data. Moving replicate tracking to Experiment and letting downstream entities inherit it through provenance would keep this information where it belongs and simplify InputSource (or eliminate the need for it on most relationships).


     ## If InputSource is needed, why not use PROV-O?


     The schema already uses PROV-O vocabulary as values for `qualified_relation` in its examples: `prov:wasGeneratedBy`, `prov:used`, `prov:wasInformedBy`, `prov:wasDerivedFrom`, `prov:hadPrimarySource`. InputSource is structurally similar to PROV-O's Qualification Pattern — an intermediate object that annotates a relationship with metadata.


     If the schema is already using PROV-O terms, I'm wondering why it defines a custom class rather than aligning with PROV-O. Even a minimal step — declaring InputSource as a subclass of `prov:Influence` — would make the connection explicit.


     ## Summary


     1. **Is analysis provenance in scope for FGA?** If so, could it defer to existing standards (PROV-O, ISA) rather than defining InputSource?

     2. **InputSource should not be required.** Not every adopter has a full provenance chain. Making `file_input_sources`, `experiment_samples`, and `analysis_input_sources` optional would let adopters describe what they have.

     3. **Replicate labels belong on Experiment**, not on every relationship. The current design repeats them at every level of the provenance chain.

     4. **If InputSource is kept, it should align with PROV-O**, which the schema already references in its examples.

   - Latest comment text:

     No comments

4. **Issue #24 — Questions about the OutputType enum**
   - Created: 2026-03-11T20:49:34Z
   - Updated: 2026-03-11T20:58:26Z
   - Latest comment timestamp: 2026-03-11T20:58:26Z
   - Labels: None
   - Assignees: None
   - Body:

     FGA schema file: `src/schema/file.yaml`


     ## Background


     The FGA schema defines an `OutputType` enum — a closed list of ~270 string values describing the purpose or content of a file. It's used on the `data_content` field of `File`, which is required. The values are copied from ENCODE's internal `output_type` vocabulary, which is not backed by any external ontology.


     I have some questions about this design, coming from the perspective of a potential adopter (BEDbase).


     ## No ontology backing


     Every other vocabulary field in the FGA schema uses the `Term` class (a CURIE + label pair) for ontology-backed classification — `file_type`, `assay_type`, `molecule_type`, `organism_tissue`, `cell_type`, etc. `data_content` is the sole exception: it uses a closed enum of bare strings with no identifiers. Values like `"IDR thresholded peaks"` and `"pseudoreplicated peaks"` aren't resolvable URIs and can't be linked to external knowledge systems.


     Why does this one field use a different pattern from the rest of the schema?


     ## ENCODE-specific scope


     The 270 values describe ENCODE's processing pipeline outputs. They conflate *what a file contains* with *how it was processed* — there are six variants of "peaks" distinguished only by QC method (`"peaks"`, `"replicated peaks"`, `"pseudoreplicated peaks"`, `"IDR thresholded peaks"`, `"conservative IDR thresholded peaks"`, `"optimal IDR thresholded peaks"`), plus 30+ strand-specific signal variants that encode processing decisions rather than content type.


     This vocabulary is meaningless for non-ENCODE files. BEDbase ingests files from GEO (labeled generically as "BED" or "narrowPeak") and other sources that have no ENCODE-style output_type. At the same time, common BED content types like CpG islands, repeat elements, conservation scores, and TAD boundaries have no applicable OutputType value.


     ## Maintenance burden


     The enum is a frozen snapshot — ~270 lines, the largest single block in the schema. ENCODE's vocabulary evolves independently as new assays and pipelines are developed. The FGA schema has no mechanism to stay synchronized. Any update requires editing the LinkML source and re-releasing the schema.


     ## What should replace it?


     Ideally, an external ontology would provide a comprehensive vocabulary for genomic file content types. EDAM is the closest candidate, but a mapping of all 270 OutputType values found only ~7% with direct EDAM matches, ~48% with a broader parent term, and ~45% with no equivalent at all. The unmatched values are heavily ENCODE-pipeline-specific (IDR stages, strand-specific signal variants, CRISPR screening outputs) — concepts no general ontology has modeled.


     No existing ontology covers this domain well enough to serve as a drop-in replacement. But that doesn't mean the schema should hardcode ENCODE's vocabulary as a stopgap. The pragmatic path is to switch `data_content` to use the schema's existing `Term` class (CURIE + label), which would:


     - Make it consistent with every other vocabulary field in the schema

     - Let ENCODE files use `{id: "encode:output_type/peaks", label: "peaks"}` — preserving the vocabulary with a proper namespace

     - Let other sources use EDAM, GEO terms, or any vocabulary with a CURIE prefix

     - Allow the field to converge on better vocabularies over time, without schema changes

     - Eliminate ~270 lines of schema maintenance


     If EDAM or another ontology eventually builds better coverage of genomic file content types, adopters can simply use those CURIEs in their `Term` values — no schema release needed.


     ## Summary


     1. **Why does `data_content` use a closed enum when every other vocabulary field uses `Term`?** This inconsistency seems unintentional.

     2. **The OutputType values are ENCODE-specific** and don't cover non-ENCODE data. A general-purpose schema shouldn't hardcode one project's internal vocabulary.

     3. **Switching to `Term` preserves ENCODE compatibility** while opening the field to any ontology or vocabulary.

     4. **The enum is a maintenance burden** — 270 lines of frozen ENCODE vocabulary with no update mechanism.

   - Latest comment text:

     No comments

5. **Issue #3 — Data representation/geometry of a GenomicAnnotation**
   - Created: 2024-12-10T17:09:27Z
   - Updated: 2026-02-25T15:58:29Z
   - Latest comment timestamp: 2026-02-25T15:58:29Z
   - Labels: None
   - Assignees: None
   - Body:

     GenomicAnnotations have a genomic geometry; this is what Sveinung referred to as the "geometric type" of the data. Example: does the data represent Points in a genome (single nucleotides), or Regions in a genome (with start/end coordinates)? (Alternative name possibility: "data geometry"?)


     One way I was thinking we could accommodate this is like so:


     Each of these variables is boolean:

     - are gaps allowed between elements?

     - do elements have lengths?

     	- if yes, are the lengths constant?

     	- if yes, may elements overlap?

     - do elements link to one another?

     - do elements have values?


     So, something like this:


     ```

     geometry:

       gaps: true

       lengths: true

       lengths-constant: true

       lengths-overlap: true

       links: true

       values: true

     ```

   - Latest comment text:

     @nsheff:


     I suggest naming it "data geometry" instead of track geometry, since this is useful beyond visualization.

6. **Issue #14 — Deliverable 2.3: Strategy for providing (persistent) identifiers**
   - Created: 2025-08-26T14:18:05Z
   - Updated: 2025-10-06T05:15:41Z
   - Latest comment timestamp: 2025-10-06T05:15:41Z
   - Labels: None
   - Assignees: None
   - Body:

     From the [Case statement of the WG (v1.1)](https://www.rd-alliance.org/wp-content/uploads/2024/11/FAIRification-of-Genomic-Annotations-WG-Case-Statement-v1.1.pdf):


     > **2.3. Strategy for providing persistent identifiers**

     > 

     > Adopting the FAIR principles

     > necessitates persistent identifiers (PIDs) on at least the collection level, preferably on a

     > file level. As a minimal solution, we can adopt the current FAIRtracks solution of a

     > combination of a DOI for a metadata deposition and a locally unique identifier within that

     > dataset. We will investigate the option of producing content-derived digests for this

     > purpose, building on experience from the [Sequence Collections GA4GH working group](https://ga4gh.github.io/refget/seqcols/)

     > and elsewhere. Other alternatives include adopting decentralised PIDs from the [dPID

     > Working Group](https://www.dpid.org/working-group) from [DeSci Labs](https://www.dpid.org/working-group).

   - Latest comment text:

     No comments

7. **Issue #13 — FGA-WG Metadata model version 0.9 finished!**
   - Created: 2025-07-04T14:32:53Z
   - Updated: 2025-10-05T21:28:15Z
   - Latest comment timestamp: 2025-10-05T21:27:06Z
   - Labels: None
   - Assignees: None
   - Body:

     I am happy to announce that I have finally finished the first full draft of the "FGA-WG Harmonised Metadata Model" (or whatever we will call it)!


     <img width="1078" height="966" alt="Image" src="https://github.com/user-attachments/assets/e26ec029-bf9a-46e6-86ed-d52b96a9ee1a" />


     Find the details in the [RDA Genomic Annotations metadata models and use cases spreadsheet](https://docs.google.com/spreadsheets/d/1wqlcnYHwT9yQVCj525n41LQJENbgHeQfn7V572e8ev8/edit?gid=1471635995#gid=1471635995)


     Finalisation of the first draft took way more effort than I imagined (but then again, I am always too optimistic). I have spent quite some time to test out and adapt the model according to a real-world example, which was this relatively randomly picked bigBed file from the [International Human Epigenome Consortium (IHEC) Data Portal](https://epigenomesportal.ca/ihec/grid.html):


     ![Image](https://github.com/user-attachments/assets/f191faba-d54a-44ed-8068-b202aea27e70)


     The reason for using IHEC was to illustrate one use cases of the FileCollection entity, however since the metadata returned from IHEC was rather limited, most of the metadata used for the test example came from ENCODE.


     An interesting point was that the bigBed file in question did not contain any identifiers that made me able to link it to the related ENCODE metadata – I had to rely on the MD5 checksum to confirm the identity! As such, this is a great example of the usefulness of a file-level identifier solution, e.g. a content-derived annotation file digest.


     I'll write up some overall considerations and changes soon, and try to tidy up the issues a bit.

   - Latest comment text:

     @sveinugu:


     Simplified version of UML diagram:


     <img width="1055" height="814" alt="Image" src="https://github.com/user-attachments/assets/1093c625-c17f-42c8-9992-8513ea085196" />

8. **Issue #9 — Deliverable 2.2: Strategy for persistent and public deposition of harmonised metadata**
   - Created: 2025-02-04T17:21:41Z
   - Updated: 2025-10-02T14:04:16Z
   - Latest comment timestamp: 2025-10-02T14:04:16Z
   - Labels: None
   - Assignees: None
   - Body:

     ## From the [Case statement of the WG (v1.1)](https://www.rd-alliance.org/wp-content/uploads/2024/11/FAIRification-of-Genomic-Annotations-WG-Case-Statement-v1.1.pdf):


     > **2.2. Strategy for persistent and public deposition of harmonised metadata**

     > Community trust in the availability of FAIR metadata on genomic annotations depends on a common

     > strategy for permanent storage of such metadata in public repositories. We will also need

     > to define and implement a simple registry of relevant metadata depositions


     ## Minutes from meeting Jan 29, 14-15 UTC 

     Present: @bianchini88, @egchristensen, @sveinugu


     1. @sveinugu presented a conceptual illustration of FGA-WG core infrastructure:

         <img src="https://raw.githubusercontent.com/fairtracks/fga-wg/refs/heads/materials/material/images/fga_wg_overview.png" alt="FGA-WG core infrastructure" width="300px">

         * This relates the subtask "Strategy for persistent and public deposition of harmonised metadata" with the other subtasks and ideas.

         * The actual metadata registry / search provider is out of scope of the WG, however we intend to provide a simple way for harvesters to locate harmonised metadata (aim of this subtask), and a unified search API for downstream users to search across databases (other subtask).


     2. @sveinugu recapped related recommendations from the [FAIRtracks paper](https://doi.org/10.12688/f1000research.28449.1), in particular:

         * From ["F1: (Meta)data are assigned a globally unique and persistent identifier"](https://f1000research.com/articles/10-268/v1#d354463e1851):

             > For now, we are leveraging the widespread adoption of the document identifier (DOI) by requiring a FAIRtracks document to be published and identified with a DOI. We require the publisher to support DOI versioning and also the possibility of reserving a DOI prior to publication (to include the DOI in the published file itself). We currently recommend using Zenodo as the publishing platform, as the service supports both features, but other platforms are also possible as long as both DOI versioning and reservation are possible. FAIRtracks is easily extendable to support other global identifier types.

         * From F3: Metadata clearly and explicitly include the identifier of the data they describe:

             > As FAIRtracks requires a global identifier for the metadata document itself (using DOI), it should be possible to uniquely identify a track file from a joint identifier containing the DOI of a FAIRtracks document and the local identifier for a track file within that document.

         * From A2: Metadata are accessible, even when the data are no longer available:

             > As a minimum, track metadata should persist. Even though Track Hub Registry (THR) and TrackFind could technically be able to fill such a role, we choose to depend on existing persistent repositories using DOI identifiers (e.g., Zenodo, see F1), as the operational model of THR allows submitters to delete their submissions, while the architecture of TrackFind is primarily designed around its search functionality. Zenodo provides storage connected to the CERN project infrastructure, to be maintained for at least 20 yearsxliii.

         * To recap:

             * Harmonised metadata published and made available with DOI. Three main requirements for a publishing platform:

                 * DOI versioning, preferably one static DOI (pointing to latest version) + versioned DOIs

                 * Preregistration of DOIs - to include self-referring DOIs in the published metadata

                 * (Semi-)permanent storage

             * Locally unique identifiers (within a metadata submission) for:

                 * Single files

                 * Collection of files

             * Combination of DOI + local identifiers = globally unique identifier

             * Issue:

                 * How to relate to files within a submission? One solution would be to just have one consistently named file within a submission. Also, some publishing platforms might support file-level DOIs.


     3. @egchristensen introduced the ISO/IEC 11179 standard for metadata registries, which he is investigating independently of the FGA-WG. Consensus: While this standard most likely has useful concepts/solutions, a "metadata registry" mainly refers to the third-party search services that are out-of-scope. @egchristensen will, however, update us with relevant info from the standard as he looks into it.


     4. There is a need of some sort of simple registry with an overview of all published metadata, as a starting point for automatic harvesting:


         * This could be as simple as a list of DOIs in a GitHub repo.

         * Some solution to notify that there is an update (new entry or update) would be highly useful!

       

     5. We discussed how DOIs work and concluded that we needed more knowledge. Hence, we agreed on three ACTION POINTS:

         - [ ] Investigate the metadata model of the DOI standard [Evan]

         - [ ] Investigate solutions for file-specific DOIs [Sveinung]

         - [ ] Investigate DOI versioning [Federico]

   - Latest comment text:

     @sveinugu:


     > [@sveinugu](https://github.com/sveinugu), [@nsheff](https://github.com/nsheff) and I spoke in-person at GA4GH April Connect 2025 (Cambridge, MA, USA) about how we should structure identifiers for annotations.

     > 

     > A phased approach to identifiers will likely be required to balance standardization and ease of implementation:

     > 

     > 1. First phase, an identifier will be required but we will not specify how the identifier should be formatted/structured.

     > 2. Second phase, an identifier will required to conform to a specific format/structure.

     > 3. Third phase, an identifier will be required to be persistent.

     > 

     > This is just an idea that came out of our discussions and I wanted to record it here. The group should discuss this phased approach in a future meeting. We should continue to explore the role that DOIs can play in identifying/referencing/dereferencing annotations.


     Just for cleanup, I believe this comment really belongs to issue https://github.com/fairtracks/fga-wg/issues/14, which we also discussed in the last WG meeting, Sep 30: https://docs.google.com/document/d/1qIsNUsi9WqnDCrKj7wyRRNApOuvw_23z4Mpt3uIOE8o/edit?tab=t.0

9. **Issue #7 — Sample models - the next Biosample concept**
   - Created: 2025-02-01T16:15:36Z
   - Updated: 2025-10-01T08:48:53Z
   - Latest comment timestamp: 2025-10-01T08:47:00Z
   - Labels: None
   - Assignees: None
   - Body:

     This issue is to initiate a discussion on how to best represent the concept (and properties) of the biological sample, on which experiments are run and genomic annotations derived.


     Known models:


     ###  ENCODE

     It is centered everything on the Experiment, which includes many Biosamples, from which many Replicates are produced, to which Files belong (sometimes with a many-to-many cardinality as files may be combined from multiple replicas).

     http://encodeproject.org/profiles/biosample_type

     http://encodeproject.org/profiles/biosample

     http://encodeproject.org/profiles/biosample_characterization


     Allowed values in Biosample classification are:

     - cell line

     - tissue

     - primary cell

     - whole organisms

     - in vitro differentiated cells

     - cell-free sample

     - organoid

     - technical sample


     As reported in https://www.encodeproject.org/help/data-organization/, when biosamples are of a specific classification, their values are mapped onto Ontologies, specifically


     - Tissues: [Uber Anatomy Ontology](http://uberon.org/) (UBERON)

     - Primary cells: [Cell Ontology](http://cellontology.org/) (CL)

     - Cell lines: [Experimental Factor Ontology](http://www.ebi.ac.uk/efo/) (EFO) and [Cell Line Ontology](http://www.clo-ontology.org/) (CLO)


     (note that, when a disease is associated with a biosample, the value are harmonized against the Disease Ontology](https://disease-ontology.org/) (DO))


     ###  Genomic Data Commons 

     It is centered on the Patient concept, from which multiple Samples are derived. From another perspective, data are divided by Project, associated with a Tumor Type, for which many Data Types are available (https://gdc.cancer.gov/developers/gdc-data-model).

     Here, biosamples are a sub entity of Biospecimen: they mainly represent tissue of tumor/healthy patients. 

     This is their schema https://docs.gdc.cancer.gov/Data_Dictionary/viewer/#?view=table-definition-view&id=sample


     Here, what is captured is the tissue type, the conditions/means of preservation, the presence of tumor, etc.


     ###  Gene Expression Omnibus

     It is organized into Series that include Samples (whereas these latter ones can be employed in multiple Series), sequenced with a Platform. (see model [here]((https://www.semanticscholar.org/paper/Gene-Expression-Omnibus-(GEO)-Barrett/a60820b4671d0f4f169c802e5fdddc920192ab60/figure/0)))


     Here the set of allowed values is less clear (e.g., https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM1565792 has "monocyte-derived dendritic cells"), we should investigate how they homogenized values in https://www.ncbi.nlm.nih.gov/biosample.


     ### BioSample EBI (https://www.ebi.ac.uk/biosamples/)

     Here sample types seem to be (not very harmonized...)

     https://doi.org/10.1093/nar/gky1061


     metagenomic assembly

     cell culture

     tissue sample

     whole organism

     stool

     feces

     single cell

     skin

     Cell culture


     ### FAIRtracks


     ID

     Species

     Biospecimen class

     Sample type

     - Cell type

     - Abnormal cell type

     - Cell line

     - Organism part

     - Details

     - Summary

     Phenotype


     ### GeCo


     Entity: BioSample	

     - BioSampleId

     - SourceId

     - Type ("ESC derived cell line", "Primary cell", "Primary culture", "In vitro differentiated cells", "Primary tissue", "Tissue", "Cell line")

     - Tissue

     - CellLine

     - IsHealthy

     - Disease


     Entity Donor (from which the Biosample may be derived)	

     - DonorId

     - SourceId

     - Species

     - Age

     - Gender

     - Ethnicity


     Here is some material to start from. @sveinugu would you like to comment on your experience/ideas or should we setup a meeting?

   - Latest comment text:

     @sveinugu:


     > It was the example content structure. Completely agree that they are all important format fields. e.g. combined the taxonomy id and scientific name in the same field as a JSON was what I was querying. Want to learn more about why the complexity, I can see it gives flexibility. What db would handle these well? Mongo? If you are going to Uppsala for the GA4GH next month can discuss over a tea.


     Right, misunderstood you, then. So the reason for the JSON blobs is that we want to include both IDs and labels for ontology terms, to not require downstream services to implement ontology lookup just to present the choice to a user. This defined in a separate Term entity with two fields. However, in the examples, the content is represented as a JSON blob as we otherwise would need to make use of a remote key for the relation. The same is done for all the other sub-entities demarked with a diamond in the [UML diagram](https://github.com/fairtracks/fga-wg/issues/13#top). So the representation in our examples is currently a combination of hierarchical and relational JSON records, something which is supported by e.g. both PostgreSQL and JSON-LD.


     I'll be inn Uppsala next week, so happy to chat there!

10. **Issue #12 — Schema representation formats**
   - Created: 2025-03-18T15:37:35Z
   - Updated: 2025-09-30T13:54:55Z
   - Latest comment timestamp: 2025-09-30T13:54:54Z
   - Labels: None
   - Assignees: adamjohnwright
   - Body:

     @adamjohnwright and @sveinugu 


     This is the GitHub issue for sub-task 1. 


     I remember discussions about JSON schema, possibly generated with automated tool which convert a YAML schema file into a JSON schema file. 


     Can one of you recall exactly which data schema we are talking bout in this issue? Any link of reference to previsou meeting is good.

   - Latest comment text:

     @Nelly-Barret:


     Hi all,


     I am done with implementing the LinkML schema. (I did it by hand to avoid "hallucinated results" from ChatGPT.)


     Mainly:

     - There is one file per entity. Each entity has:

         - an **id**

         - a section **classes** which contains its description and the list of its attributes 

         - (optionally a section **enums** to describe permissible values of some attributes)

         - a section **slots** which contains the description/type of each attribute


     In the spreadsheet (https://docs.google.com/spreadsheets/d/1wqlcnYHwT9yQVCj525n41LQJENbgHeQfn7V572e8ev8/edit?gid=1471635995#gid=1471635995) I have coloured in orange the cells that are missing information, mainly:

     - when there are two suggested data types (which one to use in the LinkML schema)

     - when the string is specified to be smaller than 60 chars (but there is a question mark which indicates that we are not sure about this restriction)

     - Incomplete "Required if"


     We can discuss this offline or next time!

11. **Issue #18 — Branding/naming of the outputs/infrastructure/community?**
   - Created: 2025-09-02T14:40:25Z
   - Updated: 2025-09-19T14:39:30Z
   - Latest comment timestamp: 2025-09-19T14:39:30Z
   - Labels: None
   - Assignees: None
   - Body:

     FAIRtracks 2.0?

     Other ideas?

   - Latest comment text:

     @sunbrn:


     I would be happy with the FAIRgnomix choice. Thank you for playing with ChatGPT and proposing the idea.

12. **Issue #20 — Manuscript for Deliverable 1: Recommendations for a Minimal FAIR Metadata Schema**
   - Created: 2025-09-02T14:50:30Z
   - Updated: 2025-09-02T15:35:33Z
   - Latest comment timestamp: 2025-09-02T15:35:33Z
   - Labels: None
   - Assignees: None
   - Body:

     As discussed at the FAIRification of Genomic Annotations Working Group meeting on 19 August 2025, @egchristensen and Francis P. Crawley have agreed to contribute to the development of the WG’s draft Recommendations for a Minimal FAIR Metadata Schema. Ryan O'Connor put together a document to start developing this [here](https://docs.google.com/document/d/1SMbx1I1wXKn4sB3D642CA8tz_21-HZgquMUoCYTokzA/edit?tab=t.0#heading=h.416xjwo5gl99) (also saved in the WG’s shared workspace folder). 


     There isn’t a template as such that RDA Recommendations need to conform to; the structure and content is at the discretion of the WG members and co-chairs. That being said, some of the information on the RDA website on the [submission guidelines](https://www.rd-alliance.org/recommendations-and-outputs/recommendations-guidelines/) may be of use. 


     What also might be of use is to scan through some other related Recommendations which Ryan pulled together here: 


     - Scholix Metadata Schema for Exchange of Scholarly Communication Links: https://doi.org/10.5281/zenodo.1120265

     - Metadata Schema for the Persistent Identification of Instruments: https://doi.org/10.15497/RDA00070 

     - Recommendations for a minimal metadata set to aid harmonised discovery of learning resources: https://doi.org/10.15497/RDA00073 


     We put down a deadline of 16 September 2025 to give the rest of the WG an update on this.

   - Latest comment text:

     @sveinugu:


     #16 is also relevant here

13. **Issue #11 —  Deliverable 2.4: Define uniform search API for downstream services and end users**
   - Created: 2025-03-18T14:24:33Z
   - Updated: 2025-09-02T15:32:45Z
   - Latest comment timestamp: 2025-09-02T15:32:36Z
   - Labels: None
   - Assignees: None
   - Body:

     This issue provides a starting point to initiate discussion of a Genomic Annotations search API standard.


     ## Overview of search API


     One of the proposed deliverables of our working group was a specification for  *Search API*. Basically, this would be a standardized way API for searching for GenomicAnnotation files. Providers of Genomic Annotations could implement this search API, which would allow tools to aggregate across providers more easily.



     ## Questions


     - How will we identify a GenAnno? One option is just by a human-readable string. Another option is by namespace/genanno_name, like `bedbase/chip_seq4`.  Another option is by some kind of unique identifier, ideally something deterministic, like a content-derived hash.

     - Do they need to be versioned? It's probably not that important; it's not a major need to version a BED file, for example, and it could just be uploaded as another independent bed file with versions added on external to the API. But a GFF definitely could be. So, this means there should probably be different APIs for different data types.

     - Versions kind of go with identifiers; Maybe we would need to solve the identifier problem before we can finalize the search API.


     ## Some initial endpoint ideas


     These are just a few thoughts to get started.

     - can we just model the specification after the [GA4GH Schema registry specification](https://ga4gh.github.io/schema-registry/)? There are some similarities but also some differences, so it's not a perfect fit, but could be a reasonable starting point.

     - I think the actual retrieval of the files/bytes should follow the [GA4GH DRS specification](https://ga4gh.github.io/data-repository-service-schemas/preview/release/drs-1.2.0/docs/).


     1. List genomic annotations by namespace

     2. Get metadata for one genomic annotation

     3. Get info about DRS object (DRS endpoint)

     4. Get a URL for fetching bytes (DRS endpoint)


     ---


     1. List genomic annotations by namespace

     	- Endpoint: `GET /genannos/{namespace}/?attr1=val1`

     	- Params:

     		- `{namespace}` - The name of a user or organization that owns these annotation files

     		- `?{attr1}={value1}` - query key-value pairs to filter response.

     	- Returns: An array with a list of genomic annotation metadata meeting the filter.

     		```

     		{

     		  "namespace": "some-namespace",

     		  "genannos": [

     		    {

     		      "genanno_name": "my_genanno_name",

                            ...

     		    }

     		  ]

     		}

     		```

     	

     2. Get metadata for one genomic annotation

     	- Endpoint: `GET /genannos/{namespace}/{genanno_name}`

     	- This would provide metadata, including the `genanno_id` (unique identifier for this file).


     3. Get info about DRS object (DRS endpoint)

     	- Endpoint: `GET /objects/{genanno_id}`

     	- Returns: object metadata and list of access methods that can be used to fetch object bytes.


     4. Get a URL for fetching bytes (DRS endpoint)

     	- Endpoint `GET /objects/{object_id}/access/{access_id}`

   - Latest comment text:

     @sveinugu:


     From the [Case statement of the WG (v1.1)](https://www.rd-alliance.org/wp-content/uploads/2024/11/FAIRification-of-Genomic-Annotations-WG-Case-Statement-v1.1.pdf):


     > **2.4. Define uniform search API for downstream services and end users** 

     > To facilitate adoption by end users and integration with software tools, we will define a 

     > standardised API for downstream search and discovery that works independently of any particular

     > implementation of a search service. This will build on experience from the [GenoSurf](http://geco.deib.polimi.it/genosurf/),

     > [TrackFind](https://trackfind.elixir.no/), [IHEC data portal](https://epigenomesportal.ca/ihec/) and similar search services as well as from downstream

     > users of such APIs, such as developers of analysis software (e.g. [LOLA](https://doi.org/10.1093/bioinformatics/btv612) and 

     > [GSuite HyperBrowser](https://doi.org/10.1093/gigascience/gix032)), as well as direct use by analytical end users.

14. **Issue #17 — Deliverable 3. Proof-of-concept integrations of third-party services with core infrastructure**
   - Created: 2025-08-26T14:45:12Z
   - Updated: 2025-09-02T15:28:12Z
   - Latest comment timestamp: 2025-09-02T15:28:12Z
   - Labels: None
   - Assignees: None
   - Body:

     From the [Case statement of the WG (v1.1)](https://www.rd-alliance.org/wp-content/uploads/2024/11/FAIRification-of-Genomic-Annotations-WG-Case-Statement-v1.1.pdf):


     > These integrations will be primarily developed through the initiative of FGA-WG members and in

     > their particular research context as integrations with other projects. The work that should be

     > counted towards the FGA-WG entails mainly coordination and exchange of ideas and

     > experience, as well as the improvements and modifications needed on the infrastructure side to

     > facilitate the integrations. The deliverable will be in the form of a report.

     > 

     > _3.1. Metadata transformation pipelines:_ Data pipelines (following Recommendation 2.1)

     > developed to transform metadata from particular data sources to conform to the minimal

     > metadata schema (Recommendation 1) and deploy compliant metadata which is made

     > uniquely identifiable with PIDs (Recommendation 2.3) into permanent public storage

     > (Recommendation 2.2).

     > 

     > _3.2. Search service implementations:_ At least one search service that imports metadata

     > from permanent storage (Recommendation 2.2) and implements the standardised search

     > API (Recommendation 2.4).

     > 

     > _3.3. Tool integrations:_ Integration of the search API in downstream tools and libraries.

     > 

     > _3.4. Track hub integrations:_ Improved integration with the track hub-based infrastructure

     > to improve the generation, discovery and distribution of data hosted as track-hubs. This

     > will build on the existing collaboration with the [Track Hub registry](https://trackhubregistry.org/) and the [Ensembl

     > genome browser](https://www.ensembl.org/index.html) through the [FAIRtracks project](https://fairtracks.net/), but will also be open for other collaborations.

   - Latest comment text:

     No comments

15. **Issue #15 — Deliverable 2.1: Create guidelines for enabling scalable and maintainable metadata transformation pipelines**
   - Created: 2025-08-26T14:22:05Z
   - Updated: 2025-09-02T15:16:34Z
   - Latest comment timestamp: 2025-09-02T15:16:34Z
   - Labels: None
   - Assignees: None
   - Body:

     From the [Case statement of the WG (v1.1)](https://www.rd-alliance.org/wp-content/uploads/2024/11/FAIRification-of-Genomic-Annotations-WG-Case-Statement-v1.1.pdf):


     > **2.1. Guidelines for enabling scalable and maintainable metadata transformation

     > pipelines:**

     > 

     > To allow for the continuous evolution of e.g. metadata schemas, ontologies, or

     > data sources, there is a need to define best practices for scalable and maintainable

     > pipelines that transform metadata from existing sources to fit our minimal schema. The

     > new [Omnipy](https://omnipy.readthedocs.io/) Python library is a possible framework for developing and orchestrating

     > such metadata mapping/transformation flows; it has been designed with this exact use

     > case in mind. We will also build on experience and code from other projects, such as the

     > ones listed under Recommendation 1 above. We furthermore aim to contribute to and

     > exchange experiences with the upcoming [FAIR Mappings WG](https://www.rd-alliance.org/groups/fair-mappings-wg/activity/).

   - Latest comment text:

     No comments

16. **Issue #19 — Summarize User Stories**
   - Created: 2025-09-02T14:48:00Z
   - Updated: 2025-09-02T14:48:00Z
   - Latest comment timestamp: 2025-09-02T14:48:00Z
   - Labels: None
   - Assignees: None
   - Body:

     The working group collected 12 use cases in [this document](https://docs.google.com/document/d/1UPSXoMKLL6uH4Rx3xeXXFevGuq_B4DMsHic-O6b0Cpw/edit?tab=t.0#heading=h.732pbeju2dkk) in October 2024. 


     I classified actors into one of three types using my own subjective classification. I also consolidated the use cases into four user stories that I think capture the needs set out by each group at a high level. 


     Actors can be classified as:

     - **Annotators** which produce and/or curate genomic annotation data and metadata.

     - **Brokers** which publish and/or develop repositories used to publish genomic annotation data and metadata.

     - **Users** which include individuals (i.e. analysts and/or researchers) that need to access and use genomic annotation data and metadata.


     All actor types expressed a need for a single, well-documented API to search for genomic annotations. Users (specifically) would like this API to help them figure out which resources contain data relevant to a particular query. Such search capabilities could enhance data discovery and streamline retrieval of data relevant to their analysis or research. Individual members of all actor types went on to detail that they would like to be able to identify and access the sources that were used in an analysis or to build a resource. Actors cited barriers sharing their own genomic annotations, assessing the relevance and quality of genomic annotations generated previously (especially those found in BAM files), and understanding whether two or more resources (i.e. knowledgebases) are built upon the same framework of knowledge and/or tooling. A couple actors also expressed interest in decoupling genomic annotation metadata from a particular species or genome build to enable more precise tracking of workflows and tools used to generate an annotation, especially in cases where annotations may be updated more than once within a genome build and where annotations may span multiple genome builds. The description, administration, and structure of genomic annotations would stand to benefit from standardization.


     The types of data and domains of research cited by use-case submitters include (in no particular order):

     - Reference annotations

     - Somatic variation representation

     - Cancer research (general)

     - Epigenomics research

     - Population-level variation statistics

     - Model organism research

     - Biodiversity research


     Please see the attached diagram for a visualization of individual use cases, actors, and consolidated user stories. We should discuss as a group whether the use cases as described are sufficient for building an API or if we should re-approach the user community for additional use cases.


     ![Image](https://github.com/user-attachments/assets/dec64667-e050-4d70-8db4-1733cea9ba42)


     If you'd like to view the diagram on Lucidchart, [here's a link](https://lucid.app/lucidchart/809bf791-3f85-4a3c-b7e0-8143889ed7e4/edit?viewport_loc=292%2C1631%2C2105%2C1039%2C33ml~.f-Hnbv&invitationId=inv_4f2951ba-b1ec-4dcb-86b3-4c387d66e0f4). Please note that you may be required to make a free Lucid account. If you are based at an academic institution, I'd recommend making the account with your institutional email address so you get access to additional features for free. You can find additional instructions [here](https://help.lucid.co/hc/en-us/articles/360049831771-Sign-up-for-a-free-Educational-account). If for whatever reason, Lucid doesn't recognize your institutional email and automatically give you the additional features, fill out the form on the instructions page to send a ticket to customer support. They should respond fairly quickly during normal business hours in Mountain Daylight Time (UTC -6).

   - Latest comment text:

     No comments

17. **Issue #5 — Align Annotation schema with GA4GH DRS standards or other standard for data access (e.g. FAIR digital objects)?**
   - Created: 2025-01-21T14:43:25Z
   - Updated: 2025-09-02T13:55:20Z
   - Latest comment timestamp: 2025-09-02T13:55:20Z
   - Labels: None
   - Assignees: None
   - Body:

     We discussed extending the simple `file_url` field from the [`Track`](https://github.com/fairtracks/fairtracks_standard/blob/master/docs/fairtracks_track.md) schema of FAIRtracks to a access-method + url format, in line with the [`AccessMethodModel` of the GA4GH DRS standard](https://ga4gh.github.io/data-repository-service-schemas/preview/release/drs-1.2.0/docs/#tag/AccessMethodModel). 


     This object is, however, part of the larger [DRS Object Model](https://ga4gh.github.io/data-repository-service-schemas/preview/release/drs-1.2.0/docs/#tag/DrsObjectModel), which also includes fields like `id`, `name`, `description`, and `checksum`, raising the issue of a closer alignment/adoption? (`checksum` is also a part of the FAIRtracks schema that should be supported somehow.)


     However, in the RDA context, FAIR digital objects is a related standard that I believe covers some of the same territory. And there are possibly others?


     I believe we should gather more information about these and other alternatives and discuss alignment with other standards on file/data access.

   - Latest comment text:

     @sveinugu:


     The DRS object model is included in [v0.9 of the data model](https://github.com/fairtracks/fga-wg/issues/13), as a number of fields in the `File` entity, and related entities (`AccessMethod`, `AccessURL`, and `Checksum`).


     Remaining issues include:

     - [ ] Consider excluding blob-related and other subfields of DRS, as suggested in the model

     - [ ] Follow up on the issue in the [DRS repository to make DRS compatible with RO-crates](https://github.com/ga4gh/data-repository-service-schemas/issues/413)

18. **Issue #6 — Data use fields (Annotation and/or elsewhere)**
   - Created: 2025-01-21T14:55:35Z
   - Updated: 2025-09-02T13:49:40Z
   - Latest comment timestamp: 2025-09-02T13:49:40Z
   - Labels: None
   - Assignees: None
   - Body:

     While adding fields for data use was planned for FAIRtracks 2.0, it was never finalised. The natural idea is to make use of the [GA4GH Data Use Ontology](https://www.ga4gh.org/product/data-use-ontology-duo/) for this, however, we should also investigate RDA-related alternatives/principles.


     From the WG Case statement (added in response to feedback from the RDA Technical Advisory Board):


     "CARE principles for Indigenous Data Governance: Endorsed and maintained by the Global

     Indigenous Data Alliance (GIDA), the [CARE principles (Collective benefit, Authority to control,

     Responsibility, and Ethics)](https://www.gida-global.org/care) are process-oriented principles aimed to complement the more

     data-oriented FAIR principles. The aim of the CARE principles is to balance the emphasis on

     greater data sharing with the needs of Indigenous Peoples to assert greater control over the

     application and use of indigenous data and knowledge for collective benefit. We will investigate

     how the CARE principles can be applied to the FGA-WG outputs, in coordination with the

     [International Indigenous Data Sovereignty IG](https://www.rd-alliance.org/groups/international-indigenous-data-sovereignty-ig/). In particular, fields in the harmonised metadata

     model that describe limitations on data usage will be aligned with the CARE principles. We will

     also investigate the use of the Labels and Notices from the [Local Contexts](https://localcontexts.org/) project."


     This is also very relevant in relation to the 25th RDA Plenary as part of the [International Data Week 2025 (IDW 2025): Data for positive change: Empowering communities and advancing research](https://www.rd-alliance.org/event/international-data-week-2025-brisbane-australia/) in Australia this autumn.


     A technical question is whether data use fields should be placed as part of the `Annotation` schema (per-file), or in another schema (e.g. Study), or both.

   - Latest comment text:

     @sveinugu:


     - [ ] Not yet handled in [v0.9 of the data model](https://github.com/fairtracks/fga-wg/issues/13)

19. **Issue #2 — Data interpretation field for a GenomicAnnotation**
   - Created: 2024-12-10T17:07:32Z
   - Updated: 2026-02-25T15:53:42Z
   - Latest comment timestamp: 2025-09-02T13:44:49Z
   - Labels: pending
   - Assignees: None
   - Body:

     One of the fields for the Annotation entity is the "data interpretation". What do the entities actually represent? For example, a GenomicAnnotation with geometry of "Point" could represent SNPs, or it could represent CpG dinucleotides. A GenomicAnnotation with a geometry of "Region" could represent  "peaks", the results of a peak-calling algorithm, or they could also represent "reads" from a sequencing experiment. (Alternative name possibility: "entity type"?)


     There are really probably 2 things here; one is something biological, and the other describes a process.


     For example: peak calling: https://bioportal.bioontology.org/ontologies/EDAM?p=classes&conceptid=http%3A%2F%2Fedamontology.org%2Foperation_3222


     But this is a process; we really needed things called "peaks" which represents the output of a process.



     Then for biological things, we need things like "CpGs" or SNPs.


     I did find in EDAM the term SNP:

     - term is here: https://bioportal.bioontology.org/ontologies/EDAM/?p=classes&lang=en&conceptid=http%3A%2F%2Fedamontology.org%2Fdata_2092&jump_to_nav=true

     -  http://edamontology.org/data_2092

     - it says obsolete, replace by "Nucleic acid features", which doesn't make sense


     So it seems like we would need to make quite a few changes here.

   - Latest comment text:

     @sveinugu:


     Mapping from the 7 aspects of "interpretation" to fields in [v0.9 of the data Model](https://github.com/fairtracks/fga-wg/issues/13):


     1. Types of sequence features contained within this file (GFF type column, Transcription Factor binding site)

       - Covered by`GenomicAnnotationFile.sequence_features`

     2. Related biological processes/chemical reactions, e.g. DNA methylation, transcription factor binding

       - Covered by`Experiment.biological_processes`

     3. What values in a file represent (type of measure)

       - Partly covered by `File.data_content` (ENCODE vocabulary) 

     4. What is being measured (level of methylation)

       - Partly covered by `File.data_content` (ENCODE vocabulary) 

     5. Molecule of interest (DNA, miRNA, ...)

       - Covered by `Experiment.molecule_type` (from GA4GH Experiment metadata core fields)

     6. Sequence library-related (E.g. ChIP-seq antibody)

       - Partly covered by `Experiment.antibody_target` (from GA4GH Experiment metadata extended fields, extensions for other types of assays/sequencing data will be added in the next round)

     7. Algorithm-related type of data (Broad peak, Signal)

       - Handled by `File.data_content` (ENCODE vocabulary)


     Remaining subissues include:

     - [ ] Consider whether values/measures (3 & 4) is well enough covered

     - [ ] Follow GA4GH Experiments metadata to add new data-specific fields and contribute if needed

20. **Issue #1 — Data formats in EDAM ontology for a GenomicAnnotation**
   - Created: 2024-12-10T16:20:07Z
   - Updated: 2026-02-25T15:49:03Z
   - Latest comment timestamp: 2025-09-02T13:31:08Z
   - Labels: wontfix
   - Assignees: None
   - Body:

     At the meeting on 2024-12-03, we discussed data/file formats. On an Annotation entity, in the data format field, we would like the terms to comply to some vocabulary, and the EDAM 'Sequence annotation track format' could be a possible ontology source for allowed terms for this field. We asked everyone to look at the formats in the current EDAM ontology and see if there is anything missing or needing to be changed.


     Those formats are here:


     https://bioportal.bioontology.org/ontologies/EDAM?p=classes&conceptid=http%3A%2F%2Fedamontology.org%2Fformat_2919


     Which looks like this:


     ![image](https://github.com/user-attachments/assets/22c07adf-06a6-447e-9eb9-029d70b32c95)

   - Latest comment text:

     @sveinugu:


     v0.9 of the data model contains a single ontology term field "file_type" in the "File" entity: https://github.com/fairtracks/fga-wg/issues/13


     Remaining subissues raised in the above include:

     - [ ] Adding file-format specific properties to the data model?

     - [ ] Cleaning up the file format part of EDAM

     - [ ] Evaluate the [file format tab of the spreadsheet](https://docs.google.com/spreadsheets/d/1wqlcnYHwT9yQVCj525n41LQJENbgHeQfn7V572e8ev8/edit?gid=56160221#gid=56160221) - are we covering the relationships expressed there

21. **Issue #16 — Review of existing metadata models**
   - Created: 2025-08-26T14:31:46Z
   - Updated: 2025-08-26T14:31:46Z
   - Latest comment timestamp: 2025-08-26T14:31:46Z
   - Labels: None
   - Assignees: None
   - Body:

     First tab of Google sheet: https://docs.google.com/spreadsheets/d/1wqlcnYHwT9yQVCj525n41LQJENbgHeQfn7V572e8ev8/edit?gid=0#gid=0

   - Latest comment text:

     No comments

22. **Issue #10 — Selection of ontologies**
   - Created: 2025-02-18T06:24:58Z
   - Updated: 2025-02-26T15:01:46Z
   - Latest comment timestamp: 2025-02-26T15:01:45Z
   - Labels: None
   - Assignees: None
   - Body:

     While the selection of particular ontologies depends on the fields we specify, I just wanted to create an issue for collecting such discussions. 


     Mainly, I wanted to share this preliminary result from the [GA4GH Data Model and Schema Consensus (DaMaSC) group](https://www.ga4gh.org/product/data-model-and-schema-consensus-damasc/), which lists GA4GH-recommended ontologies:


     ![Image](https://github.com/user-attachments/assets/12b4e6a9-7cd2-48ad-85e7-fbd23cc8c905)


     Note that EDAM is not listed, but there is also no other ontologies with the same scope. I have already suggested this addition, but can follow up that.

   - Latest comment text:

     @sveinugu:


     Regarding taxonomy, there is also now this: https://unieuk.net/

## Recommended next actions

- Triage the newest schema-question issues (#23–#26) in a single maintainer review pass and convert accepted decisions into linked schema/documentation tasks.
- Separate long-horizon deliverable issues from schema-design questions so planning and technical discussion do not compete in the same queue.
- Close or relabel stale resolved discussions after confirming whether their outcomes already landed in the schema or docs.

## Suggested labels to create

- `needs-decision` — highlights issues blocked on working-group consensus rather than implementation effort.
- `deliverable` — distinguishes project-management deliverables from schema/model design work.
- `schema-design` — groups questions that affect LinkML structure, classes, slots, or controlled vocabularies.
- `stale-review` — flags older issues that need confirmation, closure, or a refreshed owner.
