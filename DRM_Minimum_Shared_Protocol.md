# DRM-MSP 0.1.0 — Minimum Shared Protocol

**Status:** Unadopted review candidate, review revision 2. Public preparation
edition, 1 November 2026. Not a release, compatible patch or conformance certificate.
The protocol identity, review revision and illustrative example format are distinct.

This revision was permitted for provisional bounded documentary pilot use only.
Those two pilots were separately accepted and Phase 4 closed; the protocol has
not been generally adopted or released. Phase 5 is not authorised. This edition
adds no new methodological or technical decision.

The [methodological framework](DRM_Methodological_Architecture.md),
[decision summary](DECISIONS.md) and [roadmap](DRM_v1_Roadmap.md) explain its basis.
Original sources and requirement-by-requirement evidence remain private; the
[provenance note](PROVENANCE.md) states public reproduction limits.

## Candidate obligations versus example choices

The seven MSP subjects below remain the complete minimum-profile subject list.
“Required” describes proposed protections **if adopted in an approved scope**.
Mandatory/recommended/optional levels, justified applicability and proportionate
evidence remain as approved. Unmet applicable mandatory obligations are disclosed
limitations, not full passes. Methodological exceptions need DRM-owner review;
domain scientific acceptance and rights authority are not transferred.

JSON field names, enums and the small `msp-review-example-2` envelope are
**illustrative check contracts**, not required scientific representations.
A concise accountable manual record may discharge a methodological obligation.
No universal canonical schema, state machine, ontology, engine or standard
adoption is prescribed. The old `msp-review-example-1` contract is retained only
for explicitly labelled legacy checks; its success is not review-2 conformance.

## MSP-01 — Stable identity and scoped references

**Applicability:** Records, proposals, source editions and relationships that
need persistent reference. Preserve existing domain identifiers and non-reuse;
classification, row position and display labels must not be their sole identity.
No new universal numbering scheme or domain migration is required.

**Minimum evidence:** Identify namespace/reference scope, issued identity,
origin, relevant aliases and change history. Distinguish a scientific object,
its source-owned record, a proposal about it and an assertion about relationships.
A proposal owner or asserting authority is not automatically the referenced
entity's owner. Correction may retain the same scientific identity; a materially
different entity requires an explicit identity decision, not silent reassignment.

**Failure handling:** Duplicate scoped identities and invalid internal references
fail checks. Unresolved external targets remain explicit limitations in candidates.
A resolvable endpoint does not establish same-entity identity or semantic meaning.
The checker cannot prove historical/global non-reuse or actual equivalence.

## MSP-02 — Provenance, evidence editions and rights

**Applicability:** Documentary extraction, source assertions, transformations,
interpretations and decisions. Keep provenance and scientific verification separate
from proposal lifecycle and canonical source-record status.

**Minimum evidence:** Source locator/edition, contributor/process, evidence status,
rationale and relevant versions. An evidence edition may be a preserved file or
embedded snapshot when exact bytes/hash, edition identity, encoding and locators
are recoverable. Preserve old quotations and the edition that supported them;
never replace an old citation's hash/path/lines with an edited source silently.
Record recovery date separately from unknown original dates or transcript limits.

AMRKB's read-only reconciliation is a documentary example: an embedded 247-line
edition was recovered exactly, while a 393-line edition remained unchanged.
Extraction coverage and comparison coverage differ. See the source pins in the
change review; no AMRKB scientific corpus is copied into DRM examples.

Rights, sensitivity, permitted use and unknowns need proportionate documentation.
A manual accountable review/reference may suffice. Unknown rights restrict use;
public availability/citation is not permission. A methodological exception cannot
grant legal rights, community consent or scientific acceptance. Do not mandate
unneeded administrative fields in every scientific record.

**Failure handling:** Missing provenance/status or unresolved edition references,
wrong hashes, invalid quote slices and unsafe/unavailable example file paths fail.
Unknown rights/sensitivity and restricted use remain explicit limitations.
A permission or independently-verified label is a declaration, never authenticated
legal/scientific assurance. A single snapshot checker cannot detect coordinated
rewriting of edition IDs, hashes and content; compare retained input pins/history.

## MSP-03 — Separate lifecycles, decisions and acceptance authority

**Applicability:** Proposal intake and review, and source-owned record changes.
Maintain three independent dimensions:

| Dimension | Protection | Illustrative representation |
|---|---|---|
| Proposal lifecycle/decision | Accept documentary relevance only within stated purpose/use scope. | `state`, ordered decision history, `purpose`, review declarations. |
| Canonical source-record lifecycle | Source owns correction, retraction, reinstatement and acceptance policies. | `canonical_record` identity, source-defined lifecycle label and policy reference; no universal enum. |
| Scientific/evidence verification | Claim evidence and scientific review are independently declared. | `scientific_evidence` status/basis; verified claims need their own review evidence. |

Acceptance of a documentary proposal does **not** verify science, approve all
underlying claims, accept a canonical record, approve a relationship or grant
rights. An accepted documentary proposal can retain a source-candidate record,
unverified scientific status and a candidate relationship.

The review-2 **illustrative proposal** state machine is:

- proposed → reviewed, rejected or withdrawn;
- reviewed → proposed (rework), accepted, rejected or withdrawn;
- accepted → superseded;
- rejected, withdrawn and superseded are terminal in this example contract.

Same-state corrections are permitted only in proposed/reviewed, with a new
proposal revision, actor/date/summary and retained decision evidence. Rework
returns reviewed to proposed; neither erases earlier review. Withdrawal ends a
pending proposal at its owner's recorded request; it is not rejection, canonical
retraction or reversal of an accepted scientific record. Withdrawal after proposal
acceptance is rejected by this example contract. Reintroduction needs a new
proposal referencing the preserved earlier one. Supersession records an explicit
successor and decision; the scientific identity may remain unchanged.

Canonical correction, retraction and reinstatement remain **source-owned**.
They can use the same scientific identity with versioned reason/history under
that source's policy. An accepted-proposal edit requires a new proposal and
explicit linkage in this example, not a new scientific identity in every case.
No canonical database is edited by these candidate rules or fixtures.

**Minimum evidence:** Permitted proposal transitions, versioned history and scoped
decisions; correction/rework identifies unchanged scientific scope/identity.
Preserve prior decisions. Explicitly distinguish entity/reference scope, asserting
authority and approved-use scope. Multiple declared roles may be required:
contract stewards for structural exchange; domain authorities for semantics;
source/IRKB authors for their assertions; rights authority for permission.
A methodological exception additionally retains DRM-owner review.

The review-2 semantic-exchange example requires domain declarations for both
endpoint scopes plus a contract steward for the declared exchange use. This is
an illustrative bounded rule, not universal committee design or authenticated
appointment. Structural review cannot stand in for semantic/domain, author or
rights review. Detailed reviewer/dispute policy still needs owner approval.

**Failure handling:** Unsupported transitions, missing decisions/roles/use scopes,
changed correction identity, version/history conflicts or missing supersession
target fail. An accepted scientific-acceptance decision without separate declared
scientific review evidence fails; recording rejection does not require successful
verification. Passing checks authenticates no real authority.

## MSP-04 — Independent versions and compatibility by effect

**Applicability:** Scientific/source record, proposal, classification, schema,
profile, protocol, evidence edition and publication revisions; keep their meanings
and change histories distinct. Proposal acceptance is not a resource release.

**Minimum evidence:** Meaningful changes, actor/date/summary and relevant revision
references. `versions.record` in the examples means proposal-record revision;
canonical record versions remain source-owned. Unique event revisions and ordered
dates are checked; substantive meaningfulness needs review. Preserve prior editions,
IDs, assertions and decisions rather than fabricating a release history.

Review revision 2 changes obligations/interpretation and example semantics. It
is **not a compatible PATCH** of an adopted protocol. Format 2 is opt-in and not
automatically inferred from format 1; changed fields/transitions require explicit
conversion/review. Legacy fixtures remain valid under their original contract,
with a legacy check-scope label, not upgraded assurance. Any later adoption must
assess actual effects and choose a breaking-version path or explicit opt-in profile
for newly invalidating mandatory obligations. No automatic DRM v1.0 conformance.

**Failure handling:** Unsupported formats/revisions, missing version context,
reused event versions, backwards dates or current/history disagreement fail.
Hash agreement proves declared bytes, not correct scientific version policy.

## MSP-05 — Origin classifications and local extension stewardship

**Applicability:** Reuse, local extension, alignment and synthesis of classifications.
These are different operations; similar labels do not establish equivalent meaning.

**Minimum evidence:** Preserve origin scheme owner, definition/reference, identity
and base version; separately identify local extension steward and proposal owner.
A local extension of an externally owned scheme is allowed without claiming
ownership of that scheme. Local acceptance remains `provisional_local`; it neither
alters the origin definition/version nor approves a federation-wide scheme.
Classification assignments and history cannot silently change scientific IDs.

In format 2, the origin owner matches a declared scheme reference, the extension
steward matches the local scope, and the extension proposal owner matches the
proposal owner. These fields check declarations, not genuine ownership. Scheme
approval and scientific adequacy remain accountable domain decisions.

**Failure handling:** Missing/mismatched scheme ownership/version/definition or
local stewardship fails. An accepted local extension is not shared adoption.

## MSP-06 — Relationship claims, resolution and disagreement

**Applicability:** Structural mappings, semantic alignments, source assertions and
IRKB research interpretations; preserve typed meaning, authorship and authority.

**Minimum evidence:** Source/target scopes/IDs, relationship type/category,
provenance, rationale, versions and independent review status. Keep separate:

| Aspect | Meaning and handling |
|---|---|
| Reference resolution | A locator resolves or remains explicitly unresolved; invalid internal references are errors. External declared resolution needs an evidence locator, not a service call here. |
| Same-entity identity | A separately evidenced claim, unresolved/supported/not claimed in examples. Resolution alone is insufficient. |
| Semantic alignment | Scoped meaning correspondence assessed by domain reviewers; not automatic identity. |
| Contested meaning | Preserve disagreement, rationale and scope limits; do not silently force consensus. |

Candidate relationships can retain unresolved identity/meaning with limitations,
even inside an accepted documentary-inclusion proposal. Relationship approval is
a separate scoped declaration. In these examples an approved relationship needs
an accepted proposal, resolved endpoints and appropriate declared roles. An identity
claim cannot be approved while its identity is unresolved; semantic alignment
cannot be approved with contested/unassessed meaning. Other uncontroversial uses
may be separately proposed without approving that disputed claim. Confidence,
functional relevance and resolvable IDs do not establish equivalence.

**Failure handling:** Missing endpoints/type, invalid internal target, unresolved
approved endpoint, blocked identity/meaning approval, incorrect approval purpose
or missing scoped roles fail. Candidate disputes/unresolved external identities
remain visible. No identity-resolution service or universal relationship ontology
is implemented. Source assertions and IRKB interpretations retain their owners.

## MSP-07 — Bounded validation and preservation crosswalks

**Applicability:** Candidate examples/template and any later scoped evidence claim.
Record exact inputs, versions, invocation, expected outcomes, errors and limits.
Keep methodological conformance, technical checks and scientific validity separate.

**Minimum evidence:** [Checker](tools/validate_msp.py), bounded
[review-2 additions](tools/msp_review_v2.py),
[example guide](examples/msp/README.md) and fixture oracles provide repeatable
synthetic checks. Exit 0 means no detected structural error, possibly with
limitations; exit 1 means structural rejection; exit 2 means input/JSON error.
None is adoption, scientific truth, genuine authority or legal permission.
Old T1–T9, reported twelve-test prototype and planned T1–T14 stay distinct;
these checks do not reproduce that prototype or complete Phase 7.

Local adapters are **preservation crosswalks**, not wholesale transformations of
scientific records into proposal JSON. A later authorised adapter must disclose
input edition/hash, source-ID correspondence, source meanings/counts/statuses,
unknown values, transformations, omitted information, outputs and limits.
Do not turn missing into absent, relevance into acceptance, or a source into its
provider/dataset automatically. A concise manual crosswalk can be appropriate.
Actual AMRKB/OSDS adapters, copies/pilot records and operational registers are
not created here; scope, rights and preservation tests need later approval.

**Failure handling:** Lost IDs/meanings/counts/statuses/unknowns or undisclosed
omissions prevent a preservation claim. No source adapter is exercised by a
successful synthetic-envelope check. The checker cannot judge scientific content,
evidence authenticity, historical completeness or actual permission.

## Development Register template and review-format boundary

The [template](templates/development_register.template.json) remains explicitly
synthetic and unpopulated (`proposals: []`). Its proposal/decision shapes are
examples for later authorised local adaptation, not operational approvals.
Five proposal types remain: proposed records, classification extensions,
methodological changes, relationships and schema changes. Refer to authoritative
material; do not duplicate scientific catalogues. The template's unknown rights
and sensitivity are limitations, not implied permission.

Review-2 required example fields demonstrate these protections and deliberately
reject incomplete format-2 examples. They are not a mandate to add every field to
all canonical records. Manual/profile alternatives require accountable evidence.
The example checker has no ingestion, scientific acceptance or publication role.


## Public methodological traceability

| MSP subject | Methodological clauses |
|---|---|
| MSP-01 identity | P2-C09 |
| MSP-02 provenance/evidence/rights | P2-C08, P2-C13 |
| MSP-03 lifecycle/authority | P2-C04, P2-C06, P2-C08 |
| MSP-04 versions | P2-C11 |
| MSP-05 classification stewardship | P2-C03, P2-C12 |
| MSP-06 relationships | P2-C06, P2-C07 |
| MSP-07 bounded checks | P2-C04, P2-C05, P2-C15 |

These locators refer to the public methodological document; they do not reproduce
private source quotations or claim all detailed proposals have been adopted.

## Review and development boundary

The bounded Phase 4 review is closed. Proposed clarifications remain proposals;
rights, scientific evidence and real identity limits remain explicit. No further
pilot, source update, general MSP adoption/release or Phase 5 is authorised.
