# DRM Architecture and Remit

**Status:** Approved planning architecture, public preparation edition,
1 November 2026. Not a released DRM standard. Current status and approval limits
are in the [decision summary](DECISIONS.md) and [provenance note](PROVENANCE.md).

## 1. Remit and system architecture

The Database Reference Methodology (DRM) is **a methodological and technical
framework for the design, development, evaluation, governance and
interoperability of heterogeneous research databases**.

DRM is a methodology first, not merely federation management software. It
specifies how research remit, knowledge representation, engineering, analysis,
lifecycle, evidence, rights, versioning and connections are justified and
reviewed. A bounded working reference implementation will demonstrate that
these methods and contracts can be applied; it will not prescribe one engine.

| Responsibility | Authority |
|---|---|
| DRM methodology and governance | Database design/evaluation methods, domain profiles, lifecycle, standards selection, conformance and interoperability contracts. |
| Federation infrastructure | Implemented discovery, registries, identifier resolution, exchange, mapping services and provenance mechanisms under those contracts. |
| Autonomous databases | Canonical records, scientific classifications, evidence, research interpretations, domain-specific review and acceptance. |
| IRKB | Independent interdisciplinary comparison, assertions, original classifications, synthesis and research outputs. |
| Applications | Use appropriate source and federation interfaces; may access databases directly without passing through IRKB. |

This is a responsibility model, not a mandatory processing pipeline. IRKB does
not own the federation infrastructure or universal discovery catalogue. Shared
indexes, caches and derived views must disclose their authoritative origins.
No central copy of all source records or research relationships is required.

## 2. Architectural boundaries

| Boundary | DRM/shared remit | Authority retained elsewhere |
|---|---|---|
| Methodology versus research | Define how database design and evaluation are accountable. | Databases and IRKB author and assess research conclusions. |
| Governance versus implementation | Define contracts and conformance requirements. | Federation services implement them; software does not itself establish scientific authority. |
| Shared conventions versus domain meaning | Govern identity, classification exchange and mapping mechanisms. | Domains define scientific concepts, evidence hierarchies and classifications. |
| Structural mappings versus research assertions | Register approved structural/semantic exchange mappings. | Source databases and IRKB own evidence-backed research relationships. |
| Discovery versus synthesis | Specify common catalogue/discovery conventions. | IRKB maintains research-specific indexes and produces interpretation/synthesis. |

**Domain autonomy does not require domain exclusivity.** Different databases
may represent the same subject differently, with legitimate overlap. Technical
conformance does not establish scientific validity or truth: a structurally
valid, traceable claim may remain uncertain, contested or provisional.

Preserve these design distinctions without imposing a universal table model:

- **Resource, record and assertion:** source object, its description and a claim.
- **Definition, instance and observation:** a defined concept, particular case
  and observation/measurement with its context.
- **Identity, similarity and functional relationships:** same entity, related
  meaning and use together are different claims.
- **Canonical, staged and derived information:** authoritative content, pending
  candidates and reproducible outputs have different authority and lifecycles.
- **Verified evidence, historical documentation, proposals and synthetic examples:**
  each retains its evidence status; synthetic success is not scientific verification.

Keep provenance, evidence, rights, allowed reuse, uncertainty and versions
traceable. Preserve GISDS resource/platform-or-service/dataset-or-product/data-layer
distinctions as candidates for domain profiles, not a compulsory strict hierarchy.

## 3. Six-stage database methodology

Stages A–F apply iteratively to **each database's design and development**.
They are not the eight phases for developing DRM v1.0. New evidence can reopen
an earlier decision; each gate records evidence, rationale, owner, status and
unresolved issues. The methodological framework distinguishes specifically approved decisions from
detailed proposals that remain under review.

| Stage | Remit | Expected evidence and decisions | Completion criterion |
|---|---|---|---|
| A — Domain and Requirements | Define remit, boundaries, audiences, questions and intended uses. | Scope/exclusions, competency questions, representative cases; justify domain boundary and overlap. | Responsible reviewers approve remit and use cases with unresolved limits recorded. |
| B — Knowledge and Ontology | Represent domain entities, concepts, relationships and competing interpretations. | Conceptual model, glossary, contextual examples, units and relationships; choose justified distinctions. | Domain cases, exceptions and contested interpretations can be represented without loss. |
| C — Database Engineering | Select logical/physical structures, storage, schemas and integrity mechanisms. | Architecture alternatives, workload/maintenance rationale, keys/constraints and test plans. | Engineering decisions are justified and integrity/performance checks are defined. |
| D — Analytical Methods | Justify classifications, calculations and interpretations. | Method definitions, assumptions, analytical rationale, limitations and reproducibility needs. | Analyses answer scoped questions with independent justification and declared uncertainty. |
| E — Information Lifecycle | Govern discovery, candidate intake, verification, revision and publication. | Source/provenance records, staging, deduplication, review, correction and deprecation procedures. | A traceable intake/review/correction example demonstrates who can accept or reject material. |
| F — Interoperability and Governance | Govern identifiers, mappings, exchange, rights, compatibility and change. | Versioned profile, authority/rights decisions, export/import/mapping contracts and tests. | Reviewers approve exchange and governance evidence with preservation/round-trip checks. |

### Historical domain-profile candidate

The ten-part contract in the historical v0.1.0 core (development evidence summarised in the public provenance note)
is represented below as historical lineage; the current methodological document
evaluates all ten topics with proportionate accountability:

1. Identifier/remit, exclusions, audiences and uses.
2. Research questions and representative competency queries.
3. Knowledge types, evidence hierarchy, uncertainty and contested interpretations.
4. Entity/relationship model, cardinalities, data types and constraints.
5. Vocabularies/classifications only where justified.
6. Logical/physical rationale and alternatives.
7. Source, intake, deduplication, review and correction policy.
8. Identifier, citation, licensing, sensitivity and provenance conventions.
9. Versioned exports, imports and mapping specifications.
10. Tests, limitations, governance and release history.

This does not automatically adopt every historical draft requirement as a
current normative contract. No specific file layout,
engine, scientific ontology or analytical method is universally mandatory.

## 4. Requirement levels and conformance

| Class | Planning treatment |
|---|---|
| Mandatory | Core interoperability minimum and accountable methodological decisions: stable IDs, provenance, lifecycle, versions, typed relationships, validation, documented remit/design/analysis/governance. |
| Recommended | Implementation patterns such as JSON Schema, registry layouts and shared tooling when justified by the use case. |
| Optional | Specialist ontologies, storage approaches, analytical modules, graph representations, HA/IL/IM and domain-specific standards/extensions. |

Mandatory accountability requires evidence of appropriate decisions, not one
prescribed scientific method. Standards and technologies require a fitness
rationale, including omissions and alternatives.

- **Methodological conformance:** Evidence of A–F decisions, domain fidelity,
  justified analysis and governance under a specified version/profile.
- **Technical conformance:** An implementation satisfies applicable machine,
  integrity, compatibility, exchange and operational checks.
- **Scientific and interpretive validity:** Domain assessment of evidence,
  claims, uncertainty and conclusions; neither conformance category proves it.

No conformance certification is issued by planning approval. Not-applicable
checks require justification; skipped or failed tests cannot be counted as passes.

## 5. Historical methodology consolidation

A bounded historical baseline and requirement review have been completed.
The recovered core v0.1.0 is a proposed historical draft; later profile,
interoperability, prototype and preliminary audit packages remain missing or
incompletely evidenced. Conversational working revisions are not automatically
versioned releases. A reported twelve-test prototype has not been reproduced.
Historical nine-test and current fourteen-test families retain distinct meanings.
See [provenance](PROVENANCE.md) for source/reproduction limitations.

## 6. Minimum Shared Protocol strategy

**DRM-MSP 0.1.0** is a candidate bounded operational compatibility profile derived
from the consolidated methodology. It is supersedable, not a competing standard
or a shortcut around historical consolidation. It belongs to Phase 3, following
methodological consolidation. Its preparation is complete but general adoption
and release have not occurred.

| Requirement | Candidate minimum operational treatment |
|---|---|
| Stable identifiers | Non-reused identities independent of mutable classifications. |
| Provenance | Origin, source locator, contributor/process and evidence status. |
| Lifecycle and status | Proposed, reviewed, accepted, superseded and rejected material distinguished. |
| Versioning and change history | Meaningful changes and separate record, schema and protocol versions. |
| Classification extensions | Provisional local extensions without silent federation-wide adoption. |
| Relationship representation | Source, target, type, evidence and approval state preserved. |
| Basic validation | Repeatable checks, failures and limitations documented. |

Plan a lightweight **development_register.json** per database for proposed
records, classification extensions, methodological changes, relationships and
schema modifications. Candidate metadata should identify proposal, database,
affected material, provenance, rationale, state, reviewer and decision. It must
not duplicate the authoritative scientific catalogue or centralise all proposals.
An empty synthetic template and bounded candidate checker are available; no
operational source register or production ingestion is established.

Explicitly defer universal domain taxonomy, comprehensive ontology, a complete
shared JSON schema and an automated ingestion engine from the minimum profile.
The later full implementation can support reusable tooling without mandating
identical scientific models. MSP compliance is not full DRM v1.0 conformance.

## 7. Ingestion methodology

Ingestion belongs primarily to Stage E, supported by engineering in C and
contracts/governance in F. Support conversational research discovery,
agent-assisted source collection and external database imports through:

**Capture → Candidate staging → Normalisation → Identity resolution → Domain
routing → Classification → Validation → Review → Source-database acceptance**.

Separate discovery, extraction, verification and interpretation. Record
provenance and change history; repeat intake must not silently create duplicates.
DRM defines the protocol, reusable software executes it, and the source database
alone decides acceptance into its authoritative corpus under its review rules.

The minimum profile supports manual controlled intake and proposal tracking.
Full DRM v1.0 demonstrates a reusable testable interface, adapters, duplicate
resolution, review and approval controls; a bounded command-line implementation
is sufficient. Sophisticated autonomous agents are not a release prerequisite.

## 8. Zotero and Zenodo integration

Zotero retains bibliographic authority: library/item identities, citations,
reference management and metadata. DRM defines controlled linking, exchange,
validation and reconciliation, preserving domain interpretations.

Zenodo retains dataset/software/research-output preservation, DOI identification,
publication metadata and versioned research releases. DRM records external
identity, version and provenance rather than reproducing the archive.

The v1.0 reference implementation must demonstrate bibliographic metadata
retrieval/reconciliation for a Zotero item, metadata registration/resolution
for a Zenodo-hosted dataset or output, correct DOI/source/version handling and
safe service-unavailability behaviour. Registration here means recording and
resolving external metadata, not automatically creating a remote deposit or DOI.
Bidirectional Zotero synchronisation and automatic Zenodo publication remain
outside mandatory v1.0 scope. No connectors or service calls are implemented in this edition.

## 9. DRM development roadmap

The [eight-phase roadmap](DRM_v1_Roadmap.md) is the sole current development
sequence: historical baseline, methodological consolidation, minimum profile,
pilots, standards/architecture, reference implementation, integrated validation,
release. It explicitly supersedes the preliminary-stage-plus-ten-phase plan.
Each phase has dependencies, deliverables, completion criteria and an approval
gate. Planning approval neither executes nor marks any phase complete.

## 10. Post-release programmes and independent IRKB development

**Federation harmonisation:** After DRM v1.0, apply the validated methodology
through independently authorised database reviews and updates, preserving
scientific content, identifiers, classifications, provenance and autonomy.

**IRKB integration and research development:** IRKB retains its own repository,
research authority, roadmap and release schedule. Conceptual research can
proceed in parallel using provisional versioned interoperability contracts;
formal integration is tested when contracts stabilise. IRKB is not obliged to
wait for DRM release to formulate its research model. Completed federation
migration and completed IRKB development are not prerequisites for DRM v1.0.
No IRKB research implementation is established by this edition.

## 11. Risks and safeguards

| Risk | Safeguard |
|---|---|
| Universal scientific ontology imposed | Autonomous profiles, justified shared concepts and explicit mappings. |
| DRM reduced to management software | A–F methodology and research-design evaluation remain central. |
| IRKB duplicates common discovery | Shared services plus optional research-specific indexes; independent synthesis. |
| Mappings become scientific claims | Typed distinction between structural mappings and evidence-backed assertions. |
| Historical reports become implementation claims | Source locators, evidence states and independent reproduction before verification claims. |
| MSP becomes a competing standard | Derived, bounded profile with versioned compatibility/supersession rules. |
| Full migration delays release | Bounded reference implementation and representative selected-record tests. |
| Automated intake introduces unreliable evidence | Candidate staging, extraction/interpretation separation and domain acceptance. |
| External integrations duplicate service authority | Identifier-based exchange; no replacement bibliographic/archive service. |
| Excessive methodological bureaucracy | Small profiles, proportional evidence, reusable checks and justified exceptions. |

DRM defines how record approval is accountable; it does not approve every
research record or interdisciplinary interpretation itself.

## 12. Repository organisation

This public edition separates readable guidance, synthetic examples, a template,
checkers and tests. Original research evidence is retained in a private archive,
not redistributed or required at runtime. No empty standards/registry/connector
structures are issued as implemented capabilities.

## 13. Active documents and evidence boundary

- [README](README.md): purpose, current status, navigation and commands.
- [Methodological architecture](DRM_Methodological_Architecture.md): principles,
  A–F, profile accountability, scientific/technical distinctions and review limits.
- [Roadmap](DRM_v1_Roadmap.md): sole eight-phase development sequence.
- [Decisions](DECISIONS.md): approved principles, open questions and pilot closure.
- [Candidate MSP](DRM_Minimum_Shared_Protocol.md): bounded seven-subject profile.
- [Provenance](PROVENANCE.md): public derivation and evidence limitations.

## 14. Final architectural assessment

Retain separate methodology, infrastructure and research responsibilities.
Restore A–F as the database-design foundation. Derive MSP from recovered and
consolidated requirements, then test small autonomous domain pilots. Combine
standards, contracts, controlled intake and external metadata exchange in a
bounded implementation. Validate methodological, technical, research and
operational evidence before release. The framework standardises how knowledge
systems are developed, evaluated and connected; it does not standardise away
their disciplinary differences or own the knowledge they produce.

**Current limit:** no released DRM standard, general MSP adoption, reproduced
historical prototype, operational federation or completed integrated validation.
Phase 4 is closed within its bounded documentary scope; Phase 5 is not authorised.
