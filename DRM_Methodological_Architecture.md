# DRM Methodological Architecture

**Status:** Specified methodological basis approved for Phase 3 preparation;
unapproved details remain proposals. Public preparation edition, 1 November 2026.
Not a released DRM or adopted MSP specification and not a conformance award.

The framework below preserves the twelve principles, six iterative A–F stages,
ten-topic profile contract and conceptual safeguards of the current methodology.
Clause IDs P2-C01–P2-C15 are public review locators, not scientific record IDs.
These are methods for individual databases; the eight-phase [roadmap](DRM_v1_Roadmap.md)
is the DRM development sequence. Evidence depth is proportionate, not boilerplate.

The [decision summary](DECISIONS.md) records five specifically approved areas:
obligation/applicability and exceptions, role-separated authority, compatibility
by effect, ten-topic accountability and selective boundary assessment, with
historical evidence limits retained. Those approvals do not make every detailed
proposal normative. Candidate-specific rules remain unadopted outside approved
scope; no conformance certification follows from documentation approval.

Phases 1–3 completed their documented development work and Phase 4's two bounded
documentary pilots were separately accepted and closed. **Phase 5 is not authorised.**
The private per-requirement audit and approval chronology are not included; see
[provenance](PROVENANCE.md) for derivation and reproducibility limits.

## P2-C01 — Twelve consolidated principles

Methodological proposal, subject to the approved basis and qualifications above. Each principle retains its separate historical P01–P12 lineage.
Its binding force comes from explicit applicable clauses, not automatic adoption
of every draft imperative. Optional modules must still preserve core authority,
identity, rights and truthful provenance when used.

| Principle | Proposed consolidation | Evidence expected |
|---|---|---|
| P01 — Domain primacy | Subject, users and competency questions drive the representation. | Scope, representative cases, counterexamples and justified design. |
| P02 — Separation of concerns | Distinguish epistemic, conceptual, logical, physical and analytical choices. | Short rationale separating meanings from storage and analytical outputs. |
| P03 — Independent authority | Each source owns its canonical records, classifications, governance and releases. | Authority/acceptance owners and origin-labelled references/caches. |
| P04 — Evidence and interpretation | Keep observed/source facts, extracted claims, inferences and synthesis distinguishable. | Attribution, evidence status, uncertainty and correction history. |
| P05 — Stable identity | Do not reuse issued identities or derive them solely from mutable class/row position. | Namespace/identity policy, alias handling and planned preservation cases. |
| P06 — Integrity and quality | Assess structural integrity, domain fidelity, evidence quality and interpretation separately. | Applicable constraints, review criteria, failures and limitations. |
| P07 — Proportionate complexity | Choose the least complex design meeting documented requirements. | Trade-offs against expressiveness, integrity, extensibility and maintenance. |
| P08 — Interoperability by mapping | Connect models through typed, versioned, justified contracts/relationships without transferring scientific authority. | Mapping category, authority, semantics, evidence and review state. |
| P09 — Evolvability | Track changes to records, schemas, vocabularies, profiles, methods and releases independently. | Compatibility assessment, change history and migration/deprecation rationale. |
| P10 — Reuse with rights | Preserve permissions, sensitivity, restrictions and permitted reuse; FAIR does not imply openness. | Rights provenance, unresolved access questions and source restrictions. |
| P11 — Reproducibility | Make derived claims/outputs traceable to inputs and procedures appropriate to their type. | Input versions, method/parameters, review or reconstruction evidence and limits. |
| P12 — Modularity | Analytical frameworks and specialist technologies are selectable by justified domain need. | Why a module applies; no mandatory HA/IL/IM or universal scientific ontology. |

## P2-C02 — Six iterative stages and evidence gates

Methodological proposal, subject to the approved basis and qualifications above. **Mandatory methodological accountability:** record decisions,
not one mandated file per stage. A small project may use concise combined notes;
a complex/sensitive project needs deeper evidence. Review scope and residual
issues at each gate; completion does not claim that later operational checks
have run. Reopen the relevant gate when new data, interpretation, rights or
engineering evidence changes its assumptions.

| Stage | Remit and decisions | Proportionate evidence | Proposed gate |
|---|---|---|---|
| A — Domain and Requirements | Remit, exclusions, audiences, questions, intended uses and overlap. | Short scope and representative/edge/contested cases; boundary assessment selection. | Accountable owner/reviewer accepts remit and use cases with unresolved limits disclosed. |
| B — Knowledge and Ontology | Entity/relationship meanings, knowledge types, terminology and alternative interpretations. | Conceptual examples and distinction decisions; glossary/model as needed. | Domain reviewers can express selected cases without material semantic loss; disagreement is representable. |
| C — Database Engineering | Logical/physical model, integrity, workload, access and maintenance alternatives. | Rationale for model/storage/constraints, applicability of spatial/measurement/graph checks, test plan. | Decisions are justified and appropriate integrity/performance checks specified; implemented status requires later execution evidence. |
| D — Analytical Methods | Classification, calculation, comparison, inference and synthesis choices. | Question-to-method rationale, assumptions, uncertainty, limitations and reproduction/review approach. | Chosen analysis is justified for its question; technical success is not scientific endorsement. |
| E — Information Lifecycle | Discovery/acquisition, staging, identity resolution, classification, validation, review, correction and deprecation. | Traceable illustrative intake/correction and named acceptance roles; actual versus synthetic examples labelled. | Lifecycle decisions and acceptance authority are reviewable; an illustrative design does not establish operational ingestion. |
| F — Interoperability and Governance | Identity/exchange/mapping, authority, rights, compatibility and releases. | Versioned intended contract, governance decisions and planned preservation/round-trip cases. | Scope and authority accepted; technical exchange claims await actual evidence, not a design-only gate. |

A gate record should identify decision, rationale, evidence/locators, applicable
version/scope, reviewer role, unresolved issues, date and review/reopen trigger.
No universal committee or prescribed document format is required. The owner
must not self-certify unknown domain facts by relabelling a technical check.

## P2-C03 — Evaluation of the ten-part domain-profile contract

Methodological proposal, subject to the approved basis and qualifications above. Preserve **all ten topics as methodological accountability**;
require proportionate answers, not identical tables, storage, document sets or
immediate implementation. “Planned”, “not applicable with rationale”, “unknown”
and “implemented with evidence” are distinct answers. Missing evidence is not a
successful completion. A non-implemented database can document a design/profile
but cannot claim technical conformance from planned exports or tests.

| Historical clause | Proposed treatment/applicability | Minimum proportionate evidence and review |
|---|---|---|
| DP01 — Identifier/remit, exclusions, audiences and uses | Mandatory scope accountability for every profile. | Named resource/profile identity, remit and exclusions; no compulsory new federation ID format here. |
| DP02 — Research questions and competency queries | Mandatory questions/use cases; executable query language is conditional. | Plain-language competency questions and cases may suffice; document limits rather than invent query implementations. |
| DP03 — Knowledge/evidence hierarchy, uncertainty and contested interpretation | Mandatory evidence model; a single universal hierarchy is excluded. | Explain accepted evidence traditions, uncertainty/disagreement and review authority; plural evidence is allowed. |
| DP04 — Entities, relationships, cardinalities, types and constraints | Mandatory representational rationale; exact engineering artefacts conditional on chosen model. | Domain examples and constraints; do not force relational tables, one ontology or cardinalities irrelevant to the model. |
| DP05 — Justified vocabularies/classifications | Mandatory decision whether needed; actual controlled schemes optional/domain-dependent. | Rationale for selection or non-use; ownership/version/meaning if used. |
| DP06 — Logical/physical rationale and alternatives | Mandatory justification; depth scales to workload and risk. | Explain portability, access, collaboration, maintainability and rejected alternatives; no mandated engine. |
| DP07 — Sources/intake/dedup/review/correction | Mandatory lifecycle/accountability; automated pipeline optional at profile level. | Source routes, candidate versus canonical treatment, duplicate policy and acceptance/correction roles. |
| DP08 — IDs, citation, licensing, sensitivity and provenance | Mandatory rights/identity/provenance accountability. | Source locators and permissions or unresolved-rights flag; no invented licence, DOI or permission. |
| DP09 — Versioned export/import/mapping specifications | Mandatory intended exchange/compatibility decision for federation participation; live services not required for methodological design. | Describe at least one suitable portable exchange and preservation intent. Actual export/round-trip claims require technical evidence. A deliberately standalone design states participation limits. |
| DP10 — Tests, limits, governance and release history | Mandatory evidence/status reporting; no fabricated history for new designs. | Separate proposed tests, executed results, unresolved failures, owners and actual releases or explicit absence. |

Uniform file names, schemas and ten separate artefacts are excluded. A diagram,
small table or narrative may discharge several topics if each is traceable.
The historical ten-clause contract remains a source; this table is its proposed
current interpretation, not approval of its full original MUST wording.

## P2-C04 — Obligation levels, applicability and justified exceptions

Methodological proposal, subject to the approved basis and qualifications above. Use only three obligation classes, with explicit applicability:

- **Mandatory:** Core identity/authority/provenance/rights/status truthfulness
  and accountable A–F/profile decisions. An applicable mandatory requirement
  cannot be silently waived by a local implementation preference.
- **Recommended:** Default implementation or evidence patterns with an explained
  alternative where appropriate, such as migration automation or particular
  registry/validation structures.
- **Optional:** Justified analytical modules, specialist ontology, graph/spatial
  extensions and technologies. Once adopted, their applicable authority, rights,
  identity and provenance safeguards still apply.

Conditional applicability is not a fourth class. Spatial CRS evidence is needed
when spatial meaning is represented; absence of spatial data justifies N/A for
that technical aspect, not N/A for methodological accountability. A profile's
evidence depth should reflect intended use, consequence of error, sensitivity,
complexity and maturity. A concise rationale is preferable to empty boilerplate.

An applicability/exception record should identify the clause and version,
profile/use scope, reason, supporting evidence, affected cases, risk/semantic
loss, alternative control, accountable reviewer and revisit trigger. Distinguish:

1. **Not applicable:** Demonstrated absence of the triggering circumstance; record
   rationale. Do not use it for missing evidence or failed implementation.
2. **Alternative satisfaction:** Different representation/tool provides the same
   intended protection; explain and review the evidence, not the brand of tool.
3. **Derogation:** An applicable mandatory obligation is unmet; disclose partial
   status and obtain explicit authorised review. A derogation is not a full pass.
4. **Unknown or failed:** Preserve that state and restrict dependent claims/work.

No exception authorises erased provenance, reassigned identity, misrepresented
scientific authority, bypassed rights or a reported test counted as reproduced.
If material protection is missing, restrict use/conformance claims rather than
pretend an exception makes the missing protection present. DRM-owner review of methodological exceptions is approved. Scientific acceptance
and rights authority remain with domain authorities; detailed claim vocabulary
and review intervals remain review points for the candidate profile (obligation/exception review).

## P2-C05 — Conformance, validity and evidence expectations

Methodological proposal, subject to the approved basis and qualifications above. Separate:

| Judgement | What can be claimed with evidence | What cannot follow automatically |
|---|---|---|
| Methodological conformance | Applicable A–F/profile decisions have justified scope, cases, authority and review under a specified methodology/profile revision. | Implemented constraints, successful runtime, tested exchange or scientifically true claims. |
| Technical conformance | Particular implementation/version satisfies specified applicable checks against disclosed inputs and environment. | Full methodology accountability or domain/scientific validation merely from valid JSON or successful code. |
| Scientific/interpretive validity | Responsible domain assessment of methods, evidence, uncertainty, applicability and claims. | Universal certainty or transfer of scientific approval to DRM infrastructure. |

A design-only record should be described as **methodological evidence reviewed**
within an explicit scope, not “DRM implemented”. Any future conformance claim
must state specification/profile/schema versions as applicable, evidence class,
reviewer, applicable/excluded obligations and limits. This draft confers none.

Historical T1–T9 provide documentary evidence expectations: domain cases,
invalid-type/link handling plans, assertion traceability, identity through change,
derived-output reproducibility, preservation of exchange semantics, typed mappings,
evolution rationale and exercised governance when operational claims are made.
Document actual/reported/planned/synthetic/not-applicable status. Suitable design
examples can explain intent, but they cannot substitute for an implementation
run or domain verification. No particular universal test runner is prescribed.

Full execution and methodological/technical/scientific coverage reconciliation
remain Phase 7 work. Historical T1–T9, the reported twelve-test prototype, planned
T1–T14, historical scenarios, four research assessments and the DRM–IRKB boundary
scenario remain distinct. Partial topical overlap is not ordinal equivalence.
Neither the twelve reported passes nor the six example behaviours are reproduced
results; missing originals remain missing. See P2-C15 and the public provenance summary.

## P2-C06 — Authority and relationship categories

Methodological proposal, subject to the approved basis and qualifications above. Classify by the **claim being made and authority exercised**,
not merely by a storage table or RDF predicate. Record source/target, scope,
relationship kind, asserted meaning, provenance, author/process, version,
review/approval state and uncertainty/conflict as applicable. Evidence and
review status are not interchangeable with a confidence score.

| Category | Proposed authority and approval boundary | Required distinction/evidence |
|---|---|---|
| Structural mapping | Contract/registry steward can approve declared field, identifier-format or exchange correspondence under source-endorsed interfaces. | Approval of transport/structure does not establish concept identity, scientific equivalence or correctness of every mapped value. |
| Semantic alignment | An author proposes exact/close/broader/narrower/related meaning in an explicit domain/use context. Domain reviewers assess the interpretation; federation governance approves its use in an exchange contract only within declared scope. | Record definitions, context, version, rationale and evidence; contested alignments remain contested. A semantic predicate alone is not scientific verification or cross-database identity. |
| Source assertion | Source database/curator authors and reviews a claim using its own domain evidence and governance. | Shared indexes preserve authority of origin; DRM does not approve each research record or silently rewrite it. |
| IRKB research interpretation | IRKB authors its own comparison, inference, synthesis or causal/influence hypothesis and owns that research output. | Own assertion identity, sources, method, qualifications and review; not silently promoted to a verified source fact or an approved structural identity mapping. |

A relationship can reference another category without collapsing it. A registry
may record approved alignment metadata, but cannot centralise or take ownership
of all research assertions. A source can reject use of a mapping; differences
must remain visible rather than forced into consensus. The approved role separation above applies; detailed escalation/dispute
procedures remain candidate review questions (relationship-authority review), not a new central
scientific approval service.

Supersede the early common-entity proposal **only insofar as it requires a
compulsory universal scientific model**. Preserve optional shared categories,
subtypes, examples, domain extensions, discovery metadata and approved structural
registry functions. A shared category is usable when justified; category reuse
is not automatic equivalence and does not constrain a source's canonical model.
No rewriting or deletion of the earlier source proposal is authorised.

## P2-C07 — Assess conceptual distinctions without identical structures

Methodological proposal, subject to the approved basis and qualifications above. Each profile should decide whether/how the distinction affects
its cases, explain representation and note semantic loss if collapsed. Separate
records/tables are not universally required; annotations, views or another
representation can suffice when meanings and authority remain recoverable.

| Distinction | Assessment question/evidence | Guardrail |
|---|---|---|
| Resource / record / assertion | Which source object, local description and attributed claim are present? Show a case with source locator and claim owner. | Describing a resource is not owning its content or certifying each claim. |
| Definition / instance / observation | Does a definition, particular event/entity or measured value occur? Show relevant method, unit, place/time and uncertainty where meaningful. | An indicator definition is not an observation or inferred ecological condition. |
| Identity / similarity / function | Is the relation same-object identity, meaning resemblance or use together? Supply context and identity evidence where claimed. | Similar names, external IDs or use together are not proof of equivalence. |
| Canonical / staged / derived | Who owns the authoritative record; what is pending intake; what was generated? Show origin/status and reproducible inputs where relevant. | A cache, import, example or generated interpretation cannot silently become a source fact. |
| Classification / intrinsic property | Can assignments change independently of the thing described? | Classification changes cannot silently change issued identity. |
| Evidence / interpretation | What is extracted, observed, inferred, contested or synthesised? | Preserve attribution and uncertainty instead of a single unqualified truth flag. |

GISDS provider/platform/service/dataset/product/layer distinctions are domain
cases to evaluate, not a fixed global hierarchy. Practices and artefacts can be
legitimate evidence; they need not fit a publication-only ontology. A profile can
record that a distinction is irrelevant with evidence, not simply omit review.

## P2-C08 — Provenance, lifecycle and controlled acceptance

Methodological proposal, subject to the approved basis and qualifications above. Preserve source locator, edition, contributor/process,
evidence/claim type, status, meaningful changes and review authority at a level
appropriate to the record or assertion. Derived outputs also identify input
versions, method/software/parameters and limitations where needed to assess or
reproduce them. Historical documentation, synthetic examples, extracted facts,
interpretations and independently verified results must stay distinguishable.

Methodologically describe discovery/acquisition, staging, normalisation,
identity/duplicate resolution, routing/classification, validation, review,
acceptance, correction and deprecation. Domain profiles may combine or elaborate
steps while retaining the protections and decision evidence. State who can
accept/reject/correct authoritative content. No literal global state enumeration,
JSON fields or operational register is imposed by this draft; those are Phase 3
profile decisions. Separate validation from scientific acceptance.

Conversation/agent/import pathways must preserve what was supplied, what was
extracted and what was inferred. Machine-generated material is not verified by
default. Repeated intake should have an explicit duplicate policy respecting
independent cross-database interpretations. Manual controlled review is possible;
a sophisticated autonomous ingestion engine is not methodologically required.

## P2-C09 — Stable identity and origin-preserving reference

Methodological proposal, subject to the approved basis and qualifications above. Document namespace/scope, stability/non-reuse, aliases/external
references and identity-resolution evidence without selecting a universal ID
syntax here. Use portable locators suitable to intended exchange. Classification
or row ordering must not be the sole enduring identity mechanism. If a legacy
identifier encodes classification, assess actual continuity and aliases rather
than automatically reissuing it or migrating a domain in this task.

An external identifier is evidence to reconcile, not proof every referenced
concept/edition is identical. Missing or conflicting targets must fail visibly
or remain unresolved; never silently reassign the reference. Caches/indices
retain source identity/version and authority. Current local audit IDs are not
federation entity IDs, and no new scientific IDs are issued here.

## P2-C10 — Domain-appropriate engineering and analytical justification

Methodological engineering/analysis proposal, subject to the approved basis. Require an explained
choice of logical/physical model, integrity constraints, access/performance
needs, portability, collaboration and maintenance costs. Relational keys and
normal forms, graph identity/traversal, spatial CRS/geometry/time, measurement
quantities/units/uncertainty are conditional design evidence, not universal
requirements for unrelated domains. Document justified denormalisation or
alternative integrity methods. No engine, programming language or schema format
is prescribed. Planned versus executed performance/integrity checks remain clear.

Every selected analysis/classification should identify the question, method,
assumptions, evidence, context, uncertainty, limitations and review or
reproduction approach. A causal or historical-influence assertion needs more
than similarity or a technical graph edge. Practices, observations and scholarly
interpretations may have different evidence traditions. Preserve competing
interpretations instead of treating a structural pass as analytical justification.

## P2-C11 — Versions and compatibility assessed by effect

Methodological proposal, subject to the approved basis and qualifications above. Keep methodology/specification, MSP, profile, schema,
classification, record, method and publication revisions distinguishable.
Compatibility is assessed against declared users, contracts and claims, not
inferred from a version label or from parsing alone.

| Proposed change | Proposed compatibility treatment |
|---|---|
| New mandatory obligation applying to existing conforming adopters | Presume a conformance-impacting change; assess evidence/cost/semantic impact. Do not call it backward compatible merely because labelled MINOR. |
| Editorial clarification preserving obligations and interpretation | Candidate PATCH only after checking that it introduces no new effective obligation. |
| New optional capability/profile that leaves existing contracts and conformance unchanged | Candidate compatible MINOR; record scope and demonstrate compatibility before claiming it. |
| Changed meaning, required export or mapping that breaks a declared contract | Treat as breaking for that affected scope; migration/deprecation and old-version support decisions required. |
| New requirement limited to a new opt-in profile | May preserve existing-profile compatibility, but state exactly which profile/adopters are affected; no blanket claim. |

For each change record affected versions, obligations, evidence, declared
contracts, compatibility finding, review and migration/deprecation plan. Prefer
reversible/automated migration where feasible, but mandate honest reporting of
breakage rather than one migration technology. Preserve aliases and issued
identities. Historical original versions remain identifiable.

Default proposal: a newly applicable mandatory obligation that invalidates
previous conformance requires a breaking-version path or explicit opt-in profile,
not an unqualified compatible MINOR. This compatibility-by-effect principle is approved. Precise transition details,
exceptions and support-period policy remain candidate review questions (compatibility review). This draft
does not publish a SemVer standard or assign a DRM release version.

## P2-C12 — Classification reuse, alignment, synthesis and analytical modules

Methodological proposal, subject to the approved basis and qualifications above. Classifications are versioned, attributable, contextual research
resources. **Reuse** applies an existing scheme while preserving its definition,
source, version and intended context. **Alignment** asserts a scoped relation
between independently governed schemes; exact, close, broader/narrower and
related are not the same as record identity. **Synthesis** creates an authored
scheme or analytical interpretation with its own identity, evidence and method.
Record adaptations/extensions rather than silently overwriting the source.

HA/IL/IM may be curated classifications, generated views or research arguments;
represent their roles explicitly where relevant. They are optional modules,
not federation-wide scientific categories. Richness of classifications is not
quality: assess redundant/conflicting meanings and maintain interpretable
scope/version/provenance. Domain owners decide assignments and acceptance.

## P2-C13 — Rights, restricted evidence and provenance

Methodological proposal, subject to the approved basis and qualifications above. Record source permissions, attribution, sensitivity, community
or custodian constraints, restrictions and permitted reuse, or explicitly unknown
status. FAIR does not imply public access. No licence, DOI or permission is
invented. Limit reuse/disclosure and dependent claims when rights are unresolved;
record a durable permitted reference instead of reproducing protected evidence.

Evidence may be reviewable under controlled access without being publicly
redistributed. The profile should explain how reviewers can assess it and what
cannot be independently checked. Do not label restricted/unavailable material
verified solely from its citation. Appropriate community/domain authority cannot
be replaced by a central technical validator. This draft settles no database's
scope, custodianship or legally effective permission.

## P2-C14 — Proportionate boundary assessment

Methodological proposal, subject to the approved basis and qualifications above. No universal score, weighted sum, threshold or automatic
new-database decision is proposed. Begin with remit/use, accountable authority,
meaningful overlap and maintenance responsibility; select deeper criteria by
research question and consequences. Document which criteria matter and why,
using a short note for simple cases. This makes accountable **selection and
reasoning** mandatory, not twenty equally extensive forms or numeric scores.

| Criterion | When/depth to consider | Appropriate evidence/question |
|---|---|---|
| Purpose | Starting scope review. | Distinct question or unmet use; no exclusive subject ownership implied. |
| Epistemology | Different evidence traditions or claims. | What counts as knowledge and how contested interpretations are retained. |
| Ontology | Different representations could lose meaning. | Examples of distinct entities/relations, not a forced global type list. |
| Classification | Scheme reuse, overlap or extension. | Definitions, ownership, versions and assignment needs. |
| Methodology | Different investigative or analytical approaches. | Justification and limits of relevant methods. |
| Corpus | Shared/distinct source material affects stewardship. | Source coverage, identity and reasons for separate interpretation. |
| Interpretation | Same source supports different claims. | Attributed positions, disagreement and source versus derived assertions. |
| Analytical structures | HA/IL/IM or other frameworks used. | Classifier/view/argument distinction and optional applicability. |
| Provenance | Evidence is imported, transformed or contested. | Source/author/process/edition traceability and limits. |
| Validation | Different quality/conformance expectations. | Methodological versus technical versus scientific checks. |
| Temporality | Change, history or time-dependent applicability matters. | Edition, event/observation time and longitudinal scope. |
| Spatiality | Place/context affects meaning or applicability. | Geographic reference/extent or contextual specificity as appropriate. |
| Scale | Claims differ across organisational/resolution levels. | Why a scale or level changes interpretation; no universal hierarchy. |
| Applications | Research or decision use changes requirements. | Intended use, consequence of error and limits; source access need not pass IRKB. |
| Autonomy | Considering scope or independent stewardship. | Who owns records, review, change and releases. |
| Interoperability | Cross-resource exchange is intended. | Required contracts, mappings and semantic preservation needs. |
| Overlap | Shared subjects/references/classifications exist. | Legitimate complementary perspectives versus duplicated purpose. |
| Exclusivity | A separate interpretation/authority is claimed. | What needs independent representation, not ownership of a discipline. |
| Evolution | Future extension or divergence is expected. | Change triggers, version/compatibility and revision responsibility. |
| Maintainability | Any stewardship/architecture decision. | Capacity, complexity, cost and reuse alternatives. |

The resulting narrative supports domain-owner judgement, not compulsory
classification or current decisions about EIRKB, SSKB, PBCKA, AMRKB or any other
source repository. A possible merger/split/rename remains independently scoped.
Detailed application examples and review-role escalation remain profile/boundary review
points; none are tested on live databases in this task.

## P2-C15 — Evidence limits, historical tests and deferred work

Methodological proposal, subject to the approved basis and qualifications above. The bounded historical baseline does not approve every earlier recommendation.
Original wording and source pins remain in the private evidence archive;
prototype/file claims remain reported/unverified unless actual evidence is
recovered and independently assessed. Do not invent missing packages, test IDs,
results, or a complete transcript. The twelve reported passes are not twelve
recovered executable cases; six behaviours remain examples only.

Preserve the early conceptual-method revisions as history, not current release
phases or a competing roadmap. Keep historical T1–T9, reported prototype tests,
planned T1–T14, earlier cross-database scenarios, four research assessments and
DRM–IRKB scenario separately identifiable. Methodological design evidence can
be evaluated now; technical coverage/fixtures, runtime and the full Phase 7
reconciliation are deferred. No family is silently renumbered into another.

Standards fitness/adoption, exact registries/exchange contracts, software choices
and external profiles await their roadmap phases. Preserve the approved future
Zotero bibliographic and Zenodo metadata demonstrations; do not downgrade them
to optional just because the implementation is deferred. Bidirectional Zotero
sync and automatic Zenodo publication remain outside mandatory v1.0. This task
makes no external calls or domain-source verification and issues no conformance.


## Current review boundary

Detailed applicability and claim vocabulary remain reviewable. This public edition
preserves scientific/source authority and existing proposal qualifications. It
does not open further work, adopt MSP or authorise publication.
