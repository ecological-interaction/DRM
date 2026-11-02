# DRM v1.0 Development Roadmap

**Status — 1 November 2026:** Phases 1–3 completed their documented development
work. The AMRKB and OSDS bounded documentary preservation pilots were separately
accepted and Phase 4 closed. DRM-MSP 0.1.0 review revision 2 remains a candidate,
not generally adopted/released. **Phase 5 is not authorised; Phases 5–8 are future work.**

This is the sole eight-phase development sequence. A–F are iterative methods for
individual databases, not these release phases. The sections below preserve each
phase's objective, scope, inputs, tasks, outputs, criteria and review gate. They
describe phase requirements; they do not reverse the current status above or grant
execution/publication permission. Private source documents and detailed audit
crosswalks are not included; see [provenance](PROVENANCE.md) and [decisions](DECISIONS.md).

## Phase 1 — Historical Recovery and Baseline

**Objective:** Establish the verified historical foundation for the new specification.

**Scope:** Historical specifications, audits, requirements, narrative revisions and reported implementations; no software implementation or database changes.

**Inputs and dependencies:** Approved planning architecture, pinned repository inputs, recovered core and historical conversation record. Obtain Phase 1 authorisation first.

**Main tasks:** Inventory repository/evidence; record revisions and hashes; review the v0.1.0 core; extract historical requirements; distinguish narrative revisions from versioned artefacts; assess v0.2.0–v0.5.0 and audits A–D; register evidence; compare architectural decisions; assign requirement dispositions. The full baseline evidence is retained privately; public derivation limits are summarised in PROVENANCE.md.

**Deliverables:** Historical Evidence Register; Requirements Crosswalk; DRM Baseline Audit, to be created only during Phase 1.

**Completion criteria:** Every recovered requirement has a source, evidence status and disposition; missing packages and implementation evidence are explicit, not invented. No unqualified completeness claim with unresolved critical gaps.

**Approval gate:** Owner reviews and approves the baseline before Phase 2; no full implementation begins before that approval.

## Phase 2 — Methodological Consolidation

**Objective:** Establish a coherent normative methodological framework for heterogeneous databases.

**Scope:** Twelve historical principles, iterative A–F stages, profile contract, domain boundaries and conformance framework.

**Inputs and dependencies:** Approved Phase 1 evidence/dispositions and planning architecture; historical candidates are not automatically normative.

**Main tasks:** Consolidate twelve principles; restore A–F and evidence gates; review the ten-part domain-profile contract; define mandatory/recommended/optional levels; preserve resource/record/assertion distinctions, rights, design accountability and source authority; define boundary assessment and separate conformance from scientific validity.

**Deliverables:** DRM Methodological Architecture, reviewed before it becomes normative; resolved requirements and profile/conformance decisions.

**Completion criteria:** Framework describes and evaluates heterogeneous databases without imposing a universal scientific ontology, schema, analytical method or storage engine. Decisions trace to baseline evidence.

**Approval gate:** Methodological framework and remaining limitations approved before deriving DRM-MSP.

## Phase 3 — Minimum Shared Protocol

**Objective:** Produce a bounded, immediately testable compatibility profile derived from the methodology.

**Scope:** DRM-MSP 0.1.0, lifecycle/acceptance authority, proposal tracking, examples and minimal checks; not a competing methodology.

**Inputs and dependencies:** Approved methodological consolidation and historical requirements; stable identities and governance conflicts resolved before dependent adoption.

**Main tasks:** Specify seven minimum requirements below; define lifecycle transitions, minimal record/provenance treatment and provisional classifications/relationships; prepare a lightweight Development Register template, examples, manual procedures and basic automated fixtures; document version compatibility and supersession.

**Deliverables:** Approved DRM-MSP 0.1.0, minimal validation fixtures, examples and database-local proposal-tracking convention.

**Completion criteria:** A database can adopt the profile without restructuring its scientific model. Checks are repeatable and failures visible; provisional local meanings are not universal standards.

**Approval gate:** Before any domain pilot, require review of the candidate and
relevant database analysis plus explicit inputs, scope, rights, preservation,
reviewers and success criteria. Each database needs separate authorisation.
This gate was exercised for the two bounded Phase 4 pilots; it does not authorise
new pilots or generally adopt/release the MSP. Phase 4 is now closed.

## Phase 4 — Domain Pilots and Comparative Assessment

**Objective:** Test shared methods against genuinely different research systems.

**Scope:** Small representative AMRKB and OSDS record sets and historical EIRKB↔DPRKB/GISDS↔EII comparisons; no whole-database migration.

**Inputs and dependencies:** Owner-approved MSP/fixtures and explicit closure of the pre-Phase-4 checkpoint after AMRKB/OSDS analysis review; approved pilot inputs, scope, rights, preservation requirements, reviewers and success criteria; separate database authorisations and pinned inputs.

**Main tasks:** Pilot AMRKB agricultural modes/methods/practice and OSDS observation systems/methodologies/sources; evaluate contextual relationships, provenance, resource distinctions, classification extensions and verification; revisit historical cases using recovered requirements and authorised current evidence; compare common versus specialist requirements and record limitations.

**Deliverables:** Two pilot reports, comparative assessment and proposed controlled changes to MSP/full methodology.

**Completion criteria:** Shared requirements are demonstrated without forced incompatible domain structures; identities, evidence and domain acceptance authority survive; pilot findings remain distinct from historical evidence.

**Approval gate:** Domain owners review pilot results; DRM owner approves comparative findings and any specification changes before Phase 5.

## Phase 5 — Standards and Federation Architecture

**Objective:** Translate validated methodology into precise interoperable contracts.

**Scope:** Standards register; information/identifier models; domain profiles; exchange/discovery/resolution contracts; federation registries; mapping and governance.

**Inputs and dependencies:** Reviewed methodology, MSP/pilot findings and rights/authority decisions.

**Main tasks:** Evaluate standards for fitness; define stable IDs/aliases/external references, classification ownership and mappings; define database/schema/classification/identifier/relationship registries; formalise exchange contracts and governance for approval, rights, compatibility and conformance; align Zotero/Zenodo profiles without replacing their authority.

**Deliverables:** DRM v1.0 architecture release candidate with Standards and Conventions Register, profiles, registries and interoperability contracts.

**Completion criteria:** Independent implementers can interpret contracts precisely while retaining source authority. Proposed/adopted/implemented/verified standards remain distinguishable; no premature conformance claim.

**Approval gate:** Architecture/profile/standards decisions approved before the bounded operational implementation.

## Phase 6 — Operational Reference Implementation

**Objective:** Demonstrate that the methodology and contracts can be implemented and reproduced.

**Scope:** Bounded working reference, not full federation migration; support synthetic multi-database and selected real-data tests.

**Inputs and dependencies:** Approved contracts and architecture; rights-cleared pinned fixtures and a bounded implementation plan.

**Main tasks:** Develop a small registry, machine specification, domain-profile schemas/examples, validation command-line tool, candidate intake, identifier/mapping checks, discovery/exchange examples and read-only metadata profiles. Demonstrate conversational, agent-collected and structured-import pathways; preserve review/acceptance controls and source authority.

**Deliverables:** DRM_Methodology.md and DRM_Specification.json with matching version; supporting schemas, registry examples, fixtures, implementation and tests. Future filenames here are outputs, not existing files.

**Completion criteria:** An independent developer can run the reference and reproduce specified validation. Human/machine documents agree; synthetic results and selected source evidence are labelled distinctly.

**Approval gate:** Approve implementation evidence and limitations before integrated validation. The current edition does not establish operational connectors or a full reference implementation.

## Phase 7 — Integrated Validation

**Objective:** Establish methodological defensibility and technical operation with reproducible evidence.

**Scope:** Four validation families, historical/current test reconciliation, research scenarios, external failures and DRM–IRKB authority boundary.

**Inputs and dependencies:** Pinned specification/implementation candidate, historical test evidence and reviewed fixtures; authorised read-only/service tests as needed.

**Main tasks:** Reconcile historical T1–T9, reported prototype tests and current T1–T14; run methodological/technical/research/robustness checks; exercise invalid inputs, duplicates, version conflicts, missing sources and unavailable services. Demonstrate the DRM–IRKB boundary scenario and four broader assessments below.

**Deliverables:** Traceable test reconciliation, validation reports, exceptions/limitations, defect resolutions and a validated release candidate.

**Completion criteria:** All mandatory conformance requirements pass with reproducible evidence. Applicability, exceptions and failures are explicitly assessed, never silently relabelled as successes; research validity remains a separate domain judgement.

**Approval gate:** Owner approves integrated evidence and all release-blocking resolutions before release approval.

## Phase 8 — DRM v1.0 Release

**Objective:** Prepare the approved reproducible DRM 1.0.0 methodology and reference implementation.

**Scope:** Specifications, implementation, validation evidence, known limitations, compatibility and migration guidance.

**Inputs and dependencies:** Validated candidate, matching human/machine version, approved evidence and release checklist.

**Main tasks:** Reconcile methodology/specification/results; package Standards and Conventions Register, registry definitions, profile contract/examples, minimum intake, external profiles, reference implementation, tests/results, limitations, migration guidance and changelog; approve the release and pinned Git revision.

**Deliverables:** Approved versioned DRM 1.0.0 release. DRM 1.0.0-rc.1 denotes the first integrated candidate, not a released standard. Optional Zenodo archive requires separate publication approval.

**Completion criteria:** Specification, implementation and test evidence agree; release is reproducible from a pinned Git revision. No requirement to migrate the entire federation or finish IRKB.

**Approval gate:** Explicit release, tag and publication authorisation. Approval of this roadmap or any earlier phase is not publication permission.

## Minimum profile and controlled intake

Phase 3 derives seven requirements from the consolidated methodology:

1. Stable identifiers.
2. Provenance.
3. Lifecycle and status.
4. Versioning and change history.
5. Classification extensions.
6. Relationship representation.
7. Basic validation.

The proposed database-local `development_register.json` tracks proposals,
affected records/classifications, provenance, rationale, status, reviewer and
decision. It is not a second scientific catalogue or central proposal database.
No register or MSP implementation is created here. Universal taxonomy,
comprehensive ontology, a complete shared JSON schema and automated intake are
outside the interim profile; full tooling is a later bounded demonstration.

Stage E owns the intake methodology, with C/F support: conversational discovery,
agent-assisted source collection and structured external imports enter staging,
normalisation, identity resolution, routing, classification, validation and
review before source-database acceptance. Preserve provenance and change
history. Automated discovery does not establish evidence verification.

## Standards and external-reference scope

Phase 5 evaluates DCMI/Dublin Core, FAIR, SKOS, PROV-O, DCAT 3, DataCite,
JSON Schema, SHACL, relevant ISO/OGC standards, CIDOC CRM, Darwin Core, EML,
RO-Crate and appropriate domain standards. Select parts by justified use case;
record edition, owner, applicability and proposed/adopted/implemented/verified
status. Do not claim present implementation or require one scientific ontology.

The v1.0 reference must demonstrate Zotero bibliographic metadata retrieval and
reconciliation and Zenodo dataset/output metadata registration/resolution,
correct DOI/source/version/provenance treatment and safe unavailable-service
handling. These preserve external authority. Bidirectional Zotero synchronisation
and automatic Zenodo publication are outside mandatory v1.0; metadata registration
is not a licence to deposit outputs, mint DOIs or publish remotely.

## Validation families and research assessments

| Family | Required later assessment |
|---|---|
| V1 — Methodological conformance | Historical T1–T9, A–F gates, domain fidelity, analysis justification and governance. |
| V2 — Technical conformance | Reconciled T1–T14 for identity, provenance, mappings, intake and interoperability. |
| V3 — Research scenarios | Historical EIRKB/DPRKB and GISDS/EII cases plus four broader assessments. |
| V4 — Operational robustness | Invalid inputs, duplicates, version conflicts, missing sources, service failure and reproducibility. |

The reported twelve-test synthetic prototype is a distinct historical claim,
not evidence of either nine-test or fourteen-test completion. Preserve the
original families before reconciling them; no automatic one-to-one mapping.

| Current planned test | Coverage to reconcile in Phase 7 |
|---|---|
| T1 | Schema validation |
| T2 | Identifier integrity |
| T3 | Classification integrity |
| T4 | Relationship validation |
| T5 | Provenance |
| T6 | Domain autonomy |
| T7 | Ingestion |
| T8 | Duplicate resolution |
| T9 | Zotero integration |
| T10 | Zenodo integration |
| T11 | Version compatibility |
| T12 | Machine interoperability |
| T13 | Reproducibility |
| T14 | Governance |

These T1–T14 labels preserve earlier planning coverage, not a completed test suite
or a mapping to identically numbered historical T1–T9 requirements.

| Broader assessment | Research purpose and representative intake scenario |
|---|---|
| A — Interdisciplinary research | Compare concepts/theories/design precedents; review a discovered publication with bibliographic alignment. |
| B — Place-based ecological analysis | Relate geographic/observational evidence to landscape conditions; reference external catalogue/Zenodo metadata. |
| C — Technology and design choice | Trace evidence to appropriate interventions; review a practice/technology candidate and qualified relationships. |
| D — Distributed pedagogical research | Comparative regional learning, portability and reproducibility; review a student-sourced proposal. |

Early AMRKB/OSDS pilots do not replace these four assessments or technical tests.

**DRM–IRKB boundary scenario:** Resolve a systems-science concept, design method,
ecological indicator and agricultural practice without transferring source
authority. IRKB authors a new interpretation with its own identifier, evidence
and assertion-level provenance. It must not silently become a verified source
fact. Demonstrate that an application can access source records without passing
through IRKB. This is planned testing, not current IRKB validation.

## Subsequent programmes and parallel research

**Federation harmonisation:** After DRM v1.0, participating databases receive
independently authorised conformance/migration reviews and updates. Preserve
scientific content, identities, classifications and provenance without
homogenising knowledge models. Full migration is not a release prerequisite.

**IRKB integration and research development:** An independent programme with
its own authority, repository, roadmap and release schedule. Conceptual and
analytical research may proceed in parallel against provisional versioned DRM
contracts; formal integration follows sufficient contract stability. Completed
IRKB development is not required for DRM release. The former “Phase 9/10” labels
are historical numbering only; these are not DRM release phases now.

## Version families and change control

| Artefact | Version/status |
|---|---|
| Historical DRM | v0.1.0–v0.5.0 labels require artefact/narrative qualification, not assumed packages. |
| Minimum Shared Protocol | DRM-MSP 0.1.0, proposed derived profile; no full v1.0 conformance implied. |
| Integrated candidate | DRM 1.0.0-rc.1, following integrated implementation/evidence. |
| Full release | DRM 1.0.0 / DRM v1.0, only after approval. |
| Planning | Dated revisions and decision history, not specification releases. |

Database, record, schema, classification, profile and publication versions
remain separately identifiable. New conflicts or evidence can reopen decisions;
record rationale and compatibility impact. Review planning, baseline,
methodology, MSP, pilots, implementation, validation, release and database
publication at their distinct gates. Never infer scientific validation or
publication authority from a technical pass or a documentation approval.

**Public-edition history — 1 November 2026:** Preserved the approved eight-phase
sequence and phase gates, with documented Phases 1–3 work completed and Phase 4
separately accepted/closed. Private planning history is not redistributed here.
Phases 5–8 remain future work; no new phase, protocol adoption or release is
authorised by this public preparation.
